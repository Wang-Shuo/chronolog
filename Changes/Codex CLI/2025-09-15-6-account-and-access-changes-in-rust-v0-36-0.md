---
card_id: codex-cli-2025-09-15-e2e88e
date: '2025-09-15'
description: 'Codex CLI · 2025-09-15 · Account and Access: 6 changes in 0.36.0 — API
  login is no longer implicit; we do not pick up `OPENAI_API_KEY` from the environment.
  To…'
diffusion:
  first_in_tracked: "[[Changes/Notion/2020-07-28-sign-into-notion-with-your-apple-id-the-perfect-combination-of-speedy-and-secure|Sign
    into Notion with your Apple ID \U0001F5DD️ The perfect combination of speedy and
    secure]]"
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1875
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: d2992b1c172e29e4af12476b4c5acdf59984344c04ed6cee8242693093710b35
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2025-09-15-e2e88e
  comparison: ''
  date: '2025-09-15'
  description: 'Codex CLI — 0.36.0: 6 Account and Access changes'
  evidence:
  - quote: 'API login is no longer implicit; we do not pick up `OPENAI_API_KEY` from
      the environment. To use an API key programmatically, run the following _once_:'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.36.0
  - quote: To switch to ChatGPT login instead of using your API key, run `codex login`.
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.36.0
  - quote: Note that `codex logout` will remove whatever login credential is stored
      in `auth.json` (API key or ChatGPT auth token).
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.36.0
  - quote: '**Auth and login experience**'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.36.0
  - quote: login polish (#3632); fix issue allowing to be both logged in and using
      API key simultaneously (#3611); fix stray login URL characters (#3639); fix
      `get_auth_status` for custom providers (#3581).
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.36.0
  - quote: Login flow polish (#3632)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.36.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 6-account-and-access-changes-in-rust-v0-36-0
  source_release: codex-cli-2025-09-15-rust-v0-36-0-github-247381260-0ebd05e2
  source_type: github_releases
  theme: account-access
  title: 6 Account and Access changes in rust-v0.36.0
  type: change
related_changes:
- '[[Changes/Codex CLI/2025-09-08-3217-added-logic-to-cancel-pending-oauth-login-to-free-up-localhost-port|♯3217
  Added logic to cancel pending oauth login to free up localhost port]]'
- '[[Changes/Gemini CLI/2025-09-09-feat-oauth-create-hybrid-storage-class-by-shishu314-in-https-github-com-google-g|feat(oauth)
  - Create hybrid storage class]]'
- '[[Changes/Open WebUI/2025-09-09-6-account-and-access-changes-in-v0-6-27|6 Account
  and Access changes in v0.6.27]]'
source_release: '[[Releases/Codex CLI/codex-cli-2025-09-15-rust-v0-36-0-github-247381260-0ebd05e2|codex-cli-2025-09-15-rust-v0-36-0-github-247381260-0ebd05e2]]'
source_type: github_releases
theme: account-access
title: 6 Account and Access changes in rust-v0.36.0
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Account and Access changes in rust-v0.36.0

**Codex CLI** · 2025-09-15 · [[Themes/account-access|Account and Access]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.36.0) · from [[Releases/Codex CLI/codex-cli-2025-09-15-rust-v0-36-0-github-247381260-0ebd05e2|0.36.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> API login is no longer implicit; we do not pick up `OPENAI_API_KEY` from the environment. To use an API key programmatically, run the following _once_:

> To switch to ChatGPT login instead of using your API key, run `codex login`.

> Note that `codex logout` will remove whatever login credential is stored in `auth.json` (API key or ChatGPT auth token).

> **Auth and login experience**

> login polish (#3632); fix issue allowing to be both logged in and using API key simultaneously (#3611); fix stray login URL characters (#3639); fix `get_auth_status` for custom providers (#3581).

> Login flow polish (#3632)

Source: https://github.com/openai/codex/releases/tag/rust-v0.36.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2025-09-15-5-interface-experience-changes-in-rust-v0-36-0|5 Interface Experience changes in rust-v0.36.0]] · Interface Experience
- [[Changes/Codex CLI/2025-09-15-2-developer-workflow-changes-in-rust-v0-36-0|2 Developer Workflow changes in rust-v0.36.0]] · Developer Workflow
- [[Changes/Codex CLI/2025-09-15-16-model-support-changes-in-rust-v0-36-0|16 Model Support changes in rust-v0.36.0]] · Model Support
- [[Changes/Codex CLI/2025-09-15-3-context-window-changes-in-rust-v0-36-0|3 Context Window changes in rust-v0.36.0]] · Context Window
- [[Changes/Codex CLI/2025-09-15-add-readme-ide-3494|add(readme): IDE (♯3494)]] · Editor Experience
- [[Changes/Codex CLI/2025-09-15-3-safety-and-privacy-changes-in-rust-v0-36-0|3 Safety and Privacy changes in rust-v0.36.0]] · Safety and Privacy
- [[Changes/Codex CLI/2025-09-15-5-apps-and-integrations-changes-in-rust-v0-36-0|5 Apps and Integrations changes in rust-v0.36.0]] · Apps and Integrations
- [[Changes/Codex CLI/2025-09-15-49-other-changes-in-rust-v0-36-0|49 other changes in rust-v0.36.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2025-09-09 · Open WebUI · [[Changes/Open WebUI/2025-09-09-6-account-and-access-changes-in-v0-6-27|6 Account and Access changes in v0.6.27]]
- Later: 2025-09-15 · ElevenLabs · [[Changes/ElevenLabs/2025-09-15-python-sdk|Python SDK]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Notion · [[Changes/Notion/2020-07-28-sign-into-notion-with-your-apple-id-the-perfect-combination-of-speedy-and-secure|Sign into Notion with your Apple ID 🗝️ The perfect combination of speedy and secure]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2025-09-15-e2e88e&body=Card%3A%20Changes%2FCodex%20CLI%2F2025-09-15-6-account-and-access-changes-in-rust-v0-36-0.md%0ACard%20ID%3A%20codex-cli-2025-09-15-e2e88e%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.36.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->