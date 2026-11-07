---
card_id: openclaw-2026-09-08-f6d1ea
date: '2026-09-08'
description: 'OpenClaw · 2026-09-08 · Account and Access: 8 changes in v2026.9.3 —
  Connection screens lead with the problem preventing sign-in and what to do next.
  Remote…'
diffusion:
  first_in_tracked: "[[Changes/Notion/2020-07-28-sign-into-notion-with-your-apple-id-the-perfect-combination-of-speedy-and-secure|Sign
    into Notion with your Apple ID \U0001F5DD️ The perfect combination of speedy and
    secure]]"
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2233
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: bd2c7250e6390ccb9448198c167e65486a00941571adc401a46fbbbc66367b21
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-08-f6d1ea
  comparison: ''
  date: '2026-09-08'
  description: 'OpenClaw — v2026.9.3: 8 Account and Access changes'
  evidence:
  - quote: Connection screens lead with the problem preventing sign-in and what to
      do next. Remote setup uses one Gateway secret field, while local setup generates
      a token by default. Provider selection keeps credentials attached to the provider
      they belong to, instead of accepting an unrelated sign-in result.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Private-session preview links remain separate. They show a generic OpenClaw
      social card without reading the conversation, and opening the session still
      requires its normal authentication. Public HTTPS proxies may need the documented
      preview routing configured.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: A signed-in operator browser with a live pending pairing request reconnects
      automatically after approval. Paused connection states retain manual guidance,
      and existing authorization requirements still apply. Bundled UI startup recovery
      preserves pending sign-in and asks before sending its credential to the captured
      destination; damaged packages receive reinstall guidance.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Eligible failed updates and repeated Linux systemd startup failures can
      start a bounded installation-owned repair with existing authentication and permissions.
      On macOS, launchd startup recovery provides diagnostics. Only one repair runs
      per installation, and uncertain cleanup can block an automatic successor while
      leaving manual diagnosis available.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Temporary rate limits and other eligible provider failures can recover
      within the same run, keeping completed tool work and attachments available and
      the recovered answer together. Retry waits remain cancellable, and a terminal
      error stays visible when recovery is exhausted. Authentication failures, billing
      problems and refusals retain their own handling, while exhausted usage windows
      can move to an eligible fallback.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Personal GitHub connection status no longer needs an agent workspace, and
      Profile links effective agent authentication to its account settings. An authenticated
      account still needs access to the repository it will use.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Documentation also distinguishes authorized, user-requested sign-in handoffs
      in private conversations from reusable secrets, warns about shared plaintext
      credentials that still need attention, and includes enabled diagnostic exports
      when explaining where data can go.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Early WebSocket errors and rejected connections are handled without leaving
      unrelated connections exposed to an unhandled failure. Prepared model runtimes
      finish closing before authentication is torn down, and supported foreground
      restart failures leave the process available for an operator to correct the
      cause and retry, serving no requests until startup succeeds.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 8-account-and-access-changes-in-v2026-9-3
  source_release: openclaw-2026-09-08-v2026-9-3-dfcfef48
  source_type: openclaw_changelog
  theme: account-access
  title: 8 Account and Access changes in v2026.9.3
  type: change
related_changes:
- '[[Changes/Lovable/2026-09-07-send-app-emails-from-tanstack-start-projects-without-cloud|Send
  app emails from TanStack Start projects without Cloud]]'
- '[[Changes/Claude Code/2026-09-08-2-account-and-access-changes-in-v2-1-265|2 Account
  and Access changes in v2.1.265]]'
- '[[Changes/Lovable/2026-09-08-lovable-signs-in-to-test-pages-behind-your-app-s-login|Lovable
  signs in to test pages behind your app''s login]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-08-v2026-9-3-dfcfef48|openclaw-2026-09-08-v2026-9-3-dfcfef48]]'
source_type: openclaw_changelog
theme: account-access
title: 8 Account and Access changes in v2026.9.3
type: change
---

<!-- chronolog:begin region="header" -->
# 8 Account and Access changes in v2026.9.3

**OpenClaw** · 2026-09-08 · [[Themes/account-access|Account and Access]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.3) · from [[Releases/OpenClaw/openclaw-2026-09-08-v2026-9-3-dfcfef48|v2026.9.3]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Connection screens lead with the problem preventing sign-in and what to do next. Remote setup uses one Gateway secret field, while local setup generates a token by default. Provider selection keeps credentials attached to the provider they belong to, instead of accepting an unrelated sign-in result.

> Private-session preview links remain separate. They show a generic OpenClaw social card without reading the conversation, and opening the session still requires its normal authentication. Public HTTPS proxies may need the documented preview routing configured.

> A signed-in operator browser with a live pending pairing request reconnects automatically after approval. Paused connection states retain manual guidance, and existing authorization requirements still apply. Bundled UI startup recovery preserves pending sign-in and asks before sending its credential to the captured destination; damaged packages receive reinstall guidance.

> Eligible failed updates and repeated Linux systemd startup failures can start a bounded installation-owned repair with existing authentication and permissions. On macOS, launchd startup recovery provides diagnostics. Only one repair runs per installation, and uncertain cleanup can block an automatic successor while leaving manual diagnosis available.

> Temporary rate limits and other eligible provider failures can recover within the same run, keeping completed tool work and attachments available and the recovered answer together. Retry waits remain cancellable, and a terminal error stays visible when recovery is exhausted. Authentication failures, billing problems and refusals retain their own handling, while exhausted usage windows can move to an eligible fallback.

> Personal GitHub connection status no longer needs an agent workspace, and Profile links effective agent authentication to its account settings. An authenticated account still needs access to the repository it will use.

> Documentation also distinguishes authorized, user-requested sign-in handoffs in private conversations from reusable secrets, warns about shared plaintext credentials that still need attention, and includes enabled diagnostic exports when explaining where data can go.

> Early WebSocket errors and rejected connections are handled without leaving unrelated connections exposed to an unhandled failure. Prepared model runtimes finish closing before authentication is torn down, and supported foreground restart failures leave the process available for an operator to correct the cause and retry, serving no requests until startup succeeds.

Source: https://docs.openclaw.ai/releases/2026.9.3
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-09-08-7-automation-and-scheduling-changes-in-v2026-9-3|7 Automation and Scheduling changes in v2026.9.3]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-09-08-10-memory-and-personalization-changes-in-v2026-9-3|10 Memory and Personalization changes in v2026.9.3]] · Memory and Personalization
- [[Changes/OpenClaw/2026-09-08-2-files-and-data-changes-in-v2026-9-3|2 Files and Data changes in v2026.9.3]] · Files and Data
- [[Changes/OpenClaw/2026-09-08-12-context-window-changes-in-v2026-9-3|12 Context Window changes in v2026.9.3]] · Context Window
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
- [[Changes/OpenClaw/2026-09-08-22-developer-workflow-changes-in-v2026-9-3|22 Developer Workflow changes in v2026.9.3]] · Developer Workflow
- [[Changes/OpenClaw/2026-09-08-77-other-changes-in-v2026-9-3|77 other changes in v2026.9.3]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2026-09-08 · Lovable · [[Changes/Lovable/2026-09-08-lovable-signs-in-to-test-pages-behind-your-app-s-login|Lovable signs in to test pages behind your app's login]]
- Later: 2026-09-09 · Codex CLI · [[Changes/Codex CLI/2026-09-09-5-account-and-access-changes-in-rust-v0-154-0|5 Account and Access changes in rust-v0.154.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Notion · [[Changes/Notion/2020-07-28-sign-into-notion-with-your-apple-id-the-perfect-combination-of-speedy-and-secure|Sign into Notion with your Apple ID 🗝️ The perfect combination of speedy and secure]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-08-f6d1ea&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-08-8-account-and-access-changes-in-v2026-9-3.md%0ACard%20ID%3A%20openclaw-2026-09-08-f6d1ea%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.3%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->