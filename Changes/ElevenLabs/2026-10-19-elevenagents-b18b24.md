---
card_id: elevenlabs-2026-10-19-b18b24
date: '2026-10-19'
description: 'ElevenLabs · 2026-10-19 · Agent Mode: **Alerts**: [Alerts](https://elevenlabs.io/docs/eleven-agents/operate/alerts)
  notify a workspace when agent error rates…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1201
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: paradigm-shift
kind: launch
machine_hash: 98218523496c6529ea31b4e17794ec2834c6777eac22e2e64ee83876bc93b03b
product: elevenlabs
product_name: ElevenLabs
record:
  ai_generated: true
  card_id: elevenlabs-2026-10-19-b18b24
  comparison: ''
  confidence: low
  date: '2026-10-19'
  description: 'ElevenLabs — ElevenLabs updates — 2026-10-19: **Alerts**: [Alerts](https://elevenlabs.io/docs/eleven-agents/operate/alerts)
    notify a workspace when agent error rates exceed a threshold or rise sharply above
    their recent baseline. Monitors cover conversation failures, tool failures, webhook
    errors, guardrail triggers, call initiation errors and evaluation success scores,
    and run with default thresholds without any setup. Agent-level thresholds and
    notifiers can be set through `platform_settings.alerting` on [Update agent](https://elevenlabs.io/docs/api-reference/agents/update).
    Notifications can be delivered as webhooks, to Slack or to PagerDuty.'
  evidence:
  - quote: '**Alerts**: [Alerts](https://elevenlabs.io/docs/eleven-agents/operate/alerts)
      notify a workspace when agent error rates exceed a threshold or rise sharply
      above their recent baseline. Monitors cover conversation failures, tool failures,
      webhook errors, guardrail triggers, call initiation errors and evaluation success
      scores, and run with default thresholds without any setup. Agent-level thresholds
      and notifiers can be set through `platform_settings.alerting` on [Update agent](https://elevenlabs.io/docs/api-reference/agents/update).
      Notifications can be delivered as webhooks, to Slack or to PagerDuty.'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/19
  - quote: '**Guardrails generally available**: [Guardrails](https://elevenlabs.io/docs/eleven-agents/best-practices/guardrails)
      are no longer in alpha.'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/19
  - quote: '**Workspace environments**: Environments for [environment variables](https://elevenlabs.io/docs/eleven-agents/integrate/environment-variables)
      can now be managed through the API with [List environments](https://elevenlabs.io/docs/api-reference/environments/list),
      [Create environment](https://elevenlabs.io/docs/api-reference/environments/create)
      and [Delete environment](https://elevenlabs.io/docs/api-reference/environments/delete).
      A variable without a value for an environment falls back to its `production`
      value. Deleting an environment removes its values from all variables, and `production`
      cannot be deleted.'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/19
  - quote: '**Answering machine detection actions**: Twilio answering machine detection
      settings on [Outbound call](https://elevenlabs.io/docs/api-reference/twilio/outbound-call)
      and [Submit batch call](https://elevenlabs.io/docs/api-reference/batch-calling/create)
      accept `actions`, a list of rules that pair an `action` (`hang_up`) with the
      `answered_by` verdicts that trigger it, such as `machine_start` or `fax`. Verdicts
      without a rule leave the call running.'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/19
  - quote: '**New LLMs**: Agents can use `gemini-4-argon`, `claude-opus-4-6` and the
      ElevenLabs-hosted `nemotron-35-super-vl-nvfp4`. See [Models](https://elevenlabs.io/docs/eleven-agents/customization/llm).'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/19
  - quote: '**Authored-only workflow reads**: [Get agent](https://elevenlabs.io/docs/api-reference/agents/get)
      and [Update agent](https://elevenlabs.io/docs/api-reference/agents/update) accept
      `include_procedure_generated_workflow_elements`. Set it to `false` to receive
      only the workflow nodes and edges you authored, excluding the ones compiled
      from [structured procedures](https://elevenlabs.io/docs/eleven-agents/customization/procedures/structured-procedures).
      Defaults to `true`, so existing callers are unchanged.'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/19
  - quote: '**Branch rebasing from any branch**: [Rebase branch](https://elevenlabs.io/docs/api-reference/agents/branches/rebase)
      and [Preview rebase](https://elevenlabs.io/docs/api-reference/agents/branches/preview-rebase)
      accept an optional `source_branch_id` to pull changes from a branch other than
      main.'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/19
  - quote: '**Delete agents used as subagents**: [Delete agent](https://elevenlabs.io/docs/api-reference/agents/delete)
      accepts `force`. When `true`, the agent is deleted even if other agents use
      it as a subagent, and it is removed from those agents and their branches.'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/19
  - quote: '**Sort agents by last update**: [List agents](https://elevenlabs.io/docs/api-reference/agents/list)
      accepts `sort_by=updated_at`, and each agent summary includes `updated_at_unix_secs`,
      the last time the main branch or agent-level settings changed.'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/19
  - quote: '**Google Calendar event updates**: The [Google Calendar integration](https://elevenlabs.io/docs/eleven-agents/customization/integrations/google_calendar)
      adds `google_calendar_update_event` and `google_calendar_delete_event` tools.
      Both are privileged tools that can change or cancel any event on the connected
      calendar.'
    source_release: https://elevenlabs.io/docs/changelog/2026/10/19
  extractor_version: fallback-v5
  impact: paradigm-shift
  kind: launch
  product: elevenlabs
  product_name: ElevenLabs
  slug: elevenagents
  source_release: elevenlabs-2026-10-19-2026-10-19-dd219c14
  source_type: elevenlabs_changelog
  theme: agent-mode
  title: ElevenAgents
  type: change
related_changes:
- '[[Changes/Claude Code/2026-10-19-2-agent-mode-changes-in-v2-1-304|2 Agent Mode
  changes in v2.1.304]]'
- '[[Changes/Claude Code/2026-10-19-added-claude-api-managed-agents-secure-which-compares-a-managed-agents-agent-s-s|Added
  /claude-api managed-agents-secure, which compares a Managed Agents agent''s…]]'
- '[[Changes/ElevenLabs/2026-10-19-javascript-sdk|JavaScript SDK]]'
source_release: '[[Releases/ElevenLabs/elevenlabs-2026-10-19-2026-10-19-dd219c14|elevenlabs-2026-10-19-2026-10-19-dd219c14]]'
source_type: elevenlabs_changelog
theme: agent-mode
title: ElevenAgents
type: change
---

<!-- chronolog:begin region="header" -->
# ElevenAgents

**ElevenLabs** · 2026-10-19 · [[Themes/agent-mode|Agent Mode]] · Launch · [Official source](https://elevenlabs.io/docs/changelog/2026/10/19) · from [[Releases/ElevenLabs/elevenlabs-2026-10-19-2026-10-19-dd219c14|ElevenLabs updates — 2026-10-19]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> **Alerts**: [Alerts](https://elevenlabs.io/docs/eleven-agents/operate/alerts) notify a workspace when agent error rates exceed a threshold or rise sharply above their recent baseline. Monitors cover conversation failures, tool failures, webhook errors, guardrail triggers, call initiation errors and evaluation success scores, and run with default thresholds without any setup. Agent-level thresholds and notifiers can be set through `platform_settings.alerting` on [Update agent](https://elevenlabs.io/docs/api-reference/agents/update). Notifications can be delivered as webhooks, to Slack or to PagerDuty.
>
> **Guardrails generally available**: [Guardrails](https://elevenlabs.io/docs/eleven-agents/best-practices/guardrails) are no longer in alpha.
>
> **Workspace environments**: Environments for [environment variables](https://elevenlabs.io/docs/eleven-agents/integrate/environment-variables) can now be managed through the API with [List environments](https://elevenlabs.io/docs/api-reference/environments/list), [Create environment](https://elevenlabs.io/docs/api-reference/environments/create) and [Delete environment](https://elevenlabs.io/docs/api-reference/environments/delete). A variable without a value for an environment falls back to its `production` value. Deleting an environment removes its values from all variables, and `production` cannot be deleted.
>
> **Answering machine detection actions**: Twilio answering machine detection settings on [Outbound call](https://elevenlabs.io/docs/api-reference/twilio/outbound-call) and [Submit batch call](https://elevenlabs.io/docs/api-reference/batch-calling/create) accept `actions`, a list of rules that pair an `action` (`hang_up`) with the `answered_by` verdicts that trigger it, such as `machine_start` or `fax`. Verdicts without a rule leave the call running.
>
> **New LLMs**: Agents can use `gemini-4-argon`, `claude-opus-4-6` and the ElevenLabs-hosted `nemotron-35-super-vl-nvfp4`. See [Models](https://elevenlabs.io/docs/eleven-agents/customization/llm).
>
> **Authored-only workflow reads**: [Get agent](https://elevenlabs.io/docs/api-reference/agents/get) and [Update agent](https://elevenlabs.io/docs/api-reference/agents/update) accept `include_procedure_generated_workflow_elements`. Set it to `false` to receive only the workflow nodes and edges you authored, excluding the ones compiled from [structured procedures](https://elevenlabs.io/docs/eleven-agents/customization/procedures/structured-procedures). Defaults to `true`, so existing callers are unchanged.
>
> **Branch rebasing from any branch**: [Rebase branch](https://elevenlabs.io/docs/api-reference/agents/branches/rebase) and [Preview rebase](https://elevenlabs.io/docs/api-reference/agents/branches/preview-rebase) accept an optional `source_branch_id` to pull changes from a branch other than main.
>
> **Delete agents used as subagents**: [Delete agent](https://elevenlabs.io/docs/api-reference/agents/delete) accepts `force`. When `true`, the agent is deleted even if other agents use it as a subagent, and it is removed from those agents and their branches.
>
> **Sort agents by last update**: [List agents](https://elevenlabs.io/docs/api-reference/agents/list) accepts `sort_by=updated_at`, and each agent summary includes `updated_at_unix_secs`, the last time the main branch or agent-level settings changed.
>
> **Google Calendar event updates**: The [Google Calendar integration](https://elevenlabs.io/docs/eleven-agents/customization/integrations/google_calendar) adds `google_calendar_update_event` and `google_calendar_delete_event` tools. Both are privileged tools that can change or cancel any event on the connected calendar.
>
> Source: https://elevenlabs.io/docs/changelog/2026/10/19
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/ElevenLabs/2026-10-19-speech-to-text|Speech to Text]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-19-sdk-releases|SDK releases]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-10-19-music-and-sound-effects|Music and Sound Effects]] · Enterprise and Administration
- [[Changes/ElevenLabs/2026-10-19-eleven-realtime|Eleven Realtime]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-19-elevenagents|ElevenAgents]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-19-video-to-music|Video to Music]] · Multimodal Input
- [[Changes/ElevenLabs/2026-10-19-realtime-translation|Realtime Translation]] · Enterprise and Administration
- [[Changes/ElevenLabs/2026-10-19-javascript-sdk|JavaScript SDK]] · Agent Mode
- [[Changes/ElevenLabs/2026-10-19-music|Music]] · Multimodal Input
- [[Changes/ElevenLabs/2026-10-19-voices|Voices]] · Voice and Audio
- [[Changes/ElevenLabs/2026-10-19-python-sdk|Python SDK]] · Apps and Integrations
- [[Changes/ElevenLabs/2026-10-19-elevenagents-ee74ab|ElevenAgents]] · Agent Mode
- [[Changes/ElevenLabs/2026-10-19-voices-f9aa8c|Voices]] · Voice and Audio
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-10-19 · Claude Code · [[Changes/Claude Code/2026-10-19-added-claude-api-managed-agents-secure-which-compares-a-managed-agents-agent-s-s|Added /claude-api managed-agents-secure, which compares a Managed Agents agent's…]]
- Later: 2026-10-19 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-10-19-2-agent-mode-changes-in-v1-0-100|2 Agent Mode changes in v1.0.100]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20elevenlabs-2026-10-19-b18b24&body=Card%3A%20Changes%2FElevenLabs%2F2026-10-19-elevenagents-b18b24.md%0ACard%20ID%3A%20elevenlabs-2026-10-19-b18b24%0ASource%3A%20https%3A%2F%2Felevenlabs.io%2Fdocs%2Fchangelog%2F2026%2F10%2F19%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->