---
card_id: codex-cli-2026-05-20-856d25
date: '2026-05-20'
description: 'Codex CLI · 2026-05-20 · Reliability and Performance: Windows installs
  are more robust: `codex doctor` now detects npm-managed installs correctly, and
  MSVC…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General
    performance: Among other improvements, users will notice that ChatGPT is now…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1252
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: change
machine_hash: d59b52af0120bb5074f06dd8d64004293fa9d556d676c1d9a478fc4cfee8e5b7
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-05-20-856d25
  comparison: ''
  date: '2026-05-20'
  description: 'Codex CLI — 0.132.0: Windows installs are more robust: `codex doctor`
    now detects npm-managed installs correctly, and MSVC release binaries no longer
    depend on separately installed VC++ runtime DLLs. (#22967, #22905)'
  evidence:
  - quote: 'Windows installs are more robust: `codex doctor` now detects npm-managed
      installs correctly, and MSVC release binaries no longer depend on separately
      installed VC++ runtime DLLs. (#22967, #22905)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.132.0
  extractor_version: fallback-v5
  impact: incremental
  kind: change
  product: codex-cli
  product_name: Codex CLI
  slug: windows-installs-are-more-robust-codex-doctor-now-detects-npm-managed-installs-c
  source_release: codex-cli-2026-05-20-rust-v0-132-0-github-325545332-3345c1c4
  source_type: github_releases
  theme: reliability-performance
  theme_matches: []
  theme_resolution: manual-semantic-rule-v1
  title: Windows installs are more robust
  type: change
related_changes:
- '[[Changes/Lovable/2026-05-18-speed-tab-the-standalone-speed-tab-has-been-removed-speed-and-lighthouse-checks|Speed
  tab. The standalone Speed tab has been removed]]'
- '[[Changes/OpenCode/2026-05-18-desktop-speed-up-large-session-timelines|Desktop
  Speed up large session timelines]]'
- '[[Changes/Dify/2026-05-19-knowledge-base-stability-fixed-knowledge-hit-testing-rendering-empty-knowledge-c|Knowledge-base
  stability — fixed knowledge hit-testing rendering, empty…]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-05-20-rust-v0-132-0-github-325545332-3345c1c4|codex-cli-2026-05-20-rust-v0-132-0-github-325545332-3345c1c4]]'
source_type: github_releases
theme: reliability-performance
title: Windows installs are more robust
type: change
---

<!-- chronolog:begin region="header" -->
# Windows installs are more robust

**Codex CLI** · 2026-05-20 · [[Themes/reliability-performance|Reliability and Performance]] · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.132.0) · from [[Releases/Codex CLI/codex-cli-2026-05-20-rust-v0-132-0-github-325545332-3345c1c4|0.132.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Windows installs are more robust: `codex doctor` now detects npm-managed installs correctly, and MSVC release binaries no longer depend on separately installed VC++ runtime DLLs. (#22967, #22905)
>
> Source: https://github.com/openai/codex/releases/tag/rust-v0.132.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-05-20-3-interface-experience-changes-in-rust-v0-132-0|3 Interface Experience changes in rust-v0.132.0]] · Interface Experience
- [[Changes/Codex CLI/2026-05-20-5-safety-and-privacy-changes-in-rust-v0-132-0|5 Safety and Privacy changes in rust-v0.132.0]] · Safety and Privacy
- [[Changes/Codex CLI/2026-05-20-codex-exec-resume-now-accepts-output-schema-so-resumed-automations-can-keep-sess|codex exec resume now accepts --output-schema, so resumed automations can keep…]] · Automation and Scheduling
- [[Changes/Codex CLI/2026-05-20-23069-multiagent-trim-model-visible-description-cap-to-5-models-sayan-oai|♯23069 multiagent: trim model-visible description, cap to 5 models @sayan-oai]] · Model Support
- [[Changes/Codex CLI/2026-05-20-9-apps-and-integrations-changes-in-rust-v0-132-0|9 Apps and Integrations changes in rust-v0.132.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-05-20-2-account-and-access-changes-in-rust-v0-132-0|2 Account and Access changes in rust-v0.132.0]] · Account and Access
- [[Changes/Codex CLI/2026-05-20-3-developer-workflow-changes-in-rust-v0-132-0|3 Developer Workflow changes in rust-v0.132.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-05-20-2-memory-and-personalization-changes-in-rust-v0-132-0|2 Memory and Personalization changes in rust-v0.132.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-05-20-23147-make-multi-agent-v2-tool-namespace-configurable-jif-oai|♯23147 Make multi-agent v2 tool namespace configurable @jif-oai]] · Agent Mode
- [[Changes/Codex CLI/2026-05-20-3-editor-experience-changes-in-rust-v0-132-0|3 Editor Experience changes in rust-v0.132.0]] · Editor Experience
- [[Changes/Codex CLI/2026-05-20-31-other-changes-in-rust-v0-132-0|31 other changes in rust-v0.132.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Reliability and Performance

- Earlier: 2026-05-19 · Dify · [[Changes/Dify/2026-05-19-knowledge-base-stability-fixed-knowledge-hit-testing-rendering-empty-knowledge-c|Knowledge-base stability — fixed knowledge hit-testing rendering, empty…]]
- Later: 2026-05-21 · Claude Code · [[Changes/Claude Code/2026-05-21-2-reliability-and-performance-changes-in-v2-1-146|2 Reliability and Performance changes in v2.1.146]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2022-12-15 · ChatGPT · [[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General performance: Among other improvements, users will notice that ChatGPT is now…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-05-20-856d25&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-05-20-windows-installs-are-more-robust-codex-doctor-now-detects-npm-managed-installs-c.md%0ACard%20ID%3A%20codex-cli-2026-05-20-856d25%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.132.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->