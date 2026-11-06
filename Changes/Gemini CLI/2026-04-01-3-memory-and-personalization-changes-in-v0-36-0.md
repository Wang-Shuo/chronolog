---
card_id: gemini-cli-2026-04-01-08b3e4
date: '2026-04-01'
description: 'Gemini CLI · 2026-04-01 · Memory and Personalization: 3 changes in Release
  v0.36.0 — feat(core): inject memory and JIT context into subagents by @abhipatel12…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom
    instructions are rolling out in beta]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 986
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: memory
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: cfe46c550a1580498b38362d8f8f183ea1090a7eb1c5b6aaab5051ed08a142d1
product: gemini-cli
product_name: Gemini CLI
record:
  card_id: gemini-cli-2026-04-01-08b3e4
  comparison: ''
  date: '2026-04-01'
  description: 'Gemini CLI — Release v0.36.0: 3 Memory and Personalization changes'
  evidence:
  - quote: 'feat(core): inject memory and JIT context into subagents by @abhipatel12
      in https://github.com/google-gemini/gemini-cli/pull/23032'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.36.0
  - quote: 'feat(core): add experimental memory manager agent to replace save_memory
      tool by @SandyTao520 in https://github.com/google-gemini/gemini-cli/pull/22726'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.36.0
  - quote: 'eval(save_memory): add multi-turn interactive evals for memoryManager
      by @SandyTao520 in https://github.com/google-gemini/gemini-cli/pull/23572'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.36.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: gemini-cli
  product_name: Gemini CLI
  slug: 3-memory-and-personalization-changes-in-v0-36-0
  source_release: gemini-cli-2026-04-01-v0-36-0-github-304395807-bc719eb1
  source_type: github_releases
  theme: memory
  title: 3 Memory and Personalization changes in v0.36.0
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-03-26-15175-chore-morpheus-does-not-generate-memories-jif-oai|♯15175
  chore: morpheus does not generate memories @jif-oai]]'
- '[[Changes/Gemini/2026-03-26-make-the-switch-seamlessly-bring-your-ai-memories-and-chat-history-to-gemini|Make
  the switch: Seamlessly bring your AI memories and chat history to Gemini]]'
- '[[Changes/Claude Code/2026-03-27-memory-filenames-in-the-saved-n-memories-notice-now-highlight-on-hover-and-open|Memory
  filenames in the "Saved N memories" notice now highlight on hover and open on click]]'
source_release: '[[Releases/Gemini CLI/gemini-cli-2026-04-01-v0-36-0-github-304395807-bc719eb1|gemini-cli-2026-04-01-v0-36-0-github-304395807-bc719eb1]]'
source_type: github_releases
theme: memory
title: 3 Memory and Personalization changes in v0.36.0
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Memory and Personalization changes in v0.36.0

**Gemini CLI** · 2026-04-01 · [[Themes/memory|Memory and Personalization]] · Digest · [Official source](https://github.com/google-gemini/gemini-cli/releases/tag/v0.36.0) · from [[Releases/Gemini CLI/gemini-cli-2026-04-01-v0-36-0-github-304395807-bc719eb1|Release v0.36.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> feat(core): inject memory and JIT context into subagents by @abhipatel12 in https://github.com/google-gemini/gemini-cli/pull/23032

> feat(core): add experimental memory manager agent to replace save_memory tool by @SandyTao520 in https://github.com/google-gemini/gemini-cli/pull/22726

> eval(save_memory): add multi-turn interactive evals for memoryManager by @SandyTao520 in https://github.com/google-gemini/gemini-cli/pull/23572

Source: https://github.com/google-gemini/gemini-cli/releases/tag/v0.36.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Gemini CLI/2026-04-01-7-safety-and-privacy-changes-in-v0-36-0|7 Safety and Privacy changes in v0.36.0]] · Safety and Privacy
- [[Changes/Gemini CLI/2026-04-01-feat-core-implement-strict-macos-sandboxing-using-seatbelt-allowlist-by-ehedlund|feat(core): implement strict macOS sandboxing using Seatbelt allowlist]] · Mobile and Desktop
- [[Changes/Gemini CLI/2026-04-01-7-model-support-changes-in-v0-36-0|7 Model Support changes in v0.36.0]] · Model Support
- [[Changes/Gemini CLI/2026-04-01-test-core-migrate-hook-tests-to-scheduler-by-abhipatel12-in-https-github-com-goo|test(core): migrate hook tests to scheduler]] · Automation and Scheduling
- [[Changes/Gemini CLI/2026-04-01-feat-core-cap-jit-context-upward-traversal-at-git-root-by-sandytao520-in-https-g|feat(core): cap JIT context upward traversal at git root]] · Context Window
- [[Changes/Gemini CLI/2026-04-01-5-apps-and-integrations-changes-in-v0-36-0|5 Apps and Integrations changes in v0.36.0]] · Apps and Integrations
- [[Changes/Gemini CLI/2026-04-01-10-agent-mode-changes-in-v0-36-0|10 Agent Mode changes in v0.36.0]] · Agent Mode
- [[Changes/Gemini CLI/2026-04-01-refactor-ide-replace-dynamic-undici-import-with-static-fetch-import-by-cocosheng|refactor(ide): replace dynamic undici import with static fetch import]] · Editor Experience
- [[Changes/Gemini CLI/2026-04-01-2-interface-experience-changes-in-v0-36-0|2 Interface Experience changes in v0.36.0]] · Interface Experience
- [[Changes/Gemini CLI/2026-04-01-feat-core-change-user-facing-auth-type-from-oauth2-to-oauth-by-adamfweidman-in-h|feat(core): change user-facing auth type from oauth2 to oauth]] · Account and Access
- [[Changes/Gemini CLI/2026-04-01-3-developer-workflow-changes-in-v0-36-0|3 Developer Workflow changes in v0.36.0]] · Developer Workflow
- [[Changes/Gemini CLI/2026-04-01-perf-cli-background-ide-client-to-speed-up-initialization-by-sehoon38-in-https-g|perf(cli): background IDE client to speed up initialization]] · Reliability and Performance
- [[Changes/Gemini CLI/2026-04-01-53-other-changes-in-v0-36-0|53 other changes in v0.36.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Memory and Personalization

- Earlier: 2026-03-27 · Claude Code · [[Changes/Claude Code/2026-03-27-memory-filenames-in-the-saved-n-memories-notice-now-highlight-on-hover-and-open|Memory filenames in the "Saved N memories" notice now highlight on hover and open on click]]
- Later: 2026-04-08 · Gemini CLI · [[Changes/Gemini CLI/2026-04-08-2-memory-and-personalization-changes-in-v0-37-0|2 Memory and Personalization changes in v0.37.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-20 · ChatGPT · [[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom instructions are rolling out in beta]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20gemini-cli-2026-04-01-08b3e4&body=Card%3A%20Changes%2FGemini%20CLI%2F2026-04-01-3-memory-and-personalization-changes-in-v0-36-0.md%0ACard%20ID%3A%20gemini-cli-2026-04-01-08b3e4%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgoogle-gemini%2Fgemini-cli%2Freleases%2Ftag%2Fv0.36.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->