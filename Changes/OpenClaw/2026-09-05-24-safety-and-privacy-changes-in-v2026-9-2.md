---
card_id: openclaw-2026-09-05-02e2cd
date: '2026-09-05'
description: 'OpenClaw · 2026-09-05 · Safety and Privacy: 24 changes in v2026.9.2
  — Upgrade note for shared Gateways: If you run several agents on one Gateway, review
  their…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke
    Application Access]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2230
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 39d0e26b5223305c3c434c3c4c36868be3a6710bf594c93c7349427a5a9b82e9
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-05-02e2cd
  comparison: ''
  date: '2026-09-05'
  description: 'OpenClaw — v2026.9.2: 24 Safety and Privacy changes'
  evidence:
  - quote: 'Upgrade note for shared Gateways: If you run several agents on one Gateway,
      review their conversation access before upgrading. Omitted settings now let
      agents with session tools read and search other agents'' conversations, including
      other users'' transcripts. Explicitly narrow visibility and agent-pair access
      where needed; mutually untrusted users need separate Gateways. See Security
      and Privacy for the settings and their limits.'
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: When Doctor or onboarding cannot update your shell profile, completion
      setup now provides a command that loads the prepared completions in your current
      shell instead of sending you back into the same permission failure. Run the
      complete command it displays; enabling completion for future shells still requires
      fixing the reported permission or read-only error and retrying installation.
      PowerShell recovery commands also handle paths containing typographic apostrophes.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: When a saved microphone cannot be opened for a browser Talk call, the error
      can offer Use System default for this call. You decide whether to retry with
      that microphone, and your saved choice remains in place for later calls. Permission
      failures stay visible, and leaving or replacing the call retires the offer so
      an old button cannot open another microphone.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Closing the microphone picker or leaving Appearance also prevents delayed
      device discovery from requesting camera or microphone access after you have
      moved on. Deliberately returning to an active picker still allows the normal
      permission request.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Configured owners can ask for an update in chat or use /update , with guidance
      when their account lacks owner access. Chat updates require commands.ownerAllowFrom
      and the existing commands.restart permission, and reports for existing web conversations
      can be saved directly into the conversation without an extra model turn. Managed
      services may miss intermediate notices, and a usable delivery route is still
      needed for an external chat notice.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Explicit --run permits host commands without further approval prompts during
      that repair. Filesystem tools enforce the installation or candidate-root boundary,
      but shell commands follow the repair prompt and have no OS sandbox. Explicit
      tool denies remain in force, and unsupported execution routes produce guidance
      for an external handoff. The installation triage guide explains these limits
      and the checked result.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: If you use an alternative memory plugin and keep Memory Core enabled for
      Dreaming, indexing now stays with the plugin you selected. Memory Core can continue
      contributing Dreaming support without starting unwanted embedding work or lending
      its private-conversation recall permission to the other plugin. This prevents
      that unselected component from starting new work; embedding batches already
      submitted to a provider still need separate handling.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: A bundled Control UI skill now guides agents through building a dashboard
      in the intended conversation, preserving existing widgets, and checking what
      actually renders. Follow-up guidance explains supported ways to load external
      data and troubleshoot blank remote widgets without changing the widget sandbox
      or automatically configuring hosting.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: The existing native-app languages receive updated labels and guidance across
      phones, watches, and Mac, including chat selection and code-copy actions, model
      controls, Dock icon choices, and Gateway error titles. Apple translations also
      cover standalone Watch voice setup and microphone permission, plus Mac browser
      sign-in and reconnect guidance, so the instructions surrounding those features
      are available in the supported language catalogs.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: This requires a fresh authenticated Control UI turn with operator.admin
      permission, and managing someone else's job preserves its creator and scheduled
      execution policy. Creating command jobs remains a CLI or Gateway API operation.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: New automations created through Claude Code or Codex can retain the native
      file and command capabilities authorized in the creating turn. If an older job
      already has an empty tool-permission list, recreate it or explicitly edit its
      tools from a fresh authorized turn. Administrator-managed shell restrictions
      still apply.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: For agents using computer control , screenshot-capable CUA sessions can
      pause and then inspect a fresh image before continuing. Clicks and drags in
      CUA window images now account for resizing done by OpenClaw, so the delivered
      image and the requested position agree. Screenshot permission is still required,
      and a missing usable image prevents pixel-based actions while leaving supported
      element targeting available. Desktop viewing also handles the repaired clipboard
      case without dropping the connection, and a stalled receiver pauses further
      input until it can accept it again.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Session cleanup protects tabs that have been reassigned or used again,
      avoids overlapping duplicate close attempts, and skips loading browser components
      when there are no tabs to clean up. Sandbox browser startup and cleanup load
      a smaller part of the browser code and yield during activation, reducing the
      cold-path pauses while some loading remains blocking. Desktop-node setup guidance
      also removes an unnecessary Gateway restart under the default reload mode, while
      keeping the required node restart and pairing approval.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Native interfaces from user-installed plugins are experimental and off
      by default. Enable Settings → Labs → Custom plugin UI , restart the Gateway,
      and reload your browser tabs, using the connected Gateway's own HTTPS or trusted
      localhost address. Install only code you trust because it runs with your signed-in
      operator permissions, without a plugin sandbox. Authors should pin and test
      their OpenClaw host version.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: The copy follows the Team agent's normal permissions and treats imported
      history as untrusted reference material. It does not resume the source computer,
      inherit its tools, or synchronize later changes. Shared Beams are visible to
      Gateway operators with read permission; continuation also requires write or
      admin permission and access to the chosen agent. Delayed uploads no longer replace
      a newer snapshot or turn a completed snapshot live again at the same revision,
      keeping the saved history used for continuation intact.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Plugin tools now keep their supported input preparation and required one-at-a-time
      execution behavior in later sessions, using the current session's tool factory.
      A tool unavailable in that session can be omitted without taking healthy sibling
      tools with it, and literal names such as constructor work in tool permission
      rules while existing deny rules continue to apply.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: For IDEs using the Gateway-backed ACP bridge, an externally stopped run
      can show its carried error cause instead of only an unexplained cancellation.
      Recording long ACP sessions also avoids repeatedly loading previous message
      payloads while preserving saved replay. On MCP process tools and Codex's OpenClaw
      sandbox process tool, accepted final results clear their matching completion
      notice so it is not repeated later.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: When you ask an agent to change an OpenClaw setting, effective Full Access
      can now carry that permitted change through without a redundant approval card,
      including when Full Access comes from the configured default. Restricted runs
      still need approval, and operation restrictions, tool policy, and live permission
      checks continue to apply. In Guarded mode, the requesting tool waits for the
      actual result of Allow, Deny, expiry, or failure, so dismissing a card no longer
      leaves the agent reporting that it is waiting for a change that already finished.
      Stop cancels the pending request, and a late approval cannot revive it.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Codex connected-app actions in ask mode also request approval within the
      current native thread, including resumed conversations and side questions, without
      rewriting saved app preferences. If an ordinary app-inventory check times out,
      chat can continue with those app tools disabled; their availability is separate
      from permission to use them, and scheduled work retains its stricter authority
      checks. Native administrative requirements still apply. Managed ACP sessions
      using the optional plugin-tools bridge now hide denied plugin tools and reject
      direct calls to them.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: On a Mac, the local node now reuses credentials belonging to the selected
      Gateway, and switching Gateways retires the previous Gateway’s automatic skill
      permissions. The Exec Approvals pane refreshes its trusted commands and agent
      choices while keeping unfinished allowlist edits. Older Mac credentials with
      unknown Gateway ownership may require pairing again through the existing Approve
      on gateway prompt. On Windows, an approved device can move among the CLI, TUI,
      and Node Host without another approval solely for equivalent platform metadata;
      genuine identity and permission changes still go through their checks.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Agent and experimental Claw removal refuses to proceed while a database
      is actively in use and preserves directories containing another agent’s registered
      data. If session cleanup or transcript archiving fails after configuration removal,
      the result reports partial cleanup instead of completion. Correct the reported
      error, preview and retry removal, and finish cleanup before recreating the agent.
      Conversation deletion can still wait on native cleanup or database settlement,
      so these permission checks do not establish a total deletion timeout.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Doctor recovery reports keep report-bearing links out of terminal and JSON
      output and preserve the approved report when a GitHub submission has an uncertain
      outcome. A later run checks for the same report instead of automatically posting
      again, and declining consent keeps reporting local. Sanitized report bodies
      can still appear in JSON. Once a submission receipt is claimed, its version-4
      recovery manifest cannot be read by older Doctor writers that only understand
      versions 1–3, even if the claim is later cleared.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Installing an npm plugin with an expected integrity checksum now stops
      with a clear error if the registry omits the checksum needed to verify it. Those
      registries must supply integrity metadata for pinned installs to succeed; unpinned
      installations and the existing consent flow for a present but mismatched checksum
      keep their behavior.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Crafted SVG site icons that could freeze conversations and web requests
      are now rejected without triggering that validation freeze, and valid self-closing
      SVG roots pass the repaired check. HTTP-client dependencies also receive security
      updates, while proxy exception matching handles a single trailing DNS dot consistently
      in either the destination or NO_PROXY entry. Requests that bypass the proxy
      retain the normal direct-connection DNS checks.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 24-safety-and-privacy-changes-in-v2026-9-2
  source_release: openclaw-2026-09-05-v2026-9-2-377f6d77
  source_type: openclaw_changelog
  theme: safety-privacy
  title: 24 Safety and Privacy changes in v2026.9.2
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-09-04-5-safety-and-privacy-changes-in-v1-0-83|5
  Safety and Privacy changes in v1.0.83]]'
- '[[Changes/HeyGen/2026-09-04-identity-verification-ui-update|Identity verification
  UI update]]'
- '[[Changes/Kimi Code/2026-09-04-3-safety-and-privacy-changes-in-kimi-code-0-41-0|3
  Safety and Privacy changes in Kimi Code 0.41.0]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-05-v2026-9-2-377f6d77|openclaw-2026-09-05-v2026-9-2-377f6d77]]'
source_type: openclaw_changelog
theme: safety-privacy
title: 24 Safety and Privacy changes in v2026.9.2
type: change
---

<!-- chronolog:begin region="header" -->
# 24 Safety and Privacy changes in v2026.9.2

**OpenClaw** · 2026-09-05 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.2) · from [[Releases/OpenClaw/openclaw-2026-09-05-v2026-9-2-377f6d77|v2026.9.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Upgrade note for shared Gateways: If you run several agents on one Gateway, review their conversation access before upgrading. Omitted settings now let agents with session tools read and search other agents' conversations, including other users' transcripts. Explicitly narrow visibility and agent-pair access where needed; mutually untrusted users need separate Gateways. See Security and Privacy for the settings and their limits.

> When Doctor or onboarding cannot update your shell profile, completion setup now provides a command that loads the prepared completions in your current shell instead of sending you back into the same permission failure. Run the complete command it displays; enabling completion for future shells still requires fixing the reported permission or read-only error and retrying installation. PowerShell recovery commands also handle paths containing typographic apostrophes.

> When a saved microphone cannot be opened for a browser Talk call, the error can offer Use System default for this call. You decide whether to retry with that microphone, and your saved choice remains in place for later calls. Permission failures stay visible, and leaving or replacing the call retires the offer so an old button cannot open another microphone.

> Closing the microphone picker or leaving Appearance also prevents delayed device discovery from requesting camera or microphone access after you have moved on. Deliberately returning to an active picker still allows the normal permission request.

> Configured owners can ask for an update in chat or use /update , with guidance when their account lacks owner access. Chat updates require commands.ownerAllowFrom and the existing commands.restart permission, and reports for existing web conversations can be saved directly into the conversation without an extra model turn. Managed services may miss intermediate notices, and a usable delivery route is still needed for an external chat notice.

> Explicit --run permits host commands without further approval prompts during that repair. Filesystem tools enforce the installation or candidate-root boundary, but shell commands follow the repair prompt and have no OS sandbox. Explicit tool denies remain in force, and unsupported execution routes produce guidance for an external handoff. The installation triage guide explains these limits and the checked result.

> If you use an alternative memory plugin and keep Memory Core enabled for Dreaming, indexing now stays with the plugin you selected. Memory Core can continue contributing Dreaming support without starting unwanted embedding work or lending its private-conversation recall permission to the other plugin. This prevents that unselected component from starting new work; embedding batches already submitted to a provider still need separate handling.

> A bundled Control UI skill now guides agents through building a dashboard in the intended conversation, preserving existing widgets, and checking what actually renders. Follow-up guidance explains supported ways to load external data and troubleshoot blank remote widgets without changing the widget sandbox or automatically configuring hosting.

> The existing native-app languages receive updated labels and guidance across phones, watches, and Mac, including chat selection and code-copy actions, model controls, Dock icon choices, and Gateway error titles. Apple translations also cover standalone Watch voice setup and microphone permission, plus Mac browser sign-in and reconnect guidance, so the instructions surrounding those features are available in the supported language catalogs.

> This requires a fresh authenticated Control UI turn with operator.admin permission, and managing someone else's job preserves its creator and scheduled execution policy. Creating command jobs remains a CLI or Gateway API operation.

> New automations created through Claude Code or Codex can retain the native file and command capabilities authorized in the creating turn. If an older job already has an empty tool-permission list, recreate it or explicitly edit its tools from a fresh authorized turn. Administrator-managed shell restrictions still apply.

> For agents using computer control , screenshot-capable CUA sessions can pause and then inspect a fresh image before continuing. Clicks and drags in CUA window images now account for resizing done by OpenClaw, so the delivered image and the requested position agree. Screenshot permission is still required, and a missing usable image prevents pixel-based actions while leaving supported element targeting available. Desktop viewing also handles the repaired clipboard case without dropping the connection, and a stalled receiver pauses further input until it can accept it again.

> Session cleanup protects tabs that have been reassigned or used again, avoids overlapping duplicate close attempts, and skips loading browser components when there are no tabs to clean up. Sandbox browser startup and cleanup load a smaller part of the browser code and yield during activation, reducing the cold-path pauses while some loading remains blocking. Desktop-node setup guidance also removes an unnecessary Gateway restart under the default reload mode, while keeping the required node restart and pairing approval.

> Native interfaces from user-installed plugins are experimental and off by default. Enable Settings → Labs → Custom plugin UI , restart the Gateway, and reload your browser tabs, using the connected Gateway's own HTTPS or trusted localhost address. Install only code you trust because it runs with your signed-in operator permissions, without a plugin sandbox. Authors should pin and test their OpenClaw host version.

> The copy follows the Team agent's normal permissions and treats imported history as untrusted reference material. It does not resume the source computer, inherit its tools, or synchronize later changes. Shared Beams are visible to Gateway operators with read permission; continuation also requires write or admin permission and access to the chosen agent. Delayed uploads no longer replace a newer snapshot or turn a completed snapshot live again at the same revision, keeping the saved history used for continuation intact.

> Plugin tools now keep their supported input preparation and required one-at-a-time execution behavior in later sessions, using the current session's tool factory. A tool unavailable in that session can be omitted without taking healthy sibling tools with it, and literal names such as constructor work in tool permission rules while existing deny rules continue to apply.

> For IDEs using the Gateway-backed ACP bridge, an externally stopped run can show its carried error cause instead of only an unexplained cancellation. Recording long ACP sessions also avoids repeatedly loading previous message payloads while preserving saved replay. On MCP process tools and Codex's OpenClaw sandbox process tool, accepted final results clear their matching completion notice so it is not repeated later.

> When you ask an agent to change an OpenClaw setting, effective Full Access can now carry that permitted change through without a redundant approval card, including when Full Access comes from the configured default. Restricted runs still need approval, and operation restrictions, tool policy, and live permission checks continue to apply. In Guarded mode, the requesting tool waits for the actual result of Allow, Deny, expiry, or failure, so dismissing a card no longer leaves the agent reporting that it is waiting for a change that already finished. Stop cancels the pending request, and a late approval cannot revive it.

> Codex connected-app actions in ask mode also request approval within the current native thread, including resumed conversations and side questions, without rewriting saved app preferences. If an ordinary app-inventory check times out, chat can continue with those app tools disabled; their availability is separate from permission to use them, and scheduled work retains its stricter authority checks. Native administrative requirements still apply. Managed ACP sessions using the optional plugin-tools bridge now hide denied plugin tools and reject direct calls to them.

> On a Mac, the local node now reuses credentials belonging to the selected Gateway, and switching Gateways retires the previous Gateway’s automatic skill permissions. The Exec Approvals pane refreshes its trusted commands and agent choices while keeping unfinished allowlist edits. Older Mac credentials with unknown Gateway ownership may require pairing again through the existing Approve on gateway prompt. On Windows, an approved device can move among the CLI, TUI, and Node Host without another approval solely for equivalent platform metadata; genuine identity and permission changes still go through their checks.

> Agent and experimental Claw removal refuses to proceed while a database is actively in use and preserves directories containing another agent’s registered data. If session cleanup or transcript archiving fails after configuration removal, the result reports partial cleanup instead of completion. Correct the reported error, preview and retry removal, and finish cleanup before recreating the agent. Conversation deletion can still wait on native cleanup or database settlement, so these permission checks do not establish a total deletion timeout.

> Doctor recovery reports keep report-bearing links out of terminal and JSON output and preserve the approved report when a GitHub submission has an uncertain outcome. A later run checks for the same report instead of automatically posting again, and declining consent keeps reporting local. Sanitized report bodies can still appear in JSON. Once a submission receipt is claimed, its version-4 recovery manifest cannot be read by older Doctor writers that only understand versions 1–3, even if the claim is later cleared.

> Installing an npm plugin with an expected integrity checksum now stops with a clear error if the registry omits the checksum needed to verify it. Those registries must supply integrity metadata for pinned installs to succeed; unpinned installations and the existing consent flow for a present but mismatched checksum keep their behavior.

> Crafted SVG site icons that could freeze conversations and web requests are now rejected without triggering that validation freeze, and valid self-closing SVG roots pass the repaired check. HTTP-client dependencies also receive security updates, while proxy exception matching handles a single trailing DNS dot consistently in either the destination or NO_PROXY entry. Requests that bypass the proxy retain the normal direct-connection DNS checks.

Source: https://docs.openclaw.ai/releases/2026.9.2
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

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
- [[Changes/OpenClaw/2026-09-05-15-context-window-changes-in-v2026-9-2|15 Context Window changes in v2026.9.2]] · Context Window
- [[Changes/OpenClaw/2026-09-05-4-search-and-browsing-changes-in-v2026-9-2|4 Search and Browsing changes in v2026.9.2]] · Search and Browsing
- [[Changes/OpenClaw/2026-09-05-17-voice-and-audio-changes-in-v2026-9-2|17 Voice and Audio changes in v2026.9.2]] · Voice and Audio
- [[Changes/OpenClaw/2026-09-05-21-interface-experience-changes-in-v2026-9-2|21 Interface Experience changes in v2026.9.2]] · Interface Experience
- [[Changes/OpenClaw/2026-09-05-3-reliability-and-performance-changes-in-v2026-9-2|3 Reliability and Performance changes in v2026.9.2]] · Reliability and Performance
- [[Changes/OpenClaw/2026-09-05-you-can-now-put-the-part-of-a-task-you-are-working-on-in-the-main-view-and-keep|Put the part of a task you are working on in the main view and keep the conversation…]] · Developer Workflow
- [[Changes/OpenClaw/2026-09-05-72-other-changes-in-v2026-9-2|72 other changes in v2026.9.2]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-09-04 · Kimi Code · [[Changes/Kimi Code/2026-09-04-3-safety-and-privacy-changes-in-kimi-code-0-41-0|3 Safety and Privacy changes in Kimi Code 0.41.0]]
- Later: 2026-09-08 · Claude Code · [[Changes/Claude Code/2026-09-08-3-safety-and-privacy-changes-in-v2-1-265|3 Safety and Privacy changes in v2.1.265]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Descript · [[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke Application Access]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-05-02e2cd&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-05-24-safety-and-privacy-changes-in-v2026-9-2.md%0ACard%20ID%3A%20openclaw-2026-09-05-02e2cd%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.2%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->