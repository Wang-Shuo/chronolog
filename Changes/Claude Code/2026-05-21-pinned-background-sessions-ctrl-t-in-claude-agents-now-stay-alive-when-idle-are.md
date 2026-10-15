---
card_id: claude-code-2026-05-21-608fad
date: '2026-05-21'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|chatgpt-2022-12-15-9c6f9c]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1253
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v4
impact: incremental
machine_hash: c95fa42a6c0447e506dba6dff2b7a5253472849a56bf1e504c1aad97b29f4a20
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-05-21-608fad
  comparison: ''
  date: '2026-05-21'
  description: 'Claude Code — v2.1.147: Pinned background sessions (`Ctrl+T` in `claude
    agents`) now stay alive when idle, are restarted in place to apply Claude Code
    updates, and are shed under memory pressure only after non-pinned sessions'
  evidence:
  - quote: Pinned background sessions (`Ctrl+T` in `claude agents`) now stay alive
      when idle, are restarted in place to apply Claude Code updates, and are shed
      under memory pressure only after non-pinned sessions
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.147
  extractor_version: fallback-v4
  impact: incremental
  product: claude-code
  product_name: Claude Code
  slug: pinned-background-sessions-ctrl-t-in-claude-agents-now-stay-alive-when-idle-are
  source_release: claude-code-2026-05-21-v2-1-147-github-327133263-73928fcd
  source_type: github_releases
  theme: reliability-performance
  theme_matches:
  - matched_terms:
    - memory
    score: 110
    theme: memory
  - matched_terms:
    - agents
    score: 50
    theme: agent-mode
  theme_resolution: manual-semantic-rule-v2
  title: Pinned background sessions (`Ctrl+T` in `claude agents`) now stay alive when
    idle…
  type: change
related_changes:
- '[[Changes/Claude Code/2026-05-21-improved-auto-updater-reliability-native-version-checks-and-downloads-now-retry|claude-code-2026-05-21-279dd2]]'
- '[[Changes/Claude Code/2026-05-21-improved-diff-rendering-performance-for-large-file-edits-4ddf04|claude-code-2026-05-21-4ddf04]]'
- '[[Changes/Claude Code/2026-05-21-improved-auto-updater-retries-transient-network-failures-reports-specific-error|claude-code-2026-05-21-4e9152]]'
source_release: '[[Releases/Claude Code/claude-code-2026-05-21-v2-1-147-github-327133263-73928fcd|claude-code-2026-05-21-v2-1-147-github-327133263-73928fcd]]'
source_type: github_releases
theme: reliability-performance
title: Pinned background sessions (Ctrl+T in claude agents) now stay alive when idle…
type: change
---

# Pinned background sessions (`Ctrl+T` in `claude agents`) now stay alive when idle…

<!-- chronolog:begin region="description" -->
Claude Code — v2.1.147: Pinned background sessions (`Ctrl+T` in `claude agents`) now stay alive when idle, are restarted in place to apply Claude Code updates, and are shed under memory pressure only after non-pinned sessions
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Pinned background sessions (`Ctrl+T` in `claude agents`) now stay alive when idle, are restarted in place to apply Claude Code updates, and are shed under memory pressure only after non-pinned sessions
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.147
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
No evidence-backed evolution relationship assigned.
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: reliability-performance
- Relation: same-theme-chronology
- Inference: No adoption, equivalence, or causation claim.
- Scope: tracked-products-only
- Role: later-observed
- First In Tracked: [[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|chatgpt-2022-12-15-9c6f9c]]
- Lag Days: 1253
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes