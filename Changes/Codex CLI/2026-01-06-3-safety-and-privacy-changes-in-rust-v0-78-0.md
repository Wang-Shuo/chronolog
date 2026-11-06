---
card_id: codex-cli-2026-01-06-119820
date: '2026-01-06'
description: 'Codex CLI · 2026-01-06 · Safety and Privacy: 3 changes in 0.78.0 — #8483
  use a SandboxUsers group for ACLs instead of granting to each sandbox user separately…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 996
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: f20f737f92f69568a4ce207c8d8fa8639097be570f787e40f7aa57e4a6f2a89a
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-01-06-119820
  comparison: ''
  date: '2026-01-06'
  description: 'Codex CLI — 0.78.0: 3 Safety and Privacy changes'
  evidence:
  - quote: '#8483 use a SandboxUsers group for ACLs instead of granting to each sandbox
      user separately @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.78.0
  - quote: '#8683 never let sandbox write to .codex/ or .codex/.sandbox/ @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.78.0
  - quote: '#8492 best effort to "hide" Sandbox users @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.78.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 3-safety-and-privacy-changes-in-rust-v0-78-0
  source_release: codex-cli-2026-01-06-rust-v0-78-0-github-274610568-c3df153a
  source_type: github_releases
  theme: safety-privacy
  title: 3 Safety and Privacy changes in rust-v0.78.0
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2025-12-19-add-url-permission-controls-which-affect-common-shell-commands-which-access-the|Add
  URL permission controls which affect common shell commands which access the web]]'
- '[[Changes/Codex CLI/2025-12-21-2-safety-and-privacy-changes-in-rust-v0-77-0|2 Safety
  and Privacy changes in rust-v0.77.0]]'
- '[[Changes/Cursor/2025-12-22-improved-stability-around-how-the-agent-respects-auto-run-preferences-to-prevent|Improved
  stability around how the agent respects auto-run preferences to prevent…]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-01-06-rust-v0-78-0-github-274610568-c3df153a|codex-cli-2026-01-06-rust-v0-78-0-github-274610568-c3df153a]]'
source_type: github_releases
theme: safety-privacy
title: 3 Safety and Privacy changes in rust-v0.78.0
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Safety and Privacy changes in rust-v0.78.0

**Codex CLI** · 2026-01-06 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.78.0) · from [[Releases/Codex CLI/codex-cli-2026-01-06-rust-v0-78-0-github-274610568-c3df153a|0.78.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> #8483 use a SandboxUsers group for ACLs instead of granting to each sandbox user separately @iceweasel-oai

> #8683 never let sandbox write to .codex/ or .codex/.sandbox/ @iceweasel-oai

> #8492 best effort to "hide" Sandbox users @iceweasel-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.78.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-01-06-performance-tuning-for-tuis-cap-redraw-scheduling-and-reduce-unnecessary-rerende|Performance tuning for TUIs]] · Reliability and Performance
- [[Changes/Codex CLI/2026-01-06-8743-macos-load-config-requirements-from-mdm-gt-oai|♯8743 (MacOS) Load config requirements from MDM @gt-oai]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-01-06-2-context-window-changes-in-rust-v0-78-0|2 Context Window changes in rust-v0.78.0]] · Context Window
- [[Changes/Codex CLI/2026-01-06-3-editor-experience-changes-in-rust-v0-78-0|3 Editor Experience changes in rust-v0.78.0]] · Editor Experience
- [[Changes/Codex CLI/2026-01-06-6-developer-workflow-changes-in-rust-v0-78-0|6 Developer Workflow changes in rust-v0.78.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-01-06-support-enterprise-managed-configuration-requirements-on-macos-via-an-mdm-provid|Support enterprise-managed configuration requirements on macOS via an MDM-provided…]] · Enterprise and Administration
- [[Changes/Codex CLI/2026-01-06-9-interface-experience-changes-in-rust-v0-78-0|9 Interface Experience changes in rust-v0.78.0]] · Interface Experience
- [[Changes/Codex CLI/2026-01-06-5-model-support-changes-in-rust-v0-78-0|5 Model Support changes in rust-v0.78.0]] · Model Support
- [[Changes/Codex CLI/2026-01-06-8694-mcp-sanitize-mcp-tool-names-to-ensure-they-are-compatible-with-the-response|♯8694 MCP Sanitize MCP tool names to ensure they are compatible with the Responses…]] · Apps and Integrations
- [[Changes/Codex CLI/2026-01-06-65-other-changes-in-rust-v0-78-0|65 other changes in rust-v0.78.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2025-12-22 · Cursor · [[Changes/Cursor/2025-12-22-improved-stability-around-how-the-agent-respects-auto-run-preferences-to-prevent|Improved stability around how the agent respects auto-run preferences to prevent…]]
- Later: 2026-01-07 · Codex CLI · [[Changes/Codex CLI/2026-01-07-allow-global-exec-flags-model-json-sandbox-toggles-etc-to-be-passed-after-codex|Allow global exec flags (model/json/sandbox toggles, etc.) to be passed after…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-01-06-119820&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-01-06-3-safety-and-privacy-changes-in-rust-v0-78-0.md%0ACard%20ID%3A%20codex-cli-2026-01-06-119820%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.78.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->