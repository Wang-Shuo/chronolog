---
card_id: dify-2026-02-03-539694
date: '2026-02-03'
description: 'Dify · 2026-02-03 · Safety and Privacy: 9 changes in v1.12.0 - Introducing
  Summary Index: Smarter Retrieval with AI Summarization — **Security:**'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1024
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 195dc8728b9ec9fa9255e063e8ca5916fcad140dfcd73dc8c231a5334cfec597
product: dify
product_name: Dify
record:
  card_id: dify-2026-02-03-539694
  comparison: ''
  date: '2026-02-03'
  description: 'Dify — v1.12.0 - Introducing Summary Index: Smarter Retrieval with
    AI Summarization: 9 Safety and Privacy changes'
  evidence:
  - quote: '**Security:**'
    source_release: https://github.com/langgenius/dify/releases/tag/1.12.0
  - quote: 'Logstore security fix: Addressed potential SQL injection, serialization
      issues, and optimized initialization.'
    source_release: https://github.com/langgenius/dify/releases/tag/1.12.0
  - quote: Fixed an SSRF vulnerability in WordExtractor URL download.
    source_release: https://github.com/langgenius/dify/releases/tag/1.12.0
  - quote: Upgraded `tanstack devtools` to fix seroval RCE vulnerability.
    source_release: https://github.com/langgenius/dify/releases/tag/1.12.0
  - quote: Security updates for `pdfminer.six`, `authlib`, `werkzeug`, `aiohttp`,
      and `pycryptodome`.
    source_release: https://github.com/langgenius/dify/releases/tag/1.12.0
  - quote: '`SANDBOX_EXPIRED_RECORDS_CLEAN_TASK_LOCK_TTL`: Sets the lock TTL for the
      sandbox expired records cleanup task (Default: `90000`).'
    source_release: https://github.com/langgenius/dify/releases/tag/1.12.0
  - quote: 'feat: ee workspace permission control by @douxc in https://github.com/langgenius/dify/pull/30841'
    source_release: https://github.com/langgenius/dify/releases/tag/1.12.0
  - quote: 'feat: implement workspace permission checks for member invitations an…
      by @GareArc in https://github.com/langgenius/dify/pull/31202'
    source_release: https://github.com/langgenius/dify/releases/tag/1.12.0
  - quote: 'fix(web): upgrade tanstack devtools to fix seroval RCE vulnerability by
      @lyzno1 in https://github.com/langgenius/dify/pull/31515'
    source_release: https://github.com/langgenius/dify/releases/tag/1.12.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 9-safety-and-privacy-changes-in-1-12-0
  source_release: dify-2026-02-03-1-12-0-github-282591953-290f70e4
  source_type: github_releases
  theme: safety-privacy
  title: 9 Safety and Privacy changes in 1.12.0
  type: change
related_changes:
- '[[Changes/ElevenLabs/2026-02-02-workspaces|Workspaces]]'
- '[[Changes/OpenHands/2026-02-02-2-safety-and-privacy-changes-in-1-3-0|2 Safety and
  Privacy changes in 1.3.0]]'
- '[[Changes/Claude Code/2026-02-03-fixed-permission-dialogs-stealing-focus-while-actively-typing|Fixed
  permission dialogs stealing focus while actively typing]]'
source_release: '[[Releases/Dify/dify-2026-02-03-1-12-0-github-282591953-290f70e4|dify-2026-02-03-1-12-0-github-282591953-290f70e4]]'
source_type: github_releases
theme: safety-privacy
title: 9 Safety and Privacy changes in 1.12.0
type: change
---

<!-- chronolog:begin region="header" -->
# 9 Safety and Privacy changes in 1.12.0

**Dify** · 2026-02-03 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.12.0) · from [[Releases/Dify/dify-2026-02-03-1-12-0-github-282591953-290f70e4|v1.12.0 - Introducing Summary Index: Smarter Retrieval with AI Summarization]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> **Security:**

> Logstore security fix: Addressed potential SQL injection, serialization issues, and optimized initialization.

> Fixed an SSRF vulnerability in WordExtractor URL download.

> Upgraded `tanstack devtools` to fix seroval RCE vulnerability.

> Security updates for `pdfminer.six`, `authlib`, `werkzeug`, `aiohttp`, and `pycryptodome`.

> `SANDBOX_EXPIRED_RECORDS_CLEAN_TASK_LOCK_TTL`: Sets the lock TTL for the sandbox expired records cleanup task (Default: `90000`).

> feat: ee workspace permission control by @douxc in https://github.com/langgenius/dify/pull/30841

> feat: implement workspace permission checks for member invitations an… by @GareArc in https://github.com/langgenius/dify/pull/31202

> fix(web): upgrade tanstack devtools to fix seroval RCE vulnerability by @lyzno1 in https://github.com/langgenius/dify/pull/31515

Source: https://github.com/langgenius/dify/releases/tag/1.12.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2026-02-03-2-developer-workflow-changes-in-1-12-0|2 Developer Workflow changes in 1.12.0]] · Developer Workflow
- [[Changes/Dify/2026-02-03-chore-hide-disable-try-tab-when-not-support-by-iamjoel-in-https-github-com-langg|chore: hide disable try tab when not support]] · Editor Experience
- [[Changes/Dify/2026-02-03-chore-improve-accessibility-for-learn-more-link-by-khmandarrin-in-https-github-c|chore: improve accessibility for learn more link]] · Accessibility and Localization
- [[Changes/Dify/2026-02-03-5-context-window-changes-in-1-12-0|5 Context Window changes in 1.12.0]] · Context Window
- [[Changes/Dify/2026-02-03-5-model-support-changes-in-1-12-0|5 Model Support changes in 1.12.0]] · Model Support
- [[Changes/Dify/2026-02-03-7-files-and-data-changes-in-1-12-0|7 Files and Data changes in 1.12.0]] · Files and Data
- [[Changes/Dify/2026-02-03-9-agent-mode-changes-in-1-12-0|9 Agent Mode changes in 1.12.0]] · Agent Mode
- [[Changes/Dify/2026-02-03-3-multimodal-input-changes-in-1-12-0|3 Multimodal Input changes in 1.12.0]] · Multimodal Input
- [[Changes/Dify/2026-02-03-test-enhance-hittestingpage-tests-with-additional-coverage-for-rendering-and-sta|test: enhance HitTestingPage tests with additional coverage for rendering and state…]] · Interface Experience
- [[Changes/Dify/2026-02-03-2-enterprise-and-administration-changes-in-1-12-0|2 Enterprise and Administration changes in 1.12.0]] · Enterprise and Administration
- [[Changes/Dify/2026-02-03-feat-use-xdist-to-make-make-test-faster-by-yihong0618-in-https-github-com-langge|feat: use xdist to make make test faster]] · Reliability and Performance
- [[Changes/Dify/2026-02-03-refactor-contract-restructure-console-contracts-with-nested-billing-module-by-ly|refactor(contract): restructure console contracts with nested billing module]] · Pricing Model
- [[Changes/Dify/2026-02-03-3-account-and-access-changes-in-1-12-0|3 Account and Access changes in 1.12.0]] · Account and Access
- [[Changes/Dify/2026-02-03-14-apps-and-integrations-changes-in-1-12-0|14 Apps and Integrations changes in 1.12.0]] · Apps and Integrations
- [[Changes/Dify/2026-02-03-149-other-changes-in-1-12-0|149 other changes in 1.12.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-02-03 · Claude Code · [[Changes/Claude Code/2026-02-03-fixed-permission-dialogs-stealing-focus-while-actively-typing|Fixed permission dialogs stealing focus while actively typing]]
- Later: 2026-02-04 · Codex CLI · [[Changes/Codex CLI/2026-02-04-6-safety-and-privacy-changes-in-rust-v0-95-0|6 Safety and Privacy changes in rust-v0.95.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-02-03-539694&body=Card%3A%20Changes%2FDify%2F2026-02-03-9-safety-and-privacy-changes-in-1-12-0.md%0ACard%20ID%3A%20dify-2026-02-03-539694%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.12.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->