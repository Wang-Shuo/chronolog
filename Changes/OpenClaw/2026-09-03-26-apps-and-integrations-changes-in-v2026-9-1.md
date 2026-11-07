---
card_id: openclaw-2026-09-03-aa3644
date: '2026-09-03'
description: 'OpenClaw · 2026-09-03 · Apps and Integrations: 26 changes in v2026.9.1
  — The same rule reaches the edges of maintenance. Interactive uninstall keeps local…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If
    you have a recording with each speaker with a different microphone, or saved…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2820
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 2b706b1b8946989839687eeb371bf9a9cd5832829b180411f25777cdaf892da7
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-03-aa3644
  comparison: ''
  date: '2026-09-03'
  description: 'OpenClaw — v2026.9.1: 26 Apps and Integrations changes'
  evidence:
  - quote: The same rule reaches the edges of maintenance. Interactive uninstall keeps
      local state and workspaces unless you explicitly select them, Windows snapshots
      work in mixed PowerShell installations, workspace exclusions are applied before
      backup traversal, and plugin recovery publishes a trusted install record only
      after it has verified what it is installing.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: When Doctor cannot finish automatically, its diagnostics now point more
      directly at the thing that needs attention, including retained workspace files,
      plugin version drift, shared credential health, managed Tailscale ownership,
      and externally configured paths that a copied-state rehearsal can still reach.
      Long database maintenance keeps its lease while it works, and managed Tailscale
      upgrades can reclaim only the ordinary exclusive route that still points to
      the configured local Gateway.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Windows Doctor now works across display languages, repairs an unambiguous
      retained shared workspace, and rejects unusable live workspace switches before
      activation. Path-installed Codex bundles, source-built Microsoft Teams checks,
      and compiled plugin artifacts are recognized more accurately during health checks.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Replies now hold onto more of the context that made them meaningful. Microsoft
      Teams channel threads include their parent and sibling messages even when Teams
      omits reply metadata, cross-session deliveries are written into the receiving
      conversation, and LINE tells the answering turn whether a group message actually
      addressed the bot. Wildcard peer routes no longer change with lookup order,
      and Slack RPC replies keep the selected agent’s configured name and emoji.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Slack Agent View roots now keep separate conversation context through both
      Socket Mode and HTTP Request URL restarts, and threaded replies continue targeting
      the established thread. Long-running WhatsApp replies remain readable after
      quote context expires by falling back to an unquoted message.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Several channel failures now recover without making a healthy conversation
      look dead. Telegram can move past a stale session start and acknowledges stored
      button presses before a busy chat finishes earlier work, while channel routes
      release cleanly during replacement, Matrix can repair an upgraded sync database
      with Doctor, and Slack Socket Mode or relay accounts no longer depend on an
      inactive HTTP-only secret. Failed configured channels remain visible as blocked
      with a safe recovery hint instead of disappearing from status and health.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Older supported Feishu, Telegram, WhatsApp, and Matrix plugins keep dispatching
      inbound replies after the host updates, installed external channels work with
      generic message actions and broadcast planning, and narrower Slack lookup problems
      and Tlon parser stalls are repaired. These are channel-specific repairs rather
      than a claim that every transport now behaves identically.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Stopping or replacing a turn now does a better job of stopping the work
      and narration attached to it. Active link fetches and processors are cancelled
      with the reply, obsolete narration cannot update a newer draft, Control UI commentary
      reconciles as one update, and Slack waits for a complete first preamble while
      keeping quiet-preview settings quiet. Successful reaction-only and background
      work also avoid misleading missing-reply fallbacks.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: LanceDB auto-capture now keeps its place when a long conversation is compacted,
      avoids embedding facts it has already handled, serializes overlapping capture
      for the same conversation, and lets in-flight automatic capture finish before
      the plugin closes. New facts are less likely to disappear behind retained messages
      after compaction.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Background ownership is tighter too. Native Gateway invocations no longer
      report a timeout after the operation has already settled, private node workers
      exit after their owned cleanup even when stdin or a plugin child keeps the event
      loop active, and macOS helper pipes accept short readiness messages while retaining
      split or final diagnostics from MLX speech, SSH, node workers, computer control,
      and cookie sync.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Browser control is more predictable from the first local screenshot to
      an attached Chrome tab or a remote desktop. Standalone agents can reach the
      local browser without borrowing Gateway credentials, selected tabs keep valid
      commands through ordinary group changes, paired-machine actions report where
      they ran, and Chrome MCP endpoint checks happen before a connection begins.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Existing-session attachments now use the reviewed Chrome DevTools MCP 1.8.0
      release rather than following a moving latest tag. Custom launch commands remain
      operator-managed, while offline hosts need that exact package cached or an operator-provided
      executable.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Custom Chrome MCP endpoint arguments now pass through the same hostname
      policy as the endpoint OpenClaw will actually use, before a subprocess or network
      connection begins. Unsafe, malformed, empty, duplicate, or conflicting arguments
      fail clearly without echoing credential-bearing URLs, while trusted overrides
      and host-local attachment continue to work.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Plugins now behave more like installed software that stays under the operator's
      control. Updates preserve reviewed state, managed provider removals remain removed
      after restart, channel setup follows the agent that was actually selected, and
      the integrations around them do a better job of keeping credentials, errors,
      and cleanup inside the right boundary.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Verified first-party plugins can move through installation, updates, re-enablement,
      and Doctor repair without stopping for a capability prompt that OpenClaw can
      already resolve from matching catalog, package, and source identity. That exception
      remains deliberately narrow, so local artifacts, third-party packages, custom
      registries, and conflicting or incomplete provenance still require explicit
      review.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Older installs also behave more predictably. Capability acceptance is saved
      against the replacement artifact during a legacy update, reinstalling a deliberately
      disabled plugin leaves it disabled until the operator enables it, and registry
      or inventory reads no longer mistake build-only metadata for a changed plugin.
      Catalog work does less repeated processing, bundle capabilities remain visible
      in JSON and verbose inventory, and complete POSIX source builds keep their external
      plugin dependencies after the checkout moves.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: 'An explicit channel-level enabled: false now keeps the plugin and all
      of its contributions inactive. Copied state fails closed before loading managed
      plugin code from its original tree, and updates rediscover restored or replaced
      package contents instead of acting on stale filesystem observations.'
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Uninstalling a managed provider plugin now means it stays uninstalled after
      the Gateway restarts, even when an old model, provider, or channel choice still
      refers to it. Reinstalling later does not silently reactivate it, so the final
      enable step remains an explicit operator choice.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: The recovery paths around removal are safer too. Exact orphaned path-source
      records can be cleaned up through the normal CLI instead of by editing OpenClaw
      state, another plugin's channel configuration is preserved during that cleanup,
      and versionless scoped ClawHub packages produce the expected warning when existing
      Claws still depend on them. Malformed archive names no longer derail staging,
      while updated 1Password guidance explains how to recover after Homebrew moves
      the op executable without pinning another disposable path.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Catalog-driven Weixin installs now select the SDK-compatible 2.4.8 package,
      and affected 2.4.6 operators have explicit update and restart guidance. The
      evidence verifies package selection, integrity, and compatibility rather than
      an authenticated Weixin message roundtrip.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: When a plugin does fail, retries preserve the original actionable load
      error instead of making a rejected module graph appear to recover through a
      fallback. SQLite-backed plugin state keeps its bounded WAL retry through wall-clock
      changes, loads that finish after shutdown begins are retired, and interrupted
      service startup shares one cleanup result so a stop handler is not called twice
      for the same attempt.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: External plugins built against the 2026.8.1 SDK keep their conversation-binding
      inspection import, and accepted legacy docks commands remain reachable under
      Tools after upgrade. Plugin authors also gain a supported facade for the same
      node CLI helpers OpenClaw uses, while source plugins can load .mtsx and .ctsx
      configured-state or persisted-auth checkers without falsely reporting that state
      as absent.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Doctor now compares the selected state directory only with the effective
      account's default, avoiding sibling home-directory paths and unrelated backup
      warnings on shared systems. If a targeted session import or restore cannot archive
      a transcript, its durable migration record keeps useful failure details and
      the original recovery source while masking secret-shaped values; iOS agent deep
      links omit the complete incoming URL from diagnostics, and configuration responses
      redact credentials, SecretRef identifiers, and internal plugin metadata from
      pre-migration snapshots.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Azure OpenAI BYOK traffic through the Copilot extension also gains a separate
      request boundary. Each local proxy receives a fresh credential, verifies it
      before accepting request-body data, and removes it before forwarding upstream,
      while configured provider headers and the existing non-Azure nonce path remain
      intact. The Azure path relies on header forwarding verified for the shipped
      Copilot SDK version.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Common startup paths now load less optional code and reuse more work they
      have already verified. Gateway readiness avoids repeated Doctor and plugin-metadata
      preparation, ordinary shell commands defer model review and follow-up delivery
      until those paths are actually needed, and concurrent first turns share one
      workspace Git setup. Approval, elevation, cancellation, and delivery rules stay
      where they were.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: The same principle carries through troubleshooting. Rolling log tails read
      the file OpenClaw is currently writing, session-observer warnings show a redacted
      cause instead of an empty object, failover counters agree across console and
      structured logs, and failed search or Git snapshot diagnostics explain what
      was lost while keeping sensitive values out of persisted output. Plugin validation
      reports every genuinely missing field in one pass, tool-policy warnings stop
      recommending grants that an active deny would block, and native PR quota failures
      once again include safe manual retry guidance for both observed GraphQL variants
      while failed SSH tunnel startup cleans up its readiness work.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 26-apps-and-integrations-changes-in-v2026-9-1
  source_release: openclaw-2026-09-03-v2026-9-1-281124fc
  source_type: openclaw_changelog
  theme: apps-integrations
  title: 26 Apps and Integrations changes in v2026.9.1
  type: change
related_changes:
- '[[Changes/Claude Code/2026-09-03-4-apps-and-integrations-changes-in-v2-1-260|4
  Apps and Integrations changes in v2.1.260]]'
- '[[Changes/Claude Code/2026-09-03-added-reload-plugins-to-headless-sessions-so-it-appears-in-the-claude-code-deskt|Added
  /reload-plugins to headless sessions, so it appears in the Claude Code…]]'
- '[[Changes/Codex CLI/2026-09-03-18-apps-and-integrations-changes-in-rust-v0-153-0|18
  Apps and Integrations changes in rust-v0.153.0]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-03-v2026-9-1-281124fc|openclaw-2026-09-03-v2026-9-1-281124fc]]'
source_type: openclaw_changelog
theme: apps-integrations
title: 26 Apps and Integrations changes in v2026.9.1
type: change
---

<!-- chronolog:begin region="header" -->
# 26 Apps and Integrations changes in v2026.9.1

**OpenClaw** · 2026-09-03 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.1) · from [[Releases/OpenClaw/openclaw-2026-09-03-v2026-9-1-281124fc|v2026.9.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> The same rule reaches the edges of maintenance. Interactive uninstall keeps local state and workspaces unless you explicitly select them, Windows snapshots work in mixed PowerShell installations, workspace exclusions are applied before backup traversal, and plugin recovery publishes a trusted install record only after it has verified what it is installing.

> When Doctor cannot finish automatically, its diagnostics now point more directly at the thing that needs attention, including retained workspace files, plugin version drift, shared credential health, managed Tailscale ownership, and externally configured paths that a copied-state rehearsal can still reach. Long database maintenance keeps its lease while it works, and managed Tailscale upgrades can reclaim only the ordinary exclusive route that still points to the configured local Gateway.

> Windows Doctor now works across display languages, repairs an unambiguous retained shared workspace, and rejects unusable live workspace switches before activation. Path-installed Codex bundles, source-built Microsoft Teams checks, and compiled plugin artifacts are recognized more accurately during health checks.

> Replies now hold onto more of the context that made them meaningful. Microsoft Teams channel threads include their parent and sibling messages even when Teams omits reply metadata, cross-session deliveries are written into the receiving conversation, and LINE tells the answering turn whether a group message actually addressed the bot. Wildcard peer routes no longer change with lookup order, and Slack RPC replies keep the selected agent’s configured name and emoji.

> Slack Agent View roots now keep separate conversation context through both Socket Mode and HTTP Request URL restarts, and threaded replies continue targeting the established thread. Long-running WhatsApp replies remain readable after quote context expires by falling back to an unquoted message.

> Several channel failures now recover without making a healthy conversation look dead. Telegram can move past a stale session start and acknowledges stored button presses before a busy chat finishes earlier work, while channel routes release cleanly during replacement, Matrix can repair an upgraded sync database with Doctor, and Slack Socket Mode or relay accounts no longer depend on an inactive HTTP-only secret. Failed configured channels remain visible as blocked with a safe recovery hint instead of disappearing from status and health.

> Older supported Feishu, Telegram, WhatsApp, and Matrix plugins keep dispatching inbound replies after the host updates, installed external channels work with generic message actions and broadcast planning, and narrower Slack lookup problems and Tlon parser stalls are repaired. These are channel-specific repairs rather than a claim that every transport now behaves identically.

> Stopping or replacing a turn now does a better job of stopping the work and narration attached to it. Active link fetches and processors are cancelled with the reply, obsolete narration cannot update a newer draft, Control UI commentary reconciles as one update, and Slack waits for a complete first preamble while keeping quiet-preview settings quiet. Successful reaction-only and background work also avoid misleading missing-reply fallbacks.

> LanceDB auto-capture now keeps its place when a long conversation is compacted, avoids embedding facts it has already handled, serializes overlapping capture for the same conversation, and lets in-flight automatic capture finish before the plugin closes. New facts are less likely to disappear behind retained messages after compaction.

> Background ownership is tighter too. Native Gateway invocations no longer report a timeout after the operation has already settled, private node workers exit after their owned cleanup even when stdin or a plugin child keeps the event loop active, and macOS helper pipes accept short readiness messages while retaining split or final diagnostics from MLX speech, SSH, node workers, computer control, and cookie sync.

> Browser control is more predictable from the first local screenshot to an attached Chrome tab or a remote desktop. Standalone agents can reach the local browser without borrowing Gateway credentials, selected tabs keep valid commands through ordinary group changes, paired-machine actions report where they ran, and Chrome MCP endpoint checks happen before a connection begins.

> Existing-session attachments now use the reviewed Chrome DevTools MCP 1.8.0 release rather than following a moving latest tag. Custom launch commands remain operator-managed, while offline hosts need that exact package cached or an operator-provided executable.

> Custom Chrome MCP endpoint arguments now pass through the same hostname policy as the endpoint OpenClaw will actually use, before a subprocess or network connection begins. Unsafe, malformed, empty, duplicate, or conflicting arguments fail clearly without echoing credential-bearing URLs, while trusted overrides and host-local attachment continue to work.

> Plugins now behave more like installed software that stays under the operator's control. Updates preserve reviewed state, managed provider removals remain removed after restart, channel setup follows the agent that was actually selected, and the integrations around them do a better job of keeping credentials, errors, and cleanup inside the right boundary.

> Verified first-party plugins can move through installation, updates, re-enablement, and Doctor repair without stopping for a capability prompt that OpenClaw can already resolve from matching catalog, package, and source identity. That exception remains deliberately narrow, so local artifacts, third-party packages, custom registries, and conflicting or incomplete provenance still require explicit review.

> Older installs also behave more predictably. Capability acceptance is saved against the replacement artifact during a legacy update, reinstalling a deliberately disabled plugin leaves it disabled until the operator enables it, and registry or inventory reads no longer mistake build-only metadata for a changed plugin. Catalog work does less repeated processing, bundle capabilities remain visible in JSON and verbose inventory, and complete POSIX source builds keep their external plugin dependencies after the checkout moves.

> An explicit channel-level enabled: false now keeps the plugin and all of its contributions inactive. Copied state fails closed before loading managed plugin code from its original tree, and updates rediscover restored or replaced package contents instead of acting on stale filesystem observations.

> Uninstalling a managed provider plugin now means it stays uninstalled after the Gateway restarts, even when an old model, provider, or channel choice still refers to it. Reinstalling later does not silently reactivate it, so the final enable step remains an explicit operator choice.

> The recovery paths around removal are safer too. Exact orphaned path-source records can be cleaned up through the normal CLI instead of by editing OpenClaw state, another plugin's channel configuration is preserved during that cleanup, and versionless scoped ClawHub packages produce the expected warning when existing Claws still depend on them. Malformed archive names no longer derail staging, while updated 1Password guidance explains how to recover after Homebrew moves the op executable without pinning another disposable path.

> Catalog-driven Weixin installs now select the SDK-compatible 2.4.8 package, and affected 2.4.6 operators have explicit update and restart guidance. The evidence verifies package selection, integrity, and compatibility rather than an authenticated Weixin message roundtrip.

> When a plugin does fail, retries preserve the original actionable load error instead of making a rejected module graph appear to recover through a fallback. SQLite-backed plugin state keeps its bounded WAL retry through wall-clock changes, loads that finish after shutdown begins are retired, and interrupted service startup shares one cleanup result so a stop handler is not called twice for the same attempt.

> External plugins built against the 2026.8.1 SDK keep their conversation-binding inspection import, and accepted legacy docks commands remain reachable under Tools after upgrade. Plugin authors also gain a supported facade for the same node CLI helpers OpenClaw uses, while source plugins can load .mtsx and .ctsx configured-state or persisted-auth checkers without falsely reporting that state as absent.

> Doctor now compares the selected state directory only with the effective account's default, avoiding sibling home-directory paths and unrelated backup warnings on shared systems. If a targeted session import or restore cannot archive a transcript, its durable migration record keeps useful failure details and the original recovery source while masking secret-shaped values; iOS agent deep links omit the complete incoming URL from diagnostics, and configuration responses redact credentials, SecretRef identifiers, and internal plugin metadata from pre-migration snapshots.

> Azure OpenAI BYOK traffic through the Copilot extension also gains a separate request boundary. Each local proxy receives a fresh credential, verifies it before accepting request-body data, and removes it before forwarding upstream, while configured provider headers and the existing non-Azure nonce path remain intact. The Azure path relies on header forwarding verified for the shipped Copilot SDK version.

> Common startup paths now load less optional code and reuse more work they have already verified. Gateway readiness avoids repeated Doctor and plugin-metadata preparation, ordinary shell commands defer model review and follow-up delivery until those paths are actually needed, and concurrent first turns share one workspace Git setup. Approval, elevation, cancellation, and delivery rules stay where they were.

> The same principle carries through troubleshooting. Rolling log tails read the file OpenClaw is currently writing, session-observer warnings show a redacted cause instead of an empty object, failover counters agree across console and structured logs, and failed search or Git snapshot diagnostics explain what was lost while keeping sensitive values out of persisted output. Plugin validation reports every genuinely missing field in one pass, tool-policy warnings stop recommending grants that an active deny would block, and native PR quota failures once again include safe manual retry guidance for both observed GraphQL variants while failed SSH tunnel startup cleans up its readiness work.

Source: https://docs.openclaw.ai/releases/2026.9.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-09-03-14-agent-mode-changes-in-v2026-9-1|14 Agent Mode changes in v2026.9.1]] · Agent Mode
- [[Changes/OpenClaw/2026-09-03-12-voice-and-audio-changes-in-v2026-9-1|12 Voice and Audio changes in v2026.9.1]] · Voice and Audio
- [[Changes/OpenClaw/2026-09-03-2-files-and-data-changes-in-v2026-9-1|2 Files and Data changes in v2026.9.1]] · Files and Data
- [[Changes/OpenClaw/2026-09-03-7-collaboration-changes-in-v2026-9-1|7 Collaboration changes in v2026.9.1]] · Collaboration
- [[Changes/OpenClaw/2026-09-03-10-mobile-and-desktop-changes-in-v2026-9-1|10 Mobile and Desktop changes in v2026.9.1]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-09-03-19-memory-and-personalization-changes-in-v2026-9-1|19 Memory and Personalization changes in v2026.9.1]] · Memory and Personalization
- [[Changes/OpenClaw/2026-09-03-3-editor-experience-changes-in-v2026-9-1|3 Editor Experience changes in v2026.9.1]] · Editor Experience
- [[Changes/OpenClaw/2026-09-03-2-search-and-browsing-changes-in-v2026-9-1|2 Search and Browsing changes in v2026.9.1]] · Search and Browsing
- [[Changes/OpenClaw/2026-09-03-12-account-and-access-changes-in-v2026-9-1|12 Account and Access changes in v2026.9.1]] · Account and Access
- [[Changes/OpenClaw/2026-09-03-several-less-visible-repairs-keep-the-apps-from-failing-around-dependencies-and|Several less visible repairs keep the apps from failing around dependencies…]] · Multimodal Input
- [[Changes/OpenClaw/2026-09-03-13-automation-and-scheduling-changes-in-v2026-9-1|13 Automation and Scheduling changes in v2026.9.1]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-09-03-an-update-or-doctor-repair-now-does-more-to-preserve-the-setup-you-already-autho|An update or Doctor repair now does more to preserve the setup you already authored…]] · Projects and Workspaces
- [[Changes/OpenClaw/2026-09-03-11-developer-workflow-changes-in-v2026-9-1|11 Developer Workflow changes in v2026.9.1]] · Developer Workflow
- [[Changes/OpenClaw/2026-09-03-3-accessibility-and-localization-changes-in-v2026-9-1|3 Accessibility and Localization changes in v2026.9.1]] · Accessibility and Localization
- [[Changes/OpenClaw/2026-09-03-10-safety-and-privacy-changes-in-v2026-9-1|10 Safety and Privacy changes in v2026.9.1]] · Safety and Privacy
- [[Changes/OpenClaw/2026-09-03-11-context-window-changes-in-v2026-9-1|11 Context Window changes in v2026.9.1]] · Context Window
- [[Changes/OpenClaw/2026-09-03-12-model-support-changes-in-v2026-9-1|12 Model Support changes in v2026.9.1]] · Model Support
- [[Changes/OpenClaw/2026-09-03-14-interface-experience-changes-in-v2026-9-1|14 Interface Experience changes in v2026.9.1]] · Interface Experience
- [[Changes/OpenClaw/2026-09-03-on-linux-managed-local-model-and-embedding-services-are-preferred-as-the-out-of|On Linux, managed local model and embedding services are preferred…]] · Reliability and Performance
- [[Changes/OpenClaw/2026-09-03-32-other-changes-in-v2026-9-1|32 other changes in v2026.9.1]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-09-03 · Codex CLI · [[Changes/Codex CLI/2026-09-03-18-apps-and-integrations-changes-in-rust-v0-153-0|18 Apps and Integrations changes in rust-v0.153.0]]
- Later: 2026-09-04 · Claude Code · [[Changes/Claude Code/2026-09-04-vscode-added-an-add-server-form-and-a-remove-action-to-the-mcp-servers-dialog-so|VSCode Added an Add server form and a Remove action to the MCP servers dialog…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-12-14 · Descript · [[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If you have a recording with each speaker with a different microphone, or saved…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-03-aa3644&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-03-26-apps-and-integrations-changes-in-v2026-9-1.md%0ACard%20ID%3A%20openclaw-2026-09-03-aa3644%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->