---
card_id: cline-2026-06-26-a2a54a
date: '2026-06-26'
description: 'Cline · 2026-06-26 · Apps and Integrations: 13 changes in v4.0.0 — Add
  the SDK-backed VS Code extension runtime. Cline now runs tasks through the shared
  Cline…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1191
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: fbfc4eeaf9153061720a55d7d8210a50073c93a1b0f0681fbdf7307739262295
product: cline
product_name: Cline
record:
  card_id: cline-2026-06-26-a2a54a
  comparison: ''
  date: '2026-06-26'
  description: 'Cline — v4.0.0: 13 Apps and Integrations changes'
  evidence:
  - quote: Add the SDK-backed VS Code extension runtime. Cline now runs tasks through
      the shared Cline SDK session layer for agent turns, tools, Plan/Act mode coordination,
      MCP, checkpoints, telemetry, provider changes, compaction, mistake limits, and
      task history.
    source_release: https://github.com/cline/cline/releases/tag/v4.0.0
  - quote: Add the Customize marketplace for discovering and managing Skills, MCP
      servers, and Plugins from the extension, including installed/marketplace tabs,
      search and filtering, install/uninstall flows, enable/disable controls, and
      support for plugin-bundled skills.
    source_release: https://github.com/cline/cline/releases/tag/v4.0.0
  - quote: 'Cline Plugins: Plugins let you extend Cline with custom tools, workflows,
      skills, and MCP-powered capabilities tailored to your team or project. Install
      them from the new Customize marketplace to add specialized behavior, connect
      external services, and package reusable automations—so Cline can do more than
      code: it can adapt to the way you work.'
    source_release: https://github.com/cline/cline/releases/tag/v4.0.0
  - quote: Add generic SDK provider settings and model-catalog support so more providers
      can share the same model picker, reasoning controls, dynamic model IDs, provider
      config persistence, and custom model handling.
    source_release: https://github.com/cline/cline/releases/tag/v4.0.0
  - quote: Add MCP support for plugins and shared marketplace install/uninstall plumbing
      used by the VS Code extension.
    source_release: https://github.com/cline/cline/releases/tag/v4.0.0
  - quote: Migrate the VS Code extension from the legacy task implementation to the
      shared Cline SDK and move the extension build/package workflow to Bun.
    source_release: https://github.com/cline/cline/releases/tag/v4.0.0
  - quote: Rework Plan/Act mode handling through SDK coordinators, including closer
      CLI parity and automatic continuation when switching from Plan to Act.
    source_release: https://github.com/cline/cline/releases/tag/v4.0.0
  - quote: Migrate legacy MCP files and formats into the shared settings file and
      protect MCP settings writes with safer locking/atomic updates.
    source_release: https://github.com/cline/cline/releases/tag/v4.0.0
  - quote: Refresh the MCP hub automatically after marketplace installs so newly installed
      servers are available without a manual restart.
    source_release: https://github.com/cline/cline/releases/tag/v4.0.0
  - quote: Reorganize MCP/Skills/Plugins entry points under Customize, hide workflows
      from the Customize menu, wrap Customize tabs on narrow screens, and allow the
      MCP Marketplace tab to be disabled remotely while installed MCP servers remain
      accessible.
    source_release: https://github.com/cline/cline/releases/tag/v4.0.0
  - quote: Update task history handling for the SDK migration, including legacy task
      history visibility, metadata preservation on resume, and corrected deletion
      behavior.
    source_release: https://github.com/cline/cline/releases/tag/v4.0.0
  - quote: Route compacting and mistake-limit behavior through the SDK so the Compact
      button and mistake tracking affect the active SDK session.
    source_release: https://github.com/cline/cline/releases/tag/v4.0.0
  - quote: Remove the legacy Explain Changes feature as part of the SDK migration
      cleanup.
    source_release: https://github.com/cline/cline/releases/tag/v4.0.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: cline
  product_name: Cline
  slug: 13-apps-and-integrations-changes-in-v4-0-0
  source_release: cline-2026-06-26-v4-0-0-github-345514931-9953949f
  source_type: github_releases
  theme: apps-integrations
  title: 13 Apps and Integrations changes in v4.0.0
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-06-24-2-apps-and-integrations-changes-in-v1-0-65|2
  Apps and Integrations changes in v1.0.65]]'
- '[[Changes/Claude Code/2026-06-25-2-apps-and-integrations-changes-in-v2-1-193|2
  Apps and Integrations changes in v2.1.193]]'
- '[[Changes/Codex CLI/2026-06-25-9-apps-and-integrations-changes-in-rust-v0-142-2|9
  Apps and Integrations changes in rust-v0.142.2]]'
source_release: '[[Releases/Cline/cline-2026-06-26-v4-0-0-github-345514931-9953949f|cline-2026-06-26-v4-0-0-github-345514931-9953949f]]'
source_type: github_releases
theme: apps-integrations
title: 13 Apps and Integrations changes in v4.0.0
type: change
---

<!-- chronolog:begin region="header" -->
# 13 Apps and Integrations changes in v4.0.0

**Cline** · 2026-06-26 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/cline/cline/releases/tag/v4.0.0) · from [[Releases/Cline/cline-2026-06-26-v4-0-0-github-345514931-9953949f|v4.0.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Add the SDK-backed VS Code extension runtime. Cline now runs tasks through the shared Cline SDK session layer for agent turns, tools, Plan/Act mode coordination, MCP, checkpoints, telemetry, provider changes, compaction, mistake limits, and task history.

> Add the Customize marketplace for discovering and managing Skills, MCP servers, and Plugins from the extension, including installed/marketplace tabs, search and filtering, install/uninstall flows, enable/disable controls, and support for plugin-bundled skills.

> Cline Plugins: Plugins let you extend Cline with custom tools, workflows, skills, and MCP-powered capabilities tailored to your team or project. Install them from the new Customize marketplace to add specialized behavior, connect external services, and package reusable automations—so Cline can do more than code: it can adapt to the way you work.

> Add generic SDK provider settings and model-catalog support so more providers can share the same model picker, reasoning controls, dynamic model IDs, provider config persistence, and custom model handling.

> Add MCP support for plugins and shared marketplace install/uninstall plumbing used by the VS Code extension.

> Migrate the VS Code extension from the legacy task implementation to the shared Cline SDK and move the extension build/package workflow to Bun.

> Rework Plan/Act mode handling through SDK coordinators, including closer CLI parity and automatic continuation when switching from Plan to Act.

> Migrate legacy MCP files and formats into the shared settings file and protect MCP settings writes with safer locking/atomic updates.

> Refresh the MCP hub automatically after marketplace installs so newly installed servers are available without a manual restart.

> Reorganize MCP/Skills/Plugins entry points under Customize, hide workflows from the Customize menu, wrap Customize tabs on narrow screens, and allow the MCP Marketplace tab to be disabled remotely while installed MCP servers remain accessible.

> Update task history handling for the SDK migration, including legacy task history visibility, metadata preservation on resume, and corrected deletion behavior.

> Route compacting and mistake-limit behavior through the SDK so the Compact button and mistake tracking affect the active SDK session.

> Remove the legacy Explain Changes feature as part of the SDK migration cleanup.

Source: https://github.com/cline/cline/releases/tag/v4.0.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Cline/2026-06-26-add-clinepass-to-the-vs-code-extension-including-onboarding-provider-selection-s|Add ClinePass to the VS Code extension, including onboarding, provider selection…]] · Pricing Model
- [[Changes/Cline/2026-06-26-simplify-provider-settings-ui-by-replacing-many-provider-specific-views-with-sha|Simplify provider settings UI by replacing many provider-specific views with shared…]] · Collaboration
- [[Changes/Cline/2026-06-26-temporarily-disable-subagents-in-the-vs-code-extension-while-the-sdk-backed-expe|Temporarily disable subagents in the VS Code extension while the SDK-backed…]] · Agent Mode
- [[Changes/Cline/2026-06-26-add-edit-and-regenerate-support-for-previous-user-messages-with-clearer-reset-ch|Add edit-and-regenerate support for previous user messages, with clearer Reset Chat…]] · Editor Experience
- [[Changes/Cline/2026-06-26-2-model-support-changes-in-v4-0-0|2 Model Support changes in v4.0.0]] · Model Support
- [[Changes/Cline/2026-06-26-2-developer-workflow-changes-in-v4-0-0|2 Developer Workflow changes in v4.0.0]] · Developer Workflow
- [[Changes/Cline/2026-06-26-add-queued-prompts-in-chat-messages-submitted-while-cline-is-already-working-are|Add queued prompts in chat]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-06-25 · Codex CLI · [[Changes/Codex CLI/2026-06-25-9-apps-and-integrations-changes-in-rust-v0-142-2|9 Apps and Integrations changes in rust-v0.142.2]]
- Later: 2026-06-28 · Cline · [[Changes/Cline/2026-06-28-roll-the-stable-vs-code-extension-back-to-the-pre-sdk-migration-codebase-to-reso|Roll the stable VS Code extension back to the pre-SDK-migration codebase to resolve…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20cline-2026-06-26-a2a54a&body=Card%3A%20Changes%2FCline%2F2026-06-26-13-apps-and-integrations-changes-in-v4-0-0.md%0ACard%20ID%3A%20cline-2026-06-26-a2a54a%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fcline%2Fcline%2Freleases%2Ftag%2Fv4.0.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->