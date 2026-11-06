---
card_id: github-copilot-cli-2026-08-03-0a518d
date: '2026-08-03'
description: 'GitHub Copilot CLI · 2026-08-03 · Apps and Integrations: 4 changes in
  1.0.78 — First-party plugins automatically update to the latest version at session
  start'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1229
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: d45b38a50500197fe7b0a0bb15a4478de71caa061ac640eec04be478bad8e165
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-08-03-0a518d
  comparison: ''
  date: '2026-08-03'
  description: 'GitHub Copilot CLI — 1.0.78: 4 Apps and Integrations changes'
  evidence:
  - quote: First-party plugins automatically update to the latest version at session
      start
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.78
  - quote: Extension slash commands run their handler exactly once per invocation
      when several extensions are loaded
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.78
  - quote: Switching sessions no longer restarts MCP servers or rebuilds hook state,
      so a turn running in another session is never halted with a stale-hook error
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.78
  - quote: 'Honor explicit GitHub MCP toolset/tool config: keep gh-overlap tools and
      stop steering to the gh CLI when you opt in'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.78
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 4-apps-and-integrations-changes-in-v1-0-78
  source_release: github-copilot-cli-2026-08-03-v1-0-78-github-364543196-53a079bc
  source_type: github_releases
  theme: apps-integrations
  title: 4 Apps and Integrations changes in v1.0.78
  type: change
related_changes:
- '[[Changes/OpenHands/2026-07-30-feat-enable-disable-an-installed-mcp-server-from-its-card-by-hieptl-in-https-git|feat:
  enable/disable an installed MCP server from its card]]'
- '[[Changes/Cline/2026-07-31-3-apps-and-integrations-changes-in-v4-1-0|3 Apps and
  Integrations changes in v4.1.0]]'
- '[[Changes/Cursor/2026-08-03-cursor-can-now-read-write-and-act-across-your-google-workspace|Google
  Workspace Plugins]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-08-03-v1-0-78-github-364543196-53a079bc|github-copilot-cli-2026-08-03-v1-0-78-github-364543196-53a079bc]]'
source_type: github_releases
theme: apps-integrations
title: 4 Apps and Integrations changes in v1.0.78
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Apps and Integrations changes in v1.0.78

**GitHub Copilot CLI** · 2026-08-03 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.78) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-08-03-v1-0-78-github-364543196-53a079bc|1.0.78]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> First-party plugins automatically update to the latest version at session start

> Extension slash commands run their handler exactly once per invocation when several extensions are loaded

> Switching sessions no longer restarts MCP servers or rebuilds hook state, so a turn running in another session is never halted with a stale-hook error

> Honor explicit GitHub MCP toolset/tool config: keep gh-overlap tools and stop steering to the gh CLI when you opt in

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.78
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-08-03-a-run-whose-prompt-is-piped-over-stdin-now-treats-its-sessionend-hook-the-same-w|A run whose prompt is piped over stdin now treats its sessionEnd hook the same way…]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-08-03-2-editor-experience-changes-in-v1-0-78|2 Editor Experience changes in v1.0.78]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-08-03-resuming-a-long-session-is-dramatically-faster-and-far-lighter-on-memory-because|Resuming a long session is dramatically faster and far lighter on memory, because…]] · Reliability and Performance
- [[Changes/GitHub Copilot CLI/2026-08-03-2-account-and-access-changes-in-v1-0-78|2 Account and Access changes in v1.0.78]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-08-03-the-allow-all-auto-safety-judge-model-is-no-longer-user-configurable-the-judge-m|The /allow-all auto safety-judge model is no longer user-configurable]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-08-03-2-interface-experience-changes-in-v1-0-78|2 Interface Experience changes in v1.0.78]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-08-03-3-safety-and-privacy-changes-in-v1-0-78|3 Safety and Privacy changes in v1.0.78]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-08-03-2-developer-workflow-changes-in-v1-0-78|2 Developer Workflow changes in v1.0.78]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-08-03-9-other-changes-in-v1-0-78|9 other changes in v1.0.78]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-08-03 · Cursor · [[Changes/Cursor/2026-08-03-cursor-can-now-read-write-and-act-across-your-google-workspace|Google Workspace Plugins]]
- Later: 2026-08-03 · OpenHands · [[Changes/OpenHands/2026-08-03-chore-bump-openhands-extensions-to-0-13-0-by-hieptl-in-https-github-com-openhand|chore: bump @openhands/extensions to 0.13.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-08-03-0a518d&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-08-03-4-apps-and-integrations-changes-in-v1-0-78.md%0ACard%20ID%3A%20github-copilot-cli-2026-08-03-0a518d%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.78%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->