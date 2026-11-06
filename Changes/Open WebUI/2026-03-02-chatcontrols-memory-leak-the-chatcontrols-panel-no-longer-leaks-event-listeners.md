---
card_id: open-webui-2026-03-02-5a5994
date: '2026-03-02'
description: "Open WebUI · 2026-03-02 · Reliability and Performance: \U0001F9E0 **ChatControls
  memory leak.** The ChatControls panel no longer leaks event listeners, ResizeObserver…"
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General
    performance: Among other improvements, users will notice that ChatGPT is now…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1173
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: change
machine_hash: 66a1b0d9286a08a01f6c628bf579f08f962f7176cbc41e9f5c984fd7927f7a85
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-03-02-5a5994
  comparison: ''
  date: '2026-03-02'
  description: "Open WebUI — v0.8.7: \U0001F9E0 **ChatControls memory leak.** The
    ChatControls panel no longer leaks event listeners, ResizeObserver instances,
    and media query handlers when navigating between chats, fixing memory accumulation
    that could degrade performance during extended use. [#22112](https://github.com/open-webui/open-webui/pull/22112)"
  evidence:
  - quote: "\U0001F9E0 **ChatControls memory leak.** The ChatControls panel no longer
      leaks event listeners, ResizeObserver instances, and media query handlers when
      navigating between chats, fixing memory accumulation that could degrade performance
      during extended use. [#22112](https://github.com/open-webui/open-webui/pull/22112)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.8.7
  extractor_version: fallback-v5
  impact: incremental
  kind: change
  product: open-webui
  product_name: Open WebUI
  slug: chatcontrols-memory-leak-the-chatcontrols-panel-no-longer-leaks-event-listeners
  source_release: open-webui-2026-03-02-v0-8-7-github-291874841-d7aad0b1
  source_type: github_releases
  theme: reliability-performance
  theme_matches:
  - matched_terms:
    - memory
    score: 110
    theme: memory
  - matched_terms:
    - performance
    score: 50
    theme: reliability-performance
  theme_resolution: manual-semantic-rule-v2
  title: "\U0001F9E0 **ChatControls memory leak.** The ChatControls panel no longer
    leaks event…"
  type: change
related_changes:
- '[[Changes/Claude Code/2026-02-28-improved-memory-usage-in-long-sessions-with-subagents-by-stripping-heavy-progres|Improved
  memory usage in long sessions with subagents by stripping heavy progress…]]'
- '[[Changes/Open WebUI/2026-03-01-21-reliability-and-performance-changes-in-v0-8-6|21
  Reliability and Performance changes in v0.8.6]]'
- '[[Changes/Ollama/2026-03-02-ollama-run-verbose-will-now-show-peak-memory-usage-when-using-ollama-s-mlx-engin|ollama
  run --verbose will now show peak memory usage when using Ollama''s MLX engine]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-03-02-v0-8-7-github-291874841-d7aad0b1|open-webui-2026-03-02-v0-8-7-github-291874841-d7aad0b1]]'
source_type: github_releases
theme: reliability-performance
title: "\U0001F9E0 ChatControls memory leak. The ChatControls panel no longer leaks
  event…"
type: change
---

<!-- chronolog:begin region="header" -->
# 🧠 **ChatControls memory leak.** The ChatControls panel no longer leaks event…

**Open WebUI** · 2026-03-02 · [[Themes/reliability-performance|Reliability and Performance]] · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.8.7) · from [[Releases/Open WebUI/open-webui-2026-03-02-v0-8-7-github-291874841-d7aad0b1|v0.8.7]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> 🧠 **ChatControls memory leak.** The ChatControls panel no longer leaks event listeners, ResizeObserver instances, and media query handlers when navigating between chats, fixing memory accumulation that could degrade performance during extended use. [#22112](https://github.com/open-webui/open-webui/pull/22112)
>
> Source: https://github.com/open-webui/open-webui/releases/tag/v0.8.7
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-03-02-connection-access-control-privacy-tool-server-and-terminal-connections-without-e|🔒 Connection access control privacy. Tool server and terminal connections…]] · Safety and Privacy
- [[Changes/Open WebUI/2026-03-02-temporary-chat-params-preservation-model-parameters-are-now-correctly-saved-when|💾 Temporary chat params preservation. Model parameters are now correctly saved…]] · Model Support
- [[Changes/Open WebUI/2026-03-02-faster-artifact-content-updates-artifact-content-extraction-during-streaming-is|⚡ Faster artifact content updates. Artifact content extraction during streaming…]] · Developer Workflow
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Reliability and Performance

- Earlier: 2026-03-02 · Ollama · [[Changes/Ollama/2026-03-02-ollama-run-verbose-will-now-show-peak-memory-usage-when-using-ollama-s-mlx-engin|ollama run --verbose will now show peak memory usage when using Ollama's MLX engine]]
- Later: 2026-03-02 · Open WebUI · [[Changes/Open WebUI/2026-03-02-general-improvements-various-improvements-were-implemented-across-the-applicatio|🔄 General improvements. Various improvements were implemented across…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2022-12-15 · ChatGPT · [[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General performance: Among other improvements, users will notice that ChatGPT is now…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-03-02-5a5994&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-03-02-chatcontrols-memory-leak-the-chatcontrols-panel-no-longer-leaks-event-listeners.md%0ACard%20ID%3A%20open-webui-2026-03-02-5a5994%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.8.7%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->