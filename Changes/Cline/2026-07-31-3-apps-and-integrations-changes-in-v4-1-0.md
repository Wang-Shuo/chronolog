---
card_id: cline-2026-07-31-dc68b6
date: '2026-07-31'
description: 'Cline · 2026-07-31 · Apps and Integrations: 3 changes in v4.1.0 — 4.1.0
  converts the stable extension to a **combined A/B package**: one VSIX containing
  both…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1226
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 0b00da63da0a82f4e51fdda72acb6708d05f6d3dcb7f95052a462dcd9acbba90
product: cline
product_name: Cline
record:
  card_id: cline-2026-07-31-dc68b6
  comparison: ''
  date: '2026-07-31'
  description: 'Cline — v4.1.0: 3 Apps and Integrations changes'
  evidence:
  - quote: '4.1.0 converts the stable extension to a **combined A/B package**: one
      VSIX containing both the current (legacy) extension and the new SDK-based extension,
      plus a small loader that activates exactly one per window, controlled by a staged
      remote rollout.'
    source_release: https://github.com/cline/cline/releases/tag/v4.1.0
  - quote: '**For nearly everyone, nothing changes** — the loader activates the same
      extension you were running in 4.0.12. A small percentage of users (starting
      at 1%) are gradually opted into the new SDK-based extension, which will become
      the default for everyone as the rollout completes.'
    source_release: https://github.com/cline/cline/releases/tag/v4.1.0
  - quote: 'Rollout machinery: apps/vscode-rollout (see its README for design + runbook).'
    source_release: https://github.com/cline/cline/releases/tag/v4.1.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: cline
  product_name: Cline
  slug: 3-apps-and-integrations-changes-in-v4-1-0
  source_release: cline-2026-07-31-v4-1-0-github-362842844-bb117e78
  source_type: github_releases
  theme: apps-integrations
  title: 3 Apps and Integrations changes in v4.1.0
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-07-29-47-apps-and-integrations-changes-in-rust-v0-146-0|47
  Apps and Integrations changes in rust-v0.146.0]]'
- '[[Changes/GitHub Copilot CLI/2026-07-30-2-apps-and-integrations-changes-in-v1-0-76|2
  Apps and Integrations changes in v1.0.76]]'
- '[[Changes/OpenHands/2026-07-30-feat-enable-disable-an-installed-mcp-server-from-its-card-by-hieptl-in-https-git|feat:
  enable/disable an installed MCP server from its card]]'
source_release: '[[Releases/Cline/cline-2026-07-31-v4-1-0-github-362842844-bb117e78|cline-2026-07-31-v4-1-0-github-362842844-bb117e78]]'
source_type: github_releases
theme: apps-integrations
title: 3 Apps and Integrations changes in v4.1.0
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Apps and Integrations changes in v4.1.0

**Cline** · 2026-07-31 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/cline/cline/releases/tag/v4.1.0) · from [[Releases/Cline/cline-2026-07-31-v4-1-0-github-362842844-bb117e78|v4.1.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 4.1.0 converts the stable extension to a **combined A/B package**: one VSIX containing both the current (legacy) extension and the new SDK-based extension, plus a small loader that activates exactly one per window, controlled by a staged remote rollout.

> **For nearly everyone, nothing changes** — the loader activates the same extension you were running in 4.0.12. A small percentage of users (starting at 1%) are gradually opted into the new SDK-based extension, which will become the default for everyone as the rollout completes.

> Rollout machinery: apps/vscode-rollout (see its README for design + runbook).

Source: https://github.com/cline/cline/releases/tag/v4.1.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Cline/2026-07-31-legacy-bundle-legacy-extension-3fdc186f1-4-0-12-free-model-button-wording|Legacy bundle: legacy-extension @ 3fdc186f1 (4.0.12 + free-model button wording)]] · Model Support
- [[Changes/Cline/2026-07-31-4-other-changes-in-v4-1-0|4 other changes in v4.1.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-07-30 · OpenHands · [[Changes/OpenHands/2026-07-30-feat-enable-disable-an-installed-mcp-server-from-its-card-by-hieptl-in-https-git|feat: enable/disable an installed MCP server from its card]]
- Later: 2026-08-03 · Cursor · [[Changes/Cursor/2026-08-03-cursor-can-now-read-write-and-act-across-your-google-workspace|Google Workspace Plugins]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20cline-2026-07-31-dc68b6&body=Card%3A%20Changes%2FCline%2F2026-07-31-3-apps-and-integrations-changes-in-v4-1-0.md%0ACard%20ID%3A%20cline-2026-07-31-dc68b6%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fcline%2Fcline%2Freleases%2Ftag%2Fv4.1.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->