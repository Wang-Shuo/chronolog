---
card_id: anythingllm-2024-07-26-96e890
date: '2024-07-26'
description: 'AnythingLLM · 2024-07-26 · Automation and Scheduling: refactor: convert
  insert loop to 1 insert stmt by @jwaltz in…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2019-09-18-change-gain-with-volume-automation|Change
    gain, with volume automation]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1773
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: automation-scheduling
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: change
machine_hash: 0b17a6d9a120b91182b0b43b2fecec9c350ad550009e061949cda0fda6a702ef
product: anythingllm
product_name: AnythingLLM
record:
  card_id: anythingllm-2024-07-26-96e890
  comparison: ''
  date: '2024-07-26'
  description: "AnythingLLM — AnythingLLM v1.0.0 \U0001F389: refactor: convert insert
    loop to 1 insert stmt by @jwaltz in https://github.com/Mintplex-Labs/anything-llm/pull/19"
  evidence:
  - quote: 'refactor: convert insert loop to 1 insert stmt by @jwaltz in https://github.com/Mintplex-Labs/anything-llm/pull/19'
    source_release: https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.0.0
  extractor_version: fallback-v5
  impact: incremental
  kind: change
  product: anythingllm
  product_name: AnythingLLM
  slug: refactor-convert-insert-loop-to-1-insert-stmt-by-jwaltz-in-https-github-com-mint
  source_release: anythingllm-2024-07-26-v1-0-0-github-167428396-523db21a
  source_type: github_releases
  theme: automation-scheduling
  theme_matches: []
  theme_resolution: manual-semantic-rule-v1
  title: 'refactor: convert insert loop to 1 insert stmt'
  type: change
related_changes:
- '[[Changes/Dify/2024-07-15-refactor-api-switch-to-dify-config-with-pydantic-in-controllers-and-schedule-by|refactor(api):
  switch to dify_config with Pydantic in controllers and schedule]]'
- '[[Changes/Raycast/2024-07-17-my-schedule-improved-link-detection-reliability-when-the-event-contains-html|My
  Schedule: Improved link detection reliability when the event contains HTML]]'
- '[[Changes/Dify/2024-07-23-update-celery-beat-scheduler-time-to-env-by-johnjyong-in-https-github-com-langge|update
  celery beat scheduler time to env]]'
source_release: '[[Releases/AnythingLLM/anythingllm-2024-07-26-v1-0-0-github-167428396-523db21a|anythingllm-2024-07-26-v1-0-0-github-167428396-523db21a]]'
source_type: github_releases
theme: automation-scheduling
title: 'refactor: convert insert loop to 1 insert stmt'
type: change
---

<!-- chronolog:begin region="header" -->
# refactor: convert insert loop to 1 insert stmt

**AnythingLLM** · 2024-07-26 · [[Themes/automation-scheduling|Automation and Scheduling]] · [Official source](https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.0.0) · from [[Releases/AnythingLLM/anythingllm-2024-07-26-v1-0-0-github-167428396-523db21a|AnythingLLM v1.0.0 🎉]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> refactor: convert insert loop to 1 insert stmt by @jwaltz in https://github.com/Mintplex-Labs/anything-llm/pull/19
>
> Source: https://github.com/Mintplex-Labs/anything-llm/releases/tag/v1.0.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/AnythingLLM/2024-07-26-6-context-window-changes-in-v1-0-0|6 Context Window changes in v1.0.0]] · Context Window
- [[Changes/AnythingLLM/2024-07-26-47-model-support-changes-in-v1-0-0|47 Model Support changes in v1.0.0]] · Model Support
- [[Changes/AnythingLLM/2024-07-26-6-developer-workflow-changes-in-v1-0-0|6 Developer Workflow changes in v1.0.0]] · Developer Workflow
- [[Changes/AnythingLLM/2024-07-26-3-safety-and-privacy-changes-in-v1-0-0|3 Safety and Privacy changes in v1.0.0]] · Safety and Privacy
- [[Changes/AnythingLLM/2024-07-26-4-editor-experience-changes-in-v1-0-0|4 Editor Experience changes in v1.0.0]] · Editor Experience
- [[Changes/AnythingLLM/2024-07-26-4-mobile-and-desktop-changes-in-v1-0-0|4 Mobile and Desktop changes in v1.0.0]] · Mobile and Desktop
- [[Changes/AnythingLLM/2024-07-26-15-agent-mode-changes-in-v1-0-0|15 Agent Mode changes in v1.0.0]] · Agent Mode
- [[Changes/AnythingLLM/2024-07-26-2-accessibility-and-localization-changes-in-v1-0-0|2 Accessibility and Localization changes in v1.0.0]] · Accessibility and Localization
- [[Changes/AnythingLLM/2024-07-26-11-apps-and-integrations-changes-in-v1-0-0|11 Apps and Integrations changes in v1.0.0]] · Apps and Integrations
- [[Changes/AnythingLLM/2024-07-26-25-interface-experience-changes-in-v1-0-0|25 Interface Experience changes in v1.0.0]] · Interface Experience
- [[Changes/AnythingLLM/2024-07-26-3-voice-and-audio-changes-in-v1-0-0|3 Voice and Audio changes in v1.0.0]] · Voice and Audio
- [[Changes/AnythingLLM/2024-07-26-4-account-and-access-changes-in-v1-0-0|4 Account and Access changes in v1.0.0]] · Account and Access
- [[Changes/AnythingLLM/2024-07-26-feat-bing-search-api-web-search-provider-by-shatfield4-in-https-github-com-mintp|FEAT Bing Search API web search provider]] · Search and Browsing
- [[Changes/AnythingLLM/2024-07-26-23-files-and-data-changes-in-v1-0-0|23 Files and Data changes in v1.0.0]] · Files and Data
- [[Changes/AnythingLLM/2024-07-26-331-other-changes-in-v1-0-0|331 other changes in v1.0.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Automation and Scheduling

- Earlier: 2024-07-23 · Dify · [[Changes/Dify/2024-07-23-update-celery-beat-scheduler-time-to-env-by-johnjyong-in-https-github-com-langge|update celery beat scheduler time to env]]
- Later: 2024-08-08 · AnythingLLM · [[Changes/AnythingLLM/2024-08-08-2034-automate-port-forwarding-for-github-codespaces-using-gh-cli-by-mrsimonc-in|2034 automate port forwarding for GitHub codespaces using gh cli]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2019-09-18 · Descript · [[Changes/Descript/2019-09-18-change-gain-with-volume-automation|Change gain, with volume automation]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20anythingllm-2024-07-26-96e890&body=Card%3A%20Changes%2FAnythingLLM%2F2024-07-26-refactor-convert-insert-loop-to-1-insert-stmt-by-jwaltz-in-https-github-com-mint.md%0ACard%20ID%3A%20anythingllm-2024-07-26-96e890%0ASource%3A%20https%3A%2F%2Fgithub.com%2FMintplex-Labs%2Fanything-llm%2Freleases%2Ftag%2Fv1.0.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->