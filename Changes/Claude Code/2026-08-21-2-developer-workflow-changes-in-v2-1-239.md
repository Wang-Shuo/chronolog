---
card_id: claude-code-2026-08-21-45f235
date: '2026-08-21'
description: 'Claude Code · 2026-08-21 · Developer Workflow: 2 changes in v2.1.239
  — `keybindingFlavor: "readline"` now also matches Bash for word keys: Alt+F and…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1252
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 34e0c38de62f8c184f38315b01c915d0c92564542aa7619e4750437b3acd07a9
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-08-21-45f235
  comparison: ''
  date: '2026-08-21'
  description: 'Claude Code — v2.1.239: 2 Developer Workflow changes'
  evidence:
  - quote: '`keybindingFlavor: "readline"` now also matches Bash for word keys: Alt+F
      and Ctrl/Option+→ stop at the end of the word, Alt+D deletes to it (Ctrl+Y pastes
      it back), and punctuation separates words'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.239
  - quote: 'Claude Code on the web: requests from Bash and other tools to non-API
      anthropic.com hosts (e.g. www, docs) now go through the session''s network proxy,
      so your environment''s allowed domains apply'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.239
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 2-developer-workflow-changes-in-v2-1-239
  source_release: claude-code-2026-08-21-v2-1-239-github-374556322-5f6b8918
  source_type: github_releases
  theme: developer-workflow
  title: 2 Developer Workflow changes in v2.1.239
  type: change
related_changes:
- '[[Changes/Claude Code/2026-08-14-added-gitlab-merge-request-url-support-to-the-worktree-flag-and-the-claude-agent|Added
  GitLab merge request URL support to the --worktree flag…]]'
- '[[Changes/Claude Code/2026-08-19-2-developer-workflow-changes-in-v2-1-236|2 Developer
  Workflow changes in v2.1.236]]'
- '[[Changes/Claude Code/2026-08-20-2-developer-workflow-changes-in-v2-1-238|2 Developer
  Workflow changes in v2.1.238]]'
source_release: '[[Releases/Claude Code/claude-code-2026-08-21-v2-1-239-github-374556322-5f6b8918|claude-code-2026-08-21-v2-1-239-github-374556322-5f6b8918]]'
source_type: github_releases
theme: developer-workflow
title: 2 Developer Workflow changes in v2.1.239
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Developer Workflow changes in v2.1.239

**Claude Code** · 2026-08-21 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.239) · from [[Releases/Claude Code/claude-code-2026-08-21-v2-1-239-github-374556322-5f6b8918|v2.1.239]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> `keybindingFlavor: "readline"` now also matches Bash for word keys: Alt+F and Ctrl/Option+→ stop at the end of the word, Alt+D deletes to it (Ctrl+Y pastes it back), and punctuation separates words

> Claude Code on the web: requests from Bash and other tools to non-API anthropic.com hosts (e.g. www, docs) now go through the session's network proxy, so your environment's allowed domains apply

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.239
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-08-21-3-interface-experience-changes-in-v2-1-239|3 Interface Experience changes in v2.1.239]] · Interface Experience
- [[Changes/Claude Code/2026-08-21-2-agent-mode-changes-in-v2-1-239|2 Agent Mode changes in v2.1.239]] · Agent Mode
- [[Changes/Claude Code/2026-08-21-persistent-retry-mode-claude-code-retry-watchdog-now-fails-immediately-on-organi|Persistent retry mode (CLAUDE_CODE_RETRY_WATCHDOG) now fails immediately…]] · Pricing Model
- [[Changes/Claude Code/2026-08-21-2-apps-and-integrations-changes-in-v2-1-239|2 Apps and Integrations changes in v2.1.239]] · Apps and Integrations
- [[Changes/Claude Code/2026-08-21-claude-in-chrome-clear-now-closes-the-session-s-chrome-tab-group-and-empty-group|Claude in Chrome]] · Editor Experience
- [[Changes/Claude Code/2026-08-21-improved-the-reminder-shown-after-compaction-so-a-skill-s-original-arguments-are|Improved the reminder shown after compaction so a skill's original arguments are not…]] · Context Window
- [[Changes/Claude Code/2026-08-21-remote-sessions-images-uploaded-from-mobile-now-include-their-saved-file-path-so|Remote sessions: images uploaded from mobile now include their saved file path…]] · Mobile and Desktop
- [[Changes/Claude Code/2026-08-21-fixed-fullscreen-mode-answering-a-permission-prompt-or-pressing-a-button-when-yo|Fixed fullscreen mode answering a permission prompt or pressing a button when you…]] · Safety and Privacy
- [[Changes/Claude Code/2026-08-21-windows-cross-session-messaging-is-now-available-so-claude-code-sessions-across|Windows: cross-session messaging is now available, so Claude Code sessions across…]] · Mobile and Desktop
- [[Changes/Claude Code/2026-08-21-alpine-musl-builds-native-image-paste-clipboard-and-audio-capture-add-ons-now-lo|Alpine/musl builds: native image paste, clipboard, and audio-capture add-ons now…]] · Voice and Audio
- [[Changes/Claude Code/2026-08-21-added-claude-api-upgrade-to-migrate-python-projects-from-anthropic-0-x-to-1-x-an|Added /claude-api upgrade to migrate Python projects from anthropic 0.x to 1.x…]] · Other changes
- [[Changes/Claude Code/2026-08-21-5-other-changes-in-v2-1-239|5 other changes in v2.1.239]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-08-20 · Claude Code · [[Changes/Claude Code/2026-08-20-2-developer-workflow-changes-in-v2-1-238|2 Developer Workflow changes in v2.1.238]]
- Later: 2026-08-25 · Claude Code · [[Changes/Claude Code/2026-08-25-2-developer-workflow-changes-in-v2-1-246|2 Developer Workflow changes in v2.1.246]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-18 · Cursor · [[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-08-21-45f235&body=Card%3A%20Changes%2FClaude%20Code%2F2026-08-21-2-developer-workflow-changes-in-v2-1-239.md%0ACard%20ID%3A%20claude-code-2026-08-21-45f235%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.239%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->