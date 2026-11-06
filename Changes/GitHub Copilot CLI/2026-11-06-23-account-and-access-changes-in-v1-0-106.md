---
card_id: github-copilot-cli-2026-11-06-f143f2
date: '2026-11-06'
description: 'GitHub Copilot CLI · 2026-11-06 · Account and Access: 23 changes in
  1.0.106 — Add MATS telemetry for Entra authentication through OneAuth, respecting
  client…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires
    login]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1317
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 3df80467a28477f7a0b8ec2f2233d6d26f1c171c8a267cdf778683ebff58b801
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-11-06-f143f2
  comparison: ''
  date: '2026-11-06'
  description: 'GitHub Copilot CLI — 1.0.106: 23 Account and Access changes'
  evidence:
  - quote: Add MATS telemetry for Entra authentication through OneAuth, respecting
      client telemetry opt-out.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: MCP Entra authentication now falls back to the VS Code registration when
      Copilot CLI preauthorization is unavailable.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: '`copilot login --device-code` now refuses a cleartext `http://` host,
      as browser sign-in already did: the device code is exchanged for a bearer token
      there. Use an `https://` host instead.'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Show remote MCP servers that return a bare HTTP 401 in the /mcp auth picker
      so you can sign in
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Remote HTTP MCP servers connect through proxies that require Kerberos (Negotiate)
      authentication.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Reuse valid saved MCP OAuth credentials for anonymous connections and initial
      challenges without requiring another sign-in
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Entra sign-in uses the VS Code application registration again by default
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: An unquoted -p or -i prompt that contains a command name such as update,
      login or help now gets the quoting hint instead of a parser error about an unknown
      subcommand.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Tools run on the first prompt even when ambient GitHub login finishes after
      the turn starts
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Browser sign-in lets you press any key to copy the sign-in link and reopen
      your browser.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: MCP servers dashboard keeps your active search and selection while startup
      authentication resolves
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Show the device policy warning after token authentication when --yolo is
      disabled by managed policy
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: MCP OAuth dynamic client registration now includes the scope the CLI will
      request, for authorization servers that limit a client to the scope it registered
      with
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Sign-in refuses a mistyped or non-https host (such as https:/tenant.ghe.com
      or ssh://tenant.ghe.com) instead of signing in against the scheme name as a
      host
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: MCP authentication warnings no longer repeat during automatic reconnect
      attempts
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: copilot login waits up to 2 minutes for keychain unlock prompts so token
      saving succeeds after slow unlocks.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: MCP OAuth renewal works when approved permissions are narrower than originally
      requested
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Refresh MCP OAuth tokens when idle liveness probes receive invalid_token
      challenges
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: MCP OAuth sign-in retries with a fresh callback port when a saved port
      is refused
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: MCP OAuth sign-in registers a new client once the saved dynamically registered
      client expires, instead of failing with invalid_client until the cache is deleted.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: ACP sessions now persist and refresh MCP OAuth grants from Copilot home
      to avoid repeated browser reauthorization.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: On macOS console hosts, OneAuth sign-in dialogs now open in the foreground.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Use OneAuth as the default Microsoft Entra sign-in path on Windows and
      macOS
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 23-account-and-access-changes-in-v1-0-106
  source_release: github-copilot-cli-2026-11-06-v1-0-106-github-435988160-ec5b15d4
  source_type: github_releases
  theme: account-access
  title: 23 Account and Access changes in v1.0.106
  type: change
related_changes:
- '[[Changes/OpenHands/2026-11-03-ci-deps-bump-docker-login-action-from-4-6-0-to-4-7-0-in-the-actions-group-across|ci(deps):
  bump docker/login-action from 4.6.0 to 4.7.0 in the actions group across 1…]]'
- '[[Changes/Dify/2026-11-04-2-account-and-access-changes-in-1-19-0|2 Account and
  Access changes in 1.19.0]]'
- '[[Changes/Codex CLI/2026-11-06-5-account-and-access-changes-in-rust-v0-167-0|5
  Account and Access changes in rust-v0.167.0]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-11-06-v1-0-106-github-435988160-ec5b15d4|github-copilot-cli-2026-11-06-v1-0-106-github-435988160-ec5b15d4]]'
source_type: github_releases
theme: account-access
title: 23 Account and Access changes in v1.0.106
type: change
---

<!-- chronolog:begin region="header" -->
# 23 Account and Access changes in v1.0.106

**GitHub Copilot CLI** · 2026-11-06 · [[Themes/account-access|Account and Access]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.106) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-11-06-v1-0-106-github-435988160-ec5b15d4|1.0.106]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Add MATS telemetry for Entra authentication through OneAuth, respecting client telemetry opt-out.

> MCP Entra authentication now falls back to the VS Code registration when Copilot CLI preauthorization is unavailable.

> `copilot login --device-code` now refuses a cleartext `http://` host, as browser sign-in already did: the device code is exchanged for a bearer token there. Use an `https://` host instead.

> Show remote MCP servers that return a bare HTTP 401 in the /mcp auth picker so you can sign in

> Remote HTTP MCP servers connect through proxies that require Kerberos (Negotiate) authentication.

> Reuse valid saved MCP OAuth credentials for anonymous connections and initial challenges without requiring another sign-in

> Entra sign-in uses the VS Code application registration again by default

> An unquoted -p or -i prompt that contains a command name such as update, login or help now gets the quoting hint instead of a parser error about an unknown subcommand.

> Tools run on the first prompt even when ambient GitHub login finishes after the turn starts

> Browser sign-in lets you press any key to copy the sign-in link and reopen your browser.

> MCP servers dashboard keeps your active search and selection while startup authentication resolves

> Show the device policy warning after token authentication when --yolo is disabled by managed policy

> MCP OAuth dynamic client registration now includes the scope the CLI will request, for authorization servers that limit a client to the scope it registered with

> Sign-in refuses a mistyped or non-https host (such as https:/tenant.ghe.com or ssh://tenant.ghe.com) instead of signing in against the scheme name as a host

> MCP authentication warnings no longer repeat during automatic reconnect attempts

> copilot login waits up to 2 minutes for keychain unlock prompts so token saving succeeds after slow unlocks.

> MCP OAuth renewal works when approved permissions are narrower than originally requested

> Refresh MCP OAuth tokens when idle liveness probes receive invalid_token challenges

> MCP OAuth sign-in retries with a fresh callback port when a saved port is refused

> MCP OAuth sign-in registers a new client once the saved dynamically registered client expires, instead of failing with invalid_client until the cache is deleted.

> ACP sessions now persist and refresh MCP OAuth grants from Copilot home to avoid repeated browser reauthorization.

> On macOS console hosts, OneAuth sign-in dialogs now open in the foreground.

> Use OneAuth as the default Microsoft Entra sign-in path on Windows and macOS

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.106
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-11-06-4-voice-and-audio-changes-in-v1-0-106|4 Voice and Audio changes in v1.0.106]] · Voice and Audio
- [[Changes/GitHub Copilot CLI/2026-11-06-2-files-and-data-changes-in-v1-0-106|2 Files and Data changes in v1.0.106]] · Files and Data
- [[Changes/GitHub Copilot CLI/2026-11-06-3-reliability-and-performance-changes-in-v1-0-106|3 Reliability and Performance changes in v1.0.106]] · Reliability and Performance
- [[Changes/GitHub Copilot CLI/2026-11-06-34-agent-mode-changes-in-v1-0-106|34 Agent Mode changes in v1.0.106]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-11-06-10-memory-and-personalization-changes-in-v1-0-106|10 Memory and Personalization changes in v1.0.106]] · Memory and Personalization
- [[Changes/GitHub Copilot CLI/2026-11-06-64-developer-workflow-changes-in-v1-0-106|64 Developer Workflow changes in v1.0.106]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-11-06-34-safety-and-privacy-changes-in-v1-0-106|34 Safety and Privacy changes in v1.0.106]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-11-06-9-collaboration-changes-in-v1-0-106|9 Collaboration changes in v1.0.106]] · Collaboration
- [[Changes/GitHub Copilot CLI/2026-11-06-8-mobile-and-desktop-changes-in-v1-0-106|8 Mobile and Desktop changes in v1.0.106]] · Mobile and Desktop
- [[Changes/GitHub Copilot CLI/2026-11-06-4-projects-and-workspaces-changes-in-v1-0-106|4 Projects and Workspaces changes in v1.0.106]] · Projects and Workspaces
- [[Changes/GitHub Copilot CLI/2026-11-06-8-accessibility-and-localization-changes-in-v1-0-106|8 Accessibility and Localization changes in v1.0.106]] · Accessibility and Localization
- [[Changes/GitHub Copilot CLI/2026-11-06-17-context-window-changes-in-v1-0-106|17 Context Window changes in v1.0.106]] · Context Window
- [[Changes/GitHub Copilot CLI/2026-11-06-57-editor-experience-changes-in-v1-0-106|57 Editor Experience changes in v1.0.106]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-11-06-33-model-support-changes-in-v1-0-106|33 Model Support changes in v1.0.106]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-11-06-89-apps-and-integrations-changes-in-v1-0-106|89 Apps and Integrations changes in v1.0.106]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-11-06-2-image-generation-changes-in-v1-0-106|2 Image Generation changes in v1.0.106]] · Image Generation
- [[Changes/GitHub Copilot CLI/2026-11-06-42-interface-experience-changes-in-v1-0-106|42 Interface Experience changes in v1.0.106]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-11-06-5-pricing-model-changes-in-v1-0-106|5 Pricing Model changes in v1.0.106]] · Pricing Model
- [[Changes/GitHub Copilot CLI/2026-11-06-in-the-every-schedule-manager-x-now-removes-the-highlighted-schedule-even-after|In the /every schedule manager, x now removes the highlighted schedule even after…]] · Automation and Scheduling
- [[Changes/GitHub Copilot CLI/2026-11-06-172-other-changes-in-v1-0-106|172 other changes in v1.0.106]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2026-11-06 · Codex CLI · [[Changes/Codex CLI/2026-11-06-5-account-and-access-changes-in-rust-v0-167-0|5 Account and Access changes in rust-v0.167.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-30 · Cursor · [[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires login]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-11-06-f143f2&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-11-06-23-account-and-access-changes-in-v1-0-106.md%0ACard%20ID%3A%20github-copilot-cli-2026-11-06-f143f2%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.106%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->