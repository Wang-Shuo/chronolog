---
created: '2018-07-09'
date: '2026-11-06'
description: Where ChronoLog's data comes from, how official release notes become
  reviewed Change Cards, what is grouped or skipped, and how to report a problem.
machine_hash: 7de2056d7b68ed28e4fd27bc225e8dd6aa50e22faa85c3fdc1141537fa386156
modified: '2026-11-06'
publication: active
tags:
- about
title: About the data
---

# About the data

<!-- chronolog:begin region="intro" -->
ChronoLog tracks announced changes in 37 products: Aider, ChatGPT, Claude, Claude Code, Cline, Codex CLI, Cursor, DeepSeek API, Descript, Dify, ElevenLabs, Gamma, Gemini, Gemini CLI, GitHub Copilot CLI, Google Antigravity, Granola, HeyGen, Kimi Code, Lovable, Manus, Microsoft 365 Copilot, Midjourney, Notion, Ollama, Open WebUI, OpenClaw, OpenCode, OpenHands, Qoder, Replit, Runway, Suno, Synthesia, Windsurf, Z.ai API and v0. It reads official release notes only, turns each release into dated Change Cards and groups them by theme. Every record is reviewed before it is published.
<!-- chronolog:end -->

## Sources and coverage
<!-- chronolog:begin region="sources" -->
### Aider
- Official source: [Aider GitHub releases](https://github.com/Aider-AI/aider/releases)
- Archived releases: 93, dated 2023-06-07 → 2025-08-09
- Last successful fetch: 2026-11-06T10:43:30Z.
- Known gaps: Stable versioned GitHub releases only; preview builds and unannounced changes are excluded. The latest upstream release may be older than the last successful fetch.

### ChatGPT
- Official source: [ChatGPT release notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)
- Archived releases: 304, dated 2022-12-15 → 2026-10-30
- Official browser snapshot captured: 2026-10-31T04:08:55Z. Imported snapshot; this is not a successful automatic HTTP fetch.
- Known gaps: Official changelog entries only; Codex-only entries excluded. Rollout dates are not universal availability dates.

### Claude
- Official source: [Claude release notes](https://support.claude.com/en/articles/12138966-release-notes)
- Archived releases: 63, dated 2025-08-01 → 2026-11-05
- Last successful fetch: 2026-11-06T13:12:59Z.
- Known gaps: The dated entries currently available in the official Claude app release notes, including model and plan announcements listed there. This endpoint currently starts in August 2025; it is not Claude's launch date. Claude Code has a separate history.

### Claude Code
- Official source: [Claude Code GitHub releases](https://github.com/anthropics/claude-code/releases)
- Archived releases: 257, dated 2025-12-19 → 2026-10-31
- Last successful fetch: 2026-10-31T04:08:35Z.
- Known gaps: GitHub Releases starts at v2.0.73 on 2025-12-19. Official CHANGELOG.md contains 0.2.x–2.0.72 history without publication dates; not imported.

### Cline
- Official source: [Cline GitHub releases](https://github.com/cline/cline/releases)
- Archived releases: 297, dated 2024-07-28 → 2026-10-26
- Last successful fetch: 2026-11-06T10:43:29Z.
- Known gaps: Stable versioned Cline application releases only; separately tagged SDK and CLI packages and preview builds are excluded.

### Codex CLI
- Official source: [Codex CLI GitHub releases](https://github.com/openai/codex/releases)
- Archived releases: 179, dated 2025-06-30 → 2026-11-06
- Last successful fetch: 2026-11-06T10:49:11Z.
- Known gaps: Stable versioned Codex CLI releases only; alpha builds, SDK-only releases, the Codex app and cloud-only announcements are outside this source's scope.

### Cursor
- Official source: [Cursor changelog](https://cursor.com/changelog)
- Archived releases: 257, dated 2023-03-14 → 2026-10-20
- Last successful fetch: 2026-10-31T04:08:46Z.
- Known gaps: Official paginated changelog only; unannounced changes are outside scope.

### DeepSeek API
- Official source: [DeepSeek API release notes](https://api-docs.deepseek.com/updates/)
- Archived releases: 22, dated 2024-05-17 → 2026-10-17
- Last successful fetch: 2026-11-06T13:13:00Z.
- Known gaps: The official DeepSeek API change log, including model availability, API behavior and pricing. Web and mobile changes appear only when explicitly included in the API announcement; this is not a complete consumer-app history. Benchmark tables and code examples are excluded.

### Descript
- Official source: [Descript changelog](https://feedback.descript.com/changelog)
- Archived releases: 534, dated 2018-07-07 → 2026-11-06
- Last successful fetch: 2026-11-07T03:46:29Z.
- Known gaps: Published entries across all three official Canny update types (new, improved and fixed), including AI editing, transcription and the wider video/audio editor. Each type archive is traversed to its terminal page and overlaps are deduplicated. Posts with an empty or media-only body retain their official title only; media contents are not transcribed. Drafts and deleted entries are excluded.

### Dify
- Official source: [Dify GitHub releases](https://github.com/langgenius/dify/releases)
- Archived releases: 154, dated 2023-05-15 → 2026-11-04
- Last successful fetch: 2026-11-06T13:13:44Z.
- Known gaps: Stable versioned releases of Dify's open-source platform. Cloud-only changes, separately versioned plugins and prereleases have separate histories.

### ElevenLabs
- Official source: [ElevenLabs changelog](https://elevenlabs.io/docs/changelog)
- Archived releases: 103, dated 2024-10-13 → 2026-11-02
- Last successful fetch: 2026-11-06T13:13:19Z.
- Known gaps: Every dated entry listed in the official changelog index, including voice, audio, agent and API updates. The default Markdown page contains only a recent window, so collection traverses the complete index. Documentation widgets and code examples are excluded.

### Gamma
- Official source: [Gamma changelog](https://ideas.gamma.app/changelog)
- Archived releases: 78, dated 2024-02-14 → 2026-10-26
- Last successful fetch: 2026-11-07T02:10:29Z.
- Known gaps: All published entries returned by the official public changelog, traversing every cumulative page. Drafts, deleted entries and private feedback are excluded.

### Gemini
- Official source: [Gemini release notes](https://gemini.google/us/release-notes/?hl=en)
- Archived releases: 96, dated 2023-04-10 → 2026-10-13
- Last successful fetch: 2026-11-06T13:13:00Z.
- Known gaps: English US Gemini Apps release notes available from the official page, including its historical Bard entries. Regional availability can differ. Gemini CLI and the developer API have separate release histories.

### Gemini CLI
- Official source: [Gemini CLI GitHub releases](https://github.com/google-gemini/gemini-cli/releases)
- Archived releases: 160, dated 2025-06-28 → 2026-11-04
- Last successful fetch: 2026-11-06T10:43:33Z.
- Known gaps: Stable versioned Gemini CLI releases only; nightly and preview builds are excluded. This is not the Gemini consumer app or the Gemini API changelog.

### GitHub Copilot CLI
- Official source: [GitHub Copilot CLI GitHub releases](https://github.com/github/copilot-cli/releases)
- Archived releases: 193, dated 2025-09-26 → 2026-11-06
- Last successful fetch: 2026-11-06T10:43:36Z.
- Known gaps: Stable versioned GitHub Copilot CLI releases only; prereleases are excluded. Copilot's IDE, web and other product surfaces have separate release histories.

### Google Antigravity
- Official source: [Google Antigravity changelog](https://antigravity.google/docs/changelog)
- Archived releases: 70, dated 2025-11-18 → 2026-11-03
- Last successful fetch: 2026-11-07T02:10:32Z.
- Known gaps: Dated versions of the Antigravity App (hub) and original IDE on the official changelog. Separately versioned CLI, SDK, editor extensions and undated model-launch cards are outside this scope.

### Granola
- Official source: [Granola release notes](https://www.granola.ai/updates)
- Archived releases: 25, dated 2024-05-22 → 2026-09-02
- Last successful fetch: 2026-11-07T02:10:29Z.
- Known gaps: Dated announcement summaries on the official updates index, including launch and company announcements listed there. Full blog article text and unlisted maintenance changes are outside this source's scope.

### HeyGen
- Official source: [HeyGen release notes](https://heygen.noticeable.news/)
- Archived releases: 47, dated 2025-11-29 → 2026-10-28
- Last successful fetch: 2026-11-07T03:37:41Z.
- Known gaps: All dated public updates in the official HeyGen Noticeable archive, including video, avatar, voice and API updates. Publication timestamps are checked against each linked article; company or plan announcements may appear alongside features.

### Kimi Code
- Official source: [Kimi Code GitHub releases](https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md)
- Archived releases: 91, dated 2026-05-26 → 2026-11-06
- Last successful fetch: 2026-11-07T03:37:49Z.
- Known gaps: Dated stable versions in the official English Kimi Code changelog, covering CLI and Web UI changes listed there. Unreleased sections are excluded. The Kimi consumer app and model API have separate histories; the earliest entry here is not their launch date.

### Lovable
- Official source: [Lovable changelog](https://docs.lovable.dev/changelog)
- Archived releases: 156, dated 2024-12-03 → 2026-11-04
- Last successful fetch: 2026-11-06T13:13:19Z.
- Known gaps: Dated entries available in Lovable's official product changelog. Undated help articles, hosting widgets and code examples are excluded; endpoint coverage is not proof of lifetime coverage.

### Manus
- Official source: [Manus release notes](https://www.manus.im/updates)
- Archived releases: 35, dated 2025-05-11 → 2026-09-29
- Last successful fetch: 2026-11-07T02:13:16Z.
- Known gaps: All updates exposed by the official public Updates page's notification feed. Entries use the feed's publication timestamp; entries without a public blog permalink link to the Updates index. Private account notifications are outside coverage.

### Microsoft 365 Copilot
- Official source: [Microsoft 365 Copilot release notes](https://learn.microsoft.com/en-us/microsoft-365/copilot/release-notes)
- Archived releases: 21, dated 2026-01-13 → 2026-11-04
- Last successful fetch: 2026-11-07T03:37:50Z.
- Known gaps: The official Microsoft Learn all-features tab for Microsoft 365 Copilot, currently covering 2026. App-scoped feature titles and their first change summaries are retained; platform tabs duplicate the same releases and are excluded, as are nested setup instructions and impact boilerplate. Dates label release batches; availability rolls out gradually. This does not cover the separate consumer Copilot app.

### Midjourney
- Official source: [Midjourney release notes](https://updates.midjourney.com/)
- Archived releases: 96, dated 2024-03-07 → 2026-10-08
- Last successful fetch: 2026-11-07T02:10:18Z.
- Known gaps: Posts listed in the official updates sitemap, including alpha tests and community announcements. Dates are article publication dates, not sitemap modification dates or dates mentioned in titles; older Discord-only announcements are outside coverage.

### Notion
- Official source: [Notion release notes](https://www.notion.com/releases)
- Archived releases: 154, dated 2020-01-09 → 2026-10-19
- Last successful fetch: 2026-11-07T03:38:04Z.
- Known gaps: Every dated release in the official paginated Notion archive, including Notion AI, agents and the wider workspace product. This is not an AI-only history. Explicit coming-soon blocks remain in source records but are excluded from shipped-change cards; video-player controls and error messages are removed.

### Ollama
- Official source: [Ollama GitHub releases](https://github.com/ollama/ollama/releases)
- Archived releases: 266, dated 2023-07-08 → 2026-11-03
- Last successful fetch: 2026-11-06T13:13:38Z.
- Known gaps: Stable versioned releases of the Ollama application and runtime. Prereleases and model-library updates without a corresponding application release are excluded.

### Open WebUI
- Official source: [Open WebUI GitHub releases](https://github.com/open-webui/open-webui/releases)
- Archived releases: 178, dated 2024-02-23 → 2026-11-03
- Last successful fetch: 2026-11-06T13:13:51Z.
- Known gaps: Stable versioned Open WebUI releases from the official repository. Development builds, prereleases and external model-provider updates are excluded.

### OpenClaw
- Official source: [OpenClaw release notes](https://docs.openclaw.ai/releases)
- Archived releases: 24, dated 2026-06-30 → 2026-11-05
- Last successful fetch: 2026-11-07T02:13:27Z.
- Known gaps: Curated release summaries linked from the official documentation release index, dated using published_at of the matching stable GitHub tag. Calendar-looking version numbers are not dates. Older technical changelog records and prereleases outside this index are excluded.

### OpenCode
- Official source: [OpenCode changelog](https://opencode.ai/changelog)
- Archived releases: 201, dated 2025-12-19 → 2026-11-06
- Last successful fetch: 2026-11-07T02:13:51Z.
- Known gaps: Every version currently listed in the paginated official product changelog, including CLI and app changes. GitHub tags not listed in this curated endpoint are outside coverage.

### OpenHands
- Official source: [OpenHands GitHub releases](https://github.com/OpenHands/OpenHands/releases)
- Archived releases: 137, dated 2024-06-04 → 2026-11-05
- Last successful fetch: 2026-11-06T10:46:32Z.
- Known gaps: Stable versioned releases of the OpenHands application available from its current repository. SDK releases, preview builds and temporary PR evidence uploads are excluded; endpoint coverage does not establish the product's launch date.

### Qoder
- Official source: [Qoder changelog](https://changelog.qoder.com/app)
- Archived releases: 26, dated 2026-08-27 → 2026-11-06
- Last successful fetch: 2026-11-07T03:37:49Z.
- Known gaps: The current unified Qoder app changelog, beginning with the earliest dated version on the official page. Qoder IDE, CLI and the older QoderWork changelogs are separate surfaces and are not combined or counted twice.

### Replit
- Official source: [Replit release notes](https://docs.replit.com/updates)
- Archived releases: 99, dated 2024-12-13 → 2026-10-30
- Last successful fetch: 2026-11-06T13:15:09Z.
- Known gaps: Dated weekly Replit changelog pages listed in the official sitemap, covering Agent and related development-platform features. This includes non-AI platform changes announced alongside Agent. Unindexed historical announcements are outside this source's scope.

### Runway
- Official source: [Runway changelog](https://runway.com/changelog)
- Archived releases: 161, dated 2024-01-08 → 2026-10-27
- Last successful fetch: 2026-11-07T02:10:02Z.
- Known gaps: All dated descriptions currently available on the official changelog. Multiple announcements on one date remain separate; the source does not provide individual entry permalinks.

### Suno
- Official source: [Suno release notes](https://suno.com/release-notes)
- Archived releases: 76, dated 2023-12-23 → 2026-11-06
- Last successful fetch: 2026-11-07T02:10:01Z.
- Known gaps: All dated entries currently published on the official release-notes index, including mobile, Studio and model announcements. Earlier changes absent from this endpoint are outside coverage.

### Synthesia
- Official source: [Synthesia release notes](https://www.synthesia.io/updates)
- Archived releases: 202, dated 2020-10-13 → 2026-10-27
- Last successful fetch: 2026-11-07T03:37:48Z.
- Known gaps: Dated summaries across every page of the official product-update index. Separate featured hero announcements without publication dates and full linked article bodies are excluded. This is the currently available dated index, not a lifetime release history.

### Windsurf
- Official source: [Windsurf changelog](https://docs.devin.ai/desktop/changelog)
- Archived releases: 121, dated 2025-04-02 → 2026-10-30
- Last successful fetch: 2026-11-06T10:43:34Z.
- Known gaps: Windsurf's official changelog now continues as Devin Desktop. Only the stable desktop changelog is tracked, from the earliest entry still on the page; Next previews, Windsurf plugins and Devin Cloud have separate histories.

### Z.ai API
- Official source: [Z.ai API release notes](https://docs.z.ai/release-notes/new-released)
- Archived releases: 8, dated 2025-09-30 → 2026-08-26
- Last successful fetch: 2026-11-07T03:38:05Z.
- Known gaps: All dated model announcements currently listed in the official Z.ai New Released notes. This is a model/API announcement history, not a complete consumer-chat or platform history. Performance statements are upstream claims, not independently verified benchmark results.

### v0
- Official source: [v0 changelog](https://v0.app/changelog)
- Archived releases: 92, dated 2025-10-01 → 2026-10-19
- Last successful fetch: 2026-11-06T13:13:20Z.
- Known gaps: Dated v0 product announcements available on the official changelog. This does not include the wider Vercel platform's changelog or undated documentation updates.
<!-- chronolog:end -->

## How cards are made
<!-- chronolog:begin region="method" -->
- Each archived release is read as headings, paragraphs and list items.
- Version-only lines, availability notes, instructions and unclassified bug-fix lines are skipped.
- A feature heading and the text under it become one Change Card, titled by the heading.
- Consecutive paragraphs about one theme become one card. When a release yields a single card, the card takes the release title.
- Items under a platform or plan heading (such as Web, iOS or Plus) and lists of up to eight items become one card each.
- Longer lists, lists under headings such as "What's changed" or "Bug fixes", and GitHub release notes are read item by item. Items that announce something on their own ("Introducing …", a new slash command, a feature now on by default) stay separate cards; the other items of one theme are listed together on one digest card per release.
- Every card has one theme from a fixed vocabulary and a kind: launch, expansion, pricing, policy, fix, digest or change.
- Lines without a confident theme are published in an "Other changes" digest of their release and do not appear on theme pages or the home page; prose without a theme waits in a review queue. Each release page shows "Tracked N cards from M candidate lines" and how many lines wait for review.
- Dates are announcement dates, not availability dates.
- Cadence is measured to the newest archived release date, not the clock.
- Relations between cards are same-theme chronology only; they never claim adoption or causation.
<!-- chronolog:end -->

## Review status
<!-- chronolog:begin region="status" -->
37 products · 5,076 archived releases · 18,201 tracked changes · 29 themes. Pending theme review: 2,229. Silence alerts: 1. Every generated batch is reviewed in a pull request before it is published.
<!-- chronolog:end -->

## Glossary
<!-- chronolog:begin region="glossary" -->
- **Change Card**: one announced change that can be understood on its own, taken from an official release, with a date, one theme, a kind and the quoted source text.
- **Digest card**: the smaller changes of one theme in one release, quoted together on one card.
- **Other changes**: the list items of one release without a confident theme, quoted together on one digest card (a single item keeps its own card); listed on release and product pages, not on theme pages or the home page.
- **Release**: one archived entry of an official changelog or release page; its page lists the cards tracked from it.
- **Theme**: a category from a fixed vocabulary that groups cards across products.
- **Era**: a reviewed phase of one product's history, bounded by cited releases.
- **Key moments**: on a theme page, the cards an editor selected; until then up to 12 per product are chosen automatically from launches and standalone announcements, one per quarter first and never two from one release.
- **Cadence**: releases per month on a product page. *Quiet* means each of the last two months had fewer than half the product's average monthly releases; *silent* means no release in the last two months, which also raises a silence alert.
- **Tracked products only**: comparisons and "earliest" statements cover only the tracked products, not the wider market.
- **Candidate line**: a line of release text that could become part of a card; Markdown headings, code samples and very short lines are not counted. "Tracked N cards from M candidate lines" compares the cards kept with these lines.
<!-- chronolog:end -->

## Feedback
<!-- chronolog:begin region="feedback" -->
Every card ends with a link that opens a prefilled issue. For anything else, open an issue at [https://github.com/Wang-Shuo/chronolog/issues](https://github.com/Wang-Shuo/chronolog/issues).
<!-- chronolog:end -->