---
card_id: claude-code-2026-10-19-89bbac
date: '2026-10-19'
description: 'Claude Code · 2026-10-19 · Apps and Integrations: 8 changes in v2.1.304
  — Added a transcript line when a plugin that runs first skips one of your mod''s
  hooks…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1306
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 80ef6af113552beab5fc3708b32998b06b5e33d5448f9ea9e57e9fa94d7e0a1e
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-10-19-89bbac
  comparison: ''
  date: '2026-10-19'
  description: 'Claude Code — v2.1.304: 8 Apps and Integrations changes'
  evidence:
  - quote: Added a transcript line when a plugin that runs first skips one of your
      mod's hooks, naming the event and the plugin
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.304
  - quote: 'Improved cloud sessions: a new conversation''s first turn no longer waits
      for the local (stdio) MCP servers of plugins synced from claude.ai, unless a
      server sets `alwaysLoad: true`'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.304
  - quote: 'Improved resume of large compacted sessions in SDK and headless mode:
      the first request after resuming is sent sooner'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.304
  - quote: Changed mods' `settings.read` hooks to receive each settings layer and
      rewrite the merged settings, so a managed mod can make an organization's setting
      a ceiling, including the `cleanupPeriodDays` the retention sweep uses
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.304
  - quote: 'Changed skill hooks: the skills of one source (a repo, your own folder,
      or a plugin) can register at most 1,024 hooks and 16,384 matcher characters
      per session'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.304
  - quote: 'Changed skills under a policy that allows hooks from plugins only: a skill
      used in the main conversation whose hooks are kept out no longer gets its `allowed-tools`'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.304
  - quote: Updated the /claude-api skill to use the `ant` CLI on Claude Platform on
      AWS instead of falling back to the SDK or curl
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.304
  - quote: Removed the notes from `claude plugin validate` that predicted where a
      mod's hooks would run
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.304
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 8-apps-and-integrations-changes-in-v2-1-304
  source_release: claude-code-2026-10-19-v2-1-304-github-417677344-46c4d994
  source_type: github_releases
  theme: apps-integrations
  title: 8 Apps and Integrations changes in v2.1.304
  type: change
related_changes:
- '[[Changes/Claude Code/2026-10-14-19-apps-and-integrations-changes-in-v2-1-299|19
  Apps and Integrations changes in v2.1.299]]'
- '[[Changes/ChatGPT/2026-10-16-improved-use-of-plugins-and-tools-to-carry-out-tasks|Improved
  use of plugins and tools to carry out tasks]]'
- '[[Changes/Claude Code/2026-10-16-3-apps-and-integrations-changes-in-v2-1-302|3
  Apps and Integrations changes in v2.1.302]]'
source_release: '[[Releases/Claude Code/claude-code-2026-10-19-v2-1-304-github-417677344-46c4d994|claude-code-2026-10-19-v2-1-304-github-417677344-46c4d994]]'
source_type: github_releases
theme: apps-integrations
title: 8 Apps and Integrations changes in v2.1.304
type: change
---

<!-- chronolog:begin region="header" -->
# 8 Apps and Integrations changes in v2.1.304

**Claude Code** · 2026-10-19 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.304) · from [[Releases/Claude Code/claude-code-2026-10-19-v2-1-304-github-417677344-46c4d994|v2.1.304]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added a transcript line when a plugin that runs first skips one of your mod's hooks, naming the event and the plugin

> Improved cloud sessions: a new conversation's first turn no longer waits for the local (stdio) MCP servers of plugins synced from claude.ai, unless a server sets `alwaysLoad: true`

> Improved resume of large compacted sessions in SDK and headless mode: the first request after resuming is sent sooner

> Changed mods' `settings.read` hooks to receive each settings layer and rewrite the merged settings, so a managed mod can make an organization's setting a ceiling, including the `cleanupPeriodDays` the retention sweep uses

> Changed skill hooks: the skills of one source (a repo, your own folder, or a plugin) can register at most 1,024 hooks and 16,384 matcher characters per session

> Changed skills under a policy that allows hooks from plugins only: a skill used in the main conversation whose hooks are kept out no longer gets its `allowed-tools`

> Updated the /claude-api skill to use the `ant` CLI on Claude Platform on AWS instead of falling back to the SDK or curl

> Removed the notes from `claude plugin validate` that predicted where a mod's hooks would run

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.304
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-10-19-added-a-warning-on-pro-and-max-plans-when-resuming-an-inactive-conversation-woul|Added a warning on Pro and Max plans when resuming an inactive conversation would…]] · Collaboration
- [[Changes/Claude Code/2026-10-19-windows-improved-git-command-start-up-with-a-standard-git-for-windows-install-by|Windows: Improved git command start-up with a standard Git for Windows install…]] · Mobile and Desktop
- [[Changes/Claude Code/2026-10-19-3-context-window-changes-in-v2-1-304|3 Context Window changes in v2.1.304]] · Context Window
- [[Changes/Claude Code/2026-10-19-2-agent-mode-changes-in-v2-1-304|2 Agent Mode changes in v2.1.304]] · Agent Mode
- [[Changes/Claude Code/2026-10-19-3-developer-workflow-changes-in-v2-1-304|3 Developer Workflow changes in v2.1.304]] · Developer Workflow
- [[Changes/Claude Code/2026-10-19-added-decider-person-to-a-mod-s-tool-check-answer-only-the-permission-dialog-or|Added decider: "person" to a mod's tool.check answer: only the permission dialog…]] · Safety and Privacy
- [[Changes/Claude Code/2026-10-19-added-claude-api-managed-agents-secure-which-compares-a-managed-agents-agent-s-s|Added /claude-api managed-agents-secure, which compares a Managed Agents agent's…]] · Agent Mode
- [[Changes/Claude Code/2026-10-19-2-model-support-changes-in-v2-1-304|2 Model Support changes in v2.1.304]] · Model Support
- [[Changes/Claude Code/2026-10-19-2-reliability-and-performance-changes-in-v2-1-304|2 Reliability and Performance changes in v2.1.304]] · Reliability and Performance
- [[Changes/Claude Code/2026-10-19-9-other-changes-in-v2-1-304|9 other changes in v2.1.304]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-10-16 · Claude Code · [[Changes/Claude Code/2026-10-16-3-apps-and-integrations-changes-in-v2-1-302|3 Apps and Integrations changes in v2.1.302]]
- Later: 2026-10-20 · Claude Code · [[Changes/Claude Code/2026-10-20-4-apps-and-integrations-changes-in-v2-1-305|4 Apps and Integrations changes in v2.1.305]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-10-19-89bbac&body=Card%3A%20Changes%2FClaude%20Code%2F2026-10-19-8-apps-and-integrations-changes-in-v2-1-304.md%0ACard%20ID%3A%20claude-code-2026-10-19-89bbac%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.304%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->