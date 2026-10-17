---
card_id: claude-code-2026-10-14-12d86d
date: '2026-10-14'
description: 'Claude Code · 2026-10-14 · Apps and Integrations: 7 changes in v2.1.300
  — Added the `prompt.change` mod hook, raised when the prompt box''s text changes
  without…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1301
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 3cc459107a4a0f1000eab1ee645fb2ac70a9987dbc3df8f2d000bab523d9c882
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-10-14-12d86d
  comparison: ''
  date: '2026-10-14'
  description: 'Claude Code — v2.1.300: 7 Apps and Integrations changes'
  evidence:
  - quote: 'Added the `prompt.change` mod hook, raised when the prompt box''s text
      changes without a typed edit: a recalled history entry, a clear, an undo, or
      a plugin''s fill'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.300
  - quote: 'Improved mod sharing in the built-in `plugin-authoring` skill: Claude
      scans a mod''s files for keys before opening them, and asks before scanning
      a folder outside the project'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.300
  - quote: 'Changed `PermissionRequest` hooks in Cowork cloud sessions: a `setMode`
      update in a hook''s allow is now ignored; the rest of the approval still applies'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.300
  - quote: 'Changed hooks: `updatedInput` from PreToolUse and PermissionRequest hooks
      is now validated like Claude''s own input: unknown keys are dropped, and input
      the tool rejects denies the call'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.300
  - quote: '[Claude Tag] Added support for Slack Connect channels: an Owner or Claude
      Tag admin can let Claude in Slack answer in channels shared with another organization;
      it''s off by default'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.300
  - quote: '[Claude Tag] Added a private Allow once / Deny card in Slack threads for
      connector actions that need your approval, so Claude asks instead of refusing;
      others only see that it''s waiting on you'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.300
  - quote: '[Claude Tag] Changed access bundles an admin attached to a Slack channel
      to keep applying once the channel becomes a Slack Connect channel, with no need
      to remove and re-attach them'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.300
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 7-apps-and-integrations-changes-in-v2-1-300
  source_release: claude-code-2026-10-14-v2-1-300-github-412815061-c358fcd0
  source_type: github_releases
  theme: apps-integrations
  title: 7 Apps and Integrations changes in v2.1.300
  type: change
related_changes:
- '[[Changes/Claude Code/2026-10-09-3-apps-and-integrations-changes-in-v2-1-296|3
  Apps and Integrations changes in v2.1.296]]'
- '[[Changes/Cursor/2026-10-13-2-apps-and-integrations-changes-in-origin-app-marketplace|2
  Apps and Integrations changes in Origin App Marketplace]]'
- '[[Changes/Cursor/2026-10-13-apps-for-your-stack|Apps for your stack]]'
source_release: '[[Releases/Claude Code/claude-code-2026-10-14-v2-1-300-github-412815061-c358fcd0|claude-code-2026-10-14-v2-1-300-github-412815061-c358fcd0]]'
source_type: github_releases
theme: apps-integrations
title: 7 Apps and Integrations changes in v2.1.300
type: change
---

<!-- chronolog:begin region="header" -->
# 7 Apps and Integrations changes in v2.1.300

**Claude Code** · 2026-10-14 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.300) · from [[Releases/Claude Code/claude-code-2026-10-14-v2-1-300-github-412815061-c358fcd0|v2.1.300]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added the `prompt.change` mod hook, raised when the prompt box's text changes without a typed edit: a recalled history entry, a clear, an undo, or a plugin's fill

> Improved mod sharing in the built-in `plugin-authoring` skill: Claude scans a mod's files for keys before opening them, and asks before scanning a folder outside the project

> Changed `PermissionRequest` hooks in Cowork cloud sessions: a `setMode` update in a hook's allow is now ignored; the rest of the approval still applies

> Changed hooks: `updatedInput` from PreToolUse and PermissionRequest hooks is now validated like Claude's own input: unknown keys are dropped, and input the tool rejects denies the call

> [Claude Tag] Added support for Slack Connect channels: an Owner or Claude Tag admin can let Claude in Slack answer in channels shared with another organization; it's off by default

> [Claude Tag] Added a private Allow once / Deny card in Slack threads for connector actions that need your approval, so Claude asks instead of refusing; others only see that it's waiting on you

> [Claude Tag] Changed access bundles an admin attached to a Slack channel to keep applying once the channel becomes a Slack Connect channel, with no need to remove and re-attach them

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.300
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-10-14-added-cache-creation-5m-tokens-and-cache-creation-1h-tokens-to-the-opentelemetry|Added cache_creation_5m_tokens and cache_creation_1h_tokens to the OpenTelemetry…]] · Context Window
- [[Changes/Claude Code/2026-10-14-added-a-dir-prop-on-a-mod-s-text-for-right-to-left-text-on-windows-and-in-vs-cod|Added a dir prop on a mod's Text for right-to-left text]] · Developer Workflow
- [[Changes/Claude Code/2026-10-14-2-safety-and-privacy-changes-in-v2-1-300|2 Safety and Privacy changes in v2.1.300]] · Safety and Privacy
- [[Changes/Claude Code/2026-10-14-3-mobile-and-desktop-changes-in-v2-1-300|3 Mobile and Desktop changes in v2.1.300]] · Mobile and Desktop
- [[Changes/Claude Code/2026-10-14-improved-the-note-claude-3-models-get-about-an-mentioned-pdf-so-they-less-often|Improved the note Claude 3 models get about an @-mentioned PDF, so they less often…]] · Model Support
- [[Changes/Claude Code/2026-10-14-2-editor-experience-changes-in-v2-1-300|2 Editor Experience changes in v2.1.300]] · Editor Experience
- [[Changes/Claude Code/2026-10-14-changed-exit-to-force-kill-background-commands-still-running-1-5-seconds-after-b|Changed exit to force-kill background commands still running 1.5 seconds after being…]] · Interface Experience
- [[Changes/Claude Code/2026-10-14-claude-tag-added-support-for-slack-voice-clips-in-claude-in-slack-claude-reads-s|Claude Tag Added support for Slack voice clips in Claude in Slack]] · Voice and Audio
- [[Changes/Claude Code/2026-10-14-3-agent-mode-changes-in-v2-1-300|3 Agent Mode changes in v2.1.300]] · Agent Mode
- [[Changes/Claude Code/2026-10-14-changed-local-session-transcripts-to-also-record-each-api-request-s-system-promp|Changed local session transcripts to also record each API request's system prompt…]] · Collaboration
- [[Changes/Claude Code/2026-10-14-added-advisor-on-claude-platform-on-aws-no-advisor-runs-until-you-pick-one-with|Added /advisor on Claude Platform on AWS]] · Other changes
- [[Changes/Claude Code/2026-10-14-5-other-changes-in-v2-1-300|5 other changes in v2.1.300]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-10-13 · Cursor · [[Changes/Cursor/2026-10-13-apps-for-your-stack|Apps for your stack]]
- Later: 2026-10-14 · Claude Code · [[Changes/Claude Code/2026-10-14-19-apps-and-integrations-changes-in-v2-1-299|19 Apps and Integrations changes in v2.1.299]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-10-14-12d86d&body=Card%3A%20Changes%2FClaude%20Code%2F2026-10-14-7-apps-and-integrations-changes-in-v2-1-300.md%0ACard%20ID%3A%20claude-code-2026-10-14-12d86d%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.300%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->