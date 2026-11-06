---
card_id: codex-cli-2025-09-10-5d4dac
date: '2025-09-10'
description: 'Codex CLI · 2025-09-10 · Other changes: 15 changes in 0.32.0 — OSS:
  Broader `apply_patch` OSS compatibility.'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: b9d452757ebaa2312c84fed1e2a06c8957e8b2b480fb26d7c7cb0d5fbb8f09fd
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2025-09-10-5d4dac
  comparison: ''
  date: '2025-09-10'
  description: 'Codex CLI — 0.32.0: 15 other changes'
  evidence:
  - quote: 'OSS: Broader `apply_patch` OSS compatibility.'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.32.0
  - quote: 'Rollouts: initial groundwork and `rollout_path` included in responses.'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.32.0
  - quote: 'TUI: Alt+Delete deletes the next word.'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.32.0
  - quote: 'Protocol/Types: `ArchiveConversation` request; small exports and TS type
      improvements.'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.32.0
  - quote: '[#3394] alt+delete deletes the word to the right of the cursor (delete_forward_word)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.32.0
  - quote: '[#3388] Replace config.responses_originator_header_internal_override with
      CODEX_INTERNAL_ORIGINATOR_OVERRIDE_ENV_VAR'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.32.0
  - quote: '[#3387] No fail fast'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.32.0
  - quote: '[#3380] Introduce rollout items'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.32.0
  - quote: '[#3374] tweak "failed to find expected lines" message in apply_patch'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.32.0
  - quote: '[#3353] feat: add ArchiveConversation to ClientRequest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.32.0
  - quote: '[#3338] feat: Run cargo shear during CI'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.32.0
  - quote: '[#3334] allow mach-lookup for com.apple.system.opendirectoryd.libinfo'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.32.0
  - quote: '[#3270] feat(core): re-export InitialHistory from conversation_manager'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.32.0
  - quote: '[#3219] Generate more typescript types and return conversation id with
      ConversationSummary'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.32.0
  - quote: '[#3179] feat: POSIX unification and snapshot sessions'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.32.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 15-other-changes-in-rust-v0-32-0
  source_release: codex-cli-2025-09-10-rust-v0-32-0-github-246248951-dfa94f54
  source_type: github_releases
  theme: uncategorized
  title: 15 other changes in rust-v0.32.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2025-09-10-rust-v0-32-0-github-246248951-dfa94f54|codex-cli-2025-09-10-rust-v0-32-0-github-246248951-dfa94f54]]'
source_type: github_releases
theme: uncategorized
title: 15 other changes in rust-v0.32.0
type: change
---

<!-- chronolog:begin region="header" -->
# 15 other changes in rust-v0.32.0

**Codex CLI** · 2025-09-10 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.32.0) · from [[Releases/Codex CLI/codex-cli-2025-09-10-rust-v0-32-0-github-246248951-dfa94f54|0.32.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> OSS: Broader `apply_patch` OSS compatibility.

> Rollouts: initial groundwork and `rollout_path` included in responses.

> TUI: Alt+Delete deletes the next word.

> Protocol/Types: `ArchiveConversation` request; small exports and TS type improvements.

> [#3394] alt+delete deletes the word to the right of the cursor (delete_forward_word)

> [#3388] Replace config.responses_originator_header_internal_override with CODEX_INTERNAL_ORIGINATOR_OVERRIDE_ENV_VAR

> [#3387] No fail fast

> [#3380] Introduce rollout items

> [#3374] tweak "failed to find expected lines" message in apply_patch

> [#3353] feat: add ArchiveConversation to ClientRequest

> [#3338] feat: Run cargo shear during CI

> [#3334] allow mach-lookup for com.apple.system.opendirectoryd.libinfo

> [#3270] feat(core): re-export InitialHistory from conversation_manager

> [#3219] Generate more typescript types and return conversation id with ConversationSummary

> [#3179] feat: POSIX unification and snapshot sessions

Source: https://github.com/openai/codex/releases/tag/rust-v0.32.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2025-09-10-2-apps-and-integrations-changes-in-rust-v0-32-0|2 Apps and Integrations changes in rust-v0.32.0]] · Apps and Integrations
- [[Changes/Codex CLI/2025-09-10-2-developer-workflow-changes-in-rust-v0-32-0|2 Developer Workflow changes in rust-v0.32.0]] · Developer Workflow
- [[Changes/Codex CLI/2025-09-10-2-model-support-changes-in-rust-v0-32-0|2 Model Support changes in rust-v0.32.0]] · Model Support
- [[Changes/Codex CLI/2025-09-10-ci-build-faster-tests-with-nextest-add-shear-minor-macos-permission-adjustment|CI/Build: faster tests with nextest, add shear; minor macOS permission adjustment]] · Safety and Privacy
- [[Changes/Codex CLI/2025-09-10-3323-chore-try-switching-to-cargo-nextest-to-speed-up-ci-builds|♯3323 chore: try switching to cargo nextest to speed up CI builds]] · Reliability and Performance
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2025-09-10-5d4dac&body=Card%3A%20Changes%2FCodex%20CLI%2F2025-09-10-15-other-changes-in-rust-v0-32-0.md%0ACard%20ID%3A%20codex-cli-2025-09-10-5d4dac%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.32.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->