---
card_id: claude-code-2026-05-27-40bef7
date: '2026-05-27'
description: 'Claude Code · 2026-05-27 · Apps and Integrations: 4 changes in v2.1.152
  — `SessionStart` hooks can now return `reloadSkills: true` to re-scan skill…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1161
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: f7ec83fc8c27fcbc3d2571615fa3ef58ac8a2b8a75712471d7adf93defb705fd
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-05-27-40bef7
  comparison: ''
  date: '2026-05-27'
  description: 'Claude Code — v2.1.152: 4 Apps and Integrations changes'
  evidence:
  - quote: '`SessionStart` hooks can now return `reloadSkills: true` to re-scan skill
      directories, making skills installed by the hook available in the same session'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.152
  - quote: '`SessionStart` hooks can now set the session title via `hookSpecificOutput.sessionTitle`
      on startup and resume'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.152
  - quote: Added a `MessageDisplay` hook event that lets hooks transform or hide assistant
      message text as it is displayed
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.152
  - quote: '`claude plugin marketplace remove` now accepts `--scope user|project|local`
      for symmetry with `marketplace add`, `install`, and `uninstall`'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.152
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 4-apps-and-integrations-changes-in-v2-1-152
  source_release: claude-code-2026-05-27-v2-1-152-github-329718732-e62ea850
  source_type: github_releases
  theme: apps-integrations
  title: 4 Apps and Integrations changes in v2.1.152
  type: change
related_changes:
- '[[Changes/Cursor/2026-05-19-cursor-is-now-available-in-jira|Cursor is now available
  in Jira]]'
- '[[Changes/Cursor/2026-05-19-install-the-integration-from-cursor-integrations-you-need-cursor-admin-access-an|Install
  the integration from Cursor integrations]]'
- '[[Changes/Claude Code/2026-05-22-2-apps-and-integrations-changes-in-v2-1-149|2
  Apps and Integrations changes in v2.1.149]]'
source_release: '[[Releases/Claude Code/claude-code-2026-05-27-v2-1-152-github-329718732-e62ea850|claude-code-2026-05-27-v2-1-152-github-329718732-e62ea850]]'
source_type: github_releases
theme: apps-integrations
title: 4 Apps and Integrations changes in v2.1.152
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Apps and Integrations changes in v2.1.152

**Claude Code** · 2026-05-27 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.152) · from [[Releases/Claude Code/claude-code-2026-05-27-v2-1-152-github-329718732-e62ea850|v2.1.152]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> `SessionStart` hooks can now return `reloadSkills: true` to re-scan skill directories, making skills installed by the hook available in the same session

> `SessionStart` hooks can now set the session title via `hookSpecificOutput.sessionTitle` on startup and resume

> Added a `MessageDisplay` hook event that lets hooks transform or hide assistant message text as it is displayed

> `claude plugin marketplace remove` now accepts `--scope user|project|local` for symmetry with `marketplace add`, `install`, and `uninstall`

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.152
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-05-27-in-fullscreen-mode-the-thinking-for-ns-indicator-now-counts-up-live-while-the-mo|In fullscreen mode, the "Thinking for Ns" indicator now counts up live…]] · Interface Experience
- [[Changes/Claude Code/2026-05-27-added-pluginsuggestionmarketplaces-managed-setting-admins-can-allowlist-org-mark|Added pluginSuggestionMarketplaces managed setting]] · Context Window
- [[Changes/Claude Code/2026-05-27-2-agent-mode-changes-in-v2-1-152|2 Agent Mode changes in v2.1.152]] · Agent Mode
- [[Changes/Claude Code/2026-05-27-2-model-support-changes-in-v2-1-152|2 Model Support changes in v2.1.152]] · Model Support
- [[Changes/Claude Code/2026-05-27-2-developer-workflow-changes-in-v2-1-152|2 Developer Workflow changes in v2.1.152]] · Developer Workflow
- [[Changes/Claude Code/2026-05-27-added-reload-skills-command-to-re-scan-skill-directories-without-restarting-the|Added /reload-skills command to re-scan skill directories without restarting the session]] · Developer Workflow
- [[Changes/Claude Code/2026-05-27-2-safety-and-privacy-changes-in-v2-1-152|2 Safety and Privacy changes in v2.1.152]] · Safety and Privacy
- [[Changes/Claude Code/2026-05-27-the-usage-breakdown-now-includes-large-session-files-files-are-scanned-with-a-st|The /usage breakdown now includes large session files]] · Reliability and Performance
- [[Changes/Claude Code/2026-05-27-2-other-changes-in-v2-1-152|2 other changes in v2.1.152]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-05-22 · Claude Code · [[Changes/Claude Code/2026-05-22-2-apps-and-integrations-changes-in-v2-1-149|2 Apps and Integrations changes in v2.1.149]]
- Later: 2026-05-28 · Claude Code · [[Changes/Claude Code/2026-05-28-2-apps-and-integrations-changes-in-v2-1-153|2 Apps and Integrations changes in v2.1.153]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-05-27-40bef7&body=Card%3A%20Changes%2FClaude%20Code%2F2026-05-27-4-apps-and-integrations-changes-in-v2-1-152.md%0ACard%20ID%3A%20claude-code-2026-05-27-40bef7%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.152%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->