---
card_id: claude-code-2026-09-15-4f2ea2
date: '2026-09-15'
description: 'Claude Code · 2026-09-15 · Other changes: 8 changes in v2.1.273 — Improved
  the Artifact tool''s page read to state the capabilities and database rules the…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 618beeb7ea430d5cdae64b5ae3996a24b221886a45eb30af4ed5a22cea8ce1f3
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-09-15-4f2ea2
  comparison: ''
  date: '2026-09-15'
  description: 'Claude Code — v2.1.273: 8 other changes'
  evidence:
  - quote: Improved the Artifact tool's page read to state the capabilities and database
      rules the artifact service holds for the page, for anyone who can publish to
      it
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.273
  - quote: 'Improved artifact publishing: a publish whose connection drops after reaching
      claude.ai is now re-sent safely instead of failing or creating a duplicate version'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.273
  - quote: Improved the cloud-session GitHub error for an IP allow list, a suspended
      app installation or SAML single sign-on to show the cause instead of a generic
      install hint
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.273
  - quote: Improved `/autofix-pr` to say why GitHub webhook delivery couldn't be set
      up for the PR (for example, no linked GitHub account) instead of a generic warning
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.273
  - quote: 'Improved `/web-setup` errors: a refused GitHub token now lists the likely
      reasons and the fix, and a connection failure names a configured proxy or TLS
      certificate problem'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.273
  - quote: Improved the in-session SSL certificate and proxy connection errors to
      name the error code and what to fix, such as `NODE_EXTRA_CA_CERTS` for an untrusted
      corporate CA
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.273
  - quote: '[Claude Tag] Improved AWS connection failures: when a request can''t be
      signed, such as a hostname with no region, Claude is told why and how to fix
      it instead of a bare error'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.273
  - quote: '[Claude Tag] Changed Claude to start watching related public channels
      on its own, such as an incident channel a conversation depends on, instead of
      only when asked'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.273
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 8-other-changes-in-v2-1-273
  source_release: claude-code-2026-09-15-v2-1-273-github-389362239-6ea37826
  source_type: github_releases
  theme: uncategorized
  title: 8 other changes in v2.1.273
  type: change
source_release: '[[Releases/Claude Code/claude-code-2026-09-15-v2-1-273-github-389362239-6ea37826|claude-code-2026-09-15-v2-1-273-github-389362239-6ea37826]]'
source_type: github_releases
theme: uncategorized
title: 8 other changes in v2.1.273
type: change
---

<!-- chronolog:begin region="header" -->
# 8 other changes in v2.1.273

**Claude Code** · 2026-09-15 · Other changes · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.273) · from [[Releases/Claude Code/claude-code-2026-09-15-v2-1-273-github-389362239-6ea37826|v2.1.273]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Improved the Artifact tool's page read to state the capabilities and database rules the artifact service holds for the page, for anyone who can publish to it

> Improved artifact publishing: a publish whose connection drops after reaching claude.ai is now re-sent safely instead of failing or creating a duplicate version

> Improved the cloud-session GitHub error for an IP allow list, a suspended app installation or SAML single sign-on to show the cause instead of a generic install hint

> Improved `/autofix-pr` to say why GitHub webhook delivery couldn't be set up for the PR (for example, no linked GitHub account) instead of a generic warning

> Improved `/web-setup` errors: a refused GitHub token now lists the likely reasons and the fix, and a connection failure names a configured proxy or TLS certificate problem

> Improved the in-session SSL certificate and proxy connection errors to name the error code and what to fix, such as `NODE_EXTRA_CA_CERTS` for an untrusted corporate CA

> [Claude Tag] Improved AWS connection failures: when a request can't be signed, such as a hostname with no region, Claude is told why and how to fix it instead of a bare error

> [Claude Tag] Changed Claude to start watching related public channels on its own, such as an incident channel a conversation depends on, instead of only when asked

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.273
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-09-15-claude-code-on-the-web-improved-the-routine-detail-page-menu-and-rename-in-the-b|Claude Code on the web Improved the routine detail page]] · Interface Experience
- [[Changes/Claude Code/2026-09-15-improved-artifact-database-writes-an-update-can-now-remove-a-single-field-instea|Improved artifact database writes]] · Files and Data
- [[Changes/Claude Code/2026-09-15-5-safety-and-privacy-changes-in-v2-1-273|5 Safety and Privacy changes in v2.1.273]] · Safety and Privacy
- [[Changes/Claude Code/2026-09-15-3-apps-and-integrations-changes-in-v2-1-273|3 Apps and Integrations changes in v2.1.273]] · Apps and Integrations
- [[Changes/Claude Code/2026-09-15-changed-auto-mode-on-bedrock-vertex-and-foundry-to-use-the-local-classifier-by-d|Changed auto mode on Bedrock, Vertex and Foundry to use the local classifier…]] · Agent Mode
- [[Changes/Claude Code/2026-09-15-changed-bug-and-feedback-reports-to-include-only-model-behavior-params-model-sys|Changed /bug and /feedback reports to include only model-behavior params…]] · Model Support
- [[Changes/Claude Code/2026-09-15-claude-code-on-the-web-added-a-discard-unsaved-changes-confirmation-before-the-n|Claude Code on the web Added a "Discard unsaved changes?" confirmation before…]] · Editor Experience
- [[Changes/Claude Code/2026-09-15-4-account-and-access-changes-in-v2-1-273|4 Account and Access changes in v2.1.273]] · Account and Access
- [[Changes/Claude Code/2026-09-15-improved-responsiveness-in-long-sessions-hook-progress-and-sub-agent-activity-no|Improved responsiveness in long sessions]] · Reliability and Performance
- [[Changes/Claude Code/2026-09-15-added-x-claude-code-request-class-x-claude-code-agent-type-x-claude-code-prev-to|Added x-claude-code-request-class, x-claude-code-agent-type…]] · Context Window
- [[Changes/Claude Code/2026-09-15-claude-code-on-the-web-removed-the-full-page-desktop-app-download-screen-that-ne|Claude Code on the web Removed the full-page desktop-app download screen that new…]] · Mobile and Desktop
- [[Changes/Claude Code/2026-09-15-3-developer-workflow-changes-in-v2-1-273|3 Developer Workflow changes in v2.1.273]] · Developer Workflow
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-09-15-4f2ea2&body=Card%3A%20Changes%2FClaude%20Code%2F2026-09-15-8-other-changes-in-v2-1-273.md%0ACard%20ID%3A%20claude-code-2026-09-15-4f2ea2%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.273%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->