---
card_id: krea-2026-10-27-75215a
date: '2026-10-27'
description: 'Krea · 2026-10-27 · Developer Workflow: **A new [Errors and debugging](https://www.krea.ai/docs/developers/errors-and-debugging.md)
  reference lists every API…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter
    Colors]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2968
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: significant
kind: launch
machine_hash: 4987c7376062cabdd2342a92ac0402a03c569dde2f8ade0449aa42fe9d9aed29
product: krea
product_name: Krea
record:
  ai_generated: true
  card_id: krea-2026-10-27-75215a
  comparison: ''
  confidence: low
  date: '2026-10-27'
  description: 'Krea — Agent builds custom nodes, GPT-6.1 Terra in Agent, Nodes projects
    shared with your organization, 4K Krea 3 output in the API, personal and service
    API tokens, API errors reference, searchable Nodes chats, and fixes: **A new [Errors
    and debugging](https://www.krea.ai/docs/developers/errors-and-debugging.md) reference
    lists every API status code, response body, and failed-job `error.code`.**'
  evidence:
  - quote: '**A new [Errors and debugging](https://www.krea.ai/docs/developers/errors-and-debugging.md)
      reference lists every API status code, response body, and failed-job `error.code`.**'
    source_release: https://www.krea.ai/docs/changelog
  - quote: Over your concurrency cap, jobs are backlogged only on Pro and above, for
      supported models, and outside Zero Data Retention. Otherwise the request can
      return `429`.
    source_release: https://www.krea.ai/docs/changelog
  - quote: Krea 2 requests aren't backlogged on any plan right now.
    source_release: https://www.krea.ai/docs/changelog
  - quote: The API doesn't send `Retry-After`. On `429`, retry with backoff after
      in-flight jobs finish.
    source_release: https://www.krea.ai/docs/changelog
  - quote: 'Send `Accept: application/json` to get JSON error bodies.'
    source_release: https://www.krea.ai/docs/changelog
  extractor_version: fallback-v5
  impact: significant
  kind: launch
  product: krea
  product_name: Krea
  slug: api-errors-and-concurrency-limits
  source_release: krea-2026-10-27-2026-10-27-agent-builds-custom-nodes-gpt-6-1-terra-in-agent-node-195cc82a
  source_type: krea_changelog
  theme: developer-workflow
  title: API errors and concurrency limits
  type: change
related_changes:
- '[[Changes/Windsurf/2026-10-26-2-developer-workflow-changes-in-v3-11-228|2 Developer
  Workflow changes in v3.11.228]]'
- '[[Changes/Codex CLI/2026-10-27-3-developer-workflow-changes-in-rust-v0-165-0|3
  Developer Workflow changes in rust-v0.165.0]]'
- '[[Changes/Google Antigravity/2026-10-27-long-commands-in-the-background-command-view-are-now-syntax-highlighted-and-coll|Long
  commands in the background command view are now syntax highlighted…]]'
source_release: '[[Releases/Krea/krea-2026-10-27-2026-10-27-agent-builds-custom-nodes-gpt-6-1-terra-in-agent-node-195cc82a|krea-2026-10-27-2026-10-27-agent-builds-custom-nodes-gpt-6-1-terra-in-agent-node-195cc82a]]'
source_type: krea_changelog
theme: developer-workflow
title: API errors and concurrency limits
type: change
---

<!-- chronolog:begin region="header" -->
# API errors and concurrency limits

**Krea** · 2026-10-27 · [[Themes/developer-workflow|Developer Workflow]] · Launch · [Official source](https://www.krea.ai/docs/changelog) · from [[Releases/Krea/krea-2026-10-27-2026-10-27-agent-builds-custom-nodes-gpt-6-1-terra-in-agent-node-195cc82a|Agent builds custom nodes, GPT-6.1 Terra in Agent, Nodes projects shared with your organization, 4K Krea 3 output in the API, personal and service API tokens, API errors reference, searchable Nodes chats, and fixes]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> **A new [Errors and debugging](https://www.krea.ai/docs/developers/errors-and-debugging.md) reference lists every API status code, response body, and failed-job `error.code`.**
>
> Over your concurrency cap, jobs are backlogged only on Pro and above, for supported models, and outside Zero Data Retention. Otherwise the request can return `429`.
>
> Krea 2 requests aren't backlogged on any plan right now.
>
> The API doesn't send `Retry-After`. On `429`, retry with backoff after in-flight jobs finish.
>
> Send `Accept: application/json` to get JSON error bodies.
>
> Source: https://www.krea.ai/docs/changelog
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Krea/2026-10-27-api-usage-page|API Usage page]] · Context Window
- [[Changes/Krea/2026-10-27-nodes-and-promo-updates|Nodes and promo updates]] · Agent Mode
- [[Changes/Krea/2026-10-27-share-nodes-projects-with-your-organization|Share Nodes projects with your organization]] · Collaboration
- [[Changes/Krea/2026-10-27-gpt-6-1-terra-in-agent|GPT-6.1 Terra in Agent]] · Model Support
- [[Changes/Krea/2026-10-27-krea-3-api-sizing-and-billing-updates|Krea 3 API sizing and billing updates]] · Pricing Model
- [[Changes/Krea/2026-10-27-personal-and-service-api-tokens|Personal and service API tokens]] · Context Window
- [[Changes/Krea/2026-10-27-old-and-renamed-model-page-links-now-redirect-instead-of-showing-a-404|Old and renamed model page links now redirect instead of showing a 404]] · Model Support
- [[Changes/Krea/2026-10-27-polished-the-mobile-model-picker-and-sidebar|Polished the mobile model picker and sidebar]] · Interface Experience
- [[Changes/Krea/2026-10-27-agent-builds-custom-nodes-in-nodes|Agent builds custom nodes in Nodes]] · Agent Mode
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-10-27 · Google Antigravity · [[Changes/Google Antigravity/2026-10-27-long-commands-in-the-background-command-view-are-now-syntax-highlighted-and-coll|Long commands in the background command view are now syntax highlighted…]]
- Later: 2026-10-27 · OpenClaw · [[Changes/OpenClaw/2026-10-27-2-developer-workflow-changes-in-v2026-10-8|2 Developer Workflow changes in v2026.10.8]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-09-11 · Descript · [[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter Colors]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20krea-2026-10-27-75215a&body=Card%3A%20Changes%2FKrea%2F2026-10-27-api-errors-and-concurrency-limits.md%0ACard%20ID%3A%20krea-2026-10-27-75215a%0ASource%3A%20https%3A%2F%2Fwww.krea.ai%2Fdocs%2Fchangelog%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->