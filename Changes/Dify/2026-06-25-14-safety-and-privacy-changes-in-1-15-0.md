---
card_id: dify-2026-06-25-431d73
date: '2026-06-25'
description: 'Dify · 2026-06-25 · Safety and Privacy: 14 changes in 1.15.0 — **More
  accessible** — plugin permission hints, restored contact-us menu, skip-nav link,
  and…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke
    Application Access]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2158
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: bf0ded3f46a65640ae415e64ee9d5d5c30bb2245363db0f118064003f969991f
product: dify
product_name: Dify
record:
  card_id: dify-2026-06-25-431d73
  comparison: ''
  date: '2026-06-25'
  description: 'Dify — 1.15.0: 14 Safety and Privacy changes'
  evidence:
  - quote: '**More accessible** — plugin permission hints, restored contact-us menu,
      skip-nav link, and keyboard focus polish (#37310, #37774, #37644)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.15.0
  - quote: '`SSRF_PROXY_ALLOW_PRIVATE_DOMAINS`, `SSRF_PROXY_ALLOW_PRIVATE_IPS`, `SSRF_SANDBOX_PROXY_HOST`,
      `SSRF_SANDBOX_PROXY_PORT` (`docker/envs/middleware.env.example`)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.15.0
  - quote: '`SSRF_REVERSE_PROXY_PORT`, `SSRF_SANDBOX_HOST` (`docker/envs/middleware.env.example`)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.15.0
  - quote: 'docs: add security policy by @bmtriet in https://github.com/langgenius/dify/pull/36873'
    source_release: https://github.com/langgenius/dify/releases/tag/1.15.0
  - quote: 'feat(agent): Sandbox / CLI Agent (dify.shell) + read-only sandbox file
      inspector by @zyssyz123 in https://github.com/langgenius/dify/pull/36984'
    source_release: https://github.com/langgenius/dify/releases/tag/1.15.0
  - quote: 'fix(web): show plugin auth permission hint by @Jingyi-Dify in https://github.com/langgenius/dify/pull/37310'
    source_release: https://github.com/langgenius/dify/releases/tag/1.15.0
  - quote: 'refactor(agent): replace workspace inspector with sandbox API by @BeautyyuYanli
      in https://github.com/langgenius/dify/pull/37349'
    source_release: https://github.com/langgenius/dify/releases/tag/1.15.0
  - quote: 'test: use caplog for workspace permission logging by @popsiclelmlm in
      https://github.com/langgenius/dify/pull/37473'
    source_release: https://github.com/langgenius/dify/releases/tag/1.15.0
  - quote: 'chore: workflow restore sandbox upgrade by @hjlarry in https://github.com/langgenius/dify/pull/37568'
    source_release: https://github.com/langgenius/dify/releases/tag/1.15.0
  - quote: 'chore: add ENTERPRISE_RBAC_API_URL check and update permission key by
      @fatelei in https://github.com/langgenius/dify/pull/37777'
    source_release: https://github.com/langgenius/dify/releases/tag/1.15.0
  - quote: 'chore: Update permission keys and descriptions for multiple languages
      to simplify application and dataset management phrases by @WTW0313 in https://github.com/langgenius/dify/pull/37859'
    source_release: https://github.com/langgenius/dify/releases/tag/1.15.0
  - quote: 'feat: filter dataset operator and add miss permission key by @fatelei
      in https://github.com/langgenius/dify/pull/37867'
    source_release: https://github.com/langgenius/dify/releases/tag/1.15.0
  - quote: 'build(deps): update Bleach sanitizer security fix by @gateway in https://github.com/langgenius/dify/pull/37860'
    source_release: https://github.com/langgenius/dify/releases/tag/1.15.0
  - quote: 'feat: update monitor permission key and plugin permission key by @fatelei
      in https://github.com/langgenius/dify/pull/37937'
    source_release: https://github.com/langgenius/dify/releases/tag/1.15.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 14-safety-and-privacy-changes-in-1-15-0
  source_release: dify-2026-06-25-1-15-0-github-344699591-4dd01045
  source_type: github_releases
  theme: safety-privacy
  title: 14 Safety and Privacy changes in 1.15.0
  type: change
related_changes:
- '[[Changes/Claude Code/2026-06-24-improved-sandbox-network-permission-dialog-hosts-you-allow-with-yes-are-now-reme|Improved
  sandbox network permission dialog]]'
- '[[Changes/GitHub Copilot CLI/2026-06-24-commands-with-slash-prefixed-string-arguments-e-g-body-azp-run-no-longer-trigger|Commands
  with slash-prefixed string arguments (e.g. --body "/azp run") no longer…]]'
- '[[Changes/Codex CLI/2026-06-25-2-safety-and-privacy-changes-in-rust-v0-142-2|2
  Safety and Privacy changes in rust-v0.142.2]]'
source_release: '[[Releases/Dify/dify-2026-06-25-1-15-0-github-344699591-4dd01045|dify-2026-06-25-1-15-0-github-344699591-4dd01045]]'
source_type: github_releases
theme: safety-privacy
title: 14 Safety and Privacy changes in 1.15.0
type: change
---

<!-- chronolog:begin region="header" -->
# 14 Safety and Privacy changes in 1.15.0

**Dify** · 2026-06-25 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.15.0) · from [[Releases/Dify/dify-2026-06-25-1-15-0-github-344699591-4dd01045|1.15.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> **More accessible** — plugin permission hints, restored contact-us menu, skip-nav link, and keyboard focus polish (#37310, #37774, #37644)

> `SSRF_PROXY_ALLOW_PRIVATE_DOMAINS`, `SSRF_PROXY_ALLOW_PRIVATE_IPS`, `SSRF_SANDBOX_PROXY_HOST`, `SSRF_SANDBOX_PROXY_PORT` (`docker/envs/middleware.env.example`)

> `SSRF_REVERSE_PROXY_PORT`, `SSRF_SANDBOX_HOST` (`docker/envs/middleware.env.example`)

> docs: add security policy by @bmtriet in https://github.com/langgenius/dify/pull/36873

> feat(agent): Sandbox / CLI Agent (dify.shell) + read-only sandbox file inspector by @zyssyz123 in https://github.com/langgenius/dify/pull/36984

> fix(web): show plugin auth permission hint by @Jingyi-Dify in https://github.com/langgenius/dify/pull/37310

> refactor(agent): replace workspace inspector with sandbox API by @BeautyyuYanli in https://github.com/langgenius/dify/pull/37349

> test: use caplog for workspace permission logging by @popsiclelmlm in https://github.com/langgenius/dify/pull/37473

> chore: workflow restore sandbox upgrade by @hjlarry in https://github.com/langgenius/dify/pull/37568

> chore: add ENTERPRISE_RBAC_API_URL check and update permission key by @fatelei in https://github.com/langgenius/dify/pull/37777

> chore: Update permission keys and descriptions for multiple languages to simplify application and dataset management phrases by @WTW0313 in https://github.com/langgenius/dify/pull/37859

> feat: filter dataset operator and add miss permission key by @fatelei in https://github.com/langgenius/dify/pull/37867

> build(deps): update Bleach sanitizer security fix by @gateway in https://github.com/langgenius/dify/pull/37860

> feat: update monitor permission key and plugin permission key by @fatelei in https://github.com/langgenius/dify/pull/37937

Source: https://github.com/langgenius/dify/releases/tag/1.15.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2026-06-25-6-interface-experience-changes-in-1-15-0|6 Interface Experience changes in 1.15.0]] · Interface Experience
- [[Changes/Dify/2026-06-25-38-agent-mode-changes-in-1-15-0|38 Agent Mode changes in 1.15.0]] · Agent Mode
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
- [[Changes/Dify/2026-06-25-27-apps-and-integrations-changes-in-1-15-0|27 Apps and Integrations changes in 1.15.0]] · Apps and Integrations
- [[Changes/Dify/2026-06-25-2-automation-and-scheduling-changes-in-1-15-0|2 Automation and Scheduling changes in 1.15.0]] · Automation and Scheduling
- [[Changes/Dify/2026-06-25-3-editor-experience-changes-in-1-15-0|3 Editor Experience changes in 1.15.0]] · Editor Experience
- [[Changes/Dify/2026-06-25-365-other-changes-in-1-15-0|365 other changes in 1.15.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-06-25 · Codex CLI · [[Changes/Codex CLI/2026-06-25-2-safety-and-privacy-changes-in-rust-v0-142-2|2 Safety and Privacy changes in rust-v0.142.2]]
- Later: 2026-06-25 · Google Antigravity · [[Changes/Google Antigravity/2026-06-25-3-safety-and-privacy-changes-in-hub-v2-2-1-antigravity-guide-audio|3 Safety and Privacy changes in HUB v2.2.1 — Antigravity Guide, audio…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Descript · [[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke Application Access]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-06-25-431d73&body=Card%3A%20Changes%2FDify%2F2026-06-25-14-safety-and-privacy-changes-in-1-15-0.md%0ACard%20ID%3A%20dify-2026-06-25-431d73%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.15.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->