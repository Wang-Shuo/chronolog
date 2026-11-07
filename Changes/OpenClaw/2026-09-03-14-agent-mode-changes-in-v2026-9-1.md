---
card_id: openclaw-2026-09-03-09a540
date: '2026-09-03'
description: 'OpenClaw · 2026-09-03 · Agent Mode: 14 changes in v2026.9.1 — The Control
  UI now gives visual answers, active work, and long-running conversations more room
  to…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1155
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 85288fd82451bef45a00a4dd979d6f783058155bec3b925e53357cf65598e4d3
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-03-09a540
  comparison: ''
  date: '2026-09-03'
  description: 'OpenClaw — v2026.9.1: 14 Agent Mode changes'
  evidence:
  - quote: The Control UI now gives visual answers, active work, and long-running
      conversations more room to behave like one workspace. Diagrams render where
      they are discussed, starting or returning to a session takes less waiting and
      repeated work, and the interface does a better job of holding what you sent,
      your reading position, and the agent or session you were actually looking at.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: The draft, agent workspace, model, and effort controls stay together on
      New Session. Published 2026.9.1 interface with fictional Harbor data; no live
      task execution.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Updates started by an agent on a managed Linux or macOS Gateway can hand
      the work to a detached helper before the service stops, and Windows agent-initiated
      restarts use the Gateway-owned restart path rather than dying with the old process
      tree. That handoff confirms the update was accepted, not that it finished, and
      npm 12 local archives still need a comma-free path.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Delivered replies now retain fenced-code indentation and repeated lines
      while still collapsing duplicate prose. Remote-Mac iMessage attachments wait
      through short materialization delays so the agent receives the file instead
      of an incomplete message.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: One-time jobs keep their newer retry time when the Gateway restarts, and
      an immediate main-session job can still wake its selected agent when periodic
      heartbeats are disabled. Successful one-shot jobs configured for deletion are
      removed as expected rather than being left behind in a disabled state.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Scheduled agent work now keeps model aliases attached to the selected agent,
      and system-owned heartbeats can reach their configured provider after a clean
      Gateway restart by using the currently published runtime. Long or unlimited
      heartbeat runs honor the configured deadline instead of inheriting a fixed ten-minute
      cutoff, while destination-only wakes retain the rest of the configured heartbeat
      behavior.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: The delivery edges are quieter and more accurate as well. An explicit NO_REPLY
      after successful tool work stays silent, the first-alert explanation appears
      only on the first alert for an isolated default route, and bounded agents_wait
      calls keep their requested duration when the system clock moves forward or backward.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Standalone agents with the browser tool enabled now default to the local
      browser when no Gateway or node route was selected. Viewport, full-page, and
      element screenshots capture through the page session that owns the current device
      settings, preserving mobile scale and touch behavior, while an interrupted Chromium
      capture returns a recovery error instead of leaving later screenshots or resizes
      stuck.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Gateway-hosted commands that use a managed GitHub profile stay with the
      credential selected at process launch. If that profile disappears or loses its
      token, later commands stop with reconnect guidance instead of falling back to
      a native account, while already running commands retain their launch credential.
      Dashboards can read GitHub Actions through a repository-scoped grant and the
      owning agent's authenticated access without exposing a token or creating a general
      authenticated proxy; existing anonymous widgets need to be updated or regenerated,
      and Publish PR credential checks may remain cached for up to 60 seconds.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Delegated agent creation now keeps checking the authority of the run that
      requested it through workspace, identity, session, and configuration writes.
      If that run ends while creation is still being prepared, OpenClaw stops before
      starting the next persistent effect instead of finishing later and reporting
      success for a request that is no longer authorized. Users can check openclaw
      agents list and retry from an active run.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: The boundary is forward-looking rather than destructive. A filesystem write
      that already started may finish, a fully published agent remains available,
      and its required bookkeeping can complete rather than leaving partial state
      behind.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Gateways with large agent rosters now reuse prepared roster, model, and
      workspace facts during one startup batch, which lets real HTTP health checks
      answer again instead of leaving a listening socket that never becomes useful.
      Other fleet startup costs can still produce noticeable post-listen delays, but
      the repeated discovery work covered here is gone.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Everyday command feedback is less surprising too. A temporary login-shell
      failure can recover on a later lookup without restarting the Gateway, /agents
      takes one coherent view of the subagent registry, automatic TTS leaves routine
      command output as text, zsh completion keeps examples literal, and strict-JSON
      errors point to the safer file-backed patch workflow.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Background subagent failures are logged without taking down the Gateway,
      and completions wait for a busy parent turn before delivering instead of colliding,
      disappearing, or repeatedly claiming the same result.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 14-agent-mode-changes-in-v2026-9-1
  source_release: openclaw-2026-09-03-v2026-9-1-281124fc
  source_type: openclaw_changelog
  theme: agent-mode
  title: 14 Agent Mode changes in v2026.9.1
  type: change
related_changes:
- '[[Changes/Kimi Code/2026-09-02-3-agent-mode-changes-in-kimi-code-0-40-0|3 Agent
  Mode changes in Kimi Code 0.40.0]]'
- '[[Changes/Claude Code/2026-09-03-2-agent-mode-changes-in-v2-1-260|2 Agent Mode
  changes in v2.1.260]]'
- '[[Changes/Codex CLI/2026-09-03-4-agent-mode-changes-in-rust-v0-153-0|4 Agent Mode
  changes in rust-v0.153.0]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-03-v2026-9-1-281124fc|openclaw-2026-09-03-v2026-9-1-281124fc]]'
source_type: openclaw_changelog
theme: agent-mode
title: 14 Agent Mode changes in v2026.9.1
type: change
---

<!-- chronolog:begin region="header" -->
# 14 Agent Mode changes in v2026.9.1

**OpenClaw** · 2026-09-03 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.1) · from [[Releases/OpenClaw/openclaw-2026-09-03-v2026-9-1-281124fc|v2026.9.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> The Control UI now gives visual answers, active work, and long-running conversations more room to behave like one workspace. Diagrams render where they are discussed, starting or returning to a session takes less waiting and repeated work, and the interface does a better job of holding what you sent, your reading position, and the agent or session you were actually looking at.

> The draft, agent workspace, model, and effort controls stay together on New Session. Published 2026.9.1 interface with fictional Harbor data; no live task execution.

> Updates started by an agent on a managed Linux or macOS Gateway can hand the work to a detached helper before the service stops, and Windows agent-initiated restarts use the Gateway-owned restart path rather than dying with the old process tree. That handoff confirms the update was accepted, not that it finished, and npm 12 local archives still need a comma-free path.

> Delivered replies now retain fenced-code indentation and repeated lines while still collapsing duplicate prose. Remote-Mac iMessage attachments wait through short materialization delays so the agent receives the file instead of an incomplete message.

> One-time jobs keep their newer retry time when the Gateway restarts, and an immediate main-session job can still wake its selected agent when periodic heartbeats are disabled. Successful one-shot jobs configured for deletion are removed as expected rather than being left behind in a disabled state.

> Scheduled agent work now keeps model aliases attached to the selected agent, and system-owned heartbeats can reach their configured provider after a clean Gateway restart by using the currently published runtime. Long or unlimited heartbeat runs honor the configured deadline instead of inheriting a fixed ten-minute cutoff, while destination-only wakes retain the rest of the configured heartbeat behavior.

> The delivery edges are quieter and more accurate as well. An explicit NO_REPLY after successful tool work stays silent, the first-alert explanation appears only on the first alert for an isolated default route, and bounded agents_wait calls keep their requested duration when the system clock moves forward or backward.

> Standalone agents with the browser tool enabled now default to the local browser when no Gateway or node route was selected. Viewport, full-page, and element screenshots capture through the page session that owns the current device settings, preserving mobile scale and touch behavior, while an interrupted Chromium capture returns a recovery error instead of leaving later screenshots or resizes stuck.

> Gateway-hosted commands that use a managed GitHub profile stay with the credential selected at process launch. If that profile disappears or loses its token, later commands stop with reconnect guidance instead of falling back to a native account, while already running commands retain their launch credential. Dashboards can read GitHub Actions through a repository-scoped grant and the owning agent's authenticated access without exposing a token or creating a general authenticated proxy; existing anonymous widgets need to be updated or regenerated, and Publish PR credential checks may remain cached for up to 60 seconds.

> Delegated agent creation now keeps checking the authority of the run that requested it through workspace, identity, session, and configuration writes. If that run ends while creation is still being prepared, OpenClaw stops before starting the next persistent effect instead of finishing later and reporting success for a request that is no longer authorized. Users can check openclaw agents list and retry from an active run.

> The boundary is forward-looking rather than destructive. A filesystem write that already started may finish, a fully published agent remains available, and its required bookkeeping can complete rather than leaving partial state behind.

> Gateways with large agent rosters now reuse prepared roster, model, and workspace facts during one startup batch, which lets real HTTP health checks answer again instead of leaving a listening socket that never becomes useful. Other fleet startup costs can still produce noticeable post-listen delays, but the repeated discovery work covered here is gone.

> Everyday command feedback is less surprising too. A temporary login-shell failure can recover on a later lookup without restarting the Gateway, /agents takes one coherent view of the subagent registry, automatic TTS leaves routine command output as text, zsh completion keeps examples literal, and strict-JSON errors point to the safer file-backed patch workflow.

> Background subagent failures are logged without taking down the Gateway, and completions wait for a busy parent turn before delivering instead of colliding, disappearing, or repeatedly claiming the same result.

Source: https://docs.openclaw.ai/releases/2026.9.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

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
- [[Changes/OpenClaw/2026-09-03-26-apps-and-integrations-changes-in-v2026-9-1|26 Apps and Integrations changes in v2026.9.1]] · Apps and Integrations
- [[Changes/OpenClaw/2026-09-03-10-safety-and-privacy-changes-in-v2026-9-1|10 Safety and Privacy changes in v2026.9.1]] · Safety and Privacy
- [[Changes/OpenClaw/2026-09-03-11-context-window-changes-in-v2026-9-1|11 Context Window changes in v2026.9.1]] · Context Window
- [[Changes/OpenClaw/2026-09-03-12-model-support-changes-in-v2026-9-1|12 Model Support changes in v2026.9.1]] · Model Support
- [[Changes/OpenClaw/2026-09-03-14-interface-experience-changes-in-v2026-9-1|14 Interface Experience changes in v2026.9.1]] · Interface Experience
- [[Changes/OpenClaw/2026-09-03-on-linux-managed-local-model-and-embedding-services-are-preferred-as-the-out-of|On Linux, managed local model and embedding services are preferred…]] · Reliability and Performance
- [[Changes/OpenClaw/2026-09-03-32-other-changes-in-v2026-9-1|32 other changes in v2026.9.1]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-09-03 · Codex CLI · [[Changes/Codex CLI/2026-09-03-4-agent-mode-changes-in-rust-v0-153-0|4 Agent Mode changes in rust-v0.153.0]]
- Later: 2026-09-03 · Qoder · [[Changes/Qoder/2026-09-03-artifact-preview-in-a-separate-window-open-agent-generated-artifacts-in-a-standa|Artifact preview in a separate window]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-03-09a540&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-03-14-agent-mode-changes-in-v2026-9-1.md%0ACard%20ID%3A%20openclaw-2026-09-03-09a540%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->