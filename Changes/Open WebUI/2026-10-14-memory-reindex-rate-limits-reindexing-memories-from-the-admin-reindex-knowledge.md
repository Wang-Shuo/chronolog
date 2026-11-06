---
card_id: open-webui-2026-10-14-f78750
date: '2026-10-14'
description: "Open WebUI · 2026-10-14 · Memory and Personalization: \U0001F9EE **Memory
  reindex rate limits.** Reindexing memories, from the admin Reindex Knowledge and
  Memory…"
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom
    instructions are rolling out in beta]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1182
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: memory
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: significant
kind: policy
machine_hash: f2bfc9af3793ba3b42b93d58979ac35949e82835bfc8b6171819bab8ff3042a8
product: open-webui
product_name: Open WebUI
record:
  ai_generated: true
  card_id: open-webui-2026-10-14-f78750
  comparison: ''
  confidence: low
  date: '2026-10-14'
  description: "Open WebUI — v0.12.2: \U0001F9EE **Memory reindex rate limits.** Reindexing
    memories, from the admin Reindex Knowledge and Memory Vectors button, a user resetting
    their memory vectors or the automatic reindex after an embedding model change,
    now follows the Embedding Concurrent Requests limit and batch size, where it sent
    one request per memory at once and rate-limited providers failed most of them
    with 429 errors. [#32420](https://github.com/open-webui/open-webui/pull/32420),
    [Commit](https://github.com/open-webui/open-webui/commit/8bddf9bc62c3ffcaa3e6433bc5ac0f1d04a94421),
    [#32212](https://github.com/open-webui/open-webui/issues/32212)"
  evidence:
  - quote: "\U0001F9EE **Memory reindex rate limits.** Reindexing memories, from the
      admin Reindex Knowledge and Memory Vectors button, a user resetting their memory
      vectors or the automatic reindex after an embedding model change, now follows
      the Embedding Concurrent Requests limit and batch size, where it sent one request
      per memory at once and rate-limited providers failed most of them with 429 errors.
      [#32420](https://github.com/open-webui/open-webui/pull/32420), [Commit](https://github.com/open-webui/open-webui/commit/8bddf9bc62c3ffcaa3e6433bc5ac0f1d04a94421),
      [#32212](https://github.com/open-webui/open-webui/issues/32212)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.2
  extractor_version: fallback-v5
  impact: significant
  kind: policy
  product: open-webui
  product_name: Open WebUI
  slug: memory-reindex-rate-limits-reindexing-memories-from-the-admin-reindex-knowledge
  source_release: open-webui-2026-10-14-v0-12-2-github-413184477-0a3afe9d
  source_type: github_releases
  theme: memory
  theme_matches:
  - matched_terms:
    - memory
    - memories
    score: 160
    theme: memory
  - matched_terms:
    - model
    score: 50
    theme: model-support
  title: "\U0001F9EE **Memory reindex rate limits.** Reindexing memories, from the
    admin Reindex…"
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-10-08-51223-remove-legacy-personality-template-metadata-rhan-oai|♯51223
  Remove legacy personality template metadata @rhan-oai]]'
- '[[Changes/Open WebUI/2026-10-10-2-memory-and-personalization-changes-in-v0-12-0|2
  Memory and Personalization changes in v0.12.0]]'
- "[[Changes/Open WebUI/2026-10-14-memory-in-automations-automations-now-get-the-memory-tools-when-the-user-has-mem|\U0001F9E0
  Memory in automations. Automations now get the memory tools when the user has…]]"
source_release: '[[Releases/Open WebUI/open-webui-2026-10-14-v0-12-2-github-413184477-0a3afe9d|open-webui-2026-10-14-v0-12-2-github-413184477-0a3afe9d]]'
source_type: github_releases
theme: memory
title: "\U0001F9EE Memory reindex rate limits. Reindexing memories, from the admin
  Reindex…"
type: change
---

<!-- chronolog:begin region="header" -->
# 🧮 **Memory reindex rate limits.** Reindexing memories, from the admin Reindex…

**Open WebUI** · 2026-10-14 · [[Themes/memory|Memory and Personalization]] · Policy · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.12.2) · from [[Releases/Open WebUI/open-webui-2026-10-14-v0-12-2-github-413184477-0a3afe9d|v0.12.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> 🧮 **Memory reindex rate limits.** Reindexing memories, from the admin Reindex Knowledge and Memory Vectors button, a user resetting their memory vectors or the automatic reindex after an embedding model change, now follows the Embedding Concurrent Requests limit and batch size, where it sent one request per memory at once and rate-limited providers failed most of them with 429 errors. [#32420](https://github.com/open-webui/open-webui/pull/32420), [Commit](https://github.com/open-webui/open-webui/commit/8bddf9bc62c3ffcaa3e6433bc5ac0f1d04a94421), [#32212](https://github.com/open-webui/open-webui/issues/32212)
>
> Source: https://github.com/open-webui/open-webui/releases/tag/v0.12.2
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-10-14-open-attached-knowledge-from-its-preview-clicking-the-name-in-the-preview-of-an|📚 Open attached knowledge from its preview. Clicking the name in the preview…]] · Editor Experience
- [[Changes/Open WebUI/2026-10-14-6-developer-workflow-changes-in-v0-12-2|6 Developer Workflow changes in v0.12.2]] · Developer Workflow
- [[Changes/Open WebUI/2026-10-14-general-improvements-various-improvements-were-implemented-across-the-applicatio|🔄 General improvements. Various improvements were implemented across…]] · Reliability and Performance
- [[Changes/Open WebUI/2026-10-14-automation-run-results-an-automation-run-is-now-recorded-as-successful-only-afte|⏰ Automation run results. An automation run is now recorded as successful only…]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-10-14-voice-on-android-chrome-voice-calls-and-dictation-on-android-chrome-no-longer-go|📱 Voice on Android Chrome. Voice calls and dictation on Android Chrome no longer…]] · Voice and Audio
- [[Changes/Open WebUI/2026-10-14-per-chat-terminal-file-actions-with-the-open-terminal-chat-context-set-to-per-ch|🖥️ Per chat terminal file actions. With the Open Terminal chat context set…]] · Context Window
- [[Changes/Open WebUI/2026-10-14-4-model-support-changes-in-v0-12-2|4 Model Support changes in v0.12.2]] · Model Support
- [[Changes/Open WebUI/2026-10-14-scim-cannot-delete-admins-an-identity-provider-can-no-longer-delete-administrato|👮 SCIM cannot delete admins. An identity provider can no longer delete…]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-10-14-2-interface-experience-changes-in-v0-12-2|2 Interface Experience changes in v0.12.2]] · Interface Experience
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Memory and Personalization

- Earlier: 2026-10-14 · Open WebUI · [[Changes/Open WebUI/2026-10-14-memory-in-automations-automations-now-get-the-memory-tools-when-the-user-has-mem|🧠 Memory in automations. Automations now get the memory tools when the user has…]]
- Later: 2026-10-15 · Codex CLI · [[Changes/Codex CLI/2026-10-15-codex-can-run-independent-read-only-tools-in-parallel-including-skill-memory-and|Codex can run independent read-only tools in parallel, including skill, memory…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-20 · ChatGPT · [[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom instructions are rolling out in beta]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-10-14-f78750&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-10-14-memory-reindex-rate-limits-reindexing-memories-from-the-admin-reindex-knowledge.md%0ACard%20ID%3A%20open-webui-2026-10-14-f78750%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.12.2%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->