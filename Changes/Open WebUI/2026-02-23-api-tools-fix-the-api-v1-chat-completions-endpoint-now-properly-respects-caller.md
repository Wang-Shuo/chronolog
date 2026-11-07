---
card_id: open-webui-2026-02-23-f71a23
date: '2026-02-23'
description: "Open WebUI · 2026-02-23 · Agent Mode: \U0001F6E0️ **API tools fix.**
  The /api/v1/chat/completions endpoint now properly respects caller-provided tools
  instead of…"
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 963
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: change
machine_hash: c960cce9bff522781ea4d613519269f07fa64d1df6bfae040180eec5459c7155
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-02-23-f71a23
  comparison: ''
  date: '2026-02-23'
  description: "Open WebUI — v0.8.4: \U0001F6E0️ **API tools fix.** The /api/v1/chat/completions
    endpoint now properly respects caller-provided tools instead of overriding them
    with server-side tools, fixing issues where external agents like Claude Code or
    Cursor would receive unexpected tool advertisements. [#21557](https://github.com/open-webui/open-webui/issues/21557),
    [#21555](https://github.com/open-webui/open-webui/pull/21555)"
  evidence:
  - quote: "\U0001F6E0️ **API tools fix.** The /api/v1/chat/completions endpoint now
      properly respects caller-provided tools instead of overriding them with server-side
      tools, fixing issues where external agents like Claude Code or Cursor would
      receive unexpected tool advertisements. [#21557](https://github.com/open-webui/open-webui/issues/21557),
      [#21555](https://github.com/open-webui/open-webui/pull/21555)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.4
  extractor_version: fallback-v5
  impact: incremental
  kind: change
  product: open-webui
  product_name: Open WebUI
  slug: api-tools-fix-the-api-v1-chat-completions-endpoint-now-properly-respects-caller
  source_release: open-webui-2026-02-23-v0-8-4-github-289302856-177fc54c
  source_type: github_releases
  theme: agent-mode
  title: "\U0001F6E0️ **API tools fix.** The /api/v1/chat/completions endpoint now
    properly respects…"
  type: change
related_changes:
- '[[Changes/ElevenLabs/2026-02-23-elevenagents|ElevenAgents]]'
- '[[Changes/GitHub Copilot CLI/2026-02-23-2-agent-mode-changes-in-v0-0-415|2 Agent
  Mode changes in v0.0.415]]'
- '[[Changes/Lovable/2026-02-23-file-edits-now-persist-when-stopping-the-agent-so-you-can-resume-work-without-lo|File
  edits now persist when stopping the agent, so you can resume work without…]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-02-23-v0-8-4-github-289302856-177fc54c|open-webui-2026-02-23-v0-8-4-github-289302856-177fc54c]]'
source_type: github_releases
theme: agent-mode
title: "\U0001F6E0️ API tools fix. The /api/v1/chat/completions endpoint now properly
  respects…"
type: change
---

<!-- chronolog:begin region="header" -->
# 🛠️ **API tools fix.** The /api/v1/chat/completions endpoint now properly respects…

**Open WebUI** · 2026-02-23 · [[Themes/agent-mode|Agent Mode]] · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.8.4) · from [[Releases/Open WebUI/open-webui-2026-02-23-v0-8-4-github-289302856-177fc54c|v0.8.4]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> 🛠️ **API tools fix.** The /api/v1/chat/completions endpoint now properly respects caller-provided tools instead of overriding them with server-side tools, fixing issues where external agents like Claude Code or Cursor would receive unexpected tool advertisements. [#21557](https://github.com/open-webui/open-webui/issues/21557), [#21555](https://github.com/open-webui/open-webui/pull/21555)
>
> Source: https://github.com/open-webui/open-webui/releases/tag/v0.8.4
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-02-23-12-developer-workflow-changes-in-v0-8-4|12 Developer Workflow changes in v0.8.4]] · Developer Workflow
- [[Changes/Open WebUI/2026-02-23-10-reliability-and-performance-changes-in-v0-8-4|10 Reliability and Performance changes in v0.8.4]] · Reliability and Performance
- [[Changes/Open WebUI/2026-02-23-text-file-type-detection-fix-typescript-and-other-text-files-that-were-mis-detec|📄 Text file type detection fix. TypeScript and other text files…]] · Multimodal Input
- [[Changes/Open WebUI/2026-02-23-2-memory-and-personalization-changes-in-v0-8-4|2 Memory and Personalization changes in v0.8.4]] · Memory and Personalization
- [[Changes/Open WebUI/2026-02-23-ui-accessibility-improvements-screen-reader-users-can-now-navigate-the-interface|♿ UI accessibility improvements. Screen reader users can now navigate…]] · Accessibility and Localization
- [[Changes/Open WebUI/2026-02-23-8-interface-experience-changes-in-v0-8-4|8 Interface Experience changes in v0.8.4]] · Interface Experience
- [[Changes/Open WebUI/2026-02-23-2-editor-experience-changes-in-v0-8-4|2 Editor Experience changes in v0.8.4]] · Editor Experience
- [[Changes/Open WebUI/2026-02-23-4-search-and-browsing-changes-in-v0-8-4|4 Search and Browsing changes in v0.8.4]] · Search and Browsing
- [[Changes/Open WebUI/2026-02-23-mcp-ssl-verification-fix-mcp-tool-connections-now-properly-respect-the-aiohttp-c|🔓 MCP SSL verification fix. MCP tool connections now properly respect…]] · Apps and Integrations
- [[Changes/Open WebUI/2026-02-23-file-access-control-respect-the-files-list-and-search-endpoints-now-properly-res|🗄️ File access control respect. The files list and search endpoints now properly…]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-02-23-3-account-and-access-changes-in-v0-8-4|3 Account and Access changes in v0.8.4]] · Account and Access
- [[Changes/Open WebUI/2026-02-23-3-safety-and-privacy-changes-in-v0-8-4|3 Safety and Privacy changes in v0.8.4]] · Safety and Privacy
- [[Changes/Open WebUI/2026-02-23-16-model-support-changes-in-v0-8-4|16 Model Support changes in v0.8.4]] · Model Support
- [[Changes/Open WebUI/2026-02-23-15-other-changes-in-v0-8-4|15 other changes in v0.8.4]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-02-23 · Lovable · [[Changes/Lovable/2026-02-23-file-edits-now-persist-when-stopping-the-agent-so-you-can-resume-work-without-lo|File edits now persist when stopping the agent, so you can resume work without…]]
- Later: 2026-02-24 · Cline · [[Changes/Cline/2026-02-24-3-agent-mode-changes-in-v3-67-0|3 Agent Mode changes in v3.67.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-02-23-f71a23&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-02-23-api-tools-fix-the-api-v1-chat-completions-endpoint-now-properly-respects-caller.md%0ACard%20ID%3A%20open-webui-2026-02-23-f71a23%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.8.4%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->