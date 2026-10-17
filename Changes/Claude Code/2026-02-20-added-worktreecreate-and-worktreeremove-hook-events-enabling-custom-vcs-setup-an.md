---
card_id: claude-code-2026-02-20-648196
date: '2026-02-20'
description: 'Claude Code · 2026-02-20 · Developer Workflow: Added `WorktreeCreate`
  and `WorktreeRemove` hook events, enabling custom VCS setup and teardown when agent…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1070
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v4
impact: paradigm-shift
machine_hash: 8d371b4012dd21564191cc5349ef8e15e5616dc003bfc910760ea38a6525d448
product: claude-code
product_name: Claude Code
record:
  ai_generated: true
  card_id: claude-code-2026-02-20-648196
  comparison: ''
  confidence: low
  date: '2026-02-20'
  description: 'Claude Code — v2.1.50: Added `WorktreeCreate` and `WorktreeRemove`
    hook events, enabling custom VCS setup and teardown when agent worktree isolation
    creates or removes worktrees.'
  evidence:
  - quote: Added `WorktreeCreate` and `WorktreeRemove` hook events, enabling custom
      VCS setup and teardown when agent worktree isolation creates or removes worktrees.
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.50
  extractor_version: fallback-v4
  impact: paradigm-shift
  product: claude-code
  product_name: Claude Code
  slug: added-worktreecreate-and-worktreeremove-hook-events-enabling-custom-vcs-setup-an
  source_release: claude-code-2026-02-20-v2-1-50-github-288920711-09694b82
  source_type: github_releases
  theme: developer-workflow
  theme_matches:
  - matched_terms:
    - agent
    score: 50
    theme: agent-mode
  - matched_terms:
    - worktree
    score: 50
    theme: developer-workflow
  theme_resolution: manual-semantic-rule-v1
  title: Added `WorktreeCreate` and `WorktreeRemove` hook events, enabling custom
    VCS setup…
  type: change
related_changes:
- '[[Changes/Claude Code/2026-02-10-improved-heredoc-delimiter-parsing-to-prevent-command-smuggling|Improved
  heredoc delimiter parsing to prevent command smuggling]]'
- '[[Changes/Cursor/2026-02-18-mermaid-code-blocks-now-render-inline-as-ascii-diagrams-in-your-cli-conversation|Mermaid
  code blocks now render inline as ASCII diagrams in your CLI conversation]]'
- '[[Changes/ChatGPT/2026-02-19-review-code-in-split-screen-views|Review code in split-screen
  views]]'
source_release: '[[Releases/Claude Code/claude-code-2026-02-20-v2-1-50-github-288920711-09694b82|claude-code-2026-02-20-v2-1-50-github-288920711-09694b82]]'
source_type: github_releases
superseded: true
theme: developer-workflow
title: Added WorktreeCreate and WorktreeRemove hook events, enabling custom VCS setup…
type: change
---

<!-- chronolog:begin region="header" -->
# Added `WorktreeCreate` and `WorktreeRemove` hook events, enabling custom VCS setup…

**Claude Code** · 2026-02-20 · [[Themes/developer-workflow|Developer Workflow]] · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.50) · from [[Releases/Claude Code/claude-code-2026-02-20-v2-1-50-github-288920711-09694b82|v2.1.50]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `WorktreeCreate` and `WorktreeRemove` hook events, enabling custom VCS setup and teardown when agent worktree isolation creates or removes worktrees.
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.50
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-02-20-added-support-for-isolation-worktree-in-agent-definitions-allowing-agents-to-dec|Added support for isolation: worktree in agent definitions, allowing agents…]] · Agent Mode
- [[Changes/Claude Code/2026-02-20-improved-memory-usage-during-long-sessions-by-clearing-internal-caches-after-com|Improved memory usage during long sessions by clearing internal caches after compaction]] · Reliability and Performance
- [[Changes/Claude Code/2026-02-20-claude-code-simple-mode-now-also-disables-mcp-tools-attachments-hooks-and-claude|CLAUDE_CODE_SIMPLE mode now also disables MCP tools, attachments, hooks…]] · Apps and Integrations
- [[Changes/Claude Code/2026-02-20-added-support-for-startuptimeout-configuration-for-lsp-servers|Added support for startupTimeout configuration for LSP servers]] · Developer Workflow
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-02-19 · ChatGPT · [[Changes/ChatGPT/2026-02-19-review-code-in-split-screen-views|Review code in split-screen views]]
- Later: 2026-02-24 · Claude Code · [[Changes/Claude Code/2026-02-24-bashtool-now-skips-login-shell-l-flag-by-default-when-a-shell-snapshot-is-availa|BashTool now skips login shell (-l flag) by default when a shell snapshot…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-18 · Cursor · [[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-02-20-648196&body=Card%3A%20Changes%2FClaude%20Code%2F2026-02-20-added-worktreecreate-and-worktreeremove-hook-events-enabling-custom-vcs-setup-an.md%0ACard%20ID%3A%20claude-code-2026-02-20-648196%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.50%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->