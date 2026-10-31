---
card_id: cursor-2026-05-13-827fd1
date: '2026-05-13'
description: 'Cursor · 2026-05-13 · Developer Workflow: To make it easier to change,
  debug, and review environment definitions, we have improved Dockerfile-based…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1152
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: launch
machine_hash: 55340b2078de3201bb5922f3cb85a993aba3d74d41a350bdd9215c52d1018bf7
product: cursor
product_name: Cursor
record:
  card_id: cursor-2026-05-13-827fd1
  comparison: ''
  date: '2026-05-13'
  description: 'Cursor — Development environments for cloud agents: To make it easier
    to change, debug, and review environment definitions, we have improved Dockerfile-based
    configuration.'
  evidence:
  - quote: To make it easier to change, debug, and review environment definitions,
      we have improved Dockerfile-based configuration.
    source_release: https://cursor.com/changelog/05-13-26
  - quote: This includes support for build secrets, making it easy to securely access
      private package registries directly from your Dockerfiles. Build secrets are
      scoped to the build step and aren't passed to the running agent's environment.
    source_release: https://cursor.com/changelog/05-13-26
  - quote: We've also upgraded layer caching, so that only the updated layers of your
      image rebuild when you change the Dockerfile. Builds that hit the cache run
      70% faster.
    source_release: https://cursor.com/changelog/05-13-26
  extractor_version: fallback-v5
  impact: incremental
  kind: launch
  product: cursor
  product_name: Cursor
  slug: environment-configuration-as-code
  source_release: cursor-2026-05-13-3-4-https-cursor-com-changelog-05-13-26-685b1c4c
  source_type: cursor_changelog
  theme: developer-workflow
  theme_matches: []
  theme_resolution: manual-semantic-rule-v1
  title: Environment configuration as code
  type: change
related_changes:
- '[[Changes/Claude Code/2026-05-08-2-developer-workflow-changes-in-v2-1-136|2 Developer
  Workflow changes in v2.1.136]]'
- '[[Changes/Claude Code/2026-05-11-added-hook-args-string-field-exec-form-that-spawns-the-command-directly-without|Added
  hook args: string field (exec form) that spawns the command directly…]]'
- '[[Changes/Claude Code/2026-05-13-added-terminalsequence-field-to-hook-json-output-so-hooks-can-emit-desktop-notif|Added
  terminalSequence field to hook JSON output so hooks can emit desktop…]]'
source_release: '[[Releases/Cursor/cursor-2026-05-13-3-4-https-cursor-com-changelog-05-13-26-685b1c4c|cursor-2026-05-13-3-4-https-cursor-com-changelog-05-13-26-685b1c4c]]'
source_type: cursor_changelog
theme: developer-workflow
title: Environment configuration as code
type: change
---

<!-- chronolog:begin region="header" -->
# Environment configuration as code

**Cursor** · 2026-05-13 · [[Themes/developer-workflow|Developer Workflow]] · Launch · [Official source](https://cursor.com/changelog/05-13-26) · from [[Releases/Cursor/cursor-2026-05-13-3-4-https-cursor-com-changelog-05-13-26-685b1c4c|Development environments for cloud agents]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> To make it easier to change, debug, and review environment definitions, we have improved Dockerfile-based configuration.
>
> This includes support for build secrets, making it easy to securely access private package registries directly from your Dockerfiles. Build secrets are scoped to the build step and aren't passed to the running agent's environment.
>
> We've also upgraded layer caching, so that only the updated layers of your image rebuild when you change the Dockerfile. Builds that hit the cache run 70% faster.
>
> Source: https://cursor.com/changelog/05-13-26
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Cursor/2026-05-13-improved-agent-led-environment-setup|Improved agent-led environment setup]] · Agent Mode
- [[Changes/Cursor/2026-05-13-cloud-agents-and-automations-now-support-multi-repo-environments-building-off-ou|Multi-repo environments]] · Agent Mode
- [[Changes/Cursor/2026-05-13-environment-governance-and-security-controls|Environment governance and security controls]] · Safety and Privacy
- [[Changes/Cursor/2026-05-13-to-take-engineering-tasks-from-start-to-finish-agents-need-a-development-environ-e47512|To take engineering tasks from start to finish, agents need a development…]] · Agent Mode
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-05-13 · Claude Code · [[Changes/Claude Code/2026-05-13-added-terminalsequence-field-to-hook-json-output-so-hooks-can-emit-desktop-notif|Added terminalSequence field to hook JSON output so hooks can emit desktop…]]
- Later: 2026-05-13 · Cursor · [[Changes/Cursor/2026-05-13-removed-noisy-in-app-terminal-notifications-and-improved-shortcut-behavior|Removed noisy in-app terminal notifications and improved shortcut behavior]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-18 · Cursor · [[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20cursor-2026-05-13-827fd1&body=Card%3A%20Changes%2FCursor%2F2026-05-13-environment-configuration-as-code-827fd1.md%0ACard%20ID%3A%20cursor-2026-05-13-827fd1%0ASource%3A%20https%3A%2F%2Fcursor.com%2Fchangelog%2F05-13-26%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->