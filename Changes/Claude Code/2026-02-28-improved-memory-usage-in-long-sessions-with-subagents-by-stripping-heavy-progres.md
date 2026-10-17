---
card_id: claude-code-2026-02-28-cc4a28
date: '2026-02-28'
description: 'Claude Code · 2026-02-28 · Reliability and Performance: Improved memory
  usage in long sessions with subagents by stripping heavy progress message payloads…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General
    performance: Among other improvements, users will notice that ChatGPT is now…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1171
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: change
machine_hash: 2084ce8e4d29edc3c20471566e6894b0ce6d758f328ed05bd5cf90a4bb01149c
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-02-28-cc4a28
  comparison: ''
  date: '2026-02-28'
  description: 'Claude Code — v2.1.63: Improved memory usage in long sessions with
    subagents by stripping heavy progress message payloads during context compaction'
  evidence:
  - quote: Improved memory usage in long sessions with subagents by stripping heavy
      progress message payloads during context compaction
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.63
  extractor_version: fallback-v5
  impact: incremental
  kind: change
  product: claude-code
  product_name: Claude Code
  slug: improved-memory-usage-in-long-sessions-with-subagents-by-stripping-heavy-progres
  source_release: claude-code-2026-02-28-v2-1-63-github-291579549-8767ab9c
  source_type: github_releases
  theme: reliability-performance
  theme_matches:
  - matched_terms:
    - memory
    score: 110
    theme: memory
  - matched_terms:
    - subagents
    score: 50
    theme: agent-mode
  - matched_terms:
    - context
    score: 50
    theme: context-window
  theme_resolution: manual-semantic-rule-v2
  title: Improved memory usage in long sessions with subagents by stripping heavy
    progress…
  type: change
related_changes:
- '[[Changes/Claude Code/2026-02-20-3-reliability-and-performance-changes-in-v2-1-50|3
  Reliability and Performance changes in v2.1.50]]'
- '[[Changes/Claude Code/2026-02-26-improved-memory-usage-in-multi-agent-sessions-by-releasing-completed-subagent-ta|Improved
  memory usage in multi-agent sessions by releasing completed subagent task state]]'
- '[[Changes/ChatGPT/2026-02-27-faster-sharing-sharing-chats-is-now-easier-and-faster-with-a-quicker-loading-sha|Faster
  sharing. Sharing chats is now easier and faster, with a quicker-loading share menu]]'
source_release: '[[Releases/Claude Code/claude-code-2026-02-28-v2-1-63-github-291579549-8767ab9c|claude-code-2026-02-28-v2-1-63-github-291579549-8767ab9c]]'
source_type: github_releases
theme: reliability-performance
title: Improved memory usage in long sessions with subagents by stripping heavy progress…
type: change
---

<!-- chronolog:begin region="header" -->
# Improved memory usage in long sessions with subagents by stripping heavy progress…

**Claude Code** · 2026-02-28 · [[Themes/reliability-performance|Reliability and Performance]] · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.63) · from [[Releases/Claude Code/claude-code-2026-02-28-v2-1-63-github-291579549-8767ab9c|v2.1.63]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Improved memory usage in long sessions with subagents by stripping heavy progress message payloads during context compaction
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.63
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-02-28-fixed-listener-leak-in-interactive-permission-handler-during-auto-approvals|Fixed listener leak in interactive permission handler during auto-approvals]] · Safety and Privacy
- [[Changes/Claude Code/2026-02-28-added-manual-url-paste-fallback-during-mcp-oauth-authentication-if-the-automatic|Added manual URL paste fallback during MCP OAuth authentication]] · Account and Access
- [[Changes/Claude Code/2026-02-28-project-configs-auto-memory-now-shared-across-git-worktrees-of-the-same-reposito|Project configs & auto memory now shared across git worktrees of the same repository]] · Memory and Personalization
- [[Changes/Claude Code/2026-02-28-improved-model-command-to-show-the-currently-active-model-in-the-slash-command-m|Improved /model command to show the currently active model in the slash command menu]] · Developer Workflow
- [[Changes/Claude Code/2026-02-28-added-always-copy-full-response-option-to-the-copy-picker-when-selected-future-c|Added "Always copy full response" option to the /copy picker]] · Interface Experience
- [[Changes/Claude Code/2026-02-28-added-http-hooks-which-can-post-json-to-a-url-and-receive-json-instead-of-runnin|Added HTTP hooks, which can POST JSON to a URL and receive JSON instead of running…]] · Agent Mode
- [[Changes/Claude Code/2026-02-28-added-enable-claudeai-mcp-servers-false-env-var-to-opt-out-from-making-claude-ai|Added ENABLE_CLAUDEAI_MCP_SERVERS=false env var to opt out from making claude.ai…]] · Apps and Integrations
- [[Changes/Claude Code/2026-02-28-added-simplify-and-batch-bundled-slash-commands|Added /simplify and /batch bundled slash commands]] · Developer Workflow
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Reliability and Performance

- Earlier: 2026-02-27 · ChatGPT · [[Changes/ChatGPT/2026-02-27-faster-sharing-sharing-chats-is-now-easier-and-faster-with-a-quicker-loading-sha|Faster sharing. Sharing chats is now easier and faster, with a quicker-loading share menu]]
- Later: 2026-03-03 · Cursor · [[Changes/Cursor/2026-03-03-modals-load-faster|Modals load faster]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2022-12-15 · ChatGPT · [[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General performance: Among other improvements, users will notice that ChatGPT is now…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-02-28-cc4a28&body=Card%3A%20Changes%2FClaude%20Code%2F2026-02-28-improved-memory-usage-in-long-sessions-with-subagents-by-stripping-heavy-progres.md%0ACard%20ID%3A%20claude-code-2026-02-28-cc4a28%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.63%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->