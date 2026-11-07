---
card_id: openclaw-2026-07-13-b0155e
date: '2026-07-13'
description: 'OpenClaw · 2026-07-13 · Pricing Model: 18 changes in v2026.7.1 — Control
  UI Usage can now show Anthropic and OpenAI daily spend, tokens, requests, top models…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2022-12-15-daily-limit-to-ensure-a-high-quality-experience-for-all-chatgpt-users-we-are-exp|Daily
    limit: To ensure a high-quality experience for all ChatGPT users, we…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1306
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: pricing-model
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 679482a2d9cd9db8407e2608e4d00e545b0b0ddcfdb895e36b11a3afb51f8aee
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-07-13-b0155e
  comparison: ''
  date: '2026-07-13'
  description: 'OpenClaw — v2026.7.1: 18 Pricing Model changes'
  evidence:
  - quote: 'Control UI Usage can now show Anthropic and OpenAI daily spend, tokens,
      requests, top models, and billing categories for today, seven days, and thirty
      days when admin credentials are configured. #100672'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Daily token and cost charts now include zero-activity days across bounded
      date ranges, so 7-day, 30-day, and 90-day views show the full calendar period
      instead of shrinking around active days. #81467 Thanks @adapepper.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'The Control UI context panel now shows the latest run''s estimated total
      cost and available input, output, cache-read, and cache-write breakdowns beside
      the provider and model. #100379'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Completed Control UI messages now use the timestamp to open token, cache,
      context, cost, and model details instead of adding a separate Context control
      to every footer. #100391 Thanks @steipete-oai.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'The native macOS chat window now provides a full session sidebar, real
      new-session creation, slash-command completion, context and cost visibility,
      message copying, transcript export, and compact or clear-history actions. #101103'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Telegram replies and forwards now preserve visible text from rich details,
      lists, math, captions, and credits so the agent receives the context users actually
      saw. #100570 Thanks @veda-openclaw, @wangwllu.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Long, tool-heavy or media-heavy embedded-agent conversations now retain
      more prompt-cache reuse between turns, reducing repeated token processing, latency,
      and cost on prefix-cached providers. #102610 Thanks @ugiezzz.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Anthropic OAuth subscription requests now carry the Claude Code-style billing
      identity, helping them use the intended subscription route instead of failing
      or being treated as the wrong request type. 709be93 Thanks @vincentkoc.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'OpenRouter completions that the provider bills at $0 now stay recorded
      as free in transcripts, summaries, logs, and usage totals instead of being replaced
      with estimated catalog pricing. #101177'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: '/export-session now warns when a CLI- or ACP-backed export contains only
      user messages and points users to the backend transcript for missing assistant,
      tool, usage, and cost details. #90867 Thanks @tank-x3, @vincentkoc, @xydigit-sj.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Transient transcript read failures no longer destabilize session-log diagnostics
      or let an incomplete usage scan overwrite the last complete cost cache as though
      it were current. #101062 Thanks @cxbasdev, @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Embedded openclaw agent --local runs using OpenAI-compatible providers
      now report and save streamed token usage instead of showing zero, improving
      session, context, cost, and monitoring records. #96523 Thanks @ly85206559, @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Session cost summaries now estimate a real charge when a transcript records
      zero dollars despite token use and known model pricing. c5260a3 Thanks @nianjiuzst.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Large session histories now produce smaller .usage-cost-cache.json files
      with less parsing and rewrite work, rebuilding automatically after upgrade.
      #99714 Related #99511 . Thanks @dexhunter, @wayne524.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'usage.cost and sessions.usage now reject a start date later than the end
      date with a clear INVALID_REQUEST instead of returning a misleading empty report.
      #94096 Thanks @alix-007.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'A malformed transcript timestamp no longer corrupts session usage and
      cost records with invalid values. #99420 Thanks @krissding.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'OpenClaw''s Anthropic and Claude CLI documentation now reflects the current
      subscription-limit treatment for claude -p and related usage, with official
      references for billing and deployment decisions. #96848 Thanks @fightingsleep,
      @tirion-p.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Preserved token and cost totals when oversized exported run records are
      trimmed. #96811 Thanks @aleps001, @joshavant, @lin-hongkuan.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 18-pricing-model-changes-in-v2026-7-1
  source_release: openclaw-2026-07-13-v2026-7-1-c2063718
  source_type: openclaw_changelog
  theme: pricing-model
  title: 18 Pricing Model changes in v2026.7.1
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-07-09-usage-limit-reset-credits-now-show-their-type-and-expiration-and-let-you-choose|Usage-limit
  reset credits now show their type and expiration, and let you choose…]]'
- '[[Changes/OpenCode/2026-07-09-core-prevent-crashes-and-bad-pricing-data-when-github-copilot-returns-models-wit|Core
  Prevent crashes and bad pricing data when GitHub Copilot returns models…]]'
- '[[Changes/Lovable/2026-07-13-functions-usage-is-now-labeled-compute|Functions usage
  is now labeled Compute]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-07-13-v2026-7-1-c2063718|openclaw-2026-07-13-v2026-7-1-c2063718]]'
source_type: openclaw_changelog
theme: pricing-model
title: 18 Pricing Model changes in v2026.7.1
type: change
---

<!-- chronolog:begin region="header" -->
# 18 Pricing Model changes in v2026.7.1

**OpenClaw** · 2026-07-13 · [[Themes/pricing-model|Pricing Model]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.7.1) · from [[Releases/OpenClaw/openclaw-2026-07-13-v2026-7-1-c2063718|v2026.7.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Control UI Usage can now show Anthropic and OpenAI daily spend, tokens, requests, top models, and billing categories for today, seven days, and thirty days when admin credentials are configured. #100672

> Daily token and cost charts now include zero-activity days across bounded date ranges, so 7-day, 30-day, and 90-day views show the full calendar period instead of shrinking around active days. #81467 Thanks @adapepper.

> The Control UI context panel now shows the latest run's estimated total cost and available input, output, cache-read, and cache-write breakdowns beside the provider and model. #100379

> Completed Control UI messages now use the timestamp to open token, cache, context, cost, and model details instead of adding a separate Context control to every footer. #100391 Thanks @steipete-oai.

> The native macOS chat window now provides a full session sidebar, real new-session creation, slash-command completion, context and cost visibility, message copying, transcript export, and compact or clear-history actions. #101103

> Telegram replies and forwards now preserve visible text from rich details, lists, math, captions, and credits so the agent receives the context users actually saw. #100570 Thanks @veda-openclaw, @wangwllu.

> Long, tool-heavy or media-heavy embedded-agent conversations now retain more prompt-cache reuse between turns, reducing repeated token processing, latency, and cost on prefix-cached providers. #102610 Thanks @ugiezzz.

> Anthropic OAuth subscription requests now carry the Claude Code-style billing identity, helping them use the intended subscription route instead of failing or being treated as the wrong request type. 709be93 Thanks @vincentkoc.

> OpenRouter completions that the provider bills at $0 now stay recorded as free in transcripts, summaries, logs, and usage totals instead of being replaced with estimated catalog pricing. #101177

> /export-session now warns when a CLI- or ACP-backed export contains only user messages and points users to the backend transcript for missing assistant, tool, usage, and cost details. #90867 Thanks @tank-x3, @vincentkoc, @xydigit-sj.

> Transient transcript read failures no longer destabilize session-log diagnostics or let an incomplete usage scan overwrite the last complete cost cache as though it were current. #101062 Thanks @cxbasdev, @vincentkoc.

> Embedded openclaw agent --local runs using OpenAI-compatible providers now report and save streamed token usage instead of showing zero, improving session, context, cost, and monitoring records. #96523 Thanks @ly85206559, @vincentkoc.

> Session cost summaries now estimate a real charge when a transcript records zero dollars despite token use and known model pricing. c5260a3 Thanks @nianjiuzst.

> Large session histories now produce smaller .usage-cost-cache.json files with less parsing and rewrite work, rebuilding automatically after upgrade. #99714 Related #99511 . Thanks @dexhunter, @wayne524.

> usage.cost and sessions.usage now reject a start date later than the end date with a clear INVALID_REQUEST instead of returning a misleading empty report. #94096 Thanks @alix-007.

> A malformed transcript timestamp no longer corrupts session usage and cost records with invalid values. #99420 Thanks @krissding.

> OpenClaw's Anthropic and Claude CLI documentation now reflects the current subscription-limit treatment for claude -p and related usage, with official references for billing and deployment decisions. #96848 Thanks @fightingsleep, @tirion-p.

> Preserved token and cost totals when oversized exported run records are trimmed. #96811 Thanks @aleps001, @joshavant, @lin-hongkuan.

Source: https://docs.openclaw.ai/releases/2026.7.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-07-13-5-projects-and-workspaces-changes-in-v2026-7-1|5 Projects and Workspaces changes in v2026.7.1]] · Projects and Workspaces
- [[Changes/OpenClaw/2026-07-13-99-developer-workflow-changes-in-v2026-7-1|99 Developer Workflow changes in v2026.7.1]] · Developer Workflow
- [[Changes/OpenClaw/2026-07-13-69-context-window-changes-in-v2026-7-1|69 Context Window changes in v2026.7.1]] · Context Window
- [[Changes/OpenClaw/2026-07-13-10-accessibility-and-localization-changes-in-v2026-7-1|10 Accessibility and Localization changes in v2026.7.1]] · Accessibility and Localization
- [[Changes/OpenClaw/2026-07-13-64-interface-experience-changes-in-v2026-7-1|64 Interface Experience changes in v2026.7.1]] · Interface Experience
- [[Changes/OpenClaw/2026-07-13-whatsapp-and-telegram-default-account-routing-warnings-are-now-available-through|WhatsApp and Telegram default-account routing warnings are now available through…]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-07-13-132-agent-mode-changes-in-v2026-7-1|132 Agent Mode changes in v2026.7.1]] · Agent Mode
- [[Changes/OpenClaw/2026-07-13-after-one-generated-video-clip-is-ready-a-different-next-clip-can-start-immediat|After one generated video clip is ready, a different next clip can start immediately…]] · Video Generation
- [[Changes/OpenClaw/2026-07-13-79-automation-and-scheduling-changes-in-v2026-7-1|79 Automation and Scheduling changes in v2026.7.1]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-07-13-130-model-support-changes-in-v2026-7-1|130 Model Support changes in v2026.7.1]] · Model Support
- [[Changes/OpenClaw/2026-07-13-69-account-and-access-changes-in-v2026-7-1|69 Account and Access changes in v2026.7.1]] · Account and Access
- [[Changes/OpenClaw/2026-07-13-59-safety-and-privacy-changes-in-v2026-7-1|59 Safety and Privacy changes in v2026.7.1]] · Safety and Privacy
- [[Changes/OpenClaw/2026-07-13-224-mobile-and-desktop-changes-in-v2026-7-1|224 Mobile and Desktop changes in v2026.7.1]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-07-13-83-voice-and-audio-changes-in-v2026-7-1|83 Voice and Audio changes in v2026.7.1]] · Voice and Audio
- [[Changes/OpenClaw/2026-07-13-21-editor-experience-changes-in-v2026-7-1|21 Editor Experience changes in v2026.7.1]] · Editor Experience
- [[Changes/OpenClaw/2026-07-13-7-image-generation-changes-in-v2026-7-1|7 Image Generation changes in v2026.7.1]] · Image Generation
- [[Changes/OpenClaw/2026-07-13-channel-setup-warnings-are-now-available-as-structured-doctor-lint-findings-with|Channel setup warnings are now available as structured Doctor lint findings…]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-07-13-4-enterprise-and-administration-changes-in-v2026-7-1|4 Enterprise and Administration changes in v2026.7.1]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-07-13-2-presentation-creation-changes-in-v2026-7-1|2 Presentation Creation changes in v2026.7.1]] · Presentation Creation
- [[Changes/OpenClaw/2026-07-13-136-memory-and-personalization-changes-in-v2026-7-1|136 Memory and Personalization changes in v2026.7.1]] · Memory and Personalization
- [[Changes/OpenClaw/2026-07-13-213-apps-and-integrations-changes-in-v2026-7-1|213 Apps and Integrations changes in v2026.7.1]] · Apps and Integrations
- [[Changes/OpenClaw/2026-07-13-8-search-and-browsing-changes-in-v2026-7-1|8 Search and Browsing changes in v2026.7.1]] · Search and Browsing
- [[Changes/OpenClaw/2026-07-13-20-collaboration-changes-in-v2026-7-1|20 Collaboration changes in v2026.7.1]] · Collaboration
- [[Changes/OpenClaw/2026-07-13-13-files-and-data-changes-in-v2026-7-1|13 Files and Data changes in v2026.7.1]] · Files and Data
- [[Changes/OpenClaw/2026-07-13-19-multimodal-input-changes-in-v2026-7-1|19 Multimodal Input changes in v2026.7.1]] · Multimodal Input
- [[Changes/OpenClaw/2026-07-13-38-reliability-and-performance-changes-in-v2026-7-1|38 Reliability and Performance changes in v2026.7.1]] · Reliability and Performance
- [[Changes/OpenClaw/2026-07-13-686-other-changes-in-v2026-7-1|686 other changes in v2026.7.1]] · Other changes
- [[Changes/OpenClaw/2026-07-13-official-openclaw-container-images-are-now-available-from-docker-hub-as-well-as|Official OpenClaw container images are now available from Docker Hub as well…]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Pricing Model

- Earlier: 2026-07-13 · Lovable · [[Changes/Lovable/2026-07-13-functions-usage-is-now-labeled-compute|Functions usage is now labeled Compute]]
- Later: 2026-07-16 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-07-16-3-pricing-model-changes-in-v1-0-71|3 Pricing Model changes in v1.0.71]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2022-12-15 · ChatGPT · [[Changes/ChatGPT/2022-12-15-daily-limit-to-ensure-a-high-quality-experience-for-all-chatgpt-users-we-are-exp|Daily limit: To ensure a high-quality experience for all ChatGPT users, we…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-07-13-b0155e&body=Card%3A%20Changes%2FOpenClaw%2F2026-07-13-18-pricing-model-changes-in-v2026-7-1.md%0ACard%20ID%3A%20openclaw-2026-07-13-b0155e%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.7.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->