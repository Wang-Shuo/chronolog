---
card_id: devin-2026-05-22-e1a627
date: '2026-05-22'
description: 'Devin · 2026-05-22 · Safety and Privacy: Automation sessions now appear
  in a dedicated "Automations involving you" sidebar folder instead of being auto-pinned…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke
    Application Access]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2124
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: significant
kind: change
machine_hash: e0601bb926dcb9e7f4cc377290c516c19843b7a63901c1df5773b7a584f29030
product: devin
product_name: Devin
record:
  ai_generated: true
  card_id: devin-2026-05-22-e1a627
  comparison: ''
  confidence: low
  date: '2026-05-22'
  description: 'Devin — Devin updates — 2026-05-22: Automation sessions now appear
    in a dedicated "Automations involving you" sidebar folder instead of being auto-pinned.
    Session @-mentions in chat are clickable links. A new Cmd+K action copies the
    session URL to clipboard. Archive undo now restores cascade-archived child sessions.
    MCP connection errors are surfaced instead of silently swallowed, and a new disconnect
    action removes stored OAuth tokens. Integration mappings for Linear, Slack, Teams,
    and Jira are validated at save time. The repo selector shows a Recent section
    and org labels. Tool calls in Watch Devin Work display timing. Automation-spawned
    sessions can be renamed by any org member. Integration page actions are permission-gated.
    File URLs in the timeline link to the correct git provider. GHES installations
    resolve bot identity per-config and scope webhook processing to the owning account.'
  evidence:
  - quote: Automation sessions now appear in a dedicated "Automations involving you"
      sidebar folder instead of being auto-pinned. Session @-mentions in chat are
      clickable links. A new Cmd+K action copies the session URL to clipboard. Archive
      undo now restores cascade-archived child sessions. MCP connection errors are
      surfaced instead of silently swallowed, and a new disconnect action removes
      stored OAuth tokens. Integration mappings for Linear, Slack, Teams, and Jira
      are validated at save time. The repo selector shows a Recent section and org
      labels. Tool calls in Watch Devin Work display timing. Automation-spawned sessions
      can be renamed by any org member. Integration page actions are permission-gated.
      File URLs in the timeline link to the correct git provider. GHES installations
      resolve bot identity per-config and scope webhook processing to the owning account.
    source_release: https://docs.devin.ai/release-notes/2026
  extractor_version: fallback-v5
  impact: significant
  kind: change
  product: devin
  product_name: Devin
  slug: automation-sessions-now-appear-in-a-dedicated-automations-involving-you-sidebar
  source_release: devin-2026-05-22-2026-05-22-243c68d8
  source_type: devin_changelog
  theme: safety-privacy
  theme_matches:
  - matched_terms:
    - integration
    - mcp
    score: 100
    theme: apps-integrations
  - matched_terms:
    - automation
    - automations
    score: 100
    theme: automation-scheduling
  - matched_terms:
    - cmd k
    score: 60
    theme: editor-experience
  - matched_terms:
    - oauth
    score: 50
    theme: account-access
  - matched_terms:
    - tokens
    score: 50
    theme: context-window
  - matched_terms:
    - sidebar
    score: 50
    theme: interface-experience
  theme_resolution: manual-semantic-rule-v2
  title: Automation sessions now appear in a dedicated "Automations involving you"
    sidebar…
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-05-21-17-safety-and-privacy-changes-in-rust-v0-133-0|17
  Safety and Privacy changes in rust-v0.133.0]]'
- '[[Changes/Claude Code/2026-05-22-2-safety-and-privacy-changes-in-v2-1-149|2 Safety
  and Privacy changes in v2.1.149]]'
- '[[Changes/Devin/2026-05-22-inline-repo-permission-toggle|Inline Repo Permission
  Toggle]]'
source_release: '[[Releases/Devin/devin-2026-05-22-2026-05-22-243c68d8|devin-2026-05-22-2026-05-22-243c68d8]]'
source_type: devin_changelog
theme: safety-privacy
title: Automation sessions now appear in a dedicated "Automations involving you" sidebar…
type: change
---

<!-- chronolog:begin region="header" -->
# Automation sessions now appear in a dedicated "Automations involving you" sidebar…

**Devin** · 2026-05-22 · [[Themes/safety-privacy|Safety and Privacy]] · [Official source](https://docs.devin.ai/release-notes/2026) · from [[Releases/Devin/devin-2026-05-22-2026-05-22-243c68d8|Devin updates — 2026-05-22]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Automation sessions now appear in a dedicated "Automations involving you" sidebar folder instead of being auto-pinned. Session @-mentions in chat are clickable links. A new Cmd+K action copies the session URL to clipboard. Archive undo now restores cascade-archived child sessions. MCP connection errors are surfaced instead of silently swallowed, and a new disconnect action removes stored OAuth tokens. Integration mappings for Linear, Slack, Teams, and Jira are validated at save time. The repo selector shows a Recent section and org labels. Tool calls in Watch Devin Work display timing. Automation-spawned sessions can be renamed by any org member. Integration page actions are permission-gated. File URLs in the timeline link to the correct git provider. GHES installations resolve bot identity per-config and scope webhook processing to the owning account.
>
> Source: https://docs.devin.ai/release-notes/2026
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Devin/2026-05-22-posthog-mcp|PostHog MCP]] · Apps and Integrations
- [[Changes/Devin/2026-05-22-custom-rrule-schedule-input|Custom RRULE Schedule Input]] · Automation and Scheduling
- [[Changes/Devin/2026-05-22-gitlab-oauth-scope-and-token-refresh|GitLab OAuth Scope and Token Refresh]] · Account and Access
- [[Changes/Devin/2026-05-22-github-connection-no-longer-required-for-automations|GitHub Connection No Longer Required for Automations]] · Automation and Scheduling
- [[Changes/Devin/2026-05-22-gitlab-interactive-pr-review|GitLab Interactive PR Review]] · Developer Workflow
- [[Changes/Devin/2026-05-22-enterprise-max-concurrent-snapshot-builds|Enterprise Max Concurrent Snapshot Builds]] · Enterprise and Administration
- [[Changes/Devin/2026-05-22-network-config-editor-redesign|Network Config Editor Redesign]] · Editor Experience
- [[Changes/Devin/2026-05-22-mcp-oauth-resource-parameter|MCP OAuth Resource Parameter]] · Account and Access
- [[Changes/Devin/2026-05-22-pr-review-status-api|PR Review Status API]] · Enterprise and Administration
- [[Changes/Devin/2026-05-22-platform-default-settings|Platform Default Settings]] · Automation and Scheduling
- [[Changes/Devin/2026-05-22-inline-repo-permission-toggle|Inline Repo Permission Toggle]] · Safety and Privacy
- [[Changes/Devin/2026-05-22-slack-channel-override|Slack Channel Override]] · Apps and Integrations
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-05-22 · Claude Code · [[Changes/Claude Code/2026-05-22-2-safety-and-privacy-changes-in-v2-1-149|2 Safety and Privacy changes in v2.1.149]]
- Later: 2026-05-22 · Gemini CLI · [[Changes/Gemini CLI/2026-05-22-docs-add-vi-mode-shortcuts-and-clarify-mcp-custom-sandbox-setup-by-chrisjcthomas|docs: add vi mode shortcuts and clarify MCP/custom sandbox setup]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Descript · [[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke Application Access]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20devin-2026-05-22-e1a627&body=Card%3A%20Changes%2FDevin%2F2026-05-22-automation-sessions-now-appear-in-a-dedicated-automations-involving-you-sidebar.md%0ACard%20ID%3A%20devin-2026-05-22-e1a627%0ASource%3A%20https%3A%2F%2Fdocs.devin.ai%2Frelease-notes%2F2026%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->