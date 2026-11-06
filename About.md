---
created: '2022-12-15'
date: '2026-11-06'
description: Where ChronoLog's data comes from, how official release notes become
  reviewed Change Cards, what is grouped or skipped, and how to report a problem.
machine_hash: 3a991390d842cddaafcbbeb41e7f73b49bebbc3d12006ea9a0b98ebbf8545b7d
modified: '2026-11-06'
publication: active
tags:
- about
title: About the data
---

# About the data

<!-- chronolog:begin region="intro" -->
ChronoLog tracks announced changes in ten products: Aider, ChatGPT, Claude Code, Cline, Codex CLI, Cursor, Gemini CLI, GitHub Copilot CLI, OpenHands and Windsurf. It reads official release notes only, turns each release into dated Change Cards and groups them by theme. Every record is reviewed before it is published.
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

### OpenHands
- Official source: [OpenHands GitHub releases](https://github.com/OpenHands/OpenHands/releases)
- Archived releases: 137, dated 2024-06-04 → 2026-11-05
- Last successful fetch: 2026-11-06T10:46:32Z.
- Known gaps: Stable versioned releases of the OpenHands application available from its current repository. SDK releases, preview builds and temporary PR evidence uploads are excluded; endpoint coverage does not establish the product's launch date.

### Windsurf
- Official source: [Windsurf changelog](https://docs.devin.ai/desktop/changelog)
- Archived releases: 121, dated 2025-04-02 → 2026-10-30
- Last successful fetch: 2026-11-06T10:43:34Z.
- Known gaps: Windsurf's official changelog now continues as Devin Desktop. Only the stable desktop changelog is tracked, from the earliest entry still on the page; Next previews, Windsurf plugins and Devin Cloud have separate histories.
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
10 products · 1,998 archived releases · 7,829 tracked changes · 25 themes. Pending theme review: 111. Silence alerts: 1. Every generated batch is reviewed in a pull request before it is published.
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