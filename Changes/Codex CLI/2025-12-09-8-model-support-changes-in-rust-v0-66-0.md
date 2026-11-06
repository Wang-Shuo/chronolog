---
card_id: codex-cli-2025-12-09-882a78
date: '2025-12-09'
description: 'Codex CLI · 2025-12-09 · Model Support: 8 changes in 0.66.0 — #7571
  remove model_family from `config @aibrahim-oai'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1065
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: efcee41b083796f417bbaaa99e749613cf3c05981df553283964b8905a9bb914
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2025-12-09-882a78
  comparison: ''
  date: '2025-12-09'
  description: 'Codex CLI — 0.66.0: 8 Model Support changes'
  evidence:
  - quote: '#7571 remove model_family from `config @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.66.0
  - quote: '#7603 Add models endpoint @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.66.0
  - quote: '#7616 Call models endpoint in models manager @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.66.0
  - quote: '#7621 Wire with_remote_overrides to construct model families @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.66.0
  - quote: '#7648 Add remote models feature flag @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.66.0
  - quote: '#7705 fix: update URLs to use HTTPS in model migration prompts @rakleed'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.66.0
  - quote: '#7722 load models from disk and set a ttl and etag @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.66.0
  - quote: '#7756 use chatgpt provider for /models @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.66.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 8-model-support-changes-in-rust-v0-66-0
  source_release: codex-cli-2025-12-09-rust-v0-66-0-github-268559734-698ec8f9
  source_type: github_releases
  theme: model-support
  title: 8 Model Support changes in rust-v0.66.0
  type: change
related_changes:
- '[[Changes/Windsurf/2025-12-04-1-12-39-gpt-5-1-codex-max-changelog-banner|1.12.39
  GPT-5.1 Codex Max changelog banner]]'
- '[[Changes/Windsurf/2025-12-04-gpt-5-1-codex-max|GPT-5.1-Codex Max]]'
- '[[Changes/GitHub Copilot CLI/2025-12-05-gpt-5-1-codex-max-is-now-available-in-github-copilot-cli|GPT-5.1-Codex-Max
  is now available in GitHub Copilot CLI]]'
source_release: '[[Releases/Codex CLI/codex-cli-2025-12-09-rust-v0-66-0-github-268559734-698ec8f9|codex-cli-2025-12-09-rust-v0-66-0-github-268559734-698ec8f9]]'
source_type: github_releases
theme: model-support
title: 8 Model Support changes in rust-v0.66.0
type: change
---

<!-- chronolog:begin region="header" -->
# 8 Model Support changes in rust-v0.66.0

**Codex CLI** · 2025-12-09 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.66.0) · from [[Releases/Codex CLI/codex-cli-2025-12-09-rust-v0-66-0-github-268559734-698ec8f9|0.66.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> #7571 remove model_family from `config @aibrahim-oai

> #7603 Add models endpoint @aibrahim-oai

> #7616 Call models endpoint in models manager @aibrahim-oai

> #7621 Wire with_remote_overrides to construct model families @aibrahim-oai

> #7648 Add remote models feature flag @aibrahim-oai

> #7705 fix: update URLs to use HTTPS in model migration prompts @rakleed

> #7722 load models from disk and set a ttl and etag @aibrahim-oai

> #7756 use chatgpt provider for /models @aibrahim-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.66.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2025-12-09-3-apps-and-integrations-changes-in-rust-v0-66-0|3 Apps and Integrations changes in rust-v0.66.0]] · Apps and Integrations
- [[Changes/Codex CLI/2025-12-09-2-account-and-access-changes-in-rust-v0-66-0|2 Account and Access changes in rust-v0.66.0]] · Account and Access
- [[Changes/Codex CLI/2025-12-09-3-editor-experience-changes-in-rust-v0-66-0|3 Editor Experience changes in rust-v0.66.0]] · Editor Experience
- [[Changes/Codex CLI/2025-12-09-2-interface-experience-changes-in-rust-v0-66-0|2 Interface Experience changes in rust-v0.66.0]] · Interface Experience
- [[Changes/Codex CLI/2025-12-09-7729-feat-add-is-mutating-detection-for-shell-command-handler-jif-oai|♯7729 feat: add is-mutating detection for shell command handler @jif-oai]] · Agent Mode
- [[Changes/Codex CLI/2025-12-09-7547-use-shared-check-sandboxing-pakrym-oai|♯7547 Use shared check sandboxing @pakrym-oai]] · Collaboration
- [[Changes/Codex CLI/2025-12-09-3-safety-and-privacy-changes-in-rust-v0-66-0|3 Safety and Privacy changes in rust-v0.66.0]] · Safety and Privacy
- [[Changes/Codex CLI/2025-12-09-2-developer-workflow-changes-in-rust-v0-66-0|2 Developer Workflow changes in rust-v0.66.0]] · Developer Workflow
- [[Changes/Codex CLI/2025-12-09-general-fixes-parallel-tool-call-chat-now-returns-correctly-ghost-snapshot-token|General fixes: parallel tool-call chat now returns correctly, ghost snapshot tokens…]] · Context Window
- [[Changes/Codex CLI/2025-12-09-4-mobile-and-desktop-changes-in-rust-v0-66-0|4 Mobile and Desktop changes in rust-v0.66.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2025-12-09-52-other-changes-in-rust-v0-66-0|52 other changes in rust-v0.66.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2025-12-05 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2025-12-05-gpt-5-1-codex-max-is-now-available-in-github-copilot-cli|GPT-5.1-Codex-Max is now available in GitHub Copilot CLI]]
- Later: 2025-12-09 · Gemini CLI · [[Changes/Gemini CLI/2025-12-09-7-model-support-changes-in-v0-20-0|7 Model Support changes in v0.20.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2025-12-09-882a78&body=Card%3A%20Changes%2FCodex%20CLI%2F2025-12-09-8-model-support-changes-in-rust-v0-66-0.md%0ACard%20ID%3A%20codex-cli-2025-12-09-882a78%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.66.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->