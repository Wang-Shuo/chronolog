---
card_id: windsurf-2026-08-10-9837fc
date: '2026-08-10'
description: 'Windsurf · 2026-08-10 · Interface Experience: Devin Local conversations
  can be shared: **Share Conversation** uploads a sanitized transcript (system prompts…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-04-14-descript-s-sidebar-now-has-an-economical-collapsed-state|Collapsed
    Sidebar]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2675
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: interface-experience
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: launch
machine_hash: c31e9ab9fa46c1af893ae64f7e6ba7d1e4ffc1cd278b41bf0e94886c3ec30f32
product: windsurf
product_name: Windsurf
record:
  card_id: windsurf-2026-08-10-9837fc
  comparison: ''
  date: '2026-08-10'
  description: 'Windsurf — v3.7.16: Devin Local conversations can be shared: **Share
    Conversation** uploads a sanitized transcript (system prompts and tool definitions
    dropped, secrets redacted, paths normalized) and copies a team-visible link. Share
    directly from the actions menu below a completed turn.'
  evidence:
  - quote: 'Devin Local conversations can be shared: **Share Conversation** uploads
      a sanitized transcript (system prompts and tool definitions dropped, secrets
      redacted, paths normalized) and copies a team-visible link. Share directly from
      the actions menu below a completed turn.'
    source_release: https://docs.devin.ai/desktop/changelog#v3-7-16
  - quote: 'Reverting is reliable mid-turn: revert buttons appear as soon as a prompt
      is sent and reverting while the agent is working cancels the turn first.'
    source_release: https://docs.devin.ai/desktop/changelog#v3-7-16
  - quote: The Customizations panel has search across every section (skills, subagents,
      rules, hooks, plugins, MCP servers), a new **Subagents** section, a refresh
      action for plugins, and an info indicator explaining why an enterprise-required
      plugin can't be removed.
    source_release: https://docs.devin.ai/desktop/changelog#v3-7-16
  - quote: Plugins installed from Customizations are added to your personal plugins
      by default, so they are available in Devin Cloud and on your other devices;
      choose **Install locally** for a device-only install.
    source_release: https://docs.devin.ai/desktop/changelog#v3-7-16
  - quote: Permission rules from different levels (enterprise, mode, user, project,
      subagent) now compose predictably — an explicit `deny:` always wins, "always
      allow" options only appear when the grant would actually take effect, and denials
      say which layer denied them.
    source_release: https://docs.devin.ai/desktop/changelog#v3-7-16
  - quote: Ensured `sudo` password prompts can't hang a command.
    source_release: https://docs.devin.ai/desktop/changelog#v3-7-16
  - quote: 'Separate each MCP server''s logs into its own `MCP: <server>` output channel.'
    source_release: https://docs.devin.ai/desktop/changelog#v3-7-16
  - quote: Large-file reads through ACP are bounded and paginated instead of repeatedly
      rereading overflow files. Late terminal flushes now preserve complete output
      and cannot reopen completed command cards.
    source_release: https://docs.devin.ai/desktop/changelog#v3-7-16
  extractor_version: fallback-v5
  impact: incremental
  kind: launch
  product: windsurf
  product_name: Windsurf
  slug: devin-local
  source_release: windsurf-2026-08-10-v3-7-16-bb404410
  source_type: windsurf_changelog
  theme: interface-experience
  title: Devin Local
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-08-10-2-interface-experience-changes-in-v1-0-79|2
  Interface Experience changes in v1.0.79]]'
- '[[Changes/OpenCode/2026-08-10-open-the-project-menu-with-a-right-click-in-home|Open
  the project menu with a right-click in Home]]'
- '[[Changes/OpenCode/2026-08-10-desktop-fall-back-to-listing-and-matching-local-directories-when-the-project-pic|Desktop
  Fall back to listing and matching local directories when the project picker…]]'
source_release: '[[Releases/Windsurf/windsurf-2026-08-10-v3-7-16-bb404410|windsurf-2026-08-10-v3-7-16-bb404410]]'
source_type: windsurf_changelog
theme: interface-experience
title: Devin Local
type: change
---

<!-- chronolog:begin region="header" -->
# Devin Local

**Windsurf** · 2026-08-10 · [[Themes/interface-experience|Interface Experience]] · Launch · [Official source](https://docs.devin.ai/desktop/changelog#v3-7-16) · from [[Releases/Windsurf/windsurf-2026-08-10-v3-7-16-bb404410|v3.7.16]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Devin Local conversations can be shared: **Share Conversation** uploads a sanitized transcript (system prompts and tool definitions dropped, secrets redacted, paths normalized) and copies a team-visible link. Share directly from the actions menu below a completed turn.
>
> Reverting is reliable mid-turn: revert buttons appear as soon as a prompt is sent and reverting while the agent is working cancels the turn first.
>
> The Customizations panel has search across every section (skills, subagents, rules, hooks, plugins, MCP servers), a new **Subagents** section, a refresh action for plugins, and an info indicator explaining why an enterprise-required plugin can't be removed.
>
> Plugins installed from Customizations are added to your personal plugins by default, so they are available in Devin Cloud and on your other devices; choose **Install locally** for a device-only install.
>
> Permission rules from different levels (enterprise, mode, user, project, subagent) now compose predictably — an explicit `deny:` always wins, "always allow" options only appear when the grant would actually take effect, and denials say which layer denied them.
>
> Ensured `sudo` password prompts can't hang a command.
>
> Separate each MCP server's logs into its own `MCP: <server>` output channel.
>
> Large-file reads through ACP are bounded and paginated instead of repeatedly rereading overflow files. Late terminal flushes now preserve complete output and cannot reopen completed command cards.
>
> Source: https://docs.devin.ai/desktop/changelog#v3-7-16
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Windsurf/2026-08-10-devin-cloud|Devin Cloud]] · Pricing Model
- [[Changes/Windsurf/2026-08-10-devin-desktop|Devin Desktop]] · Mobile and Desktop
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Interface Experience

- Earlier: 2026-08-10 · OpenCode · [[Changes/OpenCode/2026-08-10-desktop-fall-back-to-listing-and-matching-local-directories-when-the-project-pic|Desktop Fall back to listing and matching local directories when the project picker…]]
- Later: 2026-08-11 · Claude Code · [[Changes/Claude Code/2026-08-11-updated-terminal-title-busy-spinner-glyphs-to-reduce-tab-bar-jitter-on-some-term|Updated terminal title busy-spinner glyphs to reduce tab-bar jitter on some terminals]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-04-14 · Descript · [[Changes/Descript/2019-04-14-descript-s-sidebar-now-has-an-economical-collapsed-state|Collapsed Sidebar]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20windsurf-2026-08-10-9837fc&body=Card%3A%20Changes%2FWindsurf%2F2026-08-10-devin-local.md%0ACard%20ID%3A%20windsurf-2026-08-10-9837fc%0ASource%3A%20https%3A%2F%2Fdocs.devin.ai%2Fdesktop%2Fchangelog%23v3-7-16%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->