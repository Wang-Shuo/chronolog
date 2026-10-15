---
created: '2022-12-15'
date: '2026-10-14'
description: Where ChronoLog's data comes from, how official release notes become
  reviewed Change Cards, what is sampled or skipped, and how to report a problem.
machine_hash: 527397a8086471764f34340de1a7b78bb3c197776bd587efedb378f1d3692dba
modified: '2026-10-14'
publication: active
tags:
- about
title: About the data
---

# About the data

<!-- chronolog:begin region="intro" -->
ChronoLog tracks announced changes in three products: ChatGPT, Claude Code and Cursor. It reads official release notes only, turns each release into dated Change Cards and groups them by theme. Every record is reviewed before it is published.
<!-- chronolog:end -->

## Sources and coverage
<!-- chronolog:begin region="sources" -->
### ChatGPT
- Official source: [ChatGPT release notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)
- Archived releases: 292, dated 2022-12-15 → 2026-10-07
- Official browser snapshot captured: 2026-10-14T23:26:11+0800. Imported snapshot; this is not a successful automatic HTTP fetch.
- Known gaps: Official changelog entries only; Codex-only entries excluded. Rollout dates are not universal availability dates.

### Claude Code
- Official source: [Claude Code GitHub releases](https://github.com/anthropics/claude-code/releases)
- Archived releases: 243, dated 2025-12-19 → 2026-10-14
- Last successful fetch: 2026-10-15T01:55:15Z.
- Known gaps: GitHub Releases starts at v2.0.73 on 2025-12-19. Official CHANGELOG.md contains 0.2.x–2.0.72 history without publication dates; not imported.

### Cursor
- Official source: [Cursor changelog](https://cursor.com/changelog)
- Archived releases: 255, dated 2023-03-14 → 2026-10-13
- Last successful fetch: 2026-10-15T01:55:30Z.
- Known gaps: Official paginated changelog only; unannounced changes are outside scope.
<!-- chronolog:end -->

## How cards are made
<!-- chronolog:begin region="method" -->
- Each archived release is split into lines.
- Headings, version-only lines, availability notes, instructions and unclassified bug-fix lines are skipped.
- Each remaining line becomes one Change Card with one theme from a fixed vocabulary.
- At most five cards are kept per release, so long GitHub release notes are sampled; each release page shows "Tracked N of M candidate lines".
- Lines without a confident theme wait in a review queue and are not published.
- Dates are announcement dates, not availability dates.
- Relations between cards are same-theme chronology only; they never claim adoption or causation.
<!-- chronolog:end -->

## Review status
<!-- chronolog:begin region="status" -->
3 products · 790 archived releases · 1,949 tracked changes · 25 themes. Pending theme review: 149. Silence alerts: 0. Every generated batch is reviewed in a pull request before it is published.
<!-- chronolog:end -->

## Glossary
<!-- chronolog:begin region="glossary" -->
- **Change Card**: one announced change, taken from one line of an official release, with a date, one theme and the quoted source line.
- **Release**: one archived entry of an official changelog or release page; its page lists the cards tracked from it.
- **Theme**: a category from a fixed vocabulary that groups cards across products.
- **Era**: a reviewed phase of one product's history, bounded by cited releases.
- **Tracked products only**: comparisons and "earliest" statements cover only the tracked products, not the wider market.
- **Candidate line**: a line of release text that could become a card; Markdown headings, code samples and very short lines are not counted. "Tracked N of M candidate lines" compares the cards kept with these lines.
<!-- chronolog:end -->

## Feedback
<!-- chronolog:begin region="feedback" -->
Every card ends with a link that opens a prefilled issue. For anything else, open an issue at [https://github.com/Wang-Shuo/chronolog/issues](https://github.com/Wang-Shuo/chronolog/issues).
<!-- chronolog:end -->