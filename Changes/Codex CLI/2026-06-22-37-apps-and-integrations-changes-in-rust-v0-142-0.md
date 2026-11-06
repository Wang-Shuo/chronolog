---
card_id: codex-cli-2026-06-22-a9ed64
date: '2026-06-22'
description: 'Codex CLI · 2026-06-22 · Apps and Integrations: 37 changes in 0.142.0
  — `/plugins` now organizes remote plugins into OpenAI Curated, Workspace, and Shared
  with…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1187
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 2c96208d750ad73d9aabf0191b888cba254e465b5cca47115be2c1b99945207a
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-06-22-a9ed64
  comparison: ''
  date: '2026-06-22'
  description: 'Codex CLI — 0.142.0: 37 Apps and Integrations changes'
  evidence:
  - quote: '`/plugins` now organizes remote plugins into OpenAI Curated, Workspace,
      and Shared with me sections, while eligible turns can recommend and install
      relevant plugins. (#26703, #28399, #28400, #27704, #28403)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: 'Exec-server processes and stdio MCP sessions now survive transient disconnects,
      including signed-URL refresh and retry-safe stdin writes. (#28512, #28374, #28546,
      #28895)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: 'Plugin loading and installation now handle root marketplace layouts, manifest
      fallbacks, multiple skill paths, actionable download errors, and immediate tool
      refreshes. (#28771, #28789, #28790, #28863, #28951)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: 'Reduced startup and session latency by deferring unnecessary DNS work,
      warming the model cache, reusing parsed plugin skills, parallelizing skill metadata
      reads, and skipping redundant catalog synchronization. (#28542, #28699, #28844,
      #29326, #29005)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28508 [tests] Keep Apps out of generic core test harness @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28472 [codex] Clarify plugin load and runtime capability stages @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#27099 [codex-app-server-test-client & codex-app-server] Plugin Usage
      Analytics Smoke Test @jameswt-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#27923 [codex] Route MCP file uploads through environment filesystem @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#27100 [codex-app-server-test-client] Plugin Install/Uninstall Analytics
      Smoke Test @jameswt-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28581 [codex] re-enable absolute workdir integration test @anp-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28399 [codex] [1/4] Add recommended plugin endpoint cache @adaley-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28400 [codex] [2/4] Generalize plugin suggestion presentation @adaley-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#27704 [codex] [3/4] Activate endpoint plugin recommendations @adaley-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28403 [codex] [4/4] Simplify recommended plugin install schema @adaley-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28625 [codex] Gate remote plugin catalog by auth @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28580 [codex] Support object-valued plugin MCP manifests @charlesgong-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#27965 [ez][codex-rs] Support apps._default.default_tools_approval_mode
      @zamoshchin-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28768 Extract TUI plugin catalog rendering @canvrno-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28731 [codex] Track plugin install and import telemetry failures @charlesgong-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28771 fix(plugins): support root local marketplace plugins @caseychow-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28790 [codex] Support plugin manifest path lists @charlesgong-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28605 [codex] Split plugin and skill warmup tracing @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28608 [codex] Pass plugin namespace into skill loading @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#27812 [codex] Cache plugin metadata for tool suggestions @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#27132 Emit Trusted MCP App Identity on Tool-Call Items @martinauyeung-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28863 [codex] Preserve remote plugin download status errors @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28789 [codex] Support marketplace plugin manifest fallback @charlesgong-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28844 [codex] Reuse parsed plugin skills during session startup @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28951 [plugins] Refresh plugin and tool caches after remote install @adaley-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#29005 [codex] Skip curated repo sync for remote plugins @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#28942 Add config toggles for orchestrator skills and MCP @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#29154 Allow resume and settings commands during tasks and MCP startup
      @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#29259 [codex] prototype mcp_history thread hint injection @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#27102 [codex] Centralize Plugin Analytics Metadata @jameswt-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#26703 TUI Plugin Sharing 3 - render remote plugin catalog sections @canvrno-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#29464 [sdk/python] Stop advertising HTTP image URLs @rka-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  - quote: '#27669 [codex-core-plugins] Remote Plugin ID Persisted to File @jameswt-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.142.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 37-apps-and-integrations-changes-in-rust-v0-142-0
  source_release: codex-cli-2026-06-22-rust-v0-142-0-github-343189954-a218ab4e
  source_type: github_releases
  theme: apps-integrations
  title: 37 Apps and Integrations changes in rust-v0.142.0
  type: change
related_changes:
- '[[Changes/Replit/2026-06-19-new-mcp-servers-apollo-and-black-forest-labs|New MCP
  servers: Apollo and Black Forest Labs]]'
- '[[Changes/Replit/2026-06-19-use-replit-from-claude|Use Replit from Claude]]'
- '[[Changes/Claude Code/2026-06-22-2-apps-and-integrations-changes-in-v2-1-186|2
  Apps and Integrations changes in v2.1.186]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-06-22-rust-v0-142-0-github-343189954-a218ab4e|codex-cli-2026-06-22-rust-v0-142-0-github-343189954-a218ab4e]]'
source_type: github_releases
theme: apps-integrations
title: 37 Apps and Integrations changes in rust-v0.142.0
type: change
---

<!-- chronolog:begin region="header" -->
# 37 Apps and Integrations changes in rust-v0.142.0

**Codex CLI** · 2026-06-22 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.142.0) · from [[Releases/Codex CLI/codex-cli-2026-06-22-rust-v0-142-0-github-343189954-a218ab4e|0.142.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> `/plugins` now organizes remote plugins into OpenAI Curated, Workspace, and Shared with me sections, while eligible turns can recommend and install relevant plugins. (#26703, #28399, #28400, #27704, #28403)

> Exec-server processes and stdio MCP sessions now survive transient disconnects, including signed-URL refresh and retry-safe stdin writes. (#28512, #28374, #28546, #28895)

> Plugin loading and installation now handle root marketplace layouts, manifest fallbacks, multiple skill paths, actionable download errors, and immediate tool refreshes. (#28771, #28789, #28790, #28863, #28951)

> Reduced startup and session latency by deferring unnecessary DNS work, warming the model cache, reusing parsed plugin skills, parallelizing skill metadata reads, and skipping redundant catalog synchronization. (#28542, #28699, #28844, #29326, #29005)

> #28508 [tests] Keep Apps out of generic core test harness @jif-oai

> #28472 [codex] Clarify plugin load and runtime capability stages @xl-openai

> #27099 [codex-app-server-test-client & codex-app-server] Plugin Usage Analytics Smoke Test @jameswt-oai

> #27923 [codex] Route MCP file uploads through environment filesystem @pakrym-oai

> #27100 [codex-app-server-test-client] Plugin Install/Uninstall Analytics Smoke Test @jameswt-oai

> #28581 [codex] re-enable absolute workdir integration test @anp-oai

> #28399 [codex] [1/4] Add recommended plugin endpoint cache @adaley-openai

> #28400 [codex] [2/4] Generalize plugin suggestion presentation @adaley-openai

> #27704 [codex] [3/4] Activate endpoint plugin recommendations @adaley-openai

> #28403 [codex] [4/4] Simplify recommended plugin install schema @adaley-openai

> #28625 [codex] Gate remote plugin catalog by auth @xl-openai

> #28580 [codex] Support object-valued plugin MCP manifests @charlesgong-openai

> #27965 [ez][codex-rs] Support apps._default.default_tools_approval_mode @zamoshchin-openai

> #28768 Extract TUI plugin catalog rendering @canvrno-oai

> #28731 [codex] Track plugin install and import telemetry failures @charlesgong-openai

> #28771 fix(plugins): support root local marketplace plugins @caseychow-oai

> #28790 [codex] Support plugin manifest path lists @charlesgong-openai

> #28605 [codex] Split plugin and skill warmup tracing @mzeng-openai

> #28608 [codex] Pass plugin namespace into skill loading @mzeng-openai

> #27812 [codex] Cache plugin metadata for tool suggestions @mzeng-openai

> #27132 Emit Trusted MCP App Identity on Tool-Call Items @martinauyeung-oai

> #28863 [codex] Preserve remote plugin download status errors @xl-openai

> #28789 [codex] Support marketplace plugin manifest fallback @charlesgong-openai

> #28844 [codex] Reuse parsed plugin skills during session startup @xl-openai

> #28951 [plugins] Refresh plugin and tool caches after remote install @adaley-openai

> #29005 [codex] Skip curated repo sync for remote plugins @xl-openai

> #28942 Add config toggles for orchestrator skills and MCP @jif-oai

> #29154 Allow resume and settings commands during tasks and MCP startup @etraut-openai

> #29259 [codex] prototype mcp_history thread hint injection @pakrym-oai

> #27102 [codex] Centralize Plugin Analytics Metadata @jameswt-oai

> #26703 TUI Plugin Sharing 3 - render remote plugin catalog sections @canvrno-oai

> #29464 [sdk/python] Stop advertising HTTP image URLs @rka-oai

> #27669 [codex-core-plugins] Remote Plugin ID Persisted to File @jameswt-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.142.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-06-22-12-safety-and-privacy-changes-in-rust-v0-142-0|12 Safety and Privacy changes in rust-v0.142.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-06-22-4-interface-experience-changes-in-rust-v0-142-0|4 Interface Experience changes in rust-v0.142.0]] · Interface Experience
- [[Changes/Codex CLI/2026-06-22-26496-make-auto-review-on-request-prompt-more-proactive-maja-openai|♯26496 Make auto-review on-request prompt more proactive @maja-openai]] · Automation and Scheduling
- [[Changes/Codex CLI/2026-06-22-usage-can-now-show-and-redeem-earned-usage-limit-reset-credits-with-confirmation|/usage can now show and redeem earned usage-limit reset credits…]] · Pricing Model
- [[Changes/Codex CLI/2026-06-22-28791-bazel-refresh-expired-macos-sdk-pin-anp-oai|♯28791 bazel: refresh expired macOS SDK pin @anp-oai]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-06-22-14-agent-mode-changes-in-rust-v0-142-0|14 Agent Mode changes in rust-v0.142.0]] · Agent Mode
- [[Changes/Codex CLI/2026-06-22-26707-pac-2-add-shared-auth-system-proxy-contract-canvrno-oai|♯26707 PAC 2 - Add shared auth system proxy contract @canvrno-oai]] · Collaboration
- [[Changes/Codex CLI/2026-06-22-4-developer-workflow-changes-in-rust-v0-142-0|4 Developer Workflow changes in rust-v0.142.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-06-22-10-context-window-changes-in-rust-v0-142-0|10 Context Window changes in rust-v0.142.0]] · Context Window
- [[Changes/Codex CLI/2026-06-22-29289-code-mode-preserve-initial-yield-at-completion-cconger|♯29289 code-mode: preserve initial yield at completion @cconger]] · Editor Experience
- [[Changes/Codex CLI/2026-06-22-2-reliability-and-performance-changes-in-rust-v0-142-0|2 Reliability and Performance changes in rust-v0.142.0]] · Reliability and Performance
- [[Changes/Codex CLI/2026-06-22-29022-codex-support-protected-resource-oauth-discovery-xl-openai|♯29022 codex Support protected resource OAuth discovery @xl-openai]] · Account and Access
- [[Changes/Codex CLI/2026-06-22-28770-connectors-ignore-synthetic-links-for-app-accessibility-adaley-openai|♯28770 connectors Ignore synthetic links for app accessibility @adaley-openai]] · Accessibility and Localization
- [[Changes/Codex CLI/2026-06-22-29086-document-raw-response-item-compatibility-jif-oai|♯29086 Document raw response item compatibility @jif-oai]] · Files and Data
- [[Changes/Codex CLI/2026-06-22-3-model-support-changes-in-rust-v0-142-0|3 Model Support changes in rust-v0.142.0]] · Model Support
- [[Changes/Codex CLI/2026-06-22-2-search-and-browsing-changes-in-rust-v0-142-0|2 Search and Browsing changes in rust-v0.142.0]] · Search and Browsing
- [[Changes/Codex CLI/2026-06-22-98-other-changes-in-rust-v0-142-0|98 other changes in rust-v0.142.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-06-22 · Claude Code · [[Changes/Claude Code/2026-06-22-2-apps-and-integrations-changes-in-v2-1-186|2 Apps and Integrations changes in v2.1.186]]
- Later: 2026-06-22 · Cursor · [[Changes/Cursor/2026-06-22-plugins-skills-and-mcps-let-you-customize-cursor-for-your-workflows-the-new-cust-241c4b|Plugins, skills, and MCPs let you customize Cursor for your workflows]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-06-22-a9ed64&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-06-22-37-apps-and-integrations-changes-in-rust-v0-142-0.md%0ACard%20ID%3A%20codex-cli-2026-06-22-a9ed64%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.142.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->