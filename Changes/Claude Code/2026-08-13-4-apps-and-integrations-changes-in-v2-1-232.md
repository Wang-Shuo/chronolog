---
card_id: claude-code-2026-08-13-3f24b5
date: '2026-08-13'
description: 'Claude Code · 2026-08-13 · Apps and Integrations: 4 changes in v2.1.232
  — Added GitLab support to plugin marketplaces: bare `gitlab.com` repo URLs (including…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1239
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: bd83f675d4eaba3dfaa85ef2b9b0bd742124c6eda95d9e1e183b9da302f9b66a
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-08-13-3f24b5
  comparison: ''
  date: '2026-08-13'
  description: 'Claude Code — v2.1.232: 4 Apps and Integrations changes'
  evidence:
  - quote: 'Added GitLab support to plugin marketplaces: bare `gitlab.com` repo URLs
      (including nested subgroups) now clone like `github.com` URLs, and clone auth-failure
      hints name your actual git host'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.232
  - quote: '`/plugin install plugin@marketplace` now refreshes the marketplace first,
      so newly published plugins install without a manual marketplace update'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.232
  - quote: Remote Control now keeps reconnecting for about 30 minutes after a network
      blip and no longer drops after a few blips spread across an hour
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.232
  - quote: 'Remote Control: resuming a conversation no longer silently takes Remote
      Control away from another Claude Code on the same machine that still has it;
      run `/remote-control` there to move it'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.232
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 4-apps-and-integrations-changes-in-v2-1-232
  source_release: claude-code-2026-08-13-v2-1-232-github-370225682-71e478db
  source_type: github_releases
  theme: apps-integrations
  title: 4 Apps and Integrations changes in v2.1.232
  type: change
related_changes:
- '[[Changes/Claude Code/2026-08-08-3-apps-and-integrations-changes-in-v2-1-225|3
  Apps and Integrations changes in v2.1.225]]'
- '[[Changes/Claude Code/2026-08-11-2-apps-and-integrations-changes-in-v2-1-228|2
  Apps and Integrations changes in v2.1.228]]'
- '[[Changes/Claude Code/2026-08-12-3-apps-and-integrations-changes-in-v2-1-229|3
  Apps and Integrations changes in v2.1.229]]'
source_release: '[[Releases/Claude Code/claude-code-2026-08-13-v2-1-232-github-370225682-71e478db|claude-code-2026-08-13-v2-1-232-github-370225682-71e478db]]'
source_type: github_releases
theme: apps-integrations
title: 4 Apps and Integrations changes in v2.1.232
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Apps and Integrations changes in v2.1.232

**Claude Code** · 2026-08-13 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.232) · from [[Releases/Claude Code/claude-code-2026-08-13-v2-1-232-github-370225682-71e478db|v2.1.232]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added GitLab support to plugin marketplaces: bare `gitlab.com` repo URLs (including nested subgroups) now clone like `github.com` URLs, and clone auth-failure hints name your actual git host

> `/plugin install plugin@marketplace` now refreshes the marketplace first, so newly published plugins install without a manual marketplace update

> Remote Control now keeps reconnecting for about 30 minutes after a network blip and no longer drops after a few blips spread across an hour

> Remote Control: resuming a conversation no longer silently takes Remote Control away from another Claude Code on the same machine that still has it; run `/remote-control` there to move it

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.232
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-08-13-enterprise-policy-a-url-typed-blockedmarketplaces-entry-for-a-bare-repo-url-keep|Enterprise policy: a url-typed blockedMarketplaces entry for a bare repo URL keeps…]] · Enterprise and Administration
- [[Changes/Claude Code/2026-08-13-improved-fullscreen-streaming-long-sessions-stay-responsive-because-the-whole-co|Improved fullscreen streaming]] · Interface Experience
- [[Changes/Claude Code/2026-08-13-4-agent-mode-changes-in-v2-1-232|4 Agent Mode changes in v2.1.232]] · Agent Mode
- [[Changes/Claude Code/2026-08-13-remote-control-resuming-a-conversation-whose-session-was-deleted-from-claude-ai|Remote Control: resuming a conversation whose session was deleted from claude.ai…]] · Account and Access
- [[Changes/Claude Code/2026-08-13-cowork-sessions-no-longer-inline-external-imports-from-user-scope-memory-files|Cowork sessions no longer inline external @-imports from user-scope memory files]] · Memory and Personalization
- [[Changes/Claude Code/2026-08-13-hardened-the-auto-generated-cross-session-messaging-socket-directory-on-shared-t|Hardened the auto-generated cross-session messaging socket directory on shared /tmp]] · Collaboration
- [[Changes/Claude Code/2026-08-13-gateway-the-desktop-overlay-now-accepts-every-released-desktop-setting-was-11-ha|Gateway: the desktop: overlay now accepts every released Desktop setting…]] · Mobile and Desktop
- [[Changes/Claude Code/2026-08-13-subagent-forking-is-now-on-by-default-a-subagent-type-fork-subagent-inherits-the|Subagent forking is now on by default]] · Agent Mode
- [[Changes/Claude Code/2026-08-13-9-safety-and-privacy-changes-in-v2-1-232|9 Safety and Privacy changes in v2.1.232]] · Safety and Privacy
- [[Changes/Claude Code/2026-08-13-remote-control-the-terminal-now-says-whether-a-session-was-taken-over-by-another|Remote Control: the terminal now says whether a session was taken over by another…]] · Developer Workflow
- [[Changes/Claude Code/2026-08-13-pasted-and-clipboard-images-are-read-without-blocking-the-event-loop|Pasted and clipboard images are read without blocking the event loop]] · Automation and Scheduling
- [[Changes/Claude Code/2026-08-13-added-config-rows-for-dialog-expiry-and-messages-from-your-other-sessions-cross|Added /config rows…]] · Other changes
- [[Changes/Claude Code/2026-08-13-5-other-changes-in-v2-1-232|5 other changes in v2.1.232]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-08-12 · Claude Code · [[Changes/Claude Code/2026-08-12-3-apps-and-integrations-changes-in-v2-1-229|3 Apps and Integrations changes in v2.1.229]]
- Later: 2026-08-14 · Claude Code · [[Changes/Claude Code/2026-08-14-2-apps-and-integrations-changes-in-v2-1-233|2 Apps and Integrations changes in v2.1.233]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-08-13-3f24b5&body=Card%3A%20Changes%2FClaude%20Code%2F2026-08-13-4-apps-and-integrations-changes-in-v2-1-232.md%0ACard%20ID%3A%20claude-code-2026-08-13-3f24b5%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.232%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->