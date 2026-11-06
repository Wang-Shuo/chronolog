---
card_id: dify-2026-06-25-da6283
date: '2026-06-25'
description: 'Dify · 2026-06-25 · Apps and Integrations: 27 changes in 1.15.0 — **Faster
  plugin installs in certain regions**'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1190
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 813528165dc501a124096e9c773cf9f28ae863cc78eeca229259874f7d92e91e
product: dify
product_name: Dify
record:
  card_id: dify-2026-06-25-da6283
  comparison: ''
  date: '2026-06-25'
  description: 'Dify — 1.15.0: 27 Apps and Integrations changes'
  evidence:
  - quote: '**Faster plugin installs in certain regions**'
    source_release: https://github.com/langgenius/dify/releases/tag/1.15.0
  - quote: The plugin daemon now auto-detects your region at startup and, where network
      connectivity to PyPI is poor, automatically picks a nearby package mirror —
      so installing plugins is faster and more reliable without any manual setup.
      You can still pin a specific mirror if you prefer (dify-plugin-daemon#750)
    source_release: https://github.com/langgenius/dify/releases/tag/1.15.0
  - quote: This release fixes a path traversal issue in plugin-daemon forwarding (cve-2026-41948).
    source_release: https://github.com/langgenius/dify/releases/tag/1.15.0
  - quote: '`PLUGIN_MODEL_PROVIDERS_CACHE_TTL` (`api/.env.example`)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.15.0
  - quote: '`PIP_MIRROR_AUTO_DETECT` (plugin daemon; default `true`) — auto-select
      a nearby PyPI mirror at startup for regions with poor connectivity'
    source_release: https://github.com/langgenius/dify/releases/tag/1.15.0
  - quote: '`PIP_MIRROR_URL` (plugin daemon; default empty) — manually pin the PyPI
      mirror; takes precedence over auto-detection'
    source_release: https://github.com/langgenius/dify/releases/tag/1.15.0
  - quote: '**Category-scoped plugin auto-upgrade strategy** (`add_plugin_auto_upgrade_category`)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.15.0
  - quote: App stars, learn-dify / cloud-only flags on recommended apps
    source_release: https://github.com/langgenius/dify/releases/tag/1.15.0
  - quote: '> - **Plugin auto-upgrade is now configured per plugin category.** After
      running `flask db upgrade`, you MUST also run `flask backfill-plugin-auto-upgrade`
      to migrate existing tenants'' auto-upgrade settings into the new category-scoped
      model. If you skip this step, plugin auto-upgrade settings users previously
      configured may stop taking effect.'
    source_release: https://github.com/langgenius/dify/releases/tag/1.15.0
  - quote: '**Backfill category-scoped plugin auto-upgrade strategies** (required).'
    source_release: https://github.com/langgenius/dify/releases/tag/1.15.0
  - quote: 'chore(codeowners): update plugin ownership by @laipz8200 in https://github.com/langgenius/dify/pull/36394'
    source_release: https://github.com/langgenius/dify/releases/tag/1.15.0
  - quote: 'refactor: add missing @override decorator to datasource plugin classes
      by @AlsoTheZv3n in https://github.com/langgenius/dify/pull/36494'
    source_release: https://github.com/langgenius/dify/releases/tag/1.15.0
  - quote: 'refactor: add missing @override decorator to remaining MCP, Jieba, embeddings,
      and misc subclasses by @AlsoTheZv3n in https://github.com/langgenius/dify/pull/36528'
    source_release: https://github.com/langgenius/dify/releases/tag/1.15.0
  - quote: 'feat(plugin): cache plugin model providers by tenant by @laipz8200 in
      https://github.com/langgenius/dify/pull/36449'
    source_release: https://github.com/langgenius/dify/releases/tag/1.15.0
  - quote: 'feat: add agent backend plugin layer by @zyssyz123 in https://github.com/langgenius/dify/pull/36686'
    source_release: https://github.com/langgenius/dify/releases/tag/1.15.0
  - quote: 'test: move delete account task to container integration by @escape0707
      in https://github.com/langgenius/dify/pull/36733'
    source_release: https://github.com/langgenius/dify/releases/tag/1.15.0
  - quote: 'chore: unified plugin status icon position by @iamjoel in https://github.com/langgenius/dify/pull/36816'
    source_release: https://github.com/langgenius/dify/releases/tag/1.15.0
  - quote: 'feat: per-credential visibility control for plugin credentials by @ForeignKeyCN
      in https://github.com/langgenius/dify/pull/35468'
    source_release: https://github.com/langgenius/dify/releases/tag/1.15.0
  - quote: 'chore: add missing @override decorato to `api/extensions` by @eryue0220
      in https://github.com/langgenius/dify/pull/36941'
    source_release: https://github.com/langgenius/dify/releases/tag/1.15.0
  - quote: 'feat(web): add Forward-user-identity toggle to MCP provider modal by @CourTeous33
      in https://github.com/langgenius/dify/pull/36840'
    source_release: https://github.com/langgenius/dify/releases/tag/1.15.0
  - quote: 'feat(api): add MCP user-identity forwarding by @CourTeous33 in https://github.com/langgenius/dify/pull/36839'
    source_release: https://github.com/langgenius/dify/releases/tag/1.15.0
  - quote: 'chore: filter unavailable apps from the installed apps list API by @hjlarry
      in https://github.com/langgenius/dify/pull/37206'
    source_release: https://github.com/langgenius/dify/releases/tag/1.15.0
  - quote: 'refactor(web): mark Props of tools/mcp components as read-only (#25219)
      by @Rohit-Gahlawat in https://github.com/langgenius/dify/pull/37251'
    source_release: https://github.com/langgenius/dify/releases/tag/1.15.0
  - quote: 'refactor(web): mark Props of plugins/ components as read-only (#25219)
      by @Rohit-Gahlawat in https://github.com/langgenius/dify/pull/37303'
    source_release: https://github.com/langgenius/dify/releases/tag/1.15.0
  - quote: 'refactor: use foxact package for copied hooks by @hyoban in https://github.com/langgenius/dify/pull/37308'
    source_release: https://github.com/langgenius/dify/releases/tag/1.15.0
  - quote: 'chore: add integration tests for openapi group by @wylswz in https://github.com/langgenius/dify/pull/37314'
    source_release: https://github.com/langgenius/dify/releases/tag/1.15.0
  - quote: 'feat(api): forward user_type for MCP identity forwarding (webapp end-users)
      by @CourTeous33 in https://github.com/langgenius/dify/pull/37347'
    source_release: https://github.com/langgenius/dify/releases/tag/1.15.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 27-apps-and-integrations-changes-in-1-15-0
  source_release: dify-2026-06-25-1-15-0-github-344699591-4dd01045
  source_type: github_releases
  theme: apps-integrations
  title: 27 Apps and Integrations changes in 1.15.0
  type: change
related_changes:
- '[[Changes/Lovable/2026-06-24-app-connector-calendly|App connector: Calendly]]'
- '[[Changes/Claude Code/2026-06-25-2-apps-and-integrations-changes-in-v2-1-193|2
  Apps and Integrations changes in v2.1.193]]'
- '[[Changes/Codex CLI/2026-06-25-9-apps-and-integrations-changes-in-rust-v0-142-2|9
  Apps and Integrations changes in rust-v0.142.2]]'
source_release: '[[Releases/Dify/dify-2026-06-25-1-15-0-github-344699591-4dd01045|dify-2026-06-25-1-15-0-github-344699591-4dd01045]]'
source_type: github_releases
theme: apps-integrations
title: 27 Apps and Integrations changes in 1.15.0
type: change
---

<!-- chronolog:begin region="header" -->
# 27 Apps and Integrations changes in 1.15.0

**Dify** · 2026-06-25 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.15.0) · from [[Releases/Dify/dify-2026-06-25-1-15-0-github-344699591-4dd01045|1.15.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> **Faster plugin installs in certain regions**

> The plugin daemon now auto-detects your region at startup and, where network connectivity to PyPI is poor, automatically picks a nearby package mirror — so installing plugins is faster and more reliable without any manual setup. You can still pin a specific mirror if you prefer (dify-plugin-daemon#750)

> This release fixes a path traversal issue in plugin-daemon forwarding (cve-2026-41948).

> `PLUGIN_MODEL_PROVIDERS_CACHE_TTL` (`api/.env.example`)

> `PIP_MIRROR_AUTO_DETECT` (plugin daemon; default `true`) — auto-select a nearby PyPI mirror at startup for regions with poor connectivity

> `PIP_MIRROR_URL` (plugin daemon; default empty) — manually pin the PyPI mirror; takes precedence over auto-detection

> **Category-scoped plugin auto-upgrade strategy** (`add_plugin_auto_upgrade_category`)

> App stars, learn-dify / cloud-only flags on recommended apps

> > - **Plugin auto-upgrade is now configured per plugin category.** After running `flask db upgrade`, you MUST also run `flask backfill-plugin-auto-upgrade` to migrate existing tenants' auto-upgrade settings into the new category-scoped model. If you skip this step, plugin auto-upgrade settings users previously configured may stop taking effect.

> **Backfill category-scoped plugin auto-upgrade strategies** (required).

> chore(codeowners): update plugin ownership by @laipz8200 in https://github.com/langgenius/dify/pull/36394

> refactor: add missing @override decorator to datasource plugin classes by @AlsoTheZv3n in https://github.com/langgenius/dify/pull/36494

> refactor: add missing @override decorator to remaining MCP, Jieba, embeddings, and misc subclasses by @AlsoTheZv3n in https://github.com/langgenius/dify/pull/36528

> feat(plugin): cache plugin model providers by tenant by @laipz8200 in https://github.com/langgenius/dify/pull/36449

> feat: add agent backend plugin layer by @zyssyz123 in https://github.com/langgenius/dify/pull/36686

> test: move delete account task to container integration by @escape0707 in https://github.com/langgenius/dify/pull/36733

> chore: unified plugin status icon position by @iamjoel in https://github.com/langgenius/dify/pull/36816

> feat: per-credential visibility control for plugin credentials by @ForeignKeyCN in https://github.com/langgenius/dify/pull/35468

> chore: add missing @override decorato to `api/extensions` by @eryue0220 in https://github.com/langgenius/dify/pull/36941

> feat(web): add Forward-user-identity toggle to MCP provider modal by @CourTeous33 in https://github.com/langgenius/dify/pull/36840

> feat(api): add MCP user-identity forwarding by @CourTeous33 in https://github.com/langgenius/dify/pull/36839

> chore: filter unavailable apps from the installed apps list API by @hjlarry in https://github.com/langgenius/dify/pull/37206

> refactor(web): mark Props of tools/mcp components as read-only (#25219) by @Rohit-Gahlawat in https://github.com/langgenius/dify/pull/37251

> refactor(web): mark Props of plugins/ components as read-only (#25219) by @Rohit-Gahlawat in https://github.com/langgenius/dify/pull/37303

> refactor: use foxact package for copied hooks by @hyoban in https://github.com/langgenius/dify/pull/37308

> chore: add integration tests for openapi group by @wylswz in https://github.com/langgenius/dify/pull/37314

> feat(api): forward user_type for MCP identity forwarding (webapp end-users) by @CourTeous33 in https://github.com/langgenius/dify/pull/37347

Source: https://github.com/langgenius/dify/releases/tag/1.15.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2026-06-25-6-interface-experience-changes-in-1-15-0|6 Interface Experience changes in 1.15.0]] · Interface Experience
- [[Changes/Dify/2026-06-25-38-agent-mode-changes-in-1-15-0|38 Agent Mode changes in 1.15.0]] · Agent Mode
- [[Changes/Dify/2026-06-25-14-safety-and-privacy-changes-in-1-15-0|14 Safety and Privacy changes in 1.15.0]] · Safety and Privacy
- [[Changes/Dify/2026-06-25-refactor-inject-session-into-audio-tts-by-myshkin451-in-https-github-com-langgen|refactor: inject session into audio TTS]] · Voice and Audio
- [[Changes/Dify/2026-06-25-2-reliability-and-performance-changes-in-1-15-0|2 Reliability and Performance changes in 1.15.0]] · Reliability and Performance
- [[Changes/Dify/2026-06-25-3-context-window-changes-in-1-15-0|3 Context Window changes in 1.15.0]] · Context Window
- [[Changes/Dify/2026-06-25-install-it-on-any-platform-macos-linux-windows-with-a-single-command-and-no-acce|Install it on any platform (macOS, Linux, Windows) with a single command and no…]] · Mobile and Desktop
- [[Changes/Dify/2026-06-25-numerous-web-ui-and-accessibility-focus-ring-polish-fixes|Numerous web UI and accessibility/focus-ring polish fixes]] · Accessibility and Localization
- [[Changes/Dify/2026-06-25-6-pricing-model-changes-in-1-15-0|6 Pricing Model changes in 1.15.0]] · Pricing Model
- [[Changes/Dify/2026-06-25-9-developer-workflow-changes-in-1-15-0|9 Developer Workflow changes in 1.15.0]] · Developer Workflow
- [[Changes/Dify/2026-06-25-6-files-and-data-changes-in-1-15-0|6 Files and Data changes in 1.15.0]] · Files and Data
- [[Changes/Dify/2026-06-25-17-model-support-changes-in-1-15-0|17 Model Support changes in 1.15.0]] · Model Support
- [[Changes/Dify/2026-06-25-5-account-and-access-changes-in-1-15-0|5 Account and Access changes in 1.15.0]] · Account and Access
- [[Changes/Dify/2026-06-25-6-collaboration-changes-in-1-15-0|6 Collaboration changes in 1.15.0]] · Collaboration
- [[Changes/Dify/2026-06-25-2-automation-and-scheduling-changes-in-1-15-0|2 Automation and Scheduling changes in 1.15.0]] · Automation and Scheduling
- [[Changes/Dify/2026-06-25-3-editor-experience-changes-in-1-15-0|3 Editor Experience changes in 1.15.0]] · Editor Experience
- [[Changes/Dify/2026-06-25-365-other-changes-in-1-15-0|365 other changes in 1.15.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-06-25 · Codex CLI · [[Changes/Codex CLI/2026-06-25-9-apps-and-integrations-changes-in-rust-v0-142-2|9 Apps and Integrations changes in rust-v0.142.2]]
- Later: 2026-06-25 · Ollama · [[Changes/Ollama/2026-06-25-docs-redesign-docs-landing-and-integrations-overview-by-hoyyeva-in-https-github|docs: redesign docs landing and integrations overview]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-06-25-da6283&body=Card%3A%20Changes%2FDify%2F2026-06-25-27-apps-and-integrations-changes-in-1-15-0.md%0ACard%20ID%3A%20dify-2026-06-25-da6283%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.15.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->