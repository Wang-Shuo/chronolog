---
card_id: windsurf-2026-07-29-8ab9ef
date: '2026-07-29'
description: 'Windsurf · 2026-07-29 · Memory and Personalization: New "Devin: Open
  Cascade Migration Wizard" command opens a guided wizard that chains hooks → skills
  →…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom
    instructions are rolling out in beta]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1105
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: memory
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: significant
kind: launch
machine_hash: b5fe1a53e2a95ce75268552ae50ad9e9cd3191047ef3be39e5b040469cf56a3d
product: windsurf
product_name: Windsurf
record:
  ai_generated: true
  card_id: windsurf-2026-07-29-8ab9ef
  comparison: ''
  confidence: low
  date: '2026-07-29'
  description: 'Windsurf — v3.6.21: New "Devin: Open Cascade Migration Wizard" command
    opens a guided wizard that chains hooks → skills → memories migration in one flow,
    with per-item opt-in and dry-run previews.'
  evidence:
  - quote: 'New "Devin: Open Cascade Migration Wizard" command opens a guided wizard
      that chains hooks → skills → memories migration in one flow, with per-item opt-in
      and dry-run previews.'
    source_release: https://docs.devin.ai/desktop/changelog#v3-6-21
  - quote: 'Plan mode now works like Cascade''s: the agent researches with read-only
      commands, keeps a persistent Markdown plan file at `~/.devin/plans/plan-<session>.md`,
      and asks for approval before implementing.'
    source_release: https://docs.devin.ai/desktop/changelog#v3-6-21
  - quote: Worktree sessions now show a **Merge** button to bring their changes back
      into the workspace, and you can pick an existing worktree from the agent location
      selector's Local submenu.
    source_release: https://docs.devin.ai/desktop/changelog#v3-6-21
  - quote: New tabs now default to Devin Local when you haven't chosen a preferred
      agent (falling back to Cascade if it isn't available), and Local is selectable
      in the agent selector while it's still connecting.
    source_release: https://docs.devin.ai/desktop/changelog#v3-6-21
  - quote: '`Megaplan` now work in Devin Local, switching the session into Plan mode
      and prompting the agent to plan first.'
    source_release: https://docs.devin.ai/desktop/changelog#v3-6-21
  - quote: 'Editable command approvals: click a command in a permission card to edit
      it before approving, or use the wand action to describe a change in plain language
      and have a fast model rewrite it for review.'
    source_release: https://docs.devin.ai/desktop/changelog#v3-6-21
  - quote: Queued messages can now be edited before they send, and editing or reverting
      a prompt preserves file, directory, skill, and terminal @-mentions.
    source_release: https://docs.devin.ai/desktop/changelog#v3-6-21
  - quote: Added Rules to the @-mention menu so you can pull a manual-trigger rule
      into a conversation.
    source_release: https://docs.devin.ai/desktop/changelog#v3-6-21
  - quote: Added a "Duplicate session" action to the response footer to branch off
      a conversation, and a "Subagents (Preview)" toggle in Devin settings.
    source_release: https://docs.devin.ai/desktop/changelog#v3-6-21
  - quote: Custom subagents can now be defined as flat `agents/<name>.md` files, and
      per-agent directories also accept `AGENTS.md`, `agent.md`, and `agents.md`.
    source_release: https://docs.devin.ai/desktop/changelog#v3-6-21
  - quote: Response statistics now appear reliably after every turn.
    source_release: https://docs.devin.ai/desktop/changelog#v3-6-21
  - quote: With "Agent Diff Zones" turned off, Devin Local no longer opens edited
      files in the background, and closing the last Devin Local tab now opens a fresh
      session instead of closing the panel.
    source_release: https://docs.devin.ai/desktop/changelog#v3-6-21
  - quote: Fixed permission rules written with relative globs (e.g. `Read(**/*.pem)`)
      being pinned to the directory the CLI was launched from, so they now apply under
      every workspace directory and pick up directories added mid-session.
    source_release: https://docs.devin.ai/desktop/changelog#v3-6-21
  - quote: Session permission grants and mode switches answered on a subagent's prompt
      now apply to the whole session, so the root agent and sibling subagents no longer
      re-prompt for a scope you already granted.
    source_release: https://docs.devin.ai/desktop/changelog#v3-6-21
  extractor_version: fallback-v5
  impact: significant
  kind: launch
  product: windsurf
  product_name: Windsurf
  slug: devin-local
  source_release: windsurf-2026-07-29-v3-6-21-93635c87
  source_type: windsurf_changelog
  theme: memory
  title: Devin Local
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-07-29-35530-track-model-and-personality-in-world-state-copyberry|♯35530
  Track model and personality in world state @copyberry]]'
- '[[Changes/OpenHands/2026-07-29-feat-add-persistent-agent-memory-toggle-by-hieptl-in-https-github-com-openhands|feat:
  add persistent agent memory toggle]]'
- '[[Changes/Windsurf/2026-07-29-devin-local|Devin Local]]'
source_release: '[[Releases/Windsurf/windsurf-2026-07-29-v3-6-21-93635c87|windsurf-2026-07-29-v3-6-21-93635c87]]'
source_type: windsurf_changelog
theme: memory
title: Devin Local
type: change
---

<!-- chronolog:begin region="header" -->
# Devin Local

**Windsurf** · 2026-07-29 · [[Themes/memory|Memory and Personalization]] · Launch · [Official source](https://docs.devin.ai/desktop/changelog#v3-6-21) · from [[Releases/Windsurf/windsurf-2026-07-29-v3-6-21-93635c87|v3.6.21]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> New "Devin: Open Cascade Migration Wizard" command opens a guided wizard that chains hooks → skills → memories migration in one flow, with per-item opt-in and dry-run previews.
>
> Plan mode now works like Cascade's: the agent researches with read-only commands, keeps a persistent Markdown plan file at `~/.devin/plans/plan-<session>.md`, and asks for approval before implementing.
>
> Worktree sessions now show a **Merge** button to bring their changes back into the workspace, and you can pick an existing worktree from the agent location selector's Local submenu.
>
> New tabs now default to Devin Local when you haven't chosen a preferred agent (falling back to Cascade if it isn't available), and Local is selectable in the agent selector while it's still connecting.
>
> `Megaplan` now work in Devin Local, switching the session into Plan mode and prompting the agent to plan first.
>
> Editable command approvals: click a command in a permission card to edit it before approving, or use the wand action to describe a change in plain language and have a fast model rewrite it for review.
>
> Queued messages can now be edited before they send, and editing or reverting a prompt preserves file, directory, skill, and terminal @-mentions.
>
> Added Rules to the @-mention menu so you can pull a manual-trigger rule into a conversation.
>
> Added a "Duplicate session" action to the response footer to branch off a conversation, and a "Subagents (Preview)" toggle in Devin settings.
>
> Custom subagents can now be defined as flat `agents/<name>.md` files, and per-agent directories also accept `AGENTS.md`, `agent.md`, and `agents.md`.
>
> Response statistics now appear reliably after every turn.
>
> With "Agent Diff Zones" turned off, Devin Local no longer opens edited files in the background, and closing the last Devin Local tab now opens a fresh session instead of closing the panel.
>
> Fixed permission rules written with relative globs (e.g. `Read(**/*.pem)`) being pinned to the directory the CLI was launched from, so they now apply under every workspace directory and pick up directories added mid-session.
>
> Session permission grants and mode switches answered on a subagent's prompt now apply to the whole session, so the root agent and sibling subagents no longer re-prompt for a scope you already granted.
>
> Source: https://docs.devin.ai/desktop/changelog#v3-6-21
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Windsurf/2026-07-29-devin-cloud|Devin Cloud]] · Reliability and Performance
- [[Changes/Windsurf/2026-07-29-devin-desktop-9e1a9d|Devin Desktop]] · Mobile and Desktop
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Memory and Personalization

- Earlier: 2026-07-29 · Windsurf · [[Changes/Windsurf/2026-07-29-devin-local|Devin Local]]
- Later: 2026-07-30 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-07-30-a-userpromptsubmitted-hook-returning-a-non-string-value-for-modifiedprompt-modif|A userPromptSubmitted hook returning a non-string value for modifiedPrompt…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-20 · ChatGPT · [[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom instructions are rolling out in beta]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20windsurf-2026-07-29-8ab9ef&body=Card%3A%20Changes%2FWindsurf%2F2026-07-29-devin-local-8ab9ef.md%0ACard%20ID%3A%20windsurf-2026-07-29-8ab9ef%0ASource%3A%20https%3A%2F%2Fdocs.devin.ai%2Fdesktop%2Fchangelog%23v3-6-21%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->