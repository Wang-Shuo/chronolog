---
card_id: claude-code-2026-09-09-fd283c
date: '2026-09-09'
description: 'Claude Code · 2026-09-09 · Other changes: 3 changes in v2.1.267 — Added
  `--system-prompt-snapshot off` to render the system prompt fresh on every request…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: a8b3d6d0101dbac37d84165c6b9c8fb10e508056b4aecdb1578250de3dc65594
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-09-09-fd283c
  comparison: ''
  date: '2026-09-09'
  description: 'Claude Code — v2.1.267: 3 other changes'
  evidence:
  - quote: Added `--system-prompt-snapshot off` to render the system prompt fresh
      on every request instead of reusing the conversation's recorded prompt (for
      iterating on prompt text)
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.267
  - quote: 'Improved Artifact tool publish errors: when a publish is refused, the
      message now says why and what to do about it'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.267
  - quote: 'Gateway: Changed `forward_user_identity` upstreams to return a 429 as-is
      to a developer whose email was forwarded, instead of failing over to the next
      upstream, so the proxy''s per-user limits hold'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.267
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 3-other-changes-in-v2-1-267
  source_release: claude-code-2026-09-09-v2-1-267-github-385748811-6409148e
  source_type: github_releases
  theme: uncategorized
  title: 3 other changes in v2.1.267
  type: change
source_release: '[[Releases/Claude Code/claude-code-2026-09-09-v2-1-267-github-385748811-6409148e|claude-code-2026-09-09-v2-1-267-github-385748811-6409148e]]'
source_type: github_releases
theme: uncategorized
title: 3 other changes in v2.1.267
type: change
---

<!-- chronolog:begin region="header" -->
# 3 other changes in v2.1.267

**Claude Code** · 2026-09-09 · Other changes · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.267) · from [[Releases/Claude Code/claude-code-2026-09-09-v2-1-267-github-385748811-6409148e|v2.1.267]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added `--system-prompt-snapshot off` to render the system prompt fresh on every request instead of reusing the conversation's recorded prompt (for iterating on prompt text)

> Improved Artifact tool publish errors: when a publish is refused, the message now says why and what to do about it

> Gateway: Changed `forward_user_identity` upstreams to return a 429 as-is to a developer whose email was forwarded, instead of failing over to the next upstream, so the proxy's per-user limits hold

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.267
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-09-09-3-developer-workflow-changes-in-v2-1-267|3 Developer Workflow changes in v2.1.267]] · Developer Workflow
- [[Changes/Claude Code/2026-09-09-improved-the-diff-panel-it-no-longer-flashes-0-files-changed-and-a-spinner-befor|Improved the /diff panel]] · Interface Experience
- [[Changes/Claude Code/2026-09-09-improved-prompt-cache-stability-subagents-and-sessions-started-with-system-promp|Improved prompt-cache stability]] · Context Window
- [[Changes/Claude Code/2026-09-09-claude-tag-added-a-use-a-custom-connector-link-to-the-preset-connection-forms-in|Claude Tag Added a "Use a custom connector" link to the preset connection forms…]] · Apps and Integrations
- [[Changes/Claude Code/2026-09-09-2-safety-and-privacy-changes-in-v2-1-267|2 Safety and Privacy changes in v2.1.267]] · Safety and Privacy
- [[Changes/Claude Code/2026-09-09-improved-prompt-input-responsiveness-keystrokes-no-longer-occasionally-wait-a-fr|Improved prompt input responsiveness]] · Reliability and Performance
- [[Changes/Claude Code/2026-09-09-added-maxeffortlevel-setting-top-level-or-per-model-under-modelsettings-caps-the|Added maxEffortLevel setting (top-level or per model under modelSettings)]] · Model Support
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-09-09-fd283c&body=Card%3A%20Changes%2FClaude%20Code%2F2026-09-09-3-other-changes-in-v2-1-267.md%0ACard%20ID%3A%20claude-code-2026-09-09-fd283c%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.267%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->