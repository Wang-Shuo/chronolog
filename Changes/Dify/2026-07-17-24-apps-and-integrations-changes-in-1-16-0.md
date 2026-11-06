---
card_id: dify-2026-07-17-6ae0e2
date: '2026-07-17'
description: 'Dify · 2026-07-17 · Apps and Integrations: 24 changes in v1.16.0 — Dify
  Workflow integration for Dify Agent'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1212
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 4eb21eee46cbefb8b48b62b8db898d4483cebe3e1a54ae6767f78a39b2f658f6
product: dify
product_name: Dify
record:
  card_id: dify-2026-07-17-6ae0e2
  comparison: ''
  date: '2026-07-17'
  description: 'Dify — v1.16.0: 24 Apps and Integrations changes'
  evidence:
  - quote: Dify Workflow integration for Dify Agent
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: '**MCP Protocol Upgrade**'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: Reduced database load by caching setup status, compressing large plugin
      model objects in Redis with zstd, and retrieving published workflows via direct
      foreign key
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: '| `DIFY_AGENT_PLUGIN_DAEMON_URL` | _(empty, derived from `PLUGIN_DAEMON_URL`)_
      | `docker/envs/core-services/dify-agent.env.example` | Plugin daemon URL for
      Dify Agent |'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: '| `DIFY_AGENT_PLUGIN_DAEMON_API_KEY` | _(empty, derived from `PLUGIN_DAEMON_KEY`)_
      | `docker/envs/core-services/dify-agent.env.example` | Plugin daemon API key
      for Dify Agent |'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: '| `DIFY_AGENT_INNER_API_URL` | _(empty, derived from `PLUGIN_DIFY_INNER_API_URL`)_
      | `docker/envs/core-services/dify-agent.env.example` | Inner API URL for Dify
      Agent |'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: '| `DIFY_AGENT_INNER_API_KEY` | _(empty)_ | `docker/envs/core-services/dify-agent.env.example`
      | Inner API key (must match `INNER_API_KEY_FOR_PLUGIN`, not `INNER_API_KEY`)
      |'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: '| `NEW_USER_DEFAULT_PLUGIN_IDS` | _(empty)_ | `api/.env.example` | Comma-separated
      plugin IDs to auto-install for new users |'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: 'feat(mcp): support dynamic HTTP request headers in MCPClient by @Sanket2329
      in https://github.com/langgenius/dify/pull/37938'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: 'refactor(web): migrate plugin console contracts by @hyoban in https://github.com/langgenius/dify/pull/38252'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: 'chore: compress large plugin_model obj in redis by @hjlarry in https://github.com/langgenius/dify/pull/38374'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: 'chore: use zstd for plugin model provider cache by @hjlarry in https://github.com/langgenius/dify/pull/38382'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: 'refactor(api): clarify DSL import and plugin migration boundaries by @WH-2099
      in https://github.com/langgenius/dify/pull/38483'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: 'feat(mcp): support MCP protocol 2025-06-18 for workflow-as-MCP server
      (version negotiation + structured output) by @CourTeous33 in https://github.com/langgenius/dify/pull/37892'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: 'test(services): cover DSL import and plugin migration regressions by @Lillian68
      in https://github.com/langgenius/dify/pull/36072'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: 'perf(web): lazy-load Vite plugins by @hyoban in https://github.com/langgenius/dify/pull/38663'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: 'test: use sqlite3 session in test_plugin_tool by @asukaminato0721 in https://github.com/langgenius/dify/pull/38781'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: 'chore: simplify lint plugin configuration by @hyoban in https://github.com/langgenius/dify/pull/38872'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: 'test: use sqlite3 session in test_plugin by @asukaminato0721 in https://github.com/langgenius/dify/pull/38710'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: 'test: move plugin service coverage to unit tests by @asukaminato0721 in
      https://github.com/langgenius/dify/pull/38935'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: 'test: remove duplicate code executor integration coverage by @asukaminato0721
      in https://github.com/langgenius/dify/pull/38947'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: 'test: move MCP controller coverage to unit tests by @asukaminato0721 in
      https://github.com/langgenius/dify/pull/38930'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: 'test: move plugin parameter service coverage to unit tests by @asukaminato0721
      in https://github.com/langgenius/dify/pull/38934'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: 'feat: default plugins for new user by @hjlarry in https://github.com/langgenius/dify/pull/39167'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 24-apps-and-integrations-changes-in-1-16-0
  source_release: dify-2026-07-17-1-16-0-github-355594285-636849e9
  source_type: github_releases
  theme: apps-integrations
  title: 24 Apps and Integrations changes in 1.16.0
  type: change
related_changes:
- '[[Changes/Claude Code/2026-07-17-mcp-tool-calls-running-longer-than-2-minutes-now-move-to-the-background-automati|MCP
  tool calls running longer than 2 minutes now move to the background…]]'
- '[[Changes/Cursor/2026-07-17-cursor-in-slack-now-shares-a-plan-before-it-starts-runs-in-multi-repo-environmen|Cursor
  in Slack now shares a plan before it starts, runs in multi-repo environments…]]'
- '[[Changes/Cursor/2026-07-17-multi-repo-environment-support-4b706e|Multi-repo environment
  support]]'
source_release: '[[Releases/Dify/dify-2026-07-17-1-16-0-github-355594285-636849e9|dify-2026-07-17-1-16-0-github-355594285-636849e9]]'
source_type: github_releases
theme: apps-integrations
title: 24 Apps and Integrations changes in 1.16.0
type: change
---

<!-- chronolog:begin region="header" -->
# 24 Apps and Integrations changes in 1.16.0

**Dify** · 2026-07-17 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.16.0) · from [[Releases/Dify/dify-2026-07-17-1-16-0-github-355594285-636849e9|v1.16.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Dify Workflow integration for Dify Agent

> **MCP Protocol Upgrade**

> Reduced database load by caching setup status, compressing large plugin model objects in Redis with zstd, and retrieving published workflows via direct foreign key

> | `DIFY_AGENT_PLUGIN_DAEMON_URL` | _(empty, derived from `PLUGIN_DAEMON_URL`)_ | `docker/envs/core-services/dify-agent.env.example` | Plugin daemon URL for Dify Agent |

> | `DIFY_AGENT_PLUGIN_DAEMON_API_KEY` | _(empty, derived from `PLUGIN_DAEMON_KEY`)_ | `docker/envs/core-services/dify-agent.env.example` | Plugin daemon API key for Dify Agent |

> | `DIFY_AGENT_INNER_API_URL` | _(empty, derived from `PLUGIN_DIFY_INNER_API_URL`)_ | `docker/envs/core-services/dify-agent.env.example` | Inner API URL for Dify Agent |

> | `DIFY_AGENT_INNER_API_KEY` | _(empty)_ | `docker/envs/core-services/dify-agent.env.example` | Inner API key (must match `INNER_API_KEY_FOR_PLUGIN`, not `INNER_API_KEY`) |

> | `NEW_USER_DEFAULT_PLUGIN_IDS` | _(empty)_ | `api/.env.example` | Comma-separated plugin IDs to auto-install for new users |

> feat(mcp): support dynamic HTTP request headers in MCPClient by @Sanket2329 in https://github.com/langgenius/dify/pull/37938

> refactor(web): migrate plugin console contracts by @hyoban in https://github.com/langgenius/dify/pull/38252

> chore: compress large plugin_model obj in redis by @hjlarry in https://github.com/langgenius/dify/pull/38374

> chore: use zstd for plugin model provider cache by @hjlarry in https://github.com/langgenius/dify/pull/38382

> refactor(api): clarify DSL import and plugin migration boundaries by @WH-2099 in https://github.com/langgenius/dify/pull/38483

> feat(mcp): support MCP protocol 2025-06-18 for workflow-as-MCP server (version negotiation + structured output) by @CourTeous33 in https://github.com/langgenius/dify/pull/37892

> test(services): cover DSL import and plugin migration regressions by @Lillian68 in https://github.com/langgenius/dify/pull/36072

> perf(web): lazy-load Vite plugins by @hyoban in https://github.com/langgenius/dify/pull/38663

> test: use sqlite3 session in test_plugin_tool by @asukaminato0721 in https://github.com/langgenius/dify/pull/38781

> chore: simplify lint plugin configuration by @hyoban in https://github.com/langgenius/dify/pull/38872

> test: use sqlite3 session in test_plugin by @asukaminato0721 in https://github.com/langgenius/dify/pull/38710

> test: move plugin service coverage to unit tests by @asukaminato0721 in https://github.com/langgenius/dify/pull/38935

> test: remove duplicate code executor integration coverage by @asukaminato0721 in https://github.com/langgenius/dify/pull/38947

> test: move MCP controller coverage to unit tests by @asukaminato0721 in https://github.com/langgenius/dify/pull/38930

> test: move plugin parameter service coverage to unit tests by @asukaminato0721 in https://github.com/langgenius/dify/pull/38934

> feat: default plugins for new user by @hjlarry in https://github.com/langgenius/dify/pull/39167

Source: https://github.com/langgenius/dify/releases/tag/1.16.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2026-07-17-20-safety-and-privacy-changes-in-1-16-0|20 Safety and Privacy changes in 1.16.0]] · Safety and Privacy
- [[Changes/Dify/2026-07-17-agent-app-enters-open-beta-and-is-now-enabled-by-default-for-all-users-it-introd|Agent App enters open beta and is now enabled by default for all users]] · Safety and Privacy
- [[Changes/Dify/2026-07-17-16-context-window-changes-in-1-16-0|16 Context Window changes in 1.16.0]] · Context Window
- [[Changes/Dify/2026-07-17-perf-memory-batch-load-message-files-in-tokenbuffermemory-to-remove-n-1-queries|perf(memory): batch-load message files in TokenBufferMemory to remove N+1 queries]] · Memory and Personalization
- [[Changes/Dify/2026-07-17-8-account-and-access-changes-in-1-16-0|8 Account and Access changes in 1.16.0]] · Account and Access
- [[Changes/Dify/2026-07-17-4-editor-experience-changes-in-1-16-0|4 Editor Experience changes in 1.16.0]] · Editor Experience
- [[Changes/Dify/2026-07-17-3-voice-and-audio-changes-in-1-16-0|3 Voice and Audio changes in 1.16.0]] · Voice and Audio
- [[Changes/Dify/2026-07-17-4-collaboration-changes-in-1-16-0|4 Collaboration changes in 1.16.0]] · Collaboration
- [[Changes/Dify/2026-07-17-3-developer-workflow-changes-in-1-16-0|3 Developer Workflow changes in 1.16.0]] · Developer Workflow
- [[Changes/Dify/2026-07-17-2-automation-and-scheduling-changes-in-1-16-0|2 Automation and Scheduling changes in 1.16.0]] · Automation and Scheduling
- [[Changes/Dify/2026-07-17-2-interface-experience-changes-in-1-16-0|2 Interface Experience changes in 1.16.0]] · Interface Experience
- [[Changes/Dify/2026-07-17-2-files-and-data-changes-in-1-16-0|2 Files and Data changes in 1.16.0]] · Files and Data
- [[Changes/Dify/2026-07-17-12-model-support-changes-in-1-16-0|12 Model Support changes in 1.16.0]] · Model Support
- [[Changes/Dify/2026-07-17-chore-improve-workflow-generator-accessibility-and-api-contracts-by-crazywoola-i|chore: Improve workflow generator accessibility and API contracts]] · Accessibility and Localization
- [[Changes/Dify/2026-07-17-2-enterprise-and-administration-changes-in-1-16-0|2 Enterprise and Administration changes in 1.16.0]] · Enterprise and Administration
- [[Changes/Dify/2026-07-17-3-reliability-and-performance-changes-in-1-16-0|3 Reliability and Performance changes in 1.16.0]] · Reliability and Performance
- [[Changes/Dify/2026-07-17-64-agent-mode-changes-in-1-16-0|64 Agent Mode changes in 1.16.0]] · Agent Mode
- [[Changes/Dify/2026-07-17-5-pricing-model-changes-in-1-16-0|5 Pricing Model changes in 1.16.0]] · Pricing Model
- [[Changes/Dify/2026-07-17-237-other-changes-in-1-16-0|237 other changes in 1.16.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-07-17 · Cursor · [[Changes/Cursor/2026-07-17-multi-repo-environment-support-4b706e|Multi-repo environment support]]
- Later: 2026-07-17 · Replit · [[Changes/Replit/2026-07-17-integrations|Integrations]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-07-17-6ae0e2&body=Card%3A%20Changes%2FDify%2F2026-07-17-24-apps-and-integrations-changes-in-1-16-0.md%0ACard%20ID%3A%20dify-2026-07-17-6ae0e2%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.16.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->