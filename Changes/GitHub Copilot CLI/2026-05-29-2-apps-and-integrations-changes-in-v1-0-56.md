---
card_id: github-copilot-cli-2026-05-29-4a2bc9
date: '2026-05-29'
description: 'GitHub Copilot CLI · 2026-05-29 · Apps and Integrations: 2 changes in
  1.0.56 — MCP tools that return both human-readable `content` text and a…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1163
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: b42898b9292e63c9e213353f5c274f6c2f046d5141ab00187d94349447d10d5e
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-05-29-4a2bc9
  comparison: ''
  date: '2026-05-29'
  description: 'GitHub Copilot CLI — 1.0.56: 2 Apps and Integrations changes'
  evidence:
  - quote: MCP tools that return both human-readable `content` text and a `structuredContent`
      payload now surface both to the agent instead of dropping either side. When
      the text is the literal JSON serialization (per MCP spec §5.2.6) it is deduplicated;
      otherwise the two are concatenated.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.56
  - quote: When gh CLI is on PATH, GitHub MCP server now omits redundant gh-replaceable
      tools by default, reducing token usage
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.56
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 2-apps-and-integrations-changes-in-v1-0-56
  source_release: github-copilot-cli-2026-05-29-v1-0-56-github-331744068-421e2448
  source_type: github_releases
  theme: apps-integrations
  title: 2 Apps and Integrations changes in v1.0.56
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-05-28-14-apps-and-integrations-changes-in-rust-v0-135-0|14
  Apps and Integrations changes in rust-v0.135.0]]'
- '[[Changes/GitHub Copilot CLI/2026-05-28-10-apps-and-integrations-changes-in-v1-0-55|10
  Apps and Integrations changes in v1.0.55]]'
- '[[Changes/Claude Code/2026-05-29-4-apps-and-integrations-changes-in-v2-1-157|4
  Apps and Integrations changes in v2.1.157]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-05-29-v1-0-56-github-331744068-421e2448|github-copilot-cli-2026-05-29-v1-0-56-github-331744068-421e2448]]'
source_type: github_releases
theme: apps-integrations
title: 2 Apps and Integrations changes in v1.0.56
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Apps and Integrations changes in v1.0.56

**GitHub Copilot CLI** · 2026-05-29 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.56) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-05-29-v1-0-56-github-331744068-421e2448|1.0.56]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> MCP tools that return both human-readable `content` text and a `structuredContent` payload now surface both to the agent instead of dropping either side. When the text is the literal JSON serialization (per MCP spec §5.2.6) it is deduplicated; otherwise the two are concatenated.

> When gh CLI is on PATH, GitHub MCP server now omits redundant gh-replaceable tools by default, reducing token usage

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.56
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-05-29-2-editor-experience-changes-in-v1-0-56|2 Editor Experience changes in v1.0.56]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-05-29-2-context-window-changes-in-v1-0-56|2 Context Window changes in v1.0.56]] · Context Window
- [[Changes/GitHub Copilot CLI/2026-05-29-reasoning-effort-picker-respects-model-capabilities-options-not-supported-by-the|Reasoning effort picker respects model capabilities]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-05-29-add-builtinagents-rubberduck-setting-to-enable-or-disable-the-rubber-duck-agent|Add builtInAgents.rubberDuck setting to enable or disable the rubber duck agent…]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-05-29-4-developer-workflow-changes-in-v1-0-56|4 Developer Workflow changes in v1.0.56]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-05-29-2-model-support-changes-in-v1-0-56|2 Model Support changes in v1.0.56]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-05-29-6-other-changes-in-v1-0-56|6 other changes in v1.0.56]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-05-29 · Claude Code · [[Changes/Claude Code/2026-05-29-4-apps-and-integrations-changes-in-v2-1-157|4 Apps and Integrations changes in v2.1.157]]
- Later: 2026-06-01 · Codex CLI · [[Changes/Codex CLI/2026-06-01-20-apps-and-integrations-changes-in-rust-v0-136-0|20 Apps and Integrations changes in rust-v0.136.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-05-29-4a2bc9&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-05-29-2-apps-and-integrations-changes-in-v1-0-56.md%0ACard%20ID%3A%20github-copilot-cli-2026-05-29-4a2bc9%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.56%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->