---
card_id: github-copilot-cli-2026-08-03-28ca73
date: '2026-08-03'
description: 'GitHub Copilot CLI · 2026-08-03 · Other changes: 9 changes in 1.0.78
  — Timeline headers show how long each tool call took, right-aligned and ticking
  live while…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: d94d17575b2b651f3d8459ecd78360b9ff18ac14ac91209305d4a89d0fdeeb2b
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-08-03-28ca73
  comparison: ''
  date: '2026-08-03'
  description: 'GitHub Copilot CLI — 1.0.78: 9 other changes'
  evidence:
  - quote: Timeline headers show how long each tool call took, right-aligned and ticking
      live while it runs (for calls of at least 5 seconds). On by default — disable
      with `/settings showToolDurations`.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.78
  - quote: Inline images no longer render with their first row repeated down the whole
      picture after the timeline scrolls
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.78
  - quote: Expose token usage in ACP prompt results and live usage_update notifications
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.78
  - quote: Added a forceRemoteSettingsRefresh managed setting that requires a fresh
      managed-settings fetch on startup
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.78
  - quote: Managed settings now fall back to the persistent cache whenever a server-managed
      settings fetch fails for any reason (network error, a non-success HTTP status,
      or a malformed/unparseable response), and fail open — starting without the unconfirmed
      server restriction rather than the prior fail-closed behavior — when no usable
      cached policy is available
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.78
  - quote: Add /permissions to switch between approval modes.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.78
  - quote: ACP mode supports closing sessions with the closeSession request.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.78
  - quote: Warn on startup about unknown top-level keys in user settings.json (e.g.
      a misspelled setting) instead of silently ignoring them
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.78
  - quote: Render long session transcripts progressively to keep scrolling responsive
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.78
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 9-other-changes-in-v1-0-78
  source_release: github-copilot-cli-2026-08-03-v1-0-78-github-364543196-53a079bc
  source_type: github_releases
  theme: uncategorized
  title: 9 other changes in v1.0.78
  type: change
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-08-03-v1-0-78-github-364543196-53a079bc|github-copilot-cli-2026-08-03-v1-0-78-github-364543196-53a079bc]]'
source_type: github_releases
theme: uncategorized
title: 9 other changes in v1.0.78
type: change
---

<!-- chronolog:begin region="header" -->
# 9 other changes in v1.0.78

**GitHub Copilot CLI** · 2026-08-03 · Other changes · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.78) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-08-03-v1-0-78-github-364543196-53a079bc|1.0.78]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Timeline headers show how long each tool call took, right-aligned and ticking live while it runs (for calls of at least 5 seconds). On by default — disable with `/settings showToolDurations`.

> Inline images no longer render with their first row repeated down the whole picture after the timeline scrolls

> Expose token usage in ACP prompt results and live usage_update notifications

> Added a forceRemoteSettingsRefresh managed setting that requires a fresh managed-settings fetch on startup

> Managed settings now fall back to the persistent cache whenever a server-managed settings fetch fails for any reason (network error, a non-success HTTP status, or a malformed/unparseable response), and fail open — starting without the unconfirmed server restriction rather than the prior fail-closed behavior — when no usable cached policy is available

> Add /permissions to switch between approval modes.

> ACP mode supports closing sessions with the closeSession request.

> Warn on startup about unknown top-level keys in user settings.json (e.g. a misspelled setting) instead of silently ignoring them

> Render long session transcripts progressively to keep scrolling responsive

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.78
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-08-03-4-apps-and-integrations-changes-in-v1-0-78|4 Apps and Integrations changes in v1.0.78]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-08-03-a-run-whose-prompt-is-piped-over-stdin-now-treats-its-sessionend-hook-the-same-w|A run whose prompt is piped over stdin now treats its sessionEnd hook the same way…]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-08-03-2-editor-experience-changes-in-v1-0-78|2 Editor Experience changes in v1.0.78]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-08-03-resuming-a-long-session-is-dramatically-faster-and-far-lighter-on-memory-because|Resuming a long session is dramatically faster and far lighter on memory, because…]] · Reliability and Performance
- [[Changes/GitHub Copilot CLI/2026-08-03-2-account-and-access-changes-in-v1-0-78|2 Account and Access changes in v1.0.78]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-08-03-the-allow-all-auto-safety-judge-model-is-no-longer-user-configurable-the-judge-m|The /allow-all auto safety-judge model is no longer user-configurable]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-08-03-2-interface-experience-changes-in-v1-0-78|2 Interface Experience changes in v1.0.78]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-08-03-3-safety-and-privacy-changes-in-v1-0-78|3 Safety and Privacy changes in v1.0.78]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-08-03-2-developer-workflow-changes-in-v1-0-78|2 Developer Workflow changes in v1.0.78]] · Developer Workflow
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-08-03-28ca73&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-08-03-9-other-changes-in-v1-0-78.md%0ACard%20ID%3A%20github-copilot-cli-2026-08-03-28ca73%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.78%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->