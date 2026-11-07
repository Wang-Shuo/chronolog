---
card_id: openclaw-2026-09-23-28988e
date: '2026-09-23'
description: 'OpenClaw · 2026-09-23 · Context Window: 25 changes in v2026.9.6 — Dedicated
  compaction checkpoint links, history cards and branch or restore controls have been…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-09-18-double-click-to-select-a-range|Double-click
    to select a range]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2562
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 06f689c12780d3e0c9c52201f0c6636c9ee91bdda74da2b2a874c98e4e02451a
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-23-28988e
  comparison: ''
  date: '2026-09-23'
  description: 'OpenClaw — v2026.9.6: 25 Context Window changes'
  evidence:
  - quote: Dedicated compaction checkpoint links, history cards and branch or restore
      controls have been removed, along with sessions.compaction.list , sessions.compaction.branch
      and sessions.compaction.restore . Ordinary Fork, rewind, conversation history,
      compaction summaries and available token-savings reporting remain. There is
      no equivalent replacement for checkpoint restore, and the retirement does not
      require a data purge or configuration migration.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Chat notices, reply context, Goal previews and selected recipients sit
      above a reachable message field in a bounded footer, keeping controls usable
      in narrow or overlapping panes. Shared pickers continue to dismiss correctly
      as panes close, and moving between menu rows closes the previous submenu. Removing
      a selected recipient leaves the mention text in your message.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Long pasted excerpts appear as two-line cards in the composer and compact
      chips in sent messages, while newly attached Home context appears separately
      from the words you wrote. You can inspect the source, copy the original text
      or choose Show in text field directly on its card to restore it alongside your
      current draft without sending. The text sent to the model stays unchanged. Pasted-text
      previews cover up to 256 KiB and downloads retain the full content. The Home
      treatment applies to new messages with recorded context metadata, and attached
      context grants no additional permissions.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Usage opens with the last 30 calendar days, with history and totals covering
      the full session report you’re allowed to see, even beyond the visible list.
      Started by helps you compare tokens, estimated costs and session counts by who
      started the work. Each whole session is attributed to its recorded creator,
      with older unknown creators shown as Unattributed .
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Conversations keep more of the context needed to answer a follow-up, and
      accepted requests have clearer paths to a final reply. Changes across the messaging
      channels also keep progress, attachments, and delivery results attached to the
      work they describe.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Telegram group and topic history now survives restarts and /new or /reset
      , so the agent can look back at earlier discussion when a recent message refers
      to it. The automatic context window stays bounded, normally at 50 messages,
      while explicit reads can page through older permitted messages. Mention requirements
      still apply, and reads stay within the authorized account, group, topic, and
      sender permissions. Only messages OpenClaw received and was allowed to record
      are retained, and older attachments may expire.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Retained group history grows with traffic. Setting historyLimit to 0 turns
      off automatic context but keeps recording and explicit reads enabled, while
      resetting a session does not delete that history. Make a compatible pre-update
      backup if you may need to downgrade, and restore it before running an older
      release against this data because older versions can damage expanded retained
      history.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Automatic observed-message context is now capped at 200 messages. The maximum
      JSON integer selects each channel's default instead, while other oversized settings
      use the cap. Saved settings, stored messages, transcript retention, and explicit
      Telegram history reads are unchanged.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Interactive chats can show a waiting acknowledgement when delegated work
      would otherwise go quiet, and status checks remain visible without interrupting
      the running task or entering its later model context. Private child results
      return internally to the correct conversation, while cross-session requests
      from the Control UI receive their result without bouncing the human-facing response
      back to the other session. Thread-bound spawning is available again where channel
      settings and permissions enable it. The waiting acknowledgement is a single
      update, while independent agent peers keep their existing bounded exchanges.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: An accepted message can continue once through verified conversation compaction,
      which condenses older context to make room for more work. When continuation
      cannot be established, Refresh preserves the draft without sending a second
      message. Reset, replacement, restart, and cancellation checks still apply, and
      clients waiting on a canceled chat now receive its completion result after the
      running dispatch settles instead of waiting until they time out.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: When Telegram sticker media is unavailable, its emoji and reply context
      remain in the conversation instead of leaving a blank turn that could revive
      an unrelated request. A sticker label fills in when no emoji is available, without
      adding visual analysis or animated and video sticker downloads.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: When someone adds or removes a reaction in a channel thread, the agent
      now receives that reaction's context in the owning thread rather than the parent
      conversation.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: In Teams channels where the bot waits for a mention, unmentioned messages
      now stay available for the next request in their own thread. Answering in another
      thread no longer consumes that pending context. Group chats and messages without
      a thread keep their existing history behavior, and the separate issue of rapid
      messages from different threads being batched together remains outside this
      fix.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Context engines that opt into background maintenance can now start summarizing
      after a saved conversation turn, using idle time without holding up the completed
      reply. Engines using foreground maintenance, or leaving the mode unspecified,
      still wait for that work, and some compaction may still happen during later
      turns. New conversation summaries also receive independent text blocks with
      their boundaries preserved, avoiding text being joined together before summarization.
      Existing summaries remain unchanged.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: When the compaction quality guard checks a shortened conversation, it now
      recognizes short requests such as “How about now?” that the summary correctly
      retained. This avoids unnecessary retries or cancellation caused by that matching
      error when the guard is enabled.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: New Dream Diary entries now save when their recent context was only shortened
      to fit, instead of being mistakenly discarded as stale. Actual context changes
      and Forget still prevent stale entries from being written, and previously discarded
      entries are not recreated. Dreaming also stops trying to reconcile its scheduled
      jobs while scheduling is disabled, preserving those jobs for later. Explicitly
      disabling dreaming removes its managed jobs, and resuming scheduling still requires
      an eligible owner.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Native Mac Quick Chat keeps one composer beneath the conversation, preserving
      your draft and streamed reply when you collapse and reopen it. Separate model
      and Effort controls make thinking levels and supported Fast mode easier to choose,
      while the context ring offers Compact Thread. Model pickers keep usable choices
      visible without unrelated discovery warnings, and capture actions sit in the
      plus menu. Screenshot capture still sends after selection.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Grok 4.7 adds a text-and-image model choice with reasoning levels from
      low through xhigh. New xAI setups choose it when no primary model is selected,
      and web search, X search, and code execution use it when their model setting
      is omitted, including on existing installations. Explicit primary and tool selections
      stay pinned. Eligible Doctor repairs replace retired xai/auto selections while
      preserving account pins, fallbacks, and authored settings. Pricing above 200,000
      tokens differs from the short-context catalog rates.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Eligible background text requests can try prepared backup accounts while
      respecting explicit account pins, and canceled requests stop waiting for a shared
      credential refresh. Saved cloud failures retain their cause, partial output,
      and usage. Claude also retains generated partial replies and final usage when
      its context window fills, without completing the truncated answer. Check what
      already completed before retrying a failed run, because earlier tool actions
      may have taken effect.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Configured cache-TTL pruning now removes expired tool output on eligible
      OpenAI and ChatGPT/Codex routes. It remains opt-in, and custom proxies must
      explicitly support prompt-cache keys. Preparing long conversations also avoids
      some repeated request-copying and Unicode cleanup work while preserving valid
      multilingual text and emoji.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Native Ollama compaction checks now use valid measured prompt, output,
      and cached-token counts, falling back to estimates when those counts are missing
      or invalid.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Codex conversations keep their selected physical source, with stop and
      steer reaching the active turn and completed forks retaining their outcome.
      Compaction waits for confirmation, valid retained text spans can be forked when
      runtime policy permits, and oversized tool results can be replaced with explicit
      omission notices when reopening a conversation without changing its full transcript.
      New sender-attributed messages also preserve the submitted text needed for branching;
      older mismatched transcripts are not rewritten. Recent assistant explanations
      survive thread rotation, and successful rewinds or branch switches retire stale
      native context so the next turn follows the selected history.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Switching session stores now stops delayed child-agent activity from bringing
      the old store's context into a new conversation. Changing stores does not migrate
      conversations, and suspended child-result delivery needs explicit recovery even
      if you later select the old store again. Completed task results remain available;
      old watches whose store ownership is unknown need fresh registration. Separately,
      creating an incognito session with an explicit key checks for a collision without
      scanning unrelated durable history, while preserving existing isolation and
      authorization rules.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Operators can add optional personal preference files at users/<canonical-profile-id>/USER.md
      in an agent's workspace. Shared USER.md defaults load first, followed by at
      most one personal file selected for the assigned human session owner, or otherwise
      the authenticated human creator. Other participants can steer the conversation
      without replacing its running personal context, and reassignment takes effect
      on the next new turn, including queued work.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Optional archive cleanup now waits for a later opportunity when the database
      is busy, instead of holding up OpenClaw. Work already accepted can finish before
      a database worker closes, and saving device tokens or task information avoids
      additional waits on the main process. State directories reached through filesystem
      aliases, such as macOS /var and /private/var , also avoid a timeout caused by
      treating those paths as different locations. Fully received results survive
      cleanup failures, while writes with an unknown outcome are not automatically
      repeated. Database requests also avoid being refused prematurely just because
      a busy Gateway has not yet made its access decision.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 25-context-window-changes-in-v2026-9-6
  source_release: openclaw-2026-09-23-v2026-9-6-3f12c824
  source_type: openclaw_changelog
  theme: context-window
  title: 25 Context Window changes in v2026.9.6
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-09-22-17-context-window-changes-in-rust-v0-156-0|17 Context
  Window changes in rust-v0.156.0]]'
- '[[Changes/Devin/2026-09-23-microsoft-teams-commands-context-and-dm-cards|Microsoft
  Teams: Commands, Context and DM Cards]]'
- '[[Changes/Microsoft 365 Copilot/2026-09-23-new-copilot-notebooks-design-in-the-microsoft-365-copilot-app-web-microsoft-365|New
  Copilot Notebooks design in the Microsoft 365 Copilot App…]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-23-v2026-9-6-3f12c824|openclaw-2026-09-23-v2026-9-6-3f12c824]]'
source_type: openclaw_changelog
theme: context-window
title: 25 Context Window changes in v2026.9.6
type: change
---

<!-- chronolog:begin region="header" -->
# 25 Context Window changes in v2026.9.6

**OpenClaw** · 2026-09-23 · [[Themes/context-window|Context Window]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.6) · from [[Releases/OpenClaw/openclaw-2026-09-23-v2026-9-6-3f12c824|v2026.9.6]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Dedicated compaction checkpoint links, history cards and branch or restore controls have been removed, along with sessions.compaction.list , sessions.compaction.branch and sessions.compaction.restore . Ordinary Fork, rewind, conversation history, compaction summaries and available token-savings reporting remain. There is no equivalent replacement for checkpoint restore, and the retirement does not require a data purge or configuration migration.

> Chat notices, reply context, Goal previews and selected recipients sit above a reachable message field in a bounded footer, keeping controls usable in narrow or overlapping panes. Shared pickers continue to dismiss correctly as panes close, and moving between menu rows closes the previous submenu. Removing a selected recipient leaves the mention text in your message.

> Long pasted excerpts appear as two-line cards in the composer and compact chips in sent messages, while newly attached Home context appears separately from the words you wrote. You can inspect the source, copy the original text or choose Show in text field directly on its card to restore it alongside your current draft without sending. The text sent to the model stays unchanged. Pasted-text previews cover up to 256 KiB and downloads retain the full content. The Home treatment applies to new messages with recorded context metadata, and attached context grants no additional permissions.

> Usage opens with the last 30 calendar days, with history and totals covering the full session report you’re allowed to see, even beyond the visible list. Started by helps you compare tokens, estimated costs and session counts by who started the work. Each whole session is attributed to its recorded creator, with older unknown creators shown as Unattributed .

> Conversations keep more of the context needed to answer a follow-up, and accepted requests have clearer paths to a final reply. Changes across the messaging channels also keep progress, attachments, and delivery results attached to the work they describe.

> Telegram group and topic history now survives restarts and /new or /reset , so the agent can look back at earlier discussion when a recent message refers to it. The automatic context window stays bounded, normally at 50 messages, while explicit reads can page through older permitted messages. Mention requirements still apply, and reads stay within the authorized account, group, topic, and sender permissions. Only messages OpenClaw received and was allowed to record are retained, and older attachments may expire.

> Retained group history grows with traffic. Setting historyLimit to 0 turns off automatic context but keeps recording and explicit reads enabled, while resetting a session does not delete that history. Make a compatible pre-update backup if you may need to downgrade, and restore it before running an older release against this data because older versions can damage expanded retained history.

> Automatic observed-message context is now capped at 200 messages. The maximum JSON integer selects each channel's default instead, while other oversized settings use the cap. Saved settings, stored messages, transcript retention, and explicit Telegram history reads are unchanged.

> Interactive chats can show a waiting acknowledgement when delegated work would otherwise go quiet, and status checks remain visible without interrupting the running task or entering its later model context. Private child results return internally to the correct conversation, while cross-session requests from the Control UI receive their result without bouncing the human-facing response back to the other session. Thread-bound spawning is available again where channel settings and permissions enable it. The waiting acknowledgement is a single update, while independent agent peers keep their existing bounded exchanges.

> An accepted message can continue once through verified conversation compaction, which condenses older context to make room for more work. When continuation cannot be established, Refresh preserves the draft without sending a second message. Reset, replacement, restart, and cancellation checks still apply, and clients waiting on a canceled chat now receive its completion result after the running dispatch settles instead of waiting until they time out.

> When Telegram sticker media is unavailable, its emoji and reply context remain in the conversation instead of leaving a blank turn that could revive an unrelated request. A sticker label fills in when no emoji is available, without adding visual analysis or animated and video sticker downloads.

> When someone adds or removes a reaction in a channel thread, the agent now receives that reaction's context in the owning thread rather than the parent conversation.

> In Teams channels where the bot waits for a mention, unmentioned messages now stay available for the next request in their own thread. Answering in another thread no longer consumes that pending context. Group chats and messages without a thread keep their existing history behavior, and the separate issue of rapid messages from different threads being batched together remains outside this fix.

> Context engines that opt into background maintenance can now start summarizing after a saved conversation turn, using idle time without holding up the completed reply. Engines using foreground maintenance, or leaving the mode unspecified, still wait for that work, and some compaction may still happen during later turns. New conversation summaries also receive independent text blocks with their boundaries preserved, avoiding text being joined together before summarization. Existing summaries remain unchanged.

> When the compaction quality guard checks a shortened conversation, it now recognizes short requests such as “How about now?” that the summary correctly retained. This avoids unnecessary retries or cancellation caused by that matching error when the guard is enabled.

> New Dream Diary entries now save when their recent context was only shortened to fit, instead of being mistakenly discarded as stale. Actual context changes and Forget still prevent stale entries from being written, and previously discarded entries are not recreated. Dreaming also stops trying to reconcile its scheduled jobs while scheduling is disabled, preserving those jobs for later. Explicitly disabling dreaming removes its managed jobs, and resuming scheduling still requires an eligible owner.

> Native Mac Quick Chat keeps one composer beneath the conversation, preserving your draft and streamed reply when you collapse and reopen it. Separate model and Effort controls make thinking levels and supported Fast mode easier to choose, while the context ring offers Compact Thread. Model pickers keep usable choices visible without unrelated discovery warnings, and capture actions sit in the plus menu. Screenshot capture still sends after selection.

> Grok 4.7 adds a text-and-image model choice with reasoning levels from low through xhigh. New xAI setups choose it when no primary model is selected, and web search, X search, and code execution use it when their model setting is omitted, including on existing installations. Explicit primary and tool selections stay pinned. Eligible Doctor repairs replace retired xai/auto selections while preserving account pins, fallbacks, and authored settings. Pricing above 200,000 tokens differs from the short-context catalog rates.

> Eligible background text requests can try prepared backup accounts while respecting explicit account pins, and canceled requests stop waiting for a shared credential refresh. Saved cloud failures retain their cause, partial output, and usage. Claude also retains generated partial replies and final usage when its context window fills, without completing the truncated answer. Check what already completed before retrying a failed run, because earlier tool actions may have taken effect.

> Configured cache-TTL pruning now removes expired tool output on eligible OpenAI and ChatGPT/Codex routes. It remains opt-in, and custom proxies must explicitly support prompt-cache keys. Preparing long conversations also avoids some repeated request-copying and Unicode cleanup work while preserving valid multilingual text and emoji.

> Native Ollama compaction checks now use valid measured prompt, output, and cached-token counts, falling back to estimates when those counts are missing or invalid.

> Codex conversations keep their selected physical source, with stop and steer reaching the active turn and completed forks retaining their outcome. Compaction waits for confirmation, valid retained text spans can be forked when runtime policy permits, and oversized tool results can be replaced with explicit omission notices when reopening a conversation without changing its full transcript. New sender-attributed messages also preserve the submitted text needed for branching; older mismatched transcripts are not rewritten. Recent assistant explanations survive thread rotation, and successful rewinds or branch switches retire stale native context so the next turn follows the selected history.

> Switching session stores now stops delayed child-agent activity from bringing the old store's context into a new conversation. Changing stores does not migrate conversations, and suspended child-result delivery needs explicit recovery even if you later select the old store again. Completed task results remain available; old watches whose store ownership is unknown need fresh registration. Separately, creating an incognito session with an explicit key checks for a collision without scanning unrelated durable history, while preserving existing isolation and authorization rules.

> Operators can add optional personal preference files at users/\<canonical-profile-id>/USER.md in an agent's workspace. Shared USER.md defaults load first, followed by at most one personal file selected for the assigned human session owner, or otherwise the authenticated human creator. Other participants can steer the conversation without replacing its running personal context, and reassignment takes effect on the next new turn, including queued work.

> Optional archive cleanup now waits for a later opportunity when the database is busy, instead of holding up OpenClaw. Work already accepted can finish before a database worker closes, and saving device tokens or task information avoids additional waits on the main process. State directories reached through filesystem aliases, such as macOS /var and /private/var , also avoid a timeout caused by treating those paths as different locations. Fully received results survive cleanup failures, while writes with an unknown outcome are not automatically repeated. Database requests also avoid being refused prematurely just because a busy Gateway has not yet made its access decision.

Source: https://docs.openclaw.ai/releases/2026.9.6
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-09-23-50-safety-and-privacy-changes-in-v2026-9-6|50 Safety and Privacy changes in v2026.9.6]] · Safety and Privacy
- [[Changes/OpenClaw/2026-09-23-localization-maintenance-removes-entries-whose-interface-text-has-already-been-r|Localization maintenance removes entries whose interface text has already been…]] · Accessibility and Localization
- [[Changes/OpenClaw/2026-09-23-5-reliability-and-performance-changes-in-v2026-9-6|5 Reliability and Performance changes in v2026.9.6]] · Reliability and Performance
- [[Changes/OpenClaw/2026-09-23-2-image-generation-changes-in-v2026-9-6|2 Image Generation changes in v2026.9.6]] · Image Generation
- [[Changes/OpenClaw/2026-09-23-18-voice-and-audio-changes-in-v2026-9-6|18 Voice and Audio changes in v2026.9.6]] · Voice and Audio
- [[Changes/OpenClaw/2026-09-23-16-mobile-and-desktop-changes-in-v2026-9-6|16 Mobile and Desktop changes in v2026.9.6]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-09-23-41-agent-mode-changes-in-v2026-9-6|41 Agent Mode changes in v2026.9.6]] · Agent Mode
- [[Changes/OpenClaw/2026-09-23-16-collaboration-changes-in-v2026-9-6|16 Collaboration changes in v2026.9.6]] · Collaboration
- [[Changes/OpenClaw/2026-09-23-15-editor-experience-changes-in-v2026-9-6|15 Editor Experience changes in v2026.9.6]] · Editor Experience
- [[Changes/OpenClaw/2026-09-23-2-enterprise-and-administration-changes-in-v2026-9-6|2 Enterprise and Administration changes in v2026.9.6]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-09-23-31-developer-workflow-changes-in-v2026-9-6|31 Developer Workflow changes in v2026.9.6]] · Developer Workflow
- [[Changes/OpenClaw/2026-09-23-8-pricing-model-changes-in-v2026-9-6|8 Pricing Model changes in v2026.9.6]] · Pricing Model
- [[Changes/OpenClaw/2026-09-23-plugin-requested-answer-revisions-wait-for-session-history-to-become-available-a|Plugin-requested answer revisions wait for session history to become available…]] · Projects and Workspaces
- [[Changes/OpenClaw/2026-09-23-6-files-and-data-changes-in-v2026-9-6|6 Files and Data changes in v2026.9.6]] · Files and Data
- [[Changes/OpenClaw/2026-09-23-58-apps-and-integrations-changes-in-v2026-9-6|58 Apps and Integrations changes in v2026.9.6]] · Apps and Integrations
- [[Changes/OpenClaw/2026-09-23-17-account-and-access-changes-in-v2026-9-6|17 Account and Access changes in v2026.9.6]] · Account and Access
- [[Changes/OpenClaw/2026-09-23-background-image-video-and-music-generation-can-complete-independently-of-the-re|Background image, video, and music generation can complete independently…]] · Music Generation
- [[Changes/OpenClaw/2026-09-23-23-memory-and-personalization-changes-in-v2026-9-6|23 Memory and Personalization changes in v2026.9.6]] · Memory and Personalization
- [[Changes/OpenClaw/2026-09-23-3-search-and-browsing-changes-in-v2026-9-6|3 Search and Browsing changes in v2026.9.6]] · Search and Browsing
- [[Changes/OpenClaw/2026-09-23-19-interface-experience-changes-in-v2026-9-6|19 Interface Experience changes in v2026.9.6]] · Interface Experience
- [[Changes/OpenClaw/2026-09-23-9-automation-and-scheduling-changes-in-v2026-9-6|9 Automation and Scheduling changes in v2026.9.6]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-09-23-22-model-support-changes-in-v2026-9-6|22 Model Support changes in v2026.9.6]] · Model Support
- [[Changes/OpenClaw/2026-09-23-119-other-changes-in-v2026-9-6|119 other changes in v2026.9.6]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Context Window

- Earlier: 2026-09-23 · Microsoft 365 Copilot · [[Changes/Microsoft 365 Copilot/2026-09-23-new-copilot-notebooks-design-in-the-microsoft-365-copilot-app-web-microsoft-365|New Copilot Notebooks design in the Microsoft 365 Copilot App…]]
- Later: 2026-09-24 · Cline · [[Changes/Cline/2026-09-24-long-replies-on-local-models-llama-cpp-ollama-lm-studio-that-hit-the-output-toke|Long replies on local models (llama.cpp, Ollama, LM Studio) that hit…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-09-18 · Descript · [[Changes/Descript/2019-09-18-double-click-to-select-a-range|Double-click to select a range]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-23-28988e&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-23-25-context-window-changes-in-v2026-9-6.md%0ACard%20ID%3A%20openclaw-2026-09-23-28988e%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.6%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->