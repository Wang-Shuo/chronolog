---
card_id: codex-cli-2026-09-01-724ba6
date: '2026-09-01'
description: 'Codex CLI · 2026-09-01 · Developer Workflow: 6 changes in 0.152.0 —
  The terminal UI and `codex exec` show credential-refresh progress, including Amazon
  Bedrock…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1263
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 5961369f8fd4e494ff70702cf9f8818e20d516a9c8acf8d26f2e3615171a2552
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-09-01-724ba6
  comparison: ''
  date: '2026-09-01'
  description: 'Codex CLI — 0.152.0: 6 Developer Workflow changes'
  evidence:
  - quote: The terminal UI and `codex exec` show credential-refresh progress, including
      Amazon Bedrock reauthentication. (#41239)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.152.0
  - quote: '#41328 Review terminal input against retained permissions @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.152.0
  - quote: '#41354 Reject NUL bytes in reviewed terminal input @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.152.0
  - quote: '#41368 Match Windows shell guidance to the executor platform @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.152.0
  - quote: '#41384 Support configurable timeouts for thread shell commands @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.152.0
  - quote: '#41436 Respond to terminal queries from TTY subprocesses @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.152.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 6-developer-workflow-changes-in-rust-v0-152-0
  source_release: codex-cli-2026-09-01-rust-v0-152-0-github-380164108-cd339544
  source_type: github_releases
  theme: developer-workflow
  title: 6 Developer Workflow changes in rust-v0.152.0
  type: change
related_changes:
- '[[Changes/Open WebUI/2026-08-31-9-developer-workflow-changes-in-v0-11-2|9 Developer
  Workflow changes in v0.11.2]]'
- '[[Changes/OpenClaw/2026-08-31-each-area-below-has-its-own-page-keeping-the-user-facing-description-and-the-com|Each
  area below has its own page, keeping the user-facing description…]]'
- '[[Changes/Claude Code/2026-09-01-3-developer-workflow-changes-in-v2-1-257|3 Developer
  Workflow changes in v2.1.257]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-09-01-rust-v0-152-0-github-380164108-cd339544|codex-cli-2026-09-01-rust-v0-152-0-github-380164108-cd339544]]'
source_type: github_releases
theme: developer-workflow
title: 6 Developer Workflow changes in rust-v0.152.0
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Developer Workflow changes in rust-v0.152.0

**Codex CLI** · 2026-09-01 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.152.0) · from [[Releases/Codex CLI/codex-cli-2026-09-01-rust-v0-152-0-github-380164108-cd339544|0.152.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> The terminal UI and `codex exec` show credential-refresh progress, including Amazon Bedrock reauthentication. (#41239)

> #41328 Review terminal input against retained permissions @copyberry

> #41354 Reject NUL bytes in reviewed terminal input @copyberry

> #41368 Match Windows shell guidance to the executor platform @copyberry

> #41384 Support configurable timeouts for thread shell commands @copyberry

> #41436 Respond to terminal queries from TTY subprocesses @copyberry

Source: https://github.com/openai/codex/releases/tag/rust-v0.152.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-09-01-5-collaboration-changes-in-rust-v0-152-0|5 Collaboration changes in rust-v0.152.0]] · Collaboration
- [[Changes/Codex CLI/2026-09-01-4-agent-mode-changes-in-rust-v0-152-0|4 Agent Mode changes in rust-v0.152.0]] · Agent Mode
- [[Changes/Codex CLI/2026-09-01-41457-source-proactive-multi-agent-instructions-from-the-model-catalog-copyberry|♯41457 Source proactive multi-agent instructions from the model catalog @copyberry]] · Automation and Scheduling
- [[Changes/Codex CLI/2026-09-01-6-model-support-changes-in-rust-v0-152-0|6 Model Support changes in rust-v0.152.0]] · Model Support
- [[Changes/Codex CLI/2026-09-01-rate-limit-banners-offer-actions-for-checking-usage-managing-credits-resetting-l|Rate-limit banners offer actions for checking usage, managing credits, resetting…]] · Pricing Model
- [[Changes/Codex CLI/2026-09-01-9-context-window-changes-in-rust-v0-152-0|9 Context Window changes in rust-v0.152.0]] · Context Window
- [[Changes/Codex CLI/2026-09-01-41227-use-compatible-powershell-for-elevated-windows-sandbox-commands-copyberry|♯41227 Use compatible PowerShell for elevated Windows sandbox commands @copyberry]] · Safety and Privacy
- [[Changes/Codex CLI/2026-09-01-2-account-and-access-changes-in-rust-v0-152-0|2 Account and Access changes in rust-v0.152.0]] · Account and Access
- [[Changes/Codex CLI/2026-09-01-3-interface-experience-changes-in-rust-v0-152-0|3 Interface Experience changes in rust-v0.152.0]] · Interface Experience
- [[Changes/Codex CLI/2026-09-01-16-apps-and-integrations-changes-in-rust-v0-152-0|16 Apps and Integrations changes in rust-v0.152.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-09-01-50-other-changes-in-rust-v0-152-0|50 other changes in rust-v0.152.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-09-01 · Claude Code · [[Changes/Claude Code/2026-09-01-3-developer-workflow-changes-in-v2-1-257|3 Developer Workflow changes in v2.1.257]]
- Later: 2026-09-01 · v0 · [[Changes/v0/2026-09-01-github-backed-projects-now-have-a-unified-branch-and-publish-flow-in-v0|GitHub-backed projects now have a unified branch-and-Publish flow in v0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-18 · Cursor · [[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-09-01-724ba6&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-09-01-6-developer-workflow-changes-in-rust-v0-152-0.md%0ACard%20ID%3A%20codex-cli-2026-09-01-724ba6%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.152.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->