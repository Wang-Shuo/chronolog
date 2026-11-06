---
card_id: codex-cli-2026-01-15-01fa4e
date: '2026-01-15'
description: 'Codex CLI · 2026-01-15 · Other changes: 9 changes in 0.85.0 — `codex
  resume --last` now respects the current working directory, with `--all` as an explicit…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 67474b483216ce48297b1ff2b6087ba408560686a66a340511c605ff0e20ef33
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-01-15-01fa4e
  comparison: ''
  date: '2026-01-15'
  description: 'Codex CLI — 0.85.0: 9 other changes'
  evidence:
  - quote: '`codex resume --last` now respects the current working directory, with
      `--all` as an explicit override. (#9245)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.85.0
  - quote: Stdin prompt decoding now handles BOMs/UTF-16 and provides clearer errors
      for invalid encodings. (#9151)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.85.0
  - quote: '#9250 fix: fallback to Landlock-only when user namespaces unavailable
      and set PR_SET_NO_NEW_PRIVS early @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.85.0
  - quote: '#9213 feat: collab tools app-server event mapping @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.85.0
  - quote: '#9276 feat: add interrupt capabilities to `send_input` @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.85.0
  - quote: '#9209 feat: basic tui for event emission @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.85.0
  - quote: '#9245 Changed `codex resume --last` to honor the current cwd @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.85.0
  - quote: '#9151 fix(exec): improve stdin prompt decoding @liqiongyu'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.85.0
  - quote: '#9300 revert: remove pre-Landlock bind mounts apply @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.85.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 9-other-changes-in-rust-v0-85-0
  source_release: codex-cli-2026-01-15-rust-v0-85-0-github-277157618-2b62da73
  source_type: github_releases
  theme: uncategorized
  title: 9 other changes in rust-v0.85.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2026-01-15-rust-v0-85-0-github-277157618-2b62da73|codex-cli-2026-01-15-rust-v0-85-0-github-277157618-2b62da73]]'
source_type: github_releases
theme: uncategorized
title: 9 other changes in rust-v0.85.0
type: change
---

<!-- chronolog:begin region="header" -->
# 9 other changes in rust-v0.85.0

**Codex CLI** · 2026-01-15 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.85.0) · from [[Releases/Codex CLI/codex-cli-2026-01-15-rust-v0-85-0-github-277157618-2b62da73|0.85.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> `codex resume --last` now respects the current working directory, with `--all` as an explicit override. (#9245)

> Stdin prompt decoding now handles BOMs/UTF-16 and provides clearer errors for invalid encodings. (#9151)

> #9250 fix: fallback to Landlock-only when user namespaces unavailable and set PR_SET_NO_NEW_PRIVS early @viyatb-oai

> #9213 feat: collab tools app-server event mapping @jif-oai

> #9276 feat: add interrupt capabilities to `send_input` @jif-oai

> #9209 feat: basic tui for event emission @jif-oai

> #9245 Changed `codex resume --last` to honor the current cwd @etraut-openai

> #9151 fix(exec): improve stdin prompt decoding @liqiongyu

> #9300 revert: remove pre-Landlock bind mounts apply @viyatb-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.85.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-01-15-9207-propagate-mcp-disabled-reason-gt-oai|♯9207 Propagate MCP disabled reason @gt-oai]] · Apps and Integrations
- [[Changes/Codex CLI/2026-01-15-revert-linux-sandboxing-now-falls-back-to-landlock-only-restrictions-when-user-n|revert Linux sandboxing now falls back to Landlock-only restrictions when user…]] · Safety and Privacy
- [[Changes/Codex CLI/2026-01-15-2-collaboration-changes-in-rust-v0-85-0|2 Collaboration changes in rust-v0.85.0]] · Collaboration
- [[Changes/Codex CLI/2026-01-15-9275-feat-add-agent-roles-to-collab-tools-jif-oai|♯9275 feat: add agent roles to collab tools @jif-oai]] · Agent Mode
- [[Changes/Codex CLI/2026-01-15-2-model-support-changes-in-rust-v0-85-0|2 Model Support changes in rust-v0.85.0]] · Model Support
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-01-15-01fa4e&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-01-15-9-other-changes-in-rust-v0-85-0.md%0ACard%20ID%3A%20codex-cli-2026-01-15-01fa4e%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.85.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->