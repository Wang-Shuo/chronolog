---
card_id: dify-2026-09-10-960e35
date: '2026-09-10'
description: 'Dify · 2026-09-10 · Safety and Privacy: 16 changes in v1.17.1 - Bug
  Fixes and Improvements — The generated Service API contract was realigned with runtime…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1243
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: bb93c167fa7e9cfa0c798006cb5016668ee8645f356d6960ea0e3361175f6d99
product: dify
product_name: Dify
record:
  card_id: dify-2026-09-10-960e35
  comparison: ''
  date: '2026-09-10'
  description: 'Dify — v1.17.1 - Bug Fixes and Improvements: 16 Safety and Privacy
    changes'
  evidence:
  - quote: 'The generated Service API contract was realigned with runtime behavior:
      non-nullable fields no longer carry null defaults, Console-only permission metadata
      is excluded, error responses the endpoints never return are removed, historical
      404/503 declarations are restored, and task-stop request schemas are split so
      chat/completion and workflow behavior are documented accurately. This changes
      the exported contract and generated clients, not request handling. (#41248,
      #41274, #41943)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'Registration tracking is consent-safe and retryable, and Web App analytics
      are separated from console page tracking (#41365, #41251)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: '**Bundled Weaviate server upgraded from `1.27.0` to `1.39.2`**, moving
      the pull from Docker Hub to `cr.weaviate.io`, the registry Weaviate publishes
      to directly. `1.39` ships no breaking changes and is where Weaviate''s bug and
      security backports land — but existing data volumes require a staged manual
      upgrade, covered in the [Upgrade Guide](#bundled-weaviate-server-upgrade-127--139).
      Dify also now sends an `X-Weaviate-Client-Integration: dify/<version>` header
      so Weaviate can attribute traffic to Dify in its server-side telemetry; registration
      is best-effort and never blocks client initialization. (#38214)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: '| `EXPOSE_LOCAL_SANDBOX_PORT` | `5004` | Publishes the local sandbox in
      the middleware-only stack, so a locally-run agent backend can reach it. |'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: '| `DIFY_AGENT_LOCAL_SANDBOX_AUTH_TOKEN` | *(empty)* | `shellctl` auth
      token for the middleware-only local sandbox. |'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'fix(api): enforce RBAC permission on agent app detail GET endpoint (#41264)
      by @agarwalpranav0711 in https://github.com/langgenius/dify/pull/41265'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'fix(api): enforce RBAC permission on agent composer GET endpoint (#41324)
      by @agarwalpranav0711 in https://github.com/langgenius/dify/pull/41325'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'chore: remove permission check by @fatelei in https://github.com/langgenius/dify/pull/41349'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'chore: add permission check back by @fatelei in https://github.com/langgenius/dify/pull/41369'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'feat: hide skill_entry when use has no skill.view permission by @fatelei
      in https://github.com/langgenius/dify/pull/41429'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'fix(web): make registration tracking consent-safe and retryable by @CodingOnStar
      in https://github.com/langgenius/dify/pull/41365'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'feat: app access point permission by @WTW0313 in https://github.com/langgenius/dify/pull/41631'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'fix(web): allow CookieYes consent logging by @lyzno1 in https://github.com/langgenius/dify/pull/41812'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'fix(api): enforce RBAC permission on MCP tool provider GET endpoint (#41547)
      by @agarwalpranav0711 in https://github.com/langgenius/dify/pull/41548'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'test: split CodeNode validation from sandbox coverage by @asukaminato0721
      in https://github.com/langgenius/dify/pull/40707'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  - quote: 'fix: fix agent.id mismatch lead permission keys are empty by @fatelei
      in https://github.com/langgenius/dify/pull/42095'
    source_release: https://github.com/langgenius/dify/releases/tag/1.17.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 16-safety-and-privacy-changes-in-1-17-1
  source_release: dify-2026-09-10-1-17-1-github-386157159-e472b6fe
  source_type: github_releases
  theme: safety-privacy
  title: 16 Safety and Privacy changes in 1.17.1
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-09-09-25-safety-and-privacy-changes-in-rust-v0-154-0|25
  Safety and Privacy changes in rust-v0.154.0]]'
- '[[Changes/Google Antigravity/2026-09-09-3-safety-and-privacy-changes-in-hub-v2-13-0-introducing-new-documents|3
  Safety and Privacy changes in HUB v2.13.0 — Introducing new Documents…]]'
- '[[Changes/Claude Code/2026-09-10-8-safety-and-privacy-changes-in-v2-1-268|8 Safety
  and Privacy changes in v2.1.268]]'
source_release: '[[Releases/Dify/dify-2026-09-10-1-17-1-github-386157159-e472b6fe|dify-2026-09-10-1-17-1-github-386157159-e472b6fe]]'
source_type: github_releases
theme: safety-privacy
title: 16 Safety and Privacy changes in 1.17.1
type: change
---

<!-- chronolog:begin region="header" -->
# 16 Safety and Privacy changes in 1.17.1

**Dify** · 2026-09-10 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.17.1) · from [[Releases/Dify/dify-2026-09-10-1-17-1-github-386157159-e472b6fe|v1.17.1 - Bug Fixes and Improvements]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> The generated Service API contract was realigned with runtime behavior: non-nullable fields no longer carry null defaults, Console-only permission metadata is excluded, error responses the endpoints never return are removed, historical 404/503 declarations are restored, and task-stop request schemas are split so chat/completion and workflow behavior are documented accurately. This changes the exported contract and generated clients, not request handling. (#41248, #41274, #41943)

> Registration tracking is consent-safe and retryable, and Web App analytics are separated from console page tracking (#41365, #41251)

> **Bundled Weaviate server upgraded from `1.27.0` to `1.39.2`**, moving the pull from Docker Hub to `cr.weaviate.io`, the registry Weaviate publishes to directly. `1.39` ships no breaking changes and is where Weaviate's bug and security backports land — but existing data volumes require a staged manual upgrade, covered in the [Upgrade Guide](#bundled-weaviate-server-upgrade-127--139). Dify also now sends an `X-Weaviate-Client-Integration: dify/<version>` header so Weaviate can attribute traffic to Dify in its server-side telemetry; registration is best-effort and never blocks client initialization. (#38214)

> | `EXPOSE_LOCAL_SANDBOX_PORT` | `5004` | Publishes the local sandbox in the middleware-only stack, so a locally-run agent backend can reach it. |

> | `DIFY_AGENT_LOCAL_SANDBOX_AUTH_TOKEN` | *(empty)* | `shellctl` auth token for the middleware-only local sandbox. |

> fix(api): enforce RBAC permission on agent app detail GET endpoint (#41264) by @agarwalpranav0711 in https://github.com/langgenius/dify/pull/41265

> fix(api): enforce RBAC permission on agent composer GET endpoint (#41324) by @agarwalpranav0711 in https://github.com/langgenius/dify/pull/41325

> chore: remove permission check by @fatelei in https://github.com/langgenius/dify/pull/41349

> chore: add permission check back by @fatelei in https://github.com/langgenius/dify/pull/41369

> feat: hide skill_entry when use has no skill.view permission by @fatelei in https://github.com/langgenius/dify/pull/41429

> fix(web): make registration tracking consent-safe and retryable by @CodingOnStar in https://github.com/langgenius/dify/pull/41365

> feat: app access point permission by @WTW0313 in https://github.com/langgenius/dify/pull/41631

> fix(web): allow CookieYes consent logging by @lyzno1 in https://github.com/langgenius/dify/pull/41812

> fix(api): enforce RBAC permission on MCP tool provider GET endpoint (#41547) by @agarwalpranav0711 in https://github.com/langgenius/dify/pull/41548

> test: split CodeNode validation from sandbox coverage by @asukaminato0721 in https://github.com/langgenius/dify/pull/40707

> fix: fix agent.id mismatch lead permission keys are empty by @fatelei in https://github.com/langgenius/dify/pull/42095

Source: https://github.com/langgenius/dify/releases/tag/1.17.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2026-09-10-4-pricing-model-changes-in-1-17-1|4 Pricing Model changes in 1.17.1]] · Pricing Model
- [[Changes/Dify/2026-09-10-3-automation-and-scheduling-changes-in-1-17-1|3 Automation and Scheduling changes in 1.17.1]] · Automation and Scheduling
- [[Changes/Dify/2026-09-10-8-interface-experience-changes-in-1-17-1|8 Interface Experience changes in 1.17.1]] · Interface Experience
- [[Changes/Dify/2026-09-10-76-model-support-changes-in-1-17-1|76 Model Support changes in 1.17.1]] · Model Support
- [[Changes/Dify/2026-09-10-42-agent-mode-changes-in-1-17-1|42 Agent Mode changes in 1.17.1]] · Agent Mode
- [[Changes/Dify/2026-09-10-4-developer-workflow-changes-in-1-17-1|4 Developer Workflow changes in 1.17.1]] · Developer Workflow
- [[Changes/Dify/2026-09-10-3-collaboration-changes-in-1-17-1|3 Collaboration changes in 1.17.1]] · Collaboration
- [[Changes/Dify/2026-09-10-2-memory-and-personalization-changes-in-1-17-1|2 Memory and Personalization changes in 1.17.1]] · Memory and Personalization
- [[Changes/Dify/2026-09-10-13-files-and-data-changes-in-1-17-1|13 Files and Data changes in 1.17.1]] · Files and Data
- [[Changes/Dify/2026-09-10-skill-packages-built-on-windows-failed-with-a-misleading-error-a-skill-md-using|Skill packages built on Windows failed with a misleading error. A SKILL.md…]] · Mobile and Desktop
- [[Changes/Dify/2026-09-10-12-apps-and-integrations-changes-in-1-17-1|12 Apps and Integrations changes in 1.17.1]] · Apps and Integrations
- [[Changes/Dify/2026-09-10-6-account-and-access-changes-in-1-17-1|6 Account and Access changes in 1.17.1]] · Account and Access
- [[Changes/Dify/2026-09-10-3-multimodal-input-changes-in-1-17-1|3 Multimodal Input changes in 1.17.1]] · Multimodal Input
- [[Changes/Dify/2026-09-10-6-editor-experience-changes-in-1-17-1|6 Editor Experience changes in 1.17.1]] · Editor Experience
- [[Changes/Dify/2026-09-10-3-accessibility-and-localization-changes-in-1-17-1|3 Accessibility and Localization changes in 1.17.1]] · Accessibility and Localization
- [[Changes/Dify/2026-09-10-a-plugin-could-exhaust-worker-memory-with-one-declared-number-the-blob-chunk-mer|A plugin could exhaust worker memory with one declared number. The blob chunk…]] · Reliability and Performance
- [[Changes/Dify/2026-09-10-6-context-window-changes-in-1-17-1|6 Context Window changes in 1.17.1]] · Context Window
- [[Changes/Dify/2026-09-10-205-other-changes-in-1-17-1|205 other changes in 1.17.1]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-09-10 · Claude Code · [[Changes/Claude Code/2026-09-10-8-safety-and-privacy-changes-in-v2-1-268|8 Safety and Privacy changes in v2.1.268]]
- Later: 2026-09-10 · Windsurf · [[Changes/Windsurf/2026-09-10-devin-cloud|Devin Cloud]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-09-10-960e35&body=Card%3A%20Changes%2FDify%2F2026-09-10-16-safety-and-privacy-changes-in-1-17-1.md%0ACard%20ID%3A%20dify-2026-09-10-960e35%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.17.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->