---
card_id: codex-cli-2025-10-23-dfd226
date: '2025-10-23'
description: 'Codex CLI · 2025-10-23 · Safety and Privacy: 2 changes in 0.48.0 — Configuration
  options for `forced_login_method` and `forced_chatgpt_workspace_id` which can…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke
    Application Access]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1913
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 9510365f68186d6e1dec9db2d986ab6f56247c56bbeef58756a21fbea83c983d
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2025-10-23-dfd226
  comparison: ''
  date: '2025-10-23'
  description: 'Codex CLI — 0.48.0: 2 Safety and Privacy changes'
  evidence:
  - quote: Configuration options for `forced_login_method` and `forced_chatgpt_workspace_id`
      which can be paired with [managed configs](https://developers.openai.com/codex/security#managed-configuration)
      to give enterprises more control over Codex usage.
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.48.0
  - quote: 'docs: align sandbox defaults, dedupe sections and improve getting started
      guide by @tibo-openai in https://github.com/openai/codex/pull/5357'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.48.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 2-safety-and-privacy-changes-in-rust-v0-48-0
  source_release: codex-cli-2025-10-23-rust-v0-48-0-github-256860123-ffacccba
  source_type: github_releases
  theme: safety-privacy
  title: 2 Safety and Privacy changes in rust-v0.48.0
  type: change
related_changes:
- '[[Changes/Dify/2025-10-22-fix-web-app-permission-check-by-douxc-in-https-github-com-langgenius-dify-pull-2|Fix/web
  app permission check]]'
- '[[Changes/Gemini CLI/2025-10-22-2-safety-and-privacy-changes-in-v0-10-0|2 Safety
  and Privacy changes in v0.10.0]]'
- '[[Changes/GitHub Copilot CLI/2025-10-22-ensure-that-environment-variables-are-expanded-before-running-path-permission-ch|Ensure
  that environment variables are expanded before running path permission checks]]'
source_release: '[[Releases/Codex CLI/codex-cli-2025-10-23-rust-v0-48-0-github-256860123-ffacccba|codex-cli-2025-10-23-rust-v0-48-0-github-256860123-ffacccba]]'
source_type: github_releases
theme: safety-privacy
title: 2 Safety and Privacy changes in rust-v0.48.0
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Safety and Privacy changes in rust-v0.48.0

**Codex CLI** · 2025-10-23 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.48.0) · from [[Releases/Codex CLI/codex-cli-2025-10-23-rust-v0-48-0-github-256860123-ffacccba|0.48.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Configuration options for `forced_login_method` and `forced_chatgpt_workspace_id` which can be paired with [managed configs](https://developers.openai.com/codex/security#managed-configuration) to give enterprises more control over Codex usage.

> docs: align sandbox defaults, dedupe sections and improve getting started guide by @tibo-openai in https://github.com/openai/codex/pull/5357

Source: https://github.com/openai/codex/releases/tag/rust-v0.48.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2025-10-23-tui-drop-citation-rendering-by-nornagon-openai-in-https-github-com-openai-codex|tui: drop citation rendering]] · Interface Experience
- [[Changes/Codex CLI/2025-10-23-3-account-and-access-changes-in-rust-v0-48-0|3 Account and Access changes in rust-v0.48.0]] · Account and Access
- [[Changes/Codex CLI/2025-10-23-2-agent-mode-changes-in-rust-v0-48-0|2 Agent Mode changes in rust-v0.48.0]] · Agent Mode
- [[Changes/Codex CLI/2025-10-23-chore-ci-speed-up-macos-builds-by-using-larger-runner-by-javisoto-in-https-githu|chore(ci): Speed up macOS builds by using larger runner]] · Reliability and Performance
- [[Changes/Codex CLI/2025-10-23-auto-compact-at-90-by-aibrahim-oai-in-https-github-com-openai-codex-pull-5292|Auto compact at ~90%]] · Context Window
- [[Changes/Codex CLI/2025-10-23-docs-document-exec-json-events-by-tibo-openai-in-https-github-com-openai-codex-p|docs: document exec json events]] · Files and Data
- [[Changes/Codex CLI/2025-10-23-11-apps-and-integrations-changes-in-rust-v0-48-0|11 Apps and Integrations changes in rust-v0.48.0]] · Apps and Integrations
- [[Changes/Codex CLI/2025-10-23-3-model-support-changes-in-rust-v0-48-0|3 Model Support changes in rust-v0.48.0]] · Model Support
- [[Changes/Codex CLI/2025-10-23-4-developer-workflow-changes-in-rust-v0-48-0|4 Developer Workflow changes in rust-v0.48.0]] · Developer Workflow
- [[Changes/Codex CLI/2025-10-23-45-other-changes-in-rust-v0-48-0|45 other changes in rust-v0.48.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2025-10-22 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2025-10-22-ensure-that-environment-variables-are-expanded-before-running-path-permission-ch|Ensure that environment variables are expanded before running path permission checks]]
- Later: 2025-10-25 · Codex CLI · [[Changes/Codex CLI/2025-10-25-5536-added-model-summary-and-risk-assessment-for-commands-that-violate-sandbox-p|♯5536 — Added model summary and risk assessment for commands that violate sandbox policy]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Descript · [[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke Application Access]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2025-10-23-dfd226&body=Card%3A%20Changes%2FCodex%20CLI%2F2025-10-23-2-safety-and-privacy-changes-in-rust-v0-48-0.md%0ACard%20ID%3A%20codex-cli-2025-10-23-dfd226%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.48.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->