---
card_id: github-copilot-cli-2026-10-19-469527
date: '2026-10-19'
description: 'GitHub Copilot CLI · 2026-10-19 · Safety and Privacy: 6 changes in 1.0.100
  — Sandbox host-rule traffic now honors HTTPS_PROXY and HTTP_PROXY when no sandbox…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke
    Application Access]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2274
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 5714c69813054f8bc91c266c46bbc48cde679b7fbae3cb90456af3e6b85f50b9
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-10-19-469527
  comparison: ''
  date: '2026-10-19'
  description: 'GitHub Copilot CLI — 1.0.100: 6 Safety and Privacy changes'
  evidence:
  - quote: Sandbox host-rule traffic now honors HTTPS_PROXY and HTTP_PROXY when no
      sandbox proxy is configured
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.100
  - quote: Sandboxed shell commands now explain credential-proxy certificate trust
      failures and can offer an approved rerun outside the sandbox.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.100
  - quote: Assisted permissions send nested PowerShell and bash -c commands that only
      expand plain-data environment variables, single-quoted PowerShell, and PowerShell
      variable and alias statements to the permission judge instead of requiring unnecessary
      manual approval
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.100
  - quote: Prompt to update the sandbox proxy certificate authority when masked hosts
      change
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.100
  - quote: /sandbox can keep sandboxing enabled for the current session without enabling
      it globally
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.100
  - quote: Sandbox allows local network access by default so commands can reach localhost
      and private-network services.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.100
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 6-safety-and-privacy-changes-in-v1-0-100
  source_release: github-copilot-cli-2026-10-19-v1-0-100-github-417622960-9e2e7578
  source_type: github_releases
  theme: safety-privacy
  title: 6 Safety and Privacy changes in v1.0.100
  type: change
related_changes:
- '[[Changes/Open WebUI/2026-10-16-2-safety-and-privacy-changes-in-v0-12-3|2 Safety
  and Privacy changes in v0.12.3]]'
- '[[Changes/OpenClaw/2026-10-16-2-safety-and-privacy-changes-in-v2026-10-4|2 Safety
  and Privacy changes in v2026.10.4]]'
- '[[Changes/Claude Code/2026-10-19-added-decider-person-to-a-mod-s-tool-check-answer-only-the-permission-dialog-or|Added
  decider: "person" to a mod''s tool.check answer: only the permission dialog…]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-10-19-v1-0-100-github-417622960-9e2e7578|github-copilot-cli-2026-10-19-v1-0-100-github-417622960-9e2e7578]]'
source_type: github_releases
theme: safety-privacy
title: 6 Safety and Privacy changes in v1.0.100
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Safety and Privacy changes in v1.0.100

**GitHub Copilot CLI** · 2026-10-19 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.100) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-10-19-v1-0-100-github-417622960-9e2e7578|1.0.100]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Sandbox host-rule traffic now honors HTTPS_PROXY and HTTP_PROXY when no sandbox proxy is configured

> Sandboxed shell commands now explain credential-proxy certificate trust failures and can offer an approved rerun outside the sandbox.

> Assisted permissions send nested PowerShell and bash -c commands that only expand plain-data environment variables, single-quoted PowerShell, and PowerShell variable and alias statements to the permission judge instead of requiring unnecessary manual approval

> Prompt to update the sandbox proxy certificate authority when masked hosts change

> /sandbox can keep sandboxing enabled for the current session without enabling it globally

> Sandbox allows local network access by default so commands can reach localhost and private-network services.

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.100
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-10-19-3-account-and-access-changes-in-v1-0-100|3 Account and Access changes in v1.0.100]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-10-19-2-agent-mode-changes-in-v1-0-100|2 Agent Mode changes in v1.0.100]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-10-19-keep-saved-diff-review-comments-when-reopening-an-unchanged-diff-in-the-same-ses|Keep saved /diff review comments when reopening an unchanged diff in the same…]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-10-19-reasoning-only-max-token-responses-no-longer-loop-indefinitely-and-now-end-with|Reasoning-only max-token responses no longer loop indefinitely and now end…]] · Automation and Scheduling
- [[Changes/GitHub Copilot CLI/2026-10-19-2-interface-experience-changes-in-v1-0-100|2 Interface Experience changes in v1.0.100]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-10-19-avoid-false-context-exhaustion-and-rollover-refusal-when-tool-definitions-are-de|Avoid false context exhaustion and rollover refusal when tool definitions are deferred]] · Context Window
- [[Changes/GitHub Copilot CLI/2026-10-19-2-search-and-browsing-changes-in-v1-0-100|2 Search and Browsing changes in v1.0.100]] · Search and Browsing
- [[Changes/GitHub Copilot CLI/2026-10-19-2-developer-workflow-changes-in-v1-0-100|2 Developer Workflow changes in v1.0.100]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-10-19-voice-dictation-no-longer-inserts-language-markers-like-en-us-into-transcript-te|Voice dictation no longer inserts language markers like en-US into transcript text]] · Voice and Audio
- [[Changes/GitHub Copilot CLI/2026-10-19-10-apps-and-integrations-changes-in-v1-0-100|10 Apps and Integrations changes in v1.0.100]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-10-19-3-model-support-changes-in-v1-0-100|3 Model Support changes in v1.0.100]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-10-19-2-enterprise-and-administration-changes-in-v1-0-100|2 Enterprise and Administration changes in v1.0.100]] · Enterprise and Administration
- [[Changes/GitHub Copilot CLI/2026-10-19-complete-usage-reporting-no-longer-shows-partial-status-or-phantom-unattributed|Complete usage reporting no longer shows partial status or phantom unattributed…]] · Pricing Model
- [[Changes/GitHub Copilot CLI/2026-10-19-12-other-changes-in-v1-0-100|12 other changes in v1.0.100]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-10-19 · Claude Code · [[Changes/Claude Code/2026-10-19-added-decider-person-to-a-mod-s-tool-check-answer-only-the-permission-dialog-or|Added decider: "person" to a mod's tool.check answer: only the permission dialog…]]
- Later: 2026-10-19 · OpenHands · [[Changes/OpenHands/2026-10-19-fix-theme-make-consent-backend-scope-readable-by-enyst-in-https-github-com-openh|fix(theme): make consent backend scope readable]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Descript · [[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke Application Access]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-10-19-469527&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-10-19-6-safety-and-privacy-changes-in-v1-0-100.md%0ACard%20ID%3A%20github-copilot-cli-2026-10-19-469527%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.100%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->