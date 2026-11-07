---
card_id: opencode-2026-03-12-0b6505
date: '2026-03-12'
description: 'OpenCode · 2026-03-12 · Developer Workflow: 11 changes in v1.2.25 —
  Core Replace Bun shell with direct spawn calls in core flows'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter
    Colors]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2739
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: f918486bf8dfbd09f2a5c85365db21a17de2a35848565d659be1c32f449d8c50
product: opencode
product_name: OpenCode
record:
  card_id: opencode-2026-03-12-0b6505
  comparison: ''
  date: '2026-03-12'
  description: 'OpenCode — v1.2.25: 11 Developer Workflow changes'
  evidence:
  - quote: Core Replace Bun shell with direct spawn calls in core flows
    source_release: https://opencode.ai/changelog/v1.2.25
  - quote: Terminal Use parse() at boundaries instead of manual make() for imports
    source_release: https://opencode.ai/changelog/v1.2.25
  - quote: Terminal Wait for model store before auto-submitting --prompt in TUI
    source_release: https://opencode.ai/changelog/v1.2.25
  - quote: Terminal Handle error when creating a session in TUI
    source_release: https://opencode.ai/changelog/v1.2.25
  - quote: Desktop Fixed terminal animation in application
    source_release: https://opencode.ai/changelog/v1.2.25
  - quote: Desktop Fix terminal e2e test flakiness by implementing a real terminal
      driver
    source_release: https://opencode.ai/changelog/v1.2.25
  - quote: Desktop Set default WebSocket username and fix terminal spawn lifecycle
      issues in desktop app
    source_release: https://opencode.ai/changelog/v1.2.25
  - quote: Desktop Re-focus prompt after terminal opens in slash-terminal test
    source_release: https://opencode.ai/changelog/v1.2.25
  - quote: Desktop Fixed terminal jank in the app
    source_release: https://opencode.ai/changelog/v1.2.25
  - quote: Desktop Fixed terminal focus issues and reduced jank in the app
    source_release: https://opencode.ai/changelog/v1.2.25
  - quote: Desktop Terminal state corruption fixed
    source_release: https://opencode.ai/changelog/v1.2.25
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: opencode
  product_name: OpenCode
  slug: 11-developer-workflow-changes-in-v1-2-25
  source_release: opencode-2026-03-12-v1-2-25-4fca2d35
  source_type: opencode_changelog
  theme: developer-workflow
  title: 11 Developer Workflow changes in v1.2.25
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-03-11-4-developer-workflow-changes-in-v1-0-4|4
  Developer Workflow changes in v1.0.4]]'
- '[[Changes/OpenHands/2026-03-11-2-developer-workflow-changes-in-1-5-0|2 Developer
  Workflow changes in 1.5.0]]'
- '[[Changes/Claude Code/2026-03-12-vscode-improved-scroll-wheel-responsiveness-in-the-integrated-terminal-with-term|VSCode
  Improved scroll wheel responsiveness in the integrated terminal…]]'
source_release: '[[Releases/OpenCode/opencode-2026-03-12-v1-2-25-4fca2d35|opencode-2026-03-12-v1-2-25-4fca2d35]]'
source_type: opencode_changelog
theme: developer-workflow
title: 11 Developer Workflow changes in v1.2.25
type: change
---

<!-- chronolog:begin region="header" -->
# 11 Developer Workflow changes in v1.2.25

**OpenCode** · 2026-03-12 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://opencode.ai/changelog/v1.2.25) · from [[Releases/OpenCode/opencode-2026-03-12-v1-2-25-4fca2d35|v1.2.25]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Core Replace Bun shell with direct spawn calls in core flows

> Terminal Use parse() at boundaries instead of manual make() for imports

> Terminal Wait for model store before auto-submitting --prompt in TUI

> Terminal Handle error when creating a session in TUI

> Desktop Fixed terminal animation in application

> Desktop Fix terminal e2e test flakiness by implementing a real terminal driver

> Desktop Set default WebSocket username and fix terminal spawn lifecycle issues in desktop app

> Desktop Re-focus prompt after terminal opens in slash-terminal test

> Desktop Fixed terminal jank in the app

> Desktop Fixed terminal focus issues and reduced jank in the app

> Desktop Terminal state corruption fixed

Source: https://opencode.ai/changelog/v1.2.25
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenCode/2026-03-12-desktop-trim-session-render-work-in-app-for-improved-performance|Desktop Trim session render work in app for improved performance]] · Reliability and Performance
- [[Changes/OpenCode/2026-03-12-2-account-and-access-changes-in-v1-2-25|2 Account and Access changes in v1.2.25]] · Account and Access
- [[Changes/OpenCode/2026-03-12-2-apps-and-integrations-changes-in-v1-2-25|2 Apps and Integrations changes in v1.2.25]] · Apps and Integrations
- [[Changes/OpenCode/2026-03-12-desktop-skip-editor-reconcile-during-ime-composition|Desktop Skip editor reconcile during IME composition]] · Editor Experience
- [[Changes/OpenCode/2026-03-12-support-non-openai-azure-models-that-use-completions-endpoints|Support non-OpenAI Azure models that use completions endpoints]] · Model Support
- [[Changes/OpenCode/2026-03-12-2-safety-and-privacy-changes-in-v1-2-25|2 Safety and Privacy changes in v1.2.25]] · Safety and Privacy
- [[Changes/OpenCode/2026-03-12-2-interface-experience-changes-in-v1-2-25|2 Interface Experience changes in v1.2.25]] · Interface Experience
- [[Changes/OpenCode/2026-03-12-core-fixed-chunk-timeout-when-processing-llm-stream|Core Fixed chunk timeout when processing LLM stream]] · Model Support
- [[Changes/OpenCode/2026-03-12-core-adjust-skill-presentation-to-reduce-token-usage|Core Adjust skill presentation to reduce token usage]] · Presentation Creation
- [[Changes/OpenCode/2026-03-12-core-multiple-jdtls-lsps-eating-memory-in-java-monorepos|Core Multiple jdtls LSPs eating memory in Java monorepos]] · Memory and Personalization
- [[Changes/OpenCode/2026-03-12-10-mobile-and-desktop-changes-in-v1-2-25|10 Mobile and Desktop changes in v1.2.25]] · Mobile and Desktop
- [[Changes/OpenCode/2026-03-12-core-improve-skill-presentation-to-agent-to-increase-likelihood-of-skill-invocat|Core Improve skill presentation to agent to increase likelihood of skill invocations]] · Agent Mode
- [[Changes/OpenCode/2026-03-12-22-other-changes-in-v1-2-25|22 other changes in v1.2.25]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-03-12 · Claude Code · [[Changes/Claude Code/2026-03-12-vscode-improved-scroll-wheel-responsiveness-in-the-integrated-terminal-with-term|VSCode Improved scroll wheel responsiveness in the integrated terminal…]]
- Later: 2026-03-13 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-03-13-3-developer-workflow-changes-in-v1-0-5|3 Developer Workflow changes in v1.0.5]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-09-11 · Descript · [[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter Colors]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20opencode-2026-03-12-0b6505&body=Card%3A%20Changes%2FOpenCode%2F2026-03-12-11-developer-workflow-changes-in-v1-2-25.md%0ACard%20ID%3A%20opencode-2026-03-12-0b6505%0ASource%3A%20https%3A%2F%2Fopencode.ai%2Fchangelog%2Fv1.2.25%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->