---
card_id: codex-cli-2025-10-06-d133c2
date: '2025-10-06'
description: 'Codex CLI · 2025-10-06 · Safety and Privacy: `codex login --api-key`
  was replaced with `codex login --with-api-key` that reads the key from `stdin` to
  improve…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke
    Application Access]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1896
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: change
machine_hash: 60cadf2bc1cd60dc56019ec8e3ac2d107b658828e55ffcbc45abcb0ee829fd2a
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2025-10-06-d133c2
  comparison: ''
  date: '2025-10-06'
  description: 'Codex CLI — 0.45.0: `codex login --api-key` was replaced with `codex
    login --with-api-key` that reads the key from `stdin` to improve security.'
  evidence:
  - quote: '`codex login --api-key` was replaced with `codex login --with-api-key`
      that reads the key from `stdin` to improve security.'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.45.0
  extractor_version: fallback-v5
  impact: incremental
  kind: change
  product: codex-cli
  product_name: Codex CLI
  slug: codex-login-api-key-was-replaced-with-codex-login-with-api-key-that-reads-the-ke
  source_release: codex-cli-2025-10-06-rust-v0-45-0-github-252516377-0c83cb4a
  source_type: github_releases
  theme: safety-privacy
  theme_matches:
  - matched_terms:
    - login
    score: 50
    theme: account-access
  - matched_terms:
    - security
    score: 50
    theme: safety-privacy
  theme_resolution: manual-semantic-rule-v1
  title: '`codex login --api-key` was replaced with `codex login --with-api-key` that
    reads…'
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2025-10-01-improved-how-we-extract-paths-from-shell-commands-for-permission-handling-might|Improved
  how we extract paths from shell commands for permission handling…]]'
- '[[Changes/OpenHands/2025-10-01-significantly-improved-the-security-of-the-openhands-enterprise-docker-image-by|Significantly
  improved the security of the OpenHands enterprise Docker image…]]'
- '[[Changes/Codex CLI/2025-10-03-3-safety-and-privacy-changes-in-rust-v0-44-0|3 Safety
  and Privacy changes in rust-v0.44.0]]'
source_release: '[[Releases/Codex CLI/codex-cli-2025-10-06-rust-v0-45-0-github-252516377-0c83cb4a|codex-cli-2025-10-06-rust-v0-45-0-github-252516377-0c83cb4a]]'
source_type: github_releases
theme: safety-privacy
title: codex login --api-key was replaced with codex login --with-api-key that reads…
type: change
---

<!-- chronolog:begin region="header" -->
# `codex login --api-key` was replaced with `codex login --with-api-key` that reads…

**Codex CLI** · 2025-10-06 · [[Themes/safety-privacy|Safety and Privacy]] · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.45.0) · from [[Releases/Codex CLI/codex-cli-2025-10-06-rust-v0-45-0-github-252516377-0c83cb4a|0.45.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> `codex login --api-key` was replaced with `codex login --with-api-key` that reads the key from `stdin` to improve security.
>
> Source: https://github.com/openai/codex/releases/tag/rust-v0.45.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2025-10-06-4673-fix-colors-when-refocusing-the-terminal-after-a-system-theme-update|♯4673 Fix colors when refocusing the terminal after a system theme update]] · Developer Workflow
- [[Changes/Codex CLI/2025-10-06-2-model-support-changes-in-rust-v0-45-0|2 Model Support changes in rust-v0.45.0]] · Model Support
- [[Changes/Codex CLI/2025-10-06-4706-fix-command-output-truncation-that-sometimes-used-too-much-of-the-context-w|♯4706 Fix command output truncation that sometimes used too much of the context window]] · Context Window
- [[Changes/Codex CLI/2025-10-06-3-account-and-access-changes-in-rust-v0-45-0|3 Account and Access changes in rust-v0.45.0]] · Account and Access
- [[Changes/Codex CLI/2025-10-06-5-other-changes-in-rust-v0-45-0|5 other changes in rust-v0.45.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2025-10-03 · Codex CLI · [[Changes/Codex CLI/2025-10-03-3-safety-and-privacy-changes-in-rust-v0-44-0|3 Safety and Privacy changes in rust-v0.44.0]]
- Later: 2025-10-06 · Lovable · [[Changes/Lovable/2025-10-06-better-workspace-management|Better workspace management]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Descript · [[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke Application Access]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2025-10-06-d133c2&body=Card%3A%20Changes%2FCodex%20CLI%2F2025-10-06-codex-login-api-key-was-replaced-with-codex-login-with-api-key-that-reads-the-ke.md%0ACard%20ID%3A%20codex-cli-2025-10-06-d133c2%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.45.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->