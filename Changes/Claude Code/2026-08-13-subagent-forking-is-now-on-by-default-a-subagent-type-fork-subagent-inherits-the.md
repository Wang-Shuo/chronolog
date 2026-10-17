---
card_id: claude-code-2026-08-13-bbdff3
date: '2026-08-13'
description: 'Claude Code · 2026-08-13 · Agent Mode: Subagent forking is now on by
  default: a `subagent_type: "fork"` subagent inherits the full conversation and prompt…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1134
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: paradigm-shift
kind: change
machine_hash: 7fe84d3e7aa20b83948644ef4488078892283dfe1fa50b46e8983ea0efd0d9dc
product: claude-code
product_name: Claude Code
record:
  ai_generated: true
  card_id: claude-code-2026-08-13-bbdff3
  comparison: ''
  confidence: low
  date: '2026-08-13'
  description: 'Claude Code — v2.1.232: Subagent forking is now on by default: a `subagent_type:
    "fork"` subagent inherits the full conversation and prompt cache, and non-teammate
    agent spawns in interactive sessions now run in the background by default'
  evidence:
  - quote: 'Subagent forking is now on by default: a `subagent_type: "fork"` subagent
      inherits the full conversation and prompt cache, and non-teammate agent spawns
      in interactive sessions now run in the background by default'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.232
  extractor_version: fallback-v5
  impact: paradigm-shift
  kind: change
  product: claude-code
  product_name: Claude Code
  slug: subagent-forking-is-now-on-by-default-a-subagent-type-fork-subagent-inherits-the
  source_release: claude-code-2026-08-13-v2-1-232-github-370225682-71e478db
  source_type: github_releases
  theme: agent-mode
  title: Subagent forking is now on by default
  type: change
related_changes:
- '[[Changes/Claude Code/2026-08-07-removed-the-200-subagent-per-session-spawn-cap-long-running-sessions-no-longer-r|Removed
  the 200-subagent-per-session spawn cap]]'
- '[[Changes/Claude Code/2026-08-12-improved-workflow-fan-outs-to-stagger-same-prefix-sibling-agents-so-subsequent-a|Improved
  workflow fan-outs to stagger same-prefix sibling agents so subsequent…]]'
- '[[Changes/Claude Code/2026-08-13-4-agent-mode-changes-in-v2-1-232|4 Agent Mode
  changes in v2.1.232]]'
source_release: '[[Releases/Claude Code/claude-code-2026-08-13-v2-1-232-github-370225682-71e478db|claude-code-2026-08-13-v2-1-232-github-370225682-71e478db]]'
source_type: github_releases
theme: agent-mode
title: Subagent forking is now on by default
type: change
---

<!-- chronolog:begin region="header" -->
# Subagent forking is now on by default

**Claude Code** · 2026-08-13 · [[Themes/agent-mode|Agent Mode]] · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.232) · from [[Releases/Claude Code/claude-code-2026-08-13-v2-1-232-github-370225682-71e478db|v2.1.232]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Subagent forking is now on by default: a `subagent_type: "fork"` subagent inherits the full conversation and prompt cache, and non-teammate agent spawns in interactive sessions now run in the background by default
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.232
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-08-13-enterprise-policy-a-url-typed-blockedmarketplaces-entry-for-a-bare-repo-url-keep|Enterprise policy: a url-typed blockedMarketplaces entry for a bare repo URL keeps…]] · Enterprise and Administration
- [[Changes/Claude Code/2026-08-13-4-apps-and-integrations-changes-in-v2-1-232|4 Apps and Integrations changes in v2.1.232]] · Apps and Integrations
- [[Changes/Claude Code/2026-08-13-improved-fullscreen-streaming-long-sessions-stay-responsive-because-the-whole-co|Improved fullscreen streaming]] · Interface Experience
- [[Changes/Claude Code/2026-08-13-4-agent-mode-changes-in-v2-1-232|4 Agent Mode changes in v2.1.232]] · Agent Mode
- [[Changes/Claude Code/2026-08-13-remote-control-resuming-a-conversation-whose-session-was-deleted-from-claude-ai|Remote Control: resuming a conversation whose session was deleted from claude.ai…]] · Account and Access
- [[Changes/Claude Code/2026-08-13-cowork-sessions-no-longer-inline-external-imports-from-user-scope-memory-files|Cowork sessions no longer inline external @-imports from user-scope memory files]] · Memory and Personalization
- [[Changes/Claude Code/2026-08-13-hardened-the-auto-generated-cross-session-messaging-socket-directory-on-shared-t|Hardened the auto-generated cross-session messaging socket directory on shared /tmp]] · Collaboration
- [[Changes/Claude Code/2026-08-13-gateway-the-desktop-overlay-now-accepts-every-released-desktop-setting-was-11-ha|Gateway: the desktop: overlay now accepts every released Desktop setting…]] · Mobile and Desktop
- [[Changes/Claude Code/2026-08-13-9-safety-and-privacy-changes-in-v2-1-232|9 Safety and Privacy changes in v2.1.232]] · Safety and Privacy
- [[Changes/Claude Code/2026-08-13-remote-control-the-terminal-now-says-whether-a-session-was-taken-over-by-another|Remote Control: the terminal now says whether a session was taken over by another…]] · Developer Workflow
- [[Changes/Claude Code/2026-08-13-pasted-and-clipboard-images-are-read-without-blocking-the-event-loop|Pasted and clipboard images are read without blocking the event loop]] · Automation and Scheduling
- [[Changes/Claude Code/2026-08-13-added-config-rows-for-dialog-expiry-and-messages-from-your-other-sessions-cross|Added /config rows…]] · Other changes
- [[Changes/Claude Code/2026-08-13-5-other-changes-in-v2-1-232|5 other changes in v2.1.232]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-08-12 · Claude Code · [[Changes/Claude Code/2026-08-12-improved-workflow-fan-outs-to-stagger-same-prefix-sibling-agents-so-subsequent-a|Improved workflow fan-outs to stagger same-prefix sibling agents so subsequent…]]
- Later: 2026-08-13 · Cursor · [[Changes/Cursor/2026-08-13-2-agent-mode-changes-in-08-13-26|2 Agent Mode changes in 08.13.26]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-08-13-bbdff3&body=Card%3A%20Changes%2FClaude%20Code%2F2026-08-13-subagent-forking-is-now-on-by-default-a-subagent-type-fork-subagent-inherits-the.md%0ACard%20ID%3A%20claude-code-2026-08-13-bbdff3%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.232%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->