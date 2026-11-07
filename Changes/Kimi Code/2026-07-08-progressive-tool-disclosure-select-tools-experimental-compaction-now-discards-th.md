---
card_id: kimi-code-2026-07-08-2ac2bd
date: '2026-07-08'
description: 'Kimi Code · 2026-07-08 · Memory and Personalization: Progressive tool
  disclosure (`select_tools`, experimental): compaction now discards the loaded tool…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom
    instructions are rolling out in beta]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1084
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: memory
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: significant
kind: change
machine_hash: 2d541b566626f789cd6b1d9834b0346283a082d3c2ce2da9b8ac9fbb7de44ed7
product: kimi-code
product_name: Kimi Code
record:
  ai_generated: true
  card_id: kimi-code-2026-07-08-2ac2bd
  comparison: ''
  confidence: low
  date: '2026-07-08'
  description: 'Kimi Code — Kimi Code 0.23.2 (2026-07-08): Progressive tool disclosure
    (`select_tools`, experimental): compaction now discards the loaded tool schemas
    instead of re-injecting them, and the model re-selects the tools it still needs
    afterward. A from-memory call to a no-longer-loaded tool is rejected with guidance
    to select it first. No effect unless the `tool-select` experimental flag and a
    `select_tools`-capable model are active.'
  evidence:
  - quote: 'Progressive tool disclosure (`select_tools`, experimental): compaction
      now discards the loaded tool schemas instead of re-injecting them, and the model
      re-selects the tools it still needs afterward. A from-memory call to a no-longer-loaded
      tool is rejected with guidance to select it first. No effect unless the `tool-select`
      experimental flag and a `select_tools`-capable model are active.'
    source_release: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
  extractor_version: fallback-v5
  impact: significant
  kind: change
  product: kimi-code
  product_name: Kimi Code
  slug: progressive-tool-disclosure-select-tools-experimental-compaction-now-discards-th
  source_release: kimi-code-2026-07-08-0-23-2-9a81d837
  source_type: kimi_code_changelog
  theme: memory
  theme_matches:
  - matched_terms:
    - memory
    score: 110
    theme: memory
  - matched_terms:
    - model
    score: 50
    theme: model-support
  title: Progressive tool disclosure (`select_tools`, experimental)
  type: change
related_changes:
- '[[Changes/Kimi Code/2026-07-02-release-pasted-images-and-streaming-timers-once-they-are-no-longer-shown-so-memo|Release
  pasted images and streaming timers once they are no longer shown, so memory…]]'
- '[[Changes/v0/2026-07-07-team-members-with-v0-edit-access-can-manage-team-skills-and-memories-without-a-v|Team
  members with v0 edit access can manage team skills and memories without…]]'
- '[[Changes/Codex CLI/2026-07-08-2-memory-and-personalization-changes-in-rust-v0-143-0|2
  Memory and Personalization changes in rust-v0.143.0]]'
source_release: '[[Releases/Kimi Code/kimi-code-2026-07-08-0-23-2-9a81d837|kimi-code-2026-07-08-0-23-2-9a81d837]]'
source_type: kimi_code_changelog
theme: memory
title: Progressive tool disclosure (select_tools, experimental)
type: change
---

<!-- chronolog:begin region="header" -->
# Progressive tool disclosure (`select_tools`, experimental)

**Kimi Code** · 2026-07-08 · [[Themes/memory|Memory and Personalization]] · [Official source](https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md) · from [[Releases/Kimi Code/kimi-code-2026-07-08-0-23-2-9a81d837|Kimi Code 0.23.2 (2026-07-08)]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Progressive tool disclosure (`select_tools`, experimental): compaction now discards the loaded tool schemas instead of re-injecting them, and the model re-selects the tools it still needs afterward. A from-memory call to a no-longer-loaded tool is rejected with guidance to select it first. No effect unless the `tool-select` experimental flag and a `select_tools`-capable model are active.
>
> Source: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Kimi Code/2026-07-08-2-model-support-changes-in-kimi-code-0-23-2|2 Model Support changes in Kimi Code 0.23.2]] · Model Support
- [[Changes/Kimi Code/2026-07-08-count-the-turn-that-starts-an-autonomous-goal-toward-its-turn-budget|Count the turn that starts an autonomous goal toward its turn budget]] · Agent Mode
- [[Changes/Kimi Code/2026-07-08-web-show-session-skills-in-the-slash-menu-as-skill-so-they-are-distinguishable-f|web: Show session skills in the slash menu as /skill: so they are distinguishable…]] · Interface Experience
- [[Changes/Kimi Code/2026-07-08-add-the-vercel-plugin-to-the-bundled-plugin-marketplace-run-plugins-and-select-v|Add the Vercel plugin to the bundled plugin marketplace]] · Apps and Integrations
- [[Changes/Kimi Code/2026-07-08-5-other-changes-in-kimi-code-0-23-2|5 other changes in Kimi Code 0.23.2]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Memory and Personalization

- Earlier: 2026-07-08 · Codex CLI · [[Changes/Codex CLI/2026-07-08-2-memory-and-personalization-changes-in-rust-v0-143-0|2 Memory and Personalization changes in rust-v0.143.0]]
- Later: 2026-07-09 · Claude · [[Changes/Claude/2026-07-09-a-new-way-to-reflect-with-claude|A new way to reflect with Claude]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-20 · ChatGPT · [[Changes/ChatGPT/2023-07-20-we-re-starting-to-roll-out-custom-instructions-giving-you-more-control-over-chat-37833c|Custom instructions are rolling out in beta]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20kimi-code-2026-07-08-2ac2bd&body=Card%3A%20Changes%2FKimi%20Code%2F2026-07-08-progressive-tool-disclosure-select-tools-experimental-compaction-now-discards-th.md%0ACard%20ID%3A%20kimi-code-2026-07-08-2ac2bd%0ASource%3A%20https%3A%2F%2Fgithub.com%2FMoonshotAI%2Fkimi-code%2Fblob%2Fmain%2Fdocs%2Fen%2Frelease-notes%2Fchangelog.md%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->