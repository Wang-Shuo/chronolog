---
card_id: codex-cli-2026-05-28-f391f9
date: '2026-05-28'
description: 'Codex CLI · 2026-05-28 · Safety and Privacy: 7 changes in 0.135.0 —
  `/permissions` now understands named permission profiles and displays configured
  custom…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke
    Application Access]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2130
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 32757799e97f4e727d2864315e4c11af8f3c2e4e3ce3c07bc0f2a9456bbba3ce
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-05-28-f391f9
  comparison: ''
  date: '2026-05-28'
  description: 'Codex CLI — 0.135.0: 7 Safety and Privacy changes'
  evidence:
  - quote: '`/permissions` now understands named permission profiles and displays
      configured custom profiles. (#21559)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: The Python SDK now exposes friendly `Sandbox` presets for thread and turn
      APIs. (#24772)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: Updated Python SDK docs, examples, and notebook content to use the new
      sandbox preset API. (#24772)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: '#21559 tui: add named permission profile picker @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: '#23813 windows-sandbox: remove SandboxPolicy runner plumbing @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: '#24623 Attach Windows sandbox log to feedback reports @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  - quote: '#24772 [codex] Add friendly Python SDK sandbox presets @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.135.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 7-safety-and-privacy-changes-in-rust-v0-135-0
  source_release: codex-cli-2026-05-28-rust-v0-135-0-github-331012967-2f52956b
  source_type: github_releases
  theme: safety-privacy
  title: 7 Safety and Privacy changes in rust-v0.135.0
  type: change
related_changes:
- '[[Changes/Gemini CLI/2026-05-27-4-safety-and-privacy-changes-in-v0-44-0|4 Safety
  and Privacy changes in v0.44.0]]'
- '[[Changes/Lovable/2026-05-27-sensitive-data-scanning|Sensitive data scanning]]'
- '[[Changes/Claude Code/2026-05-28-2-safety-and-privacy-changes-in-v2-1-153|2 Safety
  and Privacy changes in v2.1.153]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-05-28-rust-v0-135-0-github-331012967-2f52956b|codex-cli-2026-05-28-rust-v0-135-0-github-331012967-2f52956b]]'
source_type: github_releases
theme: safety-privacy
title: 7 Safety and Privacy changes in rust-v0.135.0
type: change
---

<!-- chronolog:begin region="header" -->
# 7 Safety and Privacy changes in rust-v0.135.0

**Codex CLI** · 2026-05-28 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.135.0) · from [[Releases/Codex CLI/codex-cli-2026-05-28-rust-v0-135-0-github-331012967-2f52956b|0.135.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> `/permissions` now understands named permission profiles and displays configured custom profiles. (#21559)

> The Python SDK now exposes friendly `Sandbox` presets for thread and turn APIs. (#24772)

> Updated Python SDK docs, examples, and notebook content to use the new sandbox preset API. (#24772)

> #21559 tui: add named permission profile picker @viyatb-oai

> #23813 windows-sandbox: remove SandboxPolicy runner plumbing @bolinfest

> #24623 Attach Windows sandbox log to feedback reports @iceweasel-oai

> #24772 [codex] Add friendly Python SDK sandbox presets @aibrahim-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.135.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-05-28-4-context-window-changes-in-rust-v0-135-0|4 Context Window changes in rust-v0.135.0]] · Context Window
- [[Changes/Codex CLI/2026-05-28-14-apps-and-integrations-changes-in-rust-v0-135-0|14 Apps and Integrations changes in rust-v0.135.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-05-28-24714-fix-auto-review-skip-legacy-notify-for-auto-review-threads-dylan-hurd-oai|♯24714 fix(auto-review) skip legacy notify for auto review threads @dylan-hurd-oai]] · Agent Mode
- [[Changes/Codex CLI/2026-05-28-8-memory-and-personalization-changes-in-rust-v0-135-0|8 Memory and Personalization changes in rust-v0.135.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-05-28-5-mobile-and-desktop-changes-in-rust-v0-135-0|5 Mobile and Desktop changes in rust-v0.135.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-05-28-slash-command-completion-now-preserves-existing-draft-text-for-commands-that-acc|Slash-command completion now preserves existing draft text for commands that accept…]] · Editor Experience
- [[Changes/Codex CLI/2026-05-28-codex-doctor-now-reports-richer-environment-git-terminal-app-server-and-thread-i|codex doctor now reports richer environment, Git, terminal, app-server, and thread…]] · Developer Workflow
- [[Changes/Codex CLI/2026-05-28-63-other-changes-in-rust-v0-135-0|63 other changes in rust-v0.135.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-05-28 · Claude Code · [[Changes/Claude Code/2026-05-28-2-safety-and-privacy-changes-in-v2-1-153|2 Safety and Privacy changes in v2.1.153]]
- Later: 2026-05-28 · Kimi Code · [[Changes/Kimi Code/2026-05-28-add-auto-slash-command-and-auto-cli-flag-for-auto-permission-mode|Add /auto slash command and --auto CLI flag for auto permission mode]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Descript · [[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke Application Access]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-05-28-f391f9&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-05-28-7-safety-and-privacy-changes-in-rust-v0-135-0.md%0ACard%20ID%3A%20codex-cli-2026-05-28-f391f9%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.135.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->