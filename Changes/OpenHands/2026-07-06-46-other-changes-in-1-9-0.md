---
card_id: openhands-2026-07-06-fa2714
date: '2026-07-06'
description: 'OpenHands · 2026-07-06 · Other changes: 46 changes in 1.9.0 — feat:
  move existing users into the default org when first auto-added by @ak684 in…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 433d289f58e8bb163d83f0d28b00a4fd06a72817ab45c728b3f834dfd14ca824
product: openhands
product_name: OpenHands
record:
  card_id: openhands-2026-07-06-fa2714
  comparison: ''
  date: '2026-07-06'
  description: 'OpenHands — 1.9.0: 46 other changes'
  evidence:
  - quote: 'feat: move existing users into the default org when first auto-added by
      @ak684 in https://github.com/OpenHands/OpenHands/pull/14740'
    source_release: https://github.com/OpenHands/OpenHands/releases/tag/1.9.0
  - quote: 'feat: add hide_personal_workspaces flag for org-only OHE installs by @ak684
      in https://github.com/OpenHands/OpenHands/pull/14741'
    source_release: https://github.com/OpenHands/OpenHands/releases/tag/1.9.0
  - quote: 'feat: make the first signed-in user the default org owner, track the org
      by is_default flag by @ak684 in https://github.com/OpenHands/OpenHands/pull/14752'
    source_release: https://github.com/OpenHands/OpenHands/releases/tag/1.9.0
  - quote: 'feat: add validation for secret names to ensure valid env var format by
      @jpshackelford in https://github.com/OpenHands/OpenHands/pull/12980'
    source_release: https://github.com/OpenHands/OpenHands/releases/tag/1.9.0
  - quote: 'feat: auto-accept invitation links instead of the confirm/cancel modal
      by @ak684 in https://github.com/OpenHands/OpenHands/pull/14786'
    source_release: https://github.com/OpenHands/OpenHands/releases/tag/1.9.0
  - quote: 'feat: expose copyable invite links so invitations work without email delivery
      by @ak684 in https://github.com/OpenHands/OpenHands/pull/14758'
    source_release: https://github.com/OpenHands/OpenHands/releases/tag/1.9.0
  - quote: 'feat: enforce conversation limits by @HeyItsChloe in https://github.com/OpenHands/OpenHands/pull/14168'
    source_release: https://github.com/OpenHands/OpenHands/releases/tag/1.9.0
  - quote: 'feat: add DynamicRemoteSandboxSpecService backed by runtime-api warm configs
      by @tofarr in https://github.com/OpenHands/OpenHands/pull/14849'
    source_release: https://github.com/OpenHands/OpenHands/releases/tag/1.9.0
  - quote: 'feat: PLTF-2956 parallelize GitHub GraphQL queries in get_suggested_tasks
      by @aivong-openhands in https://github.com/OpenHands/OpenHands/pull/14821'
    source_release: https://github.com/OpenHands/OpenHands/releases/tag/1.9.0
  - quote: 'feat: PLTF-2968 allow per-deployment resolver macro via OH_RESOLVER_LABEL
      by @aivong-openhands in https://github.com/OpenHands/OpenHands/pull/14895'
    source_release: https://github.com/OpenHands/OpenHands/releases/tag/1.9.0
  - quote: 'feat(azure-devops): add resolver mentions + org-level one-click webhook
      setup by @ak684 in https://github.com/OpenHands/OpenHands/pull/14991'
    source_release: https://github.com/OpenHands/OpenHands/releases/tag/1.9.0
  - quote: 'feat: implement semantic file chunking using tree-sitter AST parsing by
      @ysinghc in https://github.com/OpenHands/OpenHands/pull/14699'
    source_release: https://github.com/OpenHands/OpenHands/releases/tag/1.9.0
  - quote: 'feat(org): Add organization conversation admin dashboard by @saurya in
      https://github.com/OpenHands/OpenHands/pull/14846'
    source_release: https://github.com/OpenHands/OpenHands/releases/tag/1.9.0
  - quote: 'feat(app-server): capture production workspace state — initial snapshot
      at start + archive before delete (APP-2403) by @simonrosenberg in https://github.com/OpenHands/OpenHands/pull/14953'
    source_release: https://github.com/OpenHands/OpenHands/releases/tag/1.9.0
  - quote: 'feat(device-verify): align warning, button color, and add workspace dropdown
      by @tofarr in https://github.com/OpenHands/OpenHands/pull/15031'
    source_release: https://github.com/OpenHands/OpenHands/releases/tag/1.9.0
  - quote: 'feat(org): expose caller permissions on GET /organizations/{id}/me by
      @VascoSch92 in https://github.com/OpenHands/OpenHands/pull/15048'
    source_release: https://github.com/OpenHands/OpenHands/releases/tag/1.9.0
  - quote: 'feat(api-keys): add optional active window (not_before & expires_at) by
      @tofarr in https://github.com/OpenHands/OpenHands/pull/15085'
    source_release: https://github.com/OpenHands/OpenHands/releases/tag/1.9.0
  - quote: 'feat(app-server): add repo/branch to Laminar trace metadata by @simonrosenberg
      in https://github.com/OpenHands/OpenHands/pull/15059'
    source_release: https://github.com/OpenHands/OpenHands/releases/tag/1.9.0
  - quote: 'feat(api-keys): make ''unbound'' org scope an explicit, first-class option
      by @tofarr in https://github.com/OpenHands/OpenHands/pull/15096'
    source_release: https://github.com/OpenHands/OpenHands/releases/tag/1.9.0
  - quote: 'feat(saas-auth): accept api_key cookie as a fallback credential by @tofarr
      in https://github.com/OpenHands/OpenHands/pull/15101'
    source_release: https://github.com/OpenHands/OpenHands/releases/tag/1.9.0
  - quote: 'fix: Fix CVE-2026-48526: Update pyjwt to 2.13.0 by @mamoodi in https://github.com/OpenHands/OpenHands/pull/14854'
    source_release: https://github.com/OpenHands/OpenHands/releases/tag/1.9.0
  - quote: 'fix: Fix CVE-2026-49855: Update tornado to 6.5.7 by @mamoodi in https://github.com/OpenHands/OpenHands/pull/14856'
    source_release: https://github.com/OpenHands/OpenHands/releases/tag/1.9.0
  - quote: 'fix: Fix CVE-2026-54278: Update aiohttp to 3.14.1 by @mamoodi in https://github.com/OpenHands/OpenHands/pull/14871'
    source_release: https://github.com/OpenHands/OpenHands/releases/tag/1.9.0
  - quote: 'fix: Fix CVE-2026-12143: Update form-data to 4.0.6 by @mamoodi in https://github.com/OpenHands/OpenHands/pull/14875'
    source_release: https://github.com/OpenHands/OpenHands/releases/tag/1.9.0
  - quote: 'fix: Fix CVE-2026-53539: Update python-multipart to >=0.0.30 by @mamoodi
      in https://github.com/OpenHands/OpenHands/pull/14876'
    source_release: https://github.com/OpenHands/OpenHands/releases/tag/1.9.0
  - quote: 'fix: Fix CVE-2026-45409: Update idna to 3.15 by @mamoodi in https://github.com/OpenHands/OpenHands/pull/14946'
    source_release: https://github.com/OpenHands/OpenHands/releases/tag/1.9.0
  - quote: 'fix: Fix CVE-2026-49458: Update dompurify to 3.4.6 by @mamoodi in https://github.com/OpenHands/OpenHands/pull/14872'
    source_release: https://github.com/OpenHands/OpenHands/releases/tag/1.9.0
  - quote: 'fix: Fix CVE-2026-44727: Update jupyter-server to 2.20.0 by @mamoodi in
      https://github.com/OpenHands/OpenHands/pull/14943'
    source_release: https://github.com/OpenHands/OpenHands/releases/tag/1.9.0
  - quote: 'fix: Fix CVE-2026-41691: Update i18next-http-backend to 3.0.5 by @mamoodi
      in https://github.com/OpenHands/OpenHands/pull/14955'
    source_release: https://github.com/OpenHands/OpenHands/releases/tag/1.9.0
  - quote: 'fix: Fix CVE-2026-54283: Update starlette to 1.3.1 by @mamoodi in https://github.com/OpenHands/OpenHands/pull/14874'
    source_release: https://github.com/OpenHands/OpenHands/releases/tag/1.9.0
  - quote: 'fix: Fix CVE-2026-8723: Update qs to 6.15.2 by @mamoodi in https://github.com/OpenHands/OpenHands/pull/14957'
    source_release: https://github.com/OpenHands/OpenHands/releases/tag/1.9.0
  - quote: 'fix: Fix CVE-2026-54285: Update @opentelemetry/core to 2.8.0 by @mamoodi
      in https://github.com/OpenHands/OpenHands/pull/14980'
    source_release: https://github.com/OpenHands/OpenHands/releases/tag/1.9.0
  - quote: 'fix: Fix CVE-2026-48712: Update protobufjs to 7.6.4 by @mamoodi in https://github.com/OpenHands/OpenHands/pull/14981'
    source_release: https://github.com/OpenHands/OpenHands/releases/tag/1.9.0
  - quote: 'fix: Fix CVE-2026-48779: Update ws to 8.21.0 by @mamoodi in https://github.com/OpenHands/OpenHands/pull/15007'
    source_release: https://github.com/OpenHands/OpenHands/releases/tag/1.9.0
  - quote: 'fix: Fix CVE-2026-44681: Update authlib to >=1.6.12 by @mamoodi in https://github.com/OpenHands/OpenHands/pull/14983'
    source_release: https://github.com/OpenHands/OpenHands/releases/tag/1.9.0
  - quote: 'docs: revise source code links in README.md by @enyst in https://github.com/OpenHands/OpenHands/pull/14869'
    source_release: https://github.com/OpenHands/OpenHands/releases/tag/1.9.0
  - quote: 'chore(deps): bump pyjwt from 2.12.1 to 2.13.0 by @dependabot[bot] in https://github.com/OpenHands/OpenHands/pull/14852'
    source_release: https://github.com/OpenHands/OpenHands/releases/tag/1.9.0
  - quote: 'test: replace real sleeps in maintenance runner tests by @aivong-openhands
      in https://github.com/OpenHands/OpenHands/pull/13930'
    source_release: https://github.com/OpenHands/OpenHands/releases/tag/1.9.0
  - quote: 'chore(main): release cloud 1.39.0 by @openhands-release-bot[bot] in https://github.com/OpenHands/OpenHands/pull/14748'
    source_release: https://github.com/OpenHands/OpenHands/releases/tag/1.9.0
  - quote: 'chore(deps-dev): bump jupyterlab from 4.5.7 to 4.5.9 by @dependabot[bot]
      in https://github.com/OpenHands/OpenHands/pull/15009'
    source_release: https://github.com/OpenHands/OpenHands/releases/tag/1.9.0
  - quote: 'chore(main): release cloud 1.40.0 by @openhands-release-bot[bot] in https://github.com/OpenHands/OpenHands/pull/14969'
    source_release: https://github.com/OpenHands/OpenHands/releases/tag/1.9.0
  - quote: 'build: pin dependency versions exactly by @rbren in https://github.com/OpenHands/OpenHands/pull/14384'
    source_release: https://github.com/OpenHands/OpenHands/releases/tag/1.9.0
  - quote: 'ci: add release ready gate by @enyst in https://github.com/OpenHands/OpenHands/pull/14987'
    source_release: https://github.com/OpenHands/OpenHands/releases/tag/1.9.0
  - quote: Release 1.8.0 by @mamoodi in https://github.com/OpenHands/OpenHands/pull/14743
    source_release: https://github.com/OpenHands/OpenHands/releases/tag/1.9.0
  - quote: 'ci: adopt release-please for app and cloud releases by @jlav in https://github.com/OpenHands/OpenHands/pull/14718'
    source_release: https://github.com/OpenHands/OpenHands/releases/tag/1.9.0
  - quote: Use reusable issue duplicate checker action by @enyst in https://github.com/OpenHands/OpenHands/pull/14609
    source_release: https://github.com/OpenHands/OpenHands/releases/tag/1.9.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openhands
  product_name: OpenHands
  slug: 46-other-changes-in-1-9-0
  source_release: openhands-2026-07-06-1-9-0-github-349633843-8010776a
  source_type: github_releases
  theme: uncategorized
  title: 46 other changes in 1.9.0
  type: change
source_release: '[[Releases/OpenHands/openhands-2026-07-06-1-9-0-github-349633843-8010776a|openhands-2026-07-06-1-9-0-github-349633843-8010776a]]'
source_type: github_releases
theme: uncategorized
title: 46 other changes in 1.9.0
type: change
---

<!-- chronolog:begin region="header" -->
# 46 other changes in 1.9.0

**OpenHands** · 2026-07-06 · Other changes · Digest · [Official source](https://github.com/OpenHands/OpenHands/releases/tag/1.9.0) · from [[Releases/OpenHands/openhands-2026-07-06-1-9-0-github-349633843-8010776a|1.9.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> feat: move existing users into the default org when first auto-added by @ak684 in https://github.com/OpenHands/OpenHands/pull/14740

> feat: add hide_personal_workspaces flag for org-only OHE installs by @ak684 in https://github.com/OpenHands/OpenHands/pull/14741

> feat: make the first signed-in user the default org owner, track the org by is_default flag by @ak684 in https://github.com/OpenHands/OpenHands/pull/14752

> feat: add validation for secret names to ensure valid env var format by @jpshackelford in https://github.com/OpenHands/OpenHands/pull/12980

> feat: auto-accept invitation links instead of the confirm/cancel modal by @ak684 in https://github.com/OpenHands/OpenHands/pull/14786

> feat: expose copyable invite links so invitations work without email delivery by @ak684 in https://github.com/OpenHands/OpenHands/pull/14758

> feat: enforce conversation limits by @HeyItsChloe in https://github.com/OpenHands/OpenHands/pull/14168

> feat: add DynamicRemoteSandboxSpecService backed by runtime-api warm configs by @tofarr in https://github.com/OpenHands/OpenHands/pull/14849

> feat: PLTF-2956 parallelize GitHub GraphQL queries in get_suggested_tasks by @aivong-openhands in https://github.com/OpenHands/OpenHands/pull/14821

> feat: PLTF-2968 allow per-deployment resolver macro via OH_RESOLVER_LABEL by @aivong-openhands in https://github.com/OpenHands/OpenHands/pull/14895

> feat(azure-devops): add resolver mentions + org-level one-click webhook setup by @ak684 in https://github.com/OpenHands/OpenHands/pull/14991

> feat: implement semantic file chunking using tree-sitter AST parsing by @ysinghc in https://github.com/OpenHands/OpenHands/pull/14699

> feat(org): Add organization conversation admin dashboard by @saurya in https://github.com/OpenHands/OpenHands/pull/14846

> feat(app-server): capture production workspace state — initial snapshot at start + archive before delete (APP-2403) by @simonrosenberg in https://github.com/OpenHands/OpenHands/pull/14953

> feat(device-verify): align warning, button color, and add workspace dropdown by @tofarr in https://github.com/OpenHands/OpenHands/pull/15031

> feat(org): expose caller permissions on GET /organizations/{id}/me by @VascoSch92 in https://github.com/OpenHands/OpenHands/pull/15048

> feat(api-keys): add optional active window (not_before & expires_at) by @tofarr in https://github.com/OpenHands/OpenHands/pull/15085

> feat(app-server): add repo/branch to Laminar trace metadata by @simonrosenberg in https://github.com/OpenHands/OpenHands/pull/15059

> feat(api-keys): make 'unbound' org scope an explicit, first-class option by @tofarr in https://github.com/OpenHands/OpenHands/pull/15096

> feat(saas-auth): accept api_key cookie as a fallback credential by @tofarr in https://github.com/OpenHands/OpenHands/pull/15101

> fix: Fix CVE-2026-48526: Update pyjwt to 2.13.0 by @mamoodi in https://github.com/OpenHands/OpenHands/pull/14854

> fix: Fix CVE-2026-49855: Update tornado to 6.5.7 by @mamoodi in https://github.com/OpenHands/OpenHands/pull/14856

> fix: Fix CVE-2026-54278: Update aiohttp to 3.14.1 by @mamoodi in https://github.com/OpenHands/OpenHands/pull/14871

> fix: Fix CVE-2026-12143: Update form-data to 4.0.6 by @mamoodi in https://github.com/OpenHands/OpenHands/pull/14875

> fix: Fix CVE-2026-53539: Update python-multipart to >=0.0.30 by @mamoodi in https://github.com/OpenHands/OpenHands/pull/14876

> fix: Fix CVE-2026-45409: Update idna to 3.15 by @mamoodi in https://github.com/OpenHands/OpenHands/pull/14946

> fix: Fix CVE-2026-49458: Update dompurify to 3.4.6 by @mamoodi in https://github.com/OpenHands/OpenHands/pull/14872

> fix: Fix CVE-2026-44727: Update jupyter-server to 2.20.0 by @mamoodi in https://github.com/OpenHands/OpenHands/pull/14943

> fix: Fix CVE-2026-41691: Update i18next-http-backend to 3.0.5 by @mamoodi in https://github.com/OpenHands/OpenHands/pull/14955

> fix: Fix CVE-2026-54283: Update starlette to 1.3.1 by @mamoodi in https://github.com/OpenHands/OpenHands/pull/14874

> fix: Fix CVE-2026-8723: Update qs to 6.15.2 by @mamoodi in https://github.com/OpenHands/OpenHands/pull/14957

> fix: Fix CVE-2026-54285: Update @opentelemetry/core to 2.8.0 by @mamoodi in https://github.com/OpenHands/OpenHands/pull/14980

> fix: Fix CVE-2026-48712: Update protobufjs to 7.6.4 by @mamoodi in https://github.com/OpenHands/OpenHands/pull/14981

> fix: Fix CVE-2026-48779: Update ws to 8.21.0 by @mamoodi in https://github.com/OpenHands/OpenHands/pull/15007

> fix: Fix CVE-2026-44681: Update authlib to >=1.6.12 by @mamoodi in https://github.com/OpenHands/OpenHands/pull/14983

> docs: revise source code links in README.md by @enyst in https://github.com/OpenHands/OpenHands/pull/14869

> chore(deps): bump pyjwt from 2.12.1 to 2.13.0 by @dependabot[bot] in https://github.com/OpenHands/OpenHands/pull/14852

> test: replace real sleeps in maintenance runner tests by @aivong-openhands in https://github.com/OpenHands/OpenHands/pull/13930

> chore(main): release cloud 1.39.0 by @openhands-release-bot[bot] in https://github.com/OpenHands/OpenHands/pull/14748

> chore(deps-dev): bump jupyterlab from 4.5.7 to 4.5.9 by @dependabot[bot] in https://github.com/OpenHands/OpenHands/pull/15009

> chore(main): release cloud 1.40.0 by @openhands-release-bot[bot] in https://github.com/OpenHands/OpenHands/pull/14969

> build: pin dependency versions exactly by @rbren in https://github.com/OpenHands/OpenHands/pull/14384

> ci: add release ready gate by @enyst in https://github.com/OpenHands/OpenHands/pull/14987

> Release 1.8.0 by @mamoodi in https://github.com/OpenHands/OpenHands/pull/14743

> ci: adopt release-please for app and cloud releases by @jlav in https://github.com/OpenHands/OpenHands/pull/14718

> Use reusable issue duplicate checker action by @enyst in https://github.com/OpenHands/OpenHands/pull/14609

Source: https://github.com/OpenHands/OpenHands/releases/tag/1.9.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenHands/2026-07-06-2-automation-and-scheduling-changes-in-1-9-0|2 Automation and Scheduling changes in 1.9.0]] · Automation and Scheduling
- [[Changes/OpenHands/2026-07-06-3-enterprise-and-administration-changes-in-1-9-0|3 Enterprise and Administration changes in 1.9.0]] · Enterprise and Administration
- [[Changes/OpenHands/2026-07-06-docs-bring-readme-md-over-from-agent-canvas-by-rbren-in-https-github-com-openhan|docs: Bring README.md over from Agent Canvas]] · Files and Data
- [[Changes/OpenHands/2026-07-06-test-pltf-1269-replace-test-should-naming-with-test-verb-noun-context-convention|test: PLTF-1269 replace test_should naming with test_verb_noun_context convention]] · Context Window
- [[Changes/OpenHands/2026-07-06-refactor-extract-billing-test-fixtures-for-pltf-1269-by-aivong-openhands-in-http|refactor: extract billing test fixtures for PLTF-1269]] · Pricing Model
- [[Changes/OpenHands/2026-07-06-feat-jira-dc-email-mode-auto-link-targeted-repo-lookup-and-picker-mentions-by-ak|feat(jira-dc): email-mode auto-link, targeted repo lookup, and picker mentions]] · Interface Experience
- [[Changes/OpenHands/2026-07-06-4-safety-and-privacy-changes-in-1-9-0|4 Safety and Privacy changes in 1.9.0]] · Safety and Privacy
- [[Changes/OpenHands/2026-07-06-9-agent-mode-changes-in-1-9-0|9 Agent Mode changes in 1.9.0]] · Agent Mode
- [[Changes/OpenHands/2026-07-06-feat-add-full-git-history-user-setting-by-malhotra5-in-https-github-com-openhand|feat: Add full Git history user setting]] · Developer Workflow
- [[Changes/OpenHands/2026-07-06-3-account-and-access-changes-in-1-9-0|3 Account and Access changes in 1.9.0]] · Account and Access
- [[Changes/OpenHands/2026-07-06-7-apps-and-integrations-changes-in-1-9-0|7 Apps and Integrations changes in 1.9.0]] · Apps and Integrations
- [[Changes/OpenHands/2026-07-06-4-model-support-changes-in-1-9-0|4 Model Support changes in 1.9.0]] · Model Support
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openhands-2026-07-06-fa2714&body=Card%3A%20Changes%2FOpenHands%2F2026-07-06-46-other-changes-in-1-9-0.md%0ACard%20ID%3A%20openhands-2026-07-06-fa2714%0ASource%3A%20https%3A%2F%2Fgithub.com%2FOpenHands%2FOpenHands%2Freleases%2Ftag%2F1.9.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->