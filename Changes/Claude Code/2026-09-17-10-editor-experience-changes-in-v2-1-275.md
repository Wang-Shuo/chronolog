---
card_id: claude-code-2026-09-17-3dd1b0
date: '2026-09-17'
description: 'Claude Code · 2026-09-17 · Editor Experience: 10 changes in v2.1.275
  — Improved artifact publish results: they name the tab icon sent, warn when the
  page…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-14-3-editor-experience-changes-in-0-0-37|3
    Editor Experience changes in 0.0.37]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1283
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: editor-experience
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: c315ea0874cfcd3c249012b9239374bb85814bb80a0179861a7dd0b88f471600
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-09-17-3dd1b0
  comparison: ''
  date: '2026-09-17'
  description: 'Claude Code — v2.1.275: 10 Editor Experience changes'
  evidence:
  - quote: 'Improved artifact publish results: they name the tab icon sent, warn when
      the page contains a NUL byte, and retry a flaky fetch of the newer page to merge
      after a stale publish'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.275
  - quote: Improved the Artifact tool's guidance so Claude updates a shared artifact
      in place when you were given edit access to it, instead of publishing a separate
      copy
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.275
  - quote: 'Improved plan-usage reads: editor windows and non-interactive sessions
      on one machine now share a read made in the last minute instead of each calling
      the usage endpoint'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.275
  - quote: 'Improved Write and Edit results for files in the synced account-skills
      folder: they now say the change is not saved to your account and how to save
      it'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.275
  - quote: Changed the Artifact tool to ask for a one-word tab icon on a first publish
      instead of an emoji favicon
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.275
  - quote: Changed scheduled and Run now routine runs to save data to, and republish
      the page of, an artifact you can edit without asking; public artifacts, first
      publishes and deletes still ask
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.275
  - quote: '[VSCode] Added accept and reject buttons under each change in the proposed-change
      diff tab, so an edit can be reviewed change by change'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.275
  - quote: '[VSCode] Changed New session in a Claude editor tab to open in the sidebar
      when Preferred Location is set to Sidebar, instead of always opening another
      tab'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.275
  - quote: '[Claude Code on the web] Improved what Claude tells you when asked to
      edit, delete or run a routine it didn''t create: it now links to the routine''s
      page so you can do it yourself'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.275
  - quote: '[Claude Tag] Added Amazon CloudWatch, CloudWatch Logs, Amazon SNS, Google
      Cloud Monitoring and Cloud Logging presets to an access bundle''s Credentials
      tab in Claude Tag admin settings'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.275
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 10-editor-experience-changes-in-v2-1-275
  source_release: claude-code-2026-09-17-v2-1-275-github-391032307-12ccfafd
  source_type: github_releases
  theme: editor-experience
  title: 10 Editor Experience changes in v2.1.275
  type: change
related_changes:
- '[[Changes/Claude Code/2026-09-11-3-editor-experience-changes-in-v2-1-269|3 Editor
  Experience changes in v2.1.269]]'
- '[[Changes/Claude Code/2026-09-14-3-editor-experience-changes-in-v2-1-271|3 Editor
  Experience changes in v2.1.271]]'
- '[[Changes/Claude Code/2026-09-15-claude-code-on-the-web-added-a-discard-unsaved-changes-confirmation-before-the-n|Claude
  Code on the web Added a "Discard unsaved changes?" confirmation before…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-09-17-v2-1-275-github-391032307-12ccfafd|claude-code-2026-09-17-v2-1-275-github-391032307-12ccfafd]]'
source_type: github_releases
theme: editor-experience
title: 10 Editor Experience changes in v2.1.275
type: change
---

<!-- chronolog:begin region="header" -->
# 10 Editor Experience changes in v2.1.275

**Claude Code** · 2026-09-17 · [[Themes/editor-experience|Editor Experience]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.275) · from [[Releases/Claude Code/claude-code-2026-09-17-v2-1-275-github-391032307-12ccfafd|v2.1.275]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Improved artifact publish results: they name the tab icon sent, warn when the page contains a NUL byte, and retry a flaky fetch of the newer page to merge after a stale publish

> Improved the Artifact tool's guidance so Claude updates a shared artifact in place when you were given edit access to it, instead of publishing a separate copy

> Improved plan-usage reads: editor windows and non-interactive sessions on one machine now share a read made in the last minute instead of each calling the usage endpoint

> Improved Write and Edit results for files in the synced account-skills folder: they now say the change is not saved to your account and how to save it

> Changed the Artifact tool to ask for a one-word tab icon on a first publish instead of an emoji favicon

> Changed scheduled and Run now routine runs to save data to, and republish the page of, an artifact you can edit without asking; public artifacts, first publishes and deletes still ask

> [VSCode] Added accept and reject buttons under each change in the proposed-change diff tab, so an edit can be reviewed change by change

> [VSCode] Changed New session in a Claude editor tab to open in the sidebar when Preferred Location is set to Sidebar, instead of always opening another tab

> [Claude Code on the web] Improved what Claude tells you when asked to edit, delete or run a routine it didn't create: it now links to the routine's page so you can do it yourself

> [Claude Tag] Added Amazon CloudWatch, CloudWatch Logs, Amazon SNS, Google Cloud Monitoring and Cloud Logging presets to an access bundle's Credentials tab in Claude Tag admin settings

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.275
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-09-17-vscode-improved-the-agent-map-the-pill-counts-running-agents-and-turns-red-after|VSCode Improved the agent map]] · Agent Mode
- [[Changes/Claude Code/2026-09-17-6-apps-and-integrations-changes-in-v2-1-275|6 Apps and Integrations changes in v2.1.275]] · Apps and Integrations
- [[Changes/Claude Code/2026-09-17-vscode-added-viewing-editing-and-deleting-a-saved-memory-inside-the-memory-dialo|VSCode Added viewing, editing and deleting a saved memory inside the Memory dialog]] · Memory and Personalization
- [[Changes/Claude Code/2026-09-17-7-safety-and-privacy-changes-in-v2-1-275|7 Safety and Privacy changes in v2.1.275]] · Safety and Privacy
- [[Changes/Claude Code/2026-09-17-claude-tag-improved-claude-s-notices-in-enterprise-grid-channels-shared-across-w|Claude Tag Improved Claude's notices in Enterprise Grid channels shared across…]] · Enterprise and Administration
- [[Changes/Claude Code/2026-09-17-added-a-send-now-key-ctrl-enter-or-ctrl-x-ctrl-s-that-interrupts-the-current-tur|Added a send-now key (ctrl+enter, or ctrl+x ctrl+s) that interrupts the current turn…]] · Model Support
- [[Changes/Claude Code/2026-09-17-2-developer-workflow-changes-in-v2-1-275|2 Developer Workflow changes in v2.1.275]] · Developer Workflow
- [[Changes/Claude Code/2026-09-17-added-the-signed-in-account-to-claude-apps-gateway-sign-in-when-the-gateway-name|Added the signed-in account to Claude apps gateway sign-in]] · Account and Access
- [[Changes/Claude Code/2026-09-17-improved-the-desktop-error-when-claude-desktop-does-not-open-it-now-says-why-and|Improved the /desktop error when Claude Desktop does not open]] · Mobile and Desktop
- [[Changes/Claude Code/2026-09-17-improved-the-artifact-tool-s-publish-and-read-results-they-now-say-who-can-open|Improved the Artifact tool's publish and read results]] · Interface Experience
- [[Changes/Claude Code/2026-09-17-added-plugin-install-plugin-marketplace-source-which-offers-to-add-the-marketpla|Added /plugin install plugin --marketplace source, which offers to add…]] · Apps and Integrations
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Editor Experience

- Earlier: 2026-09-15 · Claude Code · [[Changes/Claude Code/2026-09-15-claude-code-on-the-web-added-a-discard-unsaved-changes-confirmation-before-the-n|Claude Code on the web Added a "Discard unsaved changes?" confirmation before…]]
- Later: 2026-09-17 · Claude Code · [[Changes/Claude Code/2026-09-17-vscode-added-a-claudecode-lockeditorgroups-setting-to-stop-claude-from-locking-t|VSCode Added a claudeCode.lockEditorGroups setting to stop Claude from locking…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-14 · Cursor · [[Changes/Cursor/2023-03-14-3-editor-experience-changes-in-0-0-37|3 Editor Experience changes in 0.0.37]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-09-17-3dd1b0&body=Card%3A%20Changes%2FClaude%20Code%2F2026-09-17-10-editor-experience-changes-in-v2-1-275.md%0ACard%20ID%3A%20claude-code-2026-09-17-3dd1b0%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.275%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->