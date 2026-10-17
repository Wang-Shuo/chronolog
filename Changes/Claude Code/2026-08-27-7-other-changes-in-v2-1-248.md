---
card_id: claude-code-2026-08-27-86489a
date: '2026-08-27'
description: 'Claude Code · 2026-08-27 · Other changes: 7 changes in v2.1.248 — Added
  `--restricted` (or `CLAUDE_CODE_RESTRICTED=1`): removes the built-in tools that
  run…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 77a6c6a9fd485f72e4f8c6795615ba1d069486a66e56e5aa696c5d650cb07391
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-08-27-86489a
  comparison: ''
  date: '2026-08-27'
  description: 'Claude Code — v2.1.248: 7 other changes'
  evidence:
  - quote: 'Added `--restricted` (or `CLAUDE_CODE_RESTRICTED=1`): removes the built-in
      tools that run commands or code and `WebFetch` (unless named in `--tools`),
      keeps file tools inside the working directory, refuses `bypassPermissions`,
      and ignores user, project and local settings files'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.248
  - quote: 'Added `claude self-hosted-runner --client-label <label>` (or `SELF_HOSTED_RUNNER_CLIENT_LABEL`)
      to override the label the runner registers with (default: hostname)'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.248
  - quote: Added a warning in `/web-setup` when the GitHub CLI token lacks the `workflow`
      scope, since pushes to very large repositories can be rejected without it
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.248
  - quote: Added cross-session messaging (`SendMessage` / `ListAgents`) between sessions
      on the same machine on Bedrock, Vertex, and Foundry, and when telemetry is disabled
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.248
  - quote: Improved `/ultrareview <PR#>` to check before launch that the GitHub account
      connected to your Claude account can access the repository, and to explain how
      to fix it, instead of failing after the cloud session starts
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.248
  - quote: 'Improved cross-session messaging: falls back to a private per-user `/tmp`
      directory when the default one can''t be used, and the notice and `/status`
      name the directory to fix'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.248
  - quote: 'Changed cross-session messaging in Linux user namespaces: root-equivalent
      trust for unmapped owners is limited to canonical system directories'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.248
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 7-other-changes-in-v2-1-248
  source_release: claude-code-2026-08-27-v2-1-248-github-378106990-677106e3
  source_type: github_releases
  theme: uncategorized
  title: 7 other changes in v2.1.248
  type: change
source_release: '[[Releases/Claude Code/claude-code-2026-08-27-v2-1-248-github-378106990-677106e3|claude-code-2026-08-27-v2-1-248-github-378106990-677106e3]]'
source_type: github_releases
theme: uncategorized
title: 7 other changes in v2.1.248
type: change
---

<!-- chronolog:begin region="header" -->
# 7 other changes in v2.1.248

**Claude Code** · 2026-08-27 · Other changes · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.248) · from [[Releases/Claude Code/claude-code-2026-08-27-v2-1-248-github-378106990-677106e3|v2.1.248]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added `--restricted` (or `CLAUDE_CODE_RESTRICTED=1`): removes the built-in tools that run commands or code and `WebFetch` (unless named in `--tools`), keeps file tools inside the working directory, refuses `bypassPermissions`, and ignores user, project and local settings files

> Added `claude self-hosted-runner --client-label <label>` (or `SELF_HOSTED_RUNNER_CLIENT_LABEL`) to override the label the runner registers with (default: hostname)

> Added a warning in `/web-setup` when the GitHub CLI token lacks the `workflow` scope, since pushes to very large repositories can be rejected without it

> Added cross-session messaging (`SendMessage` / `ListAgents`) between sessions on the same machine on Bedrock, Vertex, and Foundry, and when telemetry is disabled

> Improved `/ultrareview <PR#>` to check before launch that the GitHub account connected to your Claude account can access the repository, and to explain how to fix it, instead of failing after the cloud session starts

> Improved cross-session messaging: falls back to a private per-user `/tmp` directory when the default one can't be used, and the notice and `/status` name the directory to fix

> Changed cross-session messaging in Linux user namespaces: root-equivalent trust for unmapped owners is limited to canonical system directories

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.248
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-08-27-changed-anthropic-telemetry-export-failures-to-log-at-debug-level-as-anthropic-t|Changed Anthropic telemetry export failures to log at debug level…]] · Developer Workflow
- [[Changes/Claude Code/2026-08-27-added-usage-credits-for-enterprise-organizations-billed-through-aws-marketplace|Added /usage-credits for Enterprise organizations billed through AWS Marketplace…]] · Pricing Model
- [[Changes/Claude Code/2026-08-27-2-interface-experience-changes-in-v2-1-248|2 Interface Experience changes in v2.1.248]] · Interface Experience
- [[Changes/Claude Code/2026-08-27-4-safety-and-privacy-changes-in-v2-1-248|4 Safety and Privacy changes in v2.1.248]] · Safety and Privacy
- [[Changes/Claude Code/2026-08-27-3-agent-mode-changes-in-v2-1-248|3 Agent Mode changes in v2.1.248]] · Agent Mode
- [[Changes/Claude Code/2026-08-27-improved-the-workflow-tool-s-prompt-footprint-its-description-is-now-about-1k-to|Improved the Workflow tool's prompt footprint]] · Context Window
- [[Changes/Claude Code/2026-08-27-improved-managed-settings-client-side-timeout-mcp-startup-mode-and-stream-watchd|Improved managed settings]] · Apps and Integrations
- [[Changes/Claude Code/2026-08-27-changed-loop-self-paced-dynamic-mode-and-the-no-prompt-autonomous-default-are-no|Changed /loop: self-paced dynamic mode and the no-prompt autonomous default…]] · Automation and Scheduling
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-08-27-86489a&body=Card%3A%20Changes%2FClaude%20Code%2F2026-08-27-7-other-changes-in-v2-1-248.md%0ACard%20ID%3A%20claude-code-2026-08-27-86489a%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.248%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->