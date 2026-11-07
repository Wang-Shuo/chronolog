---
card_id: cline-2026-09-17-bd3370
date: '2026-09-17'
description: 'Cline · 2026-09-17 · Context Window: Long tasks now compact when they
  actually need to rather than running out of room. The trigger compared a character-based…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2
    Context Window changes in 0.2.9]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1232
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: significant
kind: change
machine_hash: 152e078e0eb97f355a617ce870adb7bb8f62cd67678153f0c364ee09602629e7
product: cline
product_name: Cline
record:
  ai_generated: true
  card_id: cline-2026-09-17-bd3370
  comparison: ''
  confidence: low
  date: '2026-09-17'
  description: 'Cline — v4.1.19: Long tasks now compact when they actually need to
    rather than running out of room. The trigger compared a character-based estimate
    of the conversation (~3 characters per token) against the model''s context limit,
    so content that tokenizes far denser than that — disassembly, image dumps, minified
    sources — could fill the real context window while the estimate stayed under the
    threshold and compaction never fired; the turn was then squeezed down to a handful
    of output tokens. The trigger now also uses the token count the provider itself
    reports, and how much history is kept is scaled by how far off the estimate turned
    out to be. The summarizer''s output budget also doubled, so a model that reasons
    before answering can no longer spend the whole budget thinking and return no summary
    at all.'
  evidence:
  - quote: Long tasks now compact when they actually need to rather than running out
      of room. The trigger compared a character-based estimate of the conversation
      (~3 characters per token) against the model's context limit, so content that
      tokenizes far denser than that — disassembly, image dumps, minified sources
      — could fill the real context window while the estimate stayed under the threshold
      and compaction never fired; the turn was then squeezed down to a handful of
      output tokens. The trigger now also uses the token count the provider itself
      reports, and how much history is kept is scaled by how far off the estimate
      turned out to be. The summarizer's output budget also doubled, so a model that
      reasons before answering can no longer spend the whole budget thinking and return
      no summary at all.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.19
  extractor_version: fallback-v5
  impact: significant
  kind: change
  product: cline
  product_name: Cline
  slug: long-tasks-now-compact-when-they-actually-need-to-rather-than-running-out-of-roo
  source_release: cline-2026-09-17-v4-1-19-github-390521944-270e9514
  source_type: github_releases
  theme: context-window
  theme_matches:
  - matched_terms:
    - context window
    - context
    - tokens
    score: 220
    theme: context-window
  - matched_terms:
    - model
    score: 50
    theme: model-support
  theme_resolution: manual-semantic-rule-v2
  title: Long tasks now compact when they actually need to rather than running out
    of room
  type: change
related_changes:
- '[[Changes/Runway/2026-09-15-you-can-now-mention-agent-directly-in-comments-on-any-asset-page-collaborate-and|Agent
  in Asset Comments]]'
- '[[Changes/GitHub Copilot CLI/2026-09-16-3-context-window-changes-in-v1-0-85|3 Context
  Window changes in v1.0.85]]'
- '[[Changes/OpenHands/2026-09-16-test-cover-conversation-context-menu-by-aivong-openhands-in-https-github-com-ope|test:
  cover conversation context menu]]'
source_release: '[[Releases/Cline/cline-2026-09-17-v4-1-19-github-390521944-270e9514|cline-2026-09-17-v4-1-19-github-390521944-270e9514]]'
source_type: github_releases
theme: context-window
title: Long tasks now compact when they actually need to rather than running out of
  room
type: change
---

<!-- chronolog:begin region="header" -->
# Long tasks now compact when they actually need to rather than running out of room

**Cline** · 2026-09-17 · [[Themes/context-window|Context Window]] · [Official source](https://github.com/cline/cline/releases/tag/v4.1.19) · from [[Releases/Cline/cline-2026-09-17-v4-1-19-github-390521944-270e9514|v4.1.19]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Long tasks now compact when they actually need to rather than running out of room. The trigger compared a character-based estimate of the conversation (~3 characters per token) against the model's context limit, so content that tokenizes far denser than that — disassembly, image dumps, minified sources — could fill the real context window while the estimate stayed under the threshold and compaction never fired; the turn was then squeezed down to a handful of output tokens. The trigger now also uses the token count the provider itself reports, and how much history is kept is scaled by how far off the estimate turned out to be. The summarizer's output budget also doubled, so a model that reasons before answering can no longer spend the whole budget thinking and return no summary at all.
>
> Source: https://github.com/cline/cline/releases/tag/v4.1.19
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Cline/2026-09-17-on-windows-opening-a-repository-that-contains-a-file-named-rg-exe-git-exe-or-pow|On Windows, opening a repository that contains a file named rg.exe, git.exe…]] · Mobile and Desktop
- [[Changes/Cline/2026-09-17-13-model-support-changes-in-v4-1-19|13 Model Support changes in v4.1.19]] · Model Support
- [[Changes/Cline/2026-09-17-2-developer-workflow-changes-in-v4-1-19|2 Developer Workflow changes in v4.1.19]] · Developer Workflow
- [[Changes/Cline/2026-09-17-task-history-no-longer-goes-blank-when-a-task-spawns-many-subagents-subagent-row|Task history no longer goes blank when a task spawns many subagents]] · Agent Mode
- [[Changes/Cline/2026-09-17-cline-pass-now-defaults-to-a-model-from-your-subscription-rather-than-a-free-one|Cline Pass now defaults to a model from your subscription rather than a free one]] · Pricing Model
- [[Changes/Cline/2026-09-17-web-search-is-now-enabled-by-default-on-models-that-support-it-outside-yolo-mode|Web search is now enabled by default on models that support it, outside YOLO mode]] · Search and Browsing
- [[Changes/Cline/2026-09-17-cline-s-logo-and-icons-have-been-refreshed-throughout-the-extension-including-th|Cline's logo and icons have been refreshed throughout the extension, including…]] · Interface Experience
- [[Changes/Cline/2026-09-17-terminal-commands-that-succeed-without-printing-anything-git-add-a-on-a-clean-tr|Terminal commands that succeed without printing anything…]] · Apps and Integrations
- [[Changes/Cline/2026-09-17-5-other-changes-in-v4-1-19|5 other changes in v4.1.19]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Context Window

- Earlier: 2026-09-16 · OpenHands · [[Changes/OpenHands/2026-09-16-test-cover-conversation-context-menu-by-aivong-openhands-in-https-github-com-ope|test: cover conversation context menu]]
- Later: 2026-09-17 · Codex CLI · [[Changes/Codex CLI/2026-09-17-20-context-window-changes-in-rust-v0-155-0|20 Context Window changes in rust-v0.155.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-05-04 · Cursor · [[Changes/Cursor/2023-05-04-2-context-window-changes-in-0-2-9|2 Context Window changes in 0.2.9]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20cline-2026-09-17-bd3370&body=Card%3A%20Changes%2FCline%2F2026-09-17-long-tasks-now-compact-when-they-actually-need-to-rather-than-running-out-of-roo.md%0ACard%20ID%3A%20cline-2026-09-17-bd3370%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fcline%2Fcline%2Freleases%2Ftag%2Fv4.1.19%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->