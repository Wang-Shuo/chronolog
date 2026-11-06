---
card_id: cline-2026-08-14-32294f
date: '2026-08-14'
description: 'Cline · 2026-08-14 · Automation and Scheduling: Stop two Cline installations
  on different builds from shutting each other''s Hub daemon down in a loop, which…'
diffusion:
  first_in_tracked: '[[Changes/OpenHands/2024-09-04-better-syntax-error-loop-detection-by-tobitege-in-https-github-com-all-hands-ai|Better
    syntax error loop detection]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 709
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: automation-scheduling
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: change
machine_hash: 40bbadf918cd33034ebe71ff89637856b1240deb3addd1ee69b45f289bbd74de
product: cline
product_name: Cline
record:
  card_id: cline-2026-08-14-32294f
  comparison: ''
  date: '2026-08-14'
  description: 'Cline — v4.1.10: Stop two Cline installations on different builds
    from shutting each other''s Hub daemon down in a loop, which killed live sessions
    with an abnormal socket close. Build identity is now compared through a total
    order, so at most one side of a pair can decide to retire the other.'
  evidence:
  - quote: Stop two Cline installations on different builds from shutting each other's
      Hub daemon down in a loop, which killed live sessions with an abnormal socket
      close. Build identity is now compared through a total order, so at most one
      side of a pair can decide to retire the other.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.10
  extractor_version: fallback-v5
  impact: incremental
  kind: change
  product: cline
  product_name: Cline
  slug: stop-two-cline-installations-on-different-builds-from-shutting-each-other-s-hub
  source_release: cline-2026-08-14-v4-1-10-github-370718211-daf3638f
  source_type: github_releases
  theme: automation-scheduling
  theme_matches: []
  theme_resolution: manual-semantic-rule-v1
  title: Stop two Cline installations on different builds from shutting each other's
    Hub…
  type: change
related_changes:
- '[[Changes/Gemini CLI/2026-08-11-feat-caretaker-triage-implement-main-worker-execution-loop-and-egress-action-pub|feat(caretaker-triage):
  implement main worker execution loop and egress action publisher]]'
- '[[Changes/Claude Code/2026-08-13-pasted-and-clipboard-images-are-read-without-blocking-the-event-loop|Pasted
  and clipboard images are read without blocking the event loop]]'
- '[[Changes/OpenHands/2026-08-13-chore-bump-sdk-deps-software-agent-sdk-1-42-1-automation-1-7-1-typescript-client|chore:
  bump SDK deps…]]'
source_release: '[[Releases/Cline/cline-2026-08-14-v4-1-10-github-370718211-daf3638f|cline-2026-08-14-v4-1-10-github-370718211-daf3638f]]'
source_type: github_releases
theme: automation-scheduling
title: Stop two Cline installations on different builds from shutting each other's
  Hub…
type: change
---

<!-- chronolog:begin region="header" -->
# Stop two Cline installations on different builds from shutting each other's Hub…

**Cline** · 2026-08-14 · [[Themes/automation-scheduling|Automation and Scheduling]] · [Official source](https://github.com/cline/cline/releases/tag/v4.1.10) · from [[Releases/Cline/cline-2026-08-14-v4-1-10-github-370718211-daf3638f|v4.1.10]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Stop two Cline installations on different builds from shutting each other's Hub daemon down in a loop, which killed live sessions with an abnormal socket close. Build identity is now compared through a total order, so at most one side of a pair can decide to retire the other.
>
> Source: https://github.com/cline/cline/releases/tag/v4.1.10
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Cline/2026-08-14-everything-in-this-release-lands-through-the-sdk-bundle-so-it-applies-to-windows|Everything in this release lands through the SDK bundle, so it applies to windows…]] · Apps and Integrations
- [[Changes/Cline/2026-08-14-reclaim-idle-plugin-sandbox-processes-instead-of-leaving-them-running-for-the-li|Reclaim idle plugin sandbox processes instead of leaving them running for the life…]] · Safety and Privacy
- [[Changes/Cline/2026-08-14-2-model-support-changes-in-v4-1-10|2 Model Support changes in v4.1.10]] · Model Support
- [[Changes/Cline/2026-08-14-leave-a-hub-that-is-still-serving-sessions-in-place-instead-of-replacing-it-mid|Leave a Hub that is still serving sessions in place instead of replacing it mid-handshake]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Automation and Scheduling

- Earlier: 2026-08-13 · OpenHands · [[Changes/OpenHands/2026-08-13-chore-bump-sdk-deps-software-agent-sdk-1-42-1-automation-1-7-1-typescript-client|chore: bump SDK deps…]]
- Later: 2026-08-17 · OpenHands · [[Changes/OpenHands/2026-08-17-feat-automations-add-a-git-sync-page-by-vascosch92-in-https-github-com-openhands|feat(automations): add a Git Sync page]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2024-09-04 · OpenHands · [[Changes/OpenHands/2024-09-04-better-syntax-error-loop-detection-by-tobitege-in-https-github-com-all-hands-ai|Better syntax error loop detection]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20cline-2026-08-14-32294f&body=Card%3A%20Changes%2FCline%2F2026-08-14-stop-two-cline-installations-on-different-builds-from-shutting-each-other-s-hub.md%0ACard%20ID%3A%20cline-2026-08-14-32294f%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fcline%2Fcline%2Freleases%2Ftag%2Fv4.1.10%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->