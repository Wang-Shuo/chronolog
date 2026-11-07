---
card_id: github-copilot-cli-2026-06-05-d73d25
date: '2026-06-05'
description: 'GitHub Copilot CLI · 2026-06-05 · Apps and Integrations: 10 changes
  in 1.0.60 — MCP tools glyph in /context legend displays at the correct size'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If
    you have a recording with each speaker with a different microphone, or saved…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2730
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 542c08c2fb3af334dd3d734ecc609ec72277d7ae2b7ab0b330b14e64f85612c2
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-06-05-d73d25
  comparison: ''
  date: '2026-06-05'
  description: 'GitHub Copilot CLI — 1.0.60: 10 Apps and Integrations changes'
  evidence:
  - quote: MCP tools glyph in /context legend displays at the correct size
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.60
  - quote: /context separates Custom Instructions from the system prompt and cross-references
      per-server MCP tool token costs with /mcp
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.60
  - quote: LSP server config accepts `bash`, `powershell`, and `cwd` keys; command
      launch default cwd stays project-root unless `cwd` is set, and `cwd` expansion
      now supports plugin vars like `PLUGIN_ROOT` while shell launches keep hook-matching
      cwd/env behavior
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.60
  - quote: Extensions linked via directory symlinks are now discovered and loaded
      correctly
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.60
  - quote: Force-removing a marketplace no longer causes its plugins to reinstall
      on next launch
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.60
  - quote: Repository plugin overrides no longer change globally enabled plugin settings
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.60
  - quote: MCP allowlist now matches npm scoped servers whose registry entry drops
      the leading @ from the package identifier
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.60
  - quote: MCP servers registered via Azure API Center are no longer incorrectly blocked
      by the allowlist
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.60
  - quote: Local MCP servers sharing a serialized token broker (e.g. M365) reliably
      start instead of intermittently failing
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.60
  - quote: /env command now shows hook counts and source provenance for active hooks
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.60
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 10-apps-and-integrations-changes-in-v1-0-60
  source_release: github-copilot-cli-2026-06-05-v1-0-60-github-335046279-6a5628d4
  source_type: github_releases
  theme: apps-integrations
  title: 10 Apps and Integrations changes in v1.0.60
  type: change
related_changes:
- '[[Changes/Cursor/2026-06-04-2-apps-and-integrations-changes-in-custom-stores-custom-tools|2
  Apps and Integrations changes in Custom stores, custom tools…]]'
- '[[Changes/Ollama/2026-06-04-added-cline-cli-integration-docs|Added Cline CLI integration
  docs]]'
- '[[Changes/GitHub Copilot CLI/2026-06-05-mcp-tools-added-or-removed-by-a-server-mid-turn-are-now-available-immediately-in|MCP
  tools added or removed by a server mid-turn are now available immediately…]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-06-05-v1-0-60-github-335046279-6a5628d4|github-copilot-cli-2026-06-05-v1-0-60-github-335046279-6a5628d4]]'
source_type: github_releases
theme: apps-integrations
title: 10 Apps and Integrations changes in v1.0.60
type: change
---

<!-- chronolog:begin region="header" -->
# 10 Apps and Integrations changes in v1.0.60

**GitHub Copilot CLI** · 2026-06-05 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.60) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-06-05-v1-0-60-github-335046279-6a5628d4|1.0.60]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> MCP tools glyph in /context legend displays at the correct size

> /context separates Custom Instructions from the system prompt and cross-references per-server MCP tool token costs with /mcp

> LSP server config accepts `bash`, `powershell`, and `cwd` keys; command launch default cwd stays project-root unless `cwd` is set, and `cwd` expansion now supports plugin vars like `PLUGIN_ROOT` while shell launches keep hook-matching cwd/env behavior

> Extensions linked via directory symlinks are now discovered and loaded correctly

> Force-removing a marketplace no longer causes its plugins to reinstall on next launch

> Repository plugin overrides no longer change globally enabled plugin settings

> MCP allowlist now matches npm scoped servers whose registry entry drops the leading @ from the package identifier

> MCP servers registered via Azure API Center are no longer incorrectly blocked by the allowlist

> Local MCP servers sharing a serialized token broker (e.g. M365) reliably start instead of intermittently failing

> /env command now shows hook counts and source provenance for active hooks

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.60
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-06-05-add-billing-help-topic-with-an-overview-of-ai-credit-usage-features|Add billing help topic with an overview of AI credit usage features]] · Pricing Model
- [[Changes/GitHub Copilot CLI/2026-06-05-show-the-mission-control-sharing-status-of-synced-sessions-in-the-session-info-v|Show the Mission Control sharing status of synced sessions in the /session info view]] · Collaboration
- [[Changes/GitHub Copilot CLI/2026-06-05-3-editor-experience-changes-in-v1-0-60|3 Editor Experience changes in v1.0.60]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-06-05-6-interface-experience-changes-in-v1-0-60|6 Interface Experience changes in v1.0.60]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-06-05-11-developer-workflow-changes-in-v1-0-60|11 Developer Workflow changes in v1.0.60]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-06-05-mcp-tools-added-or-removed-by-a-server-mid-turn-are-now-available-immediately-in|MCP tools added or removed by a server mid-turn are now available immediately…]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-06-05-mcp-oauth-re-authentication-no-longer-fails-with-an-address-in-use-error-when-a|MCP OAuth re-authentication no longer fails with an address-in-use error…]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-06-05-2-agent-mode-changes-in-v1-0-60|2 Agent Mode changes in v1.0.60]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-06-05-2-model-support-changes-in-v1-0-60|2 Model Support changes in v1.0.60]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-06-05-2-safety-and-privacy-changes-in-v1-0-60|2 Safety and Privacy changes in v1.0.60]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-06-05-2-context-window-changes-in-v1-0-60|2 Context Window changes in v1.0.60]] · Context Window
- [[Changes/GitHub Copilot CLI/2026-06-05-2-mobile-and-desktop-changes-in-v1-0-60|2 Mobile and Desktop changes in v1.0.60]] · Mobile and Desktop
- [[Changes/GitHub Copilot CLI/2026-06-05-15-other-changes-in-v1-0-60|15 other changes in v1.0.60]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-06-04 · Ollama · [[Changes/Ollama/2026-06-04-added-cline-cli-integration-docs|Added Cline CLI integration docs]]
- Later: 2026-06-05 · Ollama · [[Changes/Ollama/2026-06-05-ollama-launch-omp-now-integrates-with-oh-my-pi-https-omp-sh-an-ai-coding-agent-w|ollama launch omp now integrates with Oh My Pi((source link) an AI coding…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-12-14 · Descript · [[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If you have a recording with each speaker with a different microphone, or saved…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-06-05-d73d25&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-06-05-10-apps-and-integrations-changes-in-v1-0-60.md%0ACard%20ID%3A%20github-copilot-cli-2026-06-05-d73d25%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.60%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->