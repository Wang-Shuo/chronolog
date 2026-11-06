---
card_id: codex-cli-2026-10-07-27a267
date: '2026-10-07'
description: 'Codex CLI · 2026-10-07 · Safety and Privacy: 9 changes in 0.161.0 —
  #49261 Preserve Windows sandbox runner launch errors @zm-oai'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1270
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 15e903251d980a2abdd670142b9253fc1da210f97b1ba62cad26b083cf4a280f
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-10-07-27a267
  comparison: ''
  date: '2026-10-07'
  description: 'Codex CLI — 0.161.0: 9 Safety and Privacy changes'
  evidence:
  - quote: '#49261 Preserve Windows sandbox runner launch errors @zm-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49308 Run piped legacy Windows sandbox processes without a console @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49325 Retry Windows sandbox runner logon once on error 1056 @zm-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49389 Serialize tests that share Windows sandbox accounts @jgershen-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49642 Allow managed requirements to disable the Windows MXC sandbox @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49690 Preserve PowerShell relative paths in the elevated Windows sandbox
      @johnl-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49715 Add account security setup reminders to the TUI @dennyku'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49781 Include the environment''s MXC backend in MCP sandbox metadata
      @zm-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  - quote: '#49880 Bind permission grants to the originating turn @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.161.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 9-safety-and-privacy-changes-in-rust-v0-161-0
  source_release: codex-cli-2026-10-07-rust-v0-161-0-github-405921402-d1f93f55
  source_type: github_releases
  theme: safety-privacy
  title: 9 Safety and Privacy changes in rust-v0.161.0
  type: change
related_changes:
- '[[Changes/Claude Code/2026-10-06-fixed-a-regression-in-2-1-290-where-cloud-sessions-could-drop-answers-to-permiss|Fixed
  a regression in 2.1.290 where cloud sessions could drop answers to permission…]]'
- '[[Changes/OpenHands/2026-10-06-fix-consume-consent-aware-website-posthog-handoff-by-malhotra5-in-https-github-c|fix:
  consume consent-aware website PostHog handoff]]'
- '[[Changes/Claude Code/2026-10-07-3-safety-and-privacy-changes-in-v2-1-293|3 Safety
  and Privacy changes in v2.1.293]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-10-07-rust-v0-161-0-github-405921402-d1f93f55|codex-cli-2026-10-07-rust-v0-161-0-github-405921402-d1f93f55]]'
source_type: github_releases
theme: safety-privacy
title: 9 Safety and Privacy changes in rust-v0.161.0
type: change
---

<!-- chronolog:begin region="header" -->
# 9 Safety and Privacy changes in rust-v0.161.0

**Codex CLI** · 2026-10-07 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.161.0) · from [[Releases/Codex CLI/codex-cli-2026-10-07-rust-v0-161-0-github-405921402-d1f93f55|0.161.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> #49261 Preserve Windows sandbox runner launch errors @zm-oai

> #49308 Run piped legacy Windows sandbox processes without a console @etraut-openai

> #49325 Retry Windows sandbox runner logon once on error 1056 @zm-oai

> #49389 Serialize tests that share Windows sandbox accounts @jgershen-oai

> #49642 Allow managed requirements to disable the Windows MXC sandbox @iceweasel-oai

> #49690 Preserve PowerShell relative paths in the elevated Windows sandbox @johnl-oai

> #49715 Add account security setup reminders to the TUI @dennyku

> #49781 Include the environment's MXC backend in MCP sandbox metadata @zm-oai

> #49880 Bind permission grants to the originating turn @anp-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.161.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-10-07-10-developer-workflow-changes-in-rust-v0-161-0|10 Developer Workflow changes in rust-v0.161.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-10-07-3-search-and-browsing-changes-in-rust-v0-161-0|3 Search and Browsing changes in rust-v0.161.0]] · Search and Browsing
- [[Changes/Codex CLI/2026-10-07-5-apps-and-integrations-changes-in-rust-v0-161-0|5 Apps and Integrations changes in rust-v0.161.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-10-07-49856-support-daybreak-selection-in-codex-exec-etraut-openai|♯49856 Support Daybreak selection in codex exec @etraut-openai]] · Interface Experience
- [[Changes/Codex CLI/2026-10-07-9-model-support-changes-in-rust-v0-161-0|9 Model Support changes in rust-v0.161.0]] · Model Support
- [[Changes/Codex CLI/2026-10-07-49876-remove-personality-plumbing-from-the-tui-etraut-openai|♯49876 Remove personality plumbing from the TUI @etraut-openai]] · Memory and Personalization
- [[Changes/Codex CLI/2026-10-07-49473-use-the-rmcp-sdk-for-enterprise-managed-token-exchanges-nicksteele-oai|♯49473 Use the rmcp SDK for enterprise-managed token exchanges @nicksteele-oai]] · Enterprise and Administration
- [[Changes/Codex CLI/2026-10-07-10-account-and-access-changes-in-rust-v0-161-0|10 Account and Access changes in rust-v0.161.0]] · Account and Access
- [[Changes/Codex CLI/2026-10-07-9-agent-mode-changes-in-rust-v0-161-0|9 Agent Mode changes in rust-v0.161.0]] · Agent Mode
- [[Changes/Codex CLI/2026-10-07-4-voice-and-audio-changes-in-rust-v0-161-0|4 Voice and Audio changes in rust-v0.161.0]] · Voice and Audio
- [[Changes/Codex CLI/2026-10-07-9-context-window-changes-in-rust-v0-161-0|9 Context Window changes in rust-v0.161.0]] · Context Window
- [[Changes/Codex CLI/2026-10-07-2-collaboration-changes-in-rust-v0-161-0|2 Collaboration changes in rust-v0.161.0]] · Collaboration
- [[Changes/Codex CLI/2026-10-07-93-other-changes-in-rust-v0-161-0|93 other changes in rust-v0.161.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-10-07 · Claude Code · [[Changes/Claude Code/2026-10-07-3-safety-and-privacy-changes-in-v2-1-293|3 Safety and Privacy changes in v2.1.293]]
- Later: 2026-10-07 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-10-07-2-safety-and-privacy-changes-in-v1-0-93|2 Safety and Privacy changes in v1.0.93]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-10-07-27a267&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-10-07-9-safety-and-privacy-changes-in-rust-v0-161-0.md%0ACard%20ID%3A%20codex-cli-2026-10-07-27a267%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.161.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->