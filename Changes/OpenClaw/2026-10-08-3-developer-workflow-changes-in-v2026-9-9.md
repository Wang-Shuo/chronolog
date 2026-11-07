---
card_id: openclaw-2026-10-08-280f09
date: '2026-10-08'
description: 'OpenClaw · 2026-10-08 · Developer Workflow: 3 changes in v2026.9.9 —
  Monterey service commands. On affected macOS 12 installations, Gateway stop, restart
  and…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1300
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: d6e838b83eba2c8c367e80c8e08c96d2d6cf37f9c9a5a2ca6f3f5bc688c7cb27
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-10-08-280f09
  comparison: ''
  date: '2026-10-08'
  description: 'OpenClaw — v2026.9.9: 3 Developer Workflow changes'
  evidence:
  - quote: 'Monterey service commands. On affected macOS 12 installations, Gateway
      stop, restart and update commands can run from an independent Terminal window
      when OpenClaw can establish that it is safe to do so. An unfixed older updater
      may still need the one-time stop, update and start sequence . #163317 , #165935
      by @NovaUnboundAi , @xXG0DLessXx and @RomneyDa .'
    source_release: https://docs.openclaw.ai/releases/2026.9.9
  - quote: 'Bundled Codex. The copy of Codex included with OpenClaw is updated to
      0.160.0, bringing fixes for starting sessions and recording diagnostic logs.
      This bundled copy is separate from any Codex command-line app you update yourself.
      #163560 by @vincentkoc .'
    source_release: https://docs.openclaw.ai/releases/2026.9.9
  - quote: 'Delegated task startup. Cloud sessions can start with long assignments
      without shortening the task, and visible child sessions keep their own worktree
      on later turns instead of failing a workspace check. #159459 , #162308 , with
      contributions from @steipete .'
    source_release: https://docs.openclaw.ai/releases/2026.9.9
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 3-developer-workflow-changes-in-v2026-9-9
  source_release: openclaw-2026-10-08-v2026-9-9-933614cc
  source_type: openclaw_changelog
  theme: developer-workflow
  title: 3 Developer Workflow changes in v2026.9.9
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-10-07-warmed-language-servers-stay-running-across-lsp-requests-when-sandboxing-is-disa|Warmed
  language servers stay running across LSP requests when sandboxing is disabled]]'
- '[[Changes/Claude Code/2026-10-08-added-a-line-on-stderr-when-it-is-a-terminal-that-says-what-a-claude-p-run-is-wa|Added
  a line on stderr, when it is a terminal, that says what a claude -p run…]]'
- '[[Changes/Codex CLI/2026-10-08-12-developer-workflow-changes-in-rust-v0-162-0|12
  Developer Workflow changes in rust-v0.162.0]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-10-08-v2026-9-9-933614cc|openclaw-2026-10-08-v2026-9-9-933614cc]]'
source_type: openclaw_changelog
theme: developer-workflow
title: 3 Developer Workflow changes in v2026.9.9
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Developer Workflow changes in v2026.9.9

**OpenClaw** · 2026-10-08 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.9) · from [[Releases/OpenClaw/openclaw-2026-10-08-v2026-9-9-933614cc|v2026.9.9]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Monterey service commands. On affected macOS 12 installations, Gateway stop, restart and update commands can run from an independent Terminal window when OpenClaw can establish that it is safe to do so. An unfixed older updater may still need the one-time stop, update and start sequence . #163317 , #165935 by @NovaUnboundAi , @xXG0DLessXx and @RomneyDa .

> Bundled Codex. The copy of Codex included with OpenClaw is updated to 0.160.0, bringing fixes for starting sessions and recording diagnostic logs. This bundled copy is separate from any Codex command-line app you update yourself. #163560 by @vincentkoc .

> Delegated task startup. Cloud sessions can start with long assignments without shortening the task, and visible child sessions keep their own worktree on later turns instead of failing a workspace check. #159459 , #162308 , with contributions from @steipete .

Source: https://docs.openclaw.ai/releases/2026.9.9
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-10-08-4-agent-mode-changes-in-v2026-9-9|4 Agent Mode changes in v2026.9.9]] · Agent Mode
- [[Changes/OpenClaw/2026-10-08-model-retries-and-context-one-shot-model-requests-through-the-gateway-retain-the|Model retries and context]] · Context Window
- [[Changes/OpenClaw/2026-10-08-2-voice-and-audio-changes-in-v2026-9-9|2 Voice and Audio changes in v2026.9.9]] · Voice and Audio
- [[Changes/OpenClaw/2026-10-08-windows-mxc-sandbox-the-optional-mxc-sandbox-can-start-and-run-tools-on-compatib|Windows MXC sandbox]] · Safety and Privacy
- [[Changes/OpenClaw/2026-10-08-claude-haiku-5-5-you-can-select-haiku-5-5-through-the-anthropic-api-and-claude-c|Claude Haiku 5.5. You can select Haiku 5.5 through the Anthropic API and Claude CLI]] · Pricing Model
- [[Changes/OpenClaw/2026-10-08-4-interface-experience-changes-in-v2026-9-9|4 Interface Experience changes in v2026.9.9]] · Interface Experience
- [[Changes/OpenClaw/2026-10-08-10-apps-and-integrations-changes-in-v2026-9-9|10 Apps and Integrations changes in v2026.9.9]] · Apps and Integrations
- [[Changes/OpenClaw/2026-10-08-2-account-and-access-changes-in-v2026-9-9|2 Account and Access changes in v2026.9.9]] · Account and Access
- [[Changes/OpenClaw/2026-10-08-2-enterprise-and-administration-changes-in-v2026-9-9|2 Enterprise and Administration changes in v2026.9.9]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-10-08-4-model-support-changes-in-v2026-9-9|4 Model Support changes in v2026.9.9]] · Model Support
- [[Changes/OpenClaw/2026-10-08-3-mobile-and-desktop-changes-in-v2026-9-9|3 Mobile and Desktop changes in v2026.9.9]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-10-08-feishu-attachments-files-sent-with-captions-or-together-in-feishu-lark-posts-rea|Feishu attachments]] · Multimodal Input
- [[Changes/OpenClaw/2026-10-08-2-memory-and-personalization-changes-in-v2026-9-9|2 Memory and Personalization changes in v2026.9.9]] · Memory and Personalization
- [[Changes/OpenClaw/2026-10-08-2-automation-and-scheduling-changes-in-v2026-9-9|2 Automation and Scheduling changes in v2026.9.9]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-10-08-september-database-compatibility-upgrading-from-september-stable-keeps-shared-da|September database compatibility]] · Collaboration
- [[Changes/OpenClaw/2026-10-08-24-other-changes-in-v2026-9-9|24 other changes in v2026.9.9]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-10-08 · Codex CLI · [[Changes/Codex CLI/2026-10-08-12-developer-workflow-changes-in-rust-v0-162-0|12 Developer Workflow changes in rust-v0.162.0]]
- Later: 2026-10-09 · Claude Code · [[Changes/Claude Code/2026-10-09-3-developer-workflow-changes-in-v2-1-296|3 Developer Workflow changes in v2.1.296]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-18 · Cursor · [[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-10-08-280f09&body=Card%3A%20Changes%2FOpenClaw%2F2026-10-08-3-developer-workflow-changes-in-v2026-9-9.md%0ACard%20ID%3A%20openclaw-2026-10-08-280f09%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.9%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->