---
card_id: openclaw-2026-09-08-e765e5
date: '2026-09-08'
description: 'OpenClaw · 2026-09-08 · Safety and Privacy: 14 changes in v2026.9.3
  — Opening desktop or browser setup detects available providers without activating
  one until…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke
    Application Access]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2233
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: f0c39f65292e3db43ec2702edbec383644b389d4736eb85eb8174ad9408f4f1c
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-08-e765e5
  comparison: ''
  date: '2026-09-08'
  description: 'OpenClaw — v2026.9.3: 14 Safety and Privacy changes'
  evidence:
  - quote: Opening desktop or browser setup detects available providers without activating
      one until you choose it. Fresh native-conversation discovery starts unchecked,
      and cancelling or failing setup does not select a different provider. Guided
      setup can also finish without an AI provider. Saved consent choices survive
      reconciliation with an existing agent.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: A failed-update action can prepare a sanitized report for your review and
      submit it only with explicit consent. Missing GitHub authentication offers a
      browser handoff rather than sending anything automatically.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Pairing notifications come from the approved channel account, and a notification
      failure does not undo the approval itself. Mattermost direct messages on private
      servers retain the account's existing network permission, Nostr honors positive
      relay acknowledgements, and failed iMessage helper pipes stop leaving pending
      requests waiting.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Memory and Import Memory show agent-list errors with a usable retry instead
      of remaining in a loading cycle. Reads from additional memory folders report
      relevant permission or file errors, and skipped symlink roots point to their
      canonical directories without silently rewriting the configuration.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Collection reviews are also instructed to look across related skills while
      preserving useful task boundaries. Compatible CLI backends, including Claude
      CLI, can perform these reviews within the permitted root using the existing
      sandbox and approval settings.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: The Mac and iOS apps now bring connected administrator settings into Dashboard
      while keeping connection setup and offline recovery in native controls. Older
      Gateways need the matching Dashboard support, and sensitive device-capability
      changes still require native consent.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: The Start Live Voice action opens the current chat and starts Talk from
      Siri or Shortcuts. Your phone still needs to be unlocked and the app in the
      foreground, with pairing, provider setup and microphone permission completed.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Normal Apple Watch setup now includes voice authorization in the same connection
      action. Existing Watches connected only as nodes need to reconnect, and starting
      a voice conversation still requires Start and microphone permission.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Native Ollama avoids silently truncating history when a conversation exceeds
      its available context. Its requests honor per-request sampling overrides, including
      explicit zero values, and retained reasoning stays with tool follow-ups without
      becoming visible answer text. Setup rejects models known to support embeddings
      alone before selecting them for chat. llama.cpp preparation also preserves configured
      preset defaults, comments and unmanaged options. Fresh llama.cpp installation
      allows time for the first macOS security check, and managed installs receive
      updated runtime binaries.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Reports mark incomplete periods and source-coverage gaps, use UTC reporting
      windows, and remain behind Gateway authentication and operator read permission.
      Light and dark themes, GitHub avatars, and expandable activity lists help with
      browsing; collection still has documented limits, including omitted review-submission
      bodies and some historical commit and attribution cases. In an embedded tab,
      a theme choice follows in-tab navigation rather than being saved in browser
      storage.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Permission checks stay attached to the account, agent, connection, and
      file they protect. Device capability requests remain available until you resolve
      them, Android honors approximate-location choices, and credential and runtime-context
      handling receive more narrowly scoped protections.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Tool-policy groups use the same aliases and membership as core. Claude
      native Bash honors fully bindable exec allowlists under on-miss prompting while
      retaining deny and always-prompt behavior; an argument policy is not a sandbox.
      Prometheus scrapers now need effective operator read permission and receive
      a refusal when it is missing.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Telemetry documentation explains opt-in controls, inventory counts, and
      network-level IP handling. The local preview command is described as a preview
      from the current CLI process rather than a history of submitted data. These
      help and documentation corrections do not change payloads or consent defaults.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Bounded recursive session spawning is enabled by default, retaining depth,
      concurrency, target, and sandbox restrictions. Set maxSpawnDepth to 1 to retain
      leaf-only children. Tool scheduling respects sequential-only tools across Code
      Mode, Tool Search, and MCP while parallel-capable work can still run concurrently.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 14-safety-and-privacy-changes-in-v2026-9-3
  source_release: openclaw-2026-09-08-v2026-9-3-dfcfef48
  source_type: openclaw_changelog
  theme: safety-privacy
  title: 14 Safety and Privacy changes in v2026.9.3
  type: change
related_changes:
- '[[Changes/OpenClaw/2026-09-05-24-safety-and-privacy-changes-in-v2026-9-2|24 Safety
  and Privacy changes in v2026.9.2]]'
- '[[Changes/Claude Code/2026-09-08-3-safety-and-privacy-changes-in-v2-1-265|3 Safety
  and Privacy changes in v2.1.265]]'
- '[[Changes/Gemini CLI/2026-09-08-fix-core-enforce-fail-closed-workspace-trust-and-filter-mcpservers-in-restricted|fix(core):
  enforce fail-closed workspace trust and filter mcpServers in restricted mode]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-08-v2026-9-3-dfcfef48|openclaw-2026-09-08-v2026-9-3-dfcfef48]]'
source_type: openclaw_changelog
theme: safety-privacy
title: 14 Safety and Privacy changes in v2026.9.3
type: change
---

<!-- chronolog:begin region="header" -->
# 14 Safety and Privacy changes in v2026.9.3

**OpenClaw** · 2026-09-08 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.3) · from [[Releases/OpenClaw/openclaw-2026-09-08-v2026-9-3-dfcfef48|v2026.9.3]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Opening desktop or browser setup detects available providers without activating one until you choose it. Fresh native-conversation discovery starts unchecked, and cancelling or failing setup does not select a different provider. Guided setup can also finish without an AI provider. Saved consent choices survive reconciliation with an existing agent.

> A failed-update action can prepare a sanitized report for your review and submit it only with explicit consent. Missing GitHub authentication offers a browser handoff rather than sending anything automatically.

> Pairing notifications come from the approved channel account, and a notification failure does not undo the approval itself. Mattermost direct messages on private servers retain the account's existing network permission, Nostr honors positive relay acknowledgements, and failed iMessage helper pipes stop leaving pending requests waiting.

> Memory and Import Memory show agent-list errors with a usable retry instead of remaining in a loading cycle. Reads from additional memory folders report relevant permission or file errors, and skipped symlink roots point to their canonical directories without silently rewriting the configuration.

> Collection reviews are also instructed to look across related skills while preserving useful task boundaries. Compatible CLI backends, including Claude CLI, can perform these reviews within the permitted root using the existing sandbox and approval settings.

> The Mac and iOS apps now bring connected administrator settings into Dashboard while keeping connection setup and offline recovery in native controls. Older Gateways need the matching Dashboard support, and sensitive device-capability changes still require native consent.

> The Start Live Voice action opens the current chat and starts Talk from Siri or Shortcuts. Your phone still needs to be unlocked and the app in the foreground, with pairing, provider setup and microphone permission completed.

> Normal Apple Watch setup now includes voice authorization in the same connection action. Existing Watches connected only as nodes need to reconnect, and starting a voice conversation still requires Start and microphone permission.

> Native Ollama avoids silently truncating history when a conversation exceeds its available context. Its requests honor per-request sampling overrides, including explicit zero values, and retained reasoning stays with tool follow-ups without becoming visible answer text. Setup rejects models known to support embeddings alone before selecting them for chat. llama.cpp preparation also preserves configured preset defaults, comments and unmanaged options. Fresh llama.cpp installation allows time for the first macOS security check, and managed installs receive updated runtime binaries.

> Reports mark incomplete periods and source-coverage gaps, use UTC reporting windows, and remain behind Gateway authentication and operator read permission. Light and dark themes, GitHub avatars, and expandable activity lists help with browsing; collection still has documented limits, including omitted review-submission bodies and some historical commit and attribution cases. In an embedded tab, a theme choice follows in-tab navigation rather than being saved in browser storage.

> Permission checks stay attached to the account, agent, connection, and file they protect. Device capability requests remain available until you resolve them, Android honors approximate-location choices, and credential and runtime-context handling receive more narrowly scoped protections.

> Tool-policy groups use the same aliases and membership as core. Claude native Bash honors fully bindable exec allowlists under on-miss prompting while retaining deny and always-prompt behavior; an argument policy is not a sandbox. Prometheus scrapers now need effective operator read permission and receive a refusal when it is missing.

> Telemetry documentation explains opt-in controls, inventory counts, and network-level IP handling. The local preview command is described as a preview from the current CLI process rather than a history of submitted data. These help and documentation corrections do not change payloads or consent defaults.

> Bounded recursive session spawning is enabled by default, retaining depth, concurrency, target, and sandbox restrictions. Set maxSpawnDepth to 1 to retain leaf-only children. Tool scheduling respects sequential-only tools across Code Mode, Tool Search, and MCP while parallel-capable work can still run concurrently.

Source: https://docs.openclaw.ai/releases/2026.9.3
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-09-08-7-automation-and-scheduling-changes-in-v2026-9-3|7 Automation and Scheduling changes in v2026.9.3]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-09-08-10-memory-and-personalization-changes-in-v2026-9-3|10 Memory and Personalization changes in v2026.9.3]] · Memory and Personalization
- [[Changes/OpenClaw/2026-09-08-2-files-and-data-changes-in-v2026-9-3|2 Files and Data changes in v2026.9.3]] · Files and Data
- [[Changes/OpenClaw/2026-09-08-12-context-window-changes-in-v2026-9-3|12 Context Window changes in v2026.9.3]] · Context Window
- [[Changes/OpenClaw/2026-09-08-23-apps-and-integrations-changes-in-v2026-9-3|23 Apps and Integrations changes in v2026.9.3]] · Apps and Integrations
- [[Changes/OpenClaw/2026-09-08-ordinary-model-changes-now-apply-to-the-current-chat-by-default-including-admini|Ordinary model changes now apply to the current chat by default, including…]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-09-08-10-mobile-and-desktop-changes-in-v2026-9-3|10 Mobile and Desktop changes in v2026.9.3]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-09-08-4-reliability-and-performance-changes-in-v2026-9-3|4 Reliability and Performance changes in v2026.9.3]] · Reliability and Performance
- [[Changes/OpenClaw/2026-09-08-provider-adapters-preserve-initial-anthropic-text-and-thinking-keep-images-with|Provider adapters preserve initial Anthropic text and thinking, keep images…]] · Multimodal Input
- [[Changes/OpenClaw/2026-09-08-8-editor-experience-changes-in-v2026-9-3|8 Editor Experience changes in v2026.9.3]] · Editor Experience
- [[Changes/OpenClaw/2026-09-08-8-voice-and-audio-changes-in-v2026-9-3|8 Voice and Audio changes in v2026.9.3]] · Voice and Audio
- [[Changes/OpenClaw/2026-09-08-15-model-support-changes-in-v2026-9-3|15 Model Support changes in v2026.9.3]] · Model Support
- [[Changes/OpenClaw/2026-09-08-3-search-and-browsing-changes-in-v2026-9-3|3 Search and Browsing changes in v2026.9.3]] · Search and Browsing
- [[Changes/OpenClaw/2026-09-08-16-agent-mode-changes-in-v2026-9-3|16 Agent Mode changes in v2026.9.3]] · Agent Mode
- [[Changes/OpenClaw/2026-09-08-11-interface-experience-changes-in-v2026-9-3|11 Interface Experience changes in v2026.9.3]] · Interface Experience
- [[Changes/OpenClaw/2026-09-08-slack-delivers-valid-structured-sections-intact-even-when-their-accessibility-te|Slack delivers valid structured sections intact even when their accessibility text…]] · Accessibility and Localization
- [[Changes/OpenClaw/2026-09-08-4-collaboration-changes-in-v2026-9-3|4 Collaboration changes in v2026.9.3]] · Collaboration
- [[Changes/OpenClaw/2026-09-08-4-pricing-model-changes-in-v2026-9-3|4 Pricing Model changes in v2026.9.3]] · Pricing Model
- [[Changes/OpenClaw/2026-09-08-8-account-and-access-changes-in-v2026-9-3|8 Account and Access changes in v2026.9.3]] · Account and Access
- [[Changes/OpenClaw/2026-09-08-22-developer-workflow-changes-in-v2026-9-3|22 Developer Workflow changes in v2026.9.3]] · Developer Workflow
- [[Changes/OpenClaw/2026-09-08-77-other-changes-in-v2026-9-3|77 other changes in v2026.9.3]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-09-08 · Gemini CLI · [[Changes/Gemini CLI/2026-09-08-fix-core-enforce-fail-closed-workspace-trust-and-filter-mcpservers-in-restricted|fix(core): enforce fail-closed workspace trust and filter mcpServers in restricted mode]]
- Later: 2026-09-09 · Claude Code · [[Changes/Claude Code/2026-09-09-2-safety-and-privacy-changes-in-v2-1-267|2 Safety and Privacy changes in v2.1.267]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Descript · [[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke Application Access]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-08-e765e5&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-08-14-safety-and-privacy-changes-in-v2026-9-3.md%0ACard%20ID%3A%20openclaw-2026-09-08-e765e5%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.3%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->