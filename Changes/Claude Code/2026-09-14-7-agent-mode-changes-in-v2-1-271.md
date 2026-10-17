---
card_id: claude-code-2026-09-14-b0ee32
date: '2026-09-14'
description: 'Claude Code · 2026-09-14 · Agent Mode: 7 changes in v2.1.271 — Added
  per-command `allowed_domains` to Bash, PowerShell and Monitor in auto mode with…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1166
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: a2d020d4f307b2ef213e60c6e320880cdb4b30f67cb3549c49a9ff63ec2eed2f
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-09-14-b0ee32
  comparison: ''
  date: '2026-09-14'
  description: 'Claude Code — v2.1.271: 7 Agent Mode changes'
  evidence:
  - quote: 'Added per-command `allowed_domains` to Bash, PowerShell and Monitor in
      auto mode with sandboxing: the hosts a command needs are reviewed with it and
      opened for it alone; other hosts are refused'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.271
  - quote: Added `omitClaudeMd` to agent frontmatter and `--agents` JSON, letting
      custom and plugin subagents run without user, project and local CLAUDE.md files;
      managed policy files still load
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.271
  - quote: Improved dynamic workflows to pause when you hit your usage limit and continue
      automatically when it resets, instead of dropping the affected agents
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.271
  - quote: 'Improved the Claude in Chrome message in cloud sessions when the browser
      can''t be reached: it now says the computer may be asleep before it suggests
      an install'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.271
  - quote: Changed auto mode so a subagent reports back to its caller through a dedicated
      hand-back call that the safety classifier reviews, instead of its last message
      being reviewed after the fact
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.271
  - quote: Changed the default dynamic workflow size to small on Pro plans and lowered
      the medium size guideline from 15 to 10 agents
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.271
  - quote: Updated the bundled `claude-api` skill to enable `eager_input_streaming`
      on streaming custom tools, and to start deliverable-shaped Managed Agents work
      with `user.define_outcome`
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.271
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 7-agent-mode-changes-in-v2-1-271
  source_release: claude-code-2026-09-14-v2-1-271-github-388664071-570fd44f
  source_type: github_releases
  theme: agent-mode
  title: 7 Agent Mode changes in v2.1.271
  type: change
related_changes:
- '[[Changes/Cursor/2026-09-10-a-project-runs-on-its-own-computer-in-the-cloud-so-closing-your-laptop-doesn-t-s|Powered
  by Cloud Agents]]'
- '[[Changes/Cursor/2026-09-10-subscriptions|Subscriptions]]'
- '[[Changes/Claude Code/2026-09-11-2-agent-mode-changes-in-v2-1-269|2 Agent Mode
  changes in v2.1.269]]'
source_release: '[[Releases/Claude Code/claude-code-2026-09-14-v2-1-271-github-388664071-570fd44f|claude-code-2026-09-14-v2-1-271-github-388664071-570fd44f]]'
source_type: github_releases
theme: agent-mode
title: 7 Agent Mode changes in v2.1.271
type: change
---

<!-- chronolog:begin region="header" -->
# 7 Agent Mode changes in v2.1.271

**Claude Code** · 2026-09-14 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.271) · from [[Releases/Claude Code/claude-code-2026-09-14-v2-1-271-github-388664071-570fd44f|v2.1.271]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added per-command `allowed_domains` to Bash, PowerShell and Monitor in auto mode with sandboxing: the hosts a command needs are reviewed with it and opened for it alone; other hosts are refused

> Added `omitClaudeMd` to agent frontmatter and `--agents` JSON, letting custom and plugin subagents run without user, project and local CLAUDE.md files; managed policy files still load

> Improved dynamic workflows to pause when you hit your usage limit and continue automatically when it resets, instead of dropping the affected agents

> Improved the Claude in Chrome message in cloud sessions when the browser can't be reached: it now says the computer may be asleep before it suggests an install

> Changed auto mode so a subagent reports back to its caller through a dedicated hand-back call that the safety classifier reviews, instead of its last message being reviewed after the fact

> Changed the default dynamic workflow size to small on Pro plans and lowered the medium size guideline from 15 to 10 agents

> Updated the bundled `claude-api` skill to enable `eager_input_streaming` on streaming custom tools, and to start deliverable-shaped Managed Agents work with `user.define_outcome`

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.271
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-09-14-changed-claude-apps-gateway-bedrock-vertex-ai-and-foundry-sessions-so-that-they|Changed Claude apps gateway, Bedrock, Vertex AI, and Foundry sessions so that they…]] · Account and Access
- [[Changes/Claude Code/2026-09-14-added-support-for-a-multiplier-above-1-up-to-10-in-the-modelpricing-managed-sett|Added support for a multiplier above 1, up to 10, in the modelPricing managed…]] · Pricing Model
- [[Changes/Claude Code/2026-09-14-2-files-and-data-changes-in-v2-1-271|2 Files and Data changes in v2.1.271]] · Files and Data
- [[Changes/Claude Code/2026-09-14-5-apps-and-integrations-changes-in-v2-1-271|5 Apps and Integrations changes in v2.1.271]] · Apps and Integrations
- [[Changes/Claude Code/2026-09-14-3-editor-experience-changes-in-v2-1-271|3 Editor Experience changes in v2.1.271]] · Editor Experience
- [[Changes/Claude Code/2026-09-14-7-safety-and-privacy-changes-in-v2-1-271|7 Safety and Privacy changes in v2.1.271]] · Safety and Privacy
- [[Changes/Claude Code/2026-09-14-improved-the-spinner-status-during-long-thinking-it-now-reads-deep-in-thought-af|Improved the spinner status during long thinking]] · Context Window
- [[Changes/Claude Code/2026-09-14-improved-terminal-rendering-performance-large-diffs-and-long-transcripts-render|Improved terminal rendering performance]] · Reliability and Performance
- [[Changes/Claude Code/2026-09-14-2-mobile-and-desktop-changes-in-v2-1-271|2 Mobile and Desktop changes in v2.1.271]] · Mobile and Desktop
- [[Changes/Claude Code/2026-09-14-3-interface-experience-changes-in-v2-1-271|3 Interface Experience changes in v2.1.271]] · Interface Experience
- [[Changes/Claude Code/2026-09-14-improved-startup-time-slightly-by-skipping-a-redundant-validation-of-built-in-mo|Improved startup time slightly by skipping a redundant validation of built-in model…]] · Model Support
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-09-11 · Claude Code · [[Changes/Claude Code/2026-09-11-2-agent-mode-changes-in-v2-1-269|2 Agent Mode changes in v2.1.269]]
- Later: 2026-09-15 · Claude Code · [[Changes/Claude Code/2026-09-15-changed-auto-mode-on-bedrock-vertex-and-foundry-to-use-the-local-classifier-by-d|Changed auto mode on Bedrock, Vertex and Foundry to use the local classifier…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-09-14-b0ee32&body=Card%3A%20Changes%2FClaude%20Code%2F2026-09-14-7-agent-mode-changes-in-v2-1-271.md%0ACard%20ID%3A%20claude-code-2026-09-14-b0ee32%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.271%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->