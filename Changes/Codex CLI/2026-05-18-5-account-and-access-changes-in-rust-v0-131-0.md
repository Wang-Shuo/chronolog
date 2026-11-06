---
card_id: codex-cli-2026-05-18-37f24e
date: '2026-05-18'
description: 'Codex CLI · 2026-05-18 · Account and Access: 5 changes in 0.131.0 —
  Improved Git and auth reliability by using root worktree hooks consistently, ignoring
  repo…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires
    login]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1145
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 24a4769102eb5f0fd9bb7a42090455a6dc71fab25f0cf27c2b11807014b31970
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-05-18-37f24e
  comparison: ''
  date: '2026-05-18'
  description: 'Codex CLI — 0.131.0: 5 Account and Access changes'
  evidence:
  - quote: 'Improved Git and auth reliability by using root worktree hooks consistently,
      ignoring repo hook/fsmonitor config in helper commands, binding local MCP OAuth
      callbacks, and revoking superseded login tokens. (#21969, #22843, #22652, #20237,
      #21747)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#21747 [login] revoke superseded auth tokens on relogin @cooper-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22338 [app-server] Gate login issuer override constant @cassirer-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#20237 Add callback ids to local MCP OAuth redirects @stevenlee-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22575 Support explicit MCP OAuth client IDs @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 5-account-and-access-changes-in-rust-v0-131-0
  source_release: codex-cli-2026-05-18-rust-v0-131-0-github-324452638-5f16ff1d
  source_type: github_releases
  theme: account-access
  title: 5 Account and Access changes in rust-v0.131.0
  type: change
related_changes:
- '[[Changes/Dify/2026-05-12-refactor-auth-update-oauth-button-and-settings-modal-for-improved-state-manageme|refactor(auth):
  update OAuth button and settings modal for improved state management…]]'
- '[[Changes/v0/2026-05-12-added-support-for-oauth-authorized-mcp-servers-in-the-platform-api-with-referenc|Added
  support for OAuth-authorized MCP servers in the platform API, with reference…]]'
- '[[Changes/Claude Code/2026-05-13-bedrock-awscredentialexport-now-always-runs-when-configured-instead-of-being-ski|Bedrock:
  awsCredentialExport now always runs when configured instead of being…]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-05-18-rust-v0-131-0-github-324452638-5f16ff1d|codex-cli-2026-05-18-rust-v0-131-0-github-324452638-5f16ff1d]]'
source_type: github_releases
theme: account-access
title: 5 Account and Access changes in rust-v0.131.0
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Account and Access changes in rust-v0.131.0

**Codex CLI** · 2026-05-18 · [[Themes/account-access|Account and Access]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.131.0) · from [[Releases/Codex CLI/codex-cli-2026-05-18-rust-v0-131-0-github-324452638-5f16ff1d|0.131.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Improved Git and auth reliability by using root worktree hooks consistently, ignoring repo hook/fsmonitor config in helper commands, binding local MCP OAuth callbacks, and revoking superseded login tokens. (#21969, #22843, #22652, #20237, #21747)

> #21747 [login] revoke superseded auth tokens on relogin @cooper-oai

> #22338 [app-server] Gate login issuer override constant @cassirer-openai

> #20237 Add callback ids to local MCP OAuth redirects @stevenlee-oai

> #22575 Support explicit MCP OAuth client IDs @mzeng-openai

Source: https://github.com/openai/codex/releases/tag/rust-v0.131.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-05-18-17-safety-and-privacy-changes-in-rust-v0-131-0|17 Safety and Privacy changes in rust-v0.131.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-05-18-9-agent-mode-changes-in-rust-v0-131-0|9 Agent Mode changes in rust-v0.131.0]] · Agent Mode
- [[Changes/Codex CLI/2026-05-18-4-memory-and-personalization-changes-in-rust-v0-131-0|4 Memory and Personalization changes in rust-v0.131.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-05-18-5-interface-experience-changes-in-rust-v0-131-0|5 Interface Experience changes in rust-v0.131.0]] · Interface Experience
- [[Changes/Codex CLI/2026-05-18-12-developer-workflow-changes-in-rust-v0-131-0|12 Developer Workflow changes in rust-v0.131.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-05-18-56-apps-and-integrations-changes-in-rust-v0-131-0|56 Apps and Integrations changes in rust-v0.131.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-05-18-21954-fix-goal-update-and-add-goal-edit-command-in-tui-etraut-openai|♯21954 Fix goal update and add /goal edit command in TUI @etraut-openai]] · Editor Experience
- [[Changes/Codex CLI/2026-05-18-10-mobile-and-desktop-changes-in-rust-v0-131-0|10 Mobile and Desktop changes in rust-v0.131.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-05-18-7-context-window-changes-in-rust-v0-131-0|7 Context Window changes in rust-v0.131.0]] · Context Window
- [[Changes/Codex CLI/2026-05-18-3-collaboration-changes-in-rust-v0-131-0|3 Collaboration changes in rust-v0.131.0]] · Collaboration
- [[Changes/Codex CLI/2026-05-18-4-model-support-changes-in-rust-v0-131-0|4 Model Support changes in rust-v0.131.0]] · Model Support
- [[Changes/Codex CLI/2026-05-18-155-other-changes-in-rust-v0-131-0|155 other changes in rust-v0.131.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2026-05-13 · Claude Code · [[Changes/Claude Code/2026-05-13-bedrock-awscredentialexport-now-always-runs-when-configured-instead-of-being-ski|Bedrock: awsCredentialExport now always runs when configured instead of being…]]
- Later: 2026-05-19 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-05-19-3-account-and-access-changes-in-v1-0-49|3 Account and Access changes in v1.0.49]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-30 · Cursor · [[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires login]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-05-18-37f24e&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-05-18-5-account-and-access-changes-in-rust-v0-131-0.md%0ACard%20ID%3A%20codex-cli-2026-05-18-37f24e%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.131.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->