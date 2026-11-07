---
card_id: openclaw-2026-10-10-4f8692
date: '2026-10-10'
description: 'OpenClaw · 2026-10-10 · Safety and Privacy: 20 changes in v2026.10.1
  — Searching instruction text follows the agent''s current read permission and may
  cover…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke
    Application Access]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2265
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 0c6a86025661bb4afc39701f8024d6722006eb547dfb02110de656ed8d1f18bb
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-10-10-4f8692
  comparison: ''
  date: '2026-10-10'
  description: 'OpenClaw — v2026.10.1: 20 Safety and Privacy changes'
  evidence:
  - quote: Searching instruction text follows the agent's current read permission
      and may cover only part of a file, so no match does not mean no suitable skill
      exists. The agent reads a selected skill's full instructions separately; that
      read grants no permission to install or run it.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Chat file links open from the sending conversation's workspace, and supported
      HTML previews can load nearby images, media, styles and scripts, including in
      unsaved drafts. Outside-workspace previews need the agent's current authorization
      and stay read-only within account and sandbox restrictions. Local fonts, CSS
      imports and attachments without a session folder remain unsupported.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Plugin overviews put the README beneath capabilities and let you expand
      published MCP setup, authentication and permission information. Missing or withheld
      details are labeled, and this setup information does not indicate that an account
      is connected.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: In-place writes disable btrfs checksums and compression for these files.
      Before converting, stop the Gateway and other database users, keep verified
      backups and follow the tool and space requirements in SQLite maintenance . Conversion
      does not preserve all extended attributes or security labels; check required
      metadata before replacing a store.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: You can browse supported plugin conversations beside OpenClaw conversations
      in the selected-agent Mac view, organized by project, person or owner. Visibility
      is saved for each Gateway profile, and sending the first message brings the
      source conversation into OpenClaw. Source deletion requires support, write or
      administrator permission, and confirmation that another runner is not using
      it.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: You can put eligible root conversations aside until later with Snooze on
      iOS, Android and the experimental native Mac sidebar, then find them in Snoozed
      or wake them early. Work continues while they are hidden, and incoming messages
      or completed runs can wake them. Pinning or archiving clears snooze; protected,
      child and archived conversations are excluded, and changes require write permission.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Mac automation can open chat or Dashboard windows behind the app you are
      using with --no-activate . LaunchServices callers also need open -g -n . If
      an action needs a permission prompt, file selection, interactive Keychain access
      or external navigation, relaunch normally and retry it. See the launch and debugging
      guide .
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Plugins can bring a conversation beside their page, including drafts, attachments
      and removable page context, or open their registered side panel beside the conversation
      that requested it. This requires the plugin to adopt the Control UI host capabilities
      on a supported host; opening a panel through a tool needs operator.write permission.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: 'On a supported host, plugins can open their own registered side panel
      beside the requesting conversation with operator.write permission. #163428 .
      Thanks @jalehman .'
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Administrators can let an agent use its managed GitHub identity while working
      inside a supported Docker or Podman sandbox. The per-agent opt-in defaults to
      off and requires suitable nonshared isolation, GitHub tools and authentication,
      and permitted network access. Recreate the container when mounts change.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Opting in exposes the full selected profile credentials to sandbox code
      and background processes, including refreshed credentials. A read-only mount
      still permits credential use, and opting out does not revoke credentials already
      held by running processes.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: 'The default-off per-agent GitHub opt-in supports built-in Docker and Podman
      backends. Missing or insecure managed credentials refuse execution, and security
      audit reports each opted-in agent. #163784 . Thanks @steipete .'
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Installing an invalid skill no longer replaces a working copy, even with
      a forced local or Git install. Sandbox skill copies can refresh from read-only
      installations on POSIX systems, with affected copies repaired on the next full
      sync. SDK sessions also recover nested skills mistakenly hidden by root-only
      ignore rules.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Canceled Mac and iOS recordings stay canceled when microphone permission
      arrives late, and Android dictation keeps listening after an older attempt ends.
      Mac push-to-talk finishes on right-Option release, sometimes waiting briefly
      for final speech results; cancellation sends nothing. Voice fixes also preserve
      iOS stereo audio, repeated Voice Wake commands and opening words in Apple realtime
      playback through ordinary bursts and brief microphone delays. iOS Talk keeps
      voice directives out of later speech segments, and retired health checks stop
      reporting stale failures.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Update pre-July-2026 Gateways before relying on retired native-app connection
      fallbacks. Apple and Android retries with a saved device token now require explicit
      Gateway permission, and Android stops accepting older incoming field aliases.
      Apple apps also stop importing selected settings and certificate trust from
      before July 1, 2026, so older-only setups may need to reconnect and establish
      trust again. iOS and its share extension now use openclaw-ios ; old client identity
      overrides and app-local Talk keys are retired, with local Talk using Gateway-configured
      keys.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Codex avoids repeated history preparation, defers unused catalogs and servers,
      and fixes the fleet configuration-copy path that exhausted memory. Failed commands
      and supported simple Code Mode actions retain saved outcomes; sandbox listings
      and copies preserve tabs and line breaks in filenames. Missed file notifications
      can still leave listings stale until restart. Older schema-1 sidecar bindings
      stay available for diagnosis but are no longer imported or converted.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Codex startup diagnostics identify the stage reached, launcher and pending
      requests, while known process-wide log notices stop repeating in chats. A managed
      launcher failure needs installation repair and a Gateway restart to retry. After
      updating, run standalone Doctor to diagnose sandbox loopback restrictions in
      affected local Linux Docker or Podman runtimes; it does not make blocked shell
      commands succeed.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Browser inspection shows the registered tool, and sandbox reservation and
      cleanup work moves into the background while keeping its order. Old unconfigured
      browser/clawd directories now stay on disk instead of being offered for Doctor
      archival; configured profiles remain supported.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: 'Standalone SDK sandbox preparation refuses shared state owned by a live
      or unverified runtime. Use the owning runtime, or stop it through the service
      owner and wait for embedded activity before retrying offline. #164203 . Thanks
      @steipete .'
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Credential saves preserve a paired host's launch reply. Linux cleanup no
      longer mistakes the covered exited tasks for running ones; permission errors
      remain inconclusive. Saved workspace-recovery errors retain the readable process
      diagnostics shown on screen.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 20-safety-and-privacy-changes-in-v2026-10-1
  source_release: openclaw-2026-10-10-v2026-10-1-d64e4e93
  source_type: openclaw_changelog
  theme: safety-privacy
  title: 20 Safety and Privacy changes in v2026.10.1
  type: change
related_changes:
- '[[Changes/Claude Code/2026-10-09-4-safety-and-privacy-changes-in-v2-1-296|4 Safety
  and Privacy changes in v2.1.296]]'
- '[[Changes/GitHub Copilot CLI/2026-10-09-copilot-config-supports-sandbox-credential-injecthosts-keys-with-key-completion|copilot
  config supports sandbox credential injectHosts keys, with key completion…]]'
- '[[Changes/Open WebUI/2026-10-10-6-safety-and-privacy-changes-in-v0-12-0|6 Safety
  and Privacy changes in v0.12.0]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-10-10-v2026-10-1-d64e4e93|openclaw-2026-10-10-v2026-10-1-d64e4e93]]'
source_type: openclaw_changelog
theme: safety-privacy
title: 20 Safety and Privacy changes in v2026.10.1
type: change
---

<!-- chronolog:begin region="header" -->
# 20 Safety and Privacy changes in v2026.10.1

**OpenClaw** · 2026-10-10 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.10.1) · from [[Releases/OpenClaw/openclaw-2026-10-10-v2026-10-1-d64e4e93|v2026.10.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Searching instruction text follows the agent's current read permission and may cover only part of a file, so no match does not mean no suitable skill exists. The agent reads a selected skill's full instructions separately; that read grants no permission to install or run it.

> Chat file links open from the sending conversation's workspace, and supported HTML previews can load nearby images, media, styles and scripts, including in unsaved drafts. Outside-workspace previews need the agent's current authorization and stay read-only within account and sandbox restrictions. Local fonts, CSS imports and attachments without a session folder remain unsupported.

> Plugin overviews put the README beneath capabilities and let you expand published MCP setup, authentication and permission information. Missing or withheld details are labeled, and this setup information does not indicate that an account is connected.

> In-place writes disable btrfs checksums and compression for these files. Before converting, stop the Gateway and other database users, keep verified backups and follow the tool and space requirements in SQLite maintenance . Conversion does not preserve all extended attributes or security labels; check required metadata before replacing a store.

> You can browse supported plugin conversations beside OpenClaw conversations in the selected-agent Mac view, organized by project, person or owner. Visibility is saved for each Gateway profile, and sending the first message brings the source conversation into OpenClaw. Source deletion requires support, write or administrator permission, and confirmation that another runner is not using it.

> You can put eligible root conversations aside until later with Snooze on iOS, Android and the experimental native Mac sidebar, then find them in Snoozed or wake them early. Work continues while they are hidden, and incoming messages or completed runs can wake them. Pinning or archiving clears snooze; protected, child and archived conversations are excluded, and changes require write permission.

> Mac automation can open chat or Dashboard windows behind the app you are using with --no-activate . LaunchServices callers also need open -g -n . If an action needs a permission prompt, file selection, interactive Keychain access or external navigation, relaunch normally and retry it. See the launch and debugging guide .

> Plugins can bring a conversation beside their page, including drafts, attachments and removable page context, or open their registered side panel beside the conversation that requested it. This requires the plugin to adopt the Control UI host capabilities on a supported host; opening a panel through a tool needs operator.write permission.

> On a supported host, plugins can open their own registered side panel beside the requesting conversation with operator.write permission. #163428 . Thanks @jalehman .

> Administrators can let an agent use its managed GitHub identity while working inside a supported Docker or Podman sandbox. The per-agent opt-in defaults to off and requires suitable nonshared isolation, GitHub tools and authentication, and permitted network access. Recreate the container when mounts change.

> Opting in exposes the full selected profile credentials to sandbox code and background processes, including refreshed credentials. A read-only mount still permits credential use, and opting out does not revoke credentials already held by running processes.

> The default-off per-agent GitHub opt-in supports built-in Docker and Podman backends. Missing or insecure managed credentials refuse execution, and security audit reports each opted-in agent. #163784 . Thanks @steipete .

> Installing an invalid skill no longer replaces a working copy, even with a forced local or Git install. Sandbox skill copies can refresh from read-only installations on POSIX systems, with affected copies repaired on the next full sync. SDK sessions also recover nested skills mistakenly hidden by root-only ignore rules.

> Canceled Mac and iOS recordings stay canceled when microphone permission arrives late, and Android dictation keeps listening after an older attempt ends. Mac push-to-talk finishes on right-Option release, sometimes waiting briefly for final speech results; cancellation sends nothing. Voice fixes also preserve iOS stereo audio, repeated Voice Wake commands and opening words in Apple realtime playback through ordinary bursts and brief microphone delays. iOS Talk keeps voice directives out of later speech segments, and retired health checks stop reporting stale failures.

> Update pre-July-2026 Gateways before relying on retired native-app connection fallbacks. Apple and Android retries with a saved device token now require explicit Gateway permission, and Android stops accepting older incoming field aliases. Apple apps also stop importing selected settings and certificate trust from before July 1, 2026, so older-only setups may need to reconnect and establish trust again. iOS and its share extension now use openclaw-ios ; old client identity overrides and app-local Talk keys are retired, with local Talk using Gateway-configured keys.

> Codex avoids repeated history preparation, defers unused catalogs and servers, and fixes the fleet configuration-copy path that exhausted memory. Failed commands and supported simple Code Mode actions retain saved outcomes; sandbox listings and copies preserve tabs and line breaks in filenames. Missed file notifications can still leave listings stale until restart. Older schema-1 sidecar bindings stay available for diagnosis but are no longer imported or converted.

> Codex startup diagnostics identify the stage reached, launcher and pending requests, while known process-wide log notices stop repeating in chats. A managed launcher failure needs installation repair and a Gateway restart to retry. After updating, run standalone Doctor to diagnose sandbox loopback restrictions in affected local Linux Docker or Podman runtimes; it does not make blocked shell commands succeed.

> Browser inspection shows the registered tool, and sandbox reservation and cleanup work moves into the background while keeping its order. Old unconfigured browser/clawd directories now stay on disk instead of being offered for Doctor archival; configured profiles remain supported.

> Standalone SDK sandbox preparation refuses shared state owned by a live or unverified runtime. Use the owning runtime, or stop it through the service owner and wait for embedded activity before retrying offline. #164203 . Thanks @steipete .

> Credential saves preserve a paired host's launch reply. Linux cleanup no longer mistakes the covered exited tasks for running ones; permission errors remain inconclusive. Saved workspace-recovery errors retain the readable process diagnostics shown on screen.

Source: https://docs.openclaw.ai/releases/2026.10.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-10-10-2-reliability-and-performance-changes-in-v2026-10-1|2 Reliability and Performance changes in v2026.10.1]] · Reliability and Performance
- [[Changes/OpenClaw/2026-10-10-13-memory-and-personalization-changes-in-v2026-10-1|13 Memory and Personalization changes in v2026.10.1]] · Memory and Personalization
- [[Changes/OpenClaw/2026-10-10-96-apps-and-integrations-changes-in-v2026-10-1|96 Apps and Integrations changes in v2026.10.1]] · Apps and Integrations
- [[Changes/OpenClaw/2026-10-10-15-mobile-and-desktop-changes-in-v2026-10-1|15 Mobile and Desktop changes in v2026.10.1]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-10-10-12-context-window-changes-in-v2026-10-1|12 Context Window changes in v2026.10.1]] · Context Window
- [[Changes/OpenClaw/2026-10-10-4-pricing-model-changes-in-v2026-10-1|4 Pricing Model changes in v2026.10.1]] · Pricing Model
- [[Changes/OpenClaw/2026-10-10-18-account-and-access-changes-in-v2026-10-1|18 Account and Access changes in v2026.10.1]] · Account and Access
- [[Changes/OpenClaw/2026-10-10-18-model-support-changes-in-v2026-10-1|18 Model Support changes in v2026.10.1]] · Model Support
- [[Changes/OpenClaw/2026-10-10-3-search-and-browsing-changes-in-v2026-10-1|3 Search and Browsing changes in v2026.10.1]] · Search and Browsing
- [[Changes/OpenClaw/2026-10-10-plugin-authors-can-await-session-history-extension-changes-and-replay-metadata-t|Plugin authors can await session history, extension changes and replay metadata]] · Projects and Workspaces
- [[Changes/OpenClaw/2026-10-10-2-accessibility-and-localization-changes-in-v2026-10-1|2 Accessibility and Localization changes in v2026.10.1]] · Accessibility and Localization
- [[Changes/OpenClaw/2026-10-10-image-generation-with-oauth-can-retry-using-a-supported-openai-chat-model-in-age|Image generation with OAuth can retry using a supported OpenAI chat model…]] · Image Generation
- [[Changes/OpenClaw/2026-10-10-10-editor-experience-changes-in-v2026-10-1|10 Editor Experience changes in v2026.10.1]] · Editor Experience
- [[Changes/OpenClaw/2026-10-10-2-files-and-data-changes-in-v2026-10-1|2 Files and Data changes in v2026.10.1]] · Files and Data
- [[Changes/OpenClaw/2026-10-10-8-voice-and-audio-changes-in-v2026-10-1|8 Voice and Audio changes in v2026.10.1]] · Voice and Audio
- [[Changes/OpenClaw/2026-10-10-27-agent-mode-changes-in-v2026-10-1|27 Agent Mode changes in v2026.10.1]] · Agent Mode
- [[Changes/OpenClaw/2026-10-10-12-collaboration-changes-in-v2026-10-1|12 Collaboration changes in v2026.10.1]] · Collaboration
- [[Changes/OpenClaw/2026-10-10-video-previews-new-video-previews-can-download-media-before-play|Video previews: New video previews can download media before Play]] · Multimodal Input
- [[Changes/OpenClaw/2026-10-10-11-developer-workflow-changes-in-v2026-10-1|11 Developer Workflow changes in v2026.10.1]] · Developer Workflow
- [[Changes/OpenClaw/2026-10-10-5-enterprise-and-administration-changes-in-v2026-10-1|5 Enterprise and Administration changes in v2026.10.1]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-10-10-20-interface-experience-changes-in-v2026-10-1|20 Interface Experience changes in v2026.10.1]] · Interface Experience
- [[Changes/OpenClaw/2026-10-10-10-automation-and-scheduling-changes-in-v2026-10-1|10 Automation and Scheduling changes in v2026.10.1]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-10-10-112-other-changes-in-v2026-10-1|112 other changes in v2026.10.1]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-10-10 · Open WebUI · [[Changes/Open WebUI/2026-10-10-6-safety-and-privacy-changes-in-v0-12-0|6 Safety and Privacy changes in v0.12.0]]
- Later: 2026-10-12 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-10-12-3-safety-and-privacy-changes-in-v1-0-96|3 Safety and Privacy changes in v1.0.96]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Descript · [[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke Application Access]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-10-10-4f8692&body=Card%3A%20Changes%2FOpenClaw%2F2026-10-10-20-safety-and-privacy-changes-in-v2026-10-1.md%0ACard%20ID%3A%20openclaw-2026-10-10-4f8692%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.10.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->