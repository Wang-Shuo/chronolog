---
card_id: codex-cli-2026-03-05-e024bd
date: '2026-03-05'
description: 'Codex CLI · 2026-03-05 · Safety and Privacy: 4 changes in 0.110.0 —
  #13061 chore: remove SkillMetadata.permissions and derive skill sandboxing from…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1054
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: c07f2b0fb1d465cf8fa523212471388d58525c55d885eb75b35c7527df723b52
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-03-05-e024bd
  comparison: ''
  date: '2026-03-05'
  description: 'Codex CLI — 0.110.0: 4 Safety and Privacy changes'
  evidence:
  - quote: '#13061 chore: remove SkillMetadata.permissions and derive skill sandboxing
      from permission_profile @celia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#13413 copy command-runner to CODEX_HOME so sandbox users can always execute
      it @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#13409 Feat: Preserve network access on read-only sandbox policies @celia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#13484 allow apps to specify cwd for sandbox setup. @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 4-safety-and-privacy-changes-in-rust-v0-110-0
  source_release: codex-cli-2026-03-05-rust-v0-110-0-github-293239637-d5d06302
  source_type: github_releases
  theme: safety-privacy
  title: 4 Safety and Privacy changes in rust-v0.110.0
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-03-03-autopilot-permission-dialog-appears-on-first-prompt-submission-instead-of-on-mod|Autopilot
  permission dialog appears on first prompt submission instead of on mode switch]]'
- '[[Changes/v0/2026-03-03-fixed-integration-permission-checks-for-team-roles|Fixed
  integration permission checks for team roles]]'
- '[[Changes/Claude Code/2026-03-05-5-safety-and-privacy-changes-in-v2-1-69|5 Safety
  and Privacy changes in v2.1.69]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-03-05-rust-v0-110-0-github-293239637-d5d06302|codex-cli-2026-03-05-rust-v0-110-0-github-293239637-d5d06302]]'
source_type: github_releases
theme: safety-privacy
title: 4 Safety and Privacy changes in rust-v0.110.0
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Safety and Privacy changes in rust-v0.110.0

**Codex CLI** · 2026-03-05 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.110.0) · from [[Releases/Codex CLI/codex-cli-2026-03-05-rust-v0-110-0-github-293239637-d5d06302|0.110.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> #13061 chore: remove SkillMetadata.permissions and derive skill sandboxing from permission_profile @celia-oai

> #13413 copy command-runner to CODEX_HOME so sandbox users can always execute it @iceweasel-oai

> #13409 Feat: Preserve network access on read-only sandbox policies @celia-oai

> #13484 allow apps to specify cwd for sandbox setup. @iceweasel-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.110.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-03-05-12935-speed-up-subagent-startup-daveaitel-openai|♯12935 Speed up subagent startup @daveaitel-openai]] · Reliability and Performance
- [[Changes/Codex CLI/2026-03-05-2-model-support-changes-in-rust-v0-110-0|2 Model Support changes in rust-v0.110.0]] · Model Support
- [[Changes/Codex CLI/2026-03-05-13127-nit-disable-on-windows-jif-oai|♯13127 nit: disable on windows @jif-oai]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-03-05-13-agent-mode-changes-in-rust-v0-110-0|13 Agent Mode changes in rust-v0.110.0]] · Agent Mode
- [[Changes/Codex CLI/2026-03-05-13313-renaming-team-to-business-plan-during-tui-onboarding-bwanner-oai|♯13313 Renaming Team to Business plan during TUI onboarding @bwanner-oai]] · Interface Experience
- [[Changes/Codex CLI/2026-03-05-12383-add-new-scopes-to-login-adaley-openai|♯12383 add new scopes to login @adaley-openai]] · Account and Access
- [[Changes/Codex CLI/2026-03-05-4-files-and-data-changes-in-rust-v0-110-0|4 Files and Data changes in rust-v0.110.0]] · Files and Data
- [[Changes/Codex CLI/2026-03-05-13388-config-enforce-enterprise-feature-requirements-bolinfest|♯13388 config: enforce enterprise feature requirements @bolinfest]] · Enterprise and Administration
- [[Changes/Codex CLI/2026-03-05-7-apps-and-integrations-changes-in-rust-v0-110-0|7 Apps and Integrations changes in rust-v0.110.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-03-05-7-developer-workflow-changes-in-rust-v0-110-0|7 Developer Workflow changes in rust-v0.110.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-03-05-5-memory-and-personalization-changes-in-rust-v0-110-0|5 Memory and Personalization changes in rust-v0.110.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-03-05-3-context-window-changes-in-rust-v0-110-0|3 Context Window changes in rust-v0.110.0]] · Context Window
- [[Changes/Codex CLI/2026-03-05-71-other-changes-in-rust-v0-110-0|71 other changes in rust-v0.110.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-03-05 · Claude Code · [[Changes/Claude Code/2026-03-05-5-safety-and-privacy-changes-in-v2-1-69|5 Safety and Privacy changes in v2.1.69]]
- Later: 2026-03-05 · Cursor · [[Changes/Cursor/2026-03-05-when-invoked-the-agent-spins-up-a-cloud-sandbox-and-follows-your-instructions-us|When invoked, the agent spins up a cloud sandbox and follows your instructions using…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-03-05-e024bd&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-03-05-4-safety-and-privacy-changes-in-rust-v0-110-0.md%0ACard%20ID%3A%20codex-cli-2026-03-05-e024bd%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.110.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->