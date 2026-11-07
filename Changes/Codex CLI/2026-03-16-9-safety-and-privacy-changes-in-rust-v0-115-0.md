---
card_id: codex-cli-2026-03-16-cd8fdc
date: '2026-03-16'
description: 'Codex CLI · 2026-03-16 · Safety and Privacy: 9 changes in 0.115.0 —
  Spawned subagents now inherit sandbox and network rules more reliably, including…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke
    Application Access]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2057
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: db6b2f80d6bbd5522789dfdcf0dc1a3667654a83a1b368548e9322079b280558
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-03-16-cd8fdc
  comparison: ''
  date: '2026-03-16'
  description: 'Codex CLI — 0.115.0: 9 Safety and Privacy changes'
  evidence:
  - quote: 'Spawned subagents now inherit sandbox and network rules more reliably,
      including project-profile layering, persisted host approvals, and symlinked
      writable roots. (#14619, #14650, #14674, #14807)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14171 fix: align core approvals with split sandbox policies @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#13996 refactor: make bubblewrap the default Linux sandbox @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14440 fix: follow up on linux sandbox review nits @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14473 fix(cli): support legacy use_linux_sandbox_bwrap flag @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14173 fix: preserve split filesystem semantics in linux sandbox @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14400 Use a private desktop for Windows sandbox instead of Winsta0\Default
      @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14650 fix: sync split sandbox policies for spawned subagents @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  - quote: '#14674 fix: fix symlinked writable roots in sandbox policies @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.115.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 9-safety-and-privacy-changes-in-rust-v0-115-0
  source_release: codex-cli-2026-03-16-rust-v0-115-0-github-297641413-c704d9db
  source_type: github_releases
  theme: safety-privacy
  title: 9 Safety and Privacy changes in rust-v0.115.0
  type: change
related_changes:
- '[[Changes/OpenCode/2026-03-12-2-safety-and-privacy-changes-in-v1-2-25|2 Safety
  and Privacy changes in v1.2.25]]'
- '[[Changes/v0/2026-03-12-improved-snowflake-deployment-error-messages-for-permission-issues|Improved
  Snowflake deployment error messages for permission issues]]'
- '[[Changes/Claude Code/2026-03-14-3-safety-and-privacy-changes-in-v2-1-76|3 Safety
  and Privacy changes in v2.1.76]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-03-16-rust-v0-115-0-github-297641413-c704d9db|codex-cli-2026-03-16-rust-v0-115-0-github-297641413-c704d9db]]'
source_type: github_releases
theme: safety-privacy
title: 9 Safety and Privacy changes in rust-v0.115.0
type: change
---

<!-- chronolog:begin region="header" -->
# 9 Safety and Privacy changes in rust-v0.115.0

**Codex CLI** · 2026-03-16 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.115.0) · from [[Releases/Codex CLI/codex-cli-2026-03-16-rust-v0-115-0-github-297641413-c704d9db|0.115.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Spawned subagents now inherit sandbox and network rules more reliably, including project-profile layering, persisted host approvals, and symlinked writable roots. (#14619, #14650, #14674, #14807)

> #14171 fix: align core approvals with split sandbox policies @viyatb-oai

> #13996 refactor: make bubblewrap the default Linux sandbox @viyatb-oai

> #14440 fix: follow up on linux sandbox review nits @viyatb-oai

> #14473 fix(cli): support legacy use_linux_sandbox_bwrap flag @viyatb-oai

> #14173 fix: preserve split filesystem semantics in linux sandbox @viyatb-oai

> #14400 Use a private desktop for Windows sandbox instead of Winsta0\Default @iceweasel-oai

> #14650 fix: sync split sandbox policies for spawned subagents @viyatb-oai

> #14674 fix: fix symlinked writable roots in sandbox policies @viyatb-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.115.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-03-16-17-apps-and-integrations-changes-in-rust-v0-115-0|17 Apps and Integrations changes in rust-v0.115.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-03-16-2-context-window-changes-in-rust-v0-115-0|2 Context Window changes in rust-v0.115.0]] · Context Window
- [[Changes/Codex CLI/2026-03-16-16-agent-mode-changes-in-rust-v0-115-0|16 Agent Mode changes in rust-v0.115.0]] · Agent Mode
- [[Changes/Codex CLI/2026-03-16-2-mobile-and-desktop-changes-in-rust-v0-115-0|2 Mobile and Desktop changes in rust-v0.115.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-03-16-4-voice-and-audio-changes-in-rust-v0-115-0|4 Voice and Audio changes in rust-v0.115.0]] · Voice and Audio
- [[Changes/Codex CLI/2026-03-16-14493-memories-focus-write-prompts-on-user-preferences-andi-oai|♯14493 memories: focus write prompts on user preferences @andi-oai]] · Memory and Personalization
- [[Changes/Codex CLI/2026-03-16-5-model-support-changes-in-rust-v0-115-0|5 Model Support changes in rust-v0.115.0]] · Model Support
- [[Changes/Codex CLI/2026-03-16-2-account-and-access-changes-in-rust-v0-115-0|2 Account and Access changes in rust-v0.115.0]] · Account and Access
- [[Changes/Codex CLI/2026-03-16-2-developer-workflow-changes-in-rust-v0-115-0|2 Developer Workflow changes in rust-v0.115.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-03-16-14410-make-collab-model-metadata-accurate-on-completion-aibrahim-oai|♯14410 Make collab model metadata accurate on completion @aibrahim-oai]] · Interface Experience
- [[Changes/Codex CLI/2026-03-16-70-other-changes-in-rust-v0-115-0|70 other changes in rust-v0.115.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-03-14 · Claude Code · [[Changes/Claude Code/2026-03-14-3-safety-and-privacy-changes-in-v2-1-76|3 Safety and Privacy changes in v2.1.76]]
- Later: 2026-03-16 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-03-16-extension-tools-now-work-with-the-permissions-system-use-skippermission-per-tool|Extension tools now work with the permissions system, use skipPermission per-tool…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Descript · [[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke Application Access]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-03-16-cd8fdc&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-03-16-9-safety-and-privacy-changes-in-rust-v0-115-0.md%0ACard%20ID%3A%20codex-cli-2026-03-16-cd8fdc%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.115.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->