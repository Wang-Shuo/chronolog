---
card_id: claude-code-2026-05-06-d93bf0
date: '2026-05-06'
description: 'Claude Code · 2026-05-06 · Apps and Integrations: 3 changes in v2.1.129
  — Added `--plugin-url <url>` flag to fetch a plugin `.zip` archive from a URL for
  the…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1140
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 1bdaf3c1b9526b8bc470a463ac439ff573983124de8701f844c342bfe646c47b
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-05-06-d93bf0
  comparison: ''
  date: '2026-05-06'
  description: 'Claude Code — v2.1.129: 3 Apps and Integrations changes'
  evidence:
  - quote: Added `--plugin-url <url>` flag to fetch a plugin `.zip` archive from a
      URL for the current session
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.129
  - quote: 'Plugin manifests: `themes` and `monitors` should now be declared under
      `"experimental": { ... }`. Top-level declarations still work but `claude plugin
      validate` will warn'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.129
  - quote: The `claude_code.pull_request.count` OTel metric now counts PRs/MRs created
      via MCP tools, not just shell commands
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.129
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 3-apps-and-integrations-changes-in-v2-1-129
  source_release: claude-code-2026-05-06-v2-1-129-github-317982632-ec56fc0f
  source_type: github_releases
  theme: apps-integrations
  title: 3 Apps and Integrations changes in v2.1.129
  type: change
related_changes:
- '[[Changes/Cursor/2026-04-29-run-npm-install-cursor-sdk-to-get-started-you-can-also-use-cursor-s-native-sdk-s-76fb76|Run
  npm install @cursor/sdk to get started]]'
- '[[Changes/Claude Code/2026-05-04-6-apps-and-integrations-changes-in-v2-1-128|6
  Apps and Integrations changes in v2.1.128]]'
- '[[Changes/Claude Code/2026-05-06-added-claude-code-session-id-environment-variable-to-the-bash-tool-subprocess-en|Added
  CLAUDE_CODE_SESSION_ID environment variable to the Bash tool subprocess…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-05-06-v2-1-129-github-317982632-ec56fc0f|claude-code-2026-05-06-v2-1-129-github-317982632-ec56fc0f]]'
source_type: github_releases
theme: apps-integrations
title: 3 Apps and Integrations changes in v2.1.129
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Apps and Integrations changes in v2.1.129

**Claude Code** · 2026-05-06 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.129) · from [[Releases/Claude Code/claude-code-2026-05-06-v2-1-129-github-317982632-ec56fc0f|v2.1.129]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added `--plugin-url <url>` flag to fetch a plugin `.zip` archive from a URL for the current session

> Plugin manifests: `themes` and `monitors` should now be declared under `"experimental": { ... }`. Top-level declarations still work but `claude plugin validate` will warn

> The `claude_code.pull_request.count` OTel metric now counts PRs/MRs created via MCP tools, not just shell commands

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.129
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-05-06-2-model-support-changes-in-v2-1-129|2 Model Support changes in v2.1.129]] · Model Support
- [[Changes/Claude Code/2026-05-06-2-developer-workflow-changes-in-v2-1-129|2 Developer Workflow changes in v2.1.129]] · Developer Workflow
- [[Changes/Claude Code/2026-05-06-3-interface-experience-changes-in-v2-1-129|3 Interface Experience changes in v2.1.129]] · Interface Experience
- [[Changes/Claude Code/2026-05-06-fixed-session-title-chip-from-rename-disappearing-while-a-permission-or-other-di|Fixed session title chip from /rename disappearing while a permission or other…]] · Safety and Privacy
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-05-06 · Claude Code · [[Changes/Claude Code/2026-05-06-added-claude-code-session-id-environment-variable-to-the-bash-tool-subprocess-en|Added CLAUDE_CODE_SESSION_ID environment variable to the Bash tool subprocess…]]
- Later: 2026-05-07 · Claude Code · [[Changes/Claude Code/2026-05-07-2-apps-and-integrations-changes-in-v2-1-133|2 Apps and Integrations changes in v2.1.133]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-05-06-d93bf0&body=Card%3A%20Changes%2FClaude%20Code%2F2026-05-06-3-apps-and-integrations-changes-in-v2-1-129.md%0ACard%20ID%3A%20claude-code-2026-05-06-d93bf0%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.129%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->