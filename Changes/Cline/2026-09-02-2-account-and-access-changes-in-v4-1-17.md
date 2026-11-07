---
card_id: cline-2026-09-02-b0919c
date: '2026-09-02'
description: 'Cline · 2026-09-02 · Account and Access: 2 changes in v4.1.17 — Signing
  in to OpenAI Codex (ChatGPT subscription) now fails with a clear "port in use" error…'
diffusion:
  first_in_tracked: "[[Changes/Notion/2020-07-28-sign-into-notion-with-your-apple-id-the-perfect-combination-of-speedy-and-secure|Sign
    into Notion with your Apple ID \U0001F5DD️ The perfect combination of speedy and
    secure]]"
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2227
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: f9036c983a63ed056d5f4932d106a3c4245a60d944875712a456222d65368f25
product: cline
product_name: Cline
record:
  card_id: cline-2026-09-02-b0919c
  comparison: ''
  date: '2026-09-02'
  description: 'Cline — v4.1.17: 2 Account and Access changes'
  evidence:
  - quote: Signing in to OpenAI Codex (ChatGPT subscription) now fails with a clear
      "port in use" error when callback port 1455 is occupied. Previously the button
      opened a browser to a flow whose callback could never arrive, and nothing else
      happened. OAuth redirect errors such as `access_denied` are surfaced instead
      of being reported as a missing authorization code.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.17
  - quote: A transient network failure while refreshing OpenAI Codex or OpenAI-compatible-account
      tokens no longer signs you out. Only a genuinely rejected refresh token now
      requires re-authentication.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.17
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: cline
  product_name: Cline
  slug: 2-account-and-access-changes-in-v4-1-17
  source_release: cline-2026-09-02-v4-1-17-github-381000681-694bbda2
  source_type: github_releases
  theme: account-access
  title: 2 Account and Access changes in v4.1.17
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-09-01-2-account-and-access-changes-in-rust-v0-152-0|2
  Account and Access changes in rust-v0.152.0]]'
- '[[Changes/OpenClaw/2026-09-01-2-account-and-access-changes-in-v2026-8-2|2 Account
  and Access changes in v2026.8.2]]'
- '[[Changes/OpenCode/2026-09-01-azure-cli-sign-in-now-asks-for-the-resource-name-directly-instead-of-querying-az|Azure
  CLI sign-in now asks for the resource name directly instead of querying Azure…]]'
source_release: '[[Releases/Cline/cline-2026-09-02-v4-1-17-github-381000681-694bbda2|cline-2026-09-02-v4-1-17-github-381000681-694bbda2]]'
source_type: github_releases
theme: account-access
title: 2 Account and Access changes in v4.1.17
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Account and Access changes in v4.1.17

**Cline** · 2026-09-02 · [[Themes/account-access|Account and Access]] · Digest · [Official source](https://github.com/cline/cline/releases/tag/v4.1.17) · from [[Releases/Cline/cline-2026-09-02-v4-1-17-github-381000681-694bbda2|v4.1.17]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Signing in to OpenAI Codex (ChatGPT subscription) now fails with a clear "port in use" error when callback port 1455 is occupied. Previously the button opened a browser to a flow whose callback could never arrive, and nothing else happened. OAuth redirect errors such as `access_denied` are surfaced instead of being reported as a missing authorization code.

> A transient network failure while refreshing OpenAI Codex or OpenAI-compatible-account tokens no longer signs you out. Only a genuinely rejected refresh token now requires re-authentication.

Source: https://github.com/cline/cline/releases/tag/v4.1.17
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Cline/2026-09-02-3-model-support-changes-in-v4-1-17|3 Model Support changes in v4.1.17]] · Model Support
- [[Changes/Cline/2026-09-02-2-apps-and-integrations-changes-in-v4-1-17|2 Apps and Integrations changes in v4.1.17]] · Apps and Integrations
- [[Changes/Cline/2026-09-02-aborting-a-task-now-also-cancels-the-delegated-subagents-and-teammates-it-spawne|Aborting a task now also cancels the delegated subagents and teammates it spawned…]] · Agent Mode
- [[Changes/Cline/2026-09-02-cost-estimates-no-longer-appear-in-task-history-for-subscription-billed-tasks-cl|Cost estimates no longer appear in task history for subscription-billed tasks…]] · Pricing Model
- [[Changes/Cline/2026-09-02-global-rules-are-now-also-read-from-cline-rules-which-is-where-the-rules-tab-wri|Global rules are now also read from ~/Cline/Rules, which is where the Rules tab…]] · Developer Workflow
- [[Changes/Cline/2026-09-02-7-other-changes-in-v4-1-17|7 other changes in v4.1.17]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2026-09-01 · OpenCode · [[Changes/OpenCode/2026-09-01-azure-cli-sign-in-now-asks-for-the-resource-name-directly-instead-of-querying-az|Azure CLI sign-in now asks for the resource name directly instead of querying Azure…]]
- Later: 2026-09-03 · Codex CLI · [[Changes/Codex CLI/2026-09-03-42128-https-github-com-openai-codex-pull-42128-prepare-mcp-connections-for-coord|♯42128((source link) Prepare MCP connections…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Notion · [[Changes/Notion/2020-07-28-sign-into-notion-with-your-apple-id-the-perfect-combination-of-speedy-and-secure|Sign into Notion with your Apple ID 🗝️ The perfect combination of speedy and secure]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20cline-2026-09-02-b0919c&body=Card%3A%20Changes%2FCline%2F2026-09-02-2-account-and-access-changes-in-v4-1-17.md%0ACard%20ID%3A%20cline-2026-09-02-b0919c%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fcline%2Fcline%2Freleases%2Ftag%2Fv4.1.17%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->