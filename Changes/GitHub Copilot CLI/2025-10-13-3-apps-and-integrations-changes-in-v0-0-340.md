---
card_id: github-copilot-cli-2025-10-13-853a25
date: '2025-10-13'
description: 'GitHub Copilot CLI · 2025-10-13 · Apps and Integrations: 3 changes in
  0.0.340 — Changed parsing of environment variables in MCP server configuration to
  treat…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 935
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: aa0c6b4b3265a0c4223416b16ebe26fbf0ae752da42a98492fcdea867198ab7b
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2025-10-13-853a25
  comparison: ''
  date: '2025-10-13'
  description: 'GitHub Copilot CLI — 0.0.340: 3 Apps and Integrations changes'
  evidence:
  - quote: Changed parsing of environment variables in MCP server configuration to
      treat the value of the `env` section as literal values (fixes https://github.com/github/copilot-cli/issues/26).
    source_release: https://github.com/github/copilot-cli/releases/tag/v0.0.340
  - quote: Customers who have configured MCP Servers for use with the CLI will need
      to make a slight modification to their `~/.copilot/mcp-config.json`. For any
      servers they have added with an `env` section, they will need to go add a `$`
      to the start of the "value" pair of the key value pair of each entry in the
      env-block, so to have the values treated as references to environment variables.
    source_release: https://github.com/github/copilot-cli/releases/tag/v0.0.340
  - quote: 'Before this change, the CLI would read the value of `GITHUB_TOKEN` from
      the environment of the CLI and set the environment varaible named `GITHUB_ACCESS_TOKEN`
      in the MCP process to that value. With this change, `GITHUB_ACCESS_TOKEN` would
      now be set to the literal value `GITHUB_TOKEN`. To get the old behavior, change
      to this:'
    source_release: https://github.com/github/copilot-cli/releases/tag/v0.0.340
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 3-apps-and-integrations-changes-in-v0-0-340
  source_release: github-copilot-cli-2025-10-13-v0-0-340-github-254190325-efc0f949
  source_type: github_releases
  theme: apps-integrations
  title: 3 Apps and Integrations changes in v0.0.340
  type: change
related_changes:
- '[[Changes/Codex CLI/2025-10-09-6-apps-and-integrations-changes-in-rust-v0-46-0|6
  Apps and Integrations changes in rust-v0.46.0]]'
- '[[Changes/GitHub Copilot CLI/2025-10-10-improved-argument-input-to-mcp-servers-in-mcp-add-previously-users-had-to-use-co|Improved
  argument input to MCP servers in /mcp add -- previously, users had to use…]]'
- '[[Changes/ChatGPT/2025-10-13-we-re-rolling-out-two-new-ways-to-bring-slack-and-chatgpt-together-a-connector-t-be2213|Slack
  connector and app]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2025-10-13-v0-0-340-github-254190325-efc0f949|github-copilot-cli-2025-10-13-v0-0-340-github-254190325-efc0f949]]'
source_type: github_releases
theme: apps-integrations
title: 3 Apps and Integrations changes in v0.0.340
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Apps and Integrations changes in v0.0.340

**GitHub Copilot CLI** · 2025-10-13 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v0.0.340) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2025-10-13-v0-0-340-github-254190325-efc0f949|0.0.340]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Changed parsing of environment variables in MCP server configuration to treat the value of the `env` section as literal values (fixes https://github.com/github/copilot-cli/issues/26).

> Customers who have configured MCP Servers for use with the CLI will need to make a slight modification to their `~/.copilot/mcp-config.json`. For any servers they have added with an `env` section, they will need to go add a `$` to the start of the "value" pair of the key value pair of each entry in the env-block, so to have the values treated as references to environment variables.

> Before this change, the CLI would read the value of `GITHUB_TOKEN` from the environment of the CLI and set the environment varaible named `GITHUB_ACCESS_TOKEN` in the MCP process to that value. With this change, `GITHUB_ACCESS_TOKEN` would now be set to the literal value `GITHUB_TOKEN`. To get the old behavior, change to this:

Source: https://github.com/github/copilot-cli/releases/tag/v0.0.340
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2025-10-13-2-editor-experience-changes-in-v0-0-340|2 Editor Experience changes in v0.0.340]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2025-10-13-removed-the-windows-support-is-experimental-warning-we-ve-made-some-big-strides|Removed the "Windows support is experimental" warning -- we've made some big strides…]] · Mobile and Desktop
- [[Changes/GitHub Copilot CLI/2025-10-13-2-other-changes-in-v0-0-340|2 other changes in v0.0.340]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2025-10-13 · ChatGPT · [[Changes/ChatGPT/2025-10-13-we-re-rolling-out-two-new-ways-to-bring-slack-and-chatgpt-together-a-connector-t-be2213|Slack connector and app]]
- Later: 2025-10-14 · ElevenLabs · [[Changes/ElevenLabs/2025-10-14-sdk-releases|SDK Releases]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2025-10-13-853a25&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2025-10-13-3-apps-and-integrations-changes-in-v0-0-340.md%0ACard%20ID%3A%20github-copilot-cli-2025-10-13-853a25%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv0.0.340%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->