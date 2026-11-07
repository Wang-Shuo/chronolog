---
card_id: codex-cli-2026-04-30-d184bd
date: '2026-04-30'
description: 'Codex CLI · 2026-04-30 · Safety and Privacy: 21 changes in 0.128.0 —
  Expanded permission profiles with built-in defaults, sandbox CLI profile selection,
  cwd…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1110
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 923f9ccbdee3183534068a0d4159e98430a0ae25d7ccb2b2fdbda254a663a574
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-04-30-d184bd
  comparison: ''
  date: '2026-04-30'
  description: 'Codex CLI — 0.128.0: 21 Safety and Privacy changes'
  evidence:
  - quote: 'Expanded permission profiles with built-in defaults, sandbox CLI profile
      selection, cwd controls, and active-profile metadata for clients. (#19900, #20117,
      #20118, #20095)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: Deprecated `--full-auto` while steering users toward explicit permission
      profiles and trust flows. (#20133)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19453 Serialize legacy Windows PowerShell sandbox tests @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19393 permissions: migrate approval and sandbox consumers to profiles
      @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19739 inline hostname resolution for remote sandbox config @abhinav-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19734 permissions: centralize legacy sandbox projection @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19735 permissions: store only constrained permission profiles @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19775 permissions: derive snapshot sandbox projections @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19899 app-server-protocol: mark permission profiles experimental @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19846 [sandbox] Enforce protected workspace metadata paths @evawong-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#20008 tui: use permission profiles for sandbox state @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#20010 core tests: submit turns with permission profiles @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#20011 core tests: build user turns from permission profiles @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#20013 core tests: migrate more turns to permission profiles @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#20016 core tests: send model turns with permission profiles @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#20024 core tests: migrate safety check turns to profiles @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#20027 core tests: migrate tools tests to permission profiles @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#20106 linux-sandbox: switch helper plumbing to PermissionProfile @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#20117 feat(cli): add explicit sandbox permission profiles @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#20118 feat(cli): add sandbox profile config controls @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  - quote: '#19852 Enforce workspace metadata protections in Linux sandbox @evawong-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.128.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 21-safety-and-privacy-changes-in-rust-v0-128-0
  source_release: codex-cli-2026-04-30-rust-v0-128-0-github-315916672-1708ab89
  source_type: github_releases
  theme: safety-privacy
  title: 21 Safety and Privacy changes in rust-v0.128.0
  type: change
related_changes:
- '[[Changes/Gemini CLI/2026-04-28-feat-sandbox-resolve-custom-seatbelt-profiles-from-home-gemini-first-by-mvanhorn|feat(sandbox):
  resolve custom seatbelt profiles from $HOME/.gemini first]]'
- '[[Changes/GitHub Copilot CLI/2026-04-28-allow-acp-clients-to-toggle-allow-all-permission-mode-via-session-configuration|Allow
  ACP clients to toggle allow-all permission mode via session configuration]]'
- '[[Changes/Dify/2026-04-29-7-safety-and-privacy-changes-in-1-14-0|7 Safety and Privacy
  changes in 1.14.0]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-04-30-rust-v0-128-0-github-315916672-1708ab89|codex-cli-2026-04-30-rust-v0-128-0-github-315916672-1708ab89]]'
source_type: github_releases
theme: safety-privacy
title: 21 Safety and Privacy changes in rust-v0.128.0
type: change
---

<!-- chronolog:begin region="header" -->
# 21 Safety and Privacy changes in rust-v0.128.0

**Codex CLI** · 2026-04-30 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.128.0) · from [[Releases/Codex CLI/codex-cli-2026-04-30-rust-v0-128-0-github-315916672-1708ab89|0.128.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Expanded permission profiles with built-in defaults, sandbox CLI profile selection, cwd controls, and active-profile metadata for clients. (#19900, #20117, #20118, #20095)

> Deprecated `--full-auto` while steering users toward explicit permission profiles and trust flows. (#20133)

> #19453 Serialize legacy Windows PowerShell sandbox tests @dylan-hurd-oai

> #19393 permissions: migrate approval and sandbox consumers to profiles @bolinfest

> #19739 inline hostname resolution for remote sandbox config @abhinav-oai

> #19734 permissions: centralize legacy sandbox projection @bolinfest

> #19735 permissions: store only constrained permission profiles @bolinfest

> #19775 permissions: derive snapshot sandbox projections @bolinfest

> #19899 app-server-protocol: mark permission profiles experimental @bolinfest

> #19846 [sandbox] Enforce protected workspace metadata paths @evawong-oai

> #20008 tui: use permission profiles for sandbox state @bolinfest

> #20010 core tests: submit turns with permission profiles @bolinfest

> #20011 core tests: build user turns from permission profiles @bolinfest

> #20013 core tests: migrate more turns to permission profiles @bolinfest

> #20016 core tests: send model turns with permission profiles @bolinfest

> #20024 core tests: migrate safety check turns to profiles @bolinfest

> #20027 core tests: migrate tools tests to permission profiles @bolinfest

> #20106 linux-sandbox: switch helper plumbing to PermissionProfile @bolinfest

> #20117 feat(cli): add explicit sandbox permission profiles @viyatb-oai

> #20118 feat(cli): add sandbox profile config controls @viyatb-oai

> #19852 Enforce workspace metadata protections in Linux sandbox @evawong-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.128.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-04-30-2-interface-experience-changes-in-rust-v0-128-0|2 Interface Experience changes in rust-v0.128.0]] · Interface Experience
- [[Changes/Codex CLI/2026-04-30-19805-add-multiagentv2-root-and-subagent-context-hints-jif-oai|♯19805 Add MultiAgentV2 root and subagent context hints @jif-oai]] · Context Window
- [[Changes/Codex CLI/2026-04-30-3-mobile-and-desktop-changes-in-rust-v0-128-0|3 Mobile and Desktop changes in rust-v0.128.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-04-30-12-memory-and-personalization-changes-in-rust-v0-128-0|12 Memory and Personalization changes in rust-v0.128.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-04-30-19-agent-mode-changes-in-rust-v0-128-0|19 Agent Mode changes in rust-v0.128.0]] · Agent Mode
- [[Changes/Codex CLI/2026-04-30-20149-reduce-the-surface-of-collaboration-modes-pakrym-oai|♯20149 Reduce the surface of collaboration modes @pakrym-oai]] · Collaboration
- [[Changes/Codex CLI/2026-04-30-14-developer-workflow-changes-in-rust-v0-128-0|14 Developer Workflow changes in rust-v0.128.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-04-30-37-apps-and-integrations-changes-in-rust-v0-128-0|37 Apps and Integrations changes in rust-v0.128.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-04-30-19443-add-gpt-image-2-to-bundled-openai-docs-skill-kkahadze-oai|♯19443 Add gpt-image-2 to bundled OpenAI Docs skill @kkahadze-oai]] · Image Generation
- [[Changes/Codex CLI/2026-04-30-3-account-and-access-changes-in-rust-v0-128-0|3 Account and Access changes in rust-v0.128.0]] · Account and Access
- [[Changes/Codex CLI/2026-04-30-20045-fix-plan-mode-nudge-test-after-task-completion-signature-change-canvrno-oa|♯20045 Fix plan mode nudge test after task completion signature change @canvrno-oai]] · Editor Experience
- [[Changes/Codex CLI/2026-04-30-10-model-support-changes-in-rust-v0-128-0|10 Model Support changes in rust-v0.128.0]] · Model Support
- [[Changes/Codex CLI/2026-04-30-145-other-changes-in-rust-v0-128-0|145 other changes in rust-v0.128.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-04-29 · Dify · [[Changes/Dify/2026-04-29-7-safety-and-privacy-changes-in-1-14-0|7 Safety and Privacy changes in 1.14.0]]
- Later: 2026-04-30 · Cursor · [[Changes/Cursor/2026-04-30-cursor-security-review-is-now-in-beta-on-teams-and-enterprise-plans-you-can-run|Cursor Security Review is now in beta on Teams and Enterprise plans]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-04-30-d184bd&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-04-30-21-safety-and-privacy-changes-in-rust-v0-128-0.md%0ACard%20ID%3A%20codex-cli-2026-04-30-d184bd%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.128.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->