---
card_id: cursor-2026-02-18-e3a15a
date: '2026-02-18'
description: 'Cursor · 2026-02-18 · Safety and Privacy: 7 changes in CLI Improvements
  and Mermaid ASCII Diagrams — Known-safe URLs (e.g. Cursor docs) are auto-approved…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1039
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 1ba69614a66682bd6680376b2ae1d256e2bac75920da3216f7f4b0176ed8eec8
product: cursor
product_name: Cursor
record:
  card_id: cursor-2026-02-18-e3a15a
  comparison: ''
  date: '2026-02-18'
  description: 'Cursor — CLI Improvements and Mermaid ASCII Diagrams: 7 Safety and
    Privacy changes'
  evidence:
  - quote: Known-safe URLs (e.g. Cursor docs) are auto-approved without permission
      prompts.
    source_release: https://cursor.com/changelog/cli-feb-18-2026
  - quote: 'The sandbox in the CLI now supports granular network access controls:
      user config only, user config with defaults, or allow all.'
    source_release: https://cursor.com/changelog/cli-feb-18-2026
  - quote: Use --yolo and --force flags to approve workspace trust, skip MCP confirmation
      prompts, enable auto-run, and activate web tools.
    source_release: https://cursor.com/changelog/cli-feb-18-2026
  - quote: When the sandbox isn't available, the message now explains why for your
      specific OS.
    source_release: https://cursor.com/changelog/cli-feb-18-2026
  - quote: Reduced padding, removed the sandbox lock icon from shell prompts, and
      tightened up visual spacing throughout the CLI interface.
    source_release: https://cursor.com/changelog/cli-feb-18-2026
  - quote: Fixed hanging headless mode when workspace trust is required; -force now
      implicitly trusts the workspace.
    source_release: https://cursor.com/changelog/cli-feb-18-2026
  - quote: Relative paths in sandbox.json now resolve correctly against their config
      file location.
    source_release: https://cursor.com/changelog/cli-feb-18-2026
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: cursor
  product_name: Cursor
  slug: 7-safety-and-privacy-changes-in-cli-improvements-and-mermaid-ascii
  source_release: cursor-2026-02-18-cli-improvements-and-mermaid-ascii-diagrams-https-cursor-com-cha-a75d36c7
  source_type: cursor_changelog
  theme: safety-privacy
  title: 7 Safety and Privacy changes in CLI Improvements and Mermaid ASCII…
  type: change
related_changes:
- '[[Changes/Cursor/2026-02-17-sandbox-network-access-controls|Sandbox network access
  controls]]'
- '[[Changes/Cursor/2026-02-17-3-safety-and-privacy-changes-in-2-5|3 Safety and Privacy
  changes in 2.5]]'
- '[[Changes/Claude Code/2026-02-18-2-safety-and-privacy-changes-in-v2-1-47|2 Safety
  and Privacy changes in v2.1.47]]'
source_release: '[[Releases/Cursor/cursor-2026-02-18-cli-improvements-and-mermaid-ascii-diagrams-https-cursor-com-cha-a75d36c7|cursor-2026-02-18-cli-improvements-and-mermaid-ascii-diagrams-https-cursor-com-cha-a75d36c7]]'
source_type: cursor_changelog
theme: safety-privacy
title: 7 Safety and Privacy changes in CLI Improvements and Mermaid ASCII…
type: change
---

<!-- chronolog:begin region="header" -->
# 7 Safety and Privacy changes in CLI Improvements and Mermaid ASCII…

**Cursor** · 2026-02-18 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://cursor.com/changelog/cli-feb-18-2026) · from [[Releases/Cursor/cursor-2026-02-18-cli-improvements-and-mermaid-ascii-diagrams-https-cursor-com-cha-a75d36c7|CLI Improvements and Mermaid ASCII Diagrams]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Known-safe URLs (e.g. Cursor docs) are auto-approved without permission prompts.

> The sandbox in the CLI now supports granular network access controls: user config only, user config with defaults, or allow all.

> Use --yolo and --force flags to approve workspace trust, skip MCP confirmation prompts, enable auto-run, and activate web tools.

> When the sandbox isn't available, the message now explains why for your specific OS.

> Reduced padding, removed the sandbox lock icon from shell prompts, and tightened up visual spacing throughout the CLI interface.

> Fixed hanging headless mode when workspace trust is required; -force now implicitly trusts the workspace.

> Relative paths in sandbox.json now resolve correctly against their config file location.

Source: https://cursor.com/changelog/cli-feb-18-2026
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Cursor/2026-02-18-2-mobile-and-desktop-changes-in-cli-improvements-and-mermaid-ascii|2 Mobile and Desktop changes in CLI Improvements and Mermaid ASCII…]] · Mobile and Desktop
- [[Changes/Cursor/2026-02-18-2-model-support-changes-in-cli-improvements-and-mermaid-ascii|2 Model Support changes in CLI Improvements and Mermaid ASCII…]] · Model Support
- [[Changes/Cursor/2026-02-18-2-agent-mode-changes-in-cli-improvements-and-mermaid-ascii|2 Agent Mode changes in CLI Improvements and Mermaid ASCII…]] · Agent Mode
- [[Changes/Cursor/2026-02-18-mermaid-ascii-diagrams-in-cli-8c4835|Mermaid ASCII diagrams in CLI]] · Developer Workflow
- [[Changes/Cursor/2026-02-18-plan-mode-improvements-in-cli-9a872d|Plan mode improvements in CLI]] · Interface Experience
- [[Changes/Cursor/2026-02-18-2-interface-experience-changes-in-cli-improvements-and-mermaid-ascii|2 Interface Experience changes in CLI Improvements and Mermaid ASCII…]] · Interface Experience
- [[Changes/Cursor/2026-02-18-this-release-introduces-the-ability-to-hand-off-plans-from-the-cli-to-the-cloud|Cursor introduces the ability to hand off plans from the CLI to the cloud, in-line…]] · Interface Experience
- [[Changes/Cursor/2026-02-18-cli-now-stores-conversation-transcripts-that-the-agent-can-use-as-context|CLI now stores conversation transcripts that the agent can use as context]] · Context Window
- [[Changes/Cursor/2026-02-18-auto-updates-now-run-in-the-background-for-faster-time-to-interactive|Auto-updates now run in the background for faster time-to-interactive]] · Reliability and Performance
- [[Changes/Cursor/2026-02-18-3-apps-and-integrations-changes-in-cli-improvements-and-mermaid-ascii|3 Apps and Integrations changes in CLI Improvements and Mermaid ASCII…]] · Apps and Integrations
- [[Changes/Cursor/2026-02-18-3-developer-workflow-changes-in-cli-improvements-and-mermaid-ascii|3 Developer Workflow changes in CLI Improvements and Mermaid ASCII…]] · Developer Workflow
- [[Changes/Cursor/2026-02-18-12-other-changes-in-cli-improvements-and-mermaid-ascii|12 other changes in CLI Improvements and Mermaid ASCII…]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-02-18 · Claude Code · [[Changes/Claude Code/2026-02-18-2-safety-and-privacy-changes-in-v2-1-47|2 Safety and Privacy changes in v2.1.47]]
- Later: 2026-02-19 · Claude Code · [[Changes/Claude Code/2026-02-19-3-safety-and-privacy-changes-in-v2-1-49|3 Safety and Privacy changes in v2.1.49]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20cursor-2026-02-18-e3a15a&body=Card%3A%20Changes%2FCursor%2F2026-02-18-7-safety-and-privacy-changes-in-cli-improvements-and-mermaid-ascii.md%0ACard%20ID%3A%20cursor-2026-02-18-e3a15a%0ASource%3A%20https%3A%2F%2Fcursor.com%2Fchangelog%2Fcli-feb-18-2026%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->