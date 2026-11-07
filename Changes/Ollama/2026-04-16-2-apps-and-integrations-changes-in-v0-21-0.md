---
card_id: ollama-2026-04-16-e77609
date: '2026-04-16'
description: 'Ollama · 2026-04-16 · Apps and Integrations: 2 changes in v0.21.0 —
  **OpenCode moved to inline config.** `ollama launch opencode` now writes its config
  inline…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If
    you have a recording with each speaker with a different microphone, or saved…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2680
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 8e2b34bbe26d7595b8288f49351e161fc3a56d6cc2bf70bef601e7ee50431d07
product: ollama
product_name: Ollama
record:
  card_id: ollama-2026-04-16-e77609
  comparison: ''
  date: '2026-04-16'
  description: 'Ollama — v0.21.0: 2 Apps and Integrations changes'
  evidence:
  - quote: '**OpenCode moved to inline config.** `ollama launch opencode` now writes
      its config inline rather than to a separate file, matching how other integrations
      are handled.'
    source_release: https://github.com/ollama/ollama/releases/tag/v0.21.0
  - quote: '**`ollama launch` no longer rewrites config when nothing changed.** Pressing
      → on a configured multi-model integration, or passing `--model` with the current
      primary, used to trigger a confirmation prompt and rewrite both the editor''s
      config file and `config.json`. Now it''s a no-op when the resolved model list
      matches what''s already saved.'
    source_release: https://github.com/ollama/ollama/releases/tag/v0.21.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: ollama
  product_name: Ollama
  slug: 2-apps-and-integrations-changes-in-v0-21-0
  source_release: ollama-2026-04-16-v0-21-0-github-310055812-cddcf12c
  source_type: github_releases
  theme: apps-integrations
  title: 2 Apps and Integrations changes in v0.21.0
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-04-16-2-apps-and-integrations-changes-in-v1-0-30|2
  Apps and Integrations changes in v1.0.30]]'
- '[[Changes/GitHub Copilot CLI/2026-04-16-mcp-migration-hint-now-links-to-documentation-with-platform-specific-instruction|MCP
  migration hint now links to documentation with platform-specific instructions…]]'
- '[[Changes/GitHub Copilot CLI/2026-04-16-3-apps-and-integrations-changes-in-v1-0-29|3
  Apps and Integrations changes in v1.0.29]]'
source_release: '[[Releases/Ollama/ollama-2026-04-16-v0-21-0-github-310055812-cddcf12c|ollama-2026-04-16-v0-21-0-github-310055812-cddcf12c]]'
source_type: github_releases
theme: apps-integrations
title: 2 Apps and Integrations changes in v0.21.0
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Apps and Integrations changes in v0.21.0

**Ollama** · 2026-04-16 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/ollama/ollama/releases/tag/v0.21.0) · from [[Releases/Ollama/ollama-2026-04-16-v0-21-0-github-310055812-cddcf12c|v0.21.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> **OpenCode moved to inline config.** `ollama launch opencode` now writes its config inline rather than to a separate file, matching how other integrations are handled.

> **`ollama launch` no longer rewrites config when nothing changed.** Pressing → on a configured multi-model integration, or passing `--model` with the current primary, used to trigger a confirmation prompt and rewrite both the editor's config file and `config.json`. Now it's a no-op when the resolved model list matches what's already saved.

Source: https://github.com/ollama/ollama/releases/tag/v0.21.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Ollama/2026-04-16-hermes-and-github-copilot-cli-in-ollama-launch-added-both-integrations-which-can|Hermes and GitHub Copilot CLI in ollama launch. Added both integrations…]] · Editor Experience
- [[Changes/Ollama/2026-04-16-fixed-macos-cross-compiles-so-they-no-longer-trigger-generate-which-was-breaking|Fixed macOS cross-compiles so they no longer trigger generate…]] · Mobile and Desktop
- [[Changes/Ollama/2026-04-16-gemma-4-on-mlx-added-support-for-running-gemma-4-via-mlx-on-apple-silicon-includ|Gemma 4 on MLX. Added support for running Gemma 4 via MLX on Apple Silicon…]] · Model Support
- [[Changes/Ollama/2026-04-16-6-other-changes-in-v0-21-0|6 other changes in v0.21.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-04-16 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-04-16-3-apps-and-integrations-changes-in-v1-0-29|3 Apps and Integrations changes in v1.0.29]]
- Later: 2026-04-16 · OpenCode · [[Changes/OpenCode/2026-04-16-2-apps-and-integrations-changes-in-v1-4-7|2 Apps and Integrations changes in v1.4.7]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-12-14 · Descript · [[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If you have a recording with each speaker with a different microphone, or saved…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20ollama-2026-04-16-e77609&body=Card%3A%20Changes%2FOllama%2F2026-04-16-2-apps-and-integrations-changes-in-v0-21-0.md%0ACard%20ID%3A%20ollama-2026-04-16-e77609%0ASource%3A%20https%3A%2F%2Fgithub.com%2Follama%2Follama%2Freleases%2Ftag%2Fv0.21.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->