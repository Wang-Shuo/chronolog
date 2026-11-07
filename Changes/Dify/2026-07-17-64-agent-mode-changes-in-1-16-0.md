---
card_id: dify-2026-07-17-f949f3
date: '2026-07-17'
description: 'Dify · 2026-07-17 · Agent Mode: 64 changes in v1.16.0 — > You should
  provide Dify Agent services ⚠️**only to trusted, non-malicious users**⚠️.'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1107
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: c1acc8854e70237446b1b2c0bf1512c237295046483dc2317169de85c5bb4b13
product: dify
product_name: Dify
record:
  card_id: dify-2026-07-17-f949f3
  comparison: ''
  date: '2026-07-17'
  description: 'Dify — v1.16.0: 64 Agent Mode changes'
  evidence:
  - quote: '> You should provide Dify Agent services ⚠️**only to trusted, non-malicious
      users**⚠️.'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: As many of you know, the shell-based LLM agent paradigm has brought a major
      leap in agent capabilities and changed how we think about agents. Meanwhile,
      Skills provide a standardized way to package and distribute capabilities, making
      it easier to build powerful agents.
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: A builder for creating Dify Agents
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: 'You can build Dify Agents through the UI: set a base prompt, upload Skills
      and files, and connect tools and knowledge from the Dify ecosystem.'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: You can use an existing Dify Agent in a Dify Workflow, or temporarily create
      an inline Dify Agent. It will execute the task defined by the workflow node,
      generate the required output, and pass it to the next node.
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: The Dify Agent you build can be published and used as a web app. While
      the user experience remains familiar, it is now powered by Dify Agent.
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: 'Docs: https://docs.dify.ai/en/self-host/use-dify/build/new-agent/overview'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: '**Agent App (Open Beta)**'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: App owners can now customize the chat input placeholder text (up to 64
      chars) for Chatbot, Agent, and Chatflow web apps. The customization UI has been
      refined with clearer naming ("Custom Frontend" / "Branding") and better label
      handling. App descriptions are now displayed on chat and text-generation app
      screens with a collapsible view to avoid pushing the input form off screen.
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: '**Workflow & Agent**'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: '**Landlock protection**: Agent HOME directory protected with Landlock;
      downgraded to v1 for broader kernel compatibility'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: '| `AGENT_BACKEND_BASE_URL` | `http://localhost:5050` | `api/.env.example`
      | Base URL for the Agent backend service |'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: '| `AGENT_BACKEND_STREAM_READ_TIMEOUT_SECONDS` | `30` | `api/.env.example`
      | Stream read timeout for Agent backend |'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: '| `AGENT_BACKEND_STREAM_MAX_RECONNECTS` | `3` | `api/.env.example` | Max
      reconnection attempts for Agent backend streams |'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: '| `AGENT_BACKEND_RUN_TIMEOUT_SECONDS` | `1200` | `api/.env.example` |
      Overall run timeout for Agent backend |'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: '| `DIFY_AGENT_REDIS_URL` | _(empty, derived from `REDIS_PASSWORD`)_ |
      `docker/envs/core-services/dify-agent.env.example` | Redis URL for Dify Agent
      |'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: '| `DIFY_AGENT_REDIS_PREFIX` | `dify-agent` | `docker/envs/core-services/dify-agent.env.example`
      | Redis key prefix for Dify Agent |'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: '| `DIFY_AGENT_SHUTDOWN_GRACE_SECONDS` | `30` | `docker/envs/core-services/dify-agent.env.example`
      | Grace period before forced shutdown |'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: '| `DIFY_AGENT_RUN_RETENTION_SECONDS` | `259200` | `docker/envs/core-services/dify-agent.env.example`
      | Retention period for agent run records |'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: '| `DIFY_AGENT_SHELLCTL_ENTRYPOINT` | `http://local_sandbox:5004` | `docker/envs/core-services/dify-agent.env.example`
      | Shellctl entrypoint URL |'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: '| `DIFY_AGENT_SHELLCTL_AUTH_TOKEN` | _(empty)_ | `docker/envs/core-services/dify-agent.env.example`
      | Auth token for shellctl |'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: '| `DIFY_AGENT_STUB_API_BASE_URL` | `http://agent_backend:5050/agent-stub`
      | `docker/envs/core-services/dify-agent.env.example` | Base URL for Agent Stub
      API |'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: '| `DIFY_AGENT_SERVER_SECRET_KEY` | _(dev default)_ | `docker/envs/core-services/dify-agent.env.example`
      | JWE encryption key for Agent Stub bearer tokens. **Replace in production**
      with `python -c ''import secrets; print(secrets.token_urlsafe(32))''` |'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: '| `DIFY_AGENT_SHELL_REDACT_PATTERNS` | _(empty)_ | `docker/envs/core-services/dify-agent.env.example`
      | Patterns for redacting shell output |'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: '| `NEXT_PUBLIC_ENABLE_AGENT_V2` | `true` | `docker/envs/core-services/web.env.example`
      | Enable Agent App v2 (replaces `ENABLE_AGENT_V2`) |'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: '| `ENABLE_AGENT_V2` | `false` | `docker/envs/core-services/web.env.example`
      | Replaced by `NEXT_PUBLIC_ENABLE_AGENT_V2` (now defaults to `true`) |'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: '`api` and `worker` services now depend on `agent_backend`'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: '`2026_05_25_1143-97e2e1a644e8_add_workflow_version_to_workflow_agent_.py`'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: '`2026_06_12_1100-0b2f2c8a9d1e_add_agent_role.py`'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: '`2026_06_18_2300-b2515f9d4c2a_agent_drive_skill_metadata_refactor.py`'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: '`2026_06_24_2015-e4f5a6b7c8d9_add_agent_config_drafts.py`'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: '`2026_06_25_1100-a2b3c4d5e6f7_add_agent_backing_app_id.py`'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: '`2026_06_26_1000-c3d4e5f6a7b8_add_agent_active_config_is_published.py`'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: '> - **Docker Compose configuration changed significantly**: two new services
      (`agent_backend`, `local_sandbox`) were added. If you maintain a customized
      `docker-compose.yaml`, review the changes and re-apply local customizations
      carefully.'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: '> - **`DIFY_AGENT_SERVER_SECRET_KEY`** ships with a development default.
      **You must replace it in production** with a securely generated key: `python
      -c ''import secrets; print(secrets.token_urlsafe(32))''`'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: '> - **`ENABLE_AGENT_V2`** has been renamed to `NEXT_PUBLIC_ENABLE_AGENT_V2`
      and now defaults to `true`. Remove the old variable from your env files.'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: Review the new environment variables (especially `DIFY_AGENT_SERVER_SECRET_KEY`)
      and update your `.env` file. Re-apply any local customizations.
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: Configure the new Agent backend service. Refer to the `dify-agent` section
      in `docker/envs/core-services/dify-agent.env.example` for required environment
      variables.
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: 'feat(web): add customizable input placeholder for Agent/Chatflow/Chatbot
      web app by @CyberPU2099 in https://github.com/langgenius/dify/pull/37790'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: 'feat(agent-v2): sync nightly updates to main (2026-06-25) by @BeautyyuYanli
      in https://github.com/langgenius/dify/pull/37915'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: 'test(e2e): add agent v2 test infrastructure by @lyzno1 in https://github.com/langgenius/dify/pull/38191'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: 'build(deps): bump pydantic-ai-slim from 1.85.1 to 1.102.0 in /dify-agent
      by @dependabot[bot] in https://github.com/langgenius/dify/pull/38135'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: 'chore(agent-v2): sync daily changes by @lyzno1 in https://github.com/langgenius/dify/pull/38162'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: 'test(e2e): add agent v2 core coverage by @lyzno1 in https://github.com/langgenius/dify/pull/38209'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: 'feat(agent-v2): resolve Dify core tools in agent runtime runner by @linw1995
      in https://github.com/langgenius/dify/pull/38316'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: 'chore(agent-v2): sync daily changes by @lyzno1 in https://github.com/langgenius/dify/pull/38298'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: 'test(e2e): split agent build draft apply coverage by @lyzno1 in https://github.com/langgenius/dify/pull/38431'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: 'chore(agent-v2): sync changes by @lyzno1 in https://github.com/langgenius/dify/pull/38442'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: 'test(e2e): stabilize Agent v2 external runtime checks by @hyoban in https://github.com/langgenius/dify/pull/38493'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: 'test: scope agent build draft e2e selector by @lyzno1 in https://github.com/langgenius/dify/pull/38563'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: 'chore(agent-v2): sync changes by @lyzno1 in https://github.com/langgenius/dify/pull/38513'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: 'test(e2e): stabilize agent build draft note scenario by @lyzno1 in https://github.com/langgenius/dify/pull/38571'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: 'test(e2e): fix agent build note runtime connection by @lyzno1 in https://github.com/langgenius/dify/pull/38574'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: 'test(e2e): consume agent service API SSE incrementally by @lyzno1 in https://github.com/langgenius/dify/pull/38634'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: 'test: use sqlite3 session in test_agent_drive_service by @asukaminato0721
      in https://github.com/langgenius/dify/pull/38709'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: 'chore(deps): bump json-repair from 0.59.4 to 0.60.1 in /dify-agent by
      @dependabot[bot] in https://github.com/langgenius/dify/pull/38878'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: 'feat(agent): shellctl rewritten in go by @wylswz in https://github.com/langgenius/dify/pull/38841'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: 'feat(agent): support new Agent DSL import and export by @zyssyz123 in
      https://github.com/langgenius/dify/pull/38849'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: 'feat: new agent support import and export in frontend by @iamjoel in https://github.com/langgenius/dify/pull/39012'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: 'feat: protect agent HOME with landlock by @wylswz in https://github.com/langgenius/dify/pull/39000'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: 'chore: new agent enchance by @iamjoel in https://github.com/langgenius/dify/pull/39040'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: 'chore: remove useless agent tip by @iamjoel in https://github.com/langgenius/dify/pull/39171'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: 'chore: add agent tooltip by @iamjoel in https://github.com/langgenius/dify/pull/39183'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: 'feat: redact agent shell output by @wylswz in https://github.com/langgenius/dify/pull/39190'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 64-agent-mode-changes-in-1-16-0
  source_release: dify-2026-07-17-1-16-0-github-355594285-636849e9
  source_type: github_releases
  theme: agent-mode
  title: 64 Agent Mode changes in 1.16.0
  type: change
related_changes:
- '[[Changes/Notion/2026-07-16-your-agent-just-got-new-calendar-tools-to-show-and-manage-your-schedule-join-cal|Your
  agent just got new calendar tools to show and manage your schedule]]'
- '[[Changes/OpenCode/2026-07-16-desktop-fixed-custom-agent-selector-visibility-when-custom-agents-are-available|Desktop
  Fixed custom agent selector visibility when custom agents are available]]'
- '[[Changes/Claude Code/2026-07-17-7-agent-mode-changes-in-v2-1-212|7 Agent Mode
  changes in v2.1.212]]'
source_release: '[[Releases/Dify/dify-2026-07-17-1-16-0-github-355594285-636849e9|dify-2026-07-17-1-16-0-github-355594285-636849e9]]'
source_type: github_releases
theme: agent-mode
title: 64 Agent Mode changes in 1.16.0
type: change
---

<!-- chronolog:begin region="header" -->
# 64 Agent Mode changes in 1.16.0

**Dify** · 2026-07-17 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.16.0) · from [[Releases/Dify/dify-2026-07-17-1-16-0-github-355594285-636849e9|v1.16.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> > You should provide Dify Agent services ⚠️**only to trusted, non-malicious users**⚠️.

> As many of you know, the shell-based LLM agent paradigm has brought a major leap in agent capabilities and changed how we think about agents. Meanwhile, Skills provide a standardized way to package and distribute capabilities, making it easier to build powerful agents.

> A builder for creating Dify Agents

> You can build Dify Agents through the UI: set a base prompt, upload Skills and files, and connect tools and knowledge from the Dify ecosystem.

> You can use an existing Dify Agent in a Dify Workflow, or temporarily create an inline Dify Agent. It will execute the task defined by the workflow node, generate the required output, and pass it to the next node.

> The Dify Agent you build can be published and used as a web app. While the user experience remains familiar, it is now powered by Dify Agent.

> Docs: https://docs.dify.ai/en/self-host/use-dify/build/new-agent/overview

> **Agent App (Open Beta)**

> App owners can now customize the chat input placeholder text (up to 64 chars) for Chatbot, Agent, and Chatflow web apps. The customization UI has been refined with clearer naming ("Custom Frontend" / "Branding") and better label handling. App descriptions are now displayed on chat and text-generation app screens with a collapsible view to avoid pushing the input form off screen.

> **Workflow & Agent**

> **Landlock protection**: Agent HOME directory protected with Landlock; downgraded to v1 for broader kernel compatibility

> | `AGENT_BACKEND_BASE_URL` | `http://localhost:5050` | `api/.env.example` | Base URL for the Agent backend service |

> | `AGENT_BACKEND_STREAM_READ_TIMEOUT_SECONDS` | `30` | `api/.env.example` | Stream read timeout for Agent backend |

> | `AGENT_BACKEND_STREAM_MAX_RECONNECTS` | `3` | `api/.env.example` | Max reconnection attempts for Agent backend streams |

> | `AGENT_BACKEND_RUN_TIMEOUT_SECONDS` | `1200` | `api/.env.example` | Overall run timeout for Agent backend |

> | `DIFY_AGENT_REDIS_URL` | _(empty, derived from `REDIS_PASSWORD`)_ | `docker/envs/core-services/dify-agent.env.example` | Redis URL for Dify Agent |

> | `DIFY_AGENT_REDIS_PREFIX` | `dify-agent` | `docker/envs/core-services/dify-agent.env.example` | Redis key prefix for Dify Agent |

> | `DIFY_AGENT_SHUTDOWN_GRACE_SECONDS` | `30` | `docker/envs/core-services/dify-agent.env.example` | Grace period before forced shutdown |

> | `DIFY_AGENT_RUN_RETENTION_SECONDS` | `259200` | `docker/envs/core-services/dify-agent.env.example` | Retention period for agent run records |

> | `DIFY_AGENT_SHELLCTL_ENTRYPOINT` | `http://local_sandbox:5004` | `docker/envs/core-services/dify-agent.env.example` | Shellctl entrypoint URL |

> | `DIFY_AGENT_SHELLCTL_AUTH_TOKEN` | _(empty)_ | `docker/envs/core-services/dify-agent.env.example` | Auth token for shellctl |

> | `DIFY_AGENT_STUB_API_BASE_URL` | `http://agent_backend:5050/agent-stub` | `docker/envs/core-services/dify-agent.env.example` | Base URL for Agent Stub API |

> | `DIFY_AGENT_SERVER_SECRET_KEY` | _(dev default)_ | `docker/envs/core-services/dify-agent.env.example` | JWE encryption key for Agent Stub bearer tokens. **Replace in production** with `python -c 'import secrets; print(secrets.token_urlsafe(32))'` |

> | `DIFY_AGENT_SHELL_REDACT_PATTERNS` | _(empty)_ | `docker/envs/core-services/dify-agent.env.example` | Patterns for redacting shell output |

> | `NEXT_PUBLIC_ENABLE_AGENT_V2` | `true` | `docker/envs/core-services/web.env.example` | Enable Agent App v2 (replaces `ENABLE_AGENT_V2`) |

> | `ENABLE_AGENT_V2` | `false` | `docker/envs/core-services/web.env.example` | Replaced by `NEXT_PUBLIC_ENABLE_AGENT_V2` (now defaults to `true`) |

> `api` and `worker` services now depend on `agent_backend`

> `2026_05_25_1143-97e2e1a644e8_add_workflow_version_to_workflow_agent_.py`

> `2026_06_12_1100-0b2f2c8a9d1e_add_agent_role.py`

> `2026_06_18_2300-b2515f9d4c2a_agent_drive_skill_metadata_refactor.py`

> `2026_06_24_2015-e4f5a6b7c8d9_add_agent_config_drafts.py`

> `2026_06_25_1100-a2b3c4d5e6f7_add_agent_backing_app_id.py`

> `2026_06_26_1000-c3d4e5f6a7b8_add_agent_active_config_is_published.py`

> > - **Docker Compose configuration changed significantly**: two new services (`agent_backend`, `local_sandbox`) were added. If you maintain a customized `docker-compose.yaml`, review the changes and re-apply local customizations carefully.

> > - **`DIFY_AGENT_SERVER_SECRET_KEY`** ships with a development default. **You must replace it in production** with a securely generated key: `python -c 'import secrets; print(secrets.token_urlsafe(32))'`

> > - **`ENABLE_AGENT_V2`** has been renamed to `NEXT_PUBLIC_ENABLE_AGENT_V2` and now defaults to `true`. Remove the old variable from your env files.

> Review the new environment variables (especially `DIFY_AGENT_SERVER_SECRET_KEY`) and update your `.env` file. Re-apply any local customizations.

> Configure the new Agent backend service. Refer to the `dify-agent` section in `docker/envs/core-services/dify-agent.env.example` for required environment variables.

> feat(web): add customizable input placeholder for Agent/Chatflow/Chatbot web app by @CyberPU2099 in https://github.com/langgenius/dify/pull/37790

> feat(agent-v2): sync nightly updates to main (2026-06-25) by @BeautyyuYanli in https://github.com/langgenius/dify/pull/37915

> test(e2e): add agent v2 test infrastructure by @lyzno1 in https://github.com/langgenius/dify/pull/38191

> build(deps): bump pydantic-ai-slim from 1.85.1 to 1.102.0 in /dify-agent by @dependabot[bot] in https://github.com/langgenius/dify/pull/38135

> chore(agent-v2): sync daily changes by @lyzno1 in https://github.com/langgenius/dify/pull/38162

> test(e2e): add agent v2 core coverage by @lyzno1 in https://github.com/langgenius/dify/pull/38209

> feat(agent-v2): resolve Dify core tools in agent runtime runner by @linw1995 in https://github.com/langgenius/dify/pull/38316

> chore(agent-v2): sync daily changes by @lyzno1 in https://github.com/langgenius/dify/pull/38298

> test(e2e): split agent build draft apply coverage by @lyzno1 in https://github.com/langgenius/dify/pull/38431

> chore(agent-v2): sync changes by @lyzno1 in https://github.com/langgenius/dify/pull/38442

> test(e2e): stabilize Agent v2 external runtime checks by @hyoban in https://github.com/langgenius/dify/pull/38493

> test: scope agent build draft e2e selector by @lyzno1 in https://github.com/langgenius/dify/pull/38563

> chore(agent-v2): sync changes by @lyzno1 in https://github.com/langgenius/dify/pull/38513

> test(e2e): stabilize agent build draft note scenario by @lyzno1 in https://github.com/langgenius/dify/pull/38571

> test(e2e): fix agent build note runtime connection by @lyzno1 in https://github.com/langgenius/dify/pull/38574

> test(e2e): consume agent service API SSE incrementally by @lyzno1 in https://github.com/langgenius/dify/pull/38634

> test: use sqlite3 session in test_agent_drive_service by @asukaminato0721 in https://github.com/langgenius/dify/pull/38709

> chore(deps): bump json-repair from 0.59.4 to 0.60.1 in /dify-agent by @dependabot[bot] in https://github.com/langgenius/dify/pull/38878

> feat(agent): shellctl rewritten in go by @wylswz in https://github.com/langgenius/dify/pull/38841

> feat(agent): support new Agent DSL import and export by @zyssyz123 in https://github.com/langgenius/dify/pull/38849

> feat: new agent support import and export in frontend by @iamjoel in https://github.com/langgenius/dify/pull/39012

> feat: protect agent HOME with landlock by @wylswz in https://github.com/langgenius/dify/pull/39000

> chore: new agent enchance by @iamjoel in https://github.com/langgenius/dify/pull/39040

> chore: remove useless agent tip by @iamjoel in https://github.com/langgenius/dify/pull/39171

> chore: add agent tooltip by @iamjoel in https://github.com/langgenius/dify/pull/39183

> feat: redact agent shell output by @wylswz in https://github.com/langgenius/dify/pull/39190

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
- [[Changes/Dify/2026-07-17-24-apps-and-integrations-changes-in-1-16-0|24 Apps and Integrations changes in 1.16.0]] · Apps and Integrations
- [[Changes/Dify/2026-07-17-2-automation-and-scheduling-changes-in-1-16-0|2 Automation and Scheduling changes in 1.16.0]] · Automation and Scheduling
- [[Changes/Dify/2026-07-17-2-interface-experience-changes-in-1-16-0|2 Interface Experience changes in 1.16.0]] · Interface Experience
- [[Changes/Dify/2026-07-17-2-files-and-data-changes-in-1-16-0|2 Files and Data changes in 1.16.0]] · Files and Data
- [[Changes/Dify/2026-07-17-12-model-support-changes-in-1-16-0|12 Model Support changes in 1.16.0]] · Model Support
- [[Changes/Dify/2026-07-17-chore-improve-workflow-generator-accessibility-and-api-contracts-by-crazywoola-i|chore: Improve workflow generator accessibility and API contracts]] · Accessibility and Localization
- [[Changes/Dify/2026-07-17-2-enterprise-and-administration-changes-in-1-16-0|2 Enterprise and Administration changes in 1.16.0]] · Enterprise and Administration
- [[Changes/Dify/2026-07-17-3-reliability-and-performance-changes-in-1-16-0|3 Reliability and Performance changes in 1.16.0]] · Reliability and Performance
- [[Changes/Dify/2026-07-17-5-pricing-model-changes-in-1-16-0|5 Pricing Model changes in 1.16.0]] · Pricing Model
- [[Changes/Dify/2026-07-17-237-other-changes-in-1-16-0|237 other changes in 1.16.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-07-17 · Claude Code · [[Changes/Claude Code/2026-07-17-7-agent-mode-changes-in-v2-1-212|7 Agent Mode changes in v2.1.212]]
- Later: 2026-07-18 · Claude Code · [[Changes/Claude Code/2026-07-18-added-reasoning-effort-to-the-subagentstatusline-payload-so-custom-agent-rows-ca|Added reasoning effort to the subagentStatusLine payload, so custom agent rows can…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-07-17-f949f3&body=Card%3A%20Changes%2FDify%2F2026-07-17-64-agent-mode-changes-in-1-16-0.md%0ACard%20ID%3A%20dify-2026-07-17-f949f3%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.16.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->