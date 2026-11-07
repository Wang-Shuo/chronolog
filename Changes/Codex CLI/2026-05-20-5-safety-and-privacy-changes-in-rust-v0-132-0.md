---
card_id: codex-cli-2026-05-20-31b10f
date: '2026-05-20'
description: 'Codex CLI · 2026-05-20 · Safety and Privacy: 5 changes in 0.132.0 —
  #22891 tui: pass active permission profiles through app commands @bolinfest'
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke
    Application Access]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2122
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: b9586978b2a13268c4e9f8a477fb669ca7a13ee8598a7cb05491978677ff12bf
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-05-20-31b10f
  comparison: ''
  date: '2026-05-20'
  description: 'Codex CLI — 0.132.0: 5 Safety and Privacy changes'
  evidence:
  - quote: '#22891 tui: pass active permission profiles through app commands @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.132.0
  - quote: '#22920 core: set permission profiles from snapshots @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.132.0
  - quote: '#23030 test: construct permission profiles directly @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.132.0
  - quote: '#23036 test: reduce core sandbox policy test setup @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.132.0
  - quote: '#22569 Simplify legacy Windows sandbox ACL persistence @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.132.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 5-safety-and-privacy-changes-in-rust-v0-132-0
  source_release: codex-cli-2026-05-20-rust-v0-132-0-github-325545332-3345c1c4
  source_type: github_releases
  theme: safety-privacy
  title: 5 Safety and Privacy changes in rust-v0.132.0
  type: change
related_changes:
- '[[Changes/Claude Code/2026-05-19-fixed-skill-tool-failing-with-permission-error-in-headless-mode-regression-in-v2|Fixed
  Skill tool failing with permission error in headless mode (regression in v2.1.141)]]'
- '[[Changes/Dify/2026-05-19-2-safety-and-privacy-changes-in-1-14-2|2 Safety and Privacy
  changes in 1.14.2]]'
- '[[Changes/GitHub Copilot CLI/2026-05-19-memory-permission-prompts-now-name-who-can-see-a-stored-memory-user-scope-or-the|Memory
  permission prompts now name who can see a stored memory]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-05-20-rust-v0-132-0-github-325545332-3345c1c4|codex-cli-2026-05-20-rust-v0-132-0-github-325545332-3345c1c4]]'
source_type: github_releases
theme: safety-privacy
title: 5 Safety and Privacy changes in rust-v0.132.0
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Safety and Privacy changes in rust-v0.132.0

**Codex CLI** · 2026-05-20 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.132.0) · from [[Releases/Codex CLI/codex-cli-2026-05-20-rust-v0-132-0-github-325545332-3345c1c4|0.132.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> #22891 tui: pass active permission profiles through app commands @bolinfest

> #22920 core: set permission profiles from snapshots @bolinfest

> #23030 test: construct permission profiles directly @bolinfest

> #23036 test: reduce core sandbox policy test setup @bolinfest

> #22569 Simplify legacy Windows sandbox ACL persistence @iceweasel-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.132.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-05-20-3-interface-experience-changes-in-rust-v0-132-0|3 Interface Experience changes in rust-v0.132.0]] · Interface Experience
- [[Changes/Codex CLI/2026-05-20-codex-exec-resume-now-accepts-output-schema-so-resumed-automations-can-keep-sess|codex exec resume now accepts --output-schema, so resumed automations can keep…]] · Automation and Scheduling
- [[Changes/Codex CLI/2026-05-20-23069-multiagent-trim-model-visible-description-cap-to-5-models-sayan-oai|♯23069 multiagent: trim model-visible description, cap to 5 models @sayan-oai]] · Model Support
- [[Changes/Codex CLI/2026-05-20-windows-installs-are-more-robust-codex-doctor-now-detects-npm-managed-installs-c|Windows installs are more robust]] · Reliability and Performance
- [[Changes/Codex CLI/2026-05-20-9-apps-and-integrations-changes-in-rust-v0-132-0|9 Apps and Integrations changes in rust-v0.132.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-05-20-2-account-and-access-changes-in-rust-v0-132-0|2 Account and Access changes in rust-v0.132.0]] · Account and Access
- [[Changes/Codex CLI/2026-05-20-3-developer-workflow-changes-in-rust-v0-132-0|3 Developer Workflow changes in rust-v0.132.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-05-20-2-memory-and-personalization-changes-in-rust-v0-132-0|2 Memory and Personalization changes in rust-v0.132.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-05-20-23147-make-multi-agent-v2-tool-namespace-configurable-jif-oai|♯23147 Make multi-agent v2 tool namespace configurable @jif-oai]] · Agent Mode
- [[Changes/Codex CLI/2026-05-20-3-editor-experience-changes-in-rust-v0-132-0|3 Editor Experience changes in rust-v0.132.0]] · Editor Experience
- [[Changes/Codex CLI/2026-05-20-31-other-changes-in-rust-v0-132-0|31 other changes in rust-v0.132.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-05-19 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-05-19-memory-permission-prompts-now-name-who-can-see-a-stored-memory-user-scope-or-the|Memory permission prompts now name who can see a stored memory]]
- Later: 2026-05-20 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-05-20-add-security-review-slash-command-to-review-code-changes-for-security-vulnerabil|Add /security-review slash command to review code changes for security…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Descript · [[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke Application Access]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-05-20-31b10f&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-05-20-5-safety-and-privacy-changes-in-rust-v0-132-0.md%0ACard%20ID%3A%20codex-cli-2026-05-20-31b10f%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.132.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->