---
card_id: openclaw-2026-09-05-9b0343
date: '2026-09-05'
description: 'OpenClaw · 2026-09-05 · Collaboration: 9 changes in v2026.9.2 — Managed
  setup also applies lean tools for local models before checking the candidate, reducing…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-05-24-shared-links|Shared Links]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1200
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: collaboration
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 0bf4585c51dab4d03e732ee7dde9af515831ada60e6df9a64d0fa8d679458f67
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-05-9b0343
  comparison: ''
  date: '2026-09-05'
  description: 'OpenClaw — v2026.9.2: 9 Collaboration changes'
  evidence:
  - quote: Managed setup also applies lean tools for local models before checking
      the candidate, reducing the large tool list a smaller model has to process while
      keeping the agent's ordinary instructions in normal chats. An explicit opt-out
      is preserved. On a Gateway with several agents, setting up just one local agent
      can still change shared lean-tool settings used by other agents, so review those
      settings after targeted setup.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: People with operator read access share access to meetings across the Gateway,
      regardless of the selected agent; use separate Gateways when readers need isolation.
      Model summaries can fall back to heuristic notes, and very long meetings can
      omit middle sections from the model’s summary input, so use the transcript when
      a particular detail matters.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: This browser handoff currently supports Cloudflare Access, and native device
      approval remains a separate step unless the Gateway's existing automatic approval
      policy allows it. Personal saved Gateways also stay separate from the machine
      Primary that supplies Mac capabilities and Talk. Eligible Team dashboards can
      use personal identity for attribution, while shared-token and password connections
      keep their existing owner flow.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: A shared Beam snapshot can now become the start of a conversation with
      a Team agent. Write a message in its composer and OpenClaw copies the retained
      history into a new session belonging to you, using the source model when it
      is available and allowed, or explaining the switch to the agent's configured
      model.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Review conversation visibility before upgrading a shared Gateway. Conceptual
      illustration, not a screenshot. These are one-Gateway controls, not admin isolation.
      Mutually untrusted users need separate Gateways.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: The shared Gateway owner profile now stays separate from personal profiles
      and their GitHub connections. Shared-token or password access cannot absorb
      a person’s identity through an owner-profile merge, and adding the first personal
      identity no longer imposes multi-person catalog restrictions on an otherwise
      solo Gateway. If an unreleased build left a malformed owner profile, openclaw
      doctor --fix followed by reconnecting repairs supported cases while preserving
      the person’s data. GitHub-backed Cloudflare Access sign-ins also reuse verified
      public profile metadata and respect quota retry deadlines, while current identity
      bindings and permissions remain checked.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Device token rotation and revocation now complete for authorized callers
      and return the final result before self-management disconnects the client. Self-rotation
      can return the replacement token, but CLI output does not automatically save
      it for the next connection. Shared-secret callers and callers rotating another
      device receive metadata without the replacement bearer token. Removing a paired
      device also runs its worker cleanup if the requesting connection loses authorization
      after removal is committed.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: On shared installations with operator roles, knowing another person’s draft
      session key no longer lets a view, suggest, or write caller read its details
      or messages. Transcript reads check access again after loading, so revocation
      or replacement of the conversation during the read prevents disclosure; creators
      and administrators retain access. Managed image, thumbnail, and artifact downloads
      also follow the current conversation history, closing access when a reset or
      branch change removes the attachment from that history, even if an old archive
      still contains it.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Contributors running declaration builds must use dependencies owned by
      the selected checkout. Shared external toolchains are rejected, so affected
      setups may need a standalone checkout with its own pnpm install.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 9-collaboration-changes-in-v2026-9-2
  source_release: openclaw-2026-09-05-v2026-9-2-377f6d77
  source_type: openclaw_changelog
  theme: collaboration
  title: 9 Collaboration changes in v2026.9.2
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-09-03-6-collaboration-changes-in-rust-v0-153-0|6 Collaboration
  changes in rust-v0.153.0]]'
- '[[Changes/OpenClaw/2026-09-03-7-collaboration-changes-in-v2026-9-1|7 Collaboration
  changes in v2026.9.1]]'
- '[[Changes/GitHub Copilot CLI/2026-09-04-exporting-a-resumed-session-with-share-or-share-gist-writes-the-whole-transcript|Exporting
  a resumed session with --share or --share-gist writes the whole transcript…]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-05-v2026-9-2-377f6d77|openclaw-2026-09-05-v2026-9-2-377f6d77]]'
source_type: openclaw_changelog
theme: collaboration
title: 9 Collaboration changes in v2026.9.2
type: change
---

<!-- chronolog:begin region="header" -->
# 9 Collaboration changes in v2026.9.2

**OpenClaw** · 2026-09-05 · [[Themes/collaboration|Collaboration]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.2) · from [[Releases/OpenClaw/openclaw-2026-09-05-v2026-9-2-377f6d77|v2026.9.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Managed setup also applies lean tools for local models before checking the candidate, reducing the large tool list a smaller model has to process while keeping the agent's ordinary instructions in normal chats. An explicit opt-out is preserved. On a Gateway with several agents, setting up just one local agent can still change shared lean-tool settings used by other agents, so review those settings after targeted setup.

> People with operator read access share access to meetings across the Gateway, regardless of the selected agent; use separate Gateways when readers need isolation. Model summaries can fall back to heuristic notes, and very long meetings can omit middle sections from the model’s summary input, so use the transcript when a particular detail matters.

> This browser handoff currently supports Cloudflare Access, and native device approval remains a separate step unless the Gateway's existing automatic approval policy allows it. Personal saved Gateways also stay separate from the machine Primary that supplies Mac capabilities and Talk. Eligible Team dashboards can use personal identity for attribution, while shared-token and password connections keep their existing owner flow.

> A shared Beam snapshot can now become the start of a conversation with a Team agent. Write a message in its composer and OpenClaw copies the retained history into a new session belonging to you, using the source model when it is available and allowed, or explaining the switch to the agent's configured model.

> Review conversation visibility before upgrading a shared Gateway. Conceptual illustration, not a screenshot. These are one-Gateway controls, not admin isolation. Mutually untrusted users need separate Gateways.

> The shared Gateway owner profile now stays separate from personal profiles and their GitHub connections. Shared-token or password access cannot absorb a person’s identity through an owner-profile merge, and adding the first personal identity no longer imposes multi-person catalog restrictions on an otherwise solo Gateway. If an unreleased build left a malformed owner profile, openclaw doctor --fix followed by reconnecting repairs supported cases while preserving the person’s data. GitHub-backed Cloudflare Access sign-ins also reuse verified public profile metadata and respect quota retry deadlines, while current identity bindings and permissions remain checked.

> Device token rotation and revocation now complete for authorized callers and return the final result before self-management disconnects the client. Self-rotation can return the replacement token, but CLI output does not automatically save it for the next connection. Shared-secret callers and callers rotating another device receive metadata without the replacement bearer token. Removing a paired device also runs its worker cleanup if the requesting connection loses authorization after removal is committed.

> On shared installations with operator roles, knowing another person’s draft session key no longer lets a view, suggest, or write caller read its details or messages. Transcript reads check access again after loading, so revocation or replacement of the conversation during the read prevents disclosure; creators and administrators retain access. Managed image, thumbnail, and artifact downloads also follow the current conversation history, closing access when a reset or branch change removes the attachment from that history, even if an old archive still contains it.

> Contributors running declaration builds must use dependencies owned by the selected checkout. Shared external toolchains are rejected, so affected setups may need a standalone checkout with its own pnpm install.

Source: https://docs.openclaw.ai/releases/2026.9.2
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-09-05-24-safety-and-privacy-changes-in-v2026-9-2|24 Safety and Privacy changes in v2026.9.2]] · Safety and Privacy
- [[Changes/OpenClaw/2026-09-05-3-pricing-model-changes-in-v2026-9-2|3 Pricing Model changes in v2026.9.2]] · Pricing Model
- [[Changes/OpenClaw/2026-09-05-8-editor-experience-changes-in-v2026-9-2|8 Editor Experience changes in v2026.9.2]] · Editor Experience
- [[Changes/OpenClaw/2026-09-05-progress-mode-can-stay-quiet-about-routine-tool-calls-while-keeping-the-updates|Progress mode can stay quiet about routine tool calls while keeping the updates…]] · Presentation Creation
- [[Changes/OpenClaw/2026-09-05-swarm-is-now-available-to-eligible-agents-without-a-separate-enablement-step-so|Swarm is now available to eligible agents without a separate enablement step…]] · Agent Mode
- [[Changes/OpenClaw/2026-09-05-a-rejected-send-can-keep-its-original-attachments-and-retry-action-when-you-leav|A rejected send can keep its original attachments and Retry action when you leave…]] · Files and Data
- [[Changes/OpenClaw/2026-09-05-20-account-and-access-changes-in-v2026-9-2|20 Account and Access changes in v2026.9.2]] · Account and Access
- [[Changes/OpenClaw/2026-09-05-17-model-support-changes-in-v2026-9-2|17 Model Support changes in v2026.9.2]] · Model Support
- [[Changes/OpenClaw/2026-09-05-16-developer-workflow-changes-in-v2026-9-2|16 Developer Workflow changes in v2026.9.2]] · Developer Workflow
- [[Changes/OpenClaw/2026-09-05-21-memory-and-personalization-changes-in-v2026-9-2|21 Memory and Personalization changes in v2026.9.2]] · Memory and Personalization
- [[Changes/OpenClaw/2026-09-05-4-enterprise-and-administration-changes-in-v2026-9-2|4 Enterprise and Administration changes in v2026.9.2]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-09-05-if-background-image-video-or-music-generation-finishes-but-final-delivery-fails|If background image, video or music generation finishes but final delivery fails…]] · Music Generation
- [[Changes/OpenClaw/2026-09-05-34-agent-mode-changes-in-v2026-9-2|34 Agent Mode changes in v2026.9.2]] · Agent Mode
- [[Changes/OpenClaw/2026-09-05-35-apps-and-integrations-changes-in-v2026-9-2|35 Apps and Integrations changes in v2026.9.2]] · Apps and Integrations
- [[Changes/OpenClaw/2026-09-05-8-automation-and-scheduling-changes-in-v2026-9-2|8 Automation and Scheduling changes in v2026.9.2]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-09-05-10-mobile-and-desktop-changes-in-v2026-9-2|10 Mobile and Desktop changes in v2026.9.2]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-09-05-15-context-window-changes-in-v2026-9-2|15 Context Window changes in v2026.9.2]] · Context Window
- [[Changes/OpenClaw/2026-09-05-4-search-and-browsing-changes-in-v2026-9-2|4 Search and Browsing changes in v2026.9.2]] · Search and Browsing
- [[Changes/OpenClaw/2026-09-05-17-voice-and-audio-changes-in-v2026-9-2|17 Voice and Audio changes in v2026.9.2]] · Voice and Audio
- [[Changes/OpenClaw/2026-09-05-21-interface-experience-changes-in-v2026-9-2|21 Interface Experience changes in v2026.9.2]] · Interface Experience
- [[Changes/OpenClaw/2026-09-05-3-reliability-and-performance-changes-in-v2026-9-2|3 Reliability and Performance changes in v2026.9.2]] · Reliability and Performance
- [[Changes/OpenClaw/2026-09-05-you-can-now-put-the-part-of-a-task-you-are-working-on-in-the-main-view-and-keep|Put the part of a task you are working on in the main view and keep the conversation…]] · Developer Workflow
- [[Changes/OpenClaw/2026-09-05-72-other-changes-in-v2026-9-2|72 other changes in v2026.9.2]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Collaboration

- Earlier: 2026-09-04 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-09-04-exporting-a-resumed-session-with-share-or-share-gist-writes-the-whole-transcript|Exporting a resumed session with --share or --share-gist writes the whole transcript…]]
- Later: 2026-09-08 · ChatGPT · [[Changes/ChatGPT/2026-09-08-share-a-prompt-share-the-prompt-for-a-generated-image-so-others-can-create-their|Share a prompt]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-05-24 · ChatGPT · [[Changes/ChatGPT/2023-05-24-shared-links|Shared Links]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-05-9b0343&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-05-9-collaboration-changes-in-v2026-9-2.md%0ACard%20ID%3A%20openclaw-2026-09-05-9b0343%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.2%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->