---
card_id: elevenlabs-2026-10-05-5bf5b0
date: '2026-10-05'
description: 'ElevenLabs · 2026-10-05 · Agent Mode: **Structured procedures compile
  on save and publish**: [Update…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1187
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: paradigm-shift
kind: launch
machine_hash: b8c7c4b72652f8431d79a6497a358566c75a0b1d0686d3fa0b14993bac27dd85
product: elevenlabs
product_name: ElevenLabs
record:
  ai_generated: true
  card_id: elevenlabs-2026-10-05-5bf5b0
  comparison: ''
  confidence: low
  date: '2026-10-05'
  description: 'ElevenLabs — ElevenLabs updates — 2026-10-05: **Structured procedures
    compile on save and publish**: [Update agent](https://elevenlabs.io/docs/api-reference/agents/update)
    and [Create agent draft](https://elevenlabs.io/docs/api-reference/agents/drafts/create)
    now compile and validate [structured procedures](https://elevenlabs.io/docs/eleven-agents/customization/procedures/structured-procedures)
    automatically. Integrations no longer need to call the compile endpoint or manually
    update the generated workflow. Invalid procedures return per-procedure errors
    as `400 procedure_validation_failed`. Agents without structured procedures are
    unaffected.'
  evidence:
  - quote: '**Structured procedures compile on save and publish**: [Update agent](https://elevenlabs.io/docs/api-reference/agents/update)
      and [Create agent draft](https://elevenlabs.io/docs/api-reference/agents/drafts/create)
      now compile and validate [structured procedures](https://elevenlabs.io/docs/eleven-agents/customization/procedures/structured-procedures)
      automatically. Integrations no longer need to call the compile endpoint or manually
      update the generated workflow. Invalid procedures return per-procedure errors
      as `400 procedure_validation_failed`. Agents without structured procedures are
      unaffected.'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/5
  - quote: '**Compile procedures endpoint is legacy**: [Compile procedures](https://elevenlabs.io/docs/api-reference/agents/procedures/compile)
      is marked legacy and should not be used by new integrations. It remains available
      for existing callers.'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/5
  - quote: '**Merge proposals**: Merge proposals are available in alpha. Teams can
      open a proposal for an agent branch, review configuration changes and test results,
      leave comments or approval decisions, and merge approved changes into a target
      branch. See [Merge proposals](https://elevenlabs.io/docs/eleven-agents/operate/merge-proposals).'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/5
  extractor_version: fallback-v5
  impact: paradigm-shift
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: elevenagents
  source_release: elevenlabs-2026-10-05-2026-10-05-4039c076
  source_type: elevenlabs_changelog
  theme: agent-mode
  theme_matches:
  - matched_terms:
    - agent
    - agents
    score: 100
    theme: agent-mode
  - matched_terms:
    - integrations
    score: 50
    theme: apps-integrations
  title: ElevenAgents
  type: change
related_changes:
- '[[Changes/Claude Code/2026-10-05-added-claude-api-managed-agents-onboard-quickstart-name-to-build-a-console-quick|Added
  /claude-api managed-agents-onboard quickstart-name to build a Console…]]'
- '[[Changes/Claude Code/2026-10-05-4-agent-mode-changes-in-v2-1-290|4 Agent Mode
  changes in v2.1.290]]'
- '[[Changes/ElevenLabs/2026-10-05-elevenagents|ElevenAgents]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-10-05-2026-10-05-4039c076|elevenlabs-2026-10-05-2026-10-05-4039c076]]'
source_type: elevenlabs_changelog
theme: agent-mode
title: ElevenAgents
type: change
---

<!-- chronolog:begin region="header" -->
# ElevenAgents

**ElevenLabs** · 2026-10-05 · [[Themes/agent-mode|Agent Mode]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2026/10/5) · from [[Releases/ElevenLabs/elevenlabs-2026-10-05-2026-10-05-4039c076|ElevenLabs updates — 2026-10-05]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> **Structured procedures compile on save and publish**: [Update agent](https://elevenlabs.io/docs/api-reference/agents/update) and [Create agent draft](https://elevenlabs.io/docs/api-reference/agents/drafts/create) now compile and validate [structured procedures](https://elevenlabs.io/docs/eleven-agents/customization/procedures/structured-procedures) automatically. Integrations no longer need to call the compile endpoint or manually update the generated workflow. Invalid procedures return per-procedure errors as `400 procedure_validation_failed`. Agents without structured procedures are unaffected.
>
> **Compile procedures endpoint is legacy**: [Compile procedures](https://elevenlabs.io/docs/api-reference/agents/procedures/compile) is marked legacy and should not be used by new integrations. It remains available for existing callers.
>
> **Merge proposals**: Merge proposals are available in alpha. Teams can open a proposal for an agent branch, review configuration changes and test results, leave comments or approval decisions, and merge approved changes into a target branch. See [Merge proposals](https://elevenlabs.io/docs/eleven-agents/operate/merge-proposals).
>
> Source: https://elevenlabs.io/docs/changelog/2026/10/5
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-10-05-swift-sdk|Swift SDK]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-10-05-packages|Packages]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-05-elevenagents|ElevenAgents]] · Agent Mode
- [[Changes/ElevenLabs/2026-10-05-python-sdk|Python SDK]] · Model Support
- [[Changes/ElevenLabs/2026-10-05-javascript-sdk|JavaScript SDK]] · Model Support
- [[Changes/ElevenLabs/2026-10-05-sdk-releases|SDK releases]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-10-05-elevenagents-ceeb34|ElevenAgents]] · Agent Mode
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-10-05 · Claude Code · [[Changes/Claude Code/2026-10-05-4-agent-mode-changes-in-v2-1-290|4 Agent Mode changes in v2.1.290]]
- Later: 2026-10-05 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-10-05-5-agent-mode-changes-in-v1-0-92|5 Agent Mode changes in v1.0.92]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-10-05-5bf5b0&body=Card%3A%20Changes%2FElevenLabs%2F2026-10-05-elevenagents-5bf5b0.md%0ACard%20ID%3A%20elevenlabs-2026-10-05-5bf5b0%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F10%2F5%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->