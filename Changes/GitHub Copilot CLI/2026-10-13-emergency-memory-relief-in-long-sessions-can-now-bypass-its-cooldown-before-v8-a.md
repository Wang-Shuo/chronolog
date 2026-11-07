---
card_id: github-copilot-cli-2026-10-13-aa2f69
date: '2026-10-13'
description: 'GitHub Copilot CLI · 2026-10-13 · Reliability and Performance: Emergency
  memory relief in long sessions can now bypass its cooldown before V8 aborts, so
  a…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General
    performance: Among other improvements, users will notice that ChatGPT is now…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1398
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: reliability-performance
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: change
machine_hash: 125fa65b1e0524e8cb98fc32b950de74f3128c308361c9a0a17946597d5e4c8e
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-10-13-aa2f69
  comparison: ''
  date: '2026-10-13'
  description: 'GitHub Copilot CLI — 1.0.97: Emergency memory relief in long sessions
    can now bypass its cooldown before V8 aborts, so a session that would have been
    killed by a JavaScript heap out of memory crash may survive with compacted history
    instead'
  evidence:
  - quote: Emergency memory relief in long sessions can now bypass its cooldown before
      V8 aborts, so a session that would have been killed by a JavaScript heap out
      of memory crash may survive with compacted history instead
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.97
  extractor_version: fallback-v5
  impact: incremental
  kind: change
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: emergency-memory-relief-in-long-sessions-can-now-bypass-its-cooldown-before-v8-a
  source_release: github-copilot-cli-2026-10-13-v1-0-97-github-411990782-ee7b7038
  source_type: github_releases
  theme: reliability-performance
  theme_matches: []
  theme_resolution: manual-semantic-rule-v2
  title: Emergency memory relief in long sessions can now bypass its cooldown before
    V8…
  type: change
related_changes:
- '[[Changes/OpenClaw/2026-10-10-2-reliability-and-performance-changes-in-v2026-10-1|2
  Reliability and Performance changes in v2026.10.1]]'
- '[[Changes/Ollama/2026-10-11-paused-background-model-upgrade-for-embedding-and-other-request-performance-by-j|Paused
  background model upgrade for embedding and other request performance,]]'
- '[[Changes/Ollama/2026-10-12-2-reliability-and-performance-changes-in-v0-40-4|2
  Reliability and Performance changes in v0.40.4]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-10-13-v1-0-97-github-411990782-ee7b7038|github-copilot-cli-2026-10-13-v1-0-97-github-411990782-ee7b7038]]'
source_type: github_releases
theme: reliability-performance
title: Emergency memory relief in long sessions can now bypass its cooldown before
  V8…
type: change
---

<!-- chronolog:begin region="header" -->
# Emergency memory relief in long sessions can now bypass its cooldown before V8…

**GitHub Copilot CLI** · 2026-10-13 · [[Themes/reliability-performance|Reliability and Performance]] · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.97) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-10-13-v1-0-97-github-411990782-ee7b7038|1.0.97]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Emergency memory relief in long sessions can now bypass its cooldown before V8 aborts, so a session that would have been killed by a JavaScript heap out of memory crash may survive with compacted history instead
>
> Source: https://github.com/github/copilot-cli/releases/tag/v1.0.97
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-10-13-background-shell-wait-status-no-longer-animates-when-no-foreground-work-is-runni|Background-shell wait status no longer animates when no foreground work is running]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-10-13-3-safety-and-privacy-changes-in-v1-0-97|3 Safety and Privacy changes in v1.0.97]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-10-13-show-billed-ai-credits-in-usage-for-token-billed-sessions-including-after-resume|Show billed AI Credits in /usage for token-billed sessions, including after resume]] · Pricing Model
- [[Changes/GitHub Copilot CLI/2026-10-13-synchronous-task-json-output-now-includes-failed-child-error-and-lifecycle-event|Synchronous /task JSON output now includes failed child error and lifecycle events…]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-10-13-3-agent-mode-changes-in-v1-0-97|3 Agent Mode changes in v1.0.97]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-10-13-4-apps-and-integrations-changes-in-v1-0-97|4 Apps and Integrations changes in v1.0.97]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-10-13-power-bi-and-bluebird-mcp-servers-accept-their-published-resource-scopes-during|Power BI and Bluebird MCP servers accept their published resource scopes during sign-in]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-10-13-8-other-changes-in-v1-0-97|8 other changes in v1.0.97]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Reliability and Performance

- Earlier: 2026-10-12 · Ollama · [[Changes/Ollama/2026-10-12-2-reliability-and-performance-changes-in-v0-40-4|2 Reliability and Performance changes in v0.40.4]]
- Later: 2026-10-14 · Claude Code · [[Changes/Claude Code/2026-10-14-improved-memory-and-disk-use-when-pdfs-are-mentioned-their-bytes-are-no-longer-k|Improved memory and disk use when PDFs are @-mentioned]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2022-12-15 · ChatGPT · [[Changes/ChatGPT/2022-12-15-general-performance-among-other-improvements-users-will-notice-that-chatgpt-is-n|General performance: Among other improvements, users will notice that ChatGPT is now…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-10-13-aa2f69&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-10-13-emergency-memory-relief-in-long-sessions-can-now-bypass-its-cooldown-before-v8-a.md%0ACard%20ID%3A%20github-copilot-cli-2026-10-13-aa2f69%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.97%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->