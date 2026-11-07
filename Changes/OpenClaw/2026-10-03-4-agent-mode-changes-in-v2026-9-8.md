---
card_id: openclaw-2026-10-03-6d2d0d
date: '2026-10-03'
description: 'OpenClaw · 2026-10-03 · Agent Mode: 4 changes in v2026.9.8 — Silent-reply
  help. Help text in 20 existing languages now explains where an agent can stay silent…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1185
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 021dbef29f1e6a1bfb97d623fd272ea4c261434758085ee2f9a84df61dc47fe5
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-10-03-6d2d0d
  comparison: ''
  date: '2026-10-03'
  description: 'OpenClaw — v2026.9.8: 4 Agent Mode changes'
  evidence:
  - quote: 'Silent-reply help. Help text in 20 existing languages now explains where
      an agent can stay silent. Silence settings apply to group chats; direct chats
      and work requested inside OpenClaw require a reply. #163409 , using translations
      from #162942 , with contributions from @vincentkoc .'
    source_release: https://docs.openclaw.ai/releases/2026.9.8
  - quote: Replies between agents. When an agent asks another for help, the result
      comes back to the requester once. Work inside OpenClaw must return a result
      or keep working instead of ending silently. Custom workflows must handle returned
      results and request follow-up messages explicitly; REPLY_SKIP and ANNOUNCE_SKIP
      no longer hide replies. Doctor updates the old settings , preserving silence
      in group chats. Sources and credits .
    source_release: https://docs.openclaw.ai/releases/2026.9.8
  - quote: Anthropic background work. Fixed cases where an Anthropic conversation
      got stuck or finished before results from background commands, other agents
      or workflows had been collected. Sources and credits .
    source_release: https://docs.openclaw.ai/releases/2026.9.8
  - quote: 'Saved conversations on Windows. Fixed an error that stopped Windows users
      from opening saved conversations or preparing scheduled agent tasks. #162931
      , authored by @RomneyDa , backports #160075 for #157067 and #159339 . It also
      includes the desktop app access fix from #162467 and clearer messages when diagnosing
      workspace recovery.'
    source_release: https://docs.openclaw.ai/releases/2026.9.8
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 4-agent-mode-changes-in-v2026-9-8
  source_release: openclaw-2026-10-03-v2026-9-8-0844d8d3
  source_type: openclaw_changelog
  theme: agent-mode
  title: 4 Agent Mode changes in v2026.9.8
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-10-01-6-agent-mode-changes-in-rust-v0-160-0|6 Agent Mode
  changes in rust-v0.160.0]]'
- '[[Changes/Claude Code/2026-10-02-4-agent-mode-changes-in-v2-1-288|4 Agent Mode
  changes in v2.1.288]]'
- '[[Changes/Devin/2026-10-02-transcript-polish|Transcript Polish]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-10-03-v2026-9-8-0844d8d3|openclaw-2026-10-03-v2026-9-8-0844d8d3]]'
source_type: openclaw_changelog
theme: agent-mode
title: 4 Agent Mode changes in v2026.9.8
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Agent Mode changes in v2026.9.8

**OpenClaw** · 2026-10-03 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.8) · from [[Releases/OpenClaw/openclaw-2026-10-03-v2026-9-8-0844d8d3|v2026.9.8]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Silent-reply help. Help text in 20 existing languages now explains where an agent can stay silent. Silence settings apply to group chats; direct chats and work requested inside OpenClaw require a reply. #163409 , using translations from #162942 , with contributions from @vincentkoc .

> Replies between agents. When an agent asks another for help, the result comes back to the requester once. Work inside OpenClaw must return a result or keep working instead of ending silently. Custom workflows must handle returned results and request follow-up messages explicitly; REPLY_SKIP and ANNOUNCE_SKIP no longer hide replies. Doctor updates the old settings , preserving silence in group chats. Sources and credits .

> Anthropic background work. Fixed cases where an Anthropic conversation got stuck or finished before results from background commands, other agents or workflows had been collected. Sources and credits .

> Saved conversations on Windows. Fixed an error that stopped Windows users from opening saved conversations or preparing scheduled agent tasks. #162931 , authored by @RomneyDa , backports #160075 for #157067 and #159339 . It also includes the desktop app access fix from #162467 and clearer messages when diagnosing workspace recovery.

Source: https://docs.openclaw.ai/releases/2026.9.8
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-10-03-2-mobile-and-desktop-changes-in-v2026-9-8|2 Mobile and Desktop changes in v2026.9.8]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-10-03-9-pricing-model-changes-in-v2026-9-8|9 Pricing Model changes in v2026.9.8]] · Pricing Model
- [[Changes/OpenClaw/2026-10-03-2-model-support-changes-in-v2026-9-8|2 Model Support changes in v2026.9.8]] · Model Support
- [[Changes/OpenClaw/2026-10-03-session-assignment-moving-the-pointer-over-assign-to-and-then-pressing-enter-now|Session assignment]] · Interface Experience
- [[Changes/OpenClaw/2026-10-03-2-memory-and-personalization-changes-in-v2026-9-8|2 Memory and Personalization changes in v2026.9.8]] · Memory and Personalization
- [[Changes/OpenClaw/2026-10-03-2-account-and-access-changes-in-v2026-9-8|2 Account and Access changes in v2026.9.8]] · Account and Access
- [[Changes/OpenClaw/2026-10-03-browser-tabs-after-updates-if-you-leave-openclaw-s-bundled-web-interface-open-du|Browser tabs after updates]] · Editor Experience
- [[Changes/OpenClaw/2026-10-03-3-other-changes-in-v2026-9-8|3 other changes in v2026.9.8]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-10-02 · Devin · [[Changes/Devin/2026-10-02-transcript-polish|Transcript Polish]]
- Later: 2026-10-05 · Claude Code · [[Changes/Claude Code/2026-10-05-added-claude-api-managed-agents-onboard-url-to-set-up-the-managed-agents-pattern|Added /claude-api managed-agents-onboard url to set up the Managed Agents…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-10-03-6d2d0d&body=Card%3A%20Changes%2FOpenClaw%2F2026-10-03-4-agent-mode-changes-in-v2026-9-8.md%0ACard%20ID%3A%20openclaw-2026-10-03-6d2d0d%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.8%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->