---
card_id: opencode-2026-01-04-1ae779
date: '2026-01-04'
description: 'OpenCode · 2026-01-04 · Safety and Privacy: 13 changes in v1.1.1 — Breaking
  Changes for SDK Users Asked : { id, sessionID, permission, patterns, metadata…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke
    Application Access]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1986
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 6c2fa9410f112c79bcb67005e1d2975bfccbad1d970746de381a0fc32c4781d7
product: opencode
product_name: OpenCode
record:
  card_id: opencode-2026-01-04-1ae779
  comparison: ''
  date: '2026-01-04'
  description: 'OpenCode — v1.1.1: 13 Safety and Privacy changes'
  evidence:
  - quote: 'Breaking Changes for SDK Users Asked : { id, sessionID, permission, patterns,
      metadata, always, tool: { messageID, callID } }'
    source_release: https://opencode.ai/changelog/v1.1.1
  - quote: Breaking Changes for SDK Users Event name changed from permission.updated
      to permission.asked
    source_release: https://opencode.ai/changelog/v1.1.1
  - quote: Breaking Changes for SDK Users type renamed to permission
    source_release: https://opencode.ai/changelog/v1.1.1
  - quote: 'Server Changes New endpoint: POST /permission/:requestID/reply for responding
      to permission requests'
    source_release: https://opencode.ai/changelog/v1.1.1
  - quote: Server Changes GET /permission now returns PermissionNext.Request[] instead
      of Permission.Info[]
    source_release: https://opencode.ai/changelog/v1.1.1
  - quote: Other Changes Agent tools field is deprecated - use permission instead
    source_release: https://opencode.ai/changelog/v1.1.1
  - quote: Core Add sandbox support for git worktrees to allow working in multiple
      directories per project
    source_release: https://opencode.ai/changelog/v1.1.1
  - quote: Core Add reject message support to permission dialogs for better user feedback
    source_release: https://opencode.ai/changelog/v1.1.1
  - quote: Core Add escape key handling to permission dialogs for better keyboard
      navigation
    source_release: https://opencode.ai/changelog/v1.1.1
  - quote: Core Fix TUI permission tests for new evaluate function signature
    source_release: https://opencode.ai/changelog/v1.1.1
  - quote: Core Improve permission error handling and evaluation logic in TUI
    source_release: https://opencode.ai/changelog/v1.1.1
  - quote: Core Rework permission system
    source_release: https://opencode.ai/changelog/v1.1.1
  - quote: Desktop Properly decode session ID for permission context in desktop app
    source_release: https://opencode.ai/changelog/v1.1.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: opencode
  product_name: OpenCode
  slug: 13-safety-and-privacy-changes-in-v1-1-1
  source_release: opencode-2026-01-04-v1-1-1-588acaae
  source_type: opencode_changelog
  theme: safety-privacy
  title: 13 Safety and Privacy changes in v1.1.1
  type: change
related_changes:
- '[[Changes/Lovable/2025-12-23-public-preview-link-controls|Public preview link controls]]'
- '[[Changes/Dify/2025-12-25-3-safety-and-privacy-changes-in-1-11-2|3 Safety and Privacy
  changes in 1.11.2]]'
- '[[Changes/Replit/2025-12-26-security-center-for-enterprise|Security Center for
  Enterprise]]'
source_release: '[[Releases/OpenCode/opencode-2026-01-04-v1-1-1-588acaae|opencode-2026-01-04-v1-1-1-588acaae]]'
source_type: opencode_changelog
theme: safety-privacy
title: 13 Safety and Privacy changes in v1.1.1
type: change
---

<!-- chronolog:begin region="header" -->
# 13 Safety and Privacy changes in v1.1.1

**OpenCode** · 2026-01-04 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://opencode.ai/changelog/v1.1.1) · from [[Releases/OpenCode/opencode-2026-01-04-v1-1-1-588acaae|v1.1.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Breaking Changes for SDK Users Asked : { id, sessionID, permission, patterns, metadata, always, tool: { messageID, callID } }

> Breaking Changes for SDK Users Event name changed from permission.updated to permission.asked

> Breaking Changes for SDK Users type renamed to permission

> Server Changes New endpoint: POST /permission/:requestID/reply for responding to permission requests

> Server Changes GET /permission now returns PermissionNext.Request[] instead of Permission.Info[]

> Other Changes Agent tools field is deprecated - use permission instead

> Core Add sandbox support for git worktrees to allow working in multiple directories per project

> Core Add reject message support to permission dialogs for better user feedback

> Core Add escape key handling to permission dialogs for better keyboard navigation

> Core Fix TUI permission tests for new evaluate function signature

> Core Improve permission error handling and evaluation logic in TUI

> Core Rework permission system

> Desktop Properly decode session ID for permission context in desktop app

Source: https://opencode.ai/changelog/v1.1.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenCode/2026-01-04-3-model-support-changes-in-v1-1-1|3 Model Support changes in v1.1.1]] · Model Support
- [[Changes/OpenCode/2026-01-04-19-developer-workflow-changes-in-v1-1-1|19 Developer Workflow changes in v1.1.1]] · Developer Workflow
- [[Changes/OpenCode/2026-01-04-18-apps-and-integrations-changes-in-v1-1-1|18 Apps and Integrations changes in v1.1.1]] · Apps and Integrations
- [[Changes/OpenCode/2026-01-04-core-handle-notfounderror-for-non-shared-sessions-in-sync|Core Handle NotFoundError for non-shared sessions in sync]] · Collaboration
- [[Changes/OpenCode/2026-01-04-13-mobile-and-desktop-changes-in-v1-1-1|13 Mobile and Desktop changes in v1.1.1]] · Mobile and Desktop
- [[Changes/OpenCode/2026-01-04-core-add-tui-session-selection-api-endpoint-for-navigation|Core Add TUI session selection API endpoint for navigation]] · Interface Experience
- [[Changes/OpenCode/2026-01-04-4-agent-mode-changes-in-v1-1-1|4 Agent Mode changes in v1.1.1]] · Agent Mode
- [[Changes/OpenCode/2026-01-04-2-editor-experience-changes-in-v1-1-1|2 Editor Experience changes in v1.1.1]] · Editor Experience
- [[Changes/OpenCode/2026-01-04-2-context-window-changes-in-v1-1-1|2 Context Window changes in v1.1.1]] · Context Window
- [[Changes/OpenCode/2026-01-04-3-reliability-and-performance-changes-in-v1-1-1|3 Reliability and Performance changes in v1.1.1]] · Reliability and Performance
- [[Changes/OpenCode/2026-01-04-17-other-changes-in-v1-1-1|17 other changes in v1.1.1]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2025-12-26 · Replit · [[Changes/Replit/2025-12-26-security-center-for-enterprise|Security Center for Enterprise]]
- Later: 2026-01-05 · OpenCode · [[Changes/OpenCode/2026-01-05-core-fix-permission-evaluation-to-use-rule-based-matching-instead-of-wildcard-pa|Core Fix permission evaluation to use rule-based matching instead of wildcard patterns]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Descript · [[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke Application Access]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20opencode-2026-01-04-1ae779&body=Card%3A%20Changes%2FOpenCode%2F2026-01-04-13-safety-and-privacy-changes-in-v1-1-1.md%0ACard%20ID%3A%20opencode-2026-01-04-1ae779%0ASource%3A%20https%3A%2F%2Fopencode.ai%2Fchangelog%2Fv1.1.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->