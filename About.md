---
created: '2022-12-15'
date: '2026-10-22'
description: Where ChronoLog's data comes from, how official release notes become
  reviewed Change Cards, what is grouped or skipped, and how to report a problem.
machine_hash: 18173d927ef9250af5b2bbacd9d5f690bbb40b2ff8fea866acc7138829d11f7e
modified: '2026-10-22'
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
- Archived releases: 298, dated 2022-12-15 → 2026-10-20
- Official browser snapshot captured: 2026-10-23T12:07:22.643Z. Imported snapshot; this is not a successful automatic HTTP fetch.
- Known gaps: Official changelog entries only; Codex-only entries excluded. Rollout dates are not universal availability dates.

### Claude Code
- Official source: [Claude Code GitHub releases](https://github.com/anthropics/claude-code/releases)
- Archived releases: 252, dated 2025-12-19 → 2026-10-22
- Last successful fetch: 2026-10-23T12:44:27Z.
- Known gaps: GitHub Releases starts at v2.0.73 on 2025-12-19. Official CHANGELOG.md contains 0.2.x–2.0.72 history without publication dates; not imported.

### Cursor
- Official source: [Cursor changelog](https://cursor.com/changelog)
- Archived releases: 256, dated 2023-03-14 → 2026-10-16
- Last successful fetch: 2026-10-23T12:44:43Z.
- Known gaps: Official paginated changelog only; unannounced changes are outside scope.
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
3 products · 806 archived releases · 2,689 tracked changes · 25 themes. Pending theme review: 63. Silence alerts: 0. Every generated batch is reviewed in a pull request before it is published.
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