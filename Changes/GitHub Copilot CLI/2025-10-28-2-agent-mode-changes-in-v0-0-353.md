---
card_id: github-copilot-cli-2025-10-28-7d494c
date: '2025-10-28'
description: 'GitHub Copilot CLI · 2025-10-28 · Agent Mode: 2 changes in 0.0.353 —
  Added support for custom agents. Custom agent definitions are pulled from…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 845
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: c21339637356b22f7f6148aec4e6f666144649c77a24e4511a6442dc1f0e3c0a
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2025-10-28-7d494c
  comparison: ''
  date: '2025-10-28'
  description: 'GitHub Copilot CLI — 0.0.353: 2 Agent Mode changes'
  evidence:
  - quote: Added support for custom agents. Custom agent definitions are pulled from
      `~/.copilot/agents`, `.github/agents` in your repository, or your organization's
      `.github` repository. You can explicitly invoke an agent with the `/agent` slash
      command interactively or `--agent <agent>` noninteractively. Agents are also
      provided as tools that the model can call during completion of a task
    source_release: https://github.com/github/copilot-cli/releases/tag/v0.0.353
  - quote: Added a `/delegate` command to delegate a task asynchronously to Copilot
      coding agent. Any unstaged changes will be committed to a new branch, a PR will
      be opened in your GitHub repository, and Copilot will complete work in the background.
    source_release: https://github.com/github/copilot-cli/releases/tag/v0.0.353
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 2-agent-mode-changes-in-v0-0-353
  source_release: github-copilot-cli-2025-10-28-v0-0-353-github-257902150-5c3db4c7
  source_type: github_releases
  theme: agent-mode
  title: 2 Agent Mode changes in v0.0.353
  type: change
related_changes:
- '[[Changes/ElevenLabs/2025-10-27-agents-platform|Agents Platform]]'
- '[[Changes/ElevenLabs/2025-10-27-agents-platform-b53aea|Agents Platform]]'
- '[[Changes/ElevenLabs/2025-10-27-agents-cli|Agents CLI]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2025-10-28-v0-0-353-github-257902150-5c3db4c7|github-copilot-cli-2025-10-28-v0-0-353-github-257902150-5c3db4c7]]'
source_type: github_releases
theme: agent-mode
title: 2 Agent Mode changes in v0.0.353
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Agent Mode changes in v0.0.353

**GitHub Copilot CLI** · 2025-10-28 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v0.0.353) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2025-10-28-v0-0-353-github-257902150-5c3db4c7|0.0.353]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added support for custom agents. Custom agent definitions are pulled from `~/.copilot/agents`, `.github/agents` in your repository, or your organization's `.github` repository. You can explicitly invoke an agent with the `/agent` slash command interactively or `--agent <agent>` noninteractively. Agents are also provided as tools that the model can call during completion of a task

> Added a `/delegate` command to delegate a task asynchronously to Copilot coding agent. Any unstaged changes will be committed to a new branch, a PR will be opened in your GitHub repository, and Copilot will complete work in the background.

Source: https://github.com/github/copilot-cli/releases/tag/v0.0.353
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2025-10-27 · ElevenLabs · [[Changes/ElevenLabs/2025-10-27-agents-cli|Agents CLI]]
- Later: 2025-10-29 · Cursor · [[Changes/Cursor/2025-10-29-browser-ga-1124ce|Browser (GA)]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2025-10-28-7d494c&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2025-10-28-2-agent-mode-changes-in-v0-0-353.md%0ACard%20ID%3A%20github-copilot-cli-2025-10-28-7d494c%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv0.0.353%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->