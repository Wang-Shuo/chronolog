---
card_id: ollama-2026-08-21-57367d
date: '2026-08-21'
description: 'Ollama · 2026-08-21 · Other changes: 4 changes in v0.33.0 — <img width="1298"
  height="780" alt="image"…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 30079b2e0e44965f3e6837a3a28bcf56bcaafc06f780149fe9d7440703b6f12e
product: ollama
product_name: Ollama
record:
  card_id: ollama-2026-08-21-57367d
  comparison: ''
  date: '2026-08-21'
  description: 'Ollama — v0.33.0: 4 other changes'
  evidence:
  - quote: <img width="1298" height="780" alt="image" src="https://github.com/user-attachments/assets/c02fd93b-f599-40a9-83c3-d0555c0ac182"
      />
    source_release: https://github.com/ollama/ollama/releases/tag/v0.33.0
  - quote: 'Prefill restore points are now trustworthy by construction: a cancelled
      prefill keeps every restore point it crossed, so retries resume where they stopped
      instead of restarting from scratch'
    source_release: https://github.com/ollama/ollama/releases/tag/v0.33.0
  - quote: Resumed prefills no longer record restore points that fail to cover what
      they claim; on models with recurrent layers this previously forced a request
      matching 46k of 47k tokens to reprocess from zero
    source_release: https://github.com/ollama/ollama/releases/tag/v0.33.0
  - quote: MLX dependency update (#17886)
    source_release: https://github.com/ollama/ollama/releases/tag/v0.33.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: ollama
  product_name: Ollama
  slug: 4-other-changes-in-v0-33-0
  source_release: ollama-2026-08-21-v0-33-0-github-374711587-19296eb8
  source_type: github_releases
  theme: uncategorized
  title: 4 other changes in v0.33.0
  type: change
source_release: '[[Releases/Ollama/ollama-2026-08-21-v0-33-0-github-374711587-19296eb8|ollama-2026-08-21-v0-33-0-github-374711587-19296eb8]]'
source_type: github_releases
theme: uncategorized
title: 4 other changes in v0.33.0
type: change
---

<!-- chronolog:begin region="header" -->
# 4 other changes in v0.33.0

**Ollama** · 2026-08-21 · Other changes · Digest · [Official source](https://github.com/ollama/ollama/releases/tag/v0.33.0) · from [[Releases/Ollama/ollama-2026-08-21-v0-33-0-github-374711587-19296eb8|v0.33.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> \<img width="1298" height="780" alt="image" src="https://github.com/user-attachments/assets/c02fd93b-f599-40a9-83c3-d0555c0ac182" />

> Prefill restore points are now trustworthy by construction: a cancelled prefill keeps every restore point it crossed, so retries resume where they stopped instead of restarting from scratch

> Resumed prefills no longer record restore points that fail to cover what they claim; on models with recurrent layers this previously forced a request matching 46k of 47k tokens to reprocess from zero

> MLX dependency update (#17886)

Source: https://github.com/ollama/ollama/releases/tag/v0.33.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Ollama/2026-08-21-disabled-claude-code-s-tokens-left-token-countdown-system-message-which-ollama-m|Disabled Claude Code's "tokens left" token-countdown system message, which Ollama…]] · Context Window
- [[Changes/Ollama/2026-08-21-developers-can-now-easily-configure-claude-desktop-to-seamlessly-work-with-ollam|Developers can now easily configure Claude Desktop to seamlessly work with Ollama…]] · Mobile and Desktop
- [[Changes/Ollama/2026-08-21-deepseek-harness-launcher-now-falls-back-to-npx-when-the-global-npm-install-fail|DeepSeek Harness launcher now falls back to npx when the global npm install fails…]] · Developer Workflow
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20ollama-2026-08-21-57367d&body=Card%3A%20Changes%2FOllama%2F2026-08-21-4-other-changes-in-v0-33-0.md%0ACard%20ID%3A%20ollama-2026-08-21-57367d%0ASource%3A%20https%3A%2F%2Fgithub.com%2Follama%2Follama%2Freleases%2Ftag%2Fv0.33.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->