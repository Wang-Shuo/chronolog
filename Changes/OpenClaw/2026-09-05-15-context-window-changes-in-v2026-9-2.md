---
card_id: openclaw-2026-09-05-9fe54b
date: '2026-09-05'
description: 'OpenClaw · 2026-09-05 · Context Window: 15 changes in v2026.9.2 — Side
  chat has a visible keyboard shortcut, Command-Shift-S on Apple platforms and…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-09-18-double-click-to-select-a-range|Double-click
    to select a range]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2544
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 0f4145b0dfbeb073473f0a341ef0c85043202e949a4921f4881bb4410775bb97
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-05-9fe54b
  comparison: ''
  date: '2026-09-05'
  description: 'OpenClaw — v2026.9.2: 15 Context Window changes'
  evidence:
  - quote: Side chat has a visible keyboard shortcut, Command-Shift-S on Apple platforms
      and Ctrl-Shift-S elsewhere, so you can open or close the existing panel without
      reaching for its tab. Cancelling while conversation context is still loading
      now retires that request before it can later start a model call or replace a
      newer answer. The same preparation work is covered by the existing 60-second
      timeout.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Long Discord replies keep their code, Unicode characters, and surrounding
      quote or list context when they need several messages, and attachment captions
      avoid extra empty code blocks. Sends and edits also preserve intentional indentation
      and trailing newlines, while an explicitly empty edit can clear an attachment
      caption without removing the attachment. Extremely small configured message
      limits can still constrain formatting, and the existing access checks continue
      to apply.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Telegram progress mode also keeps Claude CLI commentary in one temporary
      message, shows when context compaction completes or remains incomplete, and
      gives the final answer priority over pending commentary. Commentary remains
      temporary even with verbose mode enabled. For installations that depend on a
      proxy, explicitly configured trusted SOCKS5 routes now carry Bot API requests
      and incoming attachments through the intended transport, including supported
      cases where the media destination cannot be resolved locally; the proxy itself
      must still be locally resolvable and reachable.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Astra's full context window is 1,050,000 tokens, with up to 128,000 output
      tokens, while OpenClaw keeps its default active input budget at 272,000. Choosing
      Off does not disable Astra's reasoning, and the cost estimate preserves its
      higher long-context pricing tier.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: OpenClaw now supports Meta's Muse Spark 1.3 , with Standard and Contributor
      choices for accounts that have access. Both accept text and image input and
      expose reasoning controls, a 1,048,576-token context window, and up to 131,072
      output tokens. Select meta/muse-spark-1.3 for Standard or meta/muse-spark-1.3-contributor
      for Contributor.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: If compaction is interrupted after OpenClaw saves a new session, supported
      continuation paths can recover its recorded predecessor and keep the existing
      native thread. That includes ordinary messages, side questions, and same-thread
      resume, with outdated queued compaction and control commands prevented from
      changing the successor session. A confirmed deletion of an ordinary managed
      Codex thread instead creates a fresh native thread in the same OpenClaw session;
      it cannot restore the deleted native history.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Continuing a long Codex conversation now uses a bounded history renderer
      that keeps the needed context without first building a much larger temporary
      string. Resuming large saved records also spends less CPU scanning them, and
      prompt annotation or confirmed steering avoids rebuilding search information
      when the searchable content has not changed. These changes reduce specific preparation
      costs; large-record decoding and parsing can still take time.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Session pruning keeps trimmed tool results trimmed across later requests
      while preserving the full local history. Direct Anthropic API-key requests in
      cache-TTL mode use server-side clearing based on token thresholds, rather than
      the client TTL and hard-clear settings, and protection rules now include historical
      tools that are no longer available. After restarting a branched conversation,
      client-side restoration can still pick a sibling branch's pruning marker and
      change the context sent to the model.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: OpenAI Responses retains the instruction to finish an answer after compaction
      through reasoning-only and empty-response retries. If request preparation fails,
      a later successful request can establish fresh continuation state so subsequent
      turns stop resending the entire history; that first recovery request still sends
      the full conversation.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Codex turn usage now adds the reported counts from every unique completed
      response, including responses before a retry or cancellation. Those totals remain
      separate from the current context window, so a missing final context snapshot
      stays unavailable instead of showing the cumulative usage as if it were the
      remaining conversation context.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: When Desktop disconnects, the browser console keeps the original failure
      without adding a misleading error from closing an already closed viewer. Desktop
      stream logs also retain the first known local shutdown trigger separately from
      the observed connection close code, giving you more useful context when comparing
      the Gateway and device logs. The intermittent disconnect remains unexplained,
      and code 1006 on its own does not tell you whether a network, proxy, or local
      shutdown caused it.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Questions about a busy day now load only the latest 200 eligible observations
      already used for the answer context, keeping their chronological order without
      first loading the whole day's observations.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Local utilities used to inspect busy ports, identify processes, and clear
      a port now receive a limited operating-system environment instead of inheriting
      unrelated provider credentials, application tokens, proxy settings, and runtime
      overrides. This is scoped to those diagnostic helpers. Redacted logs and sanitized
      tool results also keep valid JSON fields that could previously disappear, including
      literal __proto__ fields, while still hiding nested secrets.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Stopping or timing out compaction now prevents further preparation once
      cancellation is observed, including after a session handoff, and native CLI
      cancellation is reported as compaction aborted . An operation already in progress
      may still need to settle before cleanup completes.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: When a run fails without enough information to classify the cause, the
      message now says the agent run failed and keeps the available model context
      instead of blaming the provider. Recognized provider errors retain their specific
      guidance, so the wording reflects what OpenClaw actually knows without claiming
      to diagnose or repair an unknown failure.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 15-context-window-changes-in-v2026-9-2
  source_release: openclaw-2026-09-05-v2026-9-2-377f6d77
  source_type: openclaw_changelog
  theme: context-window
  title: 15 Context Window changes in v2026.9.2
  type: change
related_changes:
- '[[Changes/Claude Code/2026-09-04-changed-context-token-counting-to-use-a-local-estimate-when-the-token-counting-a|Changed
  /context token counting to use a local estimate when the token-counting…]]'
- '[[Changes/Claude Code/2026-09-04-added-skill-doctor-to-show-which-loaded-skills-go-unused-and-what-they-cost-in-c|Added
  /skill-doctor to show which loaded skills go unused and what they cost…]]'
- '[[Changes/Kimi Code/2026-09-04-remind-the-model-of-its-context-budget-before-automatic-compaction-and-after-com|Remind
  the model of its context budget before automatic compaction, and after…]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-05-v2026-9-2-377f6d77|openclaw-2026-09-05-v2026-9-2-377f6d77]]'
source_type: openclaw_changelog
theme: context-window
title: 15 Context Window changes in v2026.9.2
type: change
---

<!-- chronolog:begin region="header" -->
# 15 Context Window changes in v2026.9.2

**OpenClaw** · 2026-09-05 · [[Themes/context-window|Context Window]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.2) · from [[Releases/OpenClaw/openclaw-2026-09-05-v2026-9-2-377f6d77|v2026.9.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Side chat has a visible keyboard shortcut, Command-Shift-S on Apple platforms and Ctrl-Shift-S elsewhere, so you can open or close the existing panel without reaching for its tab. Cancelling while conversation context is still loading now retires that request before it can later start a model call or replace a newer answer. The same preparation work is covered by the existing 60-second timeout.

> Long Discord replies keep their code, Unicode characters, and surrounding quote or list context when they need several messages, and attachment captions avoid extra empty code blocks. Sends and edits also preserve intentional indentation and trailing newlines, while an explicitly empty edit can clear an attachment caption without removing the attachment. Extremely small configured message limits can still constrain formatting, and the existing access checks continue to apply.

> Telegram progress mode also keeps Claude CLI commentary in one temporary message, shows when context compaction completes or remains incomplete, and gives the final answer priority over pending commentary. Commentary remains temporary even with verbose mode enabled. For installations that depend on a proxy, explicitly configured trusted SOCKS5 routes now carry Bot API requests and incoming attachments through the intended transport, including supported cases where the media destination cannot be resolved locally; the proxy itself must still be locally resolvable and reachable.

> Astra's full context window is 1,050,000 tokens, with up to 128,000 output tokens, while OpenClaw keeps its default active input budget at 272,000. Choosing Off does not disable Astra's reasoning, and the cost estimate preserves its higher long-context pricing tier.

> OpenClaw now supports Meta's Muse Spark 1.3 , with Standard and Contributor choices for accounts that have access. Both accept text and image input and expose reasoning controls, a 1,048,576-token context window, and up to 131,072 output tokens. Select meta/muse-spark-1.3 for Standard or meta/muse-spark-1.3-contributor for Contributor.

> If compaction is interrupted after OpenClaw saves a new session, supported continuation paths can recover its recorded predecessor and keep the existing native thread. That includes ordinary messages, side questions, and same-thread resume, with outdated queued compaction and control commands prevented from changing the successor session. A confirmed deletion of an ordinary managed Codex thread instead creates a fresh native thread in the same OpenClaw session; it cannot restore the deleted native history.

> Continuing a long Codex conversation now uses a bounded history renderer that keeps the needed context without first building a much larger temporary string. Resuming large saved records also spends less CPU scanning them, and prompt annotation or confirmed steering avoids rebuilding search information when the searchable content has not changed. These changes reduce specific preparation costs; large-record decoding and parsing can still take time.

> Session pruning keeps trimmed tool results trimmed across later requests while preserving the full local history. Direct Anthropic API-key requests in cache-TTL mode use server-side clearing based on token thresholds, rather than the client TTL and hard-clear settings, and protection rules now include historical tools that are no longer available. After restarting a branched conversation, client-side restoration can still pick a sibling branch's pruning marker and change the context sent to the model.

> OpenAI Responses retains the instruction to finish an answer after compaction through reasoning-only and empty-response retries. If request preparation fails, a later successful request can establish fresh continuation state so subsequent turns stop resending the entire history; that first recovery request still sends the full conversation.

> Codex turn usage now adds the reported counts from every unique completed response, including responses before a retry or cancellation. Those totals remain separate from the current context window, so a missing final context snapshot stays unavailable instead of showing the cumulative usage as if it were the remaining conversation context.

> When Desktop disconnects, the browser console keeps the original failure without adding a misleading error from closing an already closed viewer. Desktop stream logs also retain the first known local shutdown trigger separately from the observed connection close code, giving you more useful context when comparing the Gateway and device logs. The intermittent disconnect remains unexplained, and code 1006 on its own does not tell you whether a network, proxy, or local shutdown caused it.

> Questions about a busy day now load only the latest 200 eligible observations already used for the answer context, keeping their chronological order without first loading the whole day's observations.

> Local utilities used to inspect busy ports, identify processes, and clear a port now receive a limited operating-system environment instead of inheriting unrelated provider credentials, application tokens, proxy settings, and runtime overrides. This is scoped to those diagnostic helpers. Redacted logs and sanitized tool results also keep valid JSON fields that could previously disappear, including literal __proto__ fields, while still hiding nested secrets.

> Stopping or timing out compaction now prevents further preparation once cancellation is observed, including after a session handoff, and native CLI cancellation is reported as compaction aborted . An operation already in progress may still need to settle before cleanup completes.

> When a run fails without enough information to classify the cause, the message now says the agent run failed and keeps the available model context instead of blaming the provider. Recognized provider errors retain their specific guidance, so the wording reflects what OpenClaw actually knows without claiming to diagnose or repair an unknown failure.

Source: https://docs.openclaw.ai/releases/2026.9.2
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-09-05-24-safety-and-privacy-changes-in-v2026-9-2|24 Safety and Privacy changes in v2026.9.2]] · Safety and Privacy
- [[Changes/OpenClaw/2026-09-05-3-pricing-model-changes-in-v2026-9-2|3 Pricing Model changes in v2026.9.2]] · Pricing Model
- [[Changes/OpenClaw/2026-09-05-8-editor-experience-changes-in-v2026-9-2|8 Editor Experience changes in v2026.9.2]] · Editor Experience
- [[Changes/OpenClaw/2026-09-05-progress-mode-can-stay-quiet-about-routine-tool-calls-while-keeping-the-updates|Progress mode can stay quiet about routine tool calls while keeping the updates…]] · Presentation Creation
- [[Changes/OpenClaw/2026-09-05-swarm-is-now-available-to-eligible-agents-without-a-separate-enablement-step-so|Swarm is now available to eligible agents without a separate enablement step…]] · Agent Mode
- [[Changes/OpenClaw/2026-09-05-a-rejected-send-can-keep-its-original-attachments-and-retry-action-when-you-leav|A rejected send can keep its original attachments and Retry action when you leave…]] · Files and Data
- [[Changes/OpenClaw/2026-09-05-20-account-and-access-changes-in-v2026-9-2|20 Account and Access changes in v2026.9.2]] · Account and Access
- [[Changes/OpenClaw/2026-09-05-17-model-support-changes-in-v2026-9-2|17 Model Support changes in v2026.9.2]] · Model Support
- [[Changes/OpenClaw/2026-09-05-16-developer-workflow-changes-in-v2026-9-2|16 Developer Workflow changes in v2026.9.2]] · Developer Workflow
- [[Changes/OpenClaw/2026-09-05-21-memory-and-personalization-changes-in-v2026-9-2|21 Memory and Personalization changes in v2026.9.2]] · Memory and Personalization
- [[Changes/OpenClaw/2026-09-05-4-enterprise-and-administration-changes-in-v2026-9-2|4 Enterprise and Administration changes in v2026.9.2]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-09-05-if-background-image-video-or-music-generation-finishes-but-final-delivery-fails|If background image, video or music generation finishes but final delivery fails…]] · Music Generation
- [[Changes/OpenClaw/2026-09-05-34-agent-mode-changes-in-v2026-9-2|34 Agent Mode changes in v2026.9.2]] · Agent Mode
- [[Changes/OpenClaw/2026-09-05-35-apps-and-integrations-changes-in-v2026-9-2|35 Apps and Integrations changes in v2026.9.2]] · Apps and Integrations
- [[Changes/OpenClaw/2026-09-05-8-automation-and-scheduling-changes-in-v2026-9-2|8 Automation and Scheduling changes in v2026.9.2]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-09-05-9-collaboration-changes-in-v2026-9-2|9 Collaboration changes in v2026.9.2]] · Collaboration
- [[Changes/OpenClaw/2026-09-05-10-mobile-and-desktop-changes-in-v2026-9-2|10 Mobile and Desktop changes in v2026.9.2]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-09-05-4-search-and-browsing-changes-in-v2026-9-2|4 Search and Browsing changes in v2026.9.2]] · Search and Browsing
- [[Changes/OpenClaw/2026-09-05-17-voice-and-audio-changes-in-v2026-9-2|17 Voice and Audio changes in v2026.9.2]] · Voice and Audio
- [[Changes/OpenClaw/2026-09-05-21-interface-experience-changes-in-v2026-9-2|21 Interface Experience changes in v2026.9.2]] · Interface Experience
- [[Changes/OpenClaw/2026-09-05-3-reliability-and-performance-changes-in-v2026-9-2|3 Reliability and Performance changes in v2026.9.2]] · Reliability and Performance
- [[Changes/OpenClaw/2026-09-05-you-can-now-put-the-part-of-a-task-you-are-working-on-in-the-main-view-and-keep|Put the part of a task you are working on in the main view and keep the conversation…]] · Developer Workflow
- [[Changes/OpenClaw/2026-09-05-72-other-changes-in-v2026-9-2|72 other changes in v2026.9.2]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Context Window

- Earlier: 2026-09-04 · Kimi Code · [[Changes/Kimi Code/2026-09-04-remind-the-model-of-its-context-budget-before-automatic-compaction-and-after-com|Remind the model of its context budget before automatic compaction, and after…]]
- Later: 2026-09-08 · OpenClaw · [[Changes/OpenClaw/2026-09-08-12-context-window-changes-in-v2026-9-3|12 Context Window changes in v2026.9.3]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-09-18 · Descript · [[Changes/Descript/2019-09-18-double-click-to-select-a-range|Double-click to select a range]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-05-9fe54b&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-05-15-context-window-changes-in-v2026-9-2.md%0ACard%20ID%3A%20openclaw-2026-09-05-9fe54b%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.2%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->