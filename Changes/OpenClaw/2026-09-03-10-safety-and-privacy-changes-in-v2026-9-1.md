---
card_id: openclaw-2026-09-03-c83ddc
date: '2026-09-03'
description: 'OpenClaw · 2026-09-03 · Safety and Privacy: 10 changes in v2026.9.1
  — The macOS AI setup sheet now shows the selected provider and the actual installation
  or…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke
    Application Access]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2228
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: b1ca16ed51db88f1837c497df9a58e3e0869e95296276d52726ba7adf00c8214
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-03-c83ddc
  comparison: ''
  date: '2026-09-03'
  description: 'OpenClaw — v2026.9.1: 10 Safety and Privacy changes'
  evidence:
  - quote: The macOS AI setup sheet now shows the selected provider and the actual
      installation or verification activity instead of presenting an elapsed-time
      percentage as progress. Input controls appear when the setup needs an answer,
      capability consent remains explicit, and late responses from an older attempt
      no longer replace the current setup state.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Returning to existing work is steadier too. Dashboards and background tasks
      stay with the selected agent, interrupted or timed-out sessions show a more
      truthful state, failed cloud or device sessions can be restarted from Chat when
      a compatible target is available, and Ask OpenClaw keeps the conversation and
      draft visible while its runtime is repaired. Sidebar groups, hovercards, assignment
      menus, status icons, and keyboard navigation make large or multi-agent workspaces
      easier to scan without changing the underlying session, permission, or placement
      boundaries.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Before OpenClaw restarts, it now checks the parts of your installation
      that actually need to be ready for the new version. Missing local-memory setup,
      unresolved plugin consent, or incomplete approval migration stops the update
      with a specific repair path, while a migration warning that does not make required
      state unsafe can leave the Gateway reachable in a clearly degraded state so
      you can run Doctor instead of watching a supervisor restart it forever.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: ZIP imports now reserve room across profiles as well. One person with many
      unfinished uploads cannot occupy every pending slot, while existing uploads
      can still finish and linked or merged identities continue to share one allowance.
      Each session also keeps the immutable skill revision that was selected, including
      its supporting files and executable permissions, as work moves through local,
      sandbox, cloud, or node workers.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: A New Session task started from the macOS app can now post a generic native
      completion notice and reopen the exact finished session, including when a fast
      task completes before notification status reaches the dashboard. The notice
      requires previously granted notification permission and a loaded originating
      dashboard, does not prompt for permission, and stays quiet when that session
      is already being viewed.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: OpenClaw can now remember an eligible approval without turning it into
      blanket permission. Durable MCP grants remain tied to one agent, configured
      server, and tool, remote Codex placement grants remain tied to the process and
      placement that earned them, and stricter session or server policy still wins.
      The same boundary now follows delegated agent creation more carefully, while
      private diagnostics, saved reasoning, network requests, guest workspaces, and
      administrative automation each get narrower protections of their own.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Codex now follows the effective session posture when deciding whether an
      MCP tool needs approval, so a default full-permission session can use an unannotated
      tool without stopping for a permission card on every call. Stricter postures
      and explicit server overrides still apply, and Allow Always follows the tool
      across argument and working-directory changes for the current session. For an
      eligible MCP tool on an OpenClaw-configured server, that choice can also become
      a durable grant for the exact agent, server, and tool across later sessions
      and Gateway restarts; Codex apps, native plugin servers, computer-use servers,
      explicit prompt mode, and ambiguous matches remain outside it.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Sandbox-required guests can once again write files, patch code, run project-local
      commands, and delegate work inside a private workspace with workspaceAccess
      set to none . The shared agent workspace and host credentials remain outside
      that boundary, managed skill overlays remain read-only, an explicit ro workspace
      remains read-only, and networking stays off unless an operator enables it.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Secrets commands using --json now return one parseable document on success
      or failure across reload, audit, configure, apply, and store list or get operations.
      Human-readable output and documented exit codes remain unchanged, and this is
      an output-contract repair rather than a change to secret contents, storage,
      or security policy.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: These are scoped resource and attribution controls, not a general security
      guarantee, and their prepared evidence includes controlled services rather than
      every live external provider.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 10-safety-and-privacy-changes-in-v2026-9-1
  source_release: openclaw-2026-09-03-v2026-9-1-281124fc
  source_type: openclaw_changelog
  theme: safety-privacy
  title: 10 Safety and Privacy changes in v2026.9.1
  type: change
related_changes:
- '[[Changes/Kimi Code/2026-09-02-2-safety-and-privacy-changes-in-kimi-code-0-40-0|2
  Safety and Privacy changes in Kimi Code 0.40.0]]'
- '[[Changes/Claude Code/2026-09-03-7-safety-and-privacy-changes-in-v2-1-260|7 Safety
  and Privacy changes in v2.1.260]]'
- '[[Changes/Codex CLI/2026-09-03-6-safety-and-privacy-changes-in-rust-v0-153-0|6
  Safety and Privacy changes in rust-v0.153.0]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-03-v2026-9-1-281124fc|openclaw-2026-09-03-v2026-9-1-281124fc]]'
source_type: openclaw_changelog
theme: safety-privacy
title: 10 Safety and Privacy changes in v2026.9.1
type: change
---

<!-- chronolog:begin region="header" -->
# 10 Safety and Privacy changes in v2026.9.1

**OpenClaw** · 2026-09-03 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.1) · from [[Releases/OpenClaw/openclaw-2026-09-03-v2026-9-1-281124fc|v2026.9.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> The macOS AI setup sheet now shows the selected provider and the actual installation or verification activity instead of presenting an elapsed-time percentage as progress. Input controls appear when the setup needs an answer, capability consent remains explicit, and late responses from an older attempt no longer replace the current setup state.

> Returning to existing work is steadier too. Dashboards and background tasks stay with the selected agent, interrupted or timed-out sessions show a more truthful state, failed cloud or device sessions can be restarted from Chat when a compatible target is available, and Ask OpenClaw keeps the conversation and draft visible while its runtime is repaired. Sidebar groups, hovercards, assignment menus, status icons, and keyboard navigation make large or multi-agent workspaces easier to scan without changing the underlying session, permission, or placement boundaries.

> Before OpenClaw restarts, it now checks the parts of your installation that actually need to be ready for the new version. Missing local-memory setup, unresolved plugin consent, or incomplete approval migration stops the update with a specific repair path, while a migration warning that does not make required state unsafe can leave the Gateway reachable in a clearly degraded state so you can run Doctor instead of watching a supervisor restart it forever.

> ZIP imports now reserve room across profiles as well. One person with many unfinished uploads cannot occupy every pending slot, while existing uploads can still finish and linked or merged identities continue to share one allowance. Each session also keeps the immutable skill revision that was selected, including its supporting files and executable permissions, as work moves through local, sandbox, cloud, or node workers.

> A New Session task started from the macOS app can now post a generic native completion notice and reopen the exact finished session, including when a fast task completes before notification status reaches the dashboard. The notice requires previously granted notification permission and a loaded originating dashboard, does not prompt for permission, and stays quiet when that session is already being viewed.

> OpenClaw can now remember an eligible approval without turning it into blanket permission. Durable MCP grants remain tied to one agent, configured server, and tool, remote Codex placement grants remain tied to the process and placement that earned them, and stricter session or server policy still wins. The same boundary now follows delegated agent creation more carefully, while private diagnostics, saved reasoning, network requests, guest workspaces, and administrative automation each get narrower protections of their own.

> Codex now follows the effective session posture when deciding whether an MCP tool needs approval, so a default full-permission session can use an unannotated tool without stopping for a permission card on every call. Stricter postures and explicit server overrides still apply, and Allow Always follows the tool across argument and working-directory changes for the current session. For an eligible MCP tool on an OpenClaw-configured server, that choice can also become a durable grant for the exact agent, server, and tool across later sessions and Gateway restarts; Codex apps, native plugin servers, computer-use servers, explicit prompt mode, and ambiguous matches remain outside it.

> Sandbox-required guests can once again write files, patch code, run project-local commands, and delegate work inside a private workspace with workspaceAccess set to none . The shared agent workspace and host credentials remain outside that boundary, managed skill overlays remain read-only, an explicit ro workspace remains read-only, and networking stays off unless an operator enables it.

> Secrets commands using --json now return one parseable document on success or failure across reload, audit, configure, apply, and store list or get operations. Human-readable output and documented exit codes remain unchanged, and this is an output-contract repair rather than a change to secret contents, storage, or security policy.

> These are scoped resource and attribution controls, not a general security guarantee, and their prepared evidence includes controlled services rather than every live external provider.

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
- [[Changes/OpenClaw/2026-09-03-11-context-window-changes-in-v2026-9-1|11 Context Window changes in v2026.9.1]] · Context Window
- [[Changes/OpenClaw/2026-09-03-12-model-support-changes-in-v2026-9-1|12 Model Support changes in v2026.9.1]] · Model Support
- [[Changes/OpenClaw/2026-09-03-14-interface-experience-changes-in-v2026-9-1|14 Interface Experience changes in v2026.9.1]] · Interface Experience
- [[Changes/OpenClaw/2026-09-03-on-linux-managed-local-model-and-embedding-services-are-preferred-as-the-out-of|On Linux, managed local model and embedding services are preferred…]] · Reliability and Performance
- [[Changes/OpenClaw/2026-09-03-32-other-changes-in-v2026-9-1|32 other changes in v2026.9.1]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-09-03 · Codex CLI · [[Changes/Codex CLI/2026-09-03-6-safety-and-privacy-changes-in-rust-v0-153-0|6 Safety and Privacy changes in rust-v0.153.0]]
- Later: 2026-09-04 · Claude Code · [[Changes/Claude Code/2026-09-04-4-safety-and-privacy-changes-in-v2-1-261|4 Safety and Privacy changes in v2.1.261]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Descript · [[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke Application Access]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-03-c83ddc&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-03-10-safety-and-privacy-changes-in-v2026-9-1.md%0ACard%20ID%3A%20openclaw-2026-09-03-c83ddc%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->