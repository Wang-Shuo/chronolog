---
card_id: claude-code-2026-10-06-9d8fc8
date: '2026-10-06'
description: 'Claude Code · 2026-10-06 · Other changes: 8 changes in v2.1.292 — Added
  `CLAUDE_CODE_OVERLOADED_RETRY_BASE_DELAY_MS` environment variable to set a longer
  base…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: bd2ae8573c69bd7c5ac3865ec4d89b6f8282d65d9ad122eff4f7ec31b4e420ee
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-10-06-9d8fc8
  comparison: ''
  date: '2026-10-06'
  description: 'Claude Code — v2.1.292: 8 other changes'
  evidence:
  - quote: Added `CLAUDE_CODE_OVERLOADED_RETRY_BASE_DELAY_MS` environment variable
      to set a longer base delay for the backoff when retrying an overloaded (529)
      request
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.292
  - quote: 'Improved hook output handling: `<system-reminder>` tags written in a hook''s
      output are escaped before they reach Claude'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.292
  - quote: 'Improved tool input handling: Grep accepts `file_path` for `path`, and
      Write, WebFetch and Read ignore a few stray parameters instead of failing the
      call'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.292
  - quote: Improved the steps shown when a marketplace declared in a settings file
      has a name that looks like an official Anthropic marketplace
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.292
  - quote: 'Improved the Artifact tool''s listing: Claude now sees how many published
      artifacts you have and can list up to 200 at once instead of 50'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.292
  - quote: 'Improved the Claude in Chrome message in claude.ai cloud sessions when
      the browser can''t be reached: Claude is now told it may continue with alternatives
      if the user prefers'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.292
  - quote: '[Claude Tag] Improved `@Claude !status` in a channel to say when Claude
      has stopped reading its untagged messages, why, and that an @-mention starts
      it reading again'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.292
  - quote: '[Claude Tag] Changed the organization-wide and default spend limit boxes
      on Claude Tag''s spend limits page in admin settings to save only when you press
      Save or Enter, not when you click away'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.292
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 8-other-changes-in-v2-1-292
  source_release: claude-code-2026-10-06-v2-1-292-github-404958910-b2fd21ab
  source_type: github_releases
  theme: uncategorized
  title: 8 other changes in v2.1.292
  type: change
source_release: '[[Releases/Claude Code/claude-code-2026-10-06-v2-1-292-github-404958910-b2fd21ab|claude-code-2026-10-06-v2-1-292-github-404958910-b2fd21ab]]'
source_type: github_releases
theme: uncategorized
title: 8 other changes in v2.1.292
type: change
---

<!-- chronolog:begin region="header" -->
# 8 other changes in v2.1.292

**Claude Code** · 2026-10-06 · Other changes · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.292) · from [[Releases/Claude Code/claude-code-2026-10-06-v2-1-292-github-404958910-b2fd21ab|v2.1.292]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added `CLAUDE_CODE_OVERLOADED_RETRY_BASE_DELAY_MS` environment variable to set a longer base delay for the backoff when retrying an overloaded (529) request

> Improved hook output handling: `<system-reminder>` tags written in a hook's output are escaped before they reach Claude

> Improved tool input handling: Grep accepts `file_path` for `path`, and Write, WebFetch and Read ignore a few stray parameters instead of failing the call

> Improved the steps shown when a marketplace declared in a settings file has a name that looks like an official Anthropic marketplace

> Improved the Artifact tool's listing: Claude now sees how many published artifacts you have and can list up to 200 at once instead of 50

> Improved the Claude in Chrome message in claude.ai cloud sessions when the browser can't be reached: Claude is now told it may continue with alternatives if the user prefers

> [Claude Tag] Improved `@Claude !status` in a channel to say when Claude has stopped reading its untagged messages, why, and that an @-mention starts it reading again

> [Claude Tag] Changed the organization-wide and default spend limit boxes on Claude Tag's spend limits page in admin settings to save only when you press Save or Enter, not when you click away

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.292
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-10-06-6-safety-and-privacy-changes-in-v2-1-292|6 Safety and Privacy changes in v2.1.292]] · Safety and Privacy
- [[Changes/Claude Code/2026-10-06-9-apps-and-integrations-changes-in-v2-1-292|9 Apps and Integrations changes in v2.1.292]] · Apps and Integrations
- [[Changes/Claude Code/2026-10-06-improved-rendering-speed-of-long-bulleted-or-numbered-replies-they-stream-resize|Improved rendering speed of long bulleted or numbered replies]] · Reliability and Performance
- [[Changes/Claude Code/2026-10-06-added-prompt-autocomplete-an-event-a-mod-hooks-to-add-its-own-rows-to-the-prompt|Added prompt.autocomplete, an event a mod hooks to add its own rows to the prompt…]] · Editor Experience
- [[Changes/Claude Code/2026-10-06-2-developer-workflow-changes-in-v2-1-292|2 Developer Workflow changes in v2.1.292]] · Developer Workflow
- [[Changes/Claude Code/2026-10-06-claude-tag-added-an-edit-button-to-the-allowed-domains-card-on-a-channel-s-confi|Claude Tag Added an Edit button to the Allowed domains card on a channel's…]] · Enterprise and Administration
- [[Changes/Claude Code/2026-10-06-improved-the-focus-tip-it-now-invites-you-to-try-focus-view-mid-turn-and-shows-h|Improved the /focus tip]] · Interface Experience
- [[Changes/Claude Code/2026-10-06-added-prompt-caching-to-model-complete-for-mods-prompt-and-system-take-blocks-of|Added prompt caching to $.model.complete for mods]] · Model Support
- [[Changes/Claude Code/2026-10-06-3-agent-mode-changes-in-v2-1-292|3 Agent Mode changes in v2.1.292]] · Agent Mode
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-10-06-9d8fc8&body=Card%3A%20Changes%2FClaude%20Code%2F2026-10-06-8-other-changes-in-v2-1-292.md%0ACard%20ID%3A%20claude-code-2026-10-06-9d8fc8%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.292%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->