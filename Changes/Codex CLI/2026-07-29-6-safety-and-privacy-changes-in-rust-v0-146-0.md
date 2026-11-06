---
card_id: codex-cli-2026-07-29-cce20d
date: '2026-07-29'
description: 'Codex CLI · 2026-07-29 · Safety and Privacy: 6 changes in 0.146.0 —
  #34598 Skip missing paths in filesystem sandbox entries @copyberry'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1200
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 480a93de0ac7e11bf9066106de536883220d719cf4b4a0c5a5945c42d554e664
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-07-29-cce20d
  comparison: ''
  date: '2026-07-29'
  description: 'Codex CLI — 0.146.0: 6 Safety and Privacy changes'
  evidence:
  - quote: '#34598 Skip missing paths in filesystem sandbox entries @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34613 Route Windows sandbox proxy traffic by restricting SID @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34615 Initialize missing-path behavior in exec-server sandbox test @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34629 Harden Windows elevated sandbox startup @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#34811 Fix network access rendering in sandbox prompts @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  - quote: '#35036 Preserve Windows sandbox proxy settings in guardian sessions @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.146.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 6-safety-and-privacy-changes-in-rust-v0-146-0
  source_release: codex-cli-2026-07-29-rust-v0-146-0-github-361463950-6d491983
  source_type: github_releases
  theme: safety-privacy
  title: 6 Safety and Privacy changes in rust-v0.146.0
  type: change
related_changes:
- '[[Changes/Open WebUI/2026-07-27-13-safety-and-privacy-changes-in-v0-11-0|13 Safety
  and Privacy changes in v0.11.0]]'
- '[[Changes/Dify/2026-07-28-11-safety-and-privacy-changes-in-1-16-1|11 Safety and
  Privacy changes in 1.16.1]]'
- '[[Changes/Gemini CLI/2026-07-28-fix-a2a-server-enforce-workspace-trust-and-task-isolation-to-prevent-rce-by-luis|fix(a2a-server):
  enforce workspace trust and task isolation to prevent RCE]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-07-29-rust-v0-146-0-github-361463950-6d491983|codex-cli-2026-07-29-rust-v0-146-0-github-361463950-6d491983]]'
source_type: github_releases
theme: safety-privacy
title: 6 Safety and Privacy changes in rust-v0.146.0
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Safety and Privacy changes in rust-v0.146.0

**Codex CLI** · 2026-07-29 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.146.0) · from [[Releases/Codex CLI/codex-cli-2026-07-29-rust-v0-146-0-github-361463950-6d491983|0.146.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> #34598 Skip missing paths in filesystem sandbox entries @copyberry

> #34613 Route Windows sandbox proxy traffic by restricting SID @copyberry

> #34615 Initialize missing-path behavior in exec-server sandbox test @copyberry

> #34629 Harden Windows elevated sandbox startup @copyberry

> #34811 Fix network access rendering in sandbox prompts @copyberry

> #35036 Preserve Windows sandbox proxy settings in guardian sessions @copyberry

Source: https://github.com/openai/codex/releases/tag/rust-v0.146.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-07-29-47-apps-and-integrations-changes-in-rust-v0-146-0|47 Apps and Integrations changes in rust-v0.146.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-07-29-2-search-and-browsing-changes-in-rust-v0-146-0|2 Search and Browsing changes in rust-v0.146.0]] · Search and Browsing
- [[Changes/Codex CLI/2026-07-29-2-mobile-and-desktop-changes-in-rust-v0-146-0|2 Mobile and Desktop changes in rust-v0.146.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-07-29-34850-disable-image-generation-for-free-plan-accounts-copyberry|♯34850 Disable image generation for Free-plan accounts @copyberry]] · Image Generation
- [[Changes/Codex CLI/2026-07-29-3-collaboration-changes-in-rust-v0-146-0|3 Collaboration changes in rust-v0.146.0]] · Collaboration
- [[Changes/Codex CLI/2026-07-29-3-model-support-changes-in-rust-v0-146-0|3 Model Support changes in rust-v0.146.0]] · Model Support
- [[Changes/Codex CLI/2026-07-29-5-context-window-changes-in-rust-v0-146-0|5 Context Window changes in rust-v0.146.0]] · Context Window
- [[Changes/Codex CLI/2026-07-29-35530-track-model-and-personality-in-world-state-copyberry|♯35530 Track model and personality in world state @copyberry]] · Memory and Personalization
- [[Changes/Codex CLI/2026-07-29-34643-migrate-login-http-construction-to-httpclient-copyberry|♯34643 Migrate login HTTP construction to HttpClient @copyberry]] · Account and Access
- [[Changes/Codex CLI/2026-07-29-8-interface-experience-changes-in-rust-v0-146-0|8 Interface Experience changes in rust-v0.146.0]] · Interface Experience
- [[Changes/Codex CLI/2026-07-29-12-developer-workflow-changes-in-rust-v0-146-0|12 Developer Workflow changes in rust-v0.146.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-07-29-11-agent-mode-changes-in-rust-v0-146-0|11 Agent Mode changes in rust-v0.146.0]] · Agent Mode
- [[Changes/Codex CLI/2026-07-29-3-editor-experience-changes-in-rust-v0-146-0|3 Editor Experience changes in rust-v0.146.0]] · Editor Experience
- [[Changes/Codex CLI/2026-07-29-2-enterprise-and-administration-changes-in-rust-v0-146-0|2 Enterprise and Administration changes in rust-v0.146.0]] · Enterprise and Administration
- [[Changes/Codex CLI/2026-07-29-2-files-and-data-changes-in-rust-v0-146-0|2 Files and Data changes in rust-v0.146.0]] · Files and Data
- [[Changes/Codex CLI/2026-07-29-129-other-changes-in-rust-v0-146-0|129 other changes in rust-v0.146.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-07-28 · Gemini CLI · [[Changes/Gemini CLI/2026-07-28-fix-a2a-server-enforce-workspace-trust-and-task-isolation-to-prevent-rce-by-luis|fix(a2a-server): enforce workspace trust and task isolation to prevent RCE]]
- Later: 2026-07-29 · Lovable · [[Changes/Lovable/2026-07-29-fewer-false-alarms-in-dependency-scans|Fewer false alarms in dependency scans]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-07-29-cce20d&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-07-29-6-safety-and-privacy-changes-in-rust-v0-146-0.md%0ACard%20ID%3A%20codex-cli-2026-07-29-cce20d%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.146.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->