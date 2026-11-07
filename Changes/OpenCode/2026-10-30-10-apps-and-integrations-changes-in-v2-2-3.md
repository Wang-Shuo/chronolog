---
card_id: opencode-2026-10-30-225fd8
date: '2026-10-30'
description: 'OpenCode · 2026-10-30 · Apps and Integrations: 10 changes in v2.2.3
  — Core Added separate managed-policy actions for connecting to integrations and
  using…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If
    you have a recording with each speaker with a different microphone, or saved…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2877
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: a32bb56a9f0dfe1523a9ba042159286726428d0f9c04ebc600fbf7ab51adff27
product: opencode
product_name: OpenCode
record:
  card_id: opencode-2026-10-30-225fd8
  comparison: ''
  date: '2026-10-30'
  description: 'OpenCode — v2.2.3: 10 Apps and Integrations changes'
  evidence:
  - quote: Core Added separate managed-policy actions for connecting to integrations
      and using integrations, MCP servers, skills, and plugins.
    source_release: https://opencode.ai/changelog/v2.2.3
  - quote: SDK Unified Effect and Promise tool declarations around tool(...) , with
      optional output schemas and executable or declaration-only tools.
    source_release: https://opencode.ai/changelog/v2.2.3
  - quote: SDK Added typed OpenRouter debug , models , plugins , provider , and user
      options to the Responses route.
    source_release: https://opencode.ai/changelog/v2.2.3
  - quote: Core Preserved plugin-provided model variants and delayed dynamic provider
      fallback until external SDK hooks have run.
    source_release: https://opencode.ai/changelog/v2.2.3
  - quote: SDK Matched the Promise AI client more closely to the Effect API and accepted
      typed tools in loops.
    source_release: https://opencode.ai/changelog/v2.2.3
  - quote: SDK Kept tools whose execute handler can throw available to the AI client.
    source_release: https://opencode.ai/changelog/v2.2.3
  - quote: SDK Continued polling queued media generations when providers return unknown
      intermediate statuses.
    source_release: https://opencode.ai/changelog/v2.2.3
  - quote: SDK Stopped sending an incompatible filename alongside file_url on OpenAI
      Responses requests.
    source_release: https://opencode.ai/changelog/v2.2.3
  - quote: Extensions Preserved null values in Code Mode text encoding.
    source_release: https://opencode.ai/changelog/v2.2.3
  - quote: Extensions Tidied nested Extensions menus.
    source_release: https://opencode.ai/changelog/v2.2.3
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: opencode
  product_name: OpenCode
  slug: 10-apps-and-integrations-changes-in-v2-2-3
  source_release: opencode-2026-10-30-v2-2-3-0c0c59eb
  source_type: opencode_changelog
  theme: apps-integrations
  title: 10 Apps and Integrations changes in v2.2.3
  type: change
related_changes:
- '[[Changes/Devin/2026-10-30-header-scripts-for-mcp-servers-on-the-session-machine|Header
  Scripts for MCP Servers on the Session Machine]]'
- '[[Changes/OpenCode/2026-10-30-4-apps-and-integrations-changes-in-v2-2-5|4 Apps
  and Integrations changes in v2.2.5]]'
- '[[Changes/OpenCode/2026-10-30-sdk-extended-client-experimental-persistentpty-update-to-rename-terminals-or-cle|SDK
  Extended client.experimental.persistentPty.update to rename terminals or clear…]]'
source_release: '[[Releases/OpenCode/opencode-2026-10-30-v2-2-3-0c0c59eb|opencode-2026-10-30-v2-2-3-0c0c59eb]]'
source_type: opencode_changelog
theme: apps-integrations
title: 10 Apps and Integrations changes in v2.2.3
type: change
---

<!-- chronolog:begin region="header" -->
# 10 Apps and Integrations changes in v2.2.3

**OpenCode** · 2026-10-30 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://opencode.ai/changelog/v2.2.3) · from [[Releases/OpenCode/opencode-2026-10-30-v2-2-3-0c0c59eb|v2.2.3]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Core Added separate managed-policy actions for connecting to integrations and using integrations, MCP servers, skills, and plugins.

> SDK Unified Effect and Promise tool declarations around tool(...) , with optional output schemas and executable or declaration-only tools.

> SDK Added typed OpenRouter debug , models , plugins , provider , and user options to the Responses route.

> Core Preserved plugin-provided model variants and delayed dynamic provider fallback until external SDK hooks have run.

> SDK Matched the Promise AI client more closely to the Effect API and accepted typed tools in loops.

> SDK Kept tools whose execute handler can throw available to the AI client.

> SDK Continued polling queued media generations when providers return unknown intermediate statuses.

> SDK Stopped sending an incompatible filename alongside file_url on OpenAI Responses requests.

> Extensions Preserved null values in Code Mode text encoding.

> Extensions Tidied nested Extensions menus.

Source: https://opencode.ai/changelog/v2.2.3
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenCode/2026-10-30-2-automation-and-scheduling-changes-in-v2-2-3|2 Automation and Scheduling changes in v2.2.3]] · Automation and Scheduling
- [[Changes/OpenCode/2026-10-30-desktop-stability-fixes|Desktop Stability Fixes]] · Reliability and Performance
- [[Changes/OpenCode/2026-10-30-faster-long-sessions-in-desktop|Faster Long Sessions in Desktop]] · Reliability and Performance
- [[Changes/OpenCode/2026-10-30-managed-policy-integration-use-covers-integrations-only|Managed policy: integration.use covers integrations only]] · Apps and Integrations
- [[Changes/OpenCode/2026-10-30-use-claude-code-in-opencode|Use Claude Code in OpenCode]] · Account and Access
- [[Changes/OpenCode/2026-10-30-desktop-fixed-timeline-growth-zoom-end-scrolling-highlighting-and-dom-observer-p|Desktop Fixed timeline growth, zoom-end scrolling, highlighting, and DOM-observer…]] · Reliability and Performance
- [[Changes/OpenCode/2026-10-30-core-preserved-permission-reasons-and-feedback-in-mcp-failures-and-made-code-mod|Core Preserved permission reasons and feedback in MCP failures, and made Code Mode…]] · Safety and Privacy
- [[Changes/OpenCode/2026-10-30-desktop-kept-the-current-and-command-menu-selection-stable-while-results-update|Desktop Kept the current @ and command-menu selection stable while results update…]] · Interface Experience
- [[Changes/OpenCode/2026-10-30-tui-plugins-require-opentui-0-8|TUI plugins require OpenTUI 0.8]] · Apps and Integrations
- [[Changes/OpenCode/2026-10-30-2-model-support-changes-in-v2-2-3|2 Model Support changes in v2.2.3]] · Model Support
- [[Changes/OpenCode/2026-10-30-8-developer-workflow-changes-in-v2-2-3|8 Developer Workflow changes in v2.2.3]] · Developer Workflow
- [[Changes/OpenCode/2026-10-30-14-mobile-and-desktop-changes-in-v2-2-3|14 Mobile and Desktop changes in v2.2.3]] · Mobile and Desktop
- [[Changes/OpenCode/2026-10-30-3-other-changes-in-v2-2-3|3 other changes in v2.2.3]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-10-30 · OpenCode · [[Changes/OpenCode/2026-10-30-sdk-extended-client-experimental-persistentpty-update-to-rename-terminals-or-cle|SDK Extended client.experimental.persistentPty.update to rename terminals or clear…]]
- Later: 2026-10-30 · OpenCode · [[Changes/OpenCode/2026-10-30-publish-interactive-artifacts|Publish Interactive Artifacts]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-12-14 · Descript · [[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If you have a recording with each speaker with a different microphone, or saved…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20opencode-2026-10-30-225fd8&body=Card%3A%20Changes%2FOpenCode%2F2026-10-30-10-apps-and-integrations-changes-in-v2-2-3.md%0ACard%20ID%3A%20opencode-2026-10-30-225fd8%0ASource%3A%20https%3A%2F%2Fopencode.ai%2Fchangelog%2Fv2.2.3%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->