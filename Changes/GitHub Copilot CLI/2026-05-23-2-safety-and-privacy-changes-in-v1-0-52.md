---
card_id: github-copilot-cli-2026-05-23-e8d24d
date: '2026-05-23'
description: 'GitHub Copilot CLI · 2026-05-23 · Safety and Privacy: 2 changes in 1.0.52
  — Switching to Autopilot mode no longer triggers unexpected permission prompts for…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1133
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 4e5894f2b51d12ddca36900a4630fc70653fe03f2688928529c1ba9c97513b61
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-05-23-e8d24d
  comparison: ''
  date: '2026-05-23'
  description: 'GitHub Copilot CLI — 1.0.52: 2 Safety and Privacy changes'
  evidence:
  - quote: Switching to Autopilot mode no longer triggers unexpected permission prompts
      for tool, path, or URL access
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.52
  - quote: Kill command safety filter no longer rejects valid commands that contain
      shell redirection like `kill -0 <PID> 2>/dev/null`.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.52
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 2-safety-and-privacy-changes-in-v1-0-52
  source_release: github-copilot-cli-2026-05-23-v1-0-52-github-328402909-801444d4
  source_type: github_releases
  theme: safety-privacy
  title: 2 Safety and Privacy changes in v1.0.52
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-05-21-17-safety-and-privacy-changes-in-rust-v0-133-0|17
  Safety and Privacy changes in rust-v0.133.0]]'
- '[[Changes/Claude Code/2026-05-22-2-safety-and-privacy-changes-in-v2-1-149|2 Safety
  and Privacy changes in v2.1.149]]'
- '[[Changes/Gemini CLI/2026-05-22-docs-add-vi-mode-shortcuts-and-clarify-mcp-custom-sandbox-setup-by-chrisjcthomas|docs:
  add vi mode shortcuts and clarify MCP/custom sandbox setup]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-05-23-v1-0-52-github-328402909-801444d4|github-copilot-cli-2026-05-23-v1-0-52-github-328402909-801444d4]]'
source_type: github_releases
theme: safety-privacy
title: 2 Safety and Privacy changes in v1.0.52
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Safety and Privacy changes in v1.0.52

**GitHub Copilot CLI** · 2026-05-23 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.52) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-05-23-v1-0-52-github-328402909-801444d4|1.0.52]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Switching to Autopilot mode no longer triggers unexpected permission prompts for tool, path, or URL access

> Kill command safety filter no longer rejects valid commands that contain shell redirection like `kill -0 <PID> 2>/dev/null`.

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.52
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-05-23-automatically-prune-old-process-log-files-from-copilot-logs-at-startup-to-preven|Automatically prune old process log files from ~/.copilot/logs/ at startup…]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-05-23-2-mobile-and-desktop-changes-in-v1-0-52|2 Mobile and Desktop changes in v1.0.52]] · Mobile and Desktop
- [[Changes/GitHub Copilot CLI/2026-05-23-2-account-and-access-changes-in-v1-0-52|2 Account and Access changes in v1.0.52]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-05-23-6-interface-experience-changes-in-v1-0-52|6 Interface Experience changes in v1.0.52]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-05-23-general-purpose-subagents-use-gpt-5-4-or-gpt-5-5-when-available|General-purpose subagents use GPT-5.4 or GPT-5.5 when available]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-05-23-custom-agents-support-opt-in-deferred-tool-loading-via-deferred-tool-loading-in|Custom agents support opt-in deferred tool loading via deferred-tool-loading…]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-05-23-2-apps-and-integrations-changes-in-v1-0-52|2 Apps and Integrations changes in v1.0.52]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-05-23-3-pricing-model-changes-in-v1-0-52|3 Pricing Model changes in v1.0.52]] · Pricing Model
- [[Changes/GitHub Copilot CLI/2026-05-23-4-context-window-changes-in-v1-0-52|4 Context Window changes in v1.0.52]] · Context Window
- [[Changes/GitHub Copilot CLI/2026-05-23-6-other-changes-in-v1-0-52|6 other changes in v1.0.52]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-05-22 · Gemini CLI · [[Changes/Gemini CLI/2026-05-22-docs-add-vi-mode-shortcuts-and-clarify-mcp-custom-sandbox-setup-by-chrisjcthomas|docs: add vi mode shortcuts and clarify MCP/custom sandbox setup]]
- Later: 2026-05-26 · Codex CLI · [[Changes/Codex CLI/2026-05-26-7-safety-and-privacy-changes-in-rust-v0-134-0|7 Safety and Privacy changes in rust-v0.134.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-05-23-e8d24d&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-05-23-2-safety-and-privacy-changes-in-v1-0-52.md%0ACard%20ID%3A%20github-copilot-cli-2026-05-23-e8d24d%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.52%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->