---
card_id: claude-code-2026-08-07-e93f80
date: '2026-08-07'
description: 'Claude Code · 2026-08-07 · Safety and Privacy: 2 changes in v2.1.224
  — Added sandbox credential-masking options: `extract` and `onExtractNoMatch` for…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1209
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 14ce20bba8c986a729c9fd6490d9b72e5382dbd5f8a1379f1cd1cbc96afde01f
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-08-07-e93f80
  comparison: ''
  date: '2026-08-07'
  description: 'Claude Code — v2.1.224: 2 Safety and Privacy changes'
  evidence:
  - quote: 'Added sandbox credential-masking options: `extract` and `onExtractNoMatch`
      for structured env values, `decode: "jwt"` with `maskClaims` for JWT-aware masking,
      and `awsPairs`/`sigv4` for AWS SigV4 re-signing; these need `network.tlsTerminate`
      and are honored only from user, managed, or `--settings` settings'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.224
  - quote: 'Changed the feedback-survey transcript share: with your consent it now
      also uploads the last request''s model settings — the system prompt (which includes
      your `CLAUDE.md` instructions), tool definitions, and model parameters. Secrets
      are redacted as before, and these fields are dropped first if the share is too
      large'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.224
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 2-safety-and-privacy-changes-in-v2-1-224
  source_release: claude-code-2026-08-07-v2-1-224-github-366468634-0ab9e64c
  source_type: github_releases
  theme: safety-privacy
  title: 2 Safety and Privacy changes in v2.1.224
  type: change
related_changes:
- '[[Changes/Claude Code/2026-08-04-improved-auto-mode-safety-messages-sent-to-other-agent-sessions-via-sendmessage|Improved
  auto mode safety]]'
- '[[Changes/Claude Code/2026-08-04-7-safety-and-privacy-changes-in-v2-1-221|7 Safety
  and Privacy changes in v2.1.221]]'
- '[[Changes/Claude Code/2026-08-06-3-safety-and-privacy-changes-in-v2-1-223|3 Safety
  and Privacy changes in v2.1.223]]'
source_release: '[[Releases/Claude Code/claude-code-2026-08-07-v2-1-224-github-366468634-0ab9e64c|claude-code-2026-08-07-v2-1-224-github-366468634-0ab9e64c]]'
source_type: github_releases
theme: safety-privacy
title: 2 Safety and Privacy changes in v2.1.224
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Safety and Privacy changes in v2.1.224

**Claude Code** · 2026-08-07 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.224) · from [[Releases/Claude Code/claude-code-2026-08-07-v2-1-224-github-366468634-0ab9e64c|v2.1.224]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added sandbox credential-masking options: `extract` and `onExtractNoMatch` for structured env values, `decode: "jwt"` with `maskClaims` for JWT-aware masking, and `awsPairs`/`sigv4` for AWS SigV4 re-signing; these need `network.tlsTerminate` and are honored only from user, managed, or `--settings` settings

> Changed the feedback-survey transcript share: with your consent it now also uploads the last request's model settings — the system prompt (which includes your `CLAUDE.md` instructions), tool definitions, and model parameters. Secrets are redacted as before, and these fields are dropped first if the share is too large

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.224
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-08-07-changed-managed-settings-the-approval-prompt-no-longer-re-appears-after-re-login|Changed managed settings]] · Account and Access
- [[Changes/Claude Code/2026-08-07-added-a-cancel-and-confirm-step-when-removing-an-unavailable-paste-changes-a-com|Added a cancel-and-confirm step when removing an unavailable paste changes…]] · Developer Workflow
- [[Changes/Claude Code/2026-08-07-improved-fullscreen-mode-to-keep-the-full-pre-compaction-history-in-scrollback-a|Improved fullscreen mode to keep the full pre-compaction history in scrollback…]] · Interface Experience
- [[Changes/Claude Code/2026-08-07-3-apps-and-integrations-changes-in-v2-1-224|3 Apps and Integrations changes in v2.1.224]] · Apps and Integrations
- [[Changes/Claude Code/2026-08-07-3-mobile-and-desktop-changes-in-v2-1-224|3 Mobile and Desktop changes in v2.1.224]] · Mobile and Desktop
- [[Changes/Claude Code/2026-08-07-removed-the-200-subagent-per-session-spawn-cap-long-running-sessions-no-longer-r|Removed the 200-subagent-per-session spawn cap]] · Agent Mode
- [[Changes/Claude Code/2026-08-07-changed-the-bash-tool-description-to-always-note-that-command-output-is-displaye|Changed the Bash tool description to always note that command output is displayed…]] · Model Support
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-08-06 · Claude Code · [[Changes/Claude Code/2026-08-06-3-safety-and-privacy-changes-in-v2-1-223|3 Safety and Privacy changes in v2.1.223]]
- Later: 2026-08-08 · Claude Code · [[Changes/Claude Code/2026-08-08-2-safety-and-privacy-changes-in-v2-1-225|2 Safety and Privacy changes in v2.1.225]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-08-07-e93f80&body=Card%3A%20Changes%2FClaude%20Code%2F2026-08-07-2-safety-and-privacy-changes-in-v2-1-224.md%0ACard%20ID%3A%20claude-code-2026-08-07-e93f80%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.224%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->