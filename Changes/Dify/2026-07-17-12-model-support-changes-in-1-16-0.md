---
card_id: dify-2026-07-17-c43856
date: '2026-07-17'
description: 'Dify · 2026-07-17 · Model Support: 12 changes in v1.16.0 — **OpenAI
  GPT-5.6 Compatibility Notice**'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1285
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: c3aa1e2df10ef7cbae15c29cf71da1e2e7b4bf9446bc92169e102e294682ac58
product: dify
product_name: Dify
record:
  card_id: dify-2026-07-17-c43856
  comparison: ''
  date: '2026-07-17'
  description: 'Dify — v1.16.0: 12 Model Support changes'
  evidence:
  - quote: '**OpenAI GPT-5.6 Compatibility Notice**'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: The OpenAI plugin previously defaulted to using the Chat Completions API,
      which was deprecated by OpenAI earlier this year and has increasingly poor support
      for newer model series. The newly released GPT-5.6 family has many unusual and
      unique parameter combination restrictions when used with Chat Completions, because
      OpenAI now provides only minimal compatibility support for Chat Completions
      with new models. **This is not a Dify system issue.**
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: '> If you have previously configured a custom OpenAI API key, please check
      your API type setting and switch to **Responses** if it is still set to Chat
      Completions, especially when using GPT-5.6 or later models.'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: '| `NEW_USER_DEFAULT_MODELS` | _(empty)_ | `api/.env.example` | Default
      models for new users |'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: '> **One-time legacy model type migration for self-hosted upgrades**'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: '> This migration is **not included in `flask db upgrade`**. Without it,
      legacy model records can cause model-related API requests to fail with errors,
      preventing affected models from being loaded or used.'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: After applying the migration, run the dry-run command again. If it reports
      no additional row updates or deletions, restart the relevant services and verify
      that existing models can be loaded and invoked successfully.
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: '> - **OpenAI GPT-5.6 users**: If you have previously configured a custom
      OpenAI API key, verify your API type is set to **Responses** (not Chat Completions).
      See the Known Issues section above.'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: 'refactor(web): migrate model provider console contracts by @hyoban in
      https://github.com/langgenius/dify/pull/38253'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: 'refactor(api): migrate workspace model endpoints to BaseModel by @cqjjjzr
      in https://github.com/langgenius/dify/pull/37963'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: 'test: use sqlite3 session in test_comment_models by @asukaminato0721 in
      https://github.com/langgenius/dify/pull/38767'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  - quote: 'feat: add Responses API tip for GPT-5.6 and later models in multiple languages
      by @WTW0313 in https://github.com/langgenius/dify/pull/39188'
    source_release: https://github.com/langgenius/dify/releases/tag/1.16.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 12-model-support-changes-in-1-16-0
  source_release: dify-2026-07-17-1-16-0-github-355594285-636849e9
  source_type: github_releases
  theme: model-support
  title: 12 Model Support changes in 1.16.0
  type: change
related_changes:
- '[[Changes/Kimi Code/2026-07-16-3-model-support-changes-in-kimi-code-0-25-0|3 Model
  Support changes in Kimi Code 0.25.0]]'
- '[[Changes/Ollama/2026-07-16-2-model-support-changes-in-v0-32-1|2 Model Support
  changes in v0.32.1]]'
- '[[Changes/Claude Code/2026-07-17-3-model-support-changes-in-v2-1-212|3 Model Support
  changes in v2.1.212]]'
source_release: '[[Releases/Dify/dify-2026-07-17-1-16-0-github-355594285-636849e9|dify-2026-07-17-1-16-0-github-355594285-636849e9]]'
source_type: github_releases
theme: model-support
title: 12 Model Support changes in 1.16.0
type: change
---

<!-- chronolog:begin region="header" -->
# 12 Model Support changes in 1.16.0

**Dify** · 2026-07-17 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.16.0) · from [[Releases/Dify/dify-2026-07-17-1-16-0-github-355594285-636849e9|v1.16.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> **OpenAI GPT-5.6 Compatibility Notice**

> The OpenAI plugin previously defaulted to using the Chat Completions API, which was deprecated by OpenAI earlier this year and has increasingly poor support for newer model series. The newly released GPT-5.6 family has many unusual and unique parameter combination restrictions when used with Chat Completions, because OpenAI now provides only minimal compatibility support for Chat Completions with new models. **This is not a Dify system issue.**

> > If you have previously configured a custom OpenAI API key, please check your API type setting and switch to **Responses** if it is still set to Chat Completions, especially when using GPT-5.6 or later models.

> | `NEW_USER_DEFAULT_MODELS` | _(empty)_ | `api/.env.example` | Default models for new users |

> > **One-time legacy model type migration for self-hosted upgrades**

> > This migration is **not included in `flask db upgrade`**. Without it, legacy model records can cause model-related API requests to fail with errors, preventing affected models from being loaded or used.

> After applying the migration, run the dry-run command again. If it reports no additional row updates or deletions, restart the relevant services and verify that existing models can be loaded and invoked successfully.

> > - **OpenAI GPT-5.6 users**: If you have previously configured a custom OpenAI API key, verify your API type is set to **Responses** (not Chat Completions). See the Known Issues section above.

> refactor(web): migrate model provider console contracts by @hyoban in https://github.com/langgenius/dify/pull/38253

> refactor(api): migrate workspace model endpoints to BaseModel by @cqjjjzr in https://github.com/langgenius/dify/pull/37963

> test: use sqlite3 session in test_comment_models by @asukaminato0721 in https://github.com/langgenius/dify/pull/38767

> feat: add Responses API tip for GPT-5.6 and later models in multiple languages by @WTW0313 in https://github.com/langgenius/dify/pull/39188

Source: https://github.com/langgenius/dify/releases/tag/1.16.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2026-07-17-20-safety-and-privacy-changes-in-1-16-0|20 Safety and Privacy changes in 1.16.0]] · Safety and Privacy
- [[Changes/Dify/2026-07-17-agent-app-enters-open-beta-and-is-now-enabled-by-default-for-all-users-it-introd|Agent App enters open beta and is now enabled by default for all users]] · Safety and Privacy
- [[Changes/Dify/2026-07-17-16-context-window-changes-in-1-16-0|16 Context Window changes in 1.16.0]] · Context Window
- [[Changes/Dify/2026-07-17-perf-memory-batch-load-message-files-in-tokenbuffermemory-to-remove-n-1-queries|perf(memory): batch-load message files in TokenBufferMemory to remove N+1 queries]] · Memory and Personalization
- [[Changes/Dify/2026-07-17-8-account-and-access-changes-in-1-16-0|8 Account and Access changes in 1.16.0]] · Account and Access
- [[Changes/Dify/2026-07-17-4-editor-experience-changes-in-1-16-0|4 Editor Experience changes in 1.16.0]] · Editor Experience
- [[Changes/Dify/2026-07-17-3-voice-and-audio-changes-in-1-16-0|3 Voice and Audio changes in 1.16.0]] · Voice and Audio
- [[Changes/Dify/2026-07-17-4-collaboration-changes-in-1-16-0|4 Collaboration changes in 1.16.0]] · Collaboration
- [[Changes/Dify/2026-07-17-3-developer-workflow-changes-in-1-16-0|3 Developer Workflow changes in 1.16.0]] · Developer Workflow
- [[Changes/Dify/2026-07-17-24-apps-and-integrations-changes-in-1-16-0|24 Apps and Integrations changes in 1.16.0]] · Apps and Integrations
- [[Changes/Dify/2026-07-17-2-automation-and-scheduling-changes-in-1-16-0|2 Automation and Scheduling changes in 1.16.0]] · Automation and Scheduling
- [[Changes/Dify/2026-07-17-2-interface-experience-changes-in-1-16-0|2 Interface Experience changes in 1.16.0]] · Interface Experience
- [[Changes/Dify/2026-07-17-2-files-and-data-changes-in-1-16-0|2 Files and Data changes in 1.16.0]] · Files and Data
- [[Changes/Dify/2026-07-17-chore-improve-workflow-generator-accessibility-and-api-contracts-by-crazywoola-i|chore: Improve workflow generator accessibility and API contracts]] · Accessibility and Localization
- [[Changes/Dify/2026-07-17-2-enterprise-and-administration-changes-in-1-16-0|2 Enterprise and Administration changes in 1.16.0]] · Enterprise and Administration
- [[Changes/Dify/2026-07-17-3-reliability-and-performance-changes-in-1-16-0|3 Reliability and Performance changes in 1.16.0]] · Reliability and Performance
- [[Changes/Dify/2026-07-17-64-agent-mode-changes-in-1-16-0|64 Agent Mode changes in 1.16.0]] · Agent Mode
- [[Changes/Dify/2026-07-17-5-pricing-model-changes-in-1-16-0|5 Pricing Model changes in 1.16.0]] · Pricing Model
- [[Changes/Dify/2026-07-17-237-other-changes-in-1-16-0|237 other changes in 1.16.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-07-17 · Claude Code · [[Changes/Claude Code/2026-07-17-3-model-support-changes-in-v2-1-212|3 Model Support changes in v2.1.212]]
- Later: 2026-07-17 · Kimi Code · [[Changes/Kimi Code/2026-07-17-using-an-api-key-for-kimi-coding-models-now-also-fetches-the-latest-model-list-a|Using an API key for Kimi coding models now also fetches the latest model list…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-07-17-c43856&body=Card%3A%20Changes%2FDify%2F2026-07-17-12-model-support-changes-in-1-16-0.md%0ACard%20ID%3A%20dify-2026-07-17-c43856%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.16.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->