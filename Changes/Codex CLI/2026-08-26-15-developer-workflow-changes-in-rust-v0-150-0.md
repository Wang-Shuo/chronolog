---
card_id: codex-cli-2026-08-26-1aa477
date: '2026-08-26'
description: 'Codex CLI · 2026-08-26 · Developer Workflow: 15 changes in 0.150.0 —
  Reference other Codex tasks with `@` mentions, and ask agents to read, create, or
  message…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter
    Colors]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2906
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 037d393cdb25eaa66f54ad1cddf7eacf93482f9c5a44881573ac49273893c6f0
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-08-26-1aa477
  comparison: ''
  date: '2026-08-26'
  description: 'Codex CLI — 0.150.0: 15 Developer Workflow changes'
  evidence:
  - quote: 'Reference other Codex tasks with `@` mentions, and ask agents to read,
      create, or message tasks from the terminal. (#40308, #40315)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.150.0
  - quote: 'Unnamed terminal tasks receive descriptive titles automatically, and `/rename`
      suggests an editable title based on the conversation. (#40492, #40495)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.150.0
  - quote: Prevented Unix shutdown hangs caused by detached processes retaining a
      terminal or full terminal output buffers. (#40460)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.150.0
  - quote: '#39756 Cache shell snapshots in the exec server @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.150.0
  - quote: '#39757 Standardize shell execution on unified exec @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.150.0
  - quote: '#39772 Standardize shell execution on unified exec @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.150.0
  - quote: '#39809 Preserve WINDIR in core Windows shell environments @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.150.0
  - quote: '#39917 Honor request PATH in exec-server shell snapshots @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.150.0
  - quote: '#39958 Stop advertising shell snapshots from local exec servers @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.150.0
  - quote: '#40006 Synchronize Git enrichment tests explicitly @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.150.0
  - quote: '#40011 Synchronize concurrent Git enrichment test explicitly @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.150.0
  - quote: '#40376 Advertise shell snapshot v2 support on Unix @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.150.0
  - quote: '#40422 Harden Windows updater command execution @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.150.0
  - quote: '#40447 Retry failed shell snapshot captures @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.150.0
  - quote: '#40528 Represent terminal input in approval reviews @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.150.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 15-developer-workflow-changes-in-rust-v0-150-0
  source_release: codex-cli-2026-08-26-rust-v0-150-0-github-377374683-d950f84c
  source_type: github_releases
  theme: developer-workflow
  title: 15 Developer Workflow changes in rust-v0.150.0
  type: change
related_changes:
- '[[Changes/Open WebUI/2026-08-25-73-developer-workflow-changes-in-v0-11-1|73 Developer
  Workflow changes in v0.11.1]]'
- '[[Changes/OpenCode/2026-08-25-terminal-fixed-github-auth-for-immutable-oidc-subject-tokens|Terminal
  Fixed GitHub auth for immutable OIDC subject tokens]]'
- '[[Changes/Claude Code/2026-08-26-changed-terminal-hyperlinks-in-rendered-markdown-link-targets-that-point-at-a-ne|Changed
  terminal hyperlinks in rendered markdown]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-08-26-rust-v0-150-0-github-377374683-d950f84c|codex-cli-2026-08-26-rust-v0-150-0-github-377374683-d950f84c]]'
source_type: github_releases
theme: developer-workflow
title: 15 Developer Workflow changes in rust-v0.150.0
type: change
---

<!-- chronolog:begin region="header" -->
# 15 Developer Workflow changes in rust-v0.150.0

**Codex CLI** · 2026-08-26 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.150.0) · from [[Releases/Codex CLI/codex-cli-2026-08-26-rust-v0-150-0-github-377374683-d950f84c|0.150.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Reference other Codex tasks with `@` mentions, and ask agents to read, create, or message tasks from the terminal. (#40308, #40315)

> Unnamed terminal tasks receive descriptive titles automatically, and `/rename` suggests an editable title based on the conversation. (#40492, #40495)

> Prevented Unix shutdown hangs caused by detached processes retaining a terminal or full terminal output buffers. (#40460)

> #39756 Cache shell snapshots in the exec server @copyberry

> #39757 Standardize shell execution on unified exec @copyberry

> #39772 Standardize shell execution on unified exec @copyberry

> #39809 Preserve WINDIR in core Windows shell environments @copyberry

> #39917 Honor request PATH in exec-server shell snapshots @copyberry

> #39958 Stop advertising shell snapshots from local exec servers @copyberry

> #40006 Synchronize Git enrichment tests explicitly @copyberry

> #40011 Synchronize concurrent Git enrichment test explicitly @copyberry

> #40376 Advertise shell snapshot v2 support on Unix @copyberry

> #40422 Harden Windows updater command execution @copyberry

> #40447 Retry failed shell snapshot captures @copyberry

> #40528 Represent terminal input in approval reviews @copyberry

Source: https://github.com/openai/codex/releases/tag/rust-v0.150.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-08-26-39953-support-voice-aware-configuration-and-version-skew-builds-copyberry|♯39953 Support voice-aware configuration and version-skew builds @copyberry]] · Voice and Audio
- [[Changes/Codex CLI/2026-08-26-6-interface-experience-changes-in-rust-v0-150-0|6 Interface Experience changes in rust-v0.150.0]] · Interface Experience
- [[Changes/Codex CLI/2026-08-26-10-model-support-changes-in-rust-v0-150-0|10 Model Support changes in rust-v0.150.0]] · Model Support
- [[Changes/Codex CLI/2026-08-26-24-apps-and-integrations-changes-in-rust-v0-150-0|24 Apps and Integrations changes in rust-v0.150.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-08-26-40544-include-transparent-background-in-image-generation-analytics-copyberry|♯40544 Include transparent background in image generation analytics @copyberry]] · Image Generation
- [[Changes/Codex CLI/2026-08-26-14-agent-mode-changes-in-rust-v0-150-0|14 Agent Mode changes in rust-v0.150.0]] · Agent Mode
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
## Nearby in Developer Workflow

- Earlier: 2026-08-26 · Claude Code · [[Changes/Claude Code/2026-08-26-changed-terminal-hyperlinks-in-rendered-markdown-link-targets-that-point-at-a-ne|Changed terminal hyperlinks in rendered markdown]]
- Later: 2026-08-26 · Google Antigravity · [[Changes/Google Antigravity/2026-08-26-generative-ui-and-ui-improvements|Generative UI and UI improvements]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-09-11 · Descript · [[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter Colors]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-08-26-1aa477&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-08-26-15-developer-workflow-changes-in-rust-v0-150-0.md%0ACard%20ID%3A%20codex-cli-2026-08-26-1aa477%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.150.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->