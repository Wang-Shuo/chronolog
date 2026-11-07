---
card_id: github-copilot-cli-2026-05-01-f49cb0
date: '2026-05-01'
description: 'GitHub Copilot CLI · 2026-05-01 · Apps and Integrations: 6 changes in
  1.0.40 — `copilot plugin list` shows the correct version after running `copilot
  plugin…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1135
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 5d5b9684d86d8f807a5b8a0a377471da4f09ac863dd2931d518712880549ecad
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-05-01-f49cb0
  comparison: ''
  date: '2026-05-01'
  description: 'GitHub Copilot CLI — 1.0.40: 6 Apps and Integrations changes'
  evidence:
  - quote: '`copilot plugin list` shows the correct version after running `copilot
      plugin update`'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.40
  - quote: Detect Azure DevOps repositories and auto-disable the GitHub MCP server
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.40
  - quote: --config-dir now propagates correctly to plugin subcommands; --config-dir
      is deprecated in favor of COPILOT_HOME
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.40
  - quote: Remote control link shows the full URL in the timeline instead of 'Open
      in browser'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.40
  - quote: MCP tool names with dots or other invalid characters are now sanitized
      correctly
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.40
  - quote: Prompt mode (-p) now gates repo hooks and workspace MCP behind opt-in env
      vars (GITHUB_COPILOT_PROMPT_MODE_REPO_HOOKS and GITHUB_COPILOT_PROMPT_MODE_WORKSPACE_MCP)
      for secure-by-default behavior
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.40
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 6-apps-and-integrations-changes-in-v1-0-40
  source_release: github-copilot-cli-2026-05-01-v1-0-40-github-316385532-9c4aec71
  source_type: github_releases
  theme: apps-integrations
  title: 6 Apps and Integrations changes in v1.0.40
  type: change
related_changes:
- '[[Changes/Cursor/2026-04-29-run-npm-install-cursor-sdk-to-get-started-you-can-also-use-cursor-s-native-sdk-s-76fb76|Run
  npm install @cursor/sdk to get started]]'
- '[[Changes/Dify/2026-04-29-48-apps-and-integrations-changes-in-1-14-0|48 Apps and
  Integrations changes in 1.14.0]]'
- '[[Changes/Codex CLI/2026-04-30-37-apps-and-integrations-changes-in-rust-v0-128-0|37
  Apps and Integrations changes in rust-v0.128.0]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-05-01-v1-0-40-github-316385532-9c4aec71|github-copilot-cli-2026-05-01-v1-0-40-github-316385532-9c4aec71]]'
source_type: github_releases
theme: apps-integrations
title: 6 Apps and Integrations changes in v1.0.40
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Apps and Integrations changes in v1.0.40

**GitHub Copilot CLI** · 2026-05-01 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.40) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-05-01-v1-0-40-github-316385532-9c4aec71|1.0.40]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> `copilot plugin list` shows the correct version after running `copilot plugin update`

> Detect Azure DevOps repositories and auto-disable the GitHub MCP server

> --config-dir now propagates correctly to plugin subcommands; --config-dir is deprecated in favor of COPILOT_HOME

> Remote control link shows the full URL in the timeline instead of 'Open in browser'

> MCP tool names with dots or other invalid characters are now sanitized correctly

> Prompt mode (-p) now gates repo hooks and workspace MCP behind opt-in env vars (GITHUB_COPILOT_PROMPT_MODE_REPO_HOOKS and GITHUB_COPILOT_PROMPT_MODE_WORKSPACE_MCP) for secure-by-default behavior

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.40
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-05-01-slash-command-suggestions-rank-prefix-matches-above-fuzzy-matches|Slash command suggestions rank prefix matches above fuzzy matches]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-05-01-3-agent-mode-changes-in-v1-0-40|3 Agent Mode changes in v1.0.40]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-05-01-2-model-support-changes-in-v1-0-40|2 Model Support changes in v1.0.40]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-05-01-2-account-and-access-changes-in-v1-0-40|2 Account and Access changes in v1.0.40]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-05-01-session-history-file-tracking-and-the-chronicle-command-are-now-available-to-all|Session history, file tracking, and the /chronicle command are now available to all users]] · Projects and Workspaces
- [[Changes/GitHub Copilot CLI/2026-05-01-remote-session-statusline-shows-the-remote-working-directory-and-branch-instead|Remote session statusline shows the remote working directory and branch instead…]] · Context Window
- [[Changes/GitHub Copilot CLI/2026-05-01-improve-cli-startup-speed-by-loading-custom-ca-certificates-asynchronously|Improve CLI startup speed by loading custom CA certificates asynchronously]] · Reliability and Performance
- [[Changes/GitHub Copilot CLI/2026-05-01-research-uses-an-orchestrator-subagent-model-for-more-thorough-and-reliable-deep|/research uses an orchestrator/subagent model for more thorough and reliable deep…]] · Search and Browsing
- [[Changes/GitHub Copilot CLI/2026-05-01-session-resume-selector-displays-summaries-on-a-single-line-truncated-to-fit-the|Session resume selector displays summaries on a single line, truncated to fit…]] · Projects and Workspaces
- [[Changes/GitHub Copilot CLI/2026-05-01-3-interface-experience-changes-in-v1-0-40|3 Interface Experience changes in v1.0.40]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-05-01-10-other-changes-in-v1-0-40|10 other changes in v1.0.40]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-04-30 · Codex CLI · [[Changes/Codex CLI/2026-04-30-37-apps-and-integrations-changes-in-rust-v0-128-0|37 Apps and Integrations changes in rust-v0.128.0]]
- Later: 2026-05-01 · OpenCode · [[Changes/OpenCode/2026-05-01-core-invalid-remote-mcp-urls-now-fail-with-a-clear-error-instead-of-breaking-set|Core Invalid remote MCP URLs now fail with a clear error instead of breaking setup]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-05-01-f49cb0&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-05-01-6-apps-and-integrations-changes-in-v1-0-40.md%0ACard%20ID%3A%20github-copilot-cli-2026-05-01-f49cb0%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.40%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->