---
card_id: github-copilot-cli-2026-05-19-887b87
date: '2026-05-19'
description: 'GitHub Copilot CLI · 2026-05-19 · Apps and Integrations: 9 changes in
  1.0.49 — Add `copilot plugin update --all` to update all installed plugins at once'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If
    you have a recording with each speaker with a different microphone, or saved…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2713
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 9185b41b34a81a8a5bd2449d7549d6466656aa3f826225f7f5e3e5b42a243ebc
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-05-19-887b87
  comparison: ''
  date: '2026-05-19'
  description: 'GitHub Copilot CLI — 1.0.49: 9 Apps and Integrations changes'
  evidence:
  - quote: Add `copilot plugin update --all` to update all installed plugins at once
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.49
  - quote: Repo hooks in `.github/hooks/` now load in prompt mode (`-p`) when the
      folder is already trusted
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.49
  - quote: MCP server configurations with no `args` field are now accepted and treated
      as an empty args list
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.49
  - quote: MCP stdio servers now display type as 'stdio' instead of 'local' for consistency
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.49
  - quote: Prompt mode (-p) automatically loads workspace MCP sources when the current
      folder is already trusted
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.49
  - quote: 'Experimental: /mcp search command to search and install MCP servers from
      registry'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.49
  - quote: 'Experimental: Tool search with deferred loading for MCP and external tools'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.49
  - quote: Add COPILOT_PLUGIN_DIR_ONLY environment variable to disable automatic plugin
      discovery, enabling deterministic plugin sets when using --plugin-dir
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.49
  - quote: --plugin-dir and --additional-mcp-config now work in --server / --headless
      mode
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.49
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 9-apps-and-integrations-changes-in-v1-0-49
  source_release: github-copilot-cli-2026-05-19-v1-0-49-github-324640083-4bf093b8
  source_type: github_releases
  theme: apps-integrations
  title: 9 Apps and Integrations changes in v1.0.49
  type: change
related_changes:
- '[[Changes/Dify/2026-05-19-4-apps-and-integrations-changes-in-1-14-2|4 Apps and
  Integrations changes in 1.14.2]]'
- '[[Changes/Gemini/2026-05-19-daily-brief-is-your-personalized-overview-of-what-matters-today|Daily
  Brief is your personalized overview of what matters today]]'
- '[[Changes/Gemini/2026-05-19-gemini-can-connect-to-more-apps-starting-with-opentable-canva-and-instacart|Gemini
  can connect to more apps, starting with OpenTable, Canva, and Instacart]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-05-19-v1-0-49-github-324640083-4bf093b8|github-copilot-cli-2026-05-19-v1-0-49-github-324640083-4bf093b8]]'
source_type: github_releases
theme: apps-integrations
title: 9 Apps and Integrations changes in v1.0.49
type: change
---

<!-- chronolog:begin region="header" -->
# 9 Apps and Integrations changes in v1.0.49

**GitHub Copilot CLI** · 2026-05-19 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.49) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-05-19-v1-0-49-github-324640083-4bf093b8|1.0.49]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Add `copilot plugin update --all` to update all installed plugins at once

> Repo hooks in `.github/hooks/` now load in prompt mode (`-p`) when the folder is already trusted

> MCP server configurations with no `args` field are now accepted and treated as an empty args list

> MCP stdio servers now display type as 'stdio' instead of 'local' for consistency

> Prompt mode (-p) automatically loads workspace MCP sources when the current folder is already trusted

> Experimental: /mcp search command to search and install MCP servers from registry

> Experimental: Tool search with deferred loading for MCP and external tools

> Add COPILOT_PLUGIN_DIR_ONLY environment variable to disable automatic plugin discovery, enabling deterministic plugin sets when using --plugin-dir

> --plugin-dir and --additional-mcp-config now work in --server / --headless mode

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.49
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-05-19-2-mobile-and-desktop-changes-in-v1-0-49|2 Mobile and Desktop changes in v1.0.49]] · Mobile and Desktop
- [[Changes/GitHub Copilot CLI/2026-05-19-4-agent-mode-changes-in-v1-0-49|4 Agent Mode changes in v1.0.49]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-05-19-2-developer-workflow-changes-in-v1-0-49|2 Developer Workflow changes in v1.0.49]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-05-19-memory-permission-prompts-now-name-who-can-see-a-stored-memory-user-scope-or-the|Memory permission prompts now name who can see a stored memory]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-05-19-2-memory-and-personalization-changes-in-v1-0-49|2 Memory and Personalization changes in v1.0.49]] · Memory and Personalization
- [[Changes/GitHub Copilot CLI/2026-05-19-file-diffs-are-correctly-reported-to-acp-clients-for-all-edit-tool-types|File diffs are correctly reported to ACP clients for all edit tool types]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-05-19-3-interface-experience-changes-in-v1-0-49|3 Interface Experience changes in v1.0.49]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-05-19-document-attachment-paths-are-included-in-context-so-the-agent-can-reference-pas|Document attachment paths are included in context so the agent can reference pasted…]] · Context Window
- [[Changes/GitHub Copilot CLI/2026-05-19-2-model-support-changes-in-v1-0-49|2 Model Support changes in v1.0.49]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-05-19-3-account-and-access-changes-in-v1-0-49|3 Account and Access changes in v1.0.49]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-05-19-10-other-changes-in-v1-0-49|10 other changes in v1.0.49]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-05-19 · Gemini · [[Changes/Gemini/2026-05-19-gemini-can-connect-to-more-apps-starting-with-opentable-canva-and-instacart|Gemini can connect to more apps, starting with OpenTable, Canva, and Instacart]]
- Later: 2026-05-19 · Microsoft 365 Copilot · [[Changes/Microsoft 365 Copilot/2026-05-19-graph-api-enhancements-for-custom-connector-relevance-and-ux-web-microsoft-365-c|Graph API enhancements for custom connector relevance and UX…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-12-14 · Descript · [[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If you have a recording with each speaker with a different microphone, or saved…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-05-19-887b87&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-05-19-9-apps-and-integrations-changes-in-v1-0-49.md%0ACard%20ID%3A%20github-copilot-cli-2026-05-19-887b87%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.49%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->