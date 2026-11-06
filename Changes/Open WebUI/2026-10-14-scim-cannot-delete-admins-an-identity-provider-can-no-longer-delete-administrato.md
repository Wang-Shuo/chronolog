---
card_id: open-webui-2026-10-14-d7c308
date: '2026-10-14'
description: "Open WebUI · 2026-10-14 · Enterprise and Administration: \U0001F46E
  **SCIM cannot delete admins.** An identity provider can no longer delete administrator
  accounts…"
diffusion:
  first_in_tracked: '[[Changes/Gemini/2023-05-05-access-for-google-workspace-accounts|Access
    for Google Workspace accounts]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1258
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: enterprise-admin
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: change
machine_hash: 87552294c16bd4834df10de51fd52c62b39c3f09f798c7694e58de33dd5cbe30
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-10-14-d7c308
  comparison: ''
  date: '2026-10-14'
  description: "Open WebUI — v0.12.2: \U0001F46E **SCIM cannot delete admins.** An
    identity provider can no longer delete administrator accounts, including the first
    admin, through a SCIM delete request, which now answers with 403 and leaves the
    account in place, so a sync that prunes unassigned users can no longer leave the
    instance without an administrator; admins are removed in the admin panel. [#32415](https://github.com/open-webui/open-webui/pull/32415),
    [Commit](https://github.com/open-webui/open-webui/commit/6276e81cec38f5c5cce067e4be905c5710c2d7d6),
    [#27662](https://github.com/open-webui/open-webui/issues/27662)"
  evidence:
  - quote: "\U0001F46E **SCIM cannot delete admins.** An identity provider can no
      longer delete administrator accounts, including the first admin, through a SCIM
      delete request, which now answers with 403 and leaves the account in place,
      so a sync that prunes unassigned users can no longer leave the instance without
      an administrator; admins are removed in the admin panel. [#32415](https://github.com/open-webui/open-webui/pull/32415),
      [Commit](https://github.com/open-webui/open-webui/commit/6276e81cec38f5c5cce067e4be905c5710c2d7d6),
      [#27662](https://github.com/open-webui/open-webui/issues/27662)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.2
  extractor_version: fallback-v5
  impact: incremental
  kind: change
  product: open-webui
  product_name: Open WebUI
  slug: scim-cannot-delete-admins-an-identity-provider-can-no-longer-delete-administrato
  source_release: open-webui-2026-10-14-v0-12-2-github-413184477-0a3afe9d
  source_type: github_releases
  theme: enterprise-admin
  title: "\U0001F46E **SCIM cannot delete admins.** An identity provider can no longer
    delete…"
  type: change
related_changes:
- '[[Changes/Open WebUI/2026-10-10-5-enterprise-and-administration-changes-in-v0-12-0|5
  Enterprise and Administration changes in v0.12.0]]'
- '[[Changes/GitHub Copilot CLI/2026-10-12-keep-allow-all-available-during-startup-while-enterprise-policy-is-still-resolvi|Keep
  /allow-all available during startup while enterprise policy is still resolving]]'
- "[[Changes/Open WebUI/2026-10-14-translated-model-prompt-suggestions-editing-the-prompt-suggestions-of-a-model-th|\U0001F4AC
  Translated model prompt suggestions. Editing the prompt suggestions of a model…]]"
source_release: '[[Releases/Open WebUI/open-webui-2026-10-14-v0-12-2-github-413184477-0a3afe9d|open-webui-2026-10-14-v0-12-2-github-413184477-0a3afe9d]]'
source_type: github_releases
theme: enterprise-admin
title: "\U0001F46E SCIM cannot delete admins. An identity provider can no longer delete…"
type: change
---

<!-- chronolog:begin region="header" -->
# 👮 **SCIM cannot delete admins.** An identity provider can no longer delete…

**Open WebUI** · 2026-10-14 · [[Themes/enterprise-admin|Enterprise and Administration]] · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.12.2) · from [[Releases/Open WebUI/open-webui-2026-10-14-v0-12-2-github-413184477-0a3afe9d|v0.12.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> 👮 **SCIM cannot delete admins.** An identity provider can no longer delete administrator accounts, including the first admin, through a SCIM delete request, which now answers with 403 and leaves the account in place, so a sync that prunes unassigned users can no longer leave the instance without an administrator; admins are removed in the admin panel. [#32415](https://github.com/open-webui/open-webui/pull/32415), [Commit](https://github.com/open-webui/open-webui/commit/6276e81cec38f5c5cce067e4be905c5710c2d7d6), [#27662](https://github.com/open-webui/open-webui/issues/27662)
>
> Source: https://github.com/open-webui/open-webui/releases/tag/v0.12.2
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-10-14-open-attached-knowledge-from-its-preview-clicking-the-name-in-the-preview-of-an|📚 Open attached knowledge from its preview. Clicking the name in the preview…]] · Editor Experience
- [[Changes/Open WebUI/2026-10-14-6-developer-workflow-changes-in-v0-12-2|6 Developer Workflow changes in v0.12.2]] · Developer Workflow
- [[Changes/Open WebUI/2026-10-14-general-improvements-various-improvements-were-implemented-across-the-applicatio|🔄 General improvements. Various improvements were implemented across…]] · Reliability and Performance
- [[Changes/Open WebUI/2026-10-14-automation-run-results-an-automation-run-is-now-recorded-as-successful-only-afte|⏰ Automation run results. An automation run is now recorded as successful only…]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-10-14-voice-on-android-chrome-voice-calls-and-dictation-on-android-chrome-no-longer-go|📱 Voice on Android Chrome. Voice calls and dictation on Android Chrome no longer…]] · Voice and Audio
- [[Changes/Open WebUI/2026-10-14-per-chat-terminal-file-actions-with-the-open-terminal-chat-context-set-to-per-ch|🖥️ Per chat terminal file actions. With the Open Terminal chat context set…]] · Context Window
- [[Changes/Open WebUI/2026-10-14-4-model-support-changes-in-v0-12-2|4 Model Support changes in v0.12.2]] · Model Support
- [[Changes/Open WebUI/2026-10-14-2-interface-experience-changes-in-v0-12-2|2 Interface Experience changes in v0.12.2]] · Interface Experience
- [[Changes/Open WebUI/2026-10-14-memory-reindex-rate-limits-reindexing-memories-from-the-admin-reindex-knowledge|🧮 Memory reindex rate limits. Reindexing memories, from the admin Reindex…]] · Memory and Personalization
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Enterprise and Administration

- Earlier: 2026-10-14 · Open WebUI · [[Changes/Open WebUI/2026-10-14-translated-model-prompt-suggestions-editing-the-prompt-suggestions-of-a-model-th|💬 Translated model prompt suggestions. Editing the prompt suggestions of a model…]]
- Later: 2026-10-15 · ChatGPT · [[Changes/ChatGPT/2026-10-15-applications-are-now-open-to-labs-at-u-s-universities-if-you-re-a-principal-inve|Applications are now open to labs at U.S. universities]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-05-05 · Gemini · [[Changes/Gemini/2023-05-05-access-for-google-workspace-accounts|Access for Google Workspace accounts]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-10-14-d7c308&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-10-14-scim-cannot-delete-admins-an-identity-provider-can-no-longer-delete-administrato.md%0ACard%20ID%3A%20open-webui-2026-10-14-d7c308%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.12.2%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->