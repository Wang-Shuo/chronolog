---
card_id: openclaw-2026-09-08-2692e9
date: '2026-09-08'
description: 'OpenClaw · 2026-09-08 · Context Window: 12 changes in v2026.9.3 — Context
  meters use the matching last-run prompt budget and fall back to context capacity
  when…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-09-18-double-click-to-select-a-range|Double-click
    to select a range]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2547
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 8a1bfbe4850498677fc7b87719a9983d9e455902dcdb05c86d67b149d75cf284
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-08-2692e9
  comparison: ''
  date: '2026-09-08'
  description: 'OpenClaw — v2026.9.3: 12 Context Window changes'
  evidence:
  - quote: Context meters use the matching last-run prompt budget and fall back to
      context capacity when that budget is stale after a model or cap change. Refresh
      reloads the selected session's timeline, conversation and prompt breakdown alongside
      totals, while exports stay tied to the concrete session instance being shown.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Enabled answer previews can show compaction status, and native choice controls
      no longer repeat their fallback list in the message text. Telegram conversations
      also keep visible delegated tasks attached to their parent conversation without
      relaxing spawn permissions.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Bots in mention-only mode need an active native or configured mention to
      reply. A handoff that relied only on Discord's reply ping needs an explicit
      mention. Policy-only changes apply to new messages and interactions without
      waiting for an active Control UI turn to finish, while transport changes and
      mixed edits remain deferred and work already admitted keeps its original context.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Question prompts explain typed replies when a channel has no buttons, and
      forwarded context remains separate from the sender's own commands so quoted
      instructions do not execute a second time. Loopback questions are delivered
      to their originating channel, and cancelled unsent questions do not replay later.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: LM Studio embeddings use the prepared model instance and its context capacity,
      and can reload an evicted embedding model when preloading is enabled. Existing
      cached vectors are retained rather than recomputed by these fixes.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Tool loops and changing background progress now preserve more of the stable
      conversation and tool content that supported providers can reuse. Responses
      history stays append-only, Claude CLI avoids repeatedly changing its startup
      context, and Codex resends workspace references when they need introduction
      or refresh.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Usage separates cached and fresh prompt tokens when Ollama reports the
      required counters, and request-level diagnostics help explain cache misses.
      Codex side questions now reach the usage hooks with their tool-loop counters
      intact.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: LM Studio now budgets against the context of the loaded model instance,
      and with preload enabled sends chat to an instance that has enough room. If
      a new instance is loaded, the request uses its returned identity while your
      configured model reference stays the same. This avoids budgeting for a larger
      instance and then sending the conversation to a smaller one.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Startup and shutdown also coordinate late listeners and service cleanup,
      and context-engine plugins receive completion for successful compaction that
      had nothing to remove. Failed, cancelled, and owner-lost compaction attempts
      remain separate from successful completion.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Saved CLI context is restored only within verified account and transcript
      boundaries. Unknown, imported, mixed, or legacy history is not automatically
      replayed or deleted. Blank or stringified-null Gateway tokens are refused; inline
      tokens can be repaired with Doctor's token-generation action, while external
      references need correction at their source and clients need the updated credential.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Private yield context and recognized runtime prefaces are kept out of public
      tool results and delivered replies, while Codex dynamic-tool text is redacted
      before budgeting and truncation. Streamed reasoning previews also handle the
      supported echoed-marker case without stripping ordinary reasoning or final answers.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: The updated runtime-context projection applies to genuinely new sessions;
      existing transcripts retain their earlier policy. These targeted changes do
      not establish a general prompt-injection or context-disclosure guarantee.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 12-context-window-changes-in-v2026-9-3
  source_release: openclaw-2026-09-08-v2026-9-3-dfcfef48
  source_type: openclaw_changelog
  theme: context-window
  title: 12 Context Window changes in v2026.9.3
  type: change
related_changes:
- '[[Changes/Claude Code/2026-09-04-added-skill-doctor-to-show-which-loaded-skills-go-unused-and-what-they-cost-in-c|Added
  /skill-doctor to show which loaded skills go unused and what they cost…]]'
- '[[Changes/Kimi Code/2026-09-04-remind-the-model-of-its-context-budget-before-automatic-compaction-and-after-com|Remind
  the model of its context budget before automatic compaction, and after…]]'
- '[[Changes/OpenClaw/2026-09-05-15-context-window-changes-in-v2026-9-2|15 Context
  Window changes in v2026.9.2]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-08-v2026-9-3-dfcfef48|openclaw-2026-09-08-v2026-9-3-dfcfef48]]'
source_type: openclaw_changelog
theme: context-window
title: 12 Context Window changes in v2026.9.3
type: change
---

<!-- chronolog:begin region="header" -->
# 12 Context Window changes in v2026.9.3

**OpenClaw** · 2026-09-08 · [[Themes/context-window|Context Window]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.3) · from [[Releases/OpenClaw/openclaw-2026-09-08-v2026-9-3-dfcfef48|v2026.9.3]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Context meters use the matching last-run prompt budget and fall back to context capacity when that budget is stale after a model or cap change. Refresh reloads the selected session's timeline, conversation and prompt breakdown alongside totals, while exports stay tied to the concrete session instance being shown.

> Enabled answer previews can show compaction status, and native choice controls no longer repeat their fallback list in the message text. Telegram conversations also keep visible delegated tasks attached to their parent conversation without relaxing spawn permissions.

> Bots in mention-only mode need an active native or configured mention to reply. A handoff that relied only on Discord's reply ping needs an explicit mention. Policy-only changes apply to new messages and interactions without waiting for an active Control UI turn to finish, while transport changes and mixed edits remain deferred and work already admitted keeps its original context.

> Question prompts explain typed replies when a channel has no buttons, and forwarded context remains separate from the sender's own commands so quoted instructions do not execute a second time. Loopback questions are delivered to their originating channel, and cancelled unsent questions do not replay later.

> LM Studio embeddings use the prepared model instance and its context capacity, and can reload an evicted embedding model when preloading is enabled. Existing cached vectors are retained rather than recomputed by these fixes.

> Tool loops and changing background progress now preserve more of the stable conversation and tool content that supported providers can reuse. Responses history stays append-only, Claude CLI avoids repeatedly changing its startup context, and Codex resends workspace references when they need introduction or refresh.

> Usage separates cached and fresh prompt tokens when Ollama reports the required counters, and request-level diagnostics help explain cache misses. Codex side questions now reach the usage hooks with their tool-loop counters intact.

> LM Studio now budgets against the context of the loaded model instance, and with preload enabled sends chat to an instance that has enough room. If a new instance is loaded, the request uses its returned identity while your configured model reference stays the same. This avoids budgeting for a larger instance and then sending the conversation to a smaller one.

> Startup and shutdown also coordinate late listeners and service cleanup, and context-engine plugins receive completion for successful compaction that had nothing to remove. Failed, cancelled, and owner-lost compaction attempts remain separate from successful completion.

> Saved CLI context is restored only within verified account and transcript boundaries. Unknown, imported, mixed, or legacy history is not automatically replayed or deleted. Blank or stringified-null Gateway tokens are refused; inline tokens can be repaired with Doctor's token-generation action, while external references need correction at their source and clients need the updated credential.

> Private yield context and recognized runtime prefaces are kept out of public tool results and delivered replies, while Codex dynamic-tool text is redacted before budgeting and truncation. Streamed reasoning previews also handle the supported echoed-marker case without stripping ordinary reasoning or final answers.

> The updated runtime-context projection applies to genuinely new sessions; existing transcripts retain their earlier policy. These targeted changes do not establish a general prompt-injection or context-disclosure guarantee.

Source: https://docs.openclaw.ai/releases/2026.9.3
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-09-08-7-automation-and-scheduling-changes-in-v2026-9-3|7 Automation and Scheduling changes in v2026.9.3]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-09-08-10-memory-and-personalization-changes-in-v2026-9-3|10 Memory and Personalization changes in v2026.9.3]] · Memory and Personalization
- [[Changes/OpenClaw/2026-09-08-2-files-and-data-changes-in-v2026-9-3|2 Files and Data changes in v2026.9.3]] · Files and Data
- [[Changes/OpenClaw/2026-09-08-23-apps-and-integrations-changes-in-v2026-9-3|23 Apps and Integrations changes in v2026.9.3]] · Apps and Integrations
- [[Changes/OpenClaw/2026-09-08-ordinary-model-changes-now-apply-to-the-current-chat-by-default-including-admini|Ordinary model changes now apply to the current chat by default, including…]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-09-08-10-mobile-and-desktop-changes-in-v2026-9-3|10 Mobile and Desktop changes in v2026.9.3]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-09-08-4-reliability-and-performance-changes-in-v2026-9-3|4 Reliability and Performance changes in v2026.9.3]] · Reliability and Performance
- [[Changes/OpenClaw/2026-09-08-provider-adapters-preserve-initial-anthropic-text-and-thinking-keep-images-with|Provider adapters preserve initial Anthropic text and thinking, keep images…]] · Multimodal Input
- [[Changes/OpenClaw/2026-09-08-8-editor-experience-changes-in-v2026-9-3|8 Editor Experience changes in v2026.9.3]] · Editor Experience
- [[Changes/OpenClaw/2026-09-08-8-voice-and-audio-changes-in-v2026-9-3|8 Voice and Audio changes in v2026.9.3]] · Voice and Audio
- [[Changes/OpenClaw/2026-09-08-15-model-support-changes-in-v2026-9-3|15 Model Support changes in v2026.9.3]] · Model Support
- [[Changes/OpenClaw/2026-09-08-3-search-and-browsing-changes-in-v2026-9-3|3 Search and Browsing changes in v2026.9.3]] · Search and Browsing
- [[Changes/OpenClaw/2026-09-08-16-agent-mode-changes-in-v2026-9-3|16 Agent Mode changes in v2026.9.3]] · Agent Mode
- [[Changes/OpenClaw/2026-09-08-11-interface-experience-changes-in-v2026-9-3|11 Interface Experience changes in v2026.9.3]] · Interface Experience
- [[Changes/OpenClaw/2026-09-08-slack-delivers-valid-structured-sections-intact-even-when-their-accessibility-te|Slack delivers valid structured sections intact even when their accessibility text…]] · Accessibility and Localization
- [[Changes/OpenClaw/2026-09-08-4-collaboration-changes-in-v2026-9-3|4 Collaboration changes in v2026.9.3]] · Collaboration
- [[Changes/OpenClaw/2026-09-08-14-safety-and-privacy-changes-in-v2026-9-3|14 Safety and Privacy changes in v2026.9.3]] · Safety and Privacy
- [[Changes/OpenClaw/2026-09-08-4-pricing-model-changes-in-v2026-9-3|4 Pricing Model changes in v2026.9.3]] · Pricing Model
- [[Changes/OpenClaw/2026-09-08-8-account-and-access-changes-in-v2026-9-3|8 Account and Access changes in v2026.9.3]] · Account and Access
- [[Changes/OpenClaw/2026-09-08-22-developer-workflow-changes-in-v2026-9-3|22 Developer Workflow changes in v2026.9.3]] · Developer Workflow
- [[Changes/OpenClaw/2026-09-08-77-other-changes-in-v2026-9-3|77 other changes in v2026.9.3]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Context Window

- Earlier: 2026-09-05 · OpenClaw · [[Changes/OpenClaw/2026-09-05-15-context-window-changes-in-v2026-9-2|15 Context Window changes in v2026.9.2]]
- Later: 2026-09-09 · Claude Code · [[Changes/Claude Code/2026-09-09-improved-prompt-cache-stability-subagents-and-sessions-started-with-system-promp|Improved prompt-cache stability]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-09-18 · Descript · [[Changes/Descript/2019-09-18-double-click-to-select-a-range|Double-click to select a range]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-08-2692e9&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-08-12-context-window-changes-in-v2026-9-3.md%0ACard%20ID%3A%20openclaw-2026-09-08-2692e9%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.3%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->