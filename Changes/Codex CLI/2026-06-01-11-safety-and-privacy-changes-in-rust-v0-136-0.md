---
card_id: codex-cli-2026-06-01-5a5981
date: '2026-06-01'
description: 'Codex CLI · 2026-06-01 · Safety and Privacy: 11 changes in 0.136.0 —
  Windows admins get an alpha `codex sandbox setup --elevated` provisioning path,
  plus…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1142
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: ece8aa47223ec147a4dc370d03f15bfff0ef7828d2f05cd88b54ae3c039628a8
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-06-01-5a5981
  comparison: ''
  date: '2026-06-01'
  description: 'Codex CLI — 0.136.0: 11 Safety and Privacy changes'
  evidence:
  - quote: 'Windows admins get an alpha `codex sandbox setup --elevated` provisioning
      path, plus requirements support for allowed Windows sandbox implementations.
      (#24831, #23766)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: 'Command-safety hardening prevents `/diff` from running repository-provided
      Git helpers/hooks, avoids PowerShell parser execution on non-Windows hosts,
      and rejects browser-origin exec-server websocket handshakes. (#24954, #24946,
      #24947)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#22729 fix(linux-sandbox): preserve shell cleanup on interruption @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#19880 fix: cancel Windows sandbox on network denial @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#23924 Surface filesystem permission profiles in prompt context @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#24108 windows-sandbox: pass workspace roots to runner @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#24974 windows-sandbox: fix capture cancellation test roots @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#24946 [codex] Avoid PowerShell safety parsing off Windows @adrian-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#24831 Add Windows sandbox provisioning setup command @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#23165 thread-store: store permission profiles @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  - quote: '#23766 Constrain Windows sandbox requirements @abhinav-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.136.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 11-safety-and-privacy-changes-in-rust-v0-136-0
  source_release: codex-cli-2026-06-01-rust-v0-136-0-github-332669350-976b06b6
  source_type: github_releases
  theme: safety-privacy
  title: 11 Safety and Privacy changes in rust-v0.136.0
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-05-28-7-safety-and-privacy-changes-in-rust-v0-135-0|7
  Safety and Privacy changes in rust-v0.135.0]]'
- '[[Changes/OpenCode/2026-05-28-core-handled-acp-next-permission-prompts-correctly|Core
  Handled acp-next permission prompts correctly]]'
- '[[Changes/Claude Code/2026-05-29-2-safety-and-privacy-changes-in-v2-1-157|2 Safety
  and Privacy changes in v2.1.157]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-06-01-rust-v0-136-0-github-332669350-976b06b6|codex-cli-2026-06-01-rust-v0-136-0-github-332669350-976b06b6]]'
source_type: github_releases
theme: safety-privacy
title: 11 Safety and Privacy changes in rust-v0.136.0
type: change
---

<!-- chronolog:begin region="header" -->
# 11 Safety and Privacy changes in rust-v0.136.0

**Codex CLI** · 2026-06-01 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.136.0) · from [[Releases/Codex CLI/codex-cli-2026-06-01-rust-v0-136-0-github-332669350-976b06b6|0.136.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Windows admins get an alpha `codex sandbox setup --elevated` provisioning path, plus requirements support for allowed Windows sandbox implementations. (#24831, #23766)

> Command-safety hardening prevents `/diff` from running repository-provided Git helpers/hooks, avoids PowerShell parser execution on non-Windows hosts, and rejects browser-origin exec-server websocket handshakes. (#24954, #24946, #24947)

> #22729 fix(linux-sandbox): preserve shell cleanup on interruption @viyatb-oai

> #19880 fix: cancel Windows sandbox on network denial @viyatb-oai

> #23924 Surface filesystem permission profiles in prompt context @bolinfest

> #24108 windows-sandbox: pass workspace roots to runner @bolinfest

> #24974 windows-sandbox: fix capture cancellation test roots @bolinfest

> #24946 [codex] Avoid PowerShell safety parsing off Windows @adrian-openai

> #24831 Add Windows sandbox provisioning setup command @iceweasel-oai

> #23165 thread-store: store permission profiles @bolinfest

> #23766 Constrain Windows sandbox requirements @abhinav-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.136.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-06-01-25110-move-config-document-helpers-into-their-own-module-jif-oai|♯25110 Move config document helpers into their own module @jif-oai]] · Files and Data
- [[Changes/Codex CLI/2026-06-01-11-developer-workflow-changes-in-rust-v0-136-0|11 Developer Workflow changes in rust-v0.136.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-06-01-20-apps-and-integrations-changes-in-rust-v0-136-0|20 Apps and Integrations changes in rust-v0.136.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-06-01-2-memory-and-personalization-changes-in-rust-v0-136-0|2 Memory and Personalization changes in rust-v0.136.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-06-01-5-model-support-changes-in-rust-v0-136-0|5 Model Support changes in rust-v0.136.0]] · Model Support
- [[Changes/Codex CLI/2026-06-01-3-agent-mode-changes-in-rust-v0-136-0|3 Agent Mode changes in rust-v0.136.0]] · Agent Mode
- [[Changes/Codex CLI/2026-06-01-2-editor-experience-changes-in-rust-v0-136-0|2 Editor Experience changes in rust-v0.136.0]] · Editor Experience
- [[Changes/Codex CLI/2026-06-01-9-context-window-changes-in-rust-v0-136-0|9 Context Window changes in rust-v0.136.0]] · Context Window
- [[Changes/Codex CLI/2026-06-01-3-search-and-browsing-changes-in-rust-v0-136-0|3 Search and Browsing changes in rust-v0.136.0]] · Search and Browsing
- [[Changes/Codex CLI/2026-06-01-2-interface-experience-changes-in-rust-v0-136-0|2 Interface Experience changes in rust-v0.136.0]] · Interface Experience
- [[Changes/Codex CLI/2026-06-01-3-image-generation-changes-in-rust-v0-136-0|3 Image Generation changes in rust-v0.136.0]] · Image Generation
- [[Changes/Codex CLI/2026-06-01-57-other-changes-in-rust-v0-136-0|57 other changes in rust-v0.136.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-05-29 · Claude Code · [[Changes/Claude Code/2026-05-29-2-safety-and-privacy-changes-in-v2-1-157|2 Safety and Privacy changes in v2.1.157]]
- Later: 2026-06-01 · Lovable · [[Changes/Lovable/2026-06-01-automatic-fixes-for-basic-scan-findings|Automatic fixes for Basic scan findings]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-06-01-5a5981&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-06-01-11-safety-and-privacy-changes-in-rust-v0-136-0.md%0ACard%20ID%3A%20codex-cli-2026-06-01-5a5981%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.136.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->