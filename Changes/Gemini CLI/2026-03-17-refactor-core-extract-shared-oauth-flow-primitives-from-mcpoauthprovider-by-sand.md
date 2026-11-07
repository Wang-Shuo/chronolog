---
card_id: gemini-cli-2026-03-17-16b32e
date: '2026-03-17'
description: 'Gemini CLI · 2026-03-17 · Account and Access: refactor(core): extract
  shared OAuth flow primitives from MCPOAuthProvider by @SandyTao520 in…'
diffusion:
  first_in_tracked: "[[Changes/Notion/2020-07-28-sign-into-notion-with-your-apple-id-the-perfect-combination-of-speedy-and-secure|Sign
    into Notion with your Apple ID \U0001F5DD️ The perfect combination of speedy and
    secure]]"
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2058
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: change
machine_hash: f0b9eea06b0c29c187c10fe948d4e1a87b8dbeafa77ab2707dc2054ae60fc23b
product: gemini-cli
product_name: Gemini CLI
record:
  card_id: gemini-cli-2026-03-17-16b32e
  comparison: ''
  date: '2026-03-17'
  description: 'Gemini CLI — Release v0.34.0: refactor(core): extract shared OAuth
    flow primitives from MCPOAuthProvider by @SandyTao520 in https://github.com/google-gemini/gemini-cli/pull/20895'
  evidence:
  - quote: 'refactor(core): extract shared OAuth flow primitives from MCPOAuthProvider
      by @SandyTao520 in https://github.com/google-gemini/gemini-cli/pull/20895'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.34.0
  extractor_version: fallback-v5
  impact: incremental
  kind: change
  product: gemini-cli
  product_name: Gemini CLI
  slug: refactor-core-extract-shared-oauth-flow-primitives-from-mcpoauthprovider-by-sand
  source_release: gemini-cli-2026-03-17-v0-34-0-github-298158994-68230a41
  source_type: github_releases
  theme: account-access
  title: 'refactor(core): extract shared OAuth flow primitives from MCPOAuthProvider'
  type: change
related_changes:
- '[[Changes/Ollama/2026-03-14-ollama-can-now-be-selected-as-an-authentication-and-model-provider-during-opencl|Ollama
  can now be selected as an authentication and model provider during OpenClaw…]]'
- '[[Changes/Codex CLI/2026-03-16-2-account-and-access-changes-in-rust-v0-115-0|2
  Account and Access changes in rust-v0.115.0]]'
- '[[Changes/Lovable/2026-03-16-authentication-emails|Authentication emails]]'
source_release: '[[Releases/Gemini CLI/gemini-cli-2026-03-17-v0-34-0-github-298158994-68230a41|gemini-cli-2026-03-17-v0-34-0-github-298158994-68230a41]]'
source_type: github_releases
theme: account-access
title: 'refactor(core): extract shared OAuth flow primitives from MCPOAuthProvider'
type: change
---

<!-- chronolog:begin region="header" -->
# refactor(core): extract shared OAuth flow primitives from MCPOAuthProvider

**Gemini CLI** · 2026-03-17 · [[Themes/account-access|Account and Access]] · [Official source](https://github.com/google-gemini/gemini-cli/releases/tag/v0.34.0) · from [[Releases/Gemini CLI/gemini-cli-2026-03-17-v0-34-0-github-298158994-68230a41|Release v0.34.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> refactor(core): extract shared OAuth flow primitives from MCPOAuthProvider by @SandyTao520 in https://github.com/google-gemini/gemini-cli/pull/20895
>
> Source: https://github.com/google-gemini/gemini-cli/releases/tag/v0.34.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Gemini CLI/2026-03-17-feat-voice-implement-speech-friendly-response-formatter-by-ayush31010-in-https-g|feat(voice): implement speech-friendly response formatter]] · Voice and Audio
- [[Changes/Gemini CLI/2026-03-17-2-pricing-model-changes-in-v0-34-0|2 Pricing Model changes in v0.34.0]] · Pricing Model
- [[Changes/Gemini CLI/2026-03-17-3-safety-and-privacy-changes-in-v0-34-0|3 Safety and Privacy changes in v0.34.0]] · Safety and Privacy
- [[Changes/Gemini CLI/2026-03-17-9-developer-workflow-changes-in-v0-34-0|9 Developer Workflow changes in v0.34.0]] · Developer Workflow
- [[Changes/Gemini CLI/2026-03-17-3-interface-experience-changes-in-v0-34-0|3 Interface Experience changes in v0.34.0]] · Interface Experience
- [[Changes/Gemini CLI/2026-03-17-4-apps-and-integrations-changes-in-v0-34-0|4 Apps and Integrations changes in v0.34.0]] · Apps and Integrations
- [[Changes/Gemini CLI/2026-03-17-docs-add-documentation-for-notifications-experimental-macos-by-jkcinouye-in-http|Docs: Add documentation for notifications (experimental)(macOS)]] · Mobile and Desktop
- [[Changes/Gemini CLI/2026-03-17-docs-document-tool-exclusion-from-memory-via-deny-policy-by-abhijit-2592-in-http|docs: document tool exclusion from memory via deny policy]] · Memory and Personalization
- [[Changes/Gemini CLI/2026-03-17-docs-document-planning-workflows-with-conductor-example-by-jerop-in-https-github|docs: document planning workflows with Conductor example]] · Files and Data
- [[Changes/Gemini CLI/2026-03-17-7-agent-mode-changes-in-v0-34-0|7 Agent Mode changes in v0.34.0]] · Agent Mode
- [[Changes/Gemini CLI/2026-03-17-feat-core-improve-file-autocomplete-to-prioritize-filenames-by-sehoon38-in-https|feat(core): improve @file autocomplete to prioritize filenames]] · Editor Experience
- [[Changes/Gemini CLI/2026-03-17-2-automation-and-scheduling-changes-in-v0-34-0|2 Automation and Scheduling changes in v0.34.0]] · Automation and Scheduling
- [[Changes/Gemini CLI/2026-03-17-5-model-support-changes-in-v0-34-0|5 Model Support changes in v0.34.0]] · Model Support
- [[Changes/Gemini CLI/2026-03-17-78-other-changes-in-v0-34-0|78 other changes in v0.34.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2026-03-16 · Lovable · [[Changes/Lovable/2026-03-16-authentication-emails|Authentication emails]]
- Later: 2026-03-18 · Claude Code · [[Changes/Claude Code/2026-03-18-added-console-flag-to-claude-auth-login-for-anthropic-console-api-billing-authen|Added --console flag to claude auth login for Anthropic Console (API billing)…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Notion · [[Changes/Notion/2020-07-28-sign-into-notion-with-your-apple-id-the-perfect-combination-of-speedy-and-secure|Sign into Notion with your Apple ID 🗝️ The perfect combination of speedy and secure]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20gemini-cli-2026-03-17-16b32e&body=Card%3A%20Changes%2FGemini%20CLI%2F2026-03-17-refactor-core-extract-shared-oauth-flow-primitives-from-mcpoauthprovider-by-sand.md%0ACard%20ID%3A%20gemini-cli-2026-03-17-16b32e%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgoogle-gemini%2Fgemini-cli%2Freleases%2Ftag%2Fv0.34.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->