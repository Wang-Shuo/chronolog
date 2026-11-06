---
card_id: codex-cli-2026-08-26-800154
date: '2026-08-26'
description: 'Codex CLI · 2026-08-26 · Agent Mode: 14 changes in 0.150.0 — #39722
  Track multi-agent v2 spawn calls in analytics @copyberry'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1147
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 085d54a3854daf4a54543a65eb956110f381c25fd5c54fc7090539359bf08845
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-08-26-800154
  comparison: ''
  date: '2026-08-26'
  description: 'Codex CLI — 0.150.0: 14 Agent Mode changes'
  evidence:
  - quote: '#39722 Track multi-agent v2 spawn calls in analytics @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.150.0
  - quote: '#39792 Reject settings updates for parent-owned subagents @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.150.0
  - quote: '#39804 Use multi-agent V1 for Amazon Bedrock models @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.150.0
  - quote: '#39870 Allow session configuration with `codex agents` @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.150.0
  - quote: '#39975 Preserve root user authorization in subagent Guardian reviews @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.150.0
  - quote: '#40221 Distinguish Guardian review threads from subagents @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.150.0
  - quote: '#40266 Preserve content annotations when filtering forked agent history
      @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.150.0
  - quote: '#40297 Preserve developer instruction annotations in subagent forks @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.150.0
  - quote: '#40437 Report completed sub-agent activity on parent turns @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.150.0
  - quote: '#40464 Enforce subagent ownership across app-server inputs @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.150.0
  - quote: '#40477 Reload Multi-Agent V2 children through their parent @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.150.0
  - quote: '#40487 Extract agent role loading into a dedicated crate @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.150.0
  - quote: '#40502 Collapse home paths in AGENTS.md status summaries @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.150.0
  - quote: '#40585 Track remaining multi-agent v2 tools in analytics @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.150.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 14-agent-mode-changes-in-rust-v0-150-0
  source_release: codex-cli-2026-08-26-rust-v0-150-0-github-377374683-d950f84c
  source_type: github_releases
  theme: agent-mode
  title: 14 Agent Mode changes in rust-v0.150.0
  type: change
related_changes:
- '[[Changes/Cline/2026-08-22-carry-session-and-client-identity-into-langfuse-traces-for-hub-backed-and-delega|Carry
  session and client identity into Langfuse traces for Hub-backed…]]'
- '[[Changes/Claude Code/2026-08-25-improved-subagent-results-a-subagent-that-stops-at-its-maxturns-limit-now-return|Improved
  subagent results]]'
- '[[Changes/Gemini CLI/2026-08-25-8-agent-mode-changes-in-v0-57-0|8 Agent Mode changes
  in v0.57.0]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-08-26-rust-v0-150-0-github-377374683-d950f84c|codex-cli-2026-08-26-rust-v0-150-0-github-377374683-d950f84c]]'
source_type: github_releases
theme: agent-mode
title: 14 Agent Mode changes in rust-v0.150.0
type: change
---

<!-- chronolog:begin region="header" -->
# 14 Agent Mode changes in rust-v0.150.0

**Codex CLI** · 2026-08-26 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.150.0) · from [[Releases/Codex CLI/codex-cli-2026-08-26-rust-v0-150-0-github-377374683-d950f84c|0.150.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> #39722 Track multi-agent v2 spawn calls in analytics @copyberry

> #39792 Reject settings updates for parent-owned subagents @copyberry

> #39804 Use multi-agent V1 for Amazon Bedrock models @copyberry

> #39870 Allow session configuration with `codex agents` @copyberry

> #39975 Preserve root user authorization in subagent Guardian reviews @copyberry

> #40221 Distinguish Guardian review threads from subagents @copyberry

> #40266 Preserve content annotations when filtering forked agent history @copyberry

> #40297 Preserve developer instruction annotations in subagent forks @copyberry

> #40437 Report completed sub-agent activity on parent turns @copyberry

> #40464 Enforce subagent ownership across app-server inputs @copyberry

> #40477 Reload Multi-Agent V2 children through their parent @copyberry

> #40487 Extract agent role loading into a dedicated crate @copyberry

> #40502 Collapse home paths in AGENTS.md status summaries @copyberry

> #40585 Track remaining multi-agent v2 tools in analytics @copyberry

Source: https://github.com/openai/codex/releases/tag/rust-v0.150.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-08-26-39953-support-voice-aware-configuration-and-version-skew-builds-copyberry|♯39953 Support voice-aware configuration and version-skew builds @copyberry]] · Voice and Audio
- [[Changes/Codex CLI/2026-08-26-6-interface-experience-changes-in-rust-v0-150-0|6 Interface Experience changes in rust-v0.150.0]] · Interface Experience
- [[Changes/Codex CLI/2026-08-26-10-model-support-changes-in-rust-v0-150-0|10 Model Support changes in rust-v0.150.0]] · Model Support
- [[Changes/Codex CLI/2026-08-26-24-apps-and-integrations-changes-in-rust-v0-150-0|24 Apps and Integrations changes in rust-v0.150.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-08-26-15-developer-workflow-changes-in-rust-v0-150-0|15 Developer Workflow changes in rust-v0.150.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-08-26-40544-include-transparent-background-in-image-generation-analytics-copyberry|♯40544 Include transparent background in image generation analytics @copyberry]] · Image Generation
- [[Changes/Codex CLI/2026-08-26-12-safety-and-privacy-changes-in-rust-v0-150-0|12 Safety and Privacy changes in rust-v0.150.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-08-26-2-account-and-access-changes-in-rust-v0-150-0|2 Account and Access changes in rust-v0.150.0]] · Account and Access
- [[Changes/Codex CLI/2026-08-26-39811-restrict-macos-preference-reads-to-full-disk-policies-copyberry|♯39811 Restrict macOS preference reads to full-disk policies @copyberry]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-08-26-40488-export-turn-cost-as-an-otel-metric-copyberry|♯40488 Export turn cost as an OTEL metric @copyberry]] · Pricing Model
- [[Changes/Codex CLI/2026-08-26-3-memory-and-personalization-changes-in-rust-v0-150-0|3 Memory and Personalization changes in rust-v0.150.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-08-26-40436-add-a-managed-gate-for-in-app-local-automation-copyberry|♯40436 Add a managed gate for in-app local automation @copyberry]] · Automation and Scheduling
- [[Changes/Codex CLI/2026-08-26-14-context-window-changes-in-rust-v0-150-0|14 Context Window changes in rust-v0.150.0]] · Context Window
- [[Changes/Codex CLI/2026-08-26-110-other-changes-in-rust-v0-150-0|110 other changes in rust-v0.150.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-08-25 · Gemini CLI · [[Changes/Gemini CLI/2026-08-25-8-agent-mode-changes-in-v0-57-0|8 Agent Mode changes in v0.57.0]]
- Later: 2026-08-27 · Claude Code · [[Changes/Claude Code/2026-08-27-3-agent-mode-changes-in-v2-1-248|3 Agent Mode changes in v2.1.248]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-08-26-800154&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-08-26-14-agent-mode-changes-in-rust-v0-150-0.md%0ACard%20ID%3A%20codex-cli-2026-08-26-800154%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.150.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->