---
card_id: claude-code-2026-03-25-502a32
date: '2026-03-25'
description: 'Claude Code · 2026-03-25 · Safety and Privacy: Added `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB=1`
  to strip Anthropic and cloud provider credentials from subprocess…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1074
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v4
impact: incremental
machine_hash: ae9986cb7a6fb7294d39797a0f9b4f9b5d07ca64d0d5c710d99eb6176a3e0e83
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-03-25-502a32
  comparison: ''
  date: '2026-03-25'
  description: 'Claude Code — v2.1.83: Added `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB=1`
    to strip Anthropic and cloud provider credentials from subprocess environments
    (Bash tool, hooks, MCP stdio servers)'
  evidence:
  - quote: Added `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB=1` to strip Anthropic and cloud
      provider credentials from subprocess environments (Bash tool, hooks, MCP stdio
      servers)
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.83
  extractor_version: fallback-v4
  impact: incremental
  product: claude-code
  product_name: Claude Code
  slug: added-claude-code-subprocess-env-scrub-1-to-strip-anthropic-and-cloud-provider-c
  source_release: claude-code-2026-03-25-v2-1-83-github-301019202-ba6a8317
  source_type: github_releases
  theme: safety-privacy
  theme_matches: []
  theme_resolution: manual-backfill-review-v1
  title: Added `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB=1` to strip Anthropic and cloud provider…
  type: change
related_changes:
- '[[Changes/Claude Code/2026-03-18-fixed-custom-status-line-showing-nothing-when-workspace-trust-is-blocking-it|Fixed
  custom status line showing nothing when workspace trust is blocking it]]'
- '[[Changes/Claude Code/2026-03-20-added-channels-permission-relay-channel-servers-that-declare-the-permission-capa|Added
  --channels permission relay]]'
- '[[Changes/Claude Code/2026-03-20-fixed-unnecessary-permission-prompts-for-bash-commands-containing-dashes-in-stri|Fixed
  unnecessary permission prompts for Bash commands containing dashes in strings]]'
source_release: '[[Releases/Claude Code/claude-code-2026-03-25-v2-1-83-github-301019202-ba6a8317|claude-code-2026-03-25-v2-1-83-github-301019202-ba6a8317]]'
source_type: github_releases
theme: safety-privacy
title: Added CLAUDE_CODE_SUBPROCESS_ENV_SCRUB=1 to strip Anthropic and cloud provider…
type: change
---

<!-- chronolog:begin region="header" -->
# Added `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB=1` to strip Anthropic and cloud provider…

**Claude Code** · 2026-03-25 · [[Themes/safety-privacy|Safety and Privacy]] · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.83) · from [[Releases/Claude Code/claude-code-2026-03-25-v2-1-83-github-301019202-ba6a8317|v2.1.83]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB=1` to strip Anthropic and cloud provider credentials from subprocess environments (Bash tool, hooks, MCP stdio servers)
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.83
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-03-25-added-sandbox-failifunavailable-setting-to-exit-with-an-error-when-sandbox-is-en|Added sandbox.failIfUnavailable setting to exit with an error when sandbox…]] · Safety and Privacy
- [[Changes/Claude Code/2026-03-25-added-disabledeeplinkregistration-setting-to-prevent-claude-cli-protocol-handler|Added disableDeepLinkRegistration setting to prevent claude-cli:// protocol…]] · Apps and Integrations
- [[Changes/Claude Code/2026-03-25-added-managed-settings-d-drop-in-directory-alongside-managed-settings-json-letti|Added managed-settings.d/ drop-in directory alongside managed-settings.json…]] · Collaboration
- [[Changes/Claude Code/2026-03-25-added-cwdchanged-and-filechanged-hook-events-for-reactive-environment-management|Added CwdChanged and FileChanged hook events for reactive environment management…]] · Apps and Integrations
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-03-20 · Claude Code · [[Changes/Claude Code/2026-03-20-fixed-unnecessary-permission-prompts-for-bash-commands-containing-dashes-in-stri|Fixed unnecessary permission prompts for Bash commands containing dashes in strings]]
- Later: 2026-03-26 · Claude Code · [[Changes/Claude Code/2026-03-26-added-conditional-if-field-for-hooks-using-permission-rule-syntax-e-g-bash-git-t|Added conditional if field for hooks using permission rule syntax…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-03-25-502a32&body=Card%3A%20Changes%2FClaude%20Code%2F2026-03-25-added-claude-code-subprocess-env-scrub-1-to-strip-anthropic-and-cloud-provider-c.md%0ACard%20ID%3A%20claude-code-2026-03-25-502a32%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.83%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->