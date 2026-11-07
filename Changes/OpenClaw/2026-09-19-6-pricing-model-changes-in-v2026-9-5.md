---
card_id: openclaw-2026-09-19-6c0489
date: '2026-09-19'
description: 'OpenClaw · 2026-09-19 · Pricing Model: 6 changes in v2026.9.5 — This
  release includes 4,179 pull requests and 64 direct commits , with credits to 502…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-07-11-improved-the-design-usefulness-of-your-billing-history|Nicer
    Invoices]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2992
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: pricing-model
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 640042047bb4214e34a062f40a7fd04fe2e8034f4b76aa710d7e61c243d4be2b
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-19-6c0489
  comparison: ''
  date: '2026-09-19'
  description: 'OpenClaw — v2026.9.5: 6 Pricing Model changes'
  evidence:
  - quote: This release includes 4,179 pull requests and 64 direct commits , with
      credits to 502 contributing accounts .
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Enabled usage footers keep available totals and cache counts even when
      separate input and output counts are missing. When a session is recreated, Usage
      clears the old timeline selection so it no longer hides the new conversation’s
      messages. Hour filters also handle daylight-saving changes without freezing,
      and Models settings labels its usage-record count as messages. These display
      fixes leave billing totals unchanged.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: GPT Live reaches Talk, meetings and phone calls. Model settings make sign-ins
      and remaining Codex usage easier to manage, with fixes that preserve selected
      models and eligible subscription billing.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Eligible automatic background OpenAI work keeps using subscription billing
      when an API key is also present. An explicit choice of a metered account still
      takes precedence.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Alibaba and Qwen video requests now enforce one total timeout, including
      downloads, using the existing 120-second default. Slow jobs may need an existing
      timeout override. A local timeout does not establish that the remote job stopped
      or that billing ended.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: These settings autosave for everyone on the Gateway and require a restart;
      the relevant plugin must be enabled. Update paired nodes as well as the Gateway
      for the newer Codex discovery behavior. Fresh Claude Code and Codex discovery
      defaults off, while OpenCode and Pi defaults on. New Claude CLI conversations
      can use saved subscription tokens while existing conversations retain their
      account and history. API keys require explicit selection, and your configured
      fallback policy still applies.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 6-pricing-model-changes-in-v2026-9-5
  source_release: openclaw-2026-09-19-v2026-9-5-506f537c
  source_type: openclaw_changelog
  theme: pricing-model
  title: 6 Pricing Model changes in v2026.9.5
  type: change
related_changes:
- '[[Changes/Claude Code/2026-09-18-vscode-added-the-session-s-cost-and-token-usage-to-the-account-usage-dialog-and|VSCode
  Added the session''s cost and token usage to the Account & usage dialog…]]'
- '[[Changes/Lovable/2026-09-18-use-firecrawl-without-a-firecrawl-account|Use Firecrawl
  without a Firecrawl account]]'
- '[[Changes/Claude Code/2026-09-19-changed-auto-mode-for-claude-api-and-enterprise-users-and-on-bedrock-vertex-foun|Changed
  auto mode for Claude API and Enterprise users, and on Bedrock, Vertex…]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-19-v2026-9-5-506f537c|openclaw-2026-09-19-v2026-9-5-506f537c]]'
source_type: openclaw_changelog
theme: pricing-model
title: 6 Pricing Model changes in v2026.9.5
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Pricing Model changes in v2026.9.5

**OpenClaw** · 2026-09-19 · [[Themes/pricing-model|Pricing Model]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.5) · from [[Releases/OpenClaw/openclaw-2026-09-19-v2026-9-5-506f537c|v2026.9.5]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> This release includes 4,179 pull requests and 64 direct commits , with credits to 502 contributing accounts .

> Enabled usage footers keep available totals and cache counts even when separate input and output counts are missing. When a session is recreated, Usage clears the old timeline selection so it no longer hides the new conversation’s messages. Hour filters also handle daylight-saving changes without freezing, and Models settings labels its usage-record count as messages. These display fixes leave billing totals unchanged.

> GPT Live reaches Talk, meetings and phone calls. Model settings make sign-ins and remaining Codex usage easier to manage, with fixes that preserve selected models and eligible subscription billing.

> Eligible automatic background OpenAI work keeps using subscription billing when an API key is also present. An explicit choice of a metered account still takes precedence.

> Alibaba and Qwen video requests now enforce one total timeout, including downloads, using the existing 120-second default. Slow jobs may need an existing timeout override. A local timeout does not establish that the remote job stopped or that billing ended.

> These settings autosave for everyone on the Gateway and require a restart; the relevant plugin must be enabled. Update paired nodes as well as the Gateway for the newer Codex discovery behavior. Fresh Claude Code and Codex discovery defaults off, while OpenCode and Pi defaults on. New Claude CLI conversations can use saved subscription tokens while existing conversations retain their account and history. API keys require explicit selection, and your configured fallback policy still applies.

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
- [[Changes/OpenClaw/2026-09-19-28-model-support-changes-in-v2026-9-5|28 Model Support changes in v2026.9.5]] · Model Support
- [[Changes/OpenClaw/2026-09-19-39-safety-and-privacy-changes-in-v2026-9-5|39 Safety and Privacy changes in v2026.9.5]] · Safety and Privacy
- [[Changes/OpenClaw/2026-09-19-14-automation-and-scheduling-changes-in-v2026-9-5|14 Automation and Scheduling changes in v2026.9.5]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-09-19-32-interface-experience-changes-in-v2026-9-5|32 Interface Experience changes in v2026.9.5]] · Interface Experience
- [[Changes/OpenClaw/2026-09-19-you-can-now-set-the-approval-reviewer-s-reasoning-and-optional-fast-mode-indepen|Set the approval reviewer's reasoning and optional Fast mode independently…]] · Agent Mode
- [[Changes/OpenClaw/2026-09-19-you-can-now-install-the-cli-on-freebsd-with-install-cli-sh-using-system-node-and|Install the CLI on FreeBSD with install-cli.sh using system Node and npm]] · Enterprise and Administration
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
## Nearby in Pricing Model

- Earlier: 2026-09-19 · Claude Code · [[Changes/Claude Code/2026-09-19-changed-auto-mode-for-claude-api-and-enterprise-users-and-on-bedrock-vertex-foun|Changed auto mode for Claude API and Enterprise users, and on Bedrock, Vertex…]]
- Later: 2026-09-21 · ElevenLabs · [[Changes/ElevenLabs/2026-09-21-user|User]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-07-11 · Descript · [[Changes/Descript/2018-07-11-improved-the-design-usefulness-of-your-billing-history|Nicer Invoices]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-19-6c0489&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-19-6-pricing-model-changes-in-v2026-9-5.md%0ACard%20ID%3A%20openclaw-2026-09-19-6c0489%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.5%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->