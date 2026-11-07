---
card_id: openclaw-2026-10-10-2c3e4c
date: '2026-10-10'
description: 'OpenClaw · 2026-10-10 · Account and Access: 18 changes in v2026.10.1
  — Supported direct Anthropic API-key conversations can keep reusing cached instructions…'
diffusion:
  first_in_tracked: "[[Changes/Notion/2020-07-28-sign-into-notion-with-your-apple-id-the-perfect-combination-of-speedy-and-secure|Sign
    into Notion with your Apple ID \U0001F5DD️ The perfect combination of speedy and
    secure]]"
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2265
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 0d597577b417506b80e55faff7e62c44d23a2e6abaf9a58c40426ac9ab23349f
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-10-10-2c3e4c
  comparison: ''
  date: '2026-10-10'
  description: 'OpenClaw — v2026.10.1: 18 Account and Access changes'
  evidence:
  - quote: Supported direct Anthropic API-key conversations can keep reusing cached
      instructions when workspace guidance or skills change, while Claude receives
      the updates later in the conversation. OAuth, proxy and other hosted routes
      keep their existing behavior, and compaction, route or tool changes can still
      invalidate caching.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Credentials must match the configured Enterprise host, with public GitHub
      sign-in kept separate. Configuring the repository does not complete GitHub authentication
      on stock cloud workers. Local repository recovery requires restoring the recorded
      host configuration.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Agents API sessions can use configured Streamable HTTP MCP tools reachable
      from their execution environment, including private services. Resolved credential
      headers are passed to the API. Use /new or /reset after changing MCP setup or
      credentials; existing conversations may also need a reset after this upgrade.
      Other MCP transports and Gateway OAuth remain unsupported.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Team administrators can assign roles by verified GitHub login before people
      first sign in, then see each person's effective role and its source. Explicit
      assignments take priority. Mappings use the cached verified primary identity,
      and applying changes immediately requires live configuration reload.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: 'Optional gateway.roles.assignments.byGithubLogin mappings use the cached
      verified primary GitHub login. An explicit role assignment takes priority, then
      the mapping, then the default; administrators can see the effective role and
      its source. #163825 . Thanks @steipete .'
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Visitor Access can invite a GitHub account with a private email and keep
      the invitation attached to the account when its login changes. Administrators
      can revoke a person's recorded invitations across verified email aliases or
      cancel one before first sign-in, preserving saved work and independent access.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: 'Visitor invitations accept a GitHub selector without requiring a public
      email. Use exactly one GitHub or email selector and an existing verified Cloudflare
      OIDC account-ID mapping; the invitation plugin does not configure the sign-in
      provider. #162666 . Thanks @shakkernerd .'
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: 'Administrators can revoke a person''s recorded visitor grants across verified
      email aliases by profile ID, or revoke one invitation by grant ID before sign-in.
      This requires host support and affects the recorded grants, leaving independent
      access intact. #162207 . Thanks @shakkernerd .'
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: If replacing a sign-in fails, setup restores the previous credential before
      reconnecting. Copilot setup can reuse an authorized saved token or secret reference
      on the same host domain; changing domains still requires a fresh login. Rerunning
      setup preserves trusted-proxy sign-in unless you explicitly change it; combining
      it with Tailscale Funnel is refused, so choose password sign-in or leave public
      exposure off.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: 'Memory search can again use an eligible saved Codex OAuth account for
      OpenAI embeddings without a separate API key. The account must have the required
      access: the separate Sign in with ChatGPT token-sharing grant does not authorize
      embeddings.'
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Mac chat stays open while its Gateway finishes setup or reconnects, and
      opening a completed conversation can restore a failed Dashboard. Refreshing
      an unrelated profile preserves sign-in for the same connection. Switching the
      primary Gateway clears the old chat and preview cache, and dismissing an older
      notification no longer hides its replacement.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: You can sign in to eligible Cloudflare Access apps inside the Mac Dashboard
      and keep those app sessions across restarts. Use an updated Mac app with an
      observed HTTPS app on port 443 on the same site, Access team and account. WebKit
      restrictions can still require the embedded app's own sign-in link.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Native Codex application control no longer reports a false browser-authentication
      error for API-key installations. Setup keeps its timeout allowance across clock
      changes, and agents get instructions for locating windows and providing browser
      and page references together.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: 'Plugins using the retired Copilot token-exchange helpers must move to
      registered authentication hooks and provider-owned endpoint resolution. #163587
      . Thanks @steipete .'
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: 'Plugin reloads keep passive model, sign-in and chat metadata available
      through waiting and failed drains. #162301 . Thanks @steipete .'
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: 'Comfy guidance separates hosted MCP account sign-in from workflow-plugin
      API keys. See MCP OAuth and Comfy MCP . #163197 . Thanks @vincentkoc .'
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: MCP library updates bind saved sign-in records to their authorization server.
      If that server changes, reconnect explicitly, including when older client information
      was saved. f9310588 . Thanks @Patrick-Erichsen , @RomneyDa , @vincentkoc .
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  - quote: Logout removes copied catalog credentials from still-saved profiles, and
      secret-excluded Git backups omit catalog keys and headers. Profiles already
      removed by older logouts and previously created or pushed backups need separate
      inspection. Permitted CLI commands and literal-loopback HTTP requests work with
      the secret egress proxy; secret substitution remains refused over HTTP. Provider
      errors hide reflected credentials, shared OAuth profiles avoid unnecessary copies,
      and A2A status identifies token settings needing repair.
    source_release: https://docs.openclaw.ai/releases/2026.10.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 18-account-and-access-changes-in-v2026-10-1
  source_release: openclaw-2026-10-10-v2026-10-1-d64e4e93
  source_type: openclaw_changelog
  theme: account-access
  title: 18 Account and Access changes in v2026.10.1
  type: change
related_changes:
- '[[Changes/Claude Code/2026-10-09-improved-the-errors-for-a-refused-cloud-session-they-now-say-why-your-organizati|Improved
  the errors for a refused cloud session]]'
- '[[Changes/GitHub Copilot CLI/2026-10-09-use-native-microsoft-entra-broker-authentication-on-macos-when-available-with-br|Use
  native Microsoft Entra broker authentication on macOS when available…]]'
- '[[Changes/Open WebUI/2026-10-10-19-account-and-access-changes-in-v0-12-0|19 Account
  and Access changes in v0.12.0]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-10-10-v2026-10-1-d64e4e93|openclaw-2026-10-10-v2026-10-1-d64e4e93]]'
source_type: openclaw_changelog
theme: account-access
title: 18 Account and Access changes in v2026.10.1
type: change
---

<!-- chronolog:begin region="header" -->
# 18 Account and Access changes in v2026.10.1

**OpenClaw** · 2026-10-10 · [[Themes/account-access|Account and Access]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.10.1) · from [[Releases/OpenClaw/openclaw-2026-10-10-v2026-10-1-d64e4e93|v2026.10.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Supported direct Anthropic API-key conversations can keep reusing cached instructions when workspace guidance or skills change, while Claude receives the updates later in the conversation. OAuth, proxy and other hosted routes keep their existing behavior, and compaction, route or tool changes can still invalidate caching.

> Credentials must match the configured Enterprise host, with public GitHub sign-in kept separate. Configuring the repository does not complete GitHub authentication on stock cloud workers. Local repository recovery requires restoring the recorded host configuration.

> Agents API sessions can use configured Streamable HTTP MCP tools reachable from their execution environment, including private services. Resolved credential headers are passed to the API. Use /new or /reset after changing MCP setup or credentials; existing conversations may also need a reset after this upgrade. Other MCP transports and Gateway OAuth remain unsupported.

> Team administrators can assign roles by verified GitHub login before people first sign in, then see each person's effective role and its source. Explicit assignments take priority. Mappings use the cached verified primary identity, and applying changes immediately requires live configuration reload.

> Optional gateway.roles.assignments.byGithubLogin mappings use the cached verified primary GitHub login. An explicit role assignment takes priority, then the mapping, then the default; administrators can see the effective role and its source. #163825 . Thanks @steipete .

> Visitor Access can invite a GitHub account with a private email and keep the invitation attached to the account when its login changes. Administrators can revoke a person's recorded invitations across verified email aliases or cancel one before first sign-in, preserving saved work and independent access.

> Visitor invitations accept a GitHub selector without requiring a public email. Use exactly one GitHub or email selector and an existing verified Cloudflare OIDC account-ID mapping; the invitation plugin does not configure the sign-in provider. #162666 . Thanks @shakkernerd .

> Administrators can revoke a person's recorded visitor grants across verified email aliases by profile ID, or revoke one invitation by grant ID before sign-in. This requires host support and affects the recorded grants, leaving independent access intact. #162207 . Thanks @shakkernerd .

> If replacing a sign-in fails, setup restores the previous credential before reconnecting. Copilot setup can reuse an authorized saved token or secret reference on the same host domain; changing domains still requires a fresh login. Rerunning setup preserves trusted-proxy sign-in unless you explicitly change it; combining it with Tailscale Funnel is refused, so choose password sign-in or leave public exposure off.

> Memory search can again use an eligible saved Codex OAuth account for OpenAI embeddings without a separate API key. The account must have the required access: the separate Sign in with ChatGPT token-sharing grant does not authorize embeddings.

> Mac chat stays open while its Gateway finishes setup or reconnects, and opening a completed conversation can restore a failed Dashboard. Refreshing an unrelated profile preserves sign-in for the same connection. Switching the primary Gateway clears the old chat and preview cache, and dismissing an older notification no longer hides its replacement.

> You can sign in to eligible Cloudflare Access apps inside the Mac Dashboard and keep those app sessions across restarts. Use an updated Mac app with an observed HTTPS app on port 443 on the same site, Access team and account. WebKit restrictions can still require the embedded app's own sign-in link.

> Native Codex application control no longer reports a false browser-authentication error for API-key installations. Setup keeps its timeout allowance across clock changes, and agents get instructions for locating windows and providing browser and page references together.

> Plugins using the retired Copilot token-exchange helpers must move to registered authentication hooks and provider-owned endpoint resolution. #163587 . Thanks @steipete .

> Plugin reloads keep passive model, sign-in and chat metadata available through waiting and failed drains. #162301 . Thanks @steipete .

> Comfy guidance separates hosted MCP account sign-in from workflow-plugin API keys. See MCP OAuth and Comfy MCP . #163197 . Thanks @vincentkoc .

> MCP library updates bind saved sign-in records to their authorization server. If that server changes, reconnect explicitly, including when older client information was saved. f9310588 . Thanks @Patrick-Erichsen , @RomneyDa , @vincentkoc .

> Logout removes copied catalog credentials from still-saved profiles, and secret-excluded Git backups omit catalog keys and headers. Profiles already removed by older logouts and previously created or pushed backups need separate inspection. Permitted CLI commands and literal-loopback HTTP requests work with the secret egress proxy; secret substitution remains refused over HTTP. Provider errors hide reflected credentials, shared OAuth profiles avoid unnecessary copies, and A2A status identifies token settings needing repair.

Source: https://docs.openclaw.ai/releases/2026.10.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-10-10-2-reliability-and-performance-changes-in-v2026-10-1|2 Reliability and Performance changes in v2026.10.1]] · Reliability and Performance
- [[Changes/OpenClaw/2026-10-10-13-memory-and-personalization-changes-in-v2026-10-1|13 Memory and Personalization changes in v2026.10.1]] · Memory and Personalization
- [[Changes/OpenClaw/2026-10-10-96-apps-and-integrations-changes-in-v2026-10-1|96 Apps and Integrations changes in v2026.10.1]] · Apps and Integrations
- [[Changes/OpenClaw/2026-10-10-15-mobile-and-desktop-changes-in-v2026-10-1|15 Mobile and Desktop changes in v2026.10.1]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-10-10-12-context-window-changes-in-v2026-10-1|12 Context Window changes in v2026.10.1]] · Context Window
- [[Changes/OpenClaw/2026-10-10-4-pricing-model-changes-in-v2026-10-1|4 Pricing Model changes in v2026.10.1]] · Pricing Model
- [[Changes/OpenClaw/2026-10-10-18-model-support-changes-in-v2026-10-1|18 Model Support changes in v2026.10.1]] · Model Support
- [[Changes/OpenClaw/2026-10-10-20-safety-and-privacy-changes-in-v2026-10-1|20 Safety and Privacy changes in v2026.10.1]] · Safety and Privacy
- [[Changes/OpenClaw/2026-10-10-3-search-and-browsing-changes-in-v2026-10-1|3 Search and Browsing changes in v2026.10.1]] · Search and Browsing
- [[Changes/OpenClaw/2026-10-10-plugin-authors-can-await-session-history-extension-changes-and-replay-metadata-t|Plugin authors can await session history, extension changes and replay metadata]] · Projects and Workspaces
- [[Changes/OpenClaw/2026-10-10-2-accessibility-and-localization-changes-in-v2026-10-1|2 Accessibility and Localization changes in v2026.10.1]] · Accessibility and Localization
- [[Changes/OpenClaw/2026-10-10-image-generation-with-oauth-can-retry-using-a-supported-openai-chat-model-in-age|Image generation with OAuth can retry using a supported OpenAI chat model…]] · Image Generation
- [[Changes/OpenClaw/2026-10-10-10-editor-experience-changes-in-v2026-10-1|10 Editor Experience changes in v2026.10.1]] · Editor Experience
- [[Changes/OpenClaw/2026-10-10-2-files-and-data-changes-in-v2026-10-1|2 Files and Data changes in v2026.10.1]] · Files and Data
- [[Changes/OpenClaw/2026-10-10-8-voice-and-audio-changes-in-v2026-10-1|8 Voice and Audio changes in v2026.10.1]] · Voice and Audio
- [[Changes/OpenClaw/2026-10-10-27-agent-mode-changes-in-v2026-10-1|27 Agent Mode changes in v2026.10.1]] · Agent Mode
- [[Changes/OpenClaw/2026-10-10-12-collaboration-changes-in-v2026-10-1|12 Collaboration changes in v2026.10.1]] · Collaboration
- [[Changes/OpenClaw/2026-10-10-video-previews-new-video-previews-can-download-media-before-play|Video previews: New video previews can download media before Play]] · Multimodal Input
- [[Changes/OpenClaw/2026-10-10-11-developer-workflow-changes-in-v2026-10-1|11 Developer Workflow changes in v2026.10.1]] · Developer Workflow
- [[Changes/OpenClaw/2026-10-10-5-enterprise-and-administration-changes-in-v2026-10-1|5 Enterprise and Administration changes in v2026.10.1]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-10-10-20-interface-experience-changes-in-v2026-10-1|20 Interface Experience changes in v2026.10.1]] · Interface Experience
- [[Changes/OpenClaw/2026-10-10-10-automation-and-scheduling-changes-in-v2026-10-1|10 Automation and Scheduling changes in v2026.10.1]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-10-10-112-other-changes-in-v2026-10-1|112 other changes in v2026.10.1]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2026-10-10 · Open WebUI · [[Changes/Open WebUI/2026-10-10-19-account-and-access-changes-in-v0-12-0|19 Account and Access changes in v0.12.0]]
- Later: 2026-10-12 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-10-12-2-account-and-access-changes-in-v1-0-96|2 Account and Access changes in v1.0.96]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Notion · [[Changes/Notion/2020-07-28-sign-into-notion-with-your-apple-id-the-perfect-combination-of-speedy-and-secure|Sign into Notion with your Apple ID 🗝️ The perfect combination of speedy and secure]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-10-10-2c3e4c&body=Card%3A%20Changes%2FOpenClaw%2F2026-10-10-18-account-and-access-changes-in-v2026-10-1.md%0ACard%20ID%3A%20openclaw-2026-10-10-2c3e4c%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.10.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->