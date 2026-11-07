---
card_id: codex-cli-2026-05-18-38d073
date: '2026-05-18'
description: 'Codex CLI · 2026-05-18 · Safety and Privacy: 17 changes in 0.131.0 —
  Hardened Windows sandbox behavior around deny-read rules, scoped write roots, ineffective…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke
    Application Access]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2120
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 083cad1783cd135c4a7d2581e78fcf93bec9d97c5b59643ccfaa087efa80f105
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-05-18-38d073
  comparison: ''
  date: '2026-05-18'
  description: 'Codex CLI — 0.131.0: 17 Safety and Privacy changes'
  evidence:
  - quote: 'Hardened Windows sandbox behavior around deny-read rules, scoped write
      roots, ineffective firewall policy, and PowerShell edge cases. (#18202, #21479,
      #22353, #21400, #22643)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: 'Preserved managed read restrictions during permission escalation and cleaned
      up workspace-root permission profile resolution. (#15977, #22624, #22683)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#21819 tests: cover sandbox link write behavior @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#21861 Apply sandbox context to local view_image reads @starr-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#18202 feat(sandbox): add Windows deny-read parity @viyatb-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22207 [codex] Tighten unified exec sandbox setup @bookholt-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22355 chore: Keep view_image sandbox test in temp dir @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#21479 [codex] Scope Windows sandbox write-root capability SIDs @adrianbravo-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22353 windows-sandbox: fail elevated setup when firewall policy is ineffective
      @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#21400 Avoid PowerShell profiles in elevated Windows sandbox @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22576 tests: avoid ambient temp sandbox roots @starr-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22687 Fix Windows sandbox clippy clones @starr-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22611 app-server: use permission ids and runtime workspace roots @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22789 guardian: use permission profile for review sandbox @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22791 telemetry: tag sandboxes from permission profiles @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22792 app-server: stop returning thread permission profiles @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  - quote: '#22795 core: construct test permission profiles directly @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.131.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 17-safety-and-privacy-changes-in-rust-v0-131-0
  source_release: codex-cli-2026-05-18-rust-v0-131-0-github-324452638-5f16ff1d
  source_type: github_releases
  theme: safety-privacy
  title: 17 Safety and Privacy changes in rust-v0.131.0
  type: change
related_changes:
- '[[Changes/v0/2026-05-15-added-docs-for-the-project-sandbox-terminal-commands-and-permission-modes|Added
  docs for the project sandbox , terminal commands , and permission modes]]'
- '[[Changes/Devin/2026-05-17-miscellaneous-improvements|Miscellaneous Improvements]]'
- '[[Changes/Devin/2026-05-17-slack-security-hardening|Slack Security Hardening]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-05-18-rust-v0-131-0-github-324452638-5f16ff1d|codex-cli-2026-05-18-rust-v0-131-0-github-324452638-5f16ff1d]]'
source_type: github_releases
theme: safety-privacy
title: 17 Safety and Privacy changes in rust-v0.131.0
type: change
---

<!-- chronolog:begin region="header" -->
# 17 Safety and Privacy changes in rust-v0.131.0

**Codex CLI** · 2026-05-18 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.131.0) · from [[Releases/Codex CLI/codex-cli-2026-05-18-rust-v0-131-0-github-324452638-5f16ff1d|0.131.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Hardened Windows sandbox behavior around deny-read rules, scoped write roots, ineffective firewall policy, and PowerShell edge cases. (#18202, #21479, #22353, #21400, #22643)

> Preserved managed read restrictions during permission escalation and cleaned up workspace-root permission profile resolution. (#15977, #22624, #22683)

> #21819 tests: cover sandbox link write behavior @bolinfest

> #21861 Apply sandbox context to local view_image reads @starr-openai

> #18202 feat(sandbox): add Windows deny-read parity @viyatb-oai

> #22207 [codex] Tighten unified exec sandbox setup @bookholt-oai

> #22355 chore: Keep view_image sandbox test in temp dir @jif-oai

> #21479 [codex] Scope Windows sandbox write-root capability SIDs @adrianbravo-oai

> #22353 windows-sandbox: fail elevated setup when firewall policy is ineffective @iceweasel-oai

> #21400 Avoid PowerShell profiles in elevated Windows sandbox @iceweasel-oai

> #22576 tests: avoid ambient temp sandbox roots @starr-openai

> #22687 Fix Windows sandbox clippy clones @starr-openai

> #22611 app-server: use permission ids and runtime workspace roots @bolinfest

> #22789 guardian: use permission profile for review sandbox @bolinfest

> #22791 telemetry: tag sandboxes from permission profiles @bolinfest

> #22792 app-server: stop returning thread permission profiles @bolinfest

> #22795 core: construct test permission profiles directly @bolinfest

Source: https://github.com/openai/codex/releases/tag/rust-v0.131.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-05-18-5-account-and-access-changes-in-rust-v0-131-0|5 Account and Access changes in rust-v0.131.0]] · Account and Access
- [[Changes/Codex CLI/2026-05-18-9-agent-mode-changes-in-rust-v0-131-0|9 Agent Mode changes in rust-v0.131.0]] · Agent Mode
- [[Changes/Codex CLI/2026-05-18-4-memory-and-personalization-changes-in-rust-v0-131-0|4 Memory and Personalization changes in rust-v0.131.0]] · Memory and Personalization
- [[Changes/Codex CLI/2026-05-18-5-interface-experience-changes-in-rust-v0-131-0|5 Interface Experience changes in rust-v0.131.0]] · Interface Experience
- [[Changes/Codex CLI/2026-05-18-12-developer-workflow-changes-in-rust-v0-131-0|12 Developer Workflow changes in rust-v0.131.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-05-18-56-apps-and-integrations-changes-in-rust-v0-131-0|56 Apps and Integrations changes in rust-v0.131.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-05-18-21954-fix-goal-update-and-add-goal-edit-command-in-tui-etraut-openai|♯21954 Fix goal update and add /goal edit command in TUI @etraut-openai]] · Editor Experience
- [[Changes/Codex CLI/2026-05-18-10-mobile-and-desktop-changes-in-rust-v0-131-0|10 Mobile and Desktop changes in rust-v0.131.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-05-18-7-context-window-changes-in-rust-v0-131-0|7 Context Window changes in rust-v0.131.0]] · Context Window
- [[Changes/Codex CLI/2026-05-18-3-collaboration-changes-in-rust-v0-131-0|3 Collaboration changes in rust-v0.131.0]] · Collaboration
- [[Changes/Codex CLI/2026-05-18-4-model-support-changes-in-rust-v0-131-0|4 Model Support changes in rust-v0.131.0]] · Model Support
- [[Changes/Codex CLI/2026-05-18-155-other-changes-in-rust-v0-131-0|155 other changes in rust-v0.131.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-05-17 · Devin · [[Changes/Devin/2026-05-17-slack-security-hardening|Slack Security Hardening]]
- Later: 2026-05-18 · Lovable · [[Changes/Lovable/2026-05-18-wiz-security-scanning|Wiz security scanning]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Descript · [[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke Application Access]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-05-18-38d073&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-05-18-17-safety-and-privacy-changes-in-rust-v0-131-0.md%0ACard%20ID%3A%20codex-cli-2026-05-18-38d073%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.131.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->