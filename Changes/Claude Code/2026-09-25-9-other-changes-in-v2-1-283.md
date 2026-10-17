---
card_id: claude-code-2026-09-25-becb25
date: '2026-09-25'
description: 'Claude Code · 2026-09-25 · Other changes: 9 changes in v2.1.283 — Improved
  `/tasks`: rows show a status icon, the name and whole facts, the title and key hints…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 974ed71e90a0ceced6cd0e25fbf7b08c890ac831a3874dc7c86e40838c3d5012
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-09-25-becb25
  comparison: ''
  date: '2026-09-25'
  description: 'Claude Code — v2.1.283: 9 other changes'
  evidence:
  - quote: 'Improved `/tasks`: rows show a status icon, the name and whole facts,
      the title and key hints stay on screen with many tasks, and the list gains paging
      keys, the mouse wheel and clicks'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.283
  - quote: Improved lists beside a search box, such as `/skills` and `/artifacts`,
      to draw their pointer dim while the search box has the keys, so only one pointer
      is highlighted
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.283
  - quote: 'Improved artifact database reads: an ordered query that returns a full
      page now says it is one page and how to read the rest'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.283
  - quote: 'Improved startup for claude.ai accounts whose Artifact tool features aren''t
      known yet, as on a first run: the prompt no longer waits up to 1.5 s to check
      them; the first message waits if needed'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.283
  - quote: Changed the `/ultrareview` launch dialog to say that reviewing a local
      branch may upload uncommitted changes to tracked files
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.283
  - quote: Changed `--system-prompt` and `--append-system-prompt` to accept their
      text and `-file` forms together; the file's text comes first
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.283
  - quote: 'Changed artifact watching: a watch that was armed automatically (not one
      you asked for) now ends after 3.5 hours with no activity; publishing or watching
      the artifact again re-arms it'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.283
  - quote: '[Cloud sessions] Improved adding a repository to a running cloud session:
      a private repository your GitHub account can read but not push to now attaches
      for reading'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.283
  - quote: '[Cloud sessions] Changed new routine schedules to default to a few minutes
      past the hour, with a note that routines set exactly on the hour can start several
      minutes late'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.283
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 9-other-changes-in-v2-1-283
  source_release: claude-code-2026-09-25-v2-1-283-github-396845205-9a5a07f8
  source_type: github_releases
  theme: uncategorized
  title: 9 other changes in v2.1.283
  type: change
source_release: '[[Releases/Claude Code/claude-code-2026-09-25-v2-1-283-github-396845205-9a5a07f8|claude-code-2026-09-25-v2-1-283-github-396845205-9a5a07f8]]'
source_type: github_releases
theme: uncategorized
title: 9 other changes in v2.1.283
type: change
---

<!-- chronolog:begin region="header" -->
# 9 other changes in v2.1.283

**Claude Code** · 2026-09-25 · Other changes · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.283) · from [[Releases/Claude Code/claude-code-2026-09-25-v2-1-283-github-396845205-9a5a07f8|v2.1.283]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Improved `/tasks`: rows show a status icon, the name and whole facts, the title and key hints stay on screen with many tasks, and the list gains paging keys, the mouse wheel and clicks

> Improved lists beside a search box, such as `/skills` and `/artifacts`, to draw their pointer dim while the search box has the keys, so only one pointer is highlighted

> Improved artifact database reads: an ordered query that returns a full page now says it is one page and how to read the rest

> Improved startup for claude.ai accounts whose Artifact tool features aren't known yet, as on a first run: the prompt no longer waits up to 1.5 s to check them; the first message waits if needed

> Changed the `/ultrareview` launch dialog to say that reviewing a local branch may upload uncommitted changes to tracked files

> Changed `--system-prompt` and `--append-system-prompt` to accept their text and `-file` forms together; the file's text comes first

> Changed artifact watching: a watch that was armed automatically (not one you asked for) now ends after 3.5 hours with no activity; publishing or watching the artifact again re-arms it

> [Cloud sessions] Improved adding a repository to a running cloud session: a private repository your GitHub account can read but not push to now attaches for reading

> [Cloud sessions] Changed new routine schedules to default to a few minutes past the hour, with a note that routines set exactly on the hour can start several minutes late

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.283
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-09-25-3-developer-workflow-changes-in-v2-1-283|3 Developer Workflow changes in v2.1.283]] · Developer Workflow
- [[Changes/Claude Code/2026-09-25-improved-startup-claude-p-and-claude-code-remote-no-longer-load-the-interactive|Improved startup: claude -p and Claude Code Remote no longer load the interactive…]] · Agent Mode
- [[Changes/Claude Code/2026-09-25-14-apps-and-integrations-changes-in-v2-1-283|14 Apps and Integrations changes in v2.1.283]] · Apps and Integrations
- [[Changes/Claude Code/2026-09-25-3-safety-and-privacy-changes-in-v2-1-283|3 Safety and Privacy changes in v2.1.283]] · Safety and Privacy
- [[Changes/Claude Code/2026-09-25-improved-prompt-audit-on-claude-code-configuration-stale-paths-stale-commands-an|Improved prompt-audit on Claude Code configuration]] · Files and Data
- [[Changes/Claude Code/2026-09-25-2-context-window-changes-in-v2-1-283|2 Context Window changes in v2.1.283]] · Context Window
- [[Changes/Claude Code/2026-09-25-2-reliability-and-performance-changes-in-v2-1-283|2 Reliability and Performance changes in v2.1.283]] · Reliability and Performance
- [[Changes/Claude Code/2026-09-25-improved-lists-in-help-hooks-copy-chrome-memory-ide-release-notes-rewind-diff-re|Improved lists in /help, /hooks, /copy, /chrome, /memory, /ide…]] · Memory and Personalization
- [[Changes/Claude Code/2026-09-25-2-interface-experience-changes-in-v2-1-283|2 Interface Experience changes in v2.1.283]] · Interface Experience
- [[Changes/Claude Code/2026-09-25-3-model-support-changes-in-v2-1-283|3 Model Support changes in v2.1.283]] · Model Support
- [[Changes/Claude Code/2026-09-25-added-doctor-prompt-audit-also-checkup-prompt-audit-to-audit-your-claude-md-file|Added /doctor prompt-audit (also /checkup prompt-audit) to audit your CLAUDE.md…]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-09-25-becb25&body=Card%3A%20Changes%2FClaude%20Code%2F2026-09-25-9-other-changes-in-v2-1-283.md%0ACard%20ID%3A%20claude-code-2026-09-25-becb25%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.283%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->