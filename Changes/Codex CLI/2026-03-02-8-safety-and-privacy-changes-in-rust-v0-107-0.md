---
card_id: codex-cli-2026-03-02-f9a86c
date: '2026-03-02'
description: 'Codex CLI · 2026-03-02 · Safety and Privacy: 8 changes in 0.107.0 —
  Updated sandbox escalation guidance so dependency-install failures caused by sandboxed…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1051
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: c77eff570d1bbc70c0f68b22bcc4838508b2b8a60e0baa36b9b7f902f675eb96
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-03-02-f9a86c
  comparison: ''
  date: '2026-03-02'
  description: 'Codex CLI — 0.107.0: 8 Safety and Privacy changes'
  evidence:
  - quote: Updated sandbox escalation guidance so dependency-install failures caused
      by sandboxed network access are more clearly treated as escalation candidates.
      (#13051)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.107.0
  - quote: 'Tightened sandbox filesystem behavior by improving restricted read-only
      handling on Linux and avoiding sensitive directories like `~/.ssh` on Windows.
      (#12369, #12835)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.107.0
  - quote: Escalated shell commands now keep their sandbox configuration when rerun,
      closing a gap where approvals could lose the intended restrictions. (#12839)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.107.0
  - quote: '#12835 don''t grant sandbox read access to ~/.ssh and a few other dirs.
      @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.107.0
  - quote: '#12839 feat: include sandbox config with escalation request @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.107.0
  - quote: '#12970 fix: use AbsolutePathBuf for permission profile file roots @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.107.0
  - quote: '#13051 Clarify escalation guidance for sandbox-related network failures
      @daniel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.107.0
  - quote: '#12369 feat(linux-sandbox): support restricted ReadOnlyAccess in bwrap
      @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.107.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 8-safety-and-privacy-changes-in-rust-v0-107-0
  source_release: codex-cli-2026-03-02-rust-v0-107-0-github-292187522-c29f3a8f
  source_type: github_releases
  theme: safety-privacy
  title: 8 Safety and Privacy changes in rust-v0.107.0
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-02-26-12800-fix-enforce-sandbox-envelope-for-zsh-fork-execution-bolinfest|♯12800
  fix: enforce sandbox envelope for zsh fork execution @bolinfest]]'
- '[[Changes/Gemini CLI/2026-02-27-6-safety-and-privacy-changes-in-v0-31-0|6 Safety
  and Privacy changes in v0.31.0]]'
- '[[Changes/Claude Code/2026-02-28-fixed-listener-leak-in-interactive-permission-handler-during-auto-approvals|Fixed
  listener leak in interactive permission handler during auto-approvals]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-03-02-rust-v0-107-0-github-292187522-c29f3a8f|codex-cli-2026-03-02-rust-v0-107-0-github-292187522-c29f3a8f]]'
source_type: github_releases
theme: safety-privacy
title: 8 Safety and Privacy changes in rust-v0.107.0
type: change
---

<!-- chronolog:begin region="header" -->
# 8 Safety and Privacy changes in rust-v0.107.0

**Codex CLI** · 2026-03-02 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.107.0) · from [[Releases/Codex CLI/codex-cli-2026-03-02-rust-v0-107-0-github-292187522-c29f3a8f|0.107.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Updated sandbox escalation guidance so dependency-install failures caused by sandboxed network access are more clearly treated as escalation candidates. (#13051)

> Tightened sandbox filesystem behavior by improving restricted read-only handling on Linux and avoiding sensitive directories like `~/.ssh` on Windows. (#12369, #12835)

> Escalated shell commands now keep their sandbox configuration when rerun, closing a gap where approvals could lose the intended restrictions. (#12839)

> #12835 don't grant sandbox read access to ~/.ssh and a few other dirs. @iceweasel-oai

> #12839 feat: include sandbox config with escalation request @bolinfest

> #12970 fix: use AbsolutePathBuf for permission profile file roots @bolinfest

> #13051 Clarify escalation guidance for sandbox-related network failures @daniel-oai

> #12369 feat(linux-sandbox): support restricted ReadOnlyAccess in bwrap @viyatb-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.107.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-03-02-2-multimodal-input-changes-in-rust-v0-107-0|2 Multimodal Input changes in rust-v0.107.0]] · Multimodal Input
- [[Changes/Codex CLI/2026-03-02-you-can-now-fork-a-thread-into-sub-agents-making-it-easier-to-branch-work-withou|Fork a thread into sub-agents, making it easier to branch work without leaving…]] · Agent Mode
- [[Changes/Codex CLI/2026-03-02-3-apps-and-integrations-changes-in-rust-v0-107-0|3 Apps and Integrations changes in rust-v0.107.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-03-02-3-account-and-access-changes-in-rust-v0-107-0|3 Account and Access changes in rust-v0.107.0]] · Account and Access
- [[Changes/Codex CLI/2026-03-02-3-developer-workflow-changes-in-rust-v0-107-0|3 Developer Workflow changes in rust-v0.107.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-03-02-12947-feat-add-local-date-timezone-to-turn-environment-context-celia-oai|♯12947 feat: add local date/timezone to turn environment context @celia-oai]] · Context Window
- [[Changes/Codex CLI/2026-03-02-2-agent-mode-changes-in-rust-v0-107-0|2 Agent Mode changes in rust-v0.107.0]] · Agent Mode
- [[Changes/Codex CLI/2026-03-02-4-model-support-changes-in-rust-v0-107-0|4 Model Support changes in rust-v0.107.0]] · Model Support
- [[Changes/Codex CLI/2026-03-02-3-editor-experience-changes-in-rust-v0-107-0|3 Editor Experience changes in rust-v0.107.0]] · Editor Experience
- [[Changes/Codex CLI/2026-03-02-6-memory-and-personalization-changes-in-rust-v0-107-0|6 Memory and Personalization changes in rust-v0.107.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-03-02-5-voice-and-audio-changes-in-rust-v0-107-0|5 Voice and Audio changes in rust-v0.107.0]] · Voice and Audio
- [[Changes/Codex CLI/2026-03-02-24-other-changes-in-rust-v0-107-0|24 other changes in rust-v0.107.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-02-28 · Claude Code · [[Changes/Claude Code/2026-02-28-fixed-listener-leak-in-interactive-permission-handler-during-auto-approvals|Fixed listener leak in interactive permission handler during auto-approvals]]
- Later: 2026-03-03 · Cursor · [[Changes/Cursor/2026-03-03-fixed-team-permission-and-access-control-inconsistencies-across-organization-set|Fixed team permission and access control inconsistencies across organization setups]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-03-02-f9a86c&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-03-02-8-safety-and-privacy-changes-in-rust-v0-107-0.md%0ACard%20ID%3A%20codex-cli-2026-03-02-f9a86c%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.107.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->