---
card_id: claude-code-2026-05-27-40bef7
date: '2026-05-27'
description: 'Claude Code · 2026-05-27 · Apps and Integrations: 4 changes in v2.1.152
  — `SessionStart` hooks can now return `reloadSkills: true` to re-scan skill…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If
    you have a recording with each speaker with a different microphone, or saved…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2721
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: a85831ba82501bc8b85e155434f7d79ac880f2cf02763f9c220d364d467a585a
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
- '[[Changes/ElevenLabs/2026-05-25-sdk-releases|SDK Releases]]'
- '[[Changes/Lovable/2026-05-25-custom-mcp-servers-available-on-all-plans|Custom MCP
  servers available on all plans]]'
- '[[Changes/Codex CLI/2026-05-26-11-apps-and-integrations-changes-in-rust-v0-134-0|11
  Apps and Integrations changes in rust-v0.134.0]]'
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

- Earlier: 2026-05-26 · Codex CLI · [[Changes/Codex CLI/2026-05-26-11-apps-and-integrations-changes-in-rust-v0-134-0|11 Apps and Integrations changes in rust-v0.134.0]]
- Later: 2026-05-27 · Gemini CLI · [[Changes/Gemini CLI/2026-05-27-docs-extensions-clarify-env-var-sanitization-policy-for-mcp-and-ext-by-galz10-in|docs(extensions): clarify env var sanitization policy for MCP and ext…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-12-14 · Descript · [[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If you have a recording with each speaker with a different microphone, or saved…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-05-27-40bef7&body=Card%3A%20Changes%2FClaude%20Code%2F2026-05-27-4-apps-and-integrations-changes-in-v2-1-152.md%0ACard%20ID%3A%20claude-code-2026-05-27-40bef7%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.152%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->