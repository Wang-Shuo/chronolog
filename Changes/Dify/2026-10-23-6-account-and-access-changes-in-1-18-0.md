---
card_id: dify-2026-10-23-d59284
date: '2026-10-23'
description: 'Dify · 2026-10-23 · Account and Access: 6 changes in v1.18.0 — Smarter
  Agent Routing, Portable Apps, Deeper Workflow Visibility — > **Read the upgrade
  guide…'
diffusion:
  first_in_tracked: "[[Changes/Notion/2020-07-28-sign-into-notion-with-your-apple-id-the-perfect-combination-of-speedy-and-secure|Sign
    into Notion with your Apple ID \U0001F5DD️ The perfect combination of speedy and
    secure]]"
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2278
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 1b02e7e5bbd41c15e3a2685c8a3ae5e7fad4f10758813528fbcde510580e24a9
product: dify
product_name: Dify
record:
  card_id: dify-2026-10-23-d59284
  comparison: ''
  date: '2026-10-23'
  description: 'Dify — v1.18.0 — Smarter Agent Routing, Portable Apps, Deeper Workflow
    Visibility: 6 Account and Access changes'
  evidence:
  - quote: '> **Read the upgrade guide below before deploying.** Upgrade the API,
      workers, Agent Backend, and Agent runtime images together. Local Agent sandboxes
      require a non-empty authentication token, and Agent Backend uses a new run protocol.
      Source installations require Python 3.13. Install the new difyctl client and
      sign in again. Preserve your existing `PASSWORD_PEPPER` configuration.'
    source_release: https://github.com/langgenius/dify/releases/tag/1.18.0
  - quote: The new client requires a fresh sign-in; see the deployment instructions
      below. (#43819)
    source_release: https://github.com/langgenius/dify/releases/tag/1.18.0
  - quote: 'Install the matching 1.18.0 client. Its v2 implementation does not reuse
      v1 login state:'
    source_release: https://github.com/langgenius/dify/releases/tag/1.18.0
  - quote: 'The CLI includes a `difyctl` skill for agents building Dify apps. Install
      it with `difyctl install skills <dir>`. Device login supports `--no-wait` and
      `--resume`, and folder uploads send one multipart part per file. (#43819, #44356)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.18.0
  - quote: 'Numeric zero and JSON object inputs keep their intended values. Browser-autofilled
      login credentials submit correctly, SSO failures are surfaced, and logout clears
      session state. (#43243, #42431, #44474, #43076, #43055)'
    source_release: https://github.com/langgenius/dify/releases/tag/1.18.0
  - quote: '| `OAUTH_TTL_DAYS` | Now read through application settings at startup,
      including `api/.env`. Default remains `14`, with the existing 1–365 day bounds.
      |'
    source_release: https://github.com/langgenius/dify/releases/tag/1.18.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 6-account-and-access-changes-in-1-18-0
  source_release: dify-2026-10-23-1-18-0-github-421489030-879b0613
  source_type: github_releases
  theme: account-access
  title: 6 Account and Access changes in 1.18.0
  type: change
related_changes:
- '[[Changes/OpenClaw/2026-10-22-mcp-sign-in-errors-now-give-a-safe-reason-and-tell-you-how-to-sign-in-or-fix-you|MCP
  sign-in errors now give a safe reason and tell you how to sign in or fix…]]'
- '[[Changes/Codex CLI/2026-10-23-24-account-and-access-changes-in-rust-v0-164-0|24
  Account and Access changes in rust-v0.164.0]]'
- '[[Changes/Codex CLI/2026-10-23-the-amazon-bedrock-setup-wizard-is-now-enabled-by-default-with-api-key-entry-gro|The
  Amazon Bedrock setup wizard is now enabled by default, with API key entry…]]'
source_release: '[[Releases/Dify/dify-2026-10-23-1-18-0-github-421489030-879b0613|dify-2026-10-23-1-18-0-github-421489030-879b0613]]'
source_type: github_releases
theme: account-access
title: 6 Account and Access changes in 1.18.0
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Account and Access changes in 1.18.0

**Dify** · 2026-10-23 · [[Themes/account-access|Account and Access]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/1.18.0) · from [[Releases/Dify/dify-2026-10-23-1-18-0-github-421489030-879b0613|v1.18.0 — Smarter Agent Routing, Portable Apps, Deeper Workflow Visibility]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> > **Read the upgrade guide below before deploying.** Upgrade the API, workers, Agent Backend, and Agent runtime images together. Local Agent sandboxes require a non-empty authentication token, and Agent Backend uses a new run protocol. Source installations require Python 3.13. Install the new difyctl client and sign in again. Preserve your existing `PASSWORD_PEPPER` configuration.

> The new client requires a fresh sign-in; see the deployment instructions below. (#43819)

> Install the matching 1.18.0 client. Its v2 implementation does not reuse v1 login state:

> The CLI includes a `difyctl` skill for agents building Dify apps. Install it with `difyctl install skills <dir>`. Device login supports `--no-wait` and `--resume`, and folder uploads send one multipart part per file. (#43819, #44356)

> Numeric zero and JSON object inputs keep their intended values. Browser-autofilled login credentials submit correctly, SSO failures are surfaced, and logout clears session state. (#43243, #42431, #44474, #43076, #43055)

> | `OAUTH_TTL_DAYS` | Now read through application settings at startup, including `api/.env`. Default remains `14`, with the existing 1–365 day bounds. |

Source: https://github.com/langgenius/dify/releases/tag/1.18.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2026-10-23-respect-xforward-headers-enabled-standalone-api-default-remains-false-bundled-co| /  RESPECT_XFORWARD_HEADERS_ENABLED  /  Standalone API default remains false]] · Developer Workflow
- [[Changes/Dify/2026-10-23-3-memory-and-personalization-changes-in-1-18-0|3 Memory and Personalization changes in 1.18.0]] · Memory and Personalization
- [[Changes/Dify/2026-10-23-3-accessibility-and-localization-changes-in-1-18-0|3 Accessibility and Localization changes in 1.18.0]] · Accessibility and Localization
- [[Changes/Dify/2026-10-23-3-context-window-changes-in-1-18-0|3 Context Window changes in 1.18.0]] · Context Window
- [[Changes/Dify/2026-10-23-operations-archive-storage-supports-configurable-s3-addressing-style-the-api-ima|Operations: archive storage supports configurable S3 addressing style]] · Model Support
- [[Changes/Dify/2026-10-23-2-interface-experience-changes-in-1-18-0|2 Interface Experience changes in 1.18.0]] · Interface Experience
- [[Changes/Dify/2026-10-23-3-editor-experience-changes-in-1-18-0|3 Editor Experience changes in 1.18.0]] · Editor Experience
- [[Changes/Dify/2026-10-23-32-agent-mode-changes-in-1-18-0|32 Agent Mode changes in 1.18.0]] · Agent Mode
- [[Changes/Dify/2026-10-23-11-safety-and-privacy-changes-in-1-18-0|11 Safety and Privacy changes in 1.18.0]] · Safety and Privacy
- [[Changes/Dify/2026-10-23-14-apps-and-integrations-changes-in-1-18-0|14 Apps and Integrations changes in 1.18.0]] · Apps and Integrations
- [[Changes/Dify/2026-10-23-2-reliability-and-performance-changes-in-1-18-0|2 Reliability and Performance changes in 1.18.0]] · Reliability and Performance
- [[Changes/Dify/2026-10-23-5-collaboration-changes-in-1-18-0|5 Collaboration changes in 1.18.0]] · Collaboration
- [[Changes/Dify/2026-10-23-8-files-and-data-changes-in-1-18-0|8 Files and Data changes in 1.18.0]] · Files and Data
- [[Changes/Dify/2026-10-23-2-automation-and-scheduling-changes-in-1-18-0|2 Automation and Scheduling changes in 1.18.0]] · Automation and Scheduling
- [[Changes/Dify/2026-10-23-81-other-changes-in-1-18-0|81 other changes in 1.18.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2026-10-23 · Codex CLI · [[Changes/Codex CLI/2026-10-23-the-amazon-bedrock-setup-wizard-is-now-enabled-by-default-with-api-key-entry-gro|The Amazon Bedrock setup wizard is now enabled by default, with API key entry…]]
- Later: 2026-10-24 · Windsurf · [[Changes/Windsurf/2026-10-24-a-saved-sign-in-keeps-working-after-updating-on-machines-where-the-editor-s-own|A saved sign-in keeps working after updating on machines where the editor's own…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Notion · [[Changes/Notion/2020-07-28-sign-into-notion-with-your-apple-id-the-perfect-combination-of-speedy-and-secure|Sign into Notion with your Apple ID 🗝️ The perfect combination of speedy and secure]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2026-10-23-d59284&body=Card%3A%20Changes%2FDify%2F2026-10-23-6-account-and-access-changes-in-1-18-0.md%0ACard%20ID%3A%20dify-2026-10-23-d59284%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F1.18.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->