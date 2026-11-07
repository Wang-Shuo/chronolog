---
card_id: github-copilot-cli-2026-08-03-e60a72
date: '2026-08-03'
description: 'GitHub Copilot CLI · 2026-08-03 · Safety and Privacy: 3 changes in 1.0.78
  — Disabling the sandbox from a bypass prompt applies only to that session; new…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1205
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: ec31274c217d088feafbe45613d8a1c445fceb4c929ad09600043a219ef405a1
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-08-03-e60a72
  comparison: ''
  date: '2026-08-03'
  description: 'GitHub Copilot CLI — 1.0.78: 3 Safety and Privacy changes'
  evidence:
  - quote: Disabling the sandbox from a bypass prompt applies only to that session;
      new sessions start sandboxed again
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.78
  - quote: When the sandbox blocks a shell command and bypass is allowed, CLI offers
      to re-run it outside the sandbox without asking the model
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.78
  - quote: 'New sandbox setting `allowDevToolCaches` (on by default): grants sandboxed
      builds access to toolchain caches, registries, and installs so builds work without
      extra setup. Set false to opt out.'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.78
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 3-safety-and-privacy-changes-in-v1-0-78
  source_release: github-copilot-cli-2026-08-03-v1-0-78-github-364543196-53a079bc
  source_type: github_releases
  theme: safety-privacy
  title: 3 Safety and Privacy changes in v1.0.78
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-07-30-5-safety-and-privacy-changes-in-v1-0-76|5
  Safety and Privacy changes in v1.0.76]]'
- '[[Changes/GitHub Copilot CLI/2026-07-30-2-safety-and-privacy-changes-in-v1-0-77|2
  Safety and Privacy changes in v1.0.77]]'
- '[[Changes/Google Antigravity/2026-07-31-2-safety-and-privacy-changes-in-hub-v2-5-0-enterprise-sign-in-gemini|2
  Safety and Privacy changes in HUB v2.5.0 — Enterprise sign-in: Gemini…]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-08-03-v1-0-78-github-364543196-53a079bc|github-copilot-cli-2026-08-03-v1-0-78-github-364543196-53a079bc]]'
source_type: github_releases
theme: safety-privacy
title: 3 Safety and Privacy changes in v1.0.78
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Safety and Privacy changes in v1.0.78

**GitHub Copilot CLI** · 2026-08-03 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.78) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-08-03-v1-0-78-github-364543196-53a079bc|1.0.78]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Disabling the sandbox from a bypass prompt applies only to that session; new sessions start sandboxed again

> When the sandbox blocks a shell command and bypass is allowed, CLI offers to re-run it outside the sandbox without asking the model

> New sandbox setting `allowDevToolCaches` (on by default): grants sandboxed builds access to toolchain caches, registries, and installs so builds work without extra setup. Set false to opt out.

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.78
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-08-03-4-apps-and-integrations-changes-in-v1-0-78|4 Apps and Integrations changes in v1.0.78]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-08-03-a-run-whose-prompt-is-piped-over-stdin-now-treats-its-sessionend-hook-the-same-w|A run whose prompt is piped over stdin now treats its sessionEnd hook the same way…]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-08-03-2-editor-experience-changes-in-v1-0-78|2 Editor Experience changes in v1.0.78]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-08-03-resuming-a-long-session-is-dramatically-faster-and-far-lighter-on-memory-because|Resuming a long session is dramatically faster and far lighter on memory, because…]] · Reliability and Performance
- [[Changes/GitHub Copilot CLI/2026-08-03-2-account-and-access-changes-in-v1-0-78|2 Account and Access changes in v1.0.78]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-08-03-the-allow-all-auto-safety-judge-model-is-no-longer-user-configurable-the-judge-m|The /allow-all auto safety-judge model is no longer user-configurable]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-08-03-2-interface-experience-changes-in-v1-0-78|2 Interface Experience changes in v1.0.78]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-08-03-2-developer-workflow-changes-in-v1-0-78|2 Developer Workflow changes in v1.0.78]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-08-03-9-other-changes-in-v1-0-78|9 other changes in v1.0.78]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-07-31 · Google Antigravity · [[Changes/Google Antigravity/2026-07-31-2-safety-and-privacy-changes-in-hub-v2-5-0-enterprise-sign-in-gemini|2 Safety and Privacy changes in HUB v2.5.0 — Enterprise sign-in: Gemini…]]
- Later: 2026-08-04 · Claude Code · [[Changes/Claude Code/2026-08-04-improved-auto-mode-safety-messages-sent-to-other-agent-sessions-via-sendmessage|Improved auto mode safety]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-08-03-e60a72&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-08-03-3-safety-and-privacy-changes-in-v1-0-78.md%0ACard%20ID%3A%20github-copilot-cli-2026-08-03-e60a72%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.78%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->