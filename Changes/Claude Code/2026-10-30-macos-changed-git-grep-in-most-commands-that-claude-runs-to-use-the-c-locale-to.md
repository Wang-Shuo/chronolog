---
card_id: claude-code-2026-10-30-76ae16
date: '2026-10-30'
description: 'Claude Code · 2026-10-30 · Reliability and Performance: macOS: Changed
  `git grep` in most commands that Claude runs to use the C locale, to avoid a reported…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General
    performance: Among other improvements, users will notice that ChatGPT is now…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1415
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: change
machine_hash: 44b480cfd6df9ea727926bc706943053c75c59ba331ceab84c1404ebd5a38132
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-10-30-76ae16
  comparison: ''
  date: '2026-10-30'
  description: 'Claude Code — v2.1.314: macOS: Changed `git grep` in most commands
    that Claude runs to use the C locale, to avoid a reported memory leak in macOS''s
    regex library on files that aren''t valid UTF-8'
  evidence:
  - quote: 'macOS: Changed `git grep` in most commands that Claude runs to use the
      C locale, to avoid a reported memory leak in macOS''s regex library on files
      that aren''t valid UTF-8'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.314
  extractor_version: fallback-v5
  impact: incremental
  kind: change
  product: claude-code
  product_name: Claude Code
  slug: macos-changed-git-grep-in-most-commands-that-claude-runs-to-use-the-c-locale-to
  source_release: claude-code-2026-10-30-v2-1-314-github-428518421-b7ac83d7
  source_type: github_releases
  theme: reliability-performance
  theme_matches:
  - matched_terms:
    - memory
    score: 110
    theme: memory
  - matched_terms:
    - macos
    score: 50
    theme: mobile-desktop
  theme_resolution: manual-semantic-rule-v2
  title: 'macOS: Changed `git grep` in most commands that Claude runs to use the C
    locale…'
  type: change
related_changes:
- '[[Changes/Cursor/2026-10-16-larger-faster-environments|Larger, faster environments]]'
- '[[Changes/Claude Code/2026-10-19-improved-responsiveness-and-throughput-when-many-subagents-are-running-at-the-sa|Improved
  responsiveness and throughput when many subagents are running at the same time]]'
- '[[Changes/Claude Code/2026-10-22-2-reliability-and-performance-changes-in-v2-1-309|2
  Reliability and Performance changes in v2.1.309]]'
source_release: '[[Releases/Claude Code/claude-code-2026-10-30-v2-1-314-github-428518421-b7ac83d7|claude-code-2026-10-30-v2-1-314-github-428518421-b7ac83d7]]'
source_type: github_releases
theme: reliability-performance
title: 'macOS: Changed git grep in most commands that Claude runs to use the C locale…'
type: change
---

<!-- chronolog:begin region="header" -->
# macOS: Changed `git grep` in most commands that Claude runs to use the C locale…

**Claude Code** · 2026-10-30 · [[Themes/reliability-performance|Reliability and Performance]] · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.314) · from [[Releases/Claude Code/claude-code-2026-10-30-v2-1-314-github-428518421-b7ac83d7|v2.1.314]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> macOS: Changed `git grep` in most commands that Claude runs to use the C locale, to avoid a reported memory leak in macOS's regex library on files that aren't valid UTF-8
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.314
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-10-30-3-agent-mode-changes-in-v2-1-314|3 Agent Mode changes in v2.1.314]] · Agent Mode
- [[Changes/Claude Code/2026-10-30-improved-permissions-review-tab-now-called-recently-blocked-the-footer-says-what|Improved /permissions review tab, now called Recently blocked]] · Editor Experience
- [[Changes/Claude Code/2026-10-30-3-enterprise-and-administration-changes-in-v2-1-314|3 Enterprise and Administration changes in v2.1.314]] · Enterprise and Administration
- [[Changes/Claude Code/2026-10-30-4-developer-workflow-changes-in-v2-1-314|4 Developer Workflow changes in v2.1.314]] · Developer Workflow
- [[Changes/Claude Code/2026-10-30-2-model-support-changes-in-v2-1-314|2 Model Support changes in v2.1.314]] · Model Support
- [[Changes/Claude Code/2026-10-30-improved-the-cloud-session-error-shown-while-a-request-refused-for-your-claude-a|Improved the cloud session error shown while a request refused for your claude.ai…]] · Account and Access
- [[Changes/Claude Code/2026-10-30-3-apps-and-integrations-changes-in-v2-1-314|3 Apps and Integrations changes in v2.1.314]] · Apps and Integrations
- [[Changes/Claude Code/2026-10-30-10-safety-and-privacy-changes-in-v2-1-314|10 Safety and Privacy changes in v2.1.314]] · Safety and Privacy
- [[Changes/Claude Code/2026-10-30-2-memory-and-personalization-changes-in-v2-1-314|2 Memory and Personalization changes in v2.1.314]] · Memory and Personalization
- [[Changes/Claude Code/2026-10-30-3-mobile-and-desktop-changes-in-v2-1-314|3 Mobile and Desktop changes in v2.1.314]] · Mobile and Desktop
- [[Changes/Claude Code/2026-10-30-10-other-changes-in-v2-1-314|10 other changes in v2.1.314]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Reliability and Performance

- Earlier: 2026-10-22 · Claude Code · [[Changes/Claude Code/2026-10-22-2-reliability-and-performance-changes-in-v2-1-309|2 Reliability and Performance changes in v2.1.309]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2022-12-15 · ChatGPT · [[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General performance: Among other improvements, users will notice that ChatGPT is now…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-10-30-76ae16&body=Card%3A%20Changes%2FClaude%20Code%2F2026-10-30-macos-changed-git-grep-in-most-commands-that-claude-runs-to-use-the-c-locale-to.md%0ACard%20ID%3A%20claude-code-2026-10-30-76ae16%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.314%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->