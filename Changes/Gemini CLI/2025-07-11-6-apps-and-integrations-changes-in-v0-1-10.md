---
card_id: gemini-cli-2025-07-11-0b23ee
date: '2025-07-11'
description: 'Gemini CLI · 2025-07-11 · Apps and Integrations: 6 changes in Release
  v0.1.10 — Add --allowed_mcp_server_names flag by @teeler in…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 841
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: e6b35a205c4becb3761e1a97d6a35aafb75faa496c4608a953b9a30a64c98e6f
product: gemini-cli
product_name: Gemini CLI
record:
  card_id: gemini-cli-2025-07-11-0b23ee
  comparison: ''
  date: '2025-07-11'
  description: 'Gemini CLI — Release v0.1.10: 6 Apps and Integrations changes'
  evidence:
  - quote: Add --allowed_mcp_server_names flag by @teeler in https://github.com/google-gemini/gemini-cli/pull/3464
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.1.10
  - quote: 'refactor: rename allowed_mcp_server_names to allowed-mcp-server-names
      by @teeler in https://github.com/google-gemini/gemini-cli/pull/3469'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.1.10
  - quote: Initialize MCP tools once at start up instead of every time we auth. by
      @scidomino in https://github.com/google-gemini/gemini-cli/pull/3483
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.1.10
  - quote: Improve auth env var validation logic and messaging to detect settings
      that confuse GenAI SDK by @mboshernitsan in https://github.com/google-gemini/gemini-cli/pull/1381
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.1.10
  - quote: Add a command line option to enable and list extensions by @bbiggs in https://github.com/google-gemini/gemini-cli/pull/3191
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.1.10
  - quote: 'chore(deps): bump actions/create-github-app-token from 1 to 2 by @dependabot
      in https://github.com/google-gemini/gemini-cli/pull/3576'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.1.10
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: gemini-cli
  product_name: Gemini CLI
  slug: 6-apps-and-integrations-changes-in-v0-1-10
  source_release: gemini-cli-2025-07-11-v0-1-10-github-231320517-434b29eb
  source_type: github_releases
  theme: apps-integrations
  title: 6 Apps and Integrations changes in v0.1.10
  type: change
related_changes:
- '[[Changes/Cline/2025-07-08-update-the-no-vscode-postmessage-eslint-rule-to-check-for-any-of-the-vscode-sdk|Update
  the no-vscode-postmessage eslint rule to check for any of the vscode SDK…]]'
- '[[Changes/Cline/2025-07-08-migrate-download-mcp-response-to-proto-by-celestial-vault-in-https-github-com-cl|migrate
  download MCP response to proto]]'
- '[[Changes/Dify/2025-07-10-10-apps-and-integrations-changes-in-1-6-0|10 Apps and
  Integrations changes in 1.6.0]]'
source_release: '[[Releases/Gemini CLI/gemini-cli-2025-07-11-v0-1-10-github-231320517-434b29eb|gemini-cli-2025-07-11-v0-1-10-github-231320517-434b29eb]]'
source_type: github_releases
theme: apps-integrations
title: 6 Apps and Integrations changes in v0.1.10
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Apps and Integrations changes in v0.1.10

**Gemini CLI** · 2025-07-11 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/google-gemini/gemini-cli/releases/tag/v0.1.10) · from [[Releases/Gemini CLI/gemini-cli-2025-07-11-v0-1-10-github-231320517-434b29eb|Release v0.1.10]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Add --allowed_mcp_server_names flag by @teeler in https://github.com/google-gemini/gemini-cli/pull/3464

> refactor: rename allowed_mcp_server_names to allowed-mcp-server-names by @teeler in https://github.com/google-gemini/gemini-cli/pull/3469

> Initialize MCP tools once at start up instead of every time we auth. by @scidomino in https://github.com/google-gemini/gemini-cli/pull/3483

> Improve auth env var validation logic and messaging to detect settings that confuse GenAI SDK by @mboshernitsan in https://github.com/google-gemini/gemini-cli/pull/1381

> Add a command line option to enable and list extensions by @bbiggs in https://github.com/google-gemini/gemini-cli/pull/3191

> chore(deps): bump actions/create-github-app-token from 1 to 2 by @dependabot in https://github.com/google-gemini/gemini-cli/pull/3576

Source: https://github.com/google-gemini/gemini-cli/releases/tag/v0.1.10
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Gemini CLI/2025-07-11-feat-handle-inline-content-modification-in-tool-scheduler-by-adamfweidman-in-htt|feat: Handle inline content modification in tool scheduler]] · Automation and Scheduling
- [[Changes/Gemini CLI/2025-07-11-help-add-shift-tab-tip-by-abhipatel12-in-https-github-com-google-gemini-gemini-c|help: add shift+tab tip]] · Editor Experience
- [[Changes/Gemini CLI/2025-07-11-feature-commands-refactor-slash-command-vision-for-the-future-by-abhipatel12-in|feature(commands) - Refactor Slash Command + Vision For the Future]] · Multimodal Input
- [[Changes/Gemini CLI/2025-07-11-don-t-enforce-leading-slash-since-that-s-not-true-on-windows-by-scidomino-in-htt|Don't enforce leading slash since that's not true on Windows]] · Mobile and Desktop
- [[Changes/Gemini CLI/2025-07-11-5-model-support-changes-in-v0-1-10|5 Model Support changes in v0.1.10]] · Model Support
- [[Changes/Gemini CLI/2025-07-11-2-developer-workflow-changes-in-v0-1-10|2 Developer Workflow changes in v0.1.10]] · Developer Workflow
- [[Changes/Gemini CLI/2025-07-11-update-terms-of-service-and-privacy-notice-for-clarity-by-jkcinouye-in-https-git|Update Terms of Service and Privacy Notice for clarity]] · Safety and Privacy
- [[Changes/Gemini CLI/2025-07-11-56-other-changes-in-v0-1-10|56 other changes in v0.1.10]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2025-07-10 · Dify · [[Changes/Dify/2025-07-10-10-apps-and-integrations-changes-in-1-6-0|10 Apps and Integrations changes in 1.6.0]]
- Later: 2025-07-14 · ElevenLabs · [[Changes/ElevenLabs/2025-07-14-sdks|SDKs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20gemini-cli-2025-07-11-0b23ee&body=Card%3A%20Changes%2FGemini%20CLI%2F2025-07-11-6-apps-and-integrations-changes-in-v0-1-10.md%0ACard%20ID%3A%20gemini-cli-2025-07-11-0b23ee%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgoogle-gemini%2Fgemini-cli%2Freleases%2Ftag%2Fv0.1.10%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->