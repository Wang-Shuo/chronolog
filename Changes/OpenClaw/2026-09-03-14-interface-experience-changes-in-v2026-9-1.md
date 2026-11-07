---
card_id: openclaw-2026-09-03-f55f8b
date: '2026-09-03'
description: 'OpenClaw · 2026-09-03 · Interface Experience: 14 changes in v2026.9.1
  — On a headless machine, the same path provides a one-time authenticated dashboard
  link…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-04-14-descript-s-sidebar-now-has-an-economical-collapsed-state|Collapsed
    Sidebar]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2699
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: interface-experience
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: c0b607f9df370ca74314326efe9d2c235345962323a4dda98a67e0f7ef2bc134
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-03-f55f8b
  comparison: ''
  date: '2026-09-03'
  description: 'OpenClaw — v2026.9.1: 14 Interface Experience changes'
  evidence:
  - quote: On a headless machine, the same path provides a one-time authenticated
      dashboard link and an SSH tunnel template instead of exposing reusable Gateway
      credentials. Custom setup, remote Gateway onboarding, and non-interactive setup
      keep their existing paths when Quick Start is not the right fit.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Guided onboarding can once again configure custom and local providers,
      including endpoints that do not need an API key, and verifies a real response
      before making the new model active. Failed or cancelled checks leave the previous
      configuration alone, while setup reruns preserve an existing agent roster and
      workspace instead of attaching temporary verification work to them.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Eligible npm-installed CLI backends can also be selected by their ordinary
      command name during Windows onboarding. OpenClaw now follows the platform's
      PATHEXT lookup while retaining the neighboring POSIX launcher used by Git Bash,
      so there is no need to hard-code a .cmd path or delete one of npm's shims.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: When an npm install fails, the shell installer still shows the useful terminal
      details and npm's durable debug log, but no longer points to a temporary installer
      log that has already been removed. Shell completion installation and reinstall
      also preserve literal cache paths containing quotes, dollar signs, or backslashes
      across Bash, zsh, Fish, and the emitted PowerShell command, without replacing
      unrelated profile commands.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: New Session now puts the first prompt and its images on screen as soon
      as you send them, keeps the draft available if creation fails, and moves into
      the confirmed conversation without an extra lookup. Chat and New Session also
      load fewer closed workspace features up front, while larger session lists do
      less repeated sidebar work when you switch between conversations. Those performance
      results come from controlled local and synthetic large-roster tests, not a promise
      that every browser or Gateway will see the same speedup, and the measured warm
      Chat path included a small composer-readiness regression.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: The surfaces around the conversation have had the same attention. Dashboards
      fill narrow screens, long task progress and Review content use the space available
      to them, settings show useful loading shapes, and the model picker, agent picker,
      Side chat, Appearance, Usage, publication controls, and pull request previews
      are easier to scan. Keyboard menus recover cleanly, scrollbars remain visible
      beside fades, stale assets are less likely to survive a cache check, and smaller
      initial Settings data leaves more startup headroom without claiming a measured
      end-user latency gain.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: When a delegated system agent asks to change OpenClaw configuration or
      plugins, operators can now approve or deny the request from a configured channel
      and see whether it was applied, denied, cancelled, expired, or could not be
      applied. The request remains tied to the run that created it, so closing that
      run also closes its authority to make the change, while Telegram keeps the approval
      and completion messages in the forum or direct-message topic where the request
      began.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Rendering stays local rather than depending on a network diagram service.
      Android offers a sharp full-screen view with zoom and pan, iOS adds an offline-capable
      vector preview with zoom, pan, and rotation, and macOS uses compact desktop
      controls with native Close and Escape behavior. The exact controls follow each
      platform rather than pretending the three implementations are identical.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Choosing a model should not be an exercise in wondering what else the click
      changed. Model selection now tells you whether a choice is for this session,
      one agent, or the global default before it is saved, while provider logins and
      catalog changes flow into the model list without the ritual Gateway restart.
      This release also tightens the less visible part of that promise, so a temporary
      provider failure, a quiet Codex turn, or a disconnected node is much less likely
      to send work down the wrong route.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: The Control UI now gathers the main model, utility model, first fallback,
      thinking level, and Fast Mode in one autosaving Defaults card, with the scope
      of a model change shown before you make it. It preserves the rest of an ordered
      fallback chain when the first choice changes, and refuses to replace a working
      model when the required harness cannot be activated. The full fallback order
      still lives in the CLI, and the scope disclosure is currently a Control UI feature
      rather than a native-app picker feature.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Child-session results now distinguish confirmed delivery, uncertain delivery,
      and intentional suppression. Fire-and-forget work can deliberately skip requester
      interruption, temporary pre-dispatch failures can retry before delivery begins,
      and Swarm or quiet subagents receive completion guidance that matches how their
      results actually arrive.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Large conversations no longer drag as much unrelated history through every
      nearby task. Resets read only the navigation data they need, session inspection
      walks backward without copying the history, and ordinary turns avoid several
      unnecessary session reads, which leaves more room for the conversation itself.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Deep configuration mutations now fail with bounded validation instead of
      exhausting the call stack, session CLI commands reject invalid or blank targets
      without selecting another agent, and Bash completion handles spaced and equals-separated
      option values more reliably.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Remote and connected setups now hold on to the state they actually observed.
      SSH tunnel startup keeps its configured listener timeout even if the system
      clock changes, node age filters use the Gateway's latest recorded connection
      time, and the Devices roster keeps the genuine Gateway visible while remaining
      bounded under peer pressure and hostname collisions. At the HTTP edge, clients
      that explicitly reject HTML receive the existing startup or not-found response
      instead of an unwanted app shell, while ordinary browser navigation keeps working
      as before.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 14-interface-experience-changes-in-v2026-9-1
  source_release: openclaw-2026-09-03-v2026-9-1-281124fc
  source_type: openclaw_changelog
  theme: interface-experience
  title: 14 Interface Experience changes in v2026.9.1
  type: change
related_changes:
- '[[Changes/Lovable/2026-09-03-open-the-dashboard-sidebar-from-inside-the-editor|Open
  the dashboard sidebar from inside the editor]]'
- '[[Changes/Midjourney/2026-09-03-polish-bugs|POLISH & BUGS]]'
- '[[Changes/Midjourney/2026-09-03-prompt-bar-pills|PROMPT BAR & PILLS]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-03-v2026-9-1-281124fc|openclaw-2026-09-03-v2026-9-1-281124fc]]'
source_type: openclaw_changelog
theme: interface-experience
title: 14 Interface Experience changes in v2026.9.1
type: change
---

<!-- chronolog:begin region="header" -->
# 14 Interface Experience changes in v2026.9.1

**OpenClaw** · 2026-09-03 · [[Themes/interface-experience|Interface Experience]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.1) · from [[Releases/OpenClaw/openclaw-2026-09-03-v2026-9-1-281124fc|v2026.9.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> On a headless machine, the same path provides a one-time authenticated dashboard link and an SSH tunnel template instead of exposing reusable Gateway credentials. Custom setup, remote Gateway onboarding, and non-interactive setup keep their existing paths when Quick Start is not the right fit.

> Guided onboarding can once again configure custom and local providers, including endpoints that do not need an API key, and verifies a real response before making the new model active. Failed or cancelled checks leave the previous configuration alone, while setup reruns preserve an existing agent roster and workspace instead of attaching temporary verification work to them.

> Eligible npm-installed CLI backends can also be selected by their ordinary command name during Windows onboarding. OpenClaw now follows the platform's PATHEXT lookup while retaining the neighboring POSIX launcher used by Git Bash, so there is no need to hard-code a .cmd path or delete one of npm's shims.

> When an npm install fails, the shell installer still shows the useful terminal details and npm's durable debug log, but no longer points to a temporary installer log that has already been removed. Shell completion installation and reinstall also preserve literal cache paths containing quotes, dollar signs, or backslashes across Bash, zsh, Fish, and the emitted PowerShell command, without replacing unrelated profile commands.

> New Session now puts the first prompt and its images on screen as soon as you send them, keeps the draft available if creation fails, and moves into the confirmed conversation without an extra lookup. Chat and New Session also load fewer closed workspace features up front, while larger session lists do less repeated sidebar work when you switch between conversations. Those performance results come from controlled local and synthetic large-roster tests, not a promise that every browser or Gateway will see the same speedup, and the measured warm Chat path included a small composer-readiness regression.

> The surfaces around the conversation have had the same attention. Dashboards fill narrow screens, long task progress and Review content use the space available to them, settings show useful loading shapes, and the model picker, agent picker, Side chat, Appearance, Usage, publication controls, and pull request previews are easier to scan. Keyboard menus recover cleanly, scrollbars remain visible beside fades, stale assets are less likely to survive a cache check, and smaller initial Settings data leaves more startup headroom without claiming a measured end-user latency gain.

> When a delegated system agent asks to change OpenClaw configuration or plugins, operators can now approve or deny the request from a configured channel and see whether it was applied, denied, cancelled, expired, or could not be applied. The request remains tied to the run that created it, so closing that run also closes its authority to make the change, while Telegram keeps the approval and completion messages in the forum or direct-message topic where the request began.

> Rendering stays local rather than depending on a network diagram service. Android offers a sharp full-screen view with zoom and pan, iOS adds an offline-capable vector preview with zoom, pan, and rotation, and macOS uses compact desktop controls with native Close and Escape behavior. The exact controls follow each platform rather than pretending the three implementations are identical.

> Choosing a model should not be an exercise in wondering what else the click changed. Model selection now tells you whether a choice is for this session, one agent, or the global default before it is saved, while provider logins and catalog changes flow into the model list without the ritual Gateway restart. This release also tightens the less visible part of that promise, so a temporary provider failure, a quiet Codex turn, or a disconnected node is much less likely to send work down the wrong route.

> The Control UI now gathers the main model, utility model, first fallback, thinking level, and Fast Mode in one autosaving Defaults card, with the scope of a model change shown before you make it. It preserves the rest of an ordered fallback chain when the first choice changes, and refuses to replace a working model when the required harness cannot be activated. The full fallback order still lives in the CLI, and the scope disclosure is currently a Control UI feature rather than a native-app picker feature.

> Child-session results now distinguish confirmed delivery, uncertain delivery, and intentional suppression. Fire-and-forget work can deliberately skip requester interruption, temporary pre-dispatch failures can retry before delivery begins, and Swarm or quiet subagents receive completion guidance that matches how their results actually arrive.

> Large conversations no longer drag as much unrelated history through every nearby task. Resets read only the navigation data they need, session inspection walks backward without copying the history, and ordinary turns avoid several unnecessary session reads, which leaves more room for the conversation itself.

> Deep configuration mutations now fail with bounded validation instead of exhausting the call stack, session CLI commands reject invalid or blank targets without selecting another agent, and Bash completion handles spaced and equals-separated option values more reliably.

> Remote and connected setups now hold on to the state they actually observed. SSH tunnel startup keeps its configured listener timeout even if the system clock changes, node age filters use the Gateway's latest recorded connection time, and the Devices roster keeps the genuine Gateway visible while remaining bounded under peer pressure and hostname collisions. At the HTTP edge, clients that explicitly reject HTML receive the existing startup or not-found response instead of an unwanted app shell, while ordinary browser navigation keeps working as before.

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
- [[Changes/OpenClaw/2026-09-03-26-apps-and-integrations-changes-in-v2026-9-1|26 Apps and Integrations changes in v2026.9.1]] · Apps and Integrations
- [[Changes/OpenClaw/2026-09-03-10-safety-and-privacy-changes-in-v2026-9-1|10 Safety and Privacy changes in v2026.9.1]] · Safety and Privacy
- [[Changes/OpenClaw/2026-09-03-11-context-window-changes-in-v2026-9-1|11 Context Window changes in v2026.9.1]] · Context Window
- [[Changes/OpenClaw/2026-09-03-12-model-support-changes-in-v2026-9-1|12 Model Support changes in v2026.9.1]] · Model Support
- [[Changes/OpenClaw/2026-09-03-on-linux-managed-local-model-and-embedding-services-are-preferred-as-the-out-of|On Linux, managed local model and embedding services are preferred…]] · Reliability and Performance
- [[Changes/OpenClaw/2026-09-03-32-other-changes-in-v2026-9-1|32 other changes in v2026.9.1]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Interface Experience

- Earlier: 2026-09-03 · Midjourney · [[Changes/Midjourney/2026-09-03-prompt-bar-pills|PROMPT BAR & PILLS]]
- Later: 2026-09-03 · Qoder · [[Changes/Qoder/2026-09-03-batch-tasks-archiving-multi-select-tasks-in-the-sidebar-to-archive-them-and-swit|Batch tasks archiving]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-04-14 · Descript · [[Changes/Descript/2019-04-14-descript-s-sidebar-now-has-an-economical-collapsed-state|Collapsed Sidebar]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-03-f55f8b&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-03-14-interface-experience-changes-in-v2026-9-1.md%0ACard%20ID%3A%20openclaw-2026-09-03-f55f8b%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->