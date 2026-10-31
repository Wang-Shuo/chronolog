from pathlib import Path
import json
import re

import pytest


def test_quartz_files_define_build_command():
    package = json.loads(Path("package.json").read_text())
    assert package["scripts"]["build"] == "quartz build"
    assert "quartz" in package["dependencies"]
    assert Path("quartz.config.ts").exists()


def test_quartz_mirror_is_ignored_because_vault_root_is_the_source_of_truth():
    ignored = Path(".gitignore").read_text(encoding="utf-8").splitlines()
    wrapper = Path("_scripts/quartz_build_wrapper.mjs").read_text(encoding="utf-8")
    config = Path("quartz.config.ts").read_text(encoding="utf-8")

    assert "content/" in ignored
    assert 'args.splice(1, 0, "--directory", ".")' in wrapper
    assert 'path.join(root, "quartz", "bootstrap-cli.mjs")' in wrapper
    assert '"content"' in config


LAYOUT = Path("quartz.layout.ts")
CONFIG = Path("quartz.config.ts")


def contrast(foreground: str, background: str) -> float:
    """WCAG 2.x contrast ratio of two #rrggbb colours."""
    def luminance(colour: str) -> float:
        channels = [int(colour.lstrip("#")[i:i + 2], 16) / 255 for i in (0, 2, 4)]
        linear = [c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4 for c in channels]
        return 0.2126 * linear[0] + 0.7152 * linear[1] + 0.0722 * linear[2]
    high, low = sorted((luminance(foreground), luminance(background)), reverse=True)
    return (high + 0.05) / (low + 0.05)


def theme_colours(mode: str) -> dict[str, str]:
    block = re.search(rf"{mode}: \{{(.*?)\}}", CONFIG.read_text(encoding="utf-8"), re.S).group(1)
    return dict(re.findall(r'(\w+): "(#[0-9a-fA-F]{6})"', block))


def test_contrast_matches_wcag_reference_values():
    assert contrast("#000000", "#ffffff") == pytest.approx(21)
    assert contrast("#9b6a19", "#f8f7f2") == pytest.approx(4.38, abs=0.01)


@pytest.mark.parametrize("mode", ["lightMode", "darkMode"])
def test_link_colour_meets_wcag_aa_body_text_contrast(mode):
    colours = theme_colours(mode)
    assert contrast(colours["secondary"], colours["light"]) >= 4.5


def test_explorer_hides_card_release_and_alert_folders_and_opens_by_default():
    layout = LAYOUT.read_text(encoding="utf-8")
    assert 'folderDefaultState: "open"' in layout
    match = re.search(r"filterFn: \(node\) => !\[(.*?)\]\.includes\(node\.slugSegment\)", layout)
    assert match
    assert {"tags", "Changes", "Releases", "Alerts"} == set(re.findall(r'"([^"]+)"', match.group(1)))


def test_explorer_sorts_folders_in_reading_order_and_months_newest_first():
    layout = LAYOUT.read_text(encoding="utf-8")
    sort_fn = re.search(r"\n    sortFn: (\(a, b\) => \{.*?\n    \}),\n", layout, re.S).group(1)
    assert 'const folders = ["Products", "Themes", "Archive"]' in sort_fn
    assert "b.slugSegment.localeCompare(a.slugSegment)" in sort_fn
    # Serialized with toString(): an inner function would be wrapped in the build's
    # __name helper, which does not exist in the browser and empties the Explorer.
    assert sort_fn.count("=>") == 1 and "function" not in sort_fn


def test_graph_renders_only_on_card_pages():
    layout = LAYOUT.read_text(encoding="utf-8")
    assert layout.count("Component.Graph(") == 1
    conditional = re.search(r"Component\.ConditionalRender\(\{(.*?)\n\}\)", layout, re.S).group(1)
    assert "component: Component.Graph()" in conditional
    assert '.startsWith("Changes/")' in conditional and "Themes/" not in conditional
    assert "Component.TableOfContents()" in layout and "Component.Backlinks()" in layout


def test_content_meta_hides_reading_time_and_title_has_a_tagline():
    layout = LAYOUT.read_text(encoding="utf-8")
    calls = re.findall(r"Component\.ContentMeta\(([^)]*)\)", layout)
    assert calls and all(call == "{ showReadingTime: false }" for call in calls)
    assert "Component.PageTitle()" not in layout and layout.count("SiteTitle()") == 2
    title = Path("_scripts/site_title.tsx").read_text(encoding="utf-8")
    assert '<p class="site-tagline">' in title and 'class="page-title"' in title
    assert "Tracked changes in ChatGPT, Claude Code and Cursor" in title
    for rule in (".global-graph-icon", "--product-chatgpt", "--product-claude-code",
                 "--product-cursor", ".site-tagline"):
        assert rule in title


def test_footer_links_the_repository_about_page_and_feed():
    layout = LAYOUT.read_text(encoding="utf-8")
    assert 'https://github.com"' not in layout
    assert 'GitHub: "https://github.com/Wang-Shuo/chronolog"' in layout
    assert "About: `${siteUrl}/About`" in layout and "RSS: `${siteUrl}/index.xml`" in layout
    assert 'process.env.CHRONOLOG_BASE_URL ?? "localhost:8080"' in layout


def test_rss_is_a_custom_feed_of_cards_and_releases():
    config = CONFIG.read_text(encoding="utf-8")
    assert "Plugin.ContentIndex({ enableSiteMap: true, enableRSS: false })" in config
    assert config.index("ChronologFeed()") > config.index("Plugin.ContentIndex(")
    feed = Path("_scripts/feed.tsx").read_text(encoding="utf-8")
    assert 'FEED_SECTIONS = ["Changes/", "Releases/"]' in feed and "FEED_LIMIT = 30" in feed
    assert ('"Tracked changes in ChatGPT, Claude Code and Cursor, from official release notes"'
            in feed)
    assert 'rel="alternate"' in feed and 'type="application/rss+xml"' in feed


def test_archive_folder_page_shows_its_folder_note_without_a_second_page_list():
    config = CONFIG.read_text(encoding="utf-8")
    assert "Plugin.FolderPage({ pageBody: ChronologFolderContent() })" in config
    assert 'import ChronologFolderContent from "./_scripts/folder_content"' in config
    component = Path("_scripts/folder_content.tsx").read_text(encoding="utf-8")
    # Only the archive's folder note (tagged "archive") drops the automatic page list.
    assert 'if (!tags.includes("archive")) {\n      return <Listing {...props} />' in component
    assert "htmlToJsx(props.fileData.filePath!, props.tree)" in component
    # The Archive folder stays visible in the Explorer.
    match = re.search(r"filterFn: \(node\) => !\[(.*?)\]\.includes\(node\.slugSegment\)",
                      LAYOUT.read_text(encoding="utf-8"))
    assert "Archive" not in match.group(1)


def test_quotes_render_verbatim_and_static_assets_ignore_gitignore():
    config = CONFIG.read_text(encoding="utf-8")
    # SmartyPants would turn `--flag` in quoted source text into `—flag`.
    assert "Plugin.GitHubFlavoredMarkdown({ enableSmartyPants: false })" in config
    # quartz/ is git-ignored, so Quartz's own Static emitter published no icon or image.
    assert "Plugin.Static()" not in config and "ChronologStatic()," in config
    emitter = Path("_scripts/static_assets.ts").read_text(encoding="utf-8")
    assert 'globby("**", { cwd: staticPath })' in emitter and "gitignore" not in emitter.split("export")[1]
    setup = Path("_scripts/setup_quartz.mjs").read_text(encoding="utf-8")
    assert 'for (const name of ["icon.png", "og-image.png"])' in setup
    for name in ("icon.png", "og-image.png"):
        assert (Path("_scripts/brand") / name).stat().st_size > 1000


def test_analytics_is_off_unless_the_deploy_sets_a_goatcounter_code():
    config = CONFIG.read_text(encoding="utf-8")
    assert "const goatcounter = process.env.CHRONOLOG_GOATCOUNTER_CODE" in config
    assert 'analytics: goatcounter ? { provider: "goatcounter", websiteId: goatcounter } : null,' in config
    deploy = Path(".github/workflows/deploy.yml").read_text(encoding="utf-8")
    assert "CHRONOLOG_GOATCOUNTER_CODE: ${{ vars.CHRONOLOG_GOATCOUNTER_CODE }}" in deploy
