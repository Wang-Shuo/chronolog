---
card_id: codex-cli-2026-05-21-697f78
date: '2026-05-21'
description: 'Codex CLI · 2026-05-21 · Apps and Integrations: 20 changes in 0.133.0
  — `codex remote-control` now runs like a foreground command, waits for readiness,
  reports…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1155
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 8be50d44389e9ec20153d6c7d2f3b96db5b93ca281663cf2665b94d41afa6e41
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-05-21-697f78
  comparison: ''
  date: '2026-05-21'
  description: 'Codex CLI — 0.133.0: 20 Apps and Integrations changes'
  evidence:
  - quote: '`codex remote-control` now runs like a foreground command, waits for readiness,
      reports machine status, and keeps explicit daemon-style `start`/`stop` commands.
      (#22878)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: 'Plugin discovery is easier to inspect, with marketplace-aware list output,
      installed versions, visible marketplace roots, and remote collection support.
      (#23372, #23584, #23727, #23730)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: Added clearer plugin-creator guidance for updating and reinstalling local
      personal plugins. (#23542)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: 'Added a canonical Codex package archive pipeline and moved installers,
      npm packages, DotSlash, and SDK runtimes toward that shared layout. (#23513,
      #23582, #23586, #23596, #23635, #23636, #23637, #23638, #23786)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#22878 Improve `codex remote-control` CLI UX @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23353 Include plugin id in plugin MCP tool metadata @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23396 [codex] Extract turn skill and plugin injections @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23356 fix(plugins): keep version upgrades additive @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23390 Remove explicit connector tool undeferral @sayan-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23372 Split plugin install discovery into list and request tools @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23535 Move plugin and skill warmup into session startup @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23584 feat: Add vertical remote plugin collection support @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23688 feat: expose turn-start metadata to extensions @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23542 [skills] Create a personal update flow for plugin creator @caseychow-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#21272 Support compact SessionStart hooks @abhinav-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#20659 Wire MITM hooks into runtime enforcement @evawong-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23727 feat(plugins): tabulate plugin list output @caseychow-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23730 [codex] List marketplaces considered by plugin discovery @caseychow-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23737 [codex] Add plugin id to MCP tool call items @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23786 sdk: launch packaged Codex runtimes @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 20-apps-and-integrations-changes-in-rust-v0-133-0
  source_release: codex-cli-2026-05-21-rust-v0-133-0-github-327109656-130a26bc
  source_type: github_releases
  theme: apps-integrations
  title: 20 Apps and Integrations changes in rust-v0.133.0
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-05-19-9-apps-and-integrations-changes-in-v1-0-49|9
  Apps and Integrations changes in v1.0.49]]'
- '[[Changes/Codex CLI/2026-05-20-9-apps-and-integrations-changes-in-rust-v0-132-0|9
  Apps and Integrations changes in rust-v0.132.0]]'
- '[[Changes/GitHub Copilot CLI/2026-05-20-4-apps-and-integrations-changes-in-v1-0-51|4
  Apps and Integrations changes in v1.0.51]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-05-21-rust-v0-133-0-github-327109656-130a26bc|codex-cli-2026-05-21-rust-v0-133-0-github-327109656-130a26bc]]'
source_type: github_releases
theme: apps-integrations
title: 20 Apps and Integrations changes in rust-v0.133.0
type: change
---

<!-- chronolog:begin region="header" -->
# 20 Apps and Integrations changes in rust-v0.133.0

**Codex CLI** · 2026-05-21 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.133.0) · from [[Releases/Codex CLI/codex-cli-2026-05-21-rust-v0-133-0-github-327109656-130a26bc|0.133.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> `codex remote-control` now runs like a foreground command, waits for readiness, reports machine status, and keeps explicit daemon-style `start`/`stop` commands. (#22878)

> Plugin discovery is easier to inspect, with marketplace-aware list output, installed versions, visible marketplace roots, and remote collection support. (#23372, #23584, #23727, #23730)

> Added clearer plugin-creator guidance for updating and reinstalling local personal plugins. (#23542)

> Added a canonical Codex package archive pipeline and moved installers, npm packages, DotSlash, and SDK runtimes toward that shared layout. (#23513, #23582, #23586, #23596, #23635, #23636, #23637, #23638, #23786)

> #22878 Improve `codex remote-control` CLI UX @owenlin0

> #23353 Include plugin id in plugin MCP tool metadata @mzeng-openai

> #23396 [codex] Extract turn skill and plugin injections @pakrym-oai

> #23356 fix(plugins): keep version upgrades additive @iceweasel-oai

> #23390 Remove explicit connector tool undeferral @sayan-oai

> #23372 Split plugin install discovery into list and request tools @mzeng-openai

> #23535 Move plugin and skill warmup into session startup @aibrahim-oai

> #23584 feat: Add vertical remote plugin collection support @xl-openai

> #23688 feat: expose turn-start metadata to extensions @jif-oai

> #23542 [skills] Create a personal update flow for plugin creator @caseychow-oai

> #21272 Support compact SessionStart hooks @abhinav-oai

> #20659 Wire MITM hooks into runtime enforcement @evawong-oai

> #23727 feat(plugins): tabulate plugin list output @caseychow-oai

> #23730 [codex] List marketplaces considered by plugin discovery @caseychow-oai

> #23737 [codex] Add plugin id to MCP tool call items @mzeng-openai

> #23786 sdk: launch packaged Codex runtimes @bolinfest

Source: https://github.com/openai/codex/releases/tag/rust-v0.133.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-05-21-7-agent-mode-changes-in-rust-v0-133-0|7 Agent Mode changes in rust-v0.133.0]] · Agent Mode
- [[Changes/Codex CLI/2026-05-21-5-context-window-changes-in-rust-v0-133-0|5 Context Window changes in rust-v0.133.0]] · Context Window
- [[Changes/Codex CLI/2026-05-21-3-developer-workflow-changes-in-rust-v0-133-0|3 Developer Workflow changes in rust-v0.133.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-05-21-18868-add-mitm-hook-config-model-evawong-oai|♯18868 Add MITM hook config model @evawong-oai]] · Model Support
- [[Changes/Codex CLI/2026-05-21-23578-fix-app-server-speed-up-shutdown-fcoury-oai|♯23578 fix(app-server): speed up shutdown @fcoury-oai]] · Reliability and Performance
- [[Changes/Codex CLI/2026-05-21-17-safety-and-privacy-changes-in-rust-v0-133-0|17 Safety and Privacy changes in rust-v0.133.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-05-21-79-other-changes-in-rust-v0-133-0|79 other changes in rust-v0.133.0]] · Other changes
- [[Changes/Codex CLI/2026-05-21-goals-are-now-enabled-by-default-backed-by-dedicated-storage-and-track-progress|Goals are now enabled by default, backed by dedicated storage, and track progress…]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-05-20 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-05-20-4-apps-and-integrations-changes-in-v1-0-51|4 Apps and Integrations changes in v1.0.51]]
- Later: 2026-05-21 · Lovable · [[Changes/Lovable/2026-05-21-app-connectors-google-maps-platform-semrush-and-tiktok|App connectors: Google Maps Platform, Semrush, and TikTok]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-05-21-697f78&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-05-21-20-apps-and-integrations-changes-in-rust-v0-133-0.md%0ACard%20ID%3A%20codex-cli-2026-05-21-697f78%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.133.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->