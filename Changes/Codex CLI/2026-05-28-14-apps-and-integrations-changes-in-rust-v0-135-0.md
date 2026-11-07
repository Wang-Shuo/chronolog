---
card_id: codex-cli-2026-05-28-3e2723
date: '2026-05-28'
description: 'Codex CLI · 2026-05-28 · Apps and Integrations: 14 changes in 0.135.0
  — App mentions now exclude inaccessible or disabled apps instead of offering unusable
  `$`…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1162
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: f7b3d1bf6afa62c071149fc6df552cbb693bc7ee9d313f61f721ef56e73eb3aa
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-05-28-3e2723
  comparison: ''
  date: '2026-05-28'
  description: 'Codex CLI — 0.135.0: 14 Apps and Integrations changes'
  evidence:
  - quote: App mentions now exclude inaccessible or disabled apps instead of offering
      unusable `$` suggestions. (#24625)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: 'Removed remaining legacy config-profile consumers and routed more TUI
      config/plugin state through app-server-owned APIs. (#24076, #24254, #24255,
      #24265, #24266, #24257)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: 'Centralized Responses retry handling and MCP tool naming logic to reduce
      duplicated internal plumbing. (#24131, #21576)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: '#24164 fix(remote-control): cap reconnect backoff @apanasenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: '#23757 Default function tools into tool hooks @abhinav-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: '#23983 fix: plugin bundle archive handling for upload and install @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: '#24265 TUI config cleanup: MCP inventory @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: '#24532 Use thread config for TUI MCP inventory @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: '#21576 Move MCP tool naming mode into manager @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: '#24625 tui: keep inaccessible apps out of mentions @canvrno-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: '#24473 fix(remote-control): surface websocket task stalls @apanasenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: '#24266 TUI config cleanup: plugin mentions @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: '#24707 Allow runtime enablement for remote plugins @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: '#24257 TUI config cleanup: plugin marketplace @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 14-apps-and-integrations-changes-in-rust-v0-135-0
  source_release: codex-cli-2026-05-28-rust-v0-135-0-github-331012967-2f52956b
  source_type: github_releases
  theme: apps-integrations
  title: 14 Apps and Integrations changes in rust-v0.135.0
  type: change
related_changes:
- '[[Changes/Claude Code/2026-05-28-2-apps-and-integrations-changes-in-v2-1-153|2
  Apps and Integrations changes in v2.1.153]]'
- '[[Changes/Claude Code/2026-05-28-4-apps-and-integrations-changes-in-v2-1-154|4
  Apps and Integrations changes in v2.1.154]]'
- '[[Changes/Cline/2026-05-28-move-the-vs-code-extension-project-into-apps-vscode|Move
  the VS Code extension project into apps/vscode]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-05-28-rust-v0-135-0-github-331012967-2f52956b|codex-cli-2026-05-28-rust-v0-135-0-github-331012967-2f52956b]]'
source_type: github_releases
theme: apps-integrations
title: 14 Apps and Integrations changes in rust-v0.135.0
type: change
---

<!-- chronolog:begin region="header" -->
# 14 Apps and Integrations changes in rust-v0.135.0

**Codex CLI** · 2026-05-28 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.135.0) · from [[Releases/Codex CLI/codex-cli-2026-05-28-rust-v0-135-0-github-331012967-2f52956b|0.135.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> App mentions now exclude inaccessible or disabled apps instead of offering unusable `$` suggestions. (#24625)

> Removed remaining legacy config-profile consumers and routed more TUI config/plugin state through app-server-owned APIs. (#24076, #24254, #24255, #24265, #24266, #24257)

> Centralized Responses retry handling and MCP tool naming logic to reduce duplicated internal plumbing. (#24131, #21576)

> #24164 fix(remote-control): cap reconnect backoff @apanasenko-oai

> #23757 Default function tools into tool hooks @abhinav-oai

> #23983 fix: plugin bundle archive handling for upload and install @xl-openai

> #24265 TUI config cleanup: MCP inventory @etraut-openai

> #24532 Use thread config for TUI MCP inventory @etraut-openai

> #21576 Move MCP tool naming mode into manager @pakrym-oai

> #24625 tui: keep inaccessible apps out of mentions @canvrno-oai

> #24473 fix(remote-control): surface websocket task stalls @apanasenko-oai

> #24266 TUI config cleanup: plugin mentions @etraut-openai

> #24707 Allow runtime enablement for remote plugins @xl-openai

> #24257 TUI config cleanup: plugin marketplace @etraut-openai

Source: https://github.com/openai/codex/releases/tag/rust-v0.135.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-05-28-4-context-window-changes-in-rust-v0-135-0|4 Context Window changes in rust-v0.135.0]] · Context Window
- [[Changes/Codex CLI/2026-05-28-24714-fix-auto-review-skip-legacy-notify-for-auto-review-threads-dylan-hurd-oai|♯24714 fix(auto-review) skip legacy notify for auto review threads @dylan-hurd-oai]] · Agent Mode
- [[Changes/Codex CLI/2026-05-28-8-memory-and-personalization-changes-in-rust-v0-135-0|8 Memory and Personalization changes in rust-v0.135.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-05-28-5-mobile-and-desktop-changes-in-rust-v0-135-0|5 Mobile and Desktop changes in rust-v0.135.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-05-28-slash-command-completion-now-preserves-existing-draft-text-for-commands-that-acc|Slash-command completion now preserves existing draft text for commands that accept…]] · Editor Experience
- [[Changes/Codex CLI/2026-05-28-7-safety-and-privacy-changes-in-rust-v0-135-0|7 Safety and Privacy changes in rust-v0.135.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-05-28-codex-doctor-now-reports-richer-environment-git-terminal-app-server-and-thread-i|codex doctor now reports richer environment, Git, terminal, app-server, and thread…]] · Developer Workflow
- [[Changes/Codex CLI/2026-05-28-63-other-changes-in-rust-v0-135-0|63 other changes in rust-v0.135.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-05-28 · Cline · [[Changes/Cline/2026-05-28-move-the-vs-code-extension-project-into-apps-vscode|Move the VS Code extension project into apps/vscode]]
- Later: 2026-05-28 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-05-28-10-apps-and-integrations-changes-in-v1-0-55|10 Apps and Integrations changes in v1.0.55]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-05-28-3e2723&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-05-28-14-apps-and-integrations-changes-in-rust-v0-135-0.md%0ACard%20ID%3A%20codex-cli-2026-05-28-3e2723%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.135.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->