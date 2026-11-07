---
card_id: codex-cli-2026-01-15-08a42f
date: '2026-01-15'
description: 'Codex CLI · 2026-01-15 · Safety and Privacy: [revert] Linux sandboxing
  now falls back to Landlock-only restrictions when user namespaces are unavailable,
  and…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke
    Application Access]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1997
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: significant
kind: change
machine_hash: 36614ad6cc9b6aa6ab426cfe92f0cd2a424d91c9e8eeec5cd9766ef013d985f8
product: codex-cli
product_name: Codex CLI
record:
  ai_generated: true
  card_id: codex-cli-2026-01-15-08a42f
  comparison: ''
  confidence: low
  date: '2026-01-15'
  description: 'Codex CLI — 0.85.0: [revert] Linux sandboxing now falls back to Landlock-only
    restrictions when user namespaces are unavailable, and sets `no_new_privs` before
    applying sandbox rules. (#9250)'
  evidence:
  - quote: '[revert] Linux sandboxing now falls back to Landlock-only restrictions
      when user namespaces are unavailable, and sets `no_new_privs` before applying
      sandbox rules. (#9250)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.85.0
  extractor_version: fallback-v5
  impact: significant
  kind: change
  product: codex-cli
  product_name: Codex CLI
  slug: revert-linux-sandboxing-now-falls-back-to-landlock-only-restrictions-when-user-n
  source_release: codex-cli-2026-01-15-rust-v0-85-0-github-277157618-2b62da73
  source_type: github_releases
  theme: safety-privacy
  theme_matches: []
  theme_resolution: manual-semantic-rule-v2
  title: '[revert] Linux sandboxing now falls back to Landlock-only restrictions when
    user…'
  type: change
related_changes:
- '[[Changes/Gemini CLI/2026-01-14-7-safety-and-privacy-changes-in-v0-24-0|7 Safety
  and Privacy changes in v0.24.0]]'
- '[[Changes/HeyGen/2026-01-14-what-s-new-a-new-guided-flow-lets-you-create-your-avatar-with-a-single-15-second|What''s
  new: A new guided flow lets you create your avatar with a single 15-second…]]'
- '[[Changes/OpenCode/2026-01-14-terminal-tweak-external-directory-permission-rendering-in-tui|Terminal
  Tweak external directory permission rendering in TUI]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-01-15-rust-v0-85-0-github-277157618-2b62da73|codex-cli-2026-01-15-rust-v0-85-0-github-277157618-2b62da73]]'
source_type: github_releases
theme: safety-privacy
title: revert Linux sandboxing now falls back to Landlock-only restrictions when user…
type: change
---

<!-- chronolog:begin region="header" -->
# [revert] Linux sandboxing now falls back to Landlock-only restrictions when user…

**Codex CLI** · 2026-01-15 · [[Themes/safety-privacy|Safety and Privacy]] · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.85.0) · from [[Releases/Codex CLI/codex-cli-2026-01-15-rust-v0-85-0-github-277157618-2b62da73|0.85.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> [revert] Linux sandboxing now falls back to Landlock-only restrictions when user namespaces are unavailable, and sets `no_new_privs` before applying sandbox rules. (#9250)
>
> Source: https://github.com/openai/codex/releases/tag/rust-v0.85.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-01-15-9207-propagate-mcp-disabled-reason-gt-oai|♯9207 Propagate MCP disabled reason @gt-oai]] · Apps and Integrations
- [[Changes/Codex CLI/2026-01-15-2-collaboration-changes-in-rust-v0-85-0|2 Collaboration changes in rust-v0.85.0]] · Collaboration
- [[Changes/Codex CLI/2026-01-15-9275-feat-add-agent-roles-to-collab-tools-jif-oai|♯9275 feat: add agent roles to collab tools @jif-oai]] · Agent Mode
- [[Changes/Codex CLI/2026-01-15-2-model-support-changes-in-rust-v0-85-0|2 Model Support changes in rust-v0.85.0]] · Model Support
- [[Changes/Codex CLI/2026-01-15-9-other-changes-in-rust-v0-85-0|9 other changes in rust-v0.85.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-01-14 · OpenCode · [[Changes/OpenCode/2026-01-14-terminal-tweak-external-directory-permission-rendering-in-tui|Terminal Tweak external directory permission rendering in TUI]]
- Later: 2026-01-16 · Lovable · [[Changes/Lovable/2026-01-16-dependency-vulnerability-scanning-is-now-available-with-issues-in-project-depend|Dependency vulnerability scanning is now available, with issues in project…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Descript · [[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke Application Access]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-01-15-08a42f&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-01-15-revert-linux-sandboxing-now-falls-back-to-landlock-only-restrictions-when-user-n.md%0ACard%20ID%3A%20codex-cli-2026-01-15-08a42f%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.85.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->