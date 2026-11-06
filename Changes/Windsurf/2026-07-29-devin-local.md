---
card_id: windsurf-2026-07-29-58da18
date: '2026-07-29'
description: 'Windsurf · 2026-07-29 · Memory and Personalization: Added a guided Cascade
  Migration Wizard that helps you migrate hooks, workflows, and memories, with…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom
    instructions are rolling out in beta]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1105
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: memory
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: launch
machine_hash: 05d5876cdf49cd5f7a3b29beacba6fe7db4b49ad63646aa99af87decd03ae1d4
product: windsurf
product_name: Windsurf
record:
  card_id: windsurf-2026-07-29-58da18
  comparison: ''
  date: '2026-07-29'
  description: 'Windsurf — v3.6.22: Added a guided Cascade Migration Wizard that helps
    you migrate hooks, workflows, and memories, with per-item selection, reviewable
    results, and a completion screen. The wizard skips archived memories and simplifies
    workflow migration choices.'
  evidence:
  - quote: Added a guided Cascade Migration Wizard that helps you migrate hooks, workflows,
      and memories, with per-item selection, reviewable results, and a completion
      screen. The wizard skips archived memories and simplifies workflow migration
      choices.
    source_release: https://docs.devin.ai/desktop/changelog#v3-6-22
  - quote: Devin Local customizations now includes a Plugins section where you can
      review, install, and remove plugins and see the skills, rules, hooks, and MCP
      servers they provide.
    source_release: https://docs.devin.ai/desktop/changelog#v3-6-22
  - quote: Added "Open customizations" entry points to the new-tab menu and Devin
      Local session context menu. Agent actions menus now show customization options
      that match the open session.
    source_release: https://docs.devin.ai/desktop/changelog#v3-6-22
  - quote: MCP servers from Devin CLI plugins and project-level configurations now
      appear in the Devin Local MCP UI, including multi-root workspaces. Servers that
      need authorization now have an **Authenticate** button to restart the OAuth
      flow.
    source_release: https://docs.devin.ai/desktop/changelog#v3-6-22
  - quote: Remote agent sessions can now open a browser preview inside Devin Desktop,
      with captured elements and console output available as pending context in the
      agent composer.
    source_release: https://docs.devin.ai/desktop/changelog#v3-6-22
  - quote: Models marked "Devin Local only" now appear disabled in Cascade's model
      picker with a tooltip directing you to Devin Local.
    source_release: https://docs.devin.ai/desktop/changelog#v3-6-22
  - quote: Implementing a plan now continues in its originating agent session when
      it is available, preserving the session's conversation context.
    source_release: https://docs.devin.ai/desktop/changelog#v3-6-22
  - quote: Editable run-command permission cards now use a quieter visual treatment,
      avoid layout shifts while editing, and support Enter to confirm, Shift+Enter
      for a newline, and Escape to cancel.
    source_release: https://docs.devin.ai/desktop/changelog#v3-6-22
  extractor_version: fallback-v5
  impact: incremental
  kind: launch
  product: windsurf
  product_name: Windsurf
  slug: devin-local
  source_release: windsurf-2026-07-29-v3-6-22-af7c57e7
  source_type: windsurf_changelog
  theme: memory
  theme_matches:
  - matched_terms:
    - completion
    score: 50
    theme: editor-experience
  - matched_terms:
    - memories
    score: 50
    theme: memory
  theme_resolution: manual-semantic-rule-v1
  title: Devin Local
  type: change
related_changes:
- '[[Changes/Dify/2026-07-28-test-use-sqlite-sessions-in-core-memory-by-asukaminato0721-in-https-github-com-l|test:
  use SQLite sessions in core memory]]'
- '[[Changes/Codex CLI/2026-07-29-35530-track-model-and-personality-in-world-state-copyberry|♯35530
  Track model and personality in world state @copyberry]]'
- '[[Changes/OpenHands/2026-07-29-feat-add-persistent-agent-memory-toggle-by-hieptl-in-https-github-com-openhands|feat:
  add persistent agent memory toggle]]'
source_release: '[[Releases/Windsurf/windsurf-2026-07-29-v3-6-22-af7c57e7|windsurf-2026-07-29-v3-6-22-af7c57e7]]'
source_type: windsurf_changelog
theme: memory
title: Devin Local
type: change
---

<!-- chronolog:begin region="header" -->
# Devin Local

**Windsurf** · 2026-07-29 · [[Themes/memory|Memory and Personalization]] · Launch · [Official source](https://docs.devin.ai/desktop/changelog#v3-6-22) · from [[Releases/Windsurf/windsurf-2026-07-29-v3-6-22-af7c57e7|v3.6.22]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added a guided Cascade Migration Wizard that helps you migrate hooks, workflows, and memories, with per-item selection, reviewable results, and a completion screen. The wizard skips archived memories and simplifies workflow migration choices.
>
> Devin Local customizations now includes a Plugins section where you can review, install, and remove plugins and see the skills, rules, hooks, and MCP servers they provide.
>
> Added "Open customizations" entry points to the new-tab menu and Devin Local session context menu. Agent actions menus now show customization options that match the open session.
>
> MCP servers from Devin CLI plugins and project-level configurations now appear in the Devin Local MCP UI, including multi-root workspaces. Servers that need authorization now have an **Authenticate** button to restart the OAuth flow.
>
> Remote agent sessions can now open a browser preview inside Devin Desktop, with captured elements and console output available as pending context in the agent composer.
>
> Models marked "Devin Local only" now appear disabled in Cascade's model picker with a tooltip directing you to Devin Local.
>
> Implementing a plan now continues in its originating agent session when it is available, preserving the session's conversation context.
>
> Editable run-command permission cards now use a quieter visual treatment, avoid layout shifts while editing, and support Enter to confirm, Shift+Enter for a newline, and Escape to cancel.
>
> Source: https://docs.devin.ai/desktop/changelog#v3-6-22
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Windsurf/2026-07-29-devin-desktop|Devin Desktop]] · Mobile and Desktop
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Memory and Personalization

- Earlier: 2026-07-29 · OpenHands · [[Changes/OpenHands/2026-07-29-feat-add-persistent-agent-memory-toggle-by-hieptl-in-https-github-com-openhands|feat: add persistent agent memory toggle]]
- Later: 2026-07-29 · Windsurf · [[Changes/Windsurf/2026-07-29-devin-local-8ab9ef|Devin Local]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-20 · ChatGPT · [[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom instructions are rolling out in beta]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20windsurf-2026-07-29-58da18&body=Card%3A%20Changes%2FWindsurf%2F2026-07-29-devin-local.md%0ACard%20ID%3A%20windsurf-2026-07-29-58da18%0ASource%3A%20https%3A%2F%2Fdocs.devin.ai%2Fdesktop%2Fchangelog%23v3-6-22%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->