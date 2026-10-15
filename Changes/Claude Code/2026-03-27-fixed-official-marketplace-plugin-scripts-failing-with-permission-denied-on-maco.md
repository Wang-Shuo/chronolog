---
card_id: claude-code-2026-03-27-6bd5a2
date: '2026-03-27'
description: 'Claude Code · 2026-03-27 · Safety and Privacy: Fixed official marketplace
  plugin scripts failing with "Permission denied" on macOS/Linux since v2.1.83'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1076
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v4
impact: incremental
machine_hash: 049698717eec5f96218162ba0f4d051cc6c645f9d31acea69ee38d00babf9558
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-03-27-6bd5a2
  comparison: ''
  date: '2026-03-27'
  description: 'Claude Code — v2.1.86: Fixed official marketplace plugin scripts failing
    with "Permission denied" on macOS/Linux since v2.1.83'
  evidence:
  - quote: Fixed official marketplace plugin scripts failing with "Permission denied"
      on macOS/Linux since v2.1.83
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.86
  extractor_version: fallback-v4
  impact: incremental
  product: claude-code
  product_name: Claude Code
  slug: fixed-official-marketplace-plugin-scripts-failing-with-permission-denied-on-maco
  source_release: claude-code-2026-03-27-v2-1-86-github-302569462-d6b30859
  source_type: github_releases
  theme: safety-privacy
  theme_matches:
  - matched_terms:
    - plugin
    score: 50
    theme: apps-integrations
  - matched_terms:
    - macos
    score: 50
    theme: mobile-desktop
  theme_resolution: manual-semantic-rule-v2
  title: Fixed official marketplace plugin scripts failing…
  type: change
related_changes:
- '[[Changes/Claude Code/2026-03-25-added-claude-code-subprocess-env-scrub-1-to-strip-anthropic-and-cloud-provider-c|Added
  CLAUDE_CODE_SUBPROCESS_ENV_SCRUB=1 to strip Anthropic and cloud provider…]]'
- '[[Changes/Claude Code/2026-03-25-added-sandbox-failifunavailable-setting-to-exit-with-an-error-when-sandbox-is-en|Added
  sandbox.failIfUnavailable setting to exit with an error when sandbox…]]'
- '[[Changes/Claude Code/2026-03-26-added-conditional-if-field-for-hooks-using-permission-rule-syntax-e-g-bash-git-t|Added
  conditional if field for hooks using permission rule syntax…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-03-27-v2-1-86-github-302569462-d6b30859|claude-code-2026-03-27-v2-1-86-github-302569462-d6b30859]]'
source_type: github_releases
theme: safety-privacy
title: Fixed official marketplace plugin scripts failing…
type: change
---

<!-- chronolog:begin region="header" -->
# Fixed official marketplace plugin scripts failing…

**Claude Code** · 2026-03-27 · [[Themes/safety-privacy|Safety and Privacy]] · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.86) · from [[Releases/Claude Code/claude-code-2026-03-27-v2-1-86-github-302569462-d6b30859|v2.1.86]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Fixed official marketplace plugin scripts failing with "Permission denied" on macOS/Linux since v2.1.83
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.86
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-03-27-reduced-token-overhead-when-mentioning-files-with-raw-string-content-no-longer-j|Reduced token overhead when mentioning files with @]] · Context Window
- [[Changes/Claude Code/2026-03-27-added-x-claude-code-session-id-header-to-api-requests-so-proxies-can-aggregate-r|Added X-Claude-Code-Session-Id header to API requests so proxies can aggregate…]] · Developer Workflow
- [[Changes/Claude Code/2026-03-27-added-jj-and-sl-to-vcs-directory-exclusion-lists-so-grep-and-file-autocomplete-d|Added .jj and .sl to VCS directory exclusion lists so Grep and file autocomplete…]] · Editor Experience
- [[Changes/Claude Code/2026-03-27-reduced-startup-event-loop-stalls-when-many-claude-ai-mcp-connectors-are-configu|Reduced startup event-loop stalls when many claude.ai MCP connectors are configured…]] · Apps and Integrations
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-03-26 · Claude Code · [[Changes/Claude Code/2026-03-26-added-conditional-if-field-for-hooks-using-permission-rule-syntax-e-g-bash-git-t|Added conditional if field for hooks using permission rule syntax…]]
- Later: 2026-04-01 · Claude Code · [[Changes/Claude Code/2026-04-01-added-husky-to-protected-directories-acceptedits-mode|Added .husky to protected directories (acceptEdits mode)]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-03-27-6bd5a2&body=Card%3A%20Changes%2FClaude%20Code%2F2026-03-27-fixed-official-marketplace-plugin-scripts-failing-with-permission-denied-on-maco.md%0ACard%20ID%3A%20claude-code-2026-03-27-6bd5a2%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.86%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->