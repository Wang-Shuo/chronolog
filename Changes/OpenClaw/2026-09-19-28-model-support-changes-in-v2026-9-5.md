---
card_id: openclaw-2026-09-19-3aed71
date: '2026-09-19'
description: 'OpenClaw · 2026-09-19 · Model Support: 28 changes in v2026.9.5 — Interrupted
  local setup can now finish in the workspace you already approved while keeping…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1349
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 8f800dfc4d9d1c39e9bafbe0daffc1f62a50c277d01dc1434e6b0557e4ec5f0d
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-19-3aed71
  comparison: ''
  date: '2026-09-19'
  description: 'OpenClaw — v2026.9.5: 28 Model Support changes'
  evidence:
  - quote: Interrupted local setup can now finish in the workspace you already approved
      while keeping your saved agents, model and runtime choices. Recovery checks
      that the pending setup still belongs to the same configuration, so replacing
      the configuration or switching to a remote Gateway does not carry that approval
      forward.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: 'Synthetic example: Check the reasoning without steering the main conversation
      away from its task.'
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Opening one conversation no longer waits for the entire session list to
      refresh. Stored titles and usage can appear first, while older titles, previews,
      and some model details arrive later. Cold archives and oversized content can
      remain without those optional details, and missing usage is not reconstructed.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Conversation saves and model changes wait for database maintenance and
      cleanup shutdown before writing. Canceled conversation changes stay canceled.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Mattermost offers buttons for supported simple questions, so you can choose
      an answer without retyping it. Typing still works, and questions needing private
      or more complex answers stay in text. Model menus also reflect the account selected
      for the conversation.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: If a room conversation still cannot continue after restart recovery, a
      reminder can explain how to start again. Use an authorized /reset or /new ,
      or choose Resume in new session in WebChat when the model is locked. Starting
      fresh keeps the old transcript.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: If Linux Quick Chat loses confirmation of a finished request, retrying
      the unchanged draft can retrieve its completed answer without asking the model
      again. The recovered reply clears the busy state so you can continue typing.
      If recent history is unavailable or contains no matching completed answer, the
      error remains.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: New Thread keeps your selected agent and offers a separate Git working
      copy when needed. The revised layout leaves more room for reading, the message
      box grows with your draft, and model sign-in sits nearby when credentials need
      attention. Full chat windows also keep Reasoning, Tool Activity, pinned and
      recent models, and collapsed sidebar groups in the active profile. Named profiles
      use their own model and sidebar choices or normal defaults; unrelated global
      preferences are not copied into them.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: If you declare a provider in current settings, supply its credentials and
      headers through the supported account or configuration settings. Keys and headers
      stored only in an older models.json no longer fill gaps in that declaration.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: If an older catalog is stored only in legacy files, run openclaw doctor
      --fix to import or repair it; ordinary discovery no longer changes those saved
      files. Unsupported native model IDs may also need an explicit definition before
      they can be selected or used for a child session. Doctor can repair supported
      retired Grok choices while preserving account pins and restrictions.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: When you delegate work to a child using the same agent, it inherits the
      model currently running in the parent, including temporary overrides. An explicit
      child choice or configured child model takes precedence, and a different agent
      uses its own selection. New visible child sessions also retain their configured
      backup models on later requests when selection was automatic; explicit choices,
      locks and empty backup lists stay strict. Existing children with incorrectly
      saved manual choices are not automatically repaired.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: When a provider asks OpenClaw to wait, affected runs can finish that retry
      delay without being mistaken for stuck work. Exhausted daily caps, including
      OpenRouter's free-model limits, skip futile same-model retries and move to eligible
      configured alternatives. Interrupted Responses tool calls can also continue
      from saved results without executing partial arguments. Cancellation, execution
      deadlines and existing retry limits still apply.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Fable 5 and 5.1 now inherit Medium reasoning effort, as does GPT-6 Astra
      when the account supports it. Your explicit effort settings still win. Fable
      and Mythos offer their supported Low through Max choices; update scripts that
      send /think minimal or /think adaptive to use /think low or /think high instead.
      The thinking guide explains model-specific defaults and how /think default clears
      a saved session override.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Thinking choices also stay with the selected model and runtime across interactive
      and automated work. Supported effort levels still depend on that route; selecting
      Off does not make a model with mandatory reasoning stop reasoning.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Custom OpenAI-compatible models keep their declared advanced reasoning
      levels when you start a session and send requests, within the API's supported
      limits. Custom Anthropic and Mistral requests also keep your chosen response-length
      limit when the model's information omits an output ceiling. Provider limits
      still apply, and Anthropic manual thinking is disabled if it cannot fit that
      response budget.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: OpenClaw now counts tool definitions when checking how much room a model
      has left for a reply. Affected OpenAI-compatible requests log a warning when
      almost no room remains, helping explain unexpectedly short answers. Custom models
      configured below the existing 4,000-token minimum now stop before sending a
      request, even if you set a larger input cap. Correct the model's declared window
      or choose one with enough room.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: 'A verified compatible custom Responses model can opt into stored HTTP
      continuation with compat.supportsResponsesContinuation set to true , allowing
      later turns to send new input with a reference to the previous response. This
      deliberately permits the backend to retain requests, even on turns that cannot
      continue. supportsStore: false and explicit no-store policy still take precedence.
      Dedicated Azure and ChatGPT/Codex routes are excluded, and some turns may still
      resend full history. See provider configuration before enabling it.'
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Tools used through ChatGPT subscriptions can leave unused optional arguments
      absent instead of filling them with empty placeholders. The correction applies
      to HTTP and WebSocket requests. Required fields and tool-execution checks remain
      in place; this does not change strict structured response output or guarantee
      which optional values a model will choose.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Image descriptions and PDF analysis keep the model selected for that request,
      and PDF results name the selected model consistently. Heavy image and PDF processing
      can run separately so other OpenClaw requests continue and cancellation can
      take effect. Busy workers can reject new work, and their three-minute deadline
      includes time spent waiting.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: The new Radius provider connects your organization's model access through
      browser sign-in or an API key, with streamed answers and supported image and
      tool use. Requests use the selected organization's credits and follow its budgets
      and policies. Available models depend on that access, and some advertised models
      can still be unavailable upstream.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Automatic retries are enabled for eligible unlocked settings and require
      access granted by the provider. An unavailable target can add a request and
      delay. Strict model selections, other refusal types and work that cannot safely
      be repeated still stop without a retry. To disable retries, set plugins.entries.codex.config.appServer.cyberFailover.mode
      to off for native Codex, or agents.defaults.embeddedAgent.cyberFailover.mode
      to off for embedded turns. See model failover for configuration.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: You can offer the same model through OpenClaw and Codex as separate, labeled
      choices in the chat model picker. Each choice shows the reasoning and context
      options that its runtime supports. To enable this, set pickerRuntimes on an
      exact model entry, with up to eight explicit runtime IDs. Your configured agentRuntime
      stays the default. Per-agent lists replace inherited alternatives, and an empty
      list removes them. See the models guide for configuration.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Quiet heartbeat checks can finish in the built-in runtime without an unwanted
      missing-summary warning or another finalization request. If a check falls back
      to a CLI backend without the response tool, it now receives explicit guidance
      to stay silent when nothing needs attention. That fallback still depends on
      the model following the instructions. Accepted alerts and private monitor notes
      also survive retries and compaction, while stopping or superseding a check suppresses
      its delivery.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Use an updated, loaded adapter with support for the scheduled action. Older
      jobs missing creator or requester information need fresh authenticated authorization
      or recreation. Changes to executable behavior, such as a prompt, model or schedule,
      can clear prior requester or local-read authority and stop further affected
      actions; an edit already accepted by Discord can still return its confirmed
      result. Reauthorize from the owning Discord conversation or, for local-read
      authority, a fresh authenticated local session. Remote management alone cannot
      grant local-read authority. The scheduled payload guide explains the required
      complete tool allowance and recovery paths.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Experimental Claw packages now preserve explicit model preferences and
      delegation settings. With a local Gateway running, add and update can activate
      up to 64 required plugins together after the usual trust and capability confirmations.
      Missing models and companion agents still need to be configured separately.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: After a restart, eligible unfinished conversations can continue from saved
      tool work without repeating your original message or discarding its results.
      Eligible tasks in the built-in runtime can also keep working when their tools
      have finished but the model times out, or when a known Responses output limit
      interrupts a tool call. Cancellation, pending approvals, unfinished tool work,
      and retry limits still apply. Messages arriving too late to join the current
      answer get their own follow-up reply. ACP background tasks that finish before
      cancellation takes effect keep their completed result and end time.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: When prompted, recover interrupted work before sending new input, and check
      uncertain tool outcomes before repeating an action. New messages can wait as
      follow-ups while recovery handles the earlier task. Acknowledged worker cleanup
      failures now block automatic model fallback from repeating completed actions.
      Cleanup does not undo earlier desktop input, so inspect the desktop and workspace
      before retrying.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: QA runtime reports keep skipped executions distinct from passing ones while
      preserving their existing acceptance rules. Maintainers can also compare clean
      built revisions with six opt-in Code Mode workloads. These require an OpenAI
      API key and explicit model selection, make paid calls, and assess task results
      separately from follow-up explanations.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 28-model-support-changes-in-v2026-9-5
  source_release: openclaw-2026-09-19-v2026-9-5-506f537c
  source_type: openclaw_changelog
  theme: model-support
  title: 28 Model Support changes in v2026.9.5
  type: change
related_changes:
- '[[Changes/Google Antigravity/2026-09-18-a-malformed-tool-call-from-the-model-now-appears-as-a-short-invalid-tool-call-no|A
  malformed tool call from the model now appears as a short "Invalid tool call" note…]]'
- '[[Changes/Runway/2026-09-18-kling-o3-4k-kling-3-0-standard-kling-o3-standard-and-kling-3-0-motion-control-ar|Kling
  Models on Runway MCP]]'
- '[[Changes/Ollama/2026-09-19-2-model-support-changes-in-v0-34-3|2 Model Support
  changes in v0.34.3]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-19-v2026-9-5-506f537c|openclaw-2026-09-19-v2026-9-5-506f537c]]'
source_type: openclaw_changelog
theme: model-support
title: 28 Model Support changes in v2026.9.5
type: change
---

<!-- chronolog:begin region="header" -->
# 28 Model Support changes in v2026.9.5

**OpenClaw** · 2026-09-19 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.5) · from [[Releases/OpenClaw/openclaw-2026-09-19-v2026-9-5-506f537c|v2026.9.5]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Interrupted local setup can now finish in the workspace you already approved while keeping your saved agents, model and runtime choices. Recovery checks that the pending setup still belongs to the same configuration, so replacing the configuration or switching to a remote Gateway does not carry that approval forward.

> Synthetic example: Check the reasoning without steering the main conversation away from its task.

> Opening one conversation no longer waits for the entire session list to refresh. Stored titles and usage can appear first, while older titles, previews, and some model details arrive later. Cold archives and oversized content can remain without those optional details, and missing usage is not reconstructed.

> Conversation saves and model changes wait for database maintenance and cleanup shutdown before writing. Canceled conversation changes stay canceled.

> Mattermost offers buttons for supported simple questions, so you can choose an answer without retyping it. Typing still works, and questions needing private or more complex answers stay in text. Model menus also reflect the account selected for the conversation.

> If a room conversation still cannot continue after restart recovery, a reminder can explain how to start again. Use an authorized /reset or /new , or choose Resume in new session in WebChat when the model is locked. Starting fresh keeps the old transcript.

> If Linux Quick Chat loses confirmation of a finished request, retrying the unchanged draft can retrieve its completed answer without asking the model again. The recovered reply clears the busy state so you can continue typing. If recent history is unavailable or contains no matching completed answer, the error remains.

> New Thread keeps your selected agent and offers a separate Git working copy when needed. The revised layout leaves more room for reading, the message box grows with your draft, and model sign-in sits nearby when credentials need attention. Full chat windows also keep Reasoning, Tool Activity, pinned and recent models, and collapsed sidebar groups in the active profile. Named profiles use their own model and sidebar choices or normal defaults; unrelated global preferences are not copied into them.

> If you declare a provider in current settings, supply its credentials and headers through the supported account or configuration settings. Keys and headers stored only in an older models.json no longer fill gaps in that declaration.

> If an older catalog is stored only in legacy files, run openclaw doctor --fix to import or repair it; ordinary discovery no longer changes those saved files. Unsupported native model IDs may also need an explicit definition before they can be selected or used for a child session. Doctor can repair supported retired Grok choices while preserving account pins and restrictions.

> When you delegate work to a child using the same agent, it inherits the model currently running in the parent, including temporary overrides. An explicit child choice or configured child model takes precedence, and a different agent uses its own selection. New visible child sessions also retain their configured backup models on later requests when selection was automatic; explicit choices, locks and empty backup lists stay strict. Existing children with incorrectly saved manual choices are not automatically repaired.

> When a provider asks OpenClaw to wait, affected runs can finish that retry delay without being mistaken for stuck work. Exhausted daily caps, including OpenRouter's free-model limits, skip futile same-model retries and move to eligible configured alternatives. Interrupted Responses tool calls can also continue from saved results without executing partial arguments. Cancellation, execution deadlines and existing retry limits still apply.

> Fable 5 and 5.1 now inherit Medium reasoning effort, as does GPT-6 Astra when the account supports it. Your explicit effort settings still win. Fable and Mythos offer their supported Low through Max choices; update scripts that send /think minimal or /think adaptive to use /think low or /think high instead. The thinking guide explains model-specific defaults and how /think default clears a saved session override.

> Thinking choices also stay with the selected model and runtime across interactive and automated work. Supported effort levels still depend on that route; selecting Off does not make a model with mandatory reasoning stop reasoning.

> Custom OpenAI-compatible models keep their declared advanced reasoning levels when you start a session and send requests, within the API's supported limits. Custom Anthropic and Mistral requests also keep your chosen response-length limit when the model's information omits an output ceiling. Provider limits still apply, and Anthropic manual thinking is disabled if it cannot fit that response budget.

> OpenClaw now counts tool definitions when checking how much room a model has left for a reply. Affected OpenAI-compatible requests log a warning when almost no room remains, helping explain unexpectedly short answers. Custom models configured below the existing 4,000-token minimum now stop before sending a request, even if you set a larger input cap. Correct the model's declared window or choose one with enough room.

> A verified compatible custom Responses model can opt into stored HTTP continuation with compat.supportsResponsesContinuation set to true , allowing later turns to send new input with a reference to the previous response. This deliberately permits the backend to retain requests, even on turns that cannot continue. supportsStore: false and explicit no-store policy still take precedence. Dedicated Azure and ChatGPT/Codex routes are excluded, and some turns may still resend full history. See provider configuration before enabling it.

> Tools used through ChatGPT subscriptions can leave unused optional arguments absent instead of filling them with empty placeholders. The correction applies to HTTP and WebSocket requests. Required fields and tool-execution checks remain in place; this does not change strict structured response output or guarantee which optional values a model will choose.

> Image descriptions and PDF analysis keep the model selected for that request, and PDF results name the selected model consistently. Heavy image and PDF processing can run separately so other OpenClaw requests continue and cancellation can take effect. Busy workers can reject new work, and their three-minute deadline includes time spent waiting.

> The new Radius provider connects your organization's model access through browser sign-in or an API key, with streamed answers and supported image and tool use. Requests use the selected organization's credits and follow its budgets and policies. Available models depend on that access, and some advertised models can still be unavailable upstream.

> Automatic retries are enabled for eligible unlocked settings and require access granted by the provider. An unavailable target can add a request and delay. Strict model selections, other refusal types and work that cannot safely be repeated still stop without a retry. To disable retries, set plugins.entries.codex.config.appServer.cyberFailover.mode to off for native Codex, or agents.defaults.embeddedAgent.cyberFailover.mode to off for embedded turns. See model failover for configuration.

> You can offer the same model through OpenClaw and Codex as separate, labeled choices in the chat model picker. Each choice shows the reasoning and context options that its runtime supports. To enable this, set pickerRuntimes on an exact model entry, with up to eight explicit runtime IDs. Your configured agentRuntime stays the default. Per-agent lists replace inherited alternatives, and an empty list removes them. See the models guide for configuration.

> Quiet heartbeat checks can finish in the built-in runtime without an unwanted missing-summary warning or another finalization request. If a check falls back to a CLI backend without the response tool, it now receives explicit guidance to stay silent when nothing needs attention. That fallback still depends on the model following the instructions. Accepted alerts and private monitor notes also survive retries and compaction, while stopping or superseding a check suppresses its delivery.

> Use an updated, loaded adapter with support for the scheduled action. Older jobs missing creator or requester information need fresh authenticated authorization or recreation. Changes to executable behavior, such as a prompt, model or schedule, can clear prior requester or local-read authority and stop further affected actions; an edit already accepted by Discord can still return its confirmed result. Reauthorize from the owning Discord conversation or, for local-read authority, a fresh authenticated local session. Remote management alone cannot grant local-read authority. The scheduled payload guide explains the required complete tool allowance and recovery paths.

> Experimental Claw packages now preserve explicit model preferences and delegation settings. With a local Gateway running, add and update can activate up to 64 required plugins together after the usual trust and capability confirmations. Missing models and companion agents still need to be configured separately.

> After a restart, eligible unfinished conversations can continue from saved tool work without repeating your original message or discarding its results. Eligible tasks in the built-in runtime can also keep working when their tools have finished but the model times out, or when a known Responses output limit interrupts a tool call. Cancellation, pending approvals, unfinished tool work, and retry limits still apply. Messages arriving too late to join the current answer get their own follow-up reply. ACP background tasks that finish before cancellation takes effect keep their completed result and end time.

> When prompted, recover interrupted work before sending new input, and check uncertain tool outcomes before repeating an action. New messages can wait as follow-ups while recovery handles the earlier task. Acknowledged worker cleanup failures now block automatic model fallback from repeating completed actions. Cleanup does not undo earlier desktop input, so inspect the desktop and workspace before retrying.

> QA runtime reports keep skipped executions distinct from passing ones while preserving their existing acceptance rules. Maintainers can also compare clean built revisions with six opt-in Code Mode workloads. These require an OpenAI API key and explicit model selection, make paid calls, and assess task results separately from follow-up explanations.

Source: https://docs.openclaw.ai/releases/2026.9.5
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-09-19-20-context-window-changes-in-v2026-9-5|20 Context Window changes in v2026.9.5]] · Context Window
- [[Changes/OpenClaw/2026-09-19-14-collaboration-changes-in-v2026-9-5|14 Collaboration changes in v2026.9.5]] · Collaboration
- [[Changes/OpenClaw/2026-09-19-the-browser-sidebar-gains-a-download-file-button-for-the-image-video-or-document|The Browser sidebar gains a Download file button for the image, video, or document…]] · Multimodal Input
- [[Changes/OpenClaw/2026-09-19-29-developer-workflow-changes-in-v2026-9-5|29 Developer Workflow changes in v2026.9.5]] · Developer Workflow
- [[Changes/OpenClaw/2026-09-19-5-reliability-and-performance-changes-in-v2026-9-5|5 Reliability and Performance changes in v2026.9.5]] · Reliability and Performance
- [[Changes/OpenClaw/2026-09-19-retained-conversation-history-continues-to-follow-current-sharing-permissions-af|Retained conversation history continues to follow current sharing permissions after…]] · Projects and Workspaces
- [[Changes/OpenClaw/2026-09-19-2-enterprise-and-administration-changes-in-v2026-9-5|2 Enterprise and Administration changes in v2026.9.5]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-09-19-72-agent-mode-changes-in-v2026-9-5|72 Agent Mode changes in v2026.9.5]] · Agent Mode
- [[Changes/OpenClaw/2026-09-19-21-editor-experience-changes-in-v2026-9-5|21 Editor Experience changes in v2026.9.5]] · Editor Experience
- [[Changes/OpenClaw/2026-09-19-39-safety-and-privacy-changes-in-v2026-9-5|39 Safety and Privacy changes in v2026.9.5]] · Safety and Privacy
- [[Changes/OpenClaw/2026-09-19-14-automation-and-scheduling-changes-in-v2026-9-5|14 Automation and Scheduling changes in v2026.9.5]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-09-19-32-interface-experience-changes-in-v2026-9-5|32 Interface Experience changes in v2026.9.5]] · Interface Experience
- [[Changes/OpenClaw/2026-09-19-you-can-now-set-the-approval-reviewer-s-reasoning-and-optional-fast-mode-indepen|Set the approval reviewer's reasoning and optional Fast mode independently…]] · Agent Mode
- [[Changes/OpenClaw/2026-09-19-you-can-now-install-the-cli-on-freebsd-with-install-cli-sh-using-system-node-and|Install the CLI on FreeBSD with install-cli.sh using system Node and npm]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-09-19-6-pricing-model-changes-in-v2026-9-5|6 Pricing Model changes in v2026.9.5]] · Pricing Model
- [[Changes/OpenClaw/2026-09-19-28-account-and-access-changes-in-v2026-9-5|28 Account and Access changes in v2026.9.5]] · Account and Access
- [[Changes/OpenClaw/2026-09-19-31-memory-and-personalization-changes-in-v2026-9-5|31 Memory and Personalization changes in v2026.9.5]] · Memory and Personalization
- [[Changes/OpenClaw/2026-09-19-you-can-now-ask-btw-side-questions-about-photos-attached-to-the-current-message|Ask /btw side questions about photos attached to the current message when using…]] · Apps and Integrations
- [[Changes/OpenClaw/2026-09-19-52-apps-and-integrations-changes-in-v2026-9-5|52 Apps and Integrations changes in v2026.9.5]] · Apps and Integrations
- [[Changes/OpenClaw/2026-09-19-23-mobile-and-desktop-changes-in-v2026-9-5|23 Mobile and Desktop changes in v2026.9.5]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-09-19-6-search-and-browsing-changes-in-v2026-9-5|6 Search and Browsing changes in v2026.9.5]] · Search and Browsing
- [[Changes/OpenClaw/2026-09-19-video-generation-preserves-repeated-reference-positions-so-the-same-image-can-se|Video generation preserves repeated reference positions, so the same image can serve…]] · Music Generation
- [[Changes/OpenClaw/2026-09-19-browser-pages-appear-directly-in-the-chat-panel-header-leaving-more-room-for-the|Browser pages appear directly in the Chat panel header, leaving more room for the page]] · Accessibility and Localization
- [[Changes/OpenClaw/2026-09-19-7-files-and-data-changes-in-v2026-9-5|7 Files and Data changes in v2026.9.5]] · Files and Data
- [[Changes/OpenClaw/2026-09-19-15-voice-and-audio-changes-in-v2026-9-5|15 Voice and Audio changes in v2026.9.5]] · Voice and Audio
- [[Changes/OpenClaw/2026-09-19-shared-helpers-consolidate-repeated-implementation-including-preparation-and-res|Shared helpers consolidate repeated implementation, including preparation…]] · Video Generation
- [[Changes/OpenClaw/2026-09-19-171-other-changes-in-v2026-9-5|171 other changes in v2026.9.5]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-09-19 · Ollama · [[Changes/Ollama/2026-09-19-2-model-support-changes-in-v0-34-3|2 Model Support changes in v0.34.3]]
- Later: 2026-09-21 · ElevenLabs · [[Changes/ElevenLabs/2026-09-21-text-to-speech-576ca6|Text to Speech]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-19-3aed71&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-19-28-model-support-changes-in-v2026-9-5.md%0ACard%20ID%3A%20openclaw-2026-09-19-3aed71%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.5%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->