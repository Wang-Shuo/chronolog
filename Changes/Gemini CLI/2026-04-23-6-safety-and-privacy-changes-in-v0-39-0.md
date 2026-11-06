---
card_id: gemini-cli-2026-04-23-3f8e6c
date: '2026-04-23'
description: 'Gemini CLI · 2026-04-23 · Safety and Privacy: 6 changes in Release v0.39.0
  — refactor(sandbox): use centralized sandbox paths in macOS Seatbelt implementation…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1103
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 960f5efe51bca210a23a03c5f43695ef3be7822f31232cfaac9aad2878145375
product: gemini-cli
product_name: Gemini CLI
record:
  card_id: gemini-cli-2026-04-23-3f8e6c
  comparison: ''
  date: '2026-04-23'
  description: 'Gemini CLI — Release v0.39.0: 6 Safety and Privacy changes'
  evidence:
  - quote: 'refactor(sandbox): use centralized sandbox paths in macOS Seatbelt implementation
      by @ehedlund in https://github.com/google-gemini/gemini-cli/pull/24984'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.39.0
  - quote: 'refactor(core): use centralized path resolution for Linux sandbox by @ehedlund
      in https://github.com/google-gemini/gemini-cli/pull/24985'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.39.0
  - quote: 'docs: add vi shortcuts and clarify MCP sandbox setup by @chrisjcthomas
      in https://github.com/google-gemini/gemini-cli/pull/21679'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.39.0
  - quote: 'perf(sandbox): optimize Windows sandbox initialization via native ACL
      application by @ehedlund in https://github.com/google-gemini/gemini-cli/pull/25077'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.39.0
  - quote: 'refactor(core): extract and centralize sandbox path utilities by @ehedlund
      in https://github.com/google-gemini/gemini-cli/pull/25305'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.39.0
  - quote: 'test(core): improve sandbox integration test coverage and fix OS-specific
      failures by @ehedlund in https://github.com/google-gemini/gemini-cli/pull/25307'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.39.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: gemini-cli
  product_name: Gemini CLI
  slug: 6-safety-and-privacy-changes-in-v0-39-0
  source_release: gemini-cli-2026-04-23-v0-39-0-github-312542426-bb57739c
  source_type: github_releases
  theme: safety-privacy
  title: 6 Safety and Privacy changes in v0.39.0
  type: change
related_changes:
- '[[Changes/Claude Code/2026-04-23-4-safety-and-privacy-changes-in-v2-1-119|4 Safety
  and Privacy changes in v2.1.119]]'
- '[[Changes/Codex CLI/2026-04-23-17-safety-and-privacy-changes-in-rust-v0-124-0|17
  Safety and Privacy changes in rust-v0.124.0]]'
- '[[Changes/Codex CLI/2026-04-23-6-safety-and-privacy-changes-in-rust-v0-123-0|6
  Safety and Privacy changes in rust-v0.123.0]]'
source_release: '[[Releases/Gemini CLI/gemini-cli-2026-04-23-v0-39-0-github-312542426-bb57739c|gemini-cli-2026-04-23-v0-39-0-github-312542426-bb57739c]]'
source_type: github_releases
theme: safety-privacy
title: 6 Safety and Privacy changes in v0.39.0
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Safety and Privacy changes in v0.39.0

**Gemini CLI** · 2026-04-23 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/google-gemini/gemini-cli/releases/tag/v0.39.0) · from [[Releases/Gemini CLI/gemini-cli-2026-04-23-v0-39-0-github-312542426-bb57739c|Release v0.39.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> refactor(sandbox): use centralized sandbox paths in macOS Seatbelt implementation by @ehedlund in https://github.com/google-gemini/gemini-cli/pull/24984

> refactor(core): use centralized path resolution for Linux sandbox by @ehedlund in https://github.com/google-gemini/gemini-cli/pull/24985

> docs: add vi shortcuts and clarify MCP sandbox setup by @chrisjcthomas in https://github.com/google-gemini/gemini-cli/pull/21679

> perf(sandbox): optimize Windows sandbox initialization via native ACL application by @ehedlund in https://github.com/google-gemini/gemini-cli/pull/25077

> refactor(core): extract and centralize sandbox path utilities by @ehedlund in https://github.com/google-gemini/gemini-cli/pull/25305

> test(core): improve sandbox integration test coverage and fix OS-specific failures by @ehedlund in https://github.com/google-gemini/gemini-cli/pull/25307

Source: https://github.com/google-gemini/gemini-cli/releases/tag/v0.39.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Gemini CLI/2026-04-23-feat-cli-extract-quotacontext-and-resolve-infinite-render-loop-by-adib234-in-htt|feat(cli): extract QuotaContext and resolve infinite render loop]] · Automation and Scheduling
- [[Changes/Gemini CLI/2026-04-23-3-developer-workflow-changes-in-v0-39-0|3 Developer Workflow changes in v0.39.0]] · Developer Workflow
- [[Changes/Gemini CLI/2026-04-23-6-agent-mode-changes-in-v0-39-0|6 Agent Mode changes in v0.39.0]] · Agent Mode
- [[Changes/Gemini CLI/2026-04-23-2-model-support-changes-in-v0-39-0|2 Model Support changes in v0.39.0]] · Model Support
- [[Changes/Gemini CLI/2026-04-23-2-reliability-and-performance-changes-in-v0-39-0|2 Reliability and Performance changes in v0.39.0]] · Reliability and Performance
- [[Changes/Gemini CLI/2026-04-23-4-apps-and-integrations-changes-in-v0-39-0|4 Apps and Integrations changes in v0.39.0]] · Apps and Integrations
- [[Changes/Gemini CLI/2026-04-23-use-macos-latest-large-runner-where-applicable-by-scidomino-in-https-github-com|use macos-latest-large runner where applicable]] · Mobile and Desktop
- [[Changes/Gemini CLI/2026-04-23-docs-correct-documentation-for-enforced-authentication-type-by-cocosheng-g-in-ht|docs: correct documentation for enforced authentication type]] · Account and Access
- [[Changes/Gemini CLI/2026-04-23-4-memory-and-personalization-changes-in-v0-39-0|4 Memory and Personalization changes in v0.39.0]] · Memory and Personalization
- [[Changes/Gemini CLI/2026-04-23-stop-showing-scrollbar-unless-we-are-in-terminalbuffer-mode-by-jacob314-in-https|Stop showing scrollbar unless we are in terminalBuffer mode]] · Interface Experience
- [[Changes/Gemini CLI/2026-04-23-chore-core-increase-codebase-investigator-turn-limits-to-50-by-abhipatel12-in-ht|chore(core): increase codebase investigator turn limits to 50]] · Editor Experience
- [[Changes/Gemini CLI/2026-04-23-30-other-changes-in-v0-39-0|30 other changes in v0.39.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-04-23 · Codex CLI · [[Changes/Codex CLI/2026-04-23-6-safety-and-privacy-changes-in-rust-v0-123-0|6 Safety and Privacy changes in rust-v0.123.0]]
- Later: 2026-04-23 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-04-23-permission-prompts-appear-correctly-in-remote-sessions-for-the-cli-tui|Permission prompts appear correctly in remote sessions for the CLI TUI]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20gemini-cli-2026-04-23-3f8e6c&body=Card%3A%20Changes%2FGemini%20CLI%2F2026-04-23-6-safety-and-privacy-changes-in-v0-39-0.md%0ACard%20ID%3A%20gemini-cli-2026-04-23-3f8e6c%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgoogle-gemini%2Fgemini-cli%2Freleases%2Ftag%2Fv0.39.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->