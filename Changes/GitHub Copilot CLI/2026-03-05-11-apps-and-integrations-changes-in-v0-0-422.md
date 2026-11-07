---
card_id: github-copilot-cli-2026-03-05-8840a8
date: '2026-03-05'
description: 'GitHub Copilot CLI · 2026-03-05 · Apps and Integrations: 11 changes
  in 0.0.422 — Load personal hooks from ~/.copilot/hooks in addition to repo-level…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If
    you have a recording with each speaker with a different microphone, or saved…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2638
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 4e18aec8565f8e5d863da174a12d437ad5c0d58241541cb305db891ff0da65db
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-03-05-8840a8
  comparison: ''
  date: '2026-03-05'
  description: 'GitHub Copilot CLI — 0.0.422: 11 Apps and Integrations changes'
  evidence:
  - quote: Load personal hooks from ~/.copilot/hooks in addition to repo-level .github/hooks
    source_release: https://github.com/github/copilot-cli/releases/tag/v0.0.422
  - quote: Plugin cache automatically recovers from a corrupted or incomplete clone
      without manual intervention
    source_release: https://github.com/github/copilot-cli/releases/tag/v0.0.422
  - quote: Show a clear, actionable error message when git is not installed and a
      remote plugin or marketplace is used
    source_release: https://github.com/github/copilot-cli/releases/tag/v0.0.422
  - quote: GitHub MCP server stays enabled in repositories that have both Azure DevOps
      and GitHub remotes
    source_release: https://github.com/github/copilot-cli/releases/tag/v0.0.422
  - quote: Plugin-contributed LSP servers are now loaded, started, and shown in /lsp
      show
    source_release: https://github.com/github/copilot-cli/releases/tag/v0.0.422
  - quote: Add --output-format json flag to emit JSONL in prompt mode for programmatic
      integrations
    source_release: https://github.com/github/copilot-cli/releases/tag/v0.0.422
  - quote: Add exitPlanMode.request protocol method for SDK plan approval support
    source_release: https://github.com/github/copilot-cli/releases/tag/v0.0.422
  - quote: GitHub MCP server connection status is accurately tracked and counted in
      the status indicator
    source_release: https://github.com/github/copilot-cli/releases/tag/v0.0.422
  - quote: Add startup prompt hooks to auto-submit prompts or slash commands when
      a session starts
    source_release: https://github.com/github/copilot-cli/releases/tag/v0.0.422
  - quote: Support enabledPlugins in config for automatic plugin installation at startup
    source_release: https://github.com/github/copilot-cli/releases/tag/v0.0.422
  - quote: Support installing plugins from ssh:// URLs
    source_release: https://github.com/github/copilot-cli/releases/tag/v0.0.422
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 11-apps-and-integrations-changes-in-v0-0-422
  source_release: github-copilot-cli-2026-03-05-v0-0-422-github-293731015-4b06f61c
  source_type: github_releases
  theme: apps-integrations
  title: 11 Apps and Integrations changes in v0.0.422
  type: change
related_changes:
- '[[Changes/Claude Code/2026-03-05-7-apps-and-integrations-changes-in-v2-1-69|7 Apps
  and Integrations changes in v2.1.69]]'
- '[[Changes/Codex CLI/2026-03-05-7-apps-and-integrations-changes-in-rust-v0-110-0|7
  Apps and Integrations changes in rust-v0.110.0]]'
- '[[Changes/Codex CLI/2026-03-05-5-apps-and-integrations-changes-in-rust-v0-111-0|5
  Apps and Integrations changes in rust-v0.111.0]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-03-05-v0-0-422-github-293731015-4b06f61c|github-copilot-cli-2026-03-05-v0-0-422-github-293731015-4b06f61c]]'
source_type: github_releases
theme: apps-integrations
title: 11 Apps and Integrations changes in v0.0.422
type: change
---

<!-- chronolog:begin region="header" -->
# 11 Apps and Integrations changes in v0.0.422

**GitHub Copilot CLI** · 2026-03-05 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v0.0.422) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-03-05-v0-0-422-github-293731015-4b06f61c|0.0.422]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Load personal hooks from ~/.copilot/hooks in addition to repo-level .github/hooks

> Plugin cache automatically recovers from a corrupted or incomplete clone without manual intervention

> Show a clear, actionable error message when git is not installed and a remote plugin or marketplace is used

> GitHub MCP server stays enabled in repositories that have both Azure DevOps and GitHub remotes

> Plugin-contributed LSP servers are now loaded, started, and shown in /lsp show

> Add --output-format json flag to emit JSONL in prompt mode for programmatic integrations

> Add exitPlanMode.request protocol method for SDK plan approval support

> GitHub MCP server connection status is accurately tracked and counted in the status indicator

> Add startup prompt hooks to auto-submit prompts or slash commands when a session starts

> Support enabledPlugins in config for automatic plugin installation at startup

> Support installing plugins from ssh:// URLs

Source: https://github.com/github/copilot-cli/releases/tag/v0.0.422
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-03-05-automatic-notifications-when-background-shell-commands-and-agents-complete|Automatic notifications when background shell commands and agents complete]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-03-05-session-usage-metrics-requests-tokens-code-changes-are-now-persisted-to-events-j|Session usage metrics (requests, tokens, code changes) are now persisted…]] · Context Window
- [[Changes/GitHub Copilot CLI/2026-03-05-display-request-id-in-authentication-and-authorization-error-messages-to-aid-tro|Display request ID in authentication and authorization error messages to aid…]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-03-05-add-support-for-gpt-5-4-model|Add support for GPT-5.4 model]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-03-05-text-selection-persists-after-copying-to-clipboard-in-alt-screen|Text selection persists after copying to clipboard in alt screen]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-03-05-reduce-memory-usage-in-alt-screen-mode-for-long-sessions|Reduce memory usage in alt-screen mode for long sessions]] · Reliability and Performance
- [[Changes/GitHub Copilot CLI/2026-03-05-6-editor-experience-changes-in-v0-0-422|6 Editor Experience changes in v0.0.422]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-03-05-opening-links-on-windows-correctly-handles-urls-with-query-parameters|Opening links on Windows correctly handles URLs with & query parameters]] · Mobile and Desktop
- [[Changes/GitHub Copilot CLI/2026-03-05-3-developer-workflow-changes-in-v0-0-422|3 Developer Workflow changes in v0.0.422]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-03-05-16-other-changes-in-v0-0-422|16 other changes in v0.0.422]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-03-05 · Codex CLI · [[Changes/Codex CLI/2026-03-05-5-apps-and-integrations-changes-in-rust-v0-111-0|5 Apps and Integrations changes in rust-v0.111.0]]
- Later: 2026-03-05 · OpenCode · [[Changes/OpenCode/2026-03-05-sdk-update-sdk-package-json|SDK Update SDK package.json]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-12-14 · Descript · [[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If you have a recording with each speaker with a different microphone, or saved…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-03-05-8840a8&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-03-05-11-apps-and-integrations-changes-in-v0-0-422.md%0ACard%20ID%3A%20github-copilot-cli-2026-03-05-8840a8%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv0.0.422%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->