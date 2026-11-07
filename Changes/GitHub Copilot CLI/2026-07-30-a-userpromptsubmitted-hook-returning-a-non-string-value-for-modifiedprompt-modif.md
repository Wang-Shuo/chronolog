---
card_id: github-copilot-cli-2026-07-30-020eef
date: '2026-07-30'
description: 'GitHub Copilot CLI · 2026-07-30 · Memory and Personalization: A `userPromptSubmitted`
  hook returning a non-string value for `modifiedPrompt`…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom
    instructions are rolling out in beta]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1106
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: memory
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: significant
kind: change
machine_hash: 4cd87a499fb74b776dd9859b1f45c3ffd7795668a5ee7545787e85f0c21ddcc1
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  ai_generated: true
  card_id: github-copilot-cli-2026-07-30-020eef
  comparison: ''
  confidence: low
  date: '2026-07-30'
  description: 'GitHub Copilot CLI — 1.0.76: A `userPromptSubmitted` hook returning
    a non-string value for `modifiedPrompt`, `modifiedTransformedPrompt`, or a handled
    `responseContent` no longer corrupts the session; the value is ignored, a type-only
    warning naming the field is logged, an empty-string replacement is rejected instead
    of blanking the model-facing content, a hook that sets `handled` without a usable
    `responseContent` is now diagnosed instead of silently falling through to the
    model, and a `null` `additionalContext` is treated as absent instead of being
    injected as the literal text `null`; hook output is also bounded at 10 MiB per
    invocation, so an HTTP or command hook returning an unbounded response can no
    longer exhaust memory or leave an oversized session behind'
  evidence:
  - quote: A `userPromptSubmitted` hook returning a non-string value for `modifiedPrompt`,
      `modifiedTransformedPrompt`, or a handled `responseContent` no longer corrupts
      the session; the value is ignored, a type-only warning naming the field is logged,
      an empty-string replacement is rejected instead of blanking the model-facing
      content, a hook that sets `handled` without a usable `responseContent` is now
      diagnosed instead of silently falling through to the model, and a `null` `additionalContext`
      is treated as absent instead of being injected as the literal text `null`; hook
      output is also bounded at 10 MiB per invocation, so an HTTP or command hook
      returning an unbounded response can no longer exhaust memory or leave an oversized
      session behind
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.76
  extractor_version: fallback-v5
  impact: significant
  kind: change
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: a-userpromptsubmitted-hook-returning-a-non-string-value-for-modifiedprompt-modif
  source_release: github-copilot-cli-2026-07-30-v1-0-76-github-362129864-0932fe29
  source_type: github_releases
  theme: memory
  theme_matches:
  - matched_terms:
    - memory
    score: 110
    theme: memory
  - matched_terms:
    - model
    score: 50
    theme: model-support
  title: A `userPromptSubmitted` hook returning a non-string value for `modifiedPrompt`…
  type: change
related_changes:
- '[[Changes/OpenHands/2026-07-29-feat-add-persistent-agent-memory-toggle-by-hieptl-in-https-github-com-openhands|feat:
  add persistent agent memory toggle]]'
- '[[Changes/Windsurf/2026-07-29-devin-local|Devin Local]]'
- '[[Changes/Windsurf/2026-07-29-devin-local-8ab9ef|Devin Local]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-07-30-v1-0-76-github-362129864-0932fe29|github-copilot-cli-2026-07-30-v1-0-76-github-362129864-0932fe29]]'
source_type: github_releases
theme: memory
title: A userPromptSubmitted hook returning a non-string value for modifiedPrompt…
type: change
---

<!-- chronolog:begin region="header" -->
# A `userPromptSubmitted` hook returning a non-string value for `modifiedPrompt`…

**GitHub Copilot CLI** · 2026-07-30 · [[Themes/memory|Memory and Personalization]] · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.76) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-07-30-v1-0-76-github-362129864-0932fe29|1.0.76]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> A `userPromptSubmitted` hook returning a non-string value for `modifiedPrompt`, `modifiedTransformedPrompt`, or a handled `responseContent` no longer corrupts the session; the value is ignored, a type-only warning naming the field is logged, an empty-string replacement is rejected instead of blanking the model-facing content, a hook that sets `handled` without a usable `responseContent` is now diagnosed instead of silently falling through to the model, and a `null` `additionalContext` is treated as absent instead of being injected as the literal text `null`; hook output is also bounded at 10 MiB per invocation, so an HTTP or command hook returning an unbounded response can no longer exhaust memory or leave an oversized session behind
>
> Source: https://github.com/github/copilot-cli/releases/tag/v1.0.76
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-07-30-5-safety-and-privacy-changes-in-v1-0-76|5 Safety and Privacy changes in v1.0.76]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-07-30-diff-scrolls-and-syntax-highlights-large-multi-file-diffs-faster|/diff scrolls and syntax-highlights large multi-file diffs faster]] · Reliability and Performance
- [[Changes/GitHub Copilot CLI/2026-07-30-2-developer-workflow-changes-in-v1-0-76|2 Developer Workflow changes in v1.0.76]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-07-30-2-apps-and-integrations-changes-in-v1-0-76|2 Apps and Integrations changes in v1.0.76]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-07-30-2-model-support-changes-in-v1-0-76|2 Model Support changes in v1.0.76]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-07-30-restore-the-early-warning-when-unreclaimable-system-and-tool-context-nears-the-l|Restore the early warning when unreclaimable system and tool context nears…]] · Context Window
- [[Changes/GitHub Copilot CLI/2026-07-30-voice-mode-pauses-playing-media-before-recording-and-resumes-it-afterward-where|Voice mode pauses playing media before recording and resumes it afterward, where…]] · Voice and Audio
- [[Changes/GitHub Copilot CLI/2026-07-30-2-agent-mode-changes-in-v1-0-76|2 Agent Mode changes in v1.0.76]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-07-30-2-editor-experience-changes-in-v1-0-76|2 Editor Experience changes in v1.0.76]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-07-30-4-interface-experience-changes-in-v1-0-76|4 Interface Experience changes in v1.0.76]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-07-30-10-other-changes-in-v1-0-76|10 other changes in v1.0.76]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Memory and Personalization

- Earlier: 2026-07-29 · Windsurf · [[Changes/Windsurf/2026-07-29-devin-local-8ab9ef|Devin Local]]
- Later: 2026-07-31 · Cline · [[Changes/Cline/2026-07-31-remove-vestigial-mcp-server-key-machinery-from-mcphub-native-mcp-tool-calls-now|Remove vestigial MCP server-key machinery from McpHub]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-20 · ChatGPT · [[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom instructions are rolling out in beta]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-07-30-020eef&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-07-30-a-userpromptsubmitted-hook-returning-a-non-string-value-for-modifiedprompt-modif.md%0ACard%20ID%3A%20github-copilot-cli-2026-07-30-020eef%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.76%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->