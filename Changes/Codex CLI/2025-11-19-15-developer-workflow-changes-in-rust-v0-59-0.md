---
card_id: codex-cli-2025-11-19-9ef357
date: '2025-11-19'
description: 'Codex CLI · 2025-11-19 · Developer Workflow: 15 changes in 0.59.0 —
  Eliminated ghost snapshot notifications when no `git` repository is present.'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter
    Colors]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2626
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 26a875c614ff753a63cd4e0c2e4e754966b1cf6b7461fe755a9fdf5584f5696f
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2025-11-19-9ef357
  comparison: ''
  date: '2025-11-19'
  description: 'Codex CLI — 0.59.0: 15 Developer Workflow changes'
  evidence:
  - quote: Eliminated ghost snapshot notifications when no `git` repository is present.
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.59.0
  - quote: 'nit: useless log to debug (#6898) — @jif'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.59.0
  - quote: Move shell to use `truncate_text` (#6842) — @aibrahim
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.59.0
  - quote: '[app-server-test-client] feat: auto approve command (#6852) — @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.59.0
  - quote: 'nit: mark ghost commit as stable (#6833) — @jif'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.59.0
  - quote: 'feat: git branch tooling (#6831) — @jif'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.59.0
  - quote: chore(core) Add shell_serialization coverage (#6810) — @dylan.hurd
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.59.0
  - quote: Demote function call payload log to debug to avoid noisy error-level stderr
      (#6808) — @cassirer
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.59.0
  - quote: '[app-server] feat: add v2 command execution approval flow (#6758) — @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.59.0
  - quote: 'core: add a feature to disable the shell tool (#6481) — @172423086+nornagon-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.59.0
  - quote: chore(core) Update shell instructions (#6679) — @dylan.hurd
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.59.0
  - quote: 'nit: personal git ignore (#6787) — @jif'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.59.0
  - quote: Revert "Revert \"Overhaul shell detection and centralize command generation
      for unified exec\"" (#6607) — @pakrym
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.59.0
  - quote: Revert "Overhaul shell detection and centralize command generation for
      unified exec" (#6606) — @pakrym
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.59.0
  - quote: Overhaul shell detection and centralize command generation for unified
      exec (#6577) — @pakrym
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.59.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 15-developer-workflow-changes-in-rust-v0-59-0
  source_release: codex-cli-2025-11-19-rust-v0-59-0-github-263735550-757042e7
  source_type: github_releases
  theme: developer-workflow
  title: 15 Developer Workflow changes in rust-v0.59.0
  type: change
related_changes:
- '[[Changes/Gemini CLI/2025-11-14-trivial-yaml-fixes-for-linter-by-joshualitt-in-https-github-com-google-gemini-ge|Trivial
  yaml fixes for linter]]'
- '[[Changes/Replit/2025-11-16-gitlab-and-bitbucket-support|GitLab and Bitbucket support]]'
- '[[Changes/GitHub Copilot CLI/2025-11-17-add-share-command-to-save-session-as-markdown-file-or-github-gist|Add
  /share command to save session as markdown file or GitHub gist]]'
source_release: '[[Releases/Codex CLI/codex-cli-2025-11-19-rust-v0-59-0-github-263735550-757042e7|codex-cli-2025-11-19-rust-v0-59-0-github-263735550-757042e7]]'
source_type: github_releases
theme: developer-workflow
title: 15 Developer Workflow changes in rust-v0.59.0
type: change
---

<!-- chronolog:begin region="header" -->
# 15 Developer Workflow changes in rust-v0.59.0

**Codex CLI** · 2025-11-19 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.59.0) · from [[Releases/Codex CLI/codex-cli-2025-11-19-rust-v0-59-0-github-263735550-757042e7|0.59.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Eliminated ghost snapshot notifications when no `git` repository is present.

> nit: useless log to debug (#6898) — @jif

> Move shell to use `truncate_text` (#6842) — @aibrahim

> [app-server-test-client] feat: auto approve command (#6852) — @owenlin0

> nit: mark ghost commit as stable (#6833) — @jif

> feat: git branch tooling (#6831) — @jif

> chore(core) Add shell_serialization coverage (#6810) — @dylan.hurd

> Demote function call payload log to debug to avoid noisy error-level stderr (#6808) — @cassirer

> [app-server] feat: add v2 command execution approval flow (#6758) — @owenlin0

> core: add a feature to disable the shell tool (#6481) — @172423086+nornagon-openai

> chore(core) Update shell instructions (#6679) — @dylan.hurd

> nit: personal git ignore (#6787) — @jif

> Revert "Revert \"Overhaul shell detection and centralize command generation for unified exec\"" (#6607) — @pakrym

> Revert "Overhaul shell detection and centralize command generation for unified exec" (#6606) — @pakrym

> Overhaul shell detection and centralize command generation for unified exec (#6577) — @pakrym

Source: https://github.com/openai/codex/releases/tag/rust-v0.59.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2025-11-19-handle-don-t-trust-directory-selection-in-onboarding-4941-viniciusmotta8|Handle "Don't Trust" directory selection in onboarding (♯4941) — @viniciusmotta8]] · Interface Experience
- [[Changes/Codex CLI/2025-11-19-2-agent-mode-changes-in-rust-v0-59-0|2 Agent Mode changes in rust-v0.59.0]] · Agent Mode
- [[Changes/Codex CLI/2025-11-19-native-compaction-support-added-first-class-support-for-compaction-improving-per|Native Compaction Support]] · Reliability and Performance
- [[Changes/Codex CLI/2025-11-19-bug-fix-rmcp-client-refresh-oauth-tokens-using-expires-at-6574-laelluo|:bug: fix(rmcp-client): refresh OAuth tokens using expires_at (♯6574) — @LaelLuo]] · Account and Access
- [[Changes/Codex CLI/2025-11-19-promote-shared-helpers-for-suite-tests-6460-aibrahim|Promote shared helpers for suite tests (♯6460) — @aibrahim]] · Collaboration
- [[Changes/Codex CLI/2025-11-19-6-context-window-changes-in-rust-v0-59-0|6 Context Window changes in rust-v0.59.0]] · Context Window
- [[Changes/Codex CLI/2025-11-19-3-mobile-and-desktop-changes-in-rust-v0-59-0|3 Mobile and Desktop changes in rust-v0.59.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2025-11-19-use-shared-network-gating-helper-in-chat-completion-tests-6461-aibrahim|Use shared network gating helper in chat completion tests (♯6461) — @aibrahim]] · Editor Experience
- [[Changes/Codex CLI/2025-11-19-5-model-support-changes-in-rust-v0-59-0|5 Model Support changes in rust-v0.59.0]] · Model Support
- [[Changes/Codex CLI/2025-11-19-5-apps-and-integrations-changes-in-rust-v0-59-0|5 Apps and Integrations changes in rust-v0.59.0]] · Apps and Integrations
- [[Changes/Codex CLI/2025-11-19-7-safety-and-privacy-changes-in-rust-v0-59-0|7 Safety and Privacy changes in rust-v0.59.0]] · Safety and Privacy
- [[Changes/Codex CLI/2025-11-19-credits-are-now-visible-in-status|Credits are now visible in /status]] · Pricing Model
- [[Changes/Codex CLI/2025-11-19-53-other-changes-in-rust-v0-59-0|53 other changes in rust-v0.59.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2025-11-17 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2025-11-17-add-share-command-to-save-session-as-markdown-file-or-github-gist|Add /share command to save session as markdown file or GitHub gist]]
- Later: 2025-11-20 · Gemini CLI · [[Changes/Gemini CLI/2025-11-20-feat-update-permissions-command-to-support-modifying-trust-for-other-by-shrutip9|feat: Update permissions command to support modifying trust for other…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-09-11 · Descript · [[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter Colors]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2025-11-19-9ef357&body=Card%3A%20Changes%2FCodex%20CLI%2F2025-11-19-15-developer-workflow-changes-in-rust-v0-59-0.md%0ACard%20ID%3A%20codex-cli-2025-11-19-9ef357%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.59.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->