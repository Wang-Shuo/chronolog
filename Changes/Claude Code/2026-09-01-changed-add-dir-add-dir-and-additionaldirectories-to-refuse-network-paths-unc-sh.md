---
card_id: claude-code-2026-09-01-c543bc
date: '2026-09-01'
description: 'Claude Code · 2026-09-01 · Mobile and Desktop: Changed `--add-dir`,
  `/add-dir`, and `additionalDirectories` to refuse network paths (UNC shares, `/net/<host>`…'
diffusion:
  first_in_tracked: "[[Changes/Cursor/2023-03-14-windows-and-linux-support|Windows
    and Linux support \U0001F973]]"
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1267
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: mobile-desktop
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: change
machine_hash: ac99d25edc3fdeb2ca1e59956c73e2f08ae30bdb1a3466f1fb315dd83baac127
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-09-01-c543bc
  comparison: ''
  date: '2026-09-01'
  description: 'Claude Code — v2.1.257: Changed `--add-dir`, `/add-dir`, and `additionalDirectories`
    to refuse network paths (UNC shares, `/net/<host>` automounts) with a message
    before touching them; on Windows use a mapped drive letter'
  evidence:
  - quote: Changed `--add-dir`, `/add-dir`, and `additionalDirectories` to refuse
      network paths (UNC shares, `/net/<host>` automounts) with a message before touching
      them; on Windows use a mapped drive letter
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.257
  extractor_version: fallback-v5
  impact: incremental
  kind: change
  product: claude-code
  product_name: Claude Code
  slug: changed-add-dir-add-dir-and-additionaldirectories-to-refuse-network-paths-unc-sh
  source_release: claude-code-2026-09-01-v2-1-257-github-380686035-b86855a6
  source_type: github_releases
  theme: mobile-desktop
  theme_matches: []
  theme_resolution: manual-semantic-rule-v1
  title: Changed `--add-dir`, `/add-dir`, and `additionalDirectories` to refuse network
    paths…
  type: change
related_changes:
- '[[Changes/ChatGPT/2026-08-31-chatgpt-work-and-codex-can-now-use-tools-that-supported-websites-provide-directl|ChatGPT
  Work and Codex can now use tools that supported websites provide directly…]]'
- '[[Changes/ChatGPT/2026-08-31-bring-your-browser-into-work-and-codex-mention-open-tabs-to-use-them-as-context-af2c3a|Bring
  your browser into Work and Codex]]'
- '[[Changes/ChatGPT/2026-08-31-site-tools-use-webmcp-and-require-a-supported-account-model-and-webpage-they-are|Site
  tools use WebMCP and require a supported account, model, and webpage]]'
source_release: '[[Releases/Claude Code/claude-code-2026-09-01-v2-1-257-github-380686035-b86855a6|claude-code-2026-09-01-v2-1-257-github-380686035-b86855a6]]'
source_type: github_releases
theme: mobile-desktop
title: Changed --add-dir, /add-dir, and additionalDirectories to refuse network paths…
type: change
---

<!-- chronolog:begin region="header" -->
# Changed `--add-dir`, `/add-dir`, and `additionalDirectories` to refuse network paths…

**Claude Code** · 2026-09-01 · [[Themes/mobile-desktop|Mobile and Desktop]] · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.257) · from [[Releases/Claude Code/claude-code-2026-09-01-v2-1-257-github-380686035-b86855a6|v2.1.257]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Changed `--add-dir`, `/add-dir`, and `additionalDirectories` to refuse network paths (UNC shares, `/net/<host>` automounts) with a message before touching them; on Windows use a mapped drive letter
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.257
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-09-01-2-editor-experience-changes-in-v2-1-257|2 Editor Experience changes in v2.1.257]] · Editor Experience
- [[Changes/Claude Code/2026-09-01-3-developer-workflow-changes-in-v2-1-257|3 Developer Workflow changes in v2.1.257]] · Developer Workflow
- [[Changes/Claude Code/2026-09-01-improved-prompt-input-responsiveness-by-reducing-per-keystroke-rendering-work|Improved prompt input responsiveness by reducing per-keystroke rendering work]] · Reliability and Performance
- [[Changes/Claude Code/2026-09-01-5-agent-mode-changes-in-v2-1-257|5 Agent Mode changes in v2.1.257]] · Agent Mode
- [[Changes/Claude Code/2026-09-01-changed-btw-history-browsing-from-to-shift-shift-or-stepping-through-your-recent|Changed /btw history browsing from ←/→ to Shift+←/Shift+→ (or /)…]] · Search and Browsing
- [[Changes/Claude Code/2026-09-01-10-safety-and-privacy-changes-in-v2-1-257|10 Safety and Privacy changes in v2.1.257]] · Safety and Privacy
- [[Changes/Claude Code/2026-09-01-2-apps-and-integrations-changes-in-v2-1-257|2 Apps and Integrations changes in v2.1.257]] · Apps and Integrations
- [[Changes/Claude Code/2026-09-01-2-account-and-access-changes-in-v2-1-257|2 Account and Access changes in v2.1.257]] · Account and Access
- [[Changes/Claude Code/2026-09-01-2-interface-experience-changes-in-v2-1-257|2 Interface Experience changes in v2.1.257]] · Interface Experience
- [[Changes/Claude Code/2026-09-01-6-model-support-changes-in-v2-1-257|6 Model Support changes in v2.1.257]] · Model Support
- [[Changes/Claude Code/2026-09-01-7-other-changes-in-v2-1-257|7 other changes in v2.1.257]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Mobile and Desktop

- Earlier: 2026-08-31 · ChatGPT · [[Changes/ChatGPT/2026-08-31-site-tools-use-webmcp-and-require-a-supported-account-model-and-webpage-they-are|Site tools use WebMCP and require a supported account, model, and webpage]]
- Later: 2026-09-02 · Cursor · [[Changes/Cursor/2026-09-02-computer-use-on-linux-and-mac|Computer use on Linux and Mac]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-14 · Cursor · [[Changes/Cursor/2023-03-14-windows-and-linux-support|Windows and Linux support 🥳]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-09-01-c543bc&body=Card%3A%20Changes%2FClaude%20Code%2F2026-09-01-changed-add-dir-add-dir-and-additionaldirectories-to-refuse-network-paths-unc-sh.md%0ACard%20ID%3A%20claude-code-2026-09-01-c543bc%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.257%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->