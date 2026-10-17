import { QuartzConfig } from "./quartz/cfg"
import * as Plugin from "./quartz/plugins"
import { ActiveChronolog } from "./_scripts/publication_filter"
import { ChronologFeed } from "./_scripts/feed"
import ChronologFolderContent from "./_scripts/folder_content"

const config: QuartzConfig = {
  configuration: {
    pageTitle: "ChronoLog",
    enableSPA: true,
    enablePopovers: true,
    analytics: null,
    locale: "en-US",
    baseUrl: process.env.CHRONOLOG_BASE_URL ?? "localhost:8080",
    ignorePatterns: [
      "private",
      "templates",
      ".obsidian",
      "_pipeline",
      "_scripts",
      "_review",
      "_inputs",
      ".github",
      "docs",
      "tests",
      "content",
      "README.md",
      "node_modules",
      "quartz",
    ],
    defaultDateType: "modified",
    theme: {
      cdnCaching: true,
      typography: {
        header: "Inter",
        body: "Inter",
        code: "JetBrains Mono",
      },
      colors: {
        lightMode: {
          light: "#f8f7f2",
          lightgray: "#dedbd2",
          gray: "#6c6a63",
          darkgray: "#34332f",
          dark: "#171714",
          // 5.4:1 on `light` (WCAG AA body text needs 4.5:1).
          secondary: "#8a5c12",
          tertiary: "#3f6f6b",
          highlight: "rgba(155, 106, 25, 0.15)",
          textHighlight: "#fff0bd",
        },
        darkMode: {
          light: "#171714",
          lightgray: "#34332f",
          gray: "#9d9a90",
          darkgray: "#dedbd2",
          dark: "#f8f7f2",
          secondary: "#d49a36",
          tertiary: "#74aaa4",
          highlight: "rgba(212, 154, 54, 0.2)",
          textHighlight: "#5a4314",
        },
      },
    },
  },
  plugins: {
    transformers: [
      Plugin.FrontMatter(),
      Plugin.CreatedModifiedDate({ priority: ["frontmatter", "filesystem"] }),
      Plugin.SyntaxHighlighting(),
      // Source quotes can contain #Heading fragments; taxonomy comes from frontmatter.
      Plugin.ObsidianFlavoredMarkdown({ enableInHtmlEmbed: false, parseTags: false }),
      Plugin.GitHubFlavoredMarkdown(),
      Plugin.TableOfContents(),
      Plugin.CrawlLinks({ markdownLinkResolution: "shortest", prettyLinks: false }),
      Plugin.Description(),
    ],
    filters: [Plugin.RemoveDrafts(), ActiveChronolog()],
    emitters: [
      Plugin.AliasRedirects(),
      Plugin.ComponentResources(),
      Plugin.ContentPage(),
      // Archive/index.md lists the months itself; other folders keep the page list.
      Plugin.FolderPage({ pageBody: ChronologFolderContent() }),
      Plugin.TagPage(),
      // The feed is ChronologFeed (cards and releases only), not the stock all-pages RSS.
      Plugin.ContentIndex({ enableSiteMap: true, enableRSS: false }),
      ChronologFeed(),
      Plugin.Assets(),
      Plugin.Static(),
      Plugin.Favicon(),
      Plugin.NotFoundPage(),
    ],
  },
}

export default config
