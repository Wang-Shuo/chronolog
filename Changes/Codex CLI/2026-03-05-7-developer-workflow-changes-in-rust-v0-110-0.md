---
card_id: codex-cli-2026-03-05-987e13
date: '2026-03-05'
description: 'Codex CLI · 2026-03-05 · Developer Workflow: 7 changes in 0.110.0 —
  Made sub-agents faster and more reliable by reusing shell state correctly and fixing…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter
    Colors]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2732
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 32bf1994258b4a4265895fb7efe133278036cbdcb5e14964c26202757f0179d6
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-03-05-987e13
  comparison: ''
  date: '2026-03-05'
  description: 'Codex CLI — 0.110.0: 7 Developer Workflow changes'
  evidence:
  - quote: 'Made sub-agents faster and more reliable by reusing shell state correctly
      and fixing `/status`, `Esc`, pending-message handling, and startup/profile race
      conditions. (#12935, #13052, #13130, #13131, #13235, #13240, #13248)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#13057 fix: use https://git.savannah.gnu.org/git/bash instead of https://github.com/bolinfest/bash
      @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#12642 fix(core) shell_snapshot multiline exports @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#12006 tui: preserve kill buffer across submit and slash-command clears
      @rakan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#13043 Collapse parsed command summaries when any stage is unknown @nornagon-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#13402 Ensure the env values of imported shell_environment_policy.set
      is string @alexsong-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  - quote: '#13458 [tui] Update Fast slash command description @pash-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.110.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 7-developer-workflow-changes-in-rust-v0-110-0
  source_release: codex-cli-2026-03-05-rust-v0-110-0-github-293239637-d5d06302
  source_type: github_releases
  theme: developer-workflow
  title: 7 Developer Workflow changes in rust-v0.110.0
  type: change
related_changes:
- '[[Changes/v0/2026-03-03-added-git-support-for-version-control-in-projects|Added
  Git support for version control in projects]]'
- '[[Changes/OpenCode/2026-03-04-5-developer-workflow-changes-in-v1-2-17|5 Developer
  Workflow changes in v1.2.17]]'
- '[[Changes/Claude Code/2026-03-05-6-developer-workflow-changes-in-v2-1-69|6 Developer
  Workflow changes in v2.1.69]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-03-05-rust-v0-110-0-github-293239637-d5d06302|codex-cli-2026-03-05-rust-v0-110-0-github-293239637-d5d06302]]'
source_type: github_releases
theme: developer-workflow
title: 7 Developer Workflow changes in rust-v0.110.0
type: change
---

<!-- chronolog:begin region="header" -->
# 7 Developer Workflow changes in rust-v0.110.0

**Codex CLI** · 2026-03-05 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.110.0) · from [[Releases/Codex CLI/codex-cli-2026-03-05-rust-v0-110-0-github-293239637-d5d06302|0.110.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Made sub-agents faster and more reliable by reusing shell state correctly and fixing `/status`, `Esc`, pending-message handling, and startup/profile race conditions. (#12935, #13052, #13130, #13131, #13235, #13240, #13248)

> #13057 fix: use https://git.savannah.gnu.org/git/bash instead of https://github.com/bolinfest/bash @bolinfest

> #12642 fix(core) shell_snapshot multiline exports @dylan-hurd-oai

> #12006 tui: preserve kill buffer across submit and slash-command clears @rakan-oai

> #13043 Collapse parsed command summaries when any stage is unknown @nornagon-openai

> #13402 Ensure the env values of imported shell_environment_policy.set is string @alexsong-oai

> #13458 [tui] Update Fast slash command description @pash-openai

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
- [[Changes/Codex CLI/2026-03-05-5-memory-and-personalization-changes-in-rust-v0-110-0|5 Memory and Personalization changes in rust-v0.110.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-03-05-4-safety-and-privacy-changes-in-rust-v0-110-0|4 Safety and Privacy changes in rust-v0.110.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-03-05-3-context-window-changes-in-rust-v0-110-0|3 Context Window changes in rust-v0.110.0]] · Context Window
- [[Changes/Codex CLI/2026-03-05-71-other-changes-in-rust-v0-110-0|71 other changes in rust-v0.110.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-03-05 · Claude Code · [[Changes/Claude Code/2026-03-05-6-developer-workflow-changes-in-v2-1-69|6 Developer Workflow changes in v2.1.69]]
- Later: 2026-03-05 · Codex CLI · [[Changes/Codex CLI/2026-03-05-13504-preserve-persisted-thread-git-info-in-resume-joeytrasatti-openai|♯13504 Preserve persisted thread git info in resume @joeytrasatti-openai]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-09-11 · Descript · [[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter Colors]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-03-05-987e13&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-03-05-7-developer-workflow-changes-in-rust-v0-110-0.md%0ACard%20ID%3A%20codex-cli-2026-03-05-987e13%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.110.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->