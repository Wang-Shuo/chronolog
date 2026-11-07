---
card_id: github-copilot-cli-2026-05-19-23cec4
date: '2026-05-19'
description: 'GitHub Copilot CLI · 2026-05-19 · Agent Mode: 4 changes in 1.0.49 —
  Add /rubber-duck command to get an independent critique of the agent''s current
  work'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1048
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 59835043b26426790e881075a8e6b3d2ef9c38101b189766cba1a2eb3c0f6680
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-05-19-23cec4
  comparison: ''
  date: '2026-05-19'
  description: 'GitHub Copilot CLI — 1.0.49: 4 Agent Mode changes'
  evidence:
  - quote: Add /rubber-duck command to get an independent critique of the agent's
      current work
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.49
  - quote: Add `/rubber-duck` command to invoke the rubber duck agent for an independent
      critique (experimental)
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.49
  - quote: Hooks (preToolUse, postToolUse, subagentStart, subagentStop) now fire correctly
      for sub-agent tool calls
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.49
  - quote: Plugins loaded via --plugin-dir now correctly register their agents as
      available task(agent_type=...) subagents in prompt mode
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.49
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 4-agent-mode-changes-in-v1-0-49
  source_release: github-copilot-cli-2026-05-19-v1-0-49-github-324640083-4bf093b8
  source_type: github_releases
  theme: agent-mode
  title: 4 Agent Mode changes in v1.0.49
  type: change
related_changes:
- '[[Changes/Cursor/2026-05-19-assign-work-items-to-cursor-or-mention-cursor-in-a-comment-to-kick-off-a-cloud-a-1c05f0|Assign
  work items to Cursor, or mention @Cursor in a comment to kick off a cloud agent]]'
- '[[Changes/Dify/2026-05-19-3-agent-mode-changes-in-1-14-2|3 Agent Mode changes in
  1.14.2]]'
- '[[Changes/Gemini/2026-05-19-gemini-spark-is-your-24-7-personal-ai-agent|Gemini
  Spark is your 24/7 personal AI agent]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-05-19-v1-0-49-github-324640083-4bf093b8|github-copilot-cli-2026-05-19-v1-0-49-github-324640083-4bf093b8]]'
source_type: github_releases
theme: agent-mode
title: 4 Agent Mode changes in v1.0.49
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Agent Mode changes in v1.0.49

**GitHub Copilot CLI** · 2026-05-19 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.49) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-05-19-v1-0-49-github-324640083-4bf093b8|1.0.49]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Add /rubber-duck command to get an independent critique of the agent's current work

> Add `/rubber-duck` command to invoke the rubber duck agent for an independent critique (experimental)

> Hooks (preToolUse, postToolUse, subagentStart, subagentStop) now fire correctly for sub-agent tool calls

> Plugins loaded via --plugin-dir now correctly register their agents as available task(agent_type=...) subagents in prompt mode

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.49
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-05-19-2-mobile-and-desktop-changes-in-v1-0-49|2 Mobile and Desktop changes in v1.0.49]] · Mobile and Desktop
- [[Changes/GitHub Copilot CLI/2026-05-19-2-developer-workflow-changes-in-v1-0-49|2 Developer Workflow changes in v1.0.49]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-05-19-memory-permission-prompts-now-name-who-can-see-a-stored-memory-user-scope-or-the|Memory permission prompts now name who can see a stored memory]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-05-19-9-apps-and-integrations-changes-in-v1-0-49|9 Apps and Integrations changes in v1.0.49]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-05-19-2-memory-and-personalization-changes-in-v1-0-49|2 Memory and Personalization changes in v1.0.49]] · Memory and Personalization
- [[Changes/GitHub Copilot CLI/2026-05-19-file-diffs-are-correctly-reported-to-acp-clients-for-all-edit-tool-types|File diffs are correctly reported to ACP clients for all edit tool types]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-05-19-3-interface-experience-changes-in-v1-0-49|3 Interface Experience changes in v1.0.49]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-05-19-document-attachment-paths-are-included-in-context-so-the-agent-can-reference-pas|Document attachment paths are included in context so the agent can reference pasted…]] · Context Window
- [[Changes/GitHub Copilot CLI/2026-05-19-2-model-support-changes-in-v1-0-49|2 Model Support changes in v1.0.49]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-05-19-3-account-and-access-changes-in-v1-0-49|3 Account and Access changes in v1.0.49]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-05-19-10-other-changes-in-v1-0-49|10 other changes in v1.0.49]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-05-19 · Gemini · [[Changes/Gemini/2026-05-19-gemini-spark-is-your-24-7-personal-ai-agent|Gemini Spark is your 24/7 personal AI agent]]
- Later: 2026-05-19 · Microsoft 365 Copilot · [[Changes/Microsoft 365 Copilot/2026-05-19-managing-your-tenant-with-sharepoint-admin-agent-web-sharepoint|Managing your tenant with SharePoint Admin Agent Web (SharePoint)]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-05-19-23cec4&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-05-19-4-agent-mode-changes-in-v1-0-49.md%0ACard%20ID%3A%20github-copilot-cli-2026-05-19-23cec4%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.49%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->