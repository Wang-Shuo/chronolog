---
card_id: dify-2026-05-19-519821
date: '2026-05-19'
description: 'Dify · 2026-05-19 · Apps and Integrations: 4 changes in v1.14.2 - Security
  fixes, agent groundwork, workflow reliability, and deployment updates — **Tracing…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If
    you have a recording with each speaker with a different microphone, or saved…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2713
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 9d26afd4f2a0d5eb56fe451e059cb07c55809647f07a070c803baf8899db266f
product: dify
product_name: Dify
record:
  card_id: dify-2026-05-19-519821
  comparison: ''
  date: '2026-05-19'
  description: 'Dify — v1.14.2 - Security fixes, agent groundwork, workflow reliability,
    and deployment updates: 4 Apps and Integrations changes'
  evidence:
  - quote: '**Tracing reliability** — isolated Langfuse v3 SDK tracer providers to
      prevent cross-task interference and added Phoenix parent trace fallback behavior.
      Thanks @GareArc and @Blackoutta in [#36136](https://github.com/langgenius/dify/pull/36136)
      and [#36290](https://github.com/langgenius/dify/pull/36290).'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.2
  - quote: '**Deployment tuning** — upgraded plugin-daemon to `0.6.1`, increased the
      default GraphEngine minimum worker count, and refreshed Docker README references.
      Thanks @laipz8200, @kenwoodjw, and @RiskeyL in [#36312](https://github.com/langgenius/dify/pull/36312),
      [#35650](https://github.com/langgenius/dify/pull/35650), and [#36303](https://github.com/langgenius/dify/pull/36303).'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.2
  - quote: 'refactor(install): improve layout and scrolling behavior for plugin installation
      step by @CodingOnStar in https://github.com/langgenius/dify/pull/36199'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.2
  - quote: 'chore(docker): upgrade plugin daemon to 0.6.1 by @laipz8200 in https://github.com/langgenius/dify/pull/36312'
    source_release: https://github.com/langgenius/dify/releases/tag/1.14.2
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 4-apps-and-integrations-changes-in-1-14-2
  source_release: dify-2026-05-19-1-14-2-github-324730496-11d48ace
  source_type: github_releases
  theme: apps-integrations
  title: 4 Apps and Integrations changes in 1.14.2
  type: change
related_changes:
- '[[Changes/Cline/2026-05-19-disable-the-mcp-restart-server-button-when-a-server-is-toggled-off|Disable
  the MCP "Restart Server" button when a server is toggled off]]'
- '[[Changes/Cursor/2026-05-19-cursor-is-now-available-in-jira|Cursor is now available
  in Jira]]'
- '[[Changes/Cursor/2026-05-19-install-the-integration-from-cursor-integrations-you-need-cursor-admin-access-an|Install
  the integration from Cursor integrations]]'
source_release: '[[Releases/Dify/dify-2026-05-19-1-14-2-github-324730496-11d48ace|dify-2026-05-19-1-14-2-github-324730496-11d48ace]]'
source_type: github_releases
theme: apps-integrations
title: 4 Apps and Integrations changes in 1.14.2
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Apps and Integrations changes in 1.14.2

**Dify** · 2026-05-19 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.14.2) · from [[Releases/Dify/dify-2026-05-19-1-14-2-github-324730496-11d48ace|v1.14.2 - Security fixes, agent groundwork, workflow reliability, and deployment updates]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> **Tracing reliability** — isolated Langfuse v3 SDK tracer providers to prevent cross-task interference and added Phoenix parent trace fallback behavior. Thanks @GareArc and @Blackoutta in [#36136](https://github.com/langgenius/dify/pull/36136) and [#36290](https://github.com/langgenius/dify/pull/36290).

> **Deployment tuning** — upgraded plugin-daemon to `0.6.1`, increased the default GraphEngine minimum worker count, and refreshed Docker README references. Thanks @laipz8200, @kenwoodjw, and @RiskeyL in [#36312](https://github.com/langgenius/dify/pull/36312), [#35650](https://github.com/langgenius/dify/pull/35650), and [#36303](https://github.com/langgenius/dify/pull/36303).

> refactor(install): improve layout and scrolling behavior for plugin installation step by @CodingOnStar in https://github.com/langgenius/dify/pull/36199

> chore(docker): upgrade plugin daemon to 0.6.1 by @laipz8200 in https://github.com/langgenius/dify/pull/36312

Source: https://github.com/langgenius/dify/releases/tag/1.14.2
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2026-05-19-3-model-support-changes-in-1-14-2|3 Model Support changes in 1.14.2]] · Model Support
- [[Changes/Dify/2026-05-19-feat-messagelogmodal-refactor-modal-structure-and-improve-tab-handling-by-coding|feat(MessageLogModal): refactor modal structure and improve tab handling]] · Editor Experience
- [[Changes/Dify/2026-05-19-knowledge-base-stability-fixed-knowledge-hit-testing-rendering-empty-knowledge-c|Knowledge-base stability — fixed knowledge hit-testing rendering, empty…]] · Reliability and Performance
- [[Changes/Dify/2026-05-19-2-safety-and-privacy-changes-in-1-14-2|2 Safety and Privacy changes in 1.14.2]] · Safety and Privacy
- [[Changes/Dify/2026-05-19-chore-enchance-copywriting-in-none-education-plan-warning-modal-by-iamjoel-in-ht|chore: enchance copywriting in none education plan warning modal]] · Enterprise and Administration
- [[Changes/Dify/2026-05-19-app-creation-and-onboarding-tracked-app-creation-source-and-template-id-initiali|App creation and onboarding]] · Interface Experience
- [[Changes/Dify/2026-05-19-3-agent-mode-changes-in-1-14-2|3 Agent Mode changes in 1.14.2]] · Agent Mode
- [[Changes/Dify/2026-05-19-workflow-execution-reliability-restored-tracing-after-hitl-workflow-resume-impro|Workflow execution reliability]] · Memory and Personalization
- [[Changes/Dify/2026-05-19-59-other-changes-in-1-14-2|59 other changes in 1.14.2]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-05-19 · Cursor · [[Changes/Cursor/2026-05-19-install-the-integration-from-cursor-integrations-you-need-cursor-admin-access-an|Install the integration from Cursor integrations]]
- Later: 2026-05-19 · Gemini · [[Changes/Gemini/2026-05-19-daily-brief-is-your-personalized-overview-of-what-matters-today|Daily Brief is your personalized overview of what matters today]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-12-14 · Descript · [[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If you have a recording with each speaker with a different microphone, or saved…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-05-19-519821&body=Card%3A%20Changes%2FDify%2F2026-05-19-4-apps-and-integrations-changes-in-1-14-2.md%0ACard%20ID%3A%20dify-2026-05-19-519821%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.14.2%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->