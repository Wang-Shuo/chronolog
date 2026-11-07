---
card_id: gemini-cli-2026-01-21-cf5fbb
date: '2026-01-21'
description: 'Gemini CLI · 2026-01-21 · Agent Mode: 13 changes in Release v0.25.0
  — feat(core): Preliminary changes for subagent model routing. by @joshualitt in…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 930
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 847ad9803fa12ff2d6262adaaffcef6e31b7b6fb40a0295f9b3686cf45f62506
product: gemini-cli
product_name: Gemini CLI
record:
  card_id: gemini-cli-2026-01-21-cf5fbb
  comparison: ''
  date: '2026-01-21'
  description: 'Gemini CLI — Release v0.25.0: 13 Agent Mode changes'
  evidence:
  - quote: 'feat(core): Preliminary changes for subagent model routing. by @joshualitt
      in https://github.com/google-gemini/gemini-cli/pull/16035'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.25.0
  - quote: enable cli_help agent by default by @scidomino in https://github.com/google-gemini/gemini-cli/pull/16100
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.25.0
  - quote: 'feat(cli): add /agents slash command to list available agents by @adamfweidman
      in https://github.com/google-gemini/gemini-cli/pull/16182'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.25.0
  - quote: 'feat(core, ui): Add `/agents refresh` command. by @joshualitt in https://github.com/google-gemini/gemini-cli/pull/16204'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.25.0
  - quote: Support for Built-in Agent Skills by @NTaylorMullen in https://github.com/google-gemini/gemini-cli/pull/16045
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.25.0
  - quote: Markdown w/ Frontmatter Agent Parser by @sehoon38 in https://github.com/google-gemini/gemini-cli/pull/16094
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.25.0
  - quote: Update cli-help agent's system prompt in sub-agents section by @sehoon38
      in https://github.com/google-gemini/gemini-cli/pull/16441
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.25.0
  - quote: 'feat(agents): improve UI feedback and parser reliability by @NTaylorMullen
      in https://github.com/google-gemini/gemini-cli/pull/16459'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.25.0
  - quote: 'feat(agents): clarify mandatory YAML frontmatter for sub-agents by @NTaylorMullen
      in https://github.com/google-gemini/gemini-cli/pull/16515'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.25.0
  - quote: Implement support for subagents as extensions. by @gundermanc in https://github.com/google-gemini/gemini-cli/pull/16473
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.25.0
  - quote: 'feat(core, cli): Add support for agents in settings.json. by @joshualitt
      in https://github.com/google-gemini/gemini-cli/pull/16433'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.25.0
  - quote: 'feat(core): Align internal agent settings with configs exposed through
      settings.json by @joshualitt in https://github.com/google-gemini/gemini-cli/pull/16458'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.25.0
  - quote: 'feat(admin): support admin-enforced settings for Agent Skills by @NTaylorMullen
      in https://github.com/google-gemini/gemini-cli/pull/16406'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.25.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: gemini-cli
  product_name: Gemini CLI
  slug: 13-agent-mode-changes-in-v0-25-0
  source_release: gemini-cli-2026-01-21-v0-25-0-github-278507155-65088397
  source_type: github_releases
  theme: agent-mode
  title: 13 Agent Mode changes in v0.25.0
  type: change
related_changes:
- '[[Changes/Notion/2026-01-20-your-agent-fits-in-your-pocket|Your Agent fits in your
  pocket]]'
- '[[Changes/OpenCode/2026-01-20-2-agent-mode-changes-in-v1-1-28|2 Agent Mode changes
  in v1.1.28]]'
- '[[Changes/Codex CLI/2026-01-21-2-agent-mode-changes-in-rust-v0-88-0|2 Agent Mode
  changes in rust-v0.88.0]]'
source_release: '[[Releases/Gemini CLI/gemini-cli-2026-01-21-v0-25-0-github-278507155-65088397|gemini-cli-2026-01-21-v0-25-0-github-278507155-65088397]]'
source_type: github_releases
theme: agent-mode
title: 13 Agent Mode changes in v0.25.0
type: change
---

<!-- chronolog:begin region="header" -->
# 13 Agent Mode changes in v0.25.0

**Gemini CLI** · 2026-01-21 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/google-gemini/gemini-cli/releases/tag/v0.25.0) · from [[Releases/Gemini CLI/gemini-cli-2026-01-21-v0-25-0-github-278507155-65088397|Release v0.25.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> feat(core): Preliminary changes for subagent model routing. by @joshualitt in https://github.com/google-gemini/gemini-cli/pull/16035

> enable cli_help agent by default by @scidomino in https://github.com/google-gemini/gemini-cli/pull/16100

> feat(cli): add /agents slash command to list available agents by @adamfweidman in https://github.com/google-gemini/gemini-cli/pull/16182

> feat(core, ui): Add `/agents refresh` command. by @joshualitt in https://github.com/google-gemini/gemini-cli/pull/16204

> Support for Built-in Agent Skills by @NTaylorMullen in https://github.com/google-gemini/gemini-cli/pull/16045

> Markdown w/ Frontmatter Agent Parser by @sehoon38 in https://github.com/google-gemini/gemini-cli/pull/16094

> Update cli-help agent's system prompt in sub-agents section by @sehoon38 in https://github.com/google-gemini/gemini-cli/pull/16441

> feat(agents): improve UI feedback and parser reliability by @NTaylorMullen in https://github.com/google-gemini/gemini-cli/pull/16459

> feat(agents): clarify mandatory YAML frontmatter for sub-agents by @NTaylorMullen in https://github.com/google-gemini/gemini-cli/pull/16515

> Implement support for subagents as extensions. by @gundermanc in https://github.com/google-gemini/gemini-cli/pull/16473

> feat(core, cli): Add support for agents in settings.json. by @joshualitt in https://github.com/google-gemini/gemini-cli/pull/16433

> feat(core): Align internal agent settings with configs exposed through settings.json by @joshualitt in https://github.com/google-gemini/gemini-cli/pull/16458

> feat(admin): support admin-enforced settings for Agent Skills by @NTaylorMullen in https://github.com/google-gemini/gemini-cli/pull/16406

Source: https://github.com/google-gemini/gemini-cli/releases/tag/v0.25.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Gemini CLI/2026-01-21-feat-a2a-introduce-memory-command-for-a2a-server-by-cocosheng-g-in-https-github|feat(a2a): Introduce /memory command for a2a server]] · Memory and Personalization
- [[Changes/Gemini CLI/2026-01-21-6-model-support-changes-in-v0-25-0|6 Model Support changes in v0.25.0]] · Model Support
- [[Changes/Gemini CLI/2026-01-21-10-apps-and-integrations-changes-in-v0-25-0|10 Apps and Integrations changes in v0.25.0]] · Apps and Integrations
- [[Changes/Gemini CLI/2026-01-21-3-interface-experience-changes-in-v0-25-0|3 Interface Experience changes in v0.25.0]] · Interface Experience
- [[Changes/Gemini CLI/2026-01-21-2-reliability-and-performance-changes-in-v0-25-0|2 Reliability and Performance changes in v0.25.0]] · Reliability and Performance
- [[Changes/Gemini CLI/2026-01-21-7-developer-workflow-changes-in-v0-25-0|7 Developer Workflow changes in v0.25.0]] · Developer Workflow
- [[Changes/Gemini CLI/2026-01-21-4-editor-experience-changes-in-v0-25-0|4 Editor Experience changes in v0.25.0]] · Editor Experience
- [[Changes/Gemini CLI/2026-01-21-feat-admin-prompt-user-to-restart-the-cli-if-they-change-auth-to-oauth-mid-sessi|feat(admin): prompt user to restart the CLI if they change auth to oauth mid-session…]] · Account and Access
- [[Changes/Gemini CLI/2026-01-21-2-automation-and-scheduling-changes-in-v0-25-0|2 Automation and Scheduling changes in v0.25.0]] · Automation and Scheduling
- [[Changes/Gemini CLI/2026-01-21-72-other-changes-in-v0-25-0|72 other changes in v0.25.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-01-21 · Codex CLI · [[Changes/Codex CLI/2026-01-21-2-agent-mode-changes-in-rust-v0-88-0|2 Agent Mode changes in rust-v0.88.0]]
- Later: 2026-01-21 · v0 · [[Changes/v0/2026-01-21-added-ai-sdk-v6-support-for-agents|Added AI SDK v6 support for agents]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20gemini-cli-2026-01-21-cf5fbb&body=Card%3A%20Changes%2FGemini%20CLI%2F2026-01-21-13-agent-mode-changes-in-v0-25-0.md%0ACard%20ID%3A%20gemini-cli-2026-01-21-cf5fbb%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgoogle-gemini%2Fgemini-cli%2Freleases%2Ftag%2Fv0.25.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->