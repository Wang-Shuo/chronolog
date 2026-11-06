---
card_id: github-copilot-cli-2026-07-20-a65114
date: '2026-07-20'
description: 'GitHub Copilot CLI · 2026-07-20 · Other changes: 13 changes in 1.0.72
  — Corrected the added-line count shown when creating a file so files ending in a
  trailing…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 1b151e8143db0568f79e5169cb77dd2a87fd56c71fac3d40ea308bfbe3765ddf
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-07-20-a65114
  comparison: ''
  date: '2026-07-20'
  description: 'GitHub Copilot CLI — 1.0.72: 13 other changes'
  evidence:
  - quote: Corrected the added-line count shown when creating a file so files ending
      in a trailing newline no longer report one extra line
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.72
  - quote: Show the exit resume hint for a renamed session with no messages when its
      workspace is only available as a cached snapshot
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.72
  - quote: Session exports keep angle brackets intact in inline code and top-level
      fenced code blocks
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.72
  - quote: Pad inline hex color swatches once inside Markdown lists
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.72
  - quote: 'Nested markdown lists render correctly in buffered output (`-p --stream
      off` and detail screens): sub-bullets are no longer glued onto the parent item''s
      line or flattened, and are indented under their parent'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.72
  - quote: Show default values in /settings and let booleans cycle back to default
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.72
  - quote: Mask secret values in /settings show output
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.72
  - quote: Show hex color codes written as inline code (e.g. `#FF0000`) as color swatches,
      and add a renderHexColors setting (on by default) to toggle hex-color swatches
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.72
  - quote: Wrap ask-user and elicitation inputs in the split-pane chat view
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.72
  - quote: Reveal full file paths when expanding compact editing rows
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.72
  - quote: Make the plan-approval menu deterministic across models
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.72
  - quote: Enable tool search for Claude Haiku 4.5+
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.72
  - quote: 'Emoji shortcodes like :tada: no longer render with a spurious trailing
      space in printed and PR/issue/gist output'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.72
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 13-other-changes-in-v1-0-72
  source_release: github-copilot-cli-2026-07-20-v1-0-72-github-356903706-84b07b91
  source_type: github_releases
  theme: uncategorized
  title: 13 other changes in v1.0.72
  type: change
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-07-20-v1-0-72-github-356903706-84b07b91|github-copilot-cli-2026-07-20-v1-0-72-github-356903706-84b07b91]]'
source_type: github_releases
theme: uncategorized
title: 13 other changes in v1.0.72
type: change
---

<!-- chronolog:begin region="header" -->
# 13 other changes in v1.0.72

**GitHub Copilot CLI** · 2026-07-20 · Other changes · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.72) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-07-20-v1-0-72-github-356903706-84b07b91|1.0.72]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Corrected the added-line count shown when creating a file so files ending in a trailing newline no longer report one extra line

> Show the exit resume hint for a renamed session with no messages when its workspace is only available as a cached snapshot

> Session exports keep angle brackets intact in inline code and top-level fenced code blocks

> Pad inline hex color swatches once inside Markdown lists

> Nested markdown lists render correctly in buffered output (`-p --stream off` and detail screens): sub-bullets are no longer glued onto the parent item's line or flattened, and are indented under their parent

> Show default values in /settings and let booleans cycle back to default

> Mask secret values in /settings show output

> Show hex color codes written as inline code (e.g. `#FF0000`) as color swatches, and add a renderHexColors setting (on by default) to toggle hex-color swatches

> Wrap ask-user and elicitation inputs in the split-pane chat view

> Reveal full file paths when expanding compact editing rows

> Make the plan-approval menu deterministic across models

> Enable tool search for Claude Haiku 4.5+

> Emoji shortcodes like :tada: no longer render with a spurious trailing space in printed and PR/issue/gist output

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.72
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-07-20-the-sessions-sidebar-is-now-navigable-with-the-keyboard-and-mouse-arrows-open-an|The Sessions sidebar is now navigable with the keyboard and mouse…]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-07-20-8-developer-workflow-changes-in-v1-0-72|8 Developer Workflow changes in v1.0.72]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-07-20-2-context-window-changes-in-v1-0-72|2 Context Window changes in v1.0.72]] · Context Window
- [[Changes/GitHub Copilot CLI/2026-07-20-10-apps-and-integrations-changes-in-v1-0-72|10 Apps and Integrations changes in v1.0.72]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-07-20-4-safety-and-privacy-changes-in-v1-0-72|4 Safety and Privacy changes in v1.0.72]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-07-20-preserve-pasted-prompt-content-when-changing-models-through-ctrl-x-model|Preserve pasted prompt content when changing models through Ctrl+X /model]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-07-20-3-agent-mode-changes-in-v1-0-72|3 Agent Mode changes in v1.0.72]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-07-20-2-editor-experience-changes-in-v1-0-72|2 Editor Experience changes in v1.0.72]] · Editor Experience
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-07-20-a65114&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-07-20-13-other-changes-in-v1-0-72.md%0ACard%20ID%3A%20github-copilot-cli-2026-07-20-a65114%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.72%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->