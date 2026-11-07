---
card_id: codex-cli-2026-02-26-28133d
date: '2026-02-26'
description: 'Codex CLI · 2026-02-26 · Agent Mode: 5 changes in 0.106.0 — Reduced
  sub-agent startup overhead by skipping expensive history metadata scans for subagent
  spawns…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 966
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 98c51dba87ad94cbe33735491817c5a9f447b5abb37b0c0c15c3eaf96c4b3e68
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-02-26-28133d
  comparison: ''
  date: '2026-02-26'
  description: 'Codex CLI — 0.106.0: 5 Agent Mode changes'
  evidence:
  - quote: Reduced sub-agent startup overhead by skipping expensive history metadata
      scans for subagent spawns (#12918)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.106.0
  - quote: '#12721 Revert "Ensure shell command skills trigger approval (#12697)"
      @celia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.106.0
  - quote: '#12884 chore: new agents name @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.106.0
  - quote: '#12918 Skip history metadata scan for subagents @daveaitel-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.106.0
  - quote: '#12911 fix: ctrl c sub agent @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.106.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 5-agent-mode-changes-in-rust-v0-106-0
  source_release: codex-cli-2026-02-26-rust-v0-106-0-github-291146451-379358db
  source_type: github_releases
  theme: agent-mode
  title: 5 Agent Mode changes in rust-v0.106.0
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-02-25-18-agent-mode-changes-in-rust-v0-105-0|18 Agent
  Mode changes in rust-v0.105.0]]'
- '[[Changes/Gemini CLI/2026-02-25-4-agent-mode-changes-in-v0-30-0|4 Agent Mode changes
  in v0.30.0]]'
- '[[Changes/GitHub Copilot CLI/2026-02-25-agent-protected-from-accidentally-killing-itself|Agent
  protected from accidentally killing itself]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-02-26-rust-v0-106-0-github-291146451-379358db|codex-cli-2026-02-26-rust-v0-106-0-github-291146451-379358db]]'
source_type: github_releases
theme: agent-mode
title: 5 Agent Mode changes in rust-v0.106.0
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Agent Mode changes in rust-v0.106.0

**Codex CLI** · 2026-02-26 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.106.0) · from [[Releases/Codex CLI/codex-cli-2026-02-26-rust-v0-106-0-github-291146451-379358db|0.106.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Reduced sub-agent startup overhead by skipping expensive history metadata scans for subagent spawns (#12918)

> #12721 Revert "Ensure shell command skills trigger approval (#12697)" @celia-oai

> #12884 chore: new agents name @jif-oai

> #12918 Skip history metadata scan for subagents @daveaitel-openai

> #12911 fix: ctrl c sub agent @jif-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.106.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-02-26-2-account-and-access-changes-in-rust-v0-106-0|2 Account and Access changes in rust-v0.106.0]] · Account and Access
- [[Changes/Codex CLI/2026-02-26-2-collaboration-changes-in-rust-v0-106-0|2 Collaboration changes in rust-v0.106.0]] · Collaboration
- [[Changes/Codex CLI/2026-02-26-improved-tui-local-file-link-rendering-to-hide-absolute-paths-while-preserving-v|Improved TUI local file-link rendering to hide absolute paths while preserving…]] · Interface Experience
- [[Changes/Codex CLI/2026-02-26-12417-core-bundle-settings-diff-updates-into-one-dev-user-envelope-charley-oai|♯12417 core: bundle settings diff updates into one dev/user envelope @charley-oai]] · Editor Experience
- [[Changes/Codex CLI/2026-02-26-4-model-support-changes-in-rust-v0-106-0|4 Model Support changes in rust-v0.106.0]] · Model Support
- [[Changes/Codex CLI/2026-02-26-3-memory-and-personalization-changes-in-rust-v0-106-0|3 Memory and Personalization changes in rust-v0.106.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-02-26-2-mobile-and-desktop-changes-in-rust-v0-106-0|2 Mobile and Desktop changes in rust-v0.106.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-02-26-12800-fix-enforce-sandbox-envelope-for-zsh-fork-execution-bolinfest|♯12800 fix: enforce sandbox envelope for zsh fork execution @bolinfest]] · Safety and Privacy
- [[Changes/Codex CLI/2026-02-26-12758-feat-include-available-decisions-in-command-approval-requests-bolinfest|♯12758 feat: include available decisions in command approval requests @bolinfest]] · Developer Workflow
- [[Changes/Codex CLI/2026-02-26-2-reliability-and-performance-changes-in-rust-v0-106-0|2 Reliability and Performance changes in rust-v0.106.0]] · Reliability and Performance
- [[Changes/Codex CLI/2026-02-26-36-other-changes-in-rust-v0-106-0|36 other changes in rust-v0.106.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-02-25 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-02-25-agent-protected-from-accidentally-killing-itself|Agent protected from accidentally killing itself]]
- Later: 2026-02-26 · Cursor · [[Changes/Cursor/2026-02-26-autofix-runs-cloud-agents-on-their-own-machines-to-test-changes-and-propose-fixe|Autofix runs cloud agents on their own machines to test changes and propose fixes…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-02-26-28133d&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-02-26-5-agent-mode-changes-in-rust-v0-106-0.md%0ACard%20ID%3A%20codex-cli-2026-02-26-28133d%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.106.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->