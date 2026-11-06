---
card_id: codex-cli-2026-05-21-f31927
date: '2026-05-21'
description: 'Codex CLI · 2026-05-21 · Safety and Privacy: 17 changes in 0.133.0 —
  Permission profiles gained list APIs, inheritance, managed `requirements.toml` support…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1131
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 6d322f3ac4c8470d1c1fb8199ac0c5bb83d3d0506a3cce286cc0df7933b73b7c
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-05-21-f31927
  comparison: ''
  date: '2026-05-21'
  description: 'Codex CLI — 0.133.0: 17 Safety and Privacy changes'
  evidence:
  - quote: 'Permission profiles gained list APIs, inheritance, managed `requirements.toml`
      support, runtime refresh behavior, and stronger Windows sandbox integration.
      (#22928, #23412, #22270, #23433, #22931, #23715)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: 'Expanded app-server/API docs and schema coverage around managed permission
      profile requirements. (#23433, #23555)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23360 app-server: use profile ids in v2 permission params @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#22928 core: expose permission profile picker metadata @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23493 Make `deny` canonical for filesystem permission entries @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23412 feat: add permission profile list api @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#22896 windows-sandbox: add resolved permissions helper @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#22918 windows-sandbox: send permission profiles to elevated runner @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23735 windows-sandbox: share bundled helper lookup @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#22270 feat(permissions): resolve permission profile inheritance @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#22923 windows-sandbox: drive write roots from resolved permissions @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23167 windows-sandbox: feed setup from resolved permissions @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#22931 core: refresh active permission profiles at runtime @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23764 Remove Windows sandbox resource stamping @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23714 windows-sandbox: add profile-native elevated APIs @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23433 feat: support managed permission profiles in requirements.toml
      @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  - quote: '#23715 core: pass permission profiles to Windows runner @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.133.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 17-safety-and-privacy-changes-in-rust-v0-133-0
  source_release: codex-cli-2026-05-21-rust-v0-133-0-github-327109656-130a26bc
  source_type: github_releases
  theme: safety-privacy
  title: 17 Safety and Privacy changes in rust-v0.133.0
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-05-19-memory-permission-prompts-now-name-who-can-see-a-stored-memory-user-scope-or-the|Memory
  permission prompts now name who can see a stored memory]]'
- '[[Changes/Codex CLI/2026-05-20-5-safety-and-privacy-changes-in-rust-v0-132-0|5
  Safety and Privacy changes in rust-v0.132.0]]'
- '[[Changes/GitHub Copilot CLI/2026-05-20-add-security-review-slash-command-to-review-code-changes-for-security-vulnerabil|Add
  /security-review slash command to review code changes for security…]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-05-21-rust-v0-133-0-github-327109656-130a26bc|codex-cli-2026-05-21-rust-v0-133-0-github-327109656-130a26bc]]'
source_type: github_releases
theme: safety-privacy
title: 17 Safety and Privacy changes in rust-v0.133.0
type: change
---

<!-- chronolog:begin region="header" -->
# 17 Safety and Privacy changes in rust-v0.133.0

**Codex CLI** · 2026-05-21 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.133.0) · from [[Releases/Codex CLI/codex-cli-2026-05-21-rust-v0-133-0-github-327109656-130a26bc|0.133.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Permission profiles gained list APIs, inheritance, managed `requirements.toml` support, runtime refresh behavior, and stronger Windows sandbox integration. (#22928, #23412, #22270, #23433, #22931, #23715)

> Expanded app-server/API docs and schema coverage around managed permission profile requirements. (#23433, #23555)

> #23360 app-server: use profile ids in v2 permission params @bolinfest

> #22928 core: expose permission profile picker metadata @viyatb-oai

> #23493 Make `deny` canonical for filesystem permission entries @viyatb-oai

> #23412 feat: add permission profile list api @viyatb-oai

> #22896 windows-sandbox: add resolved permissions helper @bolinfest

> #22918 windows-sandbox: send permission profiles to elevated runner @bolinfest

> #23735 windows-sandbox: share bundled helper lookup @bolinfest

> #22270 feat(permissions): resolve permission profile inheritance @viyatb-oai

> #22923 windows-sandbox: drive write roots from resolved permissions @bolinfest

> #23167 windows-sandbox: feed setup from resolved permissions @bolinfest

> #22931 core: refresh active permission profiles at runtime @viyatb-oai

> #23764 Remove Windows sandbox resource stamping @iceweasel-oai

> #23714 windows-sandbox: add profile-native elevated APIs @bolinfest

> #23433 feat: support managed permission profiles in requirements.toml @viyatb-oai

> #23715 core: pass permission profiles to Windows runner @bolinfest

Source: https://github.com/openai/codex/releases/tag/rust-v0.133.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-05-21-7-agent-mode-changes-in-rust-v0-133-0|7 Agent Mode changes in rust-v0.133.0]] · Agent Mode
- [[Changes/Codex CLI/2026-05-21-20-apps-and-integrations-changes-in-rust-v0-133-0|20 Apps and Integrations changes in rust-v0.133.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-05-21-5-context-window-changes-in-rust-v0-133-0|5 Context Window changes in rust-v0.133.0]] · Context Window
- [[Changes/Codex CLI/2026-05-21-3-developer-workflow-changes-in-rust-v0-133-0|3 Developer Workflow changes in rust-v0.133.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-05-21-18868-add-mitm-hook-config-model-evawong-oai|♯18868 Add MITM hook config model @evawong-oai]] · Model Support
- [[Changes/Codex CLI/2026-05-21-23578-fix-app-server-speed-up-shutdown-fcoury-oai|♯23578 fix(app-server): speed up shutdown @fcoury-oai]] · Reliability and Performance
- [[Changes/Codex CLI/2026-05-21-79-other-changes-in-rust-v0-133-0|79 other changes in rust-v0.133.0]] · Other changes
- [[Changes/Codex CLI/2026-05-21-goals-are-now-enabled-by-default-backed-by-dedicated-storage-and-track-progress|Goals are now enabled by default, backed by dedicated storage, and track progress…]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-05-20 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-05-20-add-security-review-slash-command-to-review-code-changes-for-security-vulnerabil|Add /security-review slash command to review code changes for security…]]
- Later: 2026-05-22 · Claude Code · [[Changes/Claude Code/2026-05-22-2-safety-and-privacy-changes-in-v2-1-149|2 Safety and Privacy changes in v2.1.149]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-05-21-f31927&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-05-21-17-safety-and-privacy-changes-in-rust-v0-133-0.md%0ACard%20ID%3A%20codex-cli-2026-05-21-f31927%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.133.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->