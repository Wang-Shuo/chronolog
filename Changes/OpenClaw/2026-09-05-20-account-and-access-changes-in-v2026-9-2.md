---
card_id: openclaw-2026-09-05-45fd4c
date: '2026-09-05'
description: 'OpenClaw · 2026-09-05 · Account and Access: 20 changes in v2026.9.2
  — On hosts that implement the automatic browser handoff , a dashboard bookmark or
  direct…'
diffusion:
  first_in_tracked: "[[Changes/Notion/2020-07-28-sign-into-notion-with-your-apple-id-the-perfect-combination-of-speedy-and-secure|Sign
    into Notion with your Apple ID \U0001F5DD️ The perfect combination of speedy and
    secure]]"
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2230
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: a1ffedbadabc6b789074b43ebb92e917359e97a6160957ad1f761dc56e2732ac
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-05-45fd4c
  comparison: ''
  date: '2026-09-05'
  description: 'OpenClaw — v2026.9.2: 20 Account and Access changes'
  evidence:
  - quote: On hosts that implement the automatic browser handoff , a dashboard bookmark
      or direct link can use the host's verified sign-in and return you to the page
      you intended to open. The handoff requires an identity-aware HTTPS service supplied
      by the host; deployments without it keep their existing login instructions,
      and a successful sign-in preserves the selected page, query, and fragment.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Interactive chat widgets now load their saved document through the authenticated
      OpenClaw connection, which lets supported widgets work behind login proxies
      without asking the embedded frame to sign in separately. A failed document load
      offers Retry, and an HTML download remains available when an image export cannot
      be produced.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: A single-owner installation using token or password access can now have
      a saved name, avatar, profile preferences, and My GitHub connection without
      setting up a separate sign-in service. These follow the owner profile across
      its devices. On a Mac, an owner without an uploaded image can use the picture
      of the Mac account running OpenClaw, while paired browsers and supported Mac
      SSH connections can display saved profile photos again.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: For teams, assignment menus include registered people even when they are
      offline or have not owned a conversation, and grouped session headers bring
      presence and people cards closer to their work. Participant lists reveal additional
      names, and person Activity links use readable addresses. Shared token or password
      holders still share one owner identity, its preferences, and My GitHub connection,
      so use personal sign-in when each person needs a distinct profile.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Sign-in warnings are easier to distinguish from ordinary model details,
      provider headings offer a shortcut to Model Setup, and a provider with a usable
      profile can show Ready despite a failed sibling profile. Session Observer's
      model choices also recover after temporary catalog failures and ignore obsolete
      responses after agent switching. These labels describe the available catalog
      and session state, rather than verifying a provider credential or identifying
      a billing account.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: GitHub previews keep the exact issue, pull request, or comment destination
      you opened, even when another link has already filled the preview cache. They
      use the selected agent's configured account and explain sign-in, access, rate-limit,
      or connection failures, while remaining limited to public repositories. PR badges
      collect later pages of checks before reporting complete results, so a failure
      beyond the first page does not disappear behind a passing badge. Results beyond
      the collection limits can leave the badge absent.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: For login-protected reverse proxies, the Mermaid troubleshooting guide
      explains which static renderer assets need to load without the page's cookies.
      Keep authentication on the dashboard and API routes, make only the required
      asset exception, and reload after correcting it.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Access changes apply at the place they matter. Pending automatic pairing
      approvals recheck current policy, revoked device commands are cancelled, and
      rotating a token or password within the same authentication mode reconnects
      affected shared-credential clients while independently paired clients stay connected.
      Existing sign-in failures and earned lockouts survive rate-limit changes. Changing
      the shell affects new terminals, while disabling terminals closes existing sessions
      and re-enabling allows fresh ones.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Changes that replace a channel, browser, or exporter can briefly interrupt
      that service, and failed service replacement can require Gateway recovery. Working
      hooks survive a replacement that fails to load, and active channels restore
      their incoming routes after plugin replacement. Refresh open browser pages for
      changed interface preferences or terminal policy. Listener and process settings,
      authentication-mode changes, and dashboard asset roots or base paths still require
      a full restart.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Compatible audio-only clients can now use native GPT-Live with their configured
      ChatGPT OAuth or Platform credentials while the Gateway handles tools and tasks
      for the call. The client must explicitly support the Gateway-controlled mode;
      OpenAI GA Realtime still requires a Platform key for this mode. Status requests,
      cancellation, redirects, and follow-ups stay with the work started by that call,
      and saved conversation history is kept separate from what was actually said
      in the new call.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: When an answer to a pending question loses its confirmation, OpenClaw reports
      the uncertainty instead of sending the answer again as another instruction.
      Check the conversation before retrying. Questions from standalone attached MCP
      sessions need the Control UI or native question controls, and protected Copilot
      steering remains unavailable. Talk mode covers these client and authentication
      boundaries, along with the separate handling of call audio and accepted tasks.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: If your Gateway uses Cloudflare Access, you can enter its address in the
      Mac app and sign in through your usual browser , then return to its dashboard
      under your own account without copying a shared token. The website's Get the
      apps → Open in Mac app action opens the same connection editor with the address
      filled in, and the app remembers the selected Gateway after restart.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Personal accounts support Anthropic API keys, OpenAI API keys or browser/device
      sign-in, and Grok/xAI API keys or device sign-in where those methods are enabled.
      The Gateway must identify each person first, including for CLI setup; a shared
      password or device pairing alone does not identify a distinct teammate. Collaborators
      see a personal-account label without its private email or account details. Shared
      same-provider fallback can still apply, so selection is not a billing guarantee
      or isolation from administrators. Claude CLI keeps its required account restriction.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Restricted and message-only turns keep their intended tool limits. If an
      older administrator-managed Codex policy blocks those turns, the error explains
      the manual file or MDM migration needed to preserve ChatGPT-only login restrictions.
      Scheduled runs whose app inventory times out keep their saved access binding
      and report a timeout suitable for existing retry handling, without executing
      tools or asking for unnecessary reauthorization. Codex cloud sessions also skip
      startup of an OpenClaw worker they do not use.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: OpenClaw now talks directly to the Claude Code executable already installed
      on your computer, preserving existing login and configuration, warm conversations,
      resumed sessions, approvals, and questions. Script wrappers and command aliases
      retain their verified launch arguments, and fallback session titles use the
      first real prompt instead of preceding instruction metadata. Keep Claude Code
      current.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: The Desktop panel notices when an approved machine becomes available and
      keeps your explicit selection when the session moves or refreshes. Opening a
      popout carries that same desktop and control choice with it, subject to the
      usual authentication and permissions. You can also take control while Browser
      or Terminal is launching without leaving its button stuck, and a failed launch
      shows an error you can act on.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Browser navigation now has time to return its result or its own error before
      the surrounding connection gives up. That matters when the browser is still
      responding but a page fails to load, because a generic connection timeout no
      longer hides the more specific navigation failure. On a connected node, the
      next command can also restart a stopped browser-control service under the existing
      profile and authentication rules; commands arriving during shutdown remain rejected.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: Editing one MCP server no longer needs to disconnect the other tools your
      agent is using. With Gateway hot reload enabled, unchanged servers keep their
      connections and cached tools, and an active call to one of those servers can
      finish while a different server is replaced. Changed or removed servers are
      revoked immediately, with updated definitions discovered on the next turn and
      requester sign-in tools refreshed on the next message.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: OAuth-connected tools also remain available to CLI agents after credentials
      refresh, and loading a multi-page tool, resource, or prompt list no longer times
      out just because the computer's clock jumps forward. In Settings, deleting an
      MCP server or Cloud Worker profile with list-valued settings, or clearing a
      worker's Setup field, no longer fails on those lists.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  - quote: A coding agent on an OpenClaw cloud worker or paired session host can commit,
      push, and open a GitHub pull request during its turn, so it can see the result
      and respond before handing the work back. This needs GitHub CLI on the worker
      and an available shared Gateway GitHub account with access to the repository.
      It uses that shared identity, not the paired computer's personal login.
    source_release: https://docs.openclaw.ai/releases/2026.9.2
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 20-account-and-access-changes-in-v2026-9-2
  source_release: openclaw-2026-09-05-v2026-9-2-377f6d77
  source_type: openclaw_changelog
  theme: account-access
  title: 20 Account and Access changes in v2026.9.2
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-09-04-3-account-and-access-changes-in-v1-0-83|3
  Account and Access changes in v1.0.83]]'
- '[[Changes/OpenCode/2026-09-04-desktop-use-the-desktop-client-id-during-opencode-account-device-authentication|Desktop
  Use the desktop client ID during OpenCode account device authentication]]'
- '[[Changes/Wispr Flow/2026-09-04-a-smoother-sign-in-handoff-android|A Smoother Sign-In
  Handoff (Android)]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-05-v2026-9-2-377f6d77|openclaw-2026-09-05-v2026-9-2-377f6d77]]'
source_type: openclaw_changelog
theme: account-access
title: 20 Account and Access changes in v2026.9.2
type: change
---

<!-- chronolog:begin region="header" -->
# 20 Account and Access changes in v2026.9.2

**OpenClaw** · 2026-09-05 · [[Themes/account-access|Account and Access]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.2) · from [[Releases/OpenClaw/openclaw-2026-09-05-v2026-9-2-377f6d77|v2026.9.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> On hosts that implement the automatic browser handoff , a dashboard bookmark or direct link can use the host's verified sign-in and return you to the page you intended to open. The handoff requires an identity-aware HTTPS service supplied by the host; deployments without it keep their existing login instructions, and a successful sign-in preserves the selected page, query, and fragment.

> Interactive chat widgets now load their saved document through the authenticated OpenClaw connection, which lets supported widgets work behind login proxies without asking the embedded frame to sign in separately. A failed document load offers Retry, and an HTML download remains available when an image export cannot be produced.

> A single-owner installation using token or password access can now have a saved name, avatar, profile preferences, and My GitHub connection without setting up a separate sign-in service. These follow the owner profile across its devices. On a Mac, an owner without an uploaded image can use the picture of the Mac account running OpenClaw, while paired browsers and supported Mac SSH connections can display saved profile photos again.

> For teams, assignment menus include registered people even when they are offline or have not owned a conversation, and grouped session headers bring presence and people cards closer to their work. Participant lists reveal additional names, and person Activity links use readable addresses. Shared token or password holders still share one owner identity, its preferences, and My GitHub connection, so use personal sign-in when each person needs a distinct profile.

> Sign-in warnings are easier to distinguish from ordinary model details, provider headings offer a shortcut to Model Setup, and a provider with a usable profile can show Ready despite a failed sibling profile. Session Observer's model choices also recover after temporary catalog failures and ignore obsolete responses after agent switching. These labels describe the available catalog and session state, rather than verifying a provider credential or identifying a billing account.

> GitHub previews keep the exact issue, pull request, or comment destination you opened, even when another link has already filled the preview cache. They use the selected agent's configured account and explain sign-in, access, rate-limit, or connection failures, while remaining limited to public repositories. PR badges collect later pages of checks before reporting complete results, so a failure beyond the first page does not disappear behind a passing badge. Results beyond the collection limits can leave the badge absent.

> For login-protected reverse proxies, the Mermaid troubleshooting guide explains which static renderer assets need to load without the page's cookies. Keep authentication on the dashboard and API routes, make only the required asset exception, and reload after correcting it.

> Access changes apply at the place they matter. Pending automatic pairing approvals recheck current policy, revoked device commands are cancelled, and rotating a token or password within the same authentication mode reconnects affected shared-credential clients while independently paired clients stay connected. Existing sign-in failures and earned lockouts survive rate-limit changes. Changing the shell affects new terminals, while disabling terminals closes existing sessions and re-enabling allows fresh ones.

> Changes that replace a channel, browser, or exporter can briefly interrupt that service, and failed service replacement can require Gateway recovery. Working hooks survive a replacement that fails to load, and active channels restore their incoming routes after plugin replacement. Refresh open browser pages for changed interface preferences or terminal policy. Listener and process settings, authentication-mode changes, and dashboard asset roots or base paths still require a full restart.

> Compatible audio-only clients can now use native GPT-Live with their configured ChatGPT OAuth or Platform credentials while the Gateway handles tools and tasks for the call. The client must explicitly support the Gateway-controlled mode; OpenAI GA Realtime still requires a Platform key for this mode. Status requests, cancellation, redirects, and follow-ups stay with the work started by that call, and saved conversation history is kept separate from what was actually said in the new call.

> When an answer to a pending question loses its confirmation, OpenClaw reports the uncertainty instead of sending the answer again as another instruction. Check the conversation before retrying. Questions from standalone attached MCP sessions need the Control UI or native question controls, and protected Copilot steering remains unavailable. Talk mode covers these client and authentication boundaries, along with the separate handling of call audio and accepted tasks.

> If your Gateway uses Cloudflare Access, you can enter its address in the Mac app and sign in through your usual browser , then return to its dashboard under your own account without copying a shared token. The website's Get the apps → Open in Mac app action opens the same connection editor with the address filled in, and the app remembers the selected Gateway after restart.

> Personal accounts support Anthropic API keys, OpenAI API keys or browser/device sign-in, and Grok/xAI API keys or device sign-in where those methods are enabled. The Gateway must identify each person first, including for CLI setup; a shared password or device pairing alone does not identify a distinct teammate. Collaborators see a personal-account label without its private email or account details. Shared same-provider fallback can still apply, so selection is not a billing guarantee or isolation from administrators. Claude CLI keeps its required account restriction.

> Restricted and message-only turns keep their intended tool limits. If an older administrator-managed Codex policy blocks those turns, the error explains the manual file or MDM migration needed to preserve ChatGPT-only login restrictions. Scheduled runs whose app inventory times out keep their saved access binding and report a timeout suitable for existing retry handling, without executing tools or asking for unnecessary reauthorization. Codex cloud sessions also skip startup of an OpenClaw worker they do not use.

> OpenClaw now talks directly to the Claude Code executable already installed on your computer, preserving existing login and configuration, warm conversations, resumed sessions, approvals, and questions. Script wrappers and command aliases retain their verified launch arguments, and fallback session titles use the first real prompt instead of preceding instruction metadata. Keep Claude Code current.

> The Desktop panel notices when an approved machine becomes available and keeps your explicit selection when the session moves or refreshes. Opening a popout carries that same desktop and control choice with it, subject to the usual authentication and permissions. You can also take control while Browser or Terminal is launching without leaving its button stuck, and a failed launch shows an error you can act on.

> Browser navigation now has time to return its result or its own error before the surrounding connection gives up. That matters when the browser is still responding but a page fails to load, because a generic connection timeout no longer hides the more specific navigation failure. On a connected node, the next command can also restart a stopped browser-control service under the existing profile and authentication rules; commands arriving during shutdown remain rejected.

> Editing one MCP server no longer needs to disconnect the other tools your agent is using. With Gateway hot reload enabled, unchanged servers keep their connections and cached tools, and an active call to one of those servers can finish while a different server is replaced. Changed or removed servers are revoked immediately, with updated definitions discovered on the next turn and requester sign-in tools refreshed on the next message.

> OAuth-connected tools also remain available to CLI agents after credentials refresh, and loading a multi-page tool, resource, or prompt list no longer times out just because the computer's clock jumps forward. In Settings, deleting an MCP server or Cloud Worker profile with list-valued settings, or clearing a worker's Setup field, no longer fails on those lists.

> A coding agent on an OpenClaw cloud worker or paired session host can commit, push, and open a GitHub pull request during its turn, so it can see the result and respond before handing the work back. This needs GitHub CLI on the worker and an available shared Gateway GitHub account with access to the repository. It uses that shared identity, not the paired computer's personal login.

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
- [[Changes/OpenClaw/2026-09-05-17-model-support-changes-in-v2026-9-2|17 Model Support changes in v2026.9.2]] · Model Support
- [[Changes/OpenClaw/2026-09-05-16-developer-workflow-changes-in-v2026-9-2|16 Developer Workflow changes in v2026.9.2]] · Developer Workflow
- [[Changes/OpenClaw/2026-09-05-21-memory-and-personalization-changes-in-v2026-9-2|21 Memory and Personalization changes in v2026.9.2]] · Memory and Personalization
- [[Changes/OpenClaw/2026-09-05-4-enterprise-and-administration-changes-in-v2026-9-2|4 Enterprise and Administration changes in v2026.9.2]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-09-05-if-background-image-video-or-music-generation-finishes-but-final-delivery-fails|If background image, video or music generation finishes but final delivery fails…]] · Music Generation
- [[Changes/OpenClaw/2026-09-05-34-agent-mode-changes-in-v2026-9-2|34 Agent Mode changes in v2026.9.2]] · Agent Mode
- [[Changes/OpenClaw/2026-09-05-35-apps-and-integrations-changes-in-v2026-9-2|35 Apps and Integrations changes in v2026.9.2]] · Apps and Integrations
- [[Changes/OpenClaw/2026-09-05-8-automation-and-scheduling-changes-in-v2026-9-2|8 Automation and Scheduling changes in v2026.9.2]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-09-05-9-collaboration-changes-in-v2026-9-2|9 Collaboration changes in v2026.9.2]] · Collaboration
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
## Nearby in Account and Access

- Earlier: 2026-09-04 · Wispr Flow · [[Changes/Wispr Flow/2026-09-04-a-smoother-sign-in-handoff-android|A Smoother Sign-In Handoff (Android)]]
- Later: 2026-09-07 · Krea · [[Changes/Krea/2026-09-07-sso-connection-names-and-workspace-auto-join|SSO connection names and workspace auto-join]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Notion · [[Changes/Notion/2020-07-28-sign-into-notion-with-your-apple-id-the-perfect-combination-of-speedy-and-secure|Sign into Notion with your Apple ID 🗝️ The perfect combination of speedy and secure]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-05-45fd4c&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-05-20-account-and-access-changes-in-v2026-9-2.md%0ACard%20ID%3A%20openclaw-2026-09-05-45fd4c%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.2%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->