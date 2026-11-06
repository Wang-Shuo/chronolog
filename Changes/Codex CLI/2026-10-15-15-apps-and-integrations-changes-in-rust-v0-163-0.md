---
card_id: codex-cli-2026-10-15-46ffdb
date: '2026-10-15'
description: 'Codex CLI · 2026-10-15 · Apps and Integrations: 15 changes in 0.163.0
  — #51611 Signal abandonment of unanswered MCP elicitations @nicksteele-oai'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1302
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 86c0ba12791a5cc52ae9c8ba53c0629d3eb20da89e085dfed07c5259b17aef16
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-10-15-46ffdb
  comparison: ''
  date: '2026-10-15'
  description: 'Codex CLI — 0.163.0: 15 Apps and Integrations changes'
  evidence:
  - quote: '#51611 Signal abandonment of unanswered MCP elicitations @nicksteele-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#51755 Reuse MCP handler metadata for cache comparisons @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#51808 Preserve diagnostic reasons for MCP user verification failures
      @berkdeniz-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#51823 Share MCP binding tool metadata with prepared calls @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#51865 Use readable plugin mentions without suppressing same-name skills
      @canvrno-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#51890 Add the missing `mxc-sdk` UTF-8 resource patch for Bazel @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#52200 Allow plugin toggles while searching and preserve filters on refresh
      @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#52215 Enforce application network policy in standalone MCP commands @lsingh-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#52220 Add configurable default plugin activation policy @stevenlee-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#52250 Add opt-in Guardian trust for orchestrator connector identities
      @ankushg'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#52304 Persist remote-control RPC preferences in managed daemon settings
      @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#52661 Prevent brokered credential aliases from bypassing MITM hooks @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#53109 Handle broken pipes gracefully in plugin list output @fcoury-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#53358 Remove selected protocol, apply-patch, MCP, and TUI tests @vb-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#53672 Keep discovered Apps tools available during startup recovery @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 15-apps-and-integrations-changes-in-rust-v0-163-0
  source_release: codex-cli-2026-10-15-rust-v0-163-0-github-414286110-97016fe6
  source_type: github_releases
  theme: apps-integrations
  title: 15 Apps and Integrations changes in rust-v0.163.0
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-10-14-2-apps-and-integrations-changes-in-v1-0-98|2
  Apps and Integrations changes in v1.0.98]]'
- '[[Changes/Lovable/2026-10-14-connect-your-app-to-bing-webmaster-tools|Connect your
  app to Bing Webmaster Tools]]'
- '[[Changes/Open WebUI/2026-10-14-2-apps-and-integrations-changes-in-v0-12-1|2 Apps
  and Integrations changes in v0.12.1]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-10-15-rust-v0-163-0-github-414286110-97016fe6|codex-cli-2026-10-15-rust-v0-163-0-github-414286110-97016fe6]]'
source_type: github_releases
theme: apps-integrations
title: 15 Apps and Integrations changes in rust-v0.163.0
type: change
---

<!-- chronolog:begin region="header" -->
# 15 Apps and Integrations changes in rust-v0.163.0

**Codex CLI** · 2026-10-15 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.163.0) · from [[Releases/Codex CLI/codex-cli-2026-10-15-rust-v0-163-0-github-414286110-97016fe6|0.163.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> #51611 Signal abandonment of unanswered MCP elicitations @nicksteele-oai

> #51755 Reuse MCP handler metadata for cache comparisons @owenlin0

> #51808 Preserve diagnostic reasons for MCP user verification failures @berkdeniz-oai

> #51823 Share MCP binding tool metadata with prepared calls @owenlin0

> #51865 Use readable plugin mentions without suppressing same-name skills @canvrno-oai

> #51890 Add the missing `mxc-sdk` UTF-8 resource patch for Bazel @iceweasel-oai

> #52200 Allow plugin toggles while searching and preserve filters on refresh @fcoury-oai

> #52215 Enforce application network policy in standalone MCP commands @lsingh-oai

> #52220 Add configurable default plugin activation policy @stevenlee-oai

> #52250 Add opt-in Guardian trust for orchestrator connector identities @ankushg

> #52304 Persist remote-control RPC preferences in managed daemon settings @etraut-openai

> #52661 Prevent brokered credential aliases from bypassing MITM hooks @viyatb-oai

> #53109 Handle broken pipes gracefully in plugin list output @fcoury-oai

> #53358 Remove selected protocol, apply-patch, MCP, and TUI tests @vb-openai

> #53672 Keep discovered Apps tools available during startup recovery @jif-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.163.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-10-15-3-mobile-and-desktop-changes-in-rust-v0-163-0|3 Mobile and Desktop changes in rust-v0.163.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-10-15-6-model-support-changes-in-rust-v0-163-0|6 Model Support changes in rust-v0.163.0]] · Model Support
- [[Changes/Codex CLI/2026-10-15-18-safety-and-privacy-changes-in-rust-v0-163-0|18 Safety and Privacy changes in rust-v0.163.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-10-15-4-collaboration-changes-in-rust-v0-163-0|4 Collaboration changes in rust-v0.163.0]] · Collaboration
- [[Changes/Codex CLI/2026-10-15-codex-can-run-independent-read-only-tools-in-parallel-including-skill-memory-and|Codex can run independent read-only tools in parallel, including skill, memory…]] · Memory and Personalization
- [[Changes/Codex CLI/2026-10-15-15-developer-workflow-changes-in-rust-v0-163-0|15 Developer Workflow changes in rust-v0.163.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-10-15-4-voice-and-audio-changes-in-rust-v0-163-0|4 Voice and Audio changes in rust-v0.163.0]] · Voice and Audio
- [[Changes/Codex CLI/2026-10-15-4-editor-experience-changes-in-rust-v0-163-0|4 Editor Experience changes in rust-v0.163.0]] · Editor Experience
- [[Changes/Codex CLI/2026-10-15-16-context-window-changes-in-rust-v0-163-0|16 Context Window changes in rust-v0.163.0]] · Context Window
- [[Changes/Codex CLI/2026-10-15-8-interface-experience-changes-in-rust-v0-163-0|8 Interface Experience changes in rust-v0.163.0]] · Interface Experience
- [[Changes/Codex CLI/2026-10-15-14-agent-mode-changes-in-rust-v0-163-0|14 Agent Mode changes in rust-v0.163.0]] · Agent Mode
- [[Changes/Codex CLI/2026-10-15-53389-use-cached-login-credentials-for-guardian-decisions-swastik-oai|♯53389 Use cached login credentials for Guardian decisions @swastik-oai]] · Account and Access
- [[Changes/Codex CLI/2026-10-15-134-other-changes-in-rust-v0-163-0|134 other changes in rust-v0.163.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-10-14 · Open WebUI · [[Changes/Open WebUI/2026-10-14-2-apps-and-integrations-changes-in-v0-12-1|2 Apps and Integrations changes in v0.12.1]]
- Later: 2026-10-16 · ChatGPT · [[Changes/ChatGPT/2026-10-16-improved-use-of-plugins-and-tools-to-carry-out-tasks|Improved use of plugins and tools to carry out tasks]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-10-15-46ffdb&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-10-15-15-apps-and-integrations-changes-in-rust-v0-163-0.md%0ACard%20ID%3A%20codex-cli-2026-10-15-46ffdb%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.163.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->