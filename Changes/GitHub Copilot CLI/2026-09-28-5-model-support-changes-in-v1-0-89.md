---
card_id: github-copilot-cli-2026-09-28-dba3ef
date: '2026-09-28'
description: 'GitHub Copilot CLI · 2026-09-28 · Model Support: 5 changes in 1.0.89
  — Auto shows a quick feedback prompt after switching away to a manually selected
  model'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1358
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: f8dc8d0f929837b3e1b10622627a02ec45c5e381eafaa49b810dd390a1ef405b
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-09-28-dba3ef
  comparison: ''
  date: '2026-09-28'
  description: 'GitHub Copilot CLI — 1.0.89: 5 Model Support changes'
  evidence:
  - quote: Auto shows a quick feedback prompt after switching away to a manually selected
      model
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.89
  - quote: In local sessions, Esc Esc in an empty chat input takes back a prompt whose
      turn the model has not started answering and removes it from the conversation
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.89
  - quote: Add GPT-6 Sol and GPT-6 Luna to the model picker when available
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.89
  - quote: Adding support for claude-opus-5.5
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.89
  - quote: Gemini models no longer fail every request with 400 invalid request body
      when an MCP server exposes a tool whose schema puts a type or properties beside
      anyOf, such as a nullable discriminated union
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.89
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 5-model-support-changes-in-v1-0-89
  source_release: github-copilot-cli-2026-09-28-v1-0-89-github-398551718-87b48178
  source_type: github_releases
  theme: model-support
  title: 5 Model Support changes in v1.0.89
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-09-28-7-model-support-changes-in-rust-v0-158-0|7 Model
  Support changes in rust-v0.158.0]]'
- '[[Changes/ElevenLabs/2026-09-28-elevenagents-4d99c8|ElevenAgents]]'
- '[[Changes/ElevenLabs/2026-09-28-models|Models]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-09-28-v1-0-89-github-398551718-87b48178|github-copilot-cli-2026-09-28-v1-0-89-github-398551718-87b48178]]'
source_type: github_releases
theme: model-support
title: 5 Model Support changes in v1.0.89
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Model Support changes in v1.0.89

**GitHub Copilot CLI** · 2026-09-28 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.89) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-09-28-v1-0-89-github-398551718-87b48178|1.0.89]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Auto shows a quick feedback prompt after switching away to a manually selected model

> In local sessions, Esc Esc in an empty chat input takes back a prompt whose turn the model has not started answering and removes it from the conversation

> Add GPT-6 Sol and GPT-6 Luna to the model picker when available

> Adding support for claude-opus-5.5

> Gemini models no longer fail every request with 400 invalid request body when an MCP server exposes a tool whose schema puts a type or properties beside anyOf, such as a nullable discriminated union

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.89
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-09-28-2-account-and-access-changes-in-v1-0-89|2 Account and Access changes in v1.0.89]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-09-28-2-safety-and-privacy-changes-in-v1-0-89|2 Safety and Privacy changes in v1.0.89]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-09-28-4-interface-experience-changes-in-v1-0-89|4 Interface Experience changes in v1.0.89]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-09-28-3-developer-workflow-changes-in-v1-0-89|3 Developer Workflow changes in v1.0.89]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-09-28-4-apps-and-integrations-changes-in-v1-0-89|4 Apps and Integrations changes in v1.0.89]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-09-28-queue-exit-commands-while-an-agent-response-is-still-running|Queue exit commands while an agent response is still running]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-09-28-shell-output-no-longer-shows-trailing-command-completion-metadata|Shell output no longer shows trailing command completion metadata]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-09-28-add-support-for-claude-code-rule-files-in-claude-rules-as-custom-instructions|Add support for Claude Code rule files in .claude/rules as custom instructions]] · Memory and Personalization
- [[Changes/GitHub Copilot CLI/2026-09-28-10-other-changes-in-v1-0-89|10 other changes in v1.0.89]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-09-28 · ElevenLabs · [[Changes/ElevenLabs/2026-09-28-models|Models]]
- Later: 2026-09-28 · Ollama · [[Changes/Ollama/2026-09-28-3-model-support-changes-in-v0-35-0|3 Model Support changes in v0.35.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-09-28-dba3ef&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-09-28-5-model-support-changes-in-v1-0-89.md%0ACard%20ID%3A%20github-copilot-cli-2026-09-28-dba3ef%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.89%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->