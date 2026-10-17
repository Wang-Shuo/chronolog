---
card_id: claude-code-2026-04-04-a0bc10
date: '2026-04-04'
description: 'Claude Code · 2026-04-04 · Enterprise and Administration: Added `forceRemoteSettingsRefresh`
  policy setting: when set, the CLI blocks startup until remote…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2025-06-04-enterprise-users-can-only-access-stable-release-no-pre-release|Enterprise
    users can only access stable release (no pre-release)]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 304
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: enterprise-admin
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: change
machine_hash: 69d4ca492c45c74975d5ce1a24d26bc007e41950f3f8c0f36d0d62f472a0ab71
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-04-04-a0bc10
  comparison: ''
  date: '2026-04-04'
  description: 'Claude Code — v2.1.92: Added `forceRemoteSettingsRefresh` policy setting:
    when set, the CLI blocks startup until remote managed settings are freshly fetched,
    and exits if the fetch fails (fail-closed)'
  evidence:
  - quote: 'Added `forceRemoteSettingsRefresh` policy setting: when set, the CLI blocks
      startup until remote managed settings are freshly fetched, and exits if the
      fetch fails (fail-closed)'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.92
  extractor_version: fallback-v5
  impact: incremental
  kind: change
  product: claude-code
  product_name: Claude Code
  slug: added-forceremotesettingsrefresh-policy-setting-when-set-the-cli-blocks-startup
  source_release: claude-code-2026-04-04-v2-1-92-github-305189904-2eb020f5
  source_type: github_releases
  theme: enterprise-admin
  theme_matches: []
  theme_resolution: manual-backfill-review-v1
  title: Added `forceRemoteSettingsRefresh` policy setting
  type: change
related_changes:
- '[[Changes/ChatGPT/2026-03-17-we-ve-simplified-the-model-picker-to-make-it-easier-to-choose-the-right-level-of-a3fc77|We’ve
  simplified the model picker to make it easier to choose the right level of reasoning]]'
- '[[Changes/Claude Code/2026-03-26-added-allowedchannelplugins-managed-setting-for-team-enterprise-admins-to-define|Added
  allowedChannelPlugins managed setting for team/enterprise admins to define…]]'
- '[[Changes/Cursor/2026-04-02-added-an-enterprise-admin-control-for-disabling-made-with-cursor-code-attributio|Added
  an Enterprise Admin control for disabling "Made with Cursor" code attribution…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-04-04-v2-1-92-github-305189904-2eb020f5|claude-code-2026-04-04-v2-1-92-github-305189904-2eb020f5]]'
source_type: github_releases
theme: enterprise-admin
title: Added forceRemoteSettingsRefresh policy setting
type: change
---

<!-- chronolog:begin region="header" -->
# Added `forceRemoteSettingsRefresh` policy setting

**Claude Code** · 2026-04-04 · [[Themes/enterprise-admin|Enterprise and Administration]] · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.92) · from [[Releases/Claude Code/claude-code-2026-04-04-v2-1-92-github-305189904-2eb020f5|v2.1.92]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `forceRemoteSettingsRefresh` policy setting: when set, the CLI blocks startup until remote managed settings are freshly fetched, and exits if the fetch fails (fail-closed)
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.92
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-04-04-remote-control-session-names-now-use-your-hostname-as-the-default-prefix-e-g-myh|Remote Control session names now use your hostname as the default prefix…]] · Apps and Integrations
- [[Changes/Claude Code/2026-04-04-pro-users-now-see-a-footer-hint-when-returning-to-a-session-after-the-prompt-cac|Pro users now see a footer hint when returning to a session after the prompt cache…]] · Context Window
- [[Changes/Claude Code/2026-04-04-removed-tag-command|Removed /tag command]] · Developer Workflow
- [[Changes/Claude Code/2026-04-04-improved-write-tool-diff-computation-speed-for-large-files-60-faster-on-files-wi|Improved Write tool diff computation speed for large files…]] · Reliability and Performance
- [[Changes/Claude Code/2026-04-04-linux-sandbox-now-ships-the-apply-seccomp-helper-in-both-npm-and-native-builds-r|Linux sandbox now ships the apply-seccomp helper in both npm and native builds…]] · Safety and Privacy
- [[Changes/Claude Code/2026-04-04-release-notes-is-now-an-interactive-version-picker|/release-notes is now an interactive version picker]] · Interface Experience
- [[Changes/Claude Code/2026-04-04-added-interactive-bedrock-setup-wizard-accessible-from-the-login-screen-when-sel|Added interactive Bedrock setup wizard accessible from the login screen…]] · Account and Access
- [[Changes/Claude Code/2026-04-04-removed-vim-command-toggle-vim-mode-via-config-editor-mode|Removed /vim command (toggle vim mode via /config → Editor mode)]] · Editor Experience
- [[Changes/Claude Code/2026-04-04-added-per-model-and-cache-hit-breakdown-to-cost-for-subscription-users|Added per-model and cache-hit breakdown to /cost for subscription users]] · Pricing Model
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Enterprise and Administration

- Earlier: 2026-04-02 · Cursor · [[Changes/Cursor/2026-04-02-added-an-enterprise-admin-control-for-disabling-made-with-cursor-code-attributio|Added an Enterprise Admin control for disabling "Made with Cursor" code attribution…]]
- Later: 2026-04-07 · Claude Code · [[Changes/Claude Code/2026-04-07-changed-default-effort-level-from-medium-to-high-for-api-key-bedrock-vertex-foun|Changed default effort level from medium to high for API-key…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2025-06-04 · Cursor · [[Changes/Cursor/2025-06-04-enterprise-users-can-only-access-stable-release-no-pre-release|Enterprise users can only access stable release (no pre-release)]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-04-04-a0bc10&body=Card%3A%20Changes%2FClaude%20Code%2F2026-04-04-added-forceremotesettingsrefresh-policy-setting-when-set-the-cli-blocks-startup.md%0ACard%20ID%3A%20claude-code-2026-04-04-a0bc10%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.92%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->