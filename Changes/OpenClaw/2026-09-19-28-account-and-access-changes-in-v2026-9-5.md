---
card_id: openclaw-2026-09-19-70c558
date: '2026-09-19'
description: 'OpenClaw · 2026-09-19 · Account and Access: 28 changes in v2026.9.5
  — A browser using only its device token can now reconnect after an administrator
  approves…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires
    login]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1269
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 303ca3384da0d5e655af6edadba31ae2e5e05748f09bda2cf876ee2a89103911
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-19-70c558
  comparison: ''
  date: '2026-09-19'
  description: 'OpenClaw — v2026.9.5: 28 Account and Access changes'
  evidence:
  - quote: A browser using only its device token can now reconnect after an administrator
      approves Request admin , instead of being sent back to login. Changing shared
      authentication still invalidates old credentials, and previously damaged tokens
      are not automatically repaired. Pairing requests also accept pasted IDs with
      surrounding spaces or newlines, and long Node host setup commands fit inside
      the pairing dialog while remaining complete when copied.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Authorized operators using trusted-proxy authentication can generate mobile
      setup codes without adding an unused Gateway token or password. Your phone must
      still sign in through the proxy, and scanning a QR code does not sign you into
      Cloudflare Access. Secure-transport rules and pairing approval still apply,
      and authentication mode none is still rejected.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: When expired website sign-in blocks images or files, OpenClaw first tries
      to renew access without interrupting the conversation or unsent draft. Silent
      renewal needs a valid global sign-in session and browser cookie and framing
      support. If that cannot work, sign in in a separate tab and return to the same
      chat; failed attachments retry after access is verified. Session lifetimes stay
      unchanged.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Some sites block embedding or need a separate sign-in; Open website opens
      them in another tab. Personal layout preferences, docking, and dimensions stay
      in this browser, and a live website frame is kept only while its task view remains
      cached.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: A stalled Zalo Personal connection attempt now times out after 30 seconds
      and releases its listener so the existing retry path can try again. That is
      a limit for one connection attempt, not a recovery deadline for every outage.
      Restoring saved sessions and routinely refreshing credentials also move their
      database work off the Gateway thread on supporting hosts, preserving logout
      and replacement-session checks. QR-login replacement and logout keep their existing
      synchronous storage paths.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: The WeChat guide now explains that plugin version 2.4.8 uses its own sender
      list and QR-login fallback, so normal OpenClaw pairing approvals and revocations
      do not reliably control its chat access. Disable that plugin if you require
      those controls. This is corrected guidance; the plugin's behavior has not changed.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: The bottom-left account menu now shows Gateway health and switching controls,
      with hints for existing keyboard shortcuts. Use Command-click or Control-click
      to open another window. Expired Cloudflare sign-ins have a recovery page inside
      the affected window; windows restored at launch wait for you to click “Sign
      in again.”
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: If the approval page does not appear, choose “Open browser” and check the
      browser account before approving. A timed-out attempt needs a fresh sign-in.
      Closing a sign-in window opened by a command cancels that command.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Each Mac chat now keeps its own browser tabs, so you can switch conversations
      and return to the pages you left open for that chat. Tabs last while the window
      stays open and can show the page's own icon. Update both the Mac app and Gateway-served
      UI for this behavior. Older tabs stay shared until closed, and login cookies
      remain shared across chats in the same window.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Authorized Computer work can keep an unlocked Mac awake for up to an hour
      from its first action. To keep it awake between jobs while connected and hosting,
      enable Unattended desktop hosting under Settings → This Mac and accept the native
      confirmation. That option is off by default. It does not bypass login or lock;
      after locking or losing access, sign in normally and start fresh Computer work.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: iOS and Mac chat show the model, thinking and Fast controls supported by
      your current session, with provider sign-in available from chat. Mac Quick Chat
      refreshes choices without losing your draft and offers supported speed settings
      for the next message. If an older Gateway cannot supply native model choices,
      update it or use /models and /login .
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Dashboard controls stay visible and clickable in full screen, including
      after reconnecting. Commands that finish quickly return their actual result
      instead of a false timeout, and rapid changes to launch-at-login preserve your
      latest choice. Remote-mode users who enable Cookie Sync also avoid its startup-watchdog
      crash.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Model controls follow the selected model's supported Fast and thinking
      choices, and refresh failures show a warning with a way to retry. Provider sign-in
      and API-key setup are available from the picker when supported by your Gateway
      and administrative access; older Gateways show update guidance and retain slash
      commands.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: The Tauri companion gains browser tabs beside your conversations, with
      navigation, screenshots, element inspection and native Save dialogs. Conversations
      keep separate tabs, but all reading tabs share cookies in one private browsing
      session. Closing every tab, switching Gateways or quitting ends that session;
      sign-in links still open in your system browser.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: The Linux companion can retry your saved remote Gateway, and leaving Connection
      Settings keeps your active chat and sign-in. If the app cannot tell whether
      the Gateway is running, it keeps trying to reconnect and offers Start Gateway
      only after confirming it has stopped. A failure to monitor system sleep no longer
      leaves the app thinking the computer is asleep and blocking local recovery.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: On Models, administrators can compare remaining Codex usage beside each
      saved subscription login and refresh accounts individually. This display excludes
      API keys and other providers. Stored accounts return to Ready after verified
      quota recovery without a Gateway restart.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Choosing Show all after sign-in reveals models already fetched from your
      account. Model lists can refresh expired provider catalogs in the background
      while keeping saved choices available, and a failed refresh leaves a warning
      you can retry. Model permissions now match the exact provider and model, so
      explicitly allow the intended pair if an older accidental match stops working.
      Showing a model never grants account access to it.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: 'Ordinary Codex-backed OpenClaw chats now use per-agent storage instead
      of automatically appearing in personal Codex Desktop or CLI history. If you
      relied on OpenClaw borrowing your personal login, select detected Codex in Model
      Setup to sign in, or run openclaw models auth login --provider openai and select
      the resulting profile. Explicit appServer.homeScope: "user" remains an opt-in;
      remove it to use isolated storage. Your existing personal history is neither
      moved nor deleted. See OpenAI runtimes for setup.'
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Long conversations can continue through compaction without overstated context
      pressure prematurely blocking the next request. Saved summaries retain their
      full streamed text, checkpoint branches leave the source conversation running,
      and recorded speaker IDs help preserve attribution. Slow required compaction
      can finish without repeatedly restarting the waiting reply, while authentication
      failures now reach recovery guidance. These fixes preserve usable context within
      the model's existing capacity.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Each alternative needs an enabled, compatible runtime and current account
      access. Adding a picker choice grants no credentials or access. ACP and locked
      sessions keep their runtime restrictions, and unavailable saved alternatives
      are discarded rather than silently replaced. Use explicit runtime IDs rather
      than auto or default ; wildcard model entries are excluded. Opening the picker
      uses prepared choices, while Refresh checks for new ones.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: A shared Browser dashboard lets you and your agent use the same page. Enter
      a note or change an app's filters, then ask your agent to continue from what
      you changed. It uses a local OpenClaw-managed browser profile and that profile's
      login state, including for permitted HTTP apps shown through the HTTPS Control
      UI.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: This default can change which machine and browser login session you use
      after upgrading. To keep using a node's existing session, select that node explicitly
      or set gateway.nodes.browser.node .
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Reef can reuse an explicitly configured OpenAI OAuth login for message
      checks, with the required model permissions and compatible Codex runtime policy.
      Existing API-key setups remain supported. If message-tracking storage fills,
      the shared inbox stays connected and parks affected entries until capacity becomes
      available.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: An entry may be delivered again if its earlier delivery could not be recorded.
      Before downgrading from the OAuth setup to an older version, restore the older
      API-key configuration described in the Reef guide.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Missing credentials under numeric account names or dotted provider keys
      now point to the exact setting instead of surfacing as a later authentication
      failure. The config command also preserves literal secret-provider arguments,
      including empty strings and surrounding whitespace. Quote those values in your
      shell, and reapply any previously saved argument whose whitespace an older command
      removed.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Browser download actions now follow the selected profile's destination
      restrictions, so downloads that previously bypassed those rules can be rejected.
      Nextcloud Talk and Feishu webhook listeners also limit simultaneous incomplete
      requests before authentication, reducing the resources those requests can hold
      open.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: At saturation, legitimate webhook arrivals can receive a closed 429 response
      and may be lost. Reduce or buffer upstream concurrency where needed, and do
      not assume rejected deliveries will retry. The Nextcloud Talk guide explains
      its fixed read limit and overload behavior. Mattermost slash commands now have
      separate upload capacity for recognized command credentials. Preserve the original
      Authorization Token header through proxies; OAuth callbacks and requests with
      stripped headers share anonymous capacity and can be throttled, as explained
      in Mattermost troubleshooting .
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  - quote: Reasoning choices can affect cost, waiting time, and review quality. Fast
      mode requests priority processing on supported OpenAI Responses and ChatGPT/OAuth
      routes and may cost more; other providers may ignore it. If you enable these
      options, remove the new thinking and fastMode keys before downgrading to a version
      that does not recognize them.
    source_release: https://docs.openclaw.ai/releases/2026.9.5
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 28-account-and-access-changes-in-v2026-9-5
  source_release: openclaw-2026-09-19-v2026-9-5-506f537c
  source_type: openclaw_changelog
  theme: account-access
  title: 28 Account and Access changes in v2026.9.5
  type: change
related_changes:
- '[[Changes/Claude Code/2026-09-17-improved-claude-apps-gateway-sign-in-rate-limit-errors-login-now-explains-the-re|Improved
  Claude apps gateway sign-in rate limit errors]]'
- '[[Changes/Claude Code/2026-09-17-added-the-signed-in-account-to-claude-apps-gateway-sign-in-when-the-gateway-name|Added
  the signed-in account to Claude apps gateway sign-in]]'
- '[[Changes/Codex CLI/2026-09-17-6-account-and-access-changes-in-rust-v0-155-0|6
  Account and Access changes in rust-v0.155.0]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-19-v2026-9-5-506f537c|openclaw-2026-09-19-v2026-9-5-506f537c]]'
source_type: openclaw_changelog
theme: account-access
title: 28 Account and Access changes in v2026.9.5
type: change
---

<!-- chronolog:begin region="header" -->
# 28 Account and Access changes in v2026.9.5

**OpenClaw** · 2026-09-19 · [[Themes/account-access|Account and Access]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.5) · from [[Releases/OpenClaw/openclaw-2026-09-19-v2026-9-5-506f537c|v2026.9.5]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> A browser using only its device token can now reconnect after an administrator approves Request admin , instead of being sent back to login. Changing shared authentication still invalidates old credentials, and previously damaged tokens are not automatically repaired. Pairing requests also accept pasted IDs with surrounding spaces or newlines, and long Node host setup commands fit inside the pairing dialog while remaining complete when copied.

> Authorized operators using trusted-proxy authentication can generate mobile setup codes without adding an unused Gateway token or password. Your phone must still sign in through the proxy, and scanning a QR code does not sign you into Cloudflare Access. Secure-transport rules and pairing approval still apply, and authentication mode none is still rejected.

> When expired website sign-in blocks images or files, OpenClaw first tries to renew access without interrupting the conversation or unsent draft. Silent renewal needs a valid global sign-in session and browser cookie and framing support. If that cannot work, sign in in a separate tab and return to the same chat; failed attachments retry after access is verified. Session lifetimes stay unchanged.

> Some sites block embedding or need a separate sign-in; Open website opens them in another tab. Personal layout preferences, docking, and dimensions stay in this browser, and a live website frame is kept only while its task view remains cached.

> A stalled Zalo Personal connection attempt now times out after 30 seconds and releases its listener so the existing retry path can try again. That is a limit for one connection attempt, not a recovery deadline for every outage. Restoring saved sessions and routinely refreshing credentials also move their database work off the Gateway thread on supporting hosts, preserving logout and replacement-session checks. QR-login replacement and logout keep their existing synchronous storage paths.

> The WeChat guide now explains that plugin version 2.4.8 uses its own sender list and QR-login fallback, so normal OpenClaw pairing approvals and revocations do not reliably control its chat access. Disable that plugin if you require those controls. This is corrected guidance; the plugin's behavior has not changed.

> The bottom-left account menu now shows Gateway health and switching controls, with hints for existing keyboard shortcuts. Use Command-click or Control-click to open another window. Expired Cloudflare sign-ins have a recovery page inside the affected window; windows restored at launch wait for you to click “Sign in again.”

> If the approval page does not appear, choose “Open browser” and check the browser account before approving. A timed-out attempt needs a fresh sign-in. Closing a sign-in window opened by a command cancels that command.

> Each Mac chat now keeps its own browser tabs, so you can switch conversations and return to the pages you left open for that chat. Tabs last while the window stays open and can show the page's own icon. Update both the Mac app and Gateway-served UI for this behavior. Older tabs stay shared until closed, and login cookies remain shared across chats in the same window.

> Authorized Computer work can keep an unlocked Mac awake for up to an hour from its first action. To keep it awake between jobs while connected and hosting, enable Unattended desktop hosting under Settings → This Mac and accept the native confirmation. That option is off by default. It does not bypass login or lock; after locking or losing access, sign in normally and start fresh Computer work.

> iOS and Mac chat show the model, thinking and Fast controls supported by your current session, with provider sign-in available from chat. Mac Quick Chat refreshes choices without losing your draft and offers supported speed settings for the next message. If an older Gateway cannot supply native model choices, update it or use /models and /login .

> Dashboard controls stay visible and clickable in full screen, including after reconnecting. Commands that finish quickly return their actual result instead of a false timeout, and rapid changes to launch-at-login preserve your latest choice. Remote-mode users who enable Cookie Sync also avoid its startup-watchdog crash.

> Model controls follow the selected model's supported Fast and thinking choices, and refresh failures show a warning with a way to retry. Provider sign-in and API-key setup are available from the picker when supported by your Gateway and administrative access; older Gateways show update guidance and retain slash commands.

> The Tauri companion gains browser tabs beside your conversations, with navigation, screenshots, element inspection and native Save dialogs. Conversations keep separate tabs, but all reading tabs share cookies in one private browsing session. Closing every tab, switching Gateways or quitting ends that session; sign-in links still open in your system browser.

> The Linux companion can retry your saved remote Gateway, and leaving Connection Settings keeps your active chat and sign-in. If the app cannot tell whether the Gateway is running, it keeps trying to reconnect and offers Start Gateway only after confirming it has stopped. A failure to monitor system sleep no longer leaves the app thinking the computer is asleep and blocking local recovery.

> On Models, administrators can compare remaining Codex usage beside each saved subscription login and refresh accounts individually. This display excludes API keys and other providers. Stored accounts return to Ready after verified quota recovery without a Gateway restart.

> Choosing Show all after sign-in reveals models already fetched from your account. Model lists can refresh expired provider catalogs in the background while keeping saved choices available, and a failed refresh leaves a warning you can retry. Model permissions now match the exact provider and model, so explicitly allow the intended pair if an older accidental match stops working. Showing a model never grants account access to it.

> Ordinary Codex-backed OpenClaw chats now use per-agent storage instead of automatically appearing in personal Codex Desktop or CLI history. If you relied on OpenClaw borrowing your personal login, select detected Codex in Model Setup to sign in, or run openclaw models auth login --provider openai and select the resulting profile. Explicit appServer.homeScope: "user" remains an opt-in; remove it to use isolated storage. Your existing personal history is neither moved nor deleted. See OpenAI runtimes for setup.

> Long conversations can continue through compaction without overstated context pressure prematurely blocking the next request. Saved summaries retain their full streamed text, checkpoint branches leave the source conversation running, and recorded speaker IDs help preserve attribution. Slow required compaction can finish without repeatedly restarting the waiting reply, while authentication failures now reach recovery guidance. These fixes preserve usable context within the model's existing capacity.

> Each alternative needs an enabled, compatible runtime and current account access. Adding a picker choice grants no credentials or access. ACP and locked sessions keep their runtime restrictions, and unavailable saved alternatives are discarded rather than silently replaced. Use explicit runtime IDs rather than auto or default ; wildcard model entries are excluded. Opening the picker uses prepared choices, while Refresh checks for new ones.

> A shared Browser dashboard lets you and your agent use the same page. Enter a note or change an app's filters, then ask your agent to continue from what you changed. It uses a local OpenClaw-managed browser profile and that profile's login state, including for permitted HTTP apps shown through the HTTPS Control UI.

> This default can change which machine and browser login session you use after upgrading. To keep using a node's existing session, select that node explicitly or set gateway.nodes.browser.node .

> Reef can reuse an explicitly configured OpenAI OAuth login for message checks, with the required model permissions and compatible Codex runtime policy. Existing API-key setups remain supported. If message-tracking storage fills, the shared inbox stays connected and parks affected entries until capacity becomes available.

> An entry may be delivered again if its earlier delivery could not be recorded. Before downgrading from the OAuth setup to an older version, restore the older API-key configuration described in the Reef guide.

> Missing credentials under numeric account names or dotted provider keys now point to the exact setting instead of surfacing as a later authentication failure. The config command also preserves literal secret-provider arguments, including empty strings and surrounding whitespace. Quote those values in your shell, and reapply any previously saved argument whose whitespace an older command removed.

> Browser download actions now follow the selected profile's destination restrictions, so downloads that previously bypassed those rules can be rejected. Nextcloud Talk and Feishu webhook listeners also limit simultaneous incomplete requests before authentication, reducing the resources those requests can hold open.

> At saturation, legitimate webhook arrivals can receive a closed 429 response and may be lost. Reduce or buffer upstream concurrency where needed, and do not assume rejected deliveries will retry. The Nextcloud Talk guide explains its fixed read limit and overload behavior. Mattermost slash commands now have separate upload capacity for recognized command credentials. Preserve the original Authorization Token header through proxies; OAuth callbacks and requests with stripped headers share anonymous capacity and can be throttled, as explained in Mattermost troubleshooting .

> Reasoning choices can affect cost, waiting time, and review quality. Fast mode requests priority processing on supported OpenAI Responses and ChatGPT/OAuth routes and may cost more; other providers may ignore it. If you enable these options, remove the new thinking and fastMode keys before downgrading to a version that does not recognize them.

Source: https://docs.openclaw.ai/releases/2026.9.5
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-09-19-20-context-window-changes-in-v2026-9-5|20 Context Window changes in v2026.9.5]] · Context Window
- [[Changes/OpenClaw/2026-09-19-14-collaboration-changes-in-v2026-9-5|14 Collaboration changes in v2026.9.5]] · Collaboration
- [[Changes/OpenClaw/2026-09-19-the-browser-sidebar-gains-a-download-file-button-for-the-image-video-or-document|The Browser sidebar gains a Download file button for the image, video, or document…]] · Multimodal Input
- [[Changes/OpenClaw/2026-09-19-29-developer-workflow-changes-in-v2026-9-5|29 Developer Workflow changes in v2026.9.5]] · Developer Workflow
- [[Changes/OpenClaw/2026-09-19-5-reliability-and-performance-changes-in-v2026-9-5|5 Reliability and Performance changes in v2026.9.5]] · Reliability and Performance
- [[Changes/OpenClaw/2026-09-19-retained-conversation-history-continues-to-follow-current-sharing-permissions-af|Retained conversation history continues to follow current sharing permissions after…]] · Projects and Workspaces
- [[Changes/OpenClaw/2026-09-19-2-enterprise-and-administration-changes-in-v2026-9-5|2 Enterprise and Administration changes in v2026.9.5]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-09-19-72-agent-mode-changes-in-v2026-9-5|72 Agent Mode changes in v2026.9.5]] · Agent Mode
- [[Changes/OpenClaw/2026-09-19-21-editor-experience-changes-in-v2026-9-5|21 Editor Experience changes in v2026.9.5]] · Editor Experience
- [[Changes/OpenClaw/2026-09-19-28-model-support-changes-in-v2026-9-5|28 Model Support changes in v2026.9.5]] · Model Support
- [[Changes/OpenClaw/2026-09-19-39-safety-and-privacy-changes-in-v2026-9-5|39 Safety and Privacy changes in v2026.9.5]] · Safety and Privacy
- [[Changes/OpenClaw/2026-09-19-14-automation-and-scheduling-changes-in-v2026-9-5|14 Automation and Scheduling changes in v2026.9.5]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-09-19-32-interface-experience-changes-in-v2026-9-5|32 Interface Experience changes in v2026.9.5]] · Interface Experience
- [[Changes/OpenClaw/2026-09-19-you-can-now-set-the-approval-reviewer-s-reasoning-and-optional-fast-mode-indepen|Set the approval reviewer's reasoning and optional Fast mode independently…]] · Agent Mode
- [[Changes/OpenClaw/2026-09-19-you-can-now-install-the-cli-on-freebsd-with-install-cli-sh-using-system-node-and|Install the CLI on FreeBSD with install-cli.sh using system Node and npm]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-09-19-6-pricing-model-changes-in-v2026-9-5|6 Pricing Model changes in v2026.9.5]] · Pricing Model
- [[Changes/OpenClaw/2026-09-19-31-memory-and-personalization-changes-in-v2026-9-5|31 Memory and Personalization changes in v2026.9.5]] · Memory and Personalization
- [[Changes/OpenClaw/2026-09-19-you-can-now-ask-btw-side-questions-about-photos-attached-to-the-current-message|Ask /btw side questions about photos attached to the current message when using…]] · Apps and Integrations
- [[Changes/OpenClaw/2026-09-19-52-apps-and-integrations-changes-in-v2026-9-5|52 Apps and Integrations changes in v2026.9.5]] · Apps and Integrations
- [[Changes/OpenClaw/2026-09-19-23-mobile-and-desktop-changes-in-v2026-9-5|23 Mobile and Desktop changes in v2026.9.5]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-09-19-6-search-and-browsing-changes-in-v2026-9-5|6 Search and Browsing changes in v2026.9.5]] · Search and Browsing
- [[Changes/OpenClaw/2026-09-19-video-generation-preserves-repeated-reference-positions-so-the-same-image-can-se|Video generation preserves repeated reference positions, so the same image can serve…]] · Music Generation
- [[Changes/OpenClaw/2026-09-19-browser-pages-appear-directly-in-the-chat-panel-header-leaving-more-room-for-the|Browser pages appear directly in the Chat panel header, leaving more room for the page]] · Accessibility and Localization
- [[Changes/OpenClaw/2026-09-19-7-files-and-data-changes-in-v2026-9-5|7 Files and Data changes in v2026.9.5]] · Files and Data
- [[Changes/OpenClaw/2026-09-19-15-voice-and-audio-changes-in-v2026-9-5|15 Voice and Audio changes in v2026.9.5]] · Voice and Audio
- [[Changes/OpenClaw/2026-09-19-shared-helpers-consolidate-repeated-implementation-including-preparation-and-res|Shared helpers consolidate repeated implementation, including preparation…]] · Video Generation
- [[Changes/OpenClaw/2026-09-19-171-other-changes-in-v2026-9-5|171 other changes in v2026.9.5]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2026-09-17 · Codex CLI · [[Changes/Codex CLI/2026-09-17-6-account-and-access-changes-in-rust-v0-155-0|6 Account and Access changes in rust-v0.155.0]]
- Later: 2026-09-21 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-09-21-managed-plugin-commands-load-organization-marketplace-policy-with-environment-gi|Managed plugin commands load organization marketplace policy with environment…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-30 · Cursor · [[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires login]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-19-70c558&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-19-28-account-and-access-changes-in-v2026-9-5.md%0ACard%20ID%3A%20openclaw-2026-09-19-70c558%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.5%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->