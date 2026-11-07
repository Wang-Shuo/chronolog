---
card_id: codex-cli-2025-12-02-dc38ad
date: '2025-12-02'
description: 'Codex CLI · 2025-12-02 · Mobile and Desktop: Execution gains an experimental
  “exp” model, unified exec pruning to limit session bloat, per-run custom…'
diffusion:
  first_in_tracked: "[[Changes/Cursor/2023-03-14-windows-and-linux-support|Windows
    and Linux support \U0001F973]]"
  inference: No adoption, equivalence, or causation claim.
  lag_days: 994
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: mobile-desktop
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: significant
kind: change
machine_hash: 88419eff65bf62e9fcd7f3b2f437a8ffbd37ac02b879a0538cc3d4b87cd515d8
product: codex-cli
product_name: Codex CLI
record:
  ai_generated: true
  card_id: codex-cli-2025-12-02-dc38ad
  comparison: ''
  confidence: low
  date: '2025-12-02'
  description: 'Codex CLI — 0.64.0: Execution gains an experimental “exp” model, unified
    exec pruning to limit session bloat, per-run custom environment injection, policy-approved
    command bypass, and Windows protections that flag risky browser or URL launches.
    History lookup now works on Windows and WSL, and model selection honors use_model.'
  evidence:
  - quote: Execution gains an experimental “exp” model, unified exec pruning to limit
      session bloat, per-run custom environment injection, policy-approved command
      bypass, and Windows protections that flag risky browser or URL launches. History
      lookup now works on Windows and WSL, and model selection honors use_model.
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.64.0
  extractor_version: fallback-v5
  impact: significant
  kind: change
  product: codex-cli
  product_name: Codex CLI
  slug: execution-gains-an-experimental-exp-model-unified-exec-pruning-to-limit-session
  source_release: codex-cli-2025-12-02-rust-v0-64-0-github-266901625-82376886
  source_type: github_releases
  theme: mobile-desktop
  theme_matches:
  - matched_terms:
    - wsl
    score: 50
    theme: developer-workflow
  - matched_terms:
    - model
    score: 50
    theme: model-support
  theme_resolution: manual-semantic-rule-v1
  title: Execution gains an experimental “exp” model, unified exec pruning to limit
    session…
  type: change
related_changes:
- '[[Changes/Gemini CLI/2025-11-26-improve-pty-resize-error-handling-for-windows-by-galz10-in-https-github-com-goog|Improve
  pty resize error handling for Windows]]'
- '[[Changes/ElevenLabs/2025-11-27-client|Client]]'
- '[[Changes/ElevenLabs/2025-11-27-react|React]]'
source_release: '[[Releases/Codex CLI/codex-cli-2025-12-02-rust-v0-64-0-github-266901625-82376886|codex-cli-2025-12-02-rust-v0-64-0-github-266901625-82376886]]'
source_type: github_releases
theme: mobile-desktop
title: Execution gains an experimental “exp” model, unified exec pruning to limit
  session…
type: change
---

<!-- chronolog:begin region="header" -->
# Execution gains an experimental “exp” model, unified exec pruning to limit session…

**Codex CLI** · 2025-12-02 · [[Themes/mobile-desktop|Mobile and Desktop]] · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.64.0) · from [[Releases/Codex CLI/codex-cli-2025-12-02-rust-v0-64-0-github-266901625-82376886|0.64.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Execution gains an experimental “exp” model, unified exec pruning to limit session bloat, per-run custom environment injection, policy-approved command bypass, and Windows protections that flag risky browser or URL launches. History lookup now works on Windows and WSL, and model selection honors use_model.
>
> Source: https://github.com/openai/codex/releases/tag/rust-v0.64.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2025-12-02-2-model-support-changes-in-rust-v0-64-0|2 Model Support changes in rust-v0.64.0]] · Model Support
- [[Changes/Codex CLI/2025-12-02-5-context-window-changes-in-rust-v0-64-0|5 Context Window changes in rust-v0.64.0]] · Context Window
- [[Changes/Codex CLI/2025-12-02-feat-support-login-as-an-option-on-shell-tool-mcp-by-bolinfest-in-7120|feat: support login as an option on shell-tool-mcp by @bolinfest in ♯7120]] · Account and Access
- [[Changes/Codex CLI/2025-12-02-3-apps-and-integrations-changes-in-rust-v0-64-0|3 Apps and Integrations changes in rust-v0.64.0]] · Apps and Integrations
- [[Changes/Codex CLI/2025-12-02-9-safety-and-privacy-changes-in-rust-v0-64-0|9 Safety and Privacy changes in rust-v0.64.0]] · Safety and Privacy
- [[Changes/Codex CLI/2025-12-02-powershell-apply-patch-parsing-is-corrected-and-apply-patch-tests-now-cover-shel|PowerShell apply_patch parsing is corrected, and apply_patch tests now cover…]] · Agent Mode
- [[Changes/Codex CLI/2025-12-02-4-developer-workflow-changes-in-rust-v0-64-0|4 Developer Workflow changes in rust-v0.64.0]] · Developer Workflow
- [[Changes/Codex CLI/2025-12-02-3-editor-experience-changes-in-rust-v0-64-0|3 Editor Experience changes in rust-v0.64.0]] · Editor Experience
- [[Changes/Codex CLI/2025-12-02-chore-dedup-unified-exec-waited-rendering-by-jif-oai-in-7256|chore: dedup unified exec "waited" rendering by @jif-oai in ♯7256]] · Interface Experience
- [[Changes/Codex CLI/2025-12-02-46-other-changes-in-rust-v0-64-0|46 other changes in rust-v0.64.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Mobile and Desktop

- Earlier: 2025-11-27 · ElevenLabs · [[Changes/ElevenLabs/2025-11-27-react|React]]
- Later: 2025-12-08 · ElevenLabs · [[Changes/ElevenLabs/2025-12-08-android-sdk|Android SDK]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-14 · Cursor · [[Changes/Cursor/2023-03-14-windows-and-linux-support|Windows and Linux support 🥳]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2025-12-02-dc38ad&body=Card%3A%20Changes%2FCodex%20CLI%2F2025-12-02-execution-gains-an-experimental-exp-model-unified-exec-pruning-to-limit-session.md%0ACard%20ID%3A%20codex-cli-2025-12-02-dc38ad%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.64.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->