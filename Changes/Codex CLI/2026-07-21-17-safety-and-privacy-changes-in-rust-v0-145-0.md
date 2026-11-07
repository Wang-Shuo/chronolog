---
card_id: codex-cli-2026-07-21-59a62d
date: '2026-07-21'
description: 'Codex CLI · 2026-07-21 · Safety and Privacy: 17 changes in 0.145.0 —
  Editing an earlier prompt or retrying a safety-buffered turn now creates a contextual…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke
    Application Access]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2184
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: c2ba4e2762c854e3a13de25e14029c69895d6520e17c499d7769405b8730f89d
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-07-21-59a62d
  comparison: ''
  date: '2026-07-21'
  description: 'Codex CLI — 0.145.0: 17 Safety and Privacy changes'
  evidence:
  - quote: 'Editing an earlier prompt or retrying a safety-buffered turn now creates
      a contextual branch, preserving the original conversation, attachments, and
      mention bindings. (#33201, #33207, #33211)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: 'Improved Windows execution and sandbox reliability, including native exec-server
      sandboxing, network-proxy enforcement, hidden helper consoles, and correctly
      quoted hook commands. (#32849, #32857, #33926, #34423)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: 'Strengthened safety and approval handling with better forced-`rm` detection,
      consistent full-access confirmation, and preserved rejection reasons across
      tools. (#32989, #33464, #34400)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#31813 tui: update safety buffering copy @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#31937 exec-server: expose process helper to outer sandbox @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#32232 Let permission hooks resolve strict auto-review requests @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#32286 Clarify waiting behavior in safety buffering prompts @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#32441 Preserve parent sandbox enforcement for memory consolidation @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#32857 Require the elevated Windows sandbox for network proxies @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#32864 Coalesce concurrent Windows sandbox setup requests @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33147 Support model catalog permission messages @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33200 Separate exec permission paths from core models @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33207 Retry safety-buffered turns on a forked thread @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33430 Avoid creating metadata paths in the Windows sandbox @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33445 Select the elevated Windows sandbox for network proxies @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#33944 Track permission instructions in world state @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  - quote: '#34436 Honor managed permission profiles in network proxy resolution @copyberry'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.145.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 17-safety-and-privacy-changes-in-rust-v0-145-0
  source_release: codex-cli-2026-07-21-rust-v0-145-0-github-357545274-7be4454f
  source_type: github_releases
  theme: safety-privacy
  title: 17 Safety and Privacy changes in rust-v0.145.0
  type: change
related_changes:
- '[[Changes/Kimi Code/2026-07-20-correct-the-yolo-and-auto-permission-mode-descriptions-yolo-auto-approves-tool-a|Correct
  the YOLO and Auto permission mode descriptions]]'
- '[[Changes/Kimi Code/2026-07-20-fix-running-subagents-not-observing-permission-mode-switches-made-after-they-sta|Fix
  running subagents not observing permission mode switches made after they started]]'
- '[[Changes/Claude Code/2026-07-21-fixed-remote-control-sessions-not-showing-a-pending-permission-prompt-or-dialog|Fixed
  Remote Control sessions not showing a pending permission prompt or dialog…]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-07-21-rust-v0-145-0-github-357545274-7be4454f|codex-cli-2026-07-21-rust-v0-145-0-github-357545274-7be4454f]]'
source_type: github_releases
theme: safety-privacy
title: 17 Safety and Privacy changes in rust-v0.145.0
type: change
---

<!-- chronolog:begin region="header" -->
# 17 Safety and Privacy changes in rust-v0.145.0

**Codex CLI** · 2026-07-21 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.145.0) · from [[Releases/Codex CLI/codex-cli-2026-07-21-rust-v0-145-0-github-357545274-7be4454f|0.145.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Editing an earlier prompt or retrying a safety-buffered turn now creates a contextual branch, preserving the original conversation, attachments, and mention bindings. (#33201, #33207, #33211)

> Improved Windows execution and sandbox reliability, including native exec-server sandboxing, network-proxy enforcement, hidden helper consoles, and correctly quoted hook commands. (#32849, #32857, #33926, #34423)

> Strengthened safety and approval handling with better forced-`rm` detection, consistent full-access confirmation, and preserved rejection reasons across tools. (#32989, #33464, #34400)

> #31813 tui: update safety buffering copy @etraut-openai

> #31937 exec-server: expose process helper to outer sandbox @pakrym-oai

> #32232 Let permission hooks resolve strict auto-review requests @copyberry

> #32286 Clarify waiting behavior in safety buffering prompts @copyberry

> #32441 Preserve parent sandbox enforcement for memory consolidation @copyberry

> #32857 Require the elevated Windows sandbox for network proxies @copyberry

> #32864 Coalesce concurrent Windows sandbox setup requests @copyberry

> #33147 Support model catalog permission messages @copyberry

> #33200 Separate exec permission paths from core models @copyberry

> #33207 Retry safety-buffered turns on a forked thread @copyberry

> #33430 Avoid creating metadata paths in the Windows sandbox @copyberry

> #33445 Select the elevated Windows sandbox for network proxies @copyberry

> #33944 Track permission instructions in world state @copyberry

> #34436 Honor managed permission profiles in network proxy resolution @copyberry

Source: https://github.com/openai/codex/releases/tag/rust-v0.145.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-07-21-4-collaboration-changes-in-rust-v0-145-0|4 Collaboration changes in rust-v0.145.0]] · Collaboration
- [[Changes/Codex CLI/2026-07-21-20-agent-mode-changes-in-rust-v0-145-0|20 Agent Mode changes in rust-v0.145.0]] · Agent Mode
- [[Changes/Codex CLI/2026-07-21-12-developer-workflow-changes-in-rust-v0-145-0|12 Developer Workflow changes in rust-v0.145.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-07-21-7-voice-and-audio-changes-in-rust-v0-145-0|7 Voice and Audio changes in rust-v0.145.0]] · Voice and Audio
- [[Changes/Codex CLI/2026-07-21-12-context-window-changes-in-rust-v0-145-0|12 Context Window changes in rust-v0.145.0]] · Context Window
- [[Changes/Codex CLI/2026-07-21-4-editor-experience-changes-in-rust-v0-145-0|4 Editor Experience changes in rust-v0.145.0]] · Editor Experience
- [[Changes/Codex CLI/2026-07-21-3-mobile-and-desktop-changes-in-rust-v0-145-0|3 Mobile and Desktop changes in rust-v0.145.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-07-21-3-image-generation-changes-in-rust-v0-145-0|3 Image Generation changes in rust-v0.145.0]] · Image Generation
- [[Changes/Codex CLI/2026-07-21-22-model-support-changes-in-rust-v0-145-0|22 Model Support changes in rust-v0.145.0]] · Model Support
- [[Changes/Codex CLI/2026-07-21-33201-branch-conversations-when-editing-earlier-tui-prompts-copyberry|♯33201 Branch conversations when editing earlier TUI prompts @copyberry]] · Projects and Workspaces
- [[Changes/Codex CLI/2026-07-21-3-reliability-and-performance-changes-in-rust-v0-145-0|3 Reliability and Performance changes in rust-v0.145.0]] · Reliability and Performance
- [[Changes/Codex CLI/2026-07-21-33167-document-the-windows-exec-yield-time-range-copyberry|♯33167 Document the Windows exec yield time range @copyberry]] · Files and Data
- [[Changes/Codex CLI/2026-07-21-11-memory-and-personalization-changes-in-rust-v0-145-0|11 Memory and Personalization changes in rust-v0.145.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-07-21-3-search-and-browsing-changes-in-rust-v0-145-0|3 Search and Browsing changes in rust-v0.145.0]] · Search and Browsing
- [[Changes/Codex CLI/2026-07-21-9-account-and-access-changes-in-rust-v0-145-0|9 Account and Access changes in rust-v0.145.0]] · Account and Access
- [[Changes/Codex CLI/2026-07-21-44-apps-and-integrations-changes-in-rust-v0-145-0|44 Apps and Integrations changes in rust-v0.145.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-07-21-18-interface-experience-changes-in-rust-v0-145-0|18 Interface Experience changes in rust-v0.145.0]] · Interface Experience
- [[Changes/Codex CLI/2026-07-21-161-other-changes-in-rust-v0-145-0|161 other changes in rust-v0.145.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-07-21 · Claude Code · [[Changes/Claude Code/2026-07-21-fixed-remote-control-sessions-not-showing-a-pending-permission-prompt-or-dialog|Fixed Remote Control sessions not showing a pending permission prompt or dialog…]]
- Later: 2026-07-21 · v0 · [[Changes/v0/2026-07-21-typed-prompts-survive-clarifying-questions-permission-approvals-and-queued-submi|Typed prompts survive clarifying questions, permission approvals, and queued…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Descript · [[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke Application Access]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-07-21-59a62d&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-07-21-17-safety-and-privacy-changes-in-rust-v0-145-0.md%0ACard%20ID%3A%20codex-cli-2026-07-21-59a62d%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.145.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->