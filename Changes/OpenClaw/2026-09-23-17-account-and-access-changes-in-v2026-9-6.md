---
card_id: openclaw-2026-09-23-ab1d5a
date: '2026-09-23'
description: 'OpenClaw · 2026-09-23 · Account and Access: 17 changes in v2026.9.6
  — Forget this browser in Settings → Connections → Gateway → Browser resets the current…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires
    login]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1273
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: a11102805efb18c5213b1e1d33b5ec912a653ebb750bce9e43d9bed0ba5925fc
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-23-ab1d5a
  comparison: ''
  date: '2026-09-23'
  description: 'OpenClaw — v2026.9.6: 17 Account and Access changes'
  evidence:
  - quote: Forget this browser in Settings → Connections → Gateway → Browser resets
      the current Gateway's browser sign-in without clearing unrelated preferences
      or other Gateways' sign-ins. It signs out the current tab and may require signing
      in or approval again, but does not revoke server-side devices or start a stopped
      Gateway. During ordinary reconnects, chat stays usable while its session list
      loads, with clearer account identity and connection status. Send problems are
      available from Inbox → System.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Successive repairs also preserve authored environment references, literal
      values and included-file ownership, checking for intervening edits before each
      write. A later refusal keeps earlier committed repairs and backups, and removing
      redundant local OAuth copies preserves the chosen preferred and fallback account
      order.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: With live configuration reload enabled, more settings apply without restarting
      the Gateway, including Cloud Worker profiles, meeting capture, Desktop connections,
      Browser control and access policy. Successful overlapping settings and secrets
      reloads also avoid an unnecessary recovery restart. Affected services or clients
      may reconnect, existing workers keep their original provisioning settings, and
      newly enabled auditing does not fill historical gaps. Listener address or port,
      effective authentication mode and TLS topology still require a restart.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Updates, verification and rollback no longer require model credentials.
      Optional model-powered repair starts through triage only after a failed update
      has settled and released control, using normal shared or OAuth authentication
      without changing the recorded update outcome. Supported assistance recognizes
      eligible older and hybrid Linux cgroup layouts, rechecking that it still belongs
      to the right service. Triage also explains when an agent CLI is missing from
      PATH and offers a saved debugging prompt when available. Assistance does not
      itself prove recovery or authorize a restart, and PATH changes remain yours
      to make.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Login, logout, and directory commands now reject an explicitly blank --channel
      , preventing an empty shell variable from silently selecting a configured channel
      or affecting saved credentials. Omit the flag when you want automatic selection.
      Valid names, surrounding whitespace, and supported aliases keep their existing
      behavior.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Android Talk can use supported GPT-Live realtime routes advertised by the
      Gateway and shows which route is active or why device speech was selected. The
      Codex route tries ChatGPT OAuth first and can fall back to a Platform key; the
      public API route requires a Platform key. Platform-key use is billed per use,
      including fallback. An advertised route still needs valid credentials and account
      access, and changing an active route requires stopping and restarting Talk.
      Longer replies can use the existing audio buffer more fully, and a stopped session
      now shows its failure reason in chat.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: The Tauri tray menu adds an optional Keep computer awake setting beside
      Start at Login for long-running local work. It is off by default, remembers
      the choice on this device, and stays active when windows close to the tray until
      you disable it or quit. On Linux it can also delay automatic dimming and locking;
      manual lock, explicit sleep, and lid behavior remain under operating-system
      control. The native Mac app adopts the clearer name for its existing setting,
      which still requires a connected, hosting, unlocked Mac.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Android packages omit unused resource files, reducing what they carry without
      changing authentication behavior.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Model discovery can use saved credentials in custom agent directories,
      refresh eligible empty catalogs after their cache expires, and retain existing
      choices when a catalog refresh fails. Failures and Retry remain visible even
      while other providers are still loading, so you can act on the problem without
      losing a working selection. OAuth diagnostics also identify the affected agent
      and profile with the appropriate sign-in command.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Repeated model and authentication refreshes avoid whole-database copies
      and limit temporary plugin copies created by current discovery workers. Catalog
      preparation also reuses more existing work and stops recurring retirement checks
      while workers are idle. These catalog repairs take effect in newly started workers
      and now release retired catalog registrations after refreshes. Older scratch
      directories use a separate cleanup path.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: xAI device sign-in now rejects malformed token-response bytes before they
      can be saved as corrupted credentials. Successful token-refresh responses are
      also validated before replacing stored credentials, so malformed responses leave
      the old local credential intact. Provider-side token rotation can still require
      signing in again, and existing corrupted credentials are not repaired retroactively.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Supervised turns retain their local Codex configuration and login . A shared
      Codex daemon still shares its login across chats, without per-chat account isolation
      or fallback to OpenClaw credentials. Changed policy may require a reconnect
      or retry.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Cloud desktops now support native macOS and Windows profiles, with Fit
      and Actual viewing sizes. Enable the Cloud Worker Desktop lab and a desktop-enabled
      profile first. Properly prepared native desktops also support computer control
      and Browser and Terminal launchers. Native machines start cold and do not support
      remote display resizing. Mac setup needs macOS 15 or newer, Chrome, an unlocked
      worker account, passwordless sudo, and a separately signed OpenClaw Cloud Worker
      app with its own Accessibility and Screen Recording permissions. Windows needs
      its worker-account desktop active and the Crabbox desktop launcher installed.
      WSL2 desktops, Windows sign-in, and secure Windows screens remain unsupported,
      and Mac provisioning requires existing EC2 Mac Dedicated Host capacity. Live
      Mac desktop validation remains incomplete.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Administrators can now sign in to eligible MCP connectors directly from
      Settings, approve access in the browser, and return to an Authentication saved
      result. This works for enabled HTTP OAuth connectors using shared native credentials
      when you open the Gateway through its own loopback or published Tailscale address.
      Other account modes keep their existing sign-in paths, and saving credentials
      still leaves connector reachability and tool access to be checked.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Cloudflare Access OIDC sign-in can reuse an existing OpenClaw profile,
      role, and history when the verified email matches a linked alias. Cloudflare
      admission and identity-provider email verification remain required; an unmatched
      email gets a separate profile with the configured default role. Tailscale profile-picture
      adoption also moves its database work off the main Gateway thread while preserving
      a picture you have explicitly chosen.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: 'For the private, source-built Team plugin''s Visitor Access feature, invitation
      expiry or revocation now closes dependent Gateway connections and cancels affected
      active and queued work. Saved results and independent staff access remain available.
      Operators must apply the restricted Guest role''s accessPolicyPlugin: "visitor-access"
      binding as the final setup step; unavailable policy denies access, and older
      Gateways reject this field. Keep the binding and restrictions during recovery.
      The plugin remains excluded from ordinary npm packages. Failed Cloudflare policy
      cleanup still retries at startup or hourly and may leave provider access active
      until it succeeds, but it no longer extends the dependent local work. Cloudflare
      login sessions are not separately revoked, and an invitation issued after expiry
      requires fresh admission.'
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  - quote: Control UI tests control clocks, focus and viewport state and wait for
      rendered elements before checking them. Shared fixtures reduce repeated setup
      while preserving coverage for chat, navigation, sign-in and appearance.
    source_release: https://docs.openclaw.ai/releases/2026.9.6
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 17-account-and-access-changes-in-v2026-9-6
  source_release: openclaw-2026-09-23-v2026-9-6-3f12c824
  source_type: openclaw_changelog
  theme: account-access
  title: 17 Account and Access changes in v2026.9.6
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-09-22-13-account-and-access-changes-in-rust-v0-156-0|13
  Account and Access changes in rust-v0.156.0]]'
- '[[Changes/GitHub Copilot CLI/2026-09-22-3-account-and-access-changes-in-v1-0-88|3
  Account and Access changes in v1.0.88]]'
- '[[Changes/Claude Code/2026-09-23-2-account-and-access-changes-in-v2-1-281|2 Account
  and Access changes in v2.1.281]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-23-v2026-9-6-3f12c824|openclaw-2026-09-23-v2026-9-6-3f12c824]]'
source_type: openclaw_changelog
theme: account-access
title: 17 Account and Access changes in v2026.9.6
type: change
---

<!-- chronolog:begin region="header" -->
# 17 Account and Access changes in v2026.9.6

**OpenClaw** · 2026-09-23 · [[Themes/account-access|Account and Access]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.6) · from [[Releases/OpenClaw/openclaw-2026-09-23-v2026-9-6-3f12c824|v2026.9.6]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Forget this browser in Settings → Connections → Gateway → Browser resets the current Gateway's browser sign-in without clearing unrelated preferences or other Gateways' sign-ins. It signs out the current tab and may require signing in or approval again, but does not revoke server-side devices or start a stopped Gateway. During ordinary reconnects, chat stays usable while its session list loads, with clearer account identity and connection status. Send problems are available from Inbox → System.

> Successive repairs also preserve authored environment references, literal values and included-file ownership, checking for intervening edits before each write. A later refusal keeps earlier committed repairs and backups, and removing redundant local OAuth copies preserves the chosen preferred and fallback account order.

> With live configuration reload enabled, more settings apply without restarting the Gateway, including Cloud Worker profiles, meeting capture, Desktop connections, Browser control and access policy. Successful overlapping settings and secrets reloads also avoid an unnecessary recovery restart. Affected services or clients may reconnect, existing workers keep their original provisioning settings, and newly enabled auditing does not fill historical gaps. Listener address or port, effective authentication mode and TLS topology still require a restart.

> Updates, verification and rollback no longer require model credentials. Optional model-powered repair starts through triage only after a failed update has settled and released control, using normal shared or OAuth authentication without changing the recorded update outcome. Supported assistance recognizes eligible older and hybrid Linux cgroup layouts, rechecking that it still belongs to the right service. Triage also explains when an agent CLI is missing from PATH and offers a saved debugging prompt when available. Assistance does not itself prove recovery or authorize a restart, and PATH changes remain yours to make.

> Login, logout, and directory commands now reject an explicitly blank --channel , preventing an empty shell variable from silently selecting a configured channel or affecting saved credentials. Omit the flag when you want automatic selection. Valid names, surrounding whitespace, and supported aliases keep their existing behavior.

> Android Talk can use supported GPT-Live realtime routes advertised by the Gateway and shows which route is active or why device speech was selected. The Codex route tries ChatGPT OAuth first and can fall back to a Platform key; the public API route requires a Platform key. Platform-key use is billed per use, including fallback. An advertised route still needs valid credentials and account access, and changing an active route requires stopping and restarting Talk. Longer replies can use the existing audio buffer more fully, and a stopped session now shows its failure reason in chat.

> The Tauri tray menu adds an optional Keep computer awake setting beside Start at Login for long-running local work. It is off by default, remembers the choice on this device, and stays active when windows close to the tray until you disable it or quit. On Linux it can also delay automatic dimming and locking; manual lock, explicit sleep, and lid behavior remain under operating-system control. The native Mac app adopts the clearer name for its existing setting, which still requires a connected, hosting, unlocked Mac.

> Android packages omit unused resource files, reducing what they carry without changing authentication behavior.

> Model discovery can use saved credentials in custom agent directories, refresh eligible empty catalogs after their cache expires, and retain existing choices when a catalog refresh fails. Failures and Retry remain visible even while other providers are still loading, so you can act on the problem without losing a working selection. OAuth diagnostics also identify the affected agent and profile with the appropriate sign-in command.

> Repeated model and authentication refreshes avoid whole-database copies and limit temporary plugin copies created by current discovery workers. Catalog preparation also reuses more existing work and stops recurring retirement checks while workers are idle. These catalog repairs take effect in newly started workers and now release retired catalog registrations after refreshes. Older scratch directories use a separate cleanup path.

> xAI device sign-in now rejects malformed token-response bytes before they can be saved as corrupted credentials. Successful token-refresh responses are also validated before replacing stored credentials, so malformed responses leave the old local credential intact. Provider-side token rotation can still require signing in again, and existing corrupted credentials are not repaired retroactively.

> Supervised turns retain their local Codex configuration and login . A shared Codex daemon still shares its login across chats, without per-chat account isolation or fallback to OpenClaw credentials. Changed policy may require a reconnect or retry.

> Cloud desktops now support native macOS and Windows profiles, with Fit and Actual viewing sizes. Enable the Cloud Worker Desktop lab and a desktop-enabled profile first. Properly prepared native desktops also support computer control and Browser and Terminal launchers. Native machines start cold and do not support remote display resizing. Mac setup needs macOS 15 or newer, Chrome, an unlocked worker account, passwordless sudo, and a separately signed OpenClaw Cloud Worker app with its own Accessibility and Screen Recording permissions. Windows needs its worker-account desktop active and the Crabbox desktop launcher installed. WSL2 desktops, Windows sign-in, and secure Windows screens remain unsupported, and Mac provisioning requires existing EC2 Mac Dedicated Host capacity. Live Mac desktop validation remains incomplete.

> Administrators can now sign in to eligible MCP connectors directly from Settings, approve access in the browser, and return to an Authentication saved result. This works for enabled HTTP OAuth connectors using shared native credentials when you open the Gateway through its own loopback or published Tailscale address. Other account modes keep their existing sign-in paths, and saving credentials still leaves connector reachability and tool access to be checked.

> Cloudflare Access OIDC sign-in can reuse an existing OpenClaw profile, role, and history when the verified email matches a linked alias. Cloudflare admission and identity-provider email verification remain required; an unmatched email gets a separate profile with the configured default role. Tailscale profile-picture adoption also moves its database work off the main Gateway thread while preserving a picture you have explicitly chosen.

> For the private, source-built Team plugin's Visitor Access feature, invitation expiry or revocation now closes dependent Gateway connections and cancels affected active and queued work. Saved results and independent staff access remain available. Operators must apply the restricted Guest role's accessPolicyPlugin: "visitor-access" binding as the final setup step; unavailable policy denies access, and older Gateways reject this field. Keep the binding and restrictions during recovery. The plugin remains excluded from ordinary npm packages. Failed Cloudflare policy cleanup still retries at startup or hourly and may leave provider access active until it succeeds, but it no longer extends the dependent local work. Cloudflare login sessions are not separately revoked, and an invitation issued after expiry requires fresh admission.

> Control UI tests control clocks, focus and viewport state and wait for rendered elements before checking them. Shared fixtures reduce repeated setup while preserving coverage for chat, navigation, sign-in and appearance.

Source: https://docs.openclaw.ai/releases/2026.9.6
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-09-23-50-safety-and-privacy-changes-in-v2026-9-6|50 Safety and Privacy changes in v2026.9.6]] · Safety and Privacy
- [[Changes/OpenClaw/2026-09-23-localization-maintenance-removes-entries-whose-interface-text-has-already-been-r|Localization maintenance removes entries whose interface text has already been…]] · Accessibility and Localization
- [[Changes/OpenClaw/2026-09-23-5-reliability-and-performance-changes-in-v2026-9-6|5 Reliability and Performance changes in v2026.9.6]] · Reliability and Performance
- [[Changes/OpenClaw/2026-09-23-2-image-generation-changes-in-v2026-9-6|2 Image Generation changes in v2026.9.6]] · Image Generation
- [[Changes/OpenClaw/2026-09-23-18-voice-and-audio-changes-in-v2026-9-6|18 Voice and Audio changes in v2026.9.6]] · Voice and Audio
- [[Changes/OpenClaw/2026-09-23-25-context-window-changes-in-v2026-9-6|25 Context Window changes in v2026.9.6]] · Context Window
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
- [[Changes/OpenClaw/2026-09-23-background-image-video-and-music-generation-can-complete-independently-of-the-re|Background image, video, and music generation can complete independently…]] · Music Generation
- [[Changes/OpenClaw/2026-09-23-23-memory-and-personalization-changes-in-v2026-9-6|23 Memory and Personalization changes in v2026.9.6]] · Memory and Personalization
- [[Changes/OpenClaw/2026-09-23-3-search-and-browsing-changes-in-v2026-9-6|3 Search and Browsing changes in v2026.9.6]] · Search and Browsing
- [[Changes/OpenClaw/2026-09-23-19-interface-experience-changes-in-v2026-9-6|19 Interface Experience changes in v2026.9.6]] · Interface Experience
- [[Changes/OpenClaw/2026-09-23-9-automation-and-scheduling-changes-in-v2026-9-6|9 Automation and Scheduling changes in v2026.9.6]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-09-23-22-model-support-changes-in-v2026-9-6|22 Model Support changes in v2026.9.6]] · Model Support
- [[Changes/OpenClaw/2026-09-23-119-other-changes-in-v2026-9-6|119 other changes in v2026.9.6]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2026-09-23 · Claude Code · [[Changes/Claude Code/2026-09-23-2-account-and-access-changes-in-v2-1-281|2 Account and Access changes in v2.1.281]]
- Later: 2026-09-25 · Codex CLI · [[Changes/Codex CLI/2026-09-25-5-account-and-access-changes-in-rust-v0-157-0|5 Account and Access changes in rust-v0.157.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-30 · Cursor · [[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires login]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-23-ab1d5a&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-23-17-account-and-access-changes-in-v2026-9-6.md%0ACard%20ID%3A%20openclaw-2026-09-23-ab1d5a%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.6%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->