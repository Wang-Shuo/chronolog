---
card_id: openclaw-2026-09-03-361033
date: '2026-09-03'
description: 'OpenClaw · 2026-09-03 · Mobile and Desktop: 10 changes in v2026.9.1
  — Doctor now says when a legacy WhatsApp acknowledgement setting could not survive…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-11-11-command-r-to-insert-a-speaker-label-ctrl-r-on-windows|command
    + R to insert a speaker label (ctrl + R on Windows)]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2853
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: mobile-desktop
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: f17c863313ab88cec5fef7a4e47e73484f3433b33dba4d991e0b19fb9b4013ec
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-03-361033
  comparison: ''
  date: '2026-09-03'
  description: 'OpenClaw — v2026.9.1: 10 Mobile and Desktop changes'
  evidence:
  - quote: Doctor now says when a legacy WhatsApp acknowledgement setting could not
      survive migration exactly as written. It identifies a shadowed emoji, shows
      which shared emoji remains active, and warns when the old acknowledgement scope
      changes or cannot be represented so operators can review messages.ackReactionScope
      instead of accepting a misleading clean migration.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: The 9.1 native experience brings everyday conversation controls into reachable
      places. Conceptual illustration, not a screenshot. Conceptual feature map—not
      an Android screenshot. No current native UI is presented as historical 9.1 evidence.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Mermaid diagrams no longer have to be read as raw code in supported native
      chats. Android and iOS render completed diagrams inline with source, copy, retry,
      and expanded-preview controls, while macOS brings diagrams to both full chat
      and Quick Chat and keeps that window open while a larger preview is in use.
      Each app keeps readable source for streaming, invalid, oversized, or temporarily
      failed diagrams instead of replacing it with an empty box.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Android now keeps the replacement Gateway connection in charge while an
      older connection finishes shutting down, so retired cleanup is less likely to
      publish a false offline state or discard an accepted request outcome. Messages
      acknowledged after reconnect move past Sending, a new conversation remains selected
      for the next message, later queued sends keep moving, and a queued message you
      delete stays gone even if an older refresh finishes afterward.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: The same ownership cleanup reaches other native conversation paths. Apple
      chat can retry immediately after a session-settings failure, iPhone history
      refreshes reconcile a streamed reply with its canonical transcript row instead
      of leaving an older duplicate, and native session progress cards retain the
      selected agent and workspace context.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Fresh Linux desktop installs can again choose a Gateway on another computer
      before installing a local CLI, while local setup keeps its existing installer
      path. The desktop companion also receives a compatible local-discovery refresh,
      with its Windows updater deliberately held on the earlier version until an upstream
      cleanup conflict is resolved.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Source-built Docker images now include the WhatsApp runtime when it is
      explicitly selected, rather than accepting the choice and producing an image
      without the channel. Existing QQ Bot installs recorded under the former @openclaw/qqbot
      package can move to @tencent-connect/openclaw-qqbot 2.0.3 while preserving channel
      configuration and credentials, with failed updates leaving the working legacy
      record in place.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: These protections are scoped to the named Doctor, iOS, and configuration-response
      paths. Snapshot redaction does not change stored configuration or migration
      inputs, and it does not repair the separate startup or runtime corruption symptoms
      that were not reproduced by the configuration fix.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Android masks Gateway credentials and secret replies, preserves intentional
      whitespace, and returns to ordinary input after a sensitive step. Linux Gateway
      reinstall and uninstall also remove reusable credentials from managed systemd
      backups, restrict retained files to their owner, and let Doctor identify unsafe
      remnants without printing their contents.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Gateway clients that require a verified role now stop endless reconnects
      and show the applicable trusted-proxy, Tailscale, token, or password recovery
      path. Rejected mobile setup codes point users toward a fresh code and the paired-device
      list instead of encouraging reuse.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 10-mobile-and-desktop-changes-in-v2026-9-1
  source_release: openclaw-2026-09-03-v2026-9-1-281124fc
  source_type: openclaw_changelog
  theme: mobile-desktop
  title: 10 Mobile and Desktop changes in v2026.9.1
  type: change
related_changes:
- '[[Changes/Lovable/2026-09-02-download-the-mobile-app-from-your-settings|Download
  the mobile app from your settings]]'
- '[[Changes/Claude Code/2026-09-03-3-mobile-and-desktop-changes-in-v2-1-260|3 Mobile
  and Desktop changes in v2.1.260]]'
- '[[Changes/Codex CLI/2026-09-03-42068-https-github-com-openai-codex-pull-42068-detect-standalone-installs-from-t|♯42068((source
  link) Detect standalone installs…]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-03-v2026-9-1-281124fc|openclaw-2026-09-03-v2026-9-1-281124fc]]'
source_type: openclaw_changelog
theme: mobile-desktop
title: 10 Mobile and Desktop changes in v2026.9.1
type: change
---

<!-- chronolog:begin region="header" -->
# 10 Mobile and Desktop changes in v2026.9.1

**OpenClaw** · 2026-09-03 · [[Themes/mobile-desktop|Mobile and Desktop]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.1) · from [[Releases/OpenClaw/openclaw-2026-09-03-v2026-9-1-281124fc|v2026.9.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Doctor now says when a legacy WhatsApp acknowledgement setting could not survive migration exactly as written. It identifies a shadowed emoji, shows which shared emoji remains active, and warns when the old acknowledgement scope changes or cannot be represented so operators can review messages.ackReactionScope instead of accepting a misleading clean migration.

> The 9.1 native experience brings everyday conversation controls into reachable places. Conceptual illustration, not a screenshot. Conceptual feature map—not an Android screenshot. No current native UI is presented as historical 9.1 evidence.

> Mermaid diagrams no longer have to be read as raw code in supported native chats. Android and iOS render completed diagrams inline with source, copy, retry, and expanded-preview controls, while macOS brings diagrams to both full chat and Quick Chat and keeps that window open while a larger preview is in use. Each app keeps readable source for streaming, invalid, oversized, or temporarily failed diagrams instead of replacing it with an empty box.

> Android now keeps the replacement Gateway connection in charge while an older connection finishes shutting down, so retired cleanup is less likely to publish a false offline state or discard an accepted request outcome. Messages acknowledged after reconnect move past Sending, a new conversation remains selected for the next message, later queued sends keep moving, and a queued message you delete stays gone even if an older refresh finishes afterward.

> The same ownership cleanup reaches other native conversation paths. Apple chat can retry immediately after a session-settings failure, iPhone history refreshes reconcile a streamed reply with its canonical transcript row instead of leaving an older duplicate, and native session progress cards retain the selected agent and workspace context.

> Fresh Linux desktop installs can again choose a Gateway on another computer before installing a local CLI, while local setup keeps its existing installer path. The desktop companion also receives a compatible local-discovery refresh, with its Windows updater deliberately held on the earlier version until an upstream cleanup conflict is resolved.

> Source-built Docker images now include the WhatsApp runtime when it is explicitly selected, rather than accepting the choice and producing an image without the channel. Existing QQ Bot installs recorded under the former @openclaw/qqbot package can move to @tencent-connect/openclaw-qqbot 2.0.3 while preserving channel configuration and credentials, with failed updates leaving the working legacy record in place.

> These protections are scoped to the named Doctor, iOS, and configuration-response paths. Snapshot redaction does not change stored configuration or migration inputs, and it does not repair the separate startup or runtime corruption symptoms that were not reproduced by the configuration fix.

> Android masks Gateway credentials and secret replies, preserves intentional whitespace, and returns to ordinary input after a sensitive step. Linux Gateway reinstall and uninstall also remove reusable credentials from managed systemd backups, restrict retained files to their owner, and let Doctor identify unsafe remnants without printing their contents.

> Gateway clients that require a verified role now stop endless reconnects and show the applicable trusted-proxy, Tailscale, token, or password recovery path. Rejected mobile setup codes point users toward a fresh code and the paired-device list instead of encouraging reuse.

Source: https://docs.openclaw.ai/releases/2026.9.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-09-03-14-agent-mode-changes-in-v2026-9-1|14 Agent Mode changes in v2026.9.1]] · Agent Mode
- [[Changes/OpenClaw/2026-09-03-12-voice-and-audio-changes-in-v2026-9-1|12 Voice and Audio changes in v2026.9.1]] · Voice and Audio
- [[Changes/OpenClaw/2026-09-03-2-files-and-data-changes-in-v2026-9-1|2 Files and Data changes in v2026.9.1]] · Files and Data
- [[Changes/OpenClaw/2026-09-03-7-collaboration-changes-in-v2026-9-1|7 Collaboration changes in v2026.9.1]] · Collaboration
- [[Changes/OpenClaw/2026-09-03-19-memory-and-personalization-changes-in-v2026-9-1|19 Memory and Personalization changes in v2026.9.1]] · Memory and Personalization
- [[Changes/OpenClaw/2026-09-03-3-editor-experience-changes-in-v2026-9-1|3 Editor Experience changes in v2026.9.1]] · Editor Experience
- [[Changes/OpenClaw/2026-09-03-2-search-and-browsing-changes-in-v2026-9-1|2 Search and Browsing changes in v2026.9.1]] · Search and Browsing
- [[Changes/OpenClaw/2026-09-03-12-account-and-access-changes-in-v2026-9-1|12 Account and Access changes in v2026.9.1]] · Account and Access
- [[Changes/OpenClaw/2026-09-03-several-less-visible-repairs-keep-the-apps-from-failing-around-dependencies-and|Several less visible repairs keep the apps from failing around dependencies…]] · Multimodal Input
- [[Changes/OpenClaw/2026-09-03-13-automation-and-scheduling-changes-in-v2026-9-1|13 Automation and Scheduling changes in v2026.9.1]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-09-03-an-update-or-doctor-repair-now-does-more-to-preserve-the-setup-you-already-autho|An update or Doctor repair now does more to preserve the setup you already authored…]] · Projects and Workspaces
- [[Changes/OpenClaw/2026-09-03-11-developer-workflow-changes-in-v2026-9-1|11 Developer Workflow changes in v2026.9.1]] · Developer Workflow
- [[Changes/OpenClaw/2026-09-03-3-accessibility-and-localization-changes-in-v2026-9-1|3 Accessibility and Localization changes in v2026.9.1]] · Accessibility and Localization
- [[Changes/OpenClaw/2026-09-03-26-apps-and-integrations-changes-in-v2026-9-1|26 Apps and Integrations changes in v2026.9.1]] · Apps and Integrations
- [[Changes/OpenClaw/2026-09-03-10-safety-and-privacy-changes-in-v2026-9-1|10 Safety and Privacy changes in v2026.9.1]] · Safety and Privacy
- [[Changes/OpenClaw/2026-09-03-11-context-window-changes-in-v2026-9-1|11 Context Window changes in v2026.9.1]] · Context Window
- [[Changes/OpenClaw/2026-09-03-12-model-support-changes-in-v2026-9-1|12 Model Support changes in v2026.9.1]] · Model Support
- [[Changes/OpenClaw/2026-09-03-14-interface-experience-changes-in-v2026-9-1|14 Interface Experience changes in v2026.9.1]] · Interface Experience
- [[Changes/OpenClaw/2026-09-03-on-linux-managed-local-model-and-embedding-services-are-preferred-as-the-out-of|On Linux, managed local model and embedding services are preferred…]] · Reliability and Performance
- [[Changes/OpenClaw/2026-09-03-32-other-changes-in-v2026-9-1|32 other changes in v2026.9.1]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Mobile and Desktop

- Earlier: 2026-09-03 · Codex CLI · [[Changes/Codex CLI/2026-09-03-42068-https-github-com-openai-codex-pull-42068-detect-standalone-installs-from-t|♯42068((source link) Detect standalone installs…]]
- Later: 2026-09-03 · Superwhisper · [[Changes/Superwhisper/2026-09-03-many-other-macos-27-fixes|Many other macOS 27 fixes]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-11-11 · Descript · [[Changes/Descript/2018-11-11-command-r-to-insert-a-speaker-label-ctrl-r-on-windows|command + R to insert a speaker label (ctrl + R on Windows)]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-03-361033&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-03-10-mobile-and-desktop-changes-in-v2026-9-1.md%0ACard%20ID%3A%20openclaw-2026-09-03-361033%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->