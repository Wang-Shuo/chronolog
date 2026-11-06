---
card_id: openhands-2026-09-25-5c50ca
date: '2026-09-25'
description: 'OpenHands · 2026-09-25 · Safety and Privacy: fix(mcp): keep OAuth credentials
  on cloud saves and skip consent when tokens still work by @hieptl in…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1258
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: change
machine_hash: f516cc50c220bd47f5b1892531acfc66f5aef72f2ac1c1b5b881c6c7a744ef20
product: openhands
product_name: OpenHands
record:
  card_id: openhands-2026-09-25-5c50ca
  comparison: ''
  date: '2026-09-25'
  description: 'OpenHands — v1.24.0: fix(mcp): keep OAuth credentials on cloud saves
    and skip consent when tokens still work by @hieptl in https://github.com/OpenHands/OpenHands/pull/17677'
  evidence:
  - quote: 'fix(mcp): keep OAuth credentials on cloud saves and skip consent when
      tokens still work by @hieptl in https://github.com/OpenHands/OpenHands/pull/17677'
    source_release: https://github.com/OpenHands/OpenHands/releases/tag/v1.24.0
  extractor_version: fallback-v5
  impact: incremental
  kind: change
  product: openhands
  product_name: OpenHands
  slug: fix-mcp-keep-oauth-credentials-on-cloud-saves-and-skip-consent-when-tokens-still
  source_release: openhands-2026-09-25-v1-24-0-github-396708686-384650c4
  source_type: github_releases
  theme: safety-privacy
  theme_matches:
  - matched_terms:
    - oauth
    score: 50
    theme: account-access
  - matched_terms:
    - mcp
    score: 50
    theme: apps-integrations
  - matched_terms:
    - tokens
    score: 50
    theme: context-window
  theme_resolution: manual-semantic-rule-v2
  title: 'fix(mcp): keep OAuth credentials on cloud saves and skip consent when tokens
    still work'
  type: change
related_changes:
- '[[Changes/ChatGPT/2026-09-25-we-re-introducing-security-history-a-new-way-to-review-recent-security-activity-6f32cc|Security
  history in ChatGPT]]'
- '[[Changes/Claude Code/2026-09-25-3-safety-and-privacy-changes-in-v2-1-283|3 Safety
  and Privacy changes in v2.1.283]]'
- '[[Changes/Codex CLI/2026-09-25-2-safety-and-privacy-changes-in-rust-v0-157-0|2
  Safety and Privacy changes in rust-v0.157.0]]'
source_release: '[[Releases/OpenHands/openhands-2026-09-25-v1-24-0-github-396708686-384650c4|openhands-2026-09-25-v1-24-0-github-396708686-384650c4]]'
source_type: github_releases
theme: safety-privacy
title: 'fix(mcp): keep OAuth credentials on cloud saves and skip consent when tokens
  still work'
type: change
---

<!-- chronolog:begin region="header" -->
# fix(mcp): keep OAuth credentials on cloud saves and skip consent when tokens still work

**OpenHands** · 2026-09-25 · [[Themes/safety-privacy|Safety and Privacy]] · [Official source](https://github.com/OpenHands/OpenHands/releases/tag/v1.24.0) · from [[Releases/OpenHands/openhands-2026-09-25-v1-24-0-github-396708686-384650c4|v1.24.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> fix(mcp): keep OAuth credentials on cloud saves and skip consent when tokens still work by @hieptl in https://github.com/OpenHands/OpenHands/pull/17677
>
> Source: https://github.com/OpenHands/OpenHands/releases/tag/v1.24.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenHands/2026-09-25-refactor-remove-test-conversation-id-fallbacks-in-websocket-context-add-state-up|refactor: remove test-conversation-id fallbacks in websocket context + add…]] · Context Window
- [[Changes/OpenHands/2026-09-25-chore-deps-bump-openhands-extensions-to-0-24-0-by-devinvinson-in-https-github-co|chore(deps): bump @openhands/extensions to 0.24.0]] · Apps and Integrations
- [[Changes/OpenHands/2026-09-25-docs-correct-outdated-cloud-proxy-rule-2-in-agents-md-by-juanmichelini-in-https|docs: correct outdated cloud-proxy Rule 2 in AGENTS.md]] · Agent Mode
- [[Changes/OpenHands/2026-09-25-feat-scope-openai-subscription-caches-by-backend-by-uczltw6-in-https-github-com|feat: scope OpenAI subscription caches by backend]] · Pricing Model
- [[Changes/OpenHands/2026-09-25-3-automation-and-scheduling-changes-in-v1-24-0|3 Automation and Scheduling changes in v1.24.0]] · Automation and Scheduling
- [[Changes/OpenHands/2026-09-25-9-other-changes-in-v1-24-0|9 other changes in v1.24.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-09-25 · Codex CLI · [[Changes/Codex CLI/2026-09-25-2-safety-and-privacy-changes-in-rust-v0-157-0|2 Safety and Privacy changes in rust-v0.157.0]]
- Later: 2026-09-28 · Claude Code · [[Changes/Claude Code/2026-09-28-4-safety-and-privacy-changes-in-v2-1-284|4 Safety and Privacy changes in v2.1.284]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openhands-2026-09-25-5c50ca&body=Card%3A%20Changes%2FOpenHands%2F2026-09-25-fix-mcp-keep-oauth-credentials-on-cloud-saves-and-skip-consent-when-tokens-still.md%0ACard%20ID%3A%20openhands-2026-09-25-5c50ca%0ASource%3A%20https%3A%2F%2Fgithub.com%2FOpenHands%2FOpenHands%2Freleases%2Ftag%2Fv1.24.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->