---
card_id: open-webui-2026-10-14-1e9c23
date: '2026-10-14'
description: "Open WebUI · 2026-10-14 · Developer Workflow: 6 changes in v0.12.2 —
  \U0001F91D **Keep both changes when comparing.** The Compare revision view now has
  a Keep both…"
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1306
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 0bc927ac0d11e7add2778ce366639fbebf9293b245f13b9a7edb5dac4b087020
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-10-14-1e9c23
  comparison: ''
  date: '2026-10-14'
  description: 'Open WebUI — v0.12.2: 6 Developer Workflow changes'
  evidence:
  - quote: "\U0001F91D **Keep both changes when comparing.** The Compare revision
      view now has a Keep both button that puts the original and the proposed text
      of the selected change into the proposed revision, original first, so you no
      longer have to pick one side. [Commit](https://github.com/open-webui/open-webui/commit/97b7ed73c84767611d3a26d594c36f63619d92ea)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.2
  - quote: "\U0001F510 **Custom TLS certificate for Milvus.** Open WebUI can now connect
      to a Milvus server with a self-signed or company-issued TLS certificate by pointing
      the new \"MILVUS_SERVER_PEM_PATH\" environment variable at the certificate file,
      in normal and multi-tenancy mode. [#32427](https://github.com/open-webui/open-webui/pull/32427),
      [Commit](https://github.com/open-webui/open-webui/commit/3bc82bb2c110fc3ed7064e6107a4731b8d9ab5ae),
      [#31632](https://github.com/open-webui/open-webui/issues/31632)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.2
  - quote: "\U0001F5DD️ **Collection names checked as stored.** Retrieval access checks
      now compare collection names the way vector stores resolve them, ignoring letter
      case and treating hyphens and underscores alike, so a name written differently
      can no longer pass the check as something other than the collection that is
      then read. [#32435](https://github.com/open-webui/open-webui/pull/32435), [Commit](https://github.com/open-webui/open-webui/commit/30f3c49fb02c22269b42fe3b310209926ee7e8f9)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.2
  - quote: "\U0001F4DC **Long polling kept out of the audit log.** With websocket
      support turned off, every socket.io long polling request is no longer written
      to the audit log as its own entry, which flooded it and could not be filtered
      with AUDIT_EXCLUDED_PATHS, so the audit log looks the same with either transport.
      [#32425](https://github.com/open-webui/open-webui/pull/32425), [Commit](https://github.com/open-webui/open-webui/commit/209b15b9633c63ce1b7cf3c1fdc6e032d67978c6),
      [#31871](https://github.com/open-webui/open-webui/issues/31871)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.2
  - quote: "\U0001F4CE **Sources of approved tools.** With tool approval set to ask,
      a knowledge or file tool the user approved now saves and shows its sources below
      the reply, where they were lost after approval. [#32439](https://github.com/open-webui/open-webui/pull/32439),
      [Commit](https://github.com/open-webui/open-webui/commit/5fde0485a5adda046d283416a5c4c7a543d7a5fe),
      [#32436](https://github.com/open-webui/open-webui/issues/32436)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.2
  - quote: "\U0001F516 **Valkey connections tagged as Open WebUI.** Open WebUI's Valkey
      vector store connections now report their library name as GlidePySync(open-webui),
      so operators of a shared Valkey or ElastiCache can tell its traffic apart; this
      needs valkey-glide-sync 2.5.2 or newer, so installs that use VECTOR_DB=valkey
      with an older manually installed version must upgrade it, or startup fails.
      [#32428](https://github.com/open-webui/open-webui/pull/32428), [Commit](https://github.com/open-webui/open-webui/commit/980225e5823808de7ace86a8ee73a0b880b37023),
      [#31654](https://github.com/open-webui/open-webui/issues/31654)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.2
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 6-developer-workflow-changes-in-v0-12-2
  source_release: open-webui-2026-10-14-v0-12-2-github-413184477-0a3afe9d
  source_type: github_releases
  theme: developer-workflow
  title: 6 Developer Workflow changes in v0.12.2
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-10-13-background-shell-wait-status-no-longer-animates-when-no-foreground-work-is-runni|Background-shell
  wait status no longer animates when no foreground work is running]]'
- '[[Changes/Claude Code/2026-10-14-added-a-dir-prop-on-a-mod-s-text-for-right-to-left-text-on-windows-and-in-vs-cod|Added
  a dir prop on a mod''s Text for right-to-left text]]'
- '[[Changes/Claude Code/2026-10-14-10-developer-workflow-changes-in-v2-1-299|10 Developer
  Workflow changes in v2.1.299]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-10-14-v0-12-2-github-413184477-0a3afe9d|open-webui-2026-10-14-v0-12-2-github-413184477-0a3afe9d]]'
source_type: github_releases
theme: developer-workflow
title: 6 Developer Workflow changes in v0.12.2
type: change
---

<!-- chronolog:begin region="header" -->
# 6 Developer Workflow changes in v0.12.2

**Open WebUI** · 2026-10-14 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.12.2) · from [[Releases/Open WebUI/open-webui-2026-10-14-v0-12-2-github-413184477-0a3afe9d|v0.12.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🤝 **Keep both changes when comparing.** The Compare revision view now has a Keep both button that puts the original and the proposed text of the selected change into the proposed revision, original first, so you no longer have to pick one side. [Commit](https://github.com/open-webui/open-webui/commit/97b7ed73c84767611d3a26d594c36f63619d92ea)

> 🔐 **Custom TLS certificate for Milvus.** Open WebUI can now connect to a Milvus server with a self-signed or company-issued TLS certificate by pointing the new "MILVUS_SERVER_PEM_PATH" environment variable at the certificate file, in normal and multi-tenancy mode. [#32427](https://github.com/open-webui/open-webui/pull/32427), [Commit](https://github.com/open-webui/open-webui/commit/3bc82bb2c110fc3ed7064e6107a4731b8d9ab5ae), [#31632](https://github.com/open-webui/open-webui/issues/31632)

> 🗝️ **Collection names checked as stored.** Retrieval access checks now compare collection names the way vector stores resolve them, ignoring letter case and treating hyphens and underscores alike, so a name written differently can no longer pass the check as something other than the collection that is then read. [#32435](https://github.com/open-webui/open-webui/pull/32435), [Commit](https://github.com/open-webui/open-webui/commit/30f3c49fb02c22269b42fe3b310209926ee7e8f9)

> 📜 **Long polling kept out of the audit log.** With websocket support turned off, every socket.io long polling request is no longer written to the audit log as its own entry, which flooded it and could not be filtered with AUDIT_EXCLUDED_PATHS, so the audit log looks the same with either transport. [#32425](https://github.com/open-webui/open-webui/pull/32425), [Commit](https://github.com/open-webui/open-webui/commit/209b15b9633c63ce1b7cf3c1fdc6e032d67978c6), [#31871](https://github.com/open-webui/open-webui/issues/31871)

> 📎 **Sources of approved tools.** With tool approval set to ask, a knowledge or file tool the user approved now saves and shows its sources below the reply, where they were lost after approval. [#32439](https://github.com/open-webui/open-webui/pull/32439), [Commit](https://github.com/open-webui/open-webui/commit/5fde0485a5adda046d283416a5c4c7a543d7a5fe), [#32436](https://github.com/open-webui/open-webui/issues/32436)

> 🔖 **Valkey connections tagged as Open WebUI.** Open WebUI's Valkey vector store connections now report their library name as GlidePySync(open-webui), so operators of a shared Valkey or ElastiCache can tell its traffic apart; this needs valkey-glide-sync 2.5.2 or newer, so installs that use VECTOR_DB=valkey with an older manually installed version must upgrade it, or startup fails. [#32428](https://github.com/open-webui/open-webui/pull/32428), [Commit](https://github.com/open-webui/open-webui/commit/980225e5823808de7ace86a8ee73a0b880b37023), [#31654](https://github.com/open-webui/open-webui/issues/31654)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.12.2
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-10-14-open-attached-knowledge-from-its-preview-clicking-the-name-in-the-preview-of-an|📚 Open attached knowledge from its preview. Clicking the name in the preview…]] · Editor Experience
- [[Changes/Open WebUI/2026-10-14-general-improvements-various-improvements-were-implemented-across-the-applicatio|🔄 General improvements. Various improvements were implemented across…]] · Reliability and Performance
- [[Changes/Open WebUI/2026-10-14-automation-run-results-an-automation-run-is-now-recorded-as-successful-only-afte|⏰ Automation run results. An automation run is now recorded as successful only…]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-10-14-voice-on-android-chrome-voice-calls-and-dictation-on-android-chrome-no-longer-go|📱 Voice on Android Chrome. Voice calls and dictation on Android Chrome no longer…]] · Voice and Audio
- [[Changes/Open WebUI/2026-10-14-per-chat-terminal-file-actions-with-the-open-terminal-chat-context-set-to-per-ch|🖥️ Per chat terminal file actions. With the Open Terminal chat context set…]] · Context Window
- [[Changes/Open WebUI/2026-10-14-4-model-support-changes-in-v0-12-2|4 Model Support changes in v0.12.2]] · Model Support
- [[Changes/Open WebUI/2026-10-14-scim-cannot-delete-admins-an-identity-provider-can-no-longer-delete-administrato|👮 SCIM cannot delete admins. An identity provider can no longer delete…]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-10-14-2-interface-experience-changes-in-v0-12-2|2 Interface Experience changes in v0.12.2]] · Interface Experience
- [[Changes/Open WebUI/2026-10-14-memory-reindex-rate-limits-reindexing-memories-from-the-admin-reindex-knowledge|🧮 Memory reindex rate limits. Reindexing memories, from the admin Reindex…]] · Memory and Personalization
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-10-14 · Claude Code · [[Changes/Claude Code/2026-10-14-10-developer-workflow-changes-in-v2-1-299|10 Developer Workflow changes in v2.1.299]]
- Later: 2026-10-14 · Open WebUI · [[Changes/Open WebUI/2026-10-14-6-developer-workflow-changes-in-v0-12-1|6 Developer Workflow changes in v0.12.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-18 · Cursor · [[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-10-14-1e9c23&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-10-14-6-developer-workflow-changes-in-v0-12-2.md%0ACard%20ID%3A%20open-webui-2026-10-14-1e9c23%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.12.2%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->