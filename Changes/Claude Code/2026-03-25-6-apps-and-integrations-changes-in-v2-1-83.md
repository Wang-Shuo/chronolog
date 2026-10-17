---
card_id: claude-code-2026-03-25-bcdc49
date: '2026-03-25'
description: 'Claude Code · 2026-03-25 · Apps and Integrations: 6 changes in v2.1.83
  — Added `CwdChanged` and `FileChanged` hook events for reactive environment management…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1098
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 94b6e92407ff57693f80c6eb463091f9f663421da3795e61fb31532cd7ee0c7c
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-03-25-bcdc49
  comparison: ''
  date: '2026-03-25'
  description: 'Claude Code — v2.1.83: 6 Apps and Integrations changes'
  evidence:
  - quote: Added `CwdChanged` and `FileChanged` hook events for reactive environment
      management (e.g., direnv)
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.83
  - quote: Added `disableDeepLinkRegistration` setting to prevent `claude-cli://`
      protocol handler registration
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.83
  - quote: Improved plugin startup — commands, skills, and agents now load from disk
      cache without re-fetching
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.83
  - quote: 'Improved Remote Control session titles: AI-generated titles now appear
      within seconds of the first message'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.83
  - quote: Faster `claude -p` startup with unauthenticated HTTP/SSE MCP servers (~600ms
      saved)
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.83
  - quote: Plugin MCP servers that duplicate an org-managed connector are now suppressed
      instead of running a second connection
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.83
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 6-apps-and-integrations-changes-in-v2-1-83
  source_release: claude-code-2026-03-25-v2-1-83-github-301019202-ba6a8317
  source_type: github_releases
  theme: apps-integrations
  title: 6 Apps and Integrations changes in v2.1.83
  type: change
related_changes:
- '[[Changes/Claude Code/2026-03-19-4-apps-and-integrations-changes-in-v2-1-80|4 Apps
  and Integrations changes in v2.1.80]]'
- '[[Changes/Claude Code/2026-03-20-3-apps-and-integrations-changes-in-v2-1-81|3 Apps
  and Integrations changes in v2.1.81]]'
- '[[Changes/ChatGPT/2026-03-25-google-s-file-connectors-in-chatgpt-are-now-unified-under-google-drive-providing|Google
  Drive app unification]]'
source_release: '[[Releases/Claude Code/claude-code-2026-03-25-v2-1-83-github-301019202-ba6a8317|claude-code-2026-03-25-v2-1-83-github-301019202-ba6a8317]]'
source_type: github_releases
theme: apps-integrations
title: 6 Apps and Integrations changes in v2.1.83
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Apps and Integrations changes in v2.1.83

**Claude Code** · 2026-03-25 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.83) · from [[Releases/Claude Code/claude-code-2026-03-25-v2-1-83-github-301019202-ba6a8317|v2.1.83]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added `CwdChanged` and `FileChanged` hook events for reactive environment management (e.g., direnv)

> Added `disableDeepLinkRegistration` setting to prevent `claude-cli://` protocol handler registration

> Improved plugin startup — commands, skills, and agents now load from disk cache without re-fetching

> Improved Remote Control session titles: AI-generated titles now appear within seconds of the first message

> Faster `claude -p` startup with unauthenticated HTTP/SSE MCP servers (~600ms saved)

> Plugin MCP servers that duplicate an org-managed connector are now suppressed instead of running a second connection

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.83
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-03-25-agents-can-now-declare-initialprompt-in-frontmatter-to-auto-submit-a-first-turn|Agents can now declare initialPrompt in frontmatter to auto-submit a first turn]] · Agent Mode
- [[Changes/Claude Code/2026-03-25-2-interface-experience-changes-in-v2-1-83|2 Interface Experience changes in v2.1.83]] · Interface Experience
- [[Changes/Claude Code/2026-03-25-3-editor-experience-changes-in-v2-1-83|3 Editor Experience changes in v2.1.83]] · Editor Experience
- [[Changes/Claude Code/2026-03-25-3-reliability-and-performance-changes-in-v2-1-83|3 Reliability and Performance changes in v2.1.83]] · Reliability and Performance
- [[Changes/Claude Code/2026-03-25-2-safety-and-privacy-changes-in-v2-1-83|2 Safety and Privacy changes in v2.1.83]] · Safety and Privacy
- [[Changes/Claude Code/2026-03-25-added-managed-settings-d-drop-in-directory-alongside-managed-settings-json-letti|Added managed-settings.d/ drop-in directory alongside managed-settings.json…]] · Collaboration
- [[Changes/Claude Code/2026-03-25-9-other-changes-in-v2-1-83|9 other changes in v2.1.83]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-03-25 · ChatGPT · [[Changes/ChatGPT/2026-03-25-google-s-file-connectors-in-chatgpt-are-now-unified-under-google-drive-providing|Google Drive app unification]]
- Later: 2026-03-26 · Claude Code · [[Changes/Claude Code/2026-03-26-5-apps-and-integrations-changes-in-v2-1-84|5 Apps and Integrations changes in v2.1.84]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-03-25-bcdc49&body=Card%3A%20Changes%2FClaude%20Code%2F2026-03-25-6-apps-and-integrations-changes-in-v2-1-83.md%0ACard%20ID%3A%20claude-code-2026-03-25-bcdc49%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.83%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->