---
card_id: openclaw-2026-07-13-a77324
date: '2026-07-13'
description: 'OpenClaw · 2026-07-13 · Mobile and Desktop: 224 changes in v2026.7.1
  — Mobile pairing, Gateway health, desktop-node approvals, linked GitHub work, workspace…'
diffusion:
  first_in_tracked: "[[Changes/Cursor/2023-03-14-windows-and-linux-support|Windows
    and Linux support \U0001F973]]"
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1217
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: mobile-desktop
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 9aa4462798341a966177c9139aa50a0559e507d5ed29f412163593fbbb72de2c
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-07-13-a77324
  comparison: ''
  date: '2026-07-13'
  description: 'OpenClaw — v2026.7.1: 224 Mobile and Desktop changes'
  evidence:
  - quote: Mobile pairing, Gateway health, desktop-node approvals, linked GitHub work,
      workspace files, scheduled jobs, worktrees, Workboard items, and background
      tasks are now available closer to the conversation. Their status, permissions,
      and next steps are also clearer.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Paired administrators can now create a mobile setup QR or copyable code
      from Control UI Nodes and use it to connect an official iOS or Android app.
      #94672 Thanks @bkudiess, @douhualili.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'The redesigned Control UI composer keeps attachments, provider and model
      selection, voice, run state, and message actions clearer and more stable across
      mobile and desktop layouts. #100461 Thanks @fuller-stack-dev.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Session lists across web and mobile now support pinned and custom groups,
      shared read and unread status, background-output indicators, transcript forking,
      and in-place rename, archive, move, and delete actions. #100814'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Expired mobile-pairing codes now explain how to run /pair qr again in
      the selected language. Sources: bb4afe4 , da9308d , dfaec18 , 6b7986e , 21af6e7
      , 4e62124 , 6cd0106 , a72a641 , a143ae4 , cd30b1c , f69e27a , ccddbee , 9ed03df
      , f84243f , 3d06ee9 , 9bd071e , 405b7a5 , 1a160ce .'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'The Control UI now stays fixed during trackpad overscroll on Mac and desktop
      browsers while chat threads and lists continue scrolling normally. #99830'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Administrators can now open mobile pairing from any Control UI page or
      Quick Settings, while non-admin operators continue to see the action disabled
      with an access explanation. #100157'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'The Control UI now shows a ready mobile-pairing QR code immediately even
      when the pending-device list is slow, then adds approval requests when they
      arrive. #100179'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Desktop Control UI users can choose whether Enter sends or inserts a new
      line, with Command+Enter or Ctrl+Enter available as the send shortcut and the
      choice retained for that Gateway. #100810 Thanks @moomx, @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: The Control UI mobile-pairing flow now appears in the selected language
      across 18 supported locales instead of mixing localized screens with English
      setup text. c78b0d5
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'The Control UI now shows execution approvals for supported desktop nodes
      and rejects pending, unsupported, or policy-blocked requests before they reach
      the node. #100505 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'The Control UI mobile-pairing flow is now fully localized for Hindi and
      Russian users, from setup-code creation through pending-device management. #100040'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Control UI tool-call bubbles and error badges now share clean right-edge
      alignment, so failed activity is easier to scan on phone-sized and desktop chats.
      #100163 Thanks @steipete-oai.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Desktop Control UI users can hover a shortened recent-session name to
      reveal its hidden tail and distinguish similar conversations without opening
      each one. #100276'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Long /btw answers in the desktop Control UI now stay within the browser
      window and scroll inside the result card, while mobile retains full-card scrolling.
      #101169 Thanks @snoutfirst.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'New Android users now get a guided first-run path through setup-code or
      QR entry, Gateway pairing, node approval, permissions, recovery steps, and confirmed
      phone readiness before onboarding completes. #98752 Thanks @jesse-merhi.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'macOS onboarding now offers the Gateway''s supported text-inference provider
      catalog instead of only Anthropic, OpenAI, and Google, and tests credentials
      before saving them. #101132'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: These improvements also bring the native clients closer together. Mobile
      queues survive app restarts, the macOS app gains fuller session and transcript
      tools, and each client refreshes the same conversation when the Gateway returns.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'iOS and Android chats now preserve the reader''s scroll position as new
      messages and tool activity arrive, with a clear way to return to the latest
      reply. #98258 Related #98255 . Thanks @christopheraaronhogg.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'iOS users can queue chat messages while disconnected, keep them through
      app restarts, and send them in order after reconnection with clear retry and
      delete controls. #100331'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Apple Watch users can dictate a message and hear OpenClaw''s final reply
      on the Watch, with separate silent-send, cancel, and stop controls. #100283'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Android chat now shows the last known transcript immediately and keeps
      recent cached conversations readable during a Gateway outage, then refreshes
      them after reconnection. #100227'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Android users can queue text while the Gateway is offline, keep it through
      an app restart, and send it in order after reconnection with Retry and Delete
      controls for failures. #100290'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'OpenClaw agents can now run short tasks on chat-capable Ollama models
      installed on paired macOS, Linux, or Windows nodes, with a separate control
      for disabling node inference. #99234 Related #99228 .'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: WhatsApp reconnects and overlapping replies are less likely to lose, skip,
      or disorder messages. Logged-out accounts remain stopped until they are deliberately
      reconnected, while accepted messages and completed replies continue more reliably
      through brief connection changes.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Logged-out or replaced WhatsApp accounts now stay stopped until reconnection
      instead of entering repeated restart loops that can consume resources and slow
      other accounts. #78511 Thanks @openperf.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Eligible WhatsApp messages received during a brief reconnect now reach
      OpenClaw for an automatic reply instead of being marked read and silently skipped.
      #80642 Thanks @vishalj99.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Concurrent WhatsApp Web replies, media, reactions, and queued messages
      now send one at a time per account, reducing interference and unpredictable
      delivery order. #99050 Thanks @ooiuuii.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Completed WhatsApp replies now continue delivering when another message
      arrives mid-delivery, so overlapping conversations are less likely to go unexpectedly
      silent. #100205'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Scheduled work can wake when a command finishes or a watched condition
      changes, remote browser control can pair selected signed-in tabs and save completed
      downloads safely, and guarded workspace terminals are available across web and
      mobile.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'The bundled Chrome extension now lets users control selected signed-in
      tabs from a phone or another channel without someone approving remote debugging
      at the desktop, and removing a tab revokes access. #100619'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Authenticated operators can open a guarded workspace terminal from the
      Control UI , iOS, or Android without leaving the current workspace. Sessions
      use the selected agent's workspace and configured shell, can be disabled by
      policy, and follow the Gateway protocol controls for ownership and connection
      state. Browser terminals can dock, resize, and run side by side, while iOS and
      Android provide focused entry points with clear connection guidance.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Android users can open an agent-workspace shell from Settings > Terminal,
      with clear connection guidance and Gateway credentials passed without placing
      the token in the URL when supported. fcd7eb6
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Replies and media now stay attached to the intended conversation more consistently
      across workspace, mobile, and community channels. Telegram handles albums, progress,
      retries, topics, routing, and delivery with fewer dropped, duplicated, stale,
      or hard-to-read results.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'WhatsApp group owners can reliably use /new , /stop , /status , and similar
      commands even when their sender identity arrives as an internal LID. #93379
      Related #77755 . Thanks @jiveshkalra, @xialonglee.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Attachment download failures across WhatsApp, LINE, Signal, iMessage,
      Teams, Feishu, Mattermost, and Zalo now remain visible and actionable instead
      of disappearing or masquerading as successful media. #100119'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Noisy phone numbers with extra plus signs now match the intended Signal,
      iMessage, or WhatsApp contact, while identities with no digits are rejected
      safely. #100467 Thanks @morluto.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Direct WhatsApp polls now honor the same outreach timelock as other sends
      instead of reaching recipients during a blocked window. 1d128b4 Thanks @vincentkoc.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Replies to OpenClaw-authored WhatsApp group messages now remain visible
      on WhatsApp Desktop and other multi-device clients with their quote context
      intact. #94879 Thanks @bartok9.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'WhatsApp direct sends and automatic replies now render combined bold-and-italic
      Markdown without stray asterisks, including when the formatted text contains
      emoji. #96570 Thanks @llagy007, @weeli-009.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Long WhatsApp auto-reply and inbound-message previews now preserve emoji
      and report the truncated character count accurately, making affected diagnostics
      readable without changing delivery. #96580 Thanks @llagy007, @weeli-009.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Signal QuickStart on macOS now installs signal-cli through Homebrew instead
      of downloading an incompatible Linux package, and gives platform-specific guidance
      when Homebrew is unavailable. #96909 Thanks @romneyda.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Invalid OPENCLAW_WHATSAPP_WEB_SOCKET_URL values now fail immediately with
      a clear configuration error instead of breaking later during socket startup.
      #97697 Thanks @romneyda.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'WhatsApp can now restore a saved linked-device session from a valid credential
      backup when the primary file is interrupted or corrupted, avoiding an unnecessary
      QR re-pair. #99070 Thanks @leonidaslux.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'A WhatsApp message interrupted by a temporary reply-session conflict can
      now be retried instead of being marked delivered and silently ignored on redelivery.
      #101106 Thanks @andersonjeccel.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'WhatsApp direct messages blocked by a reachout timelock now fail immediately
      with an explicit explanation instead of appearing accepted before a later delivery
      error. #101264 Thanks @mcaxtr.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'OpenClaw can use a trusted override to point the normal Baileys socket
      at a compatible local WebSocket endpoint, while normal WhatsApp connections
      continue using the default path unless explicitly overridden. #97155 Thanks
      @romneyda.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Managed Codex users on macOS, Linux, and Windows now receive app-server
      0.144.1 instead of 0.144.0. 5dcba9f Thanks @vincentkoc.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Mobile, WebChat, consult, and other chat.send clients can apply a one-time
      thinking level without losing the assistant reply or having the message mistaken
      for a text command. #98855 Thanks @jesse-merhi.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Codex desktop notifications now shorten long assistant previews containing
      emoji or CJK text without malformed characters. #101534 Thanks @lsr911.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Gateway service regeneration now keeps environment-backed secrets out
      of Linux unit definitions and preserves resolved provider and channel credentials
      on macOS. #96065 Thanks @darren2030, @obviyus.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'The /pair mobile setup flow now accepts local IPv6 ULA and link-local
      Gateway addresses without requiring TLS or a different advertised host, while
      public cleartext URLs remain blocked. #101008 Thanks @zhangguiping-xydt.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Repeated pairing repair attempts now produce one usable macOS approval
      prompt per device instead of stacking stale alerts that cannot complete approval.
      #100976'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Android notification forwarding now leaves WhatsApp, Telegram, Discord,
      and Signal messages with their dedicated channel sessions, preventing duplicate
      or wrong-conversation replies while other selected apps continue to follow forwarding
      rules. #101170'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Android users in supported languages now see key Gateway setup, connection,
      trust, shell, and recovery prompts in their device language. #97111 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'The iOS Control, Chat, Talk, Agent, Settings, Gateway, and Overview screens
      now use clearer navigation, status cues, controls, and a compact expanding chat
      composer. #98452 Thanks @joelnishanth.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'The iOS Control, Agents, and Settings screens are now easier to scan,
      with fewer duplicate destinations, more compact controls, standard navigation,
      and a direct Gateway shortcut from detail views. #98811 Related #98803 .'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Native iOS Chat now gives the conversation more room, uses a compact composer
      that grows with longer drafts, and keeps attachment, Talk, and send controls
      comfortably tappable. #98953 Related #98929 .'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Android can now keep multiple Gateways paired and switch among them without
      repeating setup, while each Gateway retains its own credentials, chat state,
      queued messages, and removable local data. #100947'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'iOS users can pair multiple Gateways once and switch among them while
      keeping credentials, trust, chats, preferences, device access, and push registration
      attached to the correct Gateway. #100948'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Android Chat now lets users choose and verify the configured agent for
      new messages, with Chat, Talk mode, and the home canvas staying aligned to that
      selection. #80422 Thanks @bcperry.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Android chats now render links, lists, quotes, emphasis, code, and plain
      text consistently through the shared Markdown renderer. #88899 Related #88014
      . Thanks @iman-sharif, @pluviobyte.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Android users can open a scheduled job to inspect its timing, payload,
      delivery state, recent results, errors, and exact ID. #95107 Thanks @tosko4.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Android background push-to-talk requests now return NODE_BACKGROUND_UNAVAILABLE
      instead of attempting a microphone start that the operating system may reject.
      #98055 Thanks @nianjiuzst.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Android Gateway actions now stop promptly when their connection closes,
      while requests started after reconnect are not cancelled by old cleanup. #98067
      Thanks @nianjiuzst.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Android can reconnect to the same Gateway without erasing saved access
      when credential fields are blank, while endpoint and setup-code changes avoid
      carrying stale credentials silently. #98277 Thanks @solvely-colin.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Android now gives clearer TLS verification guidance for reachable remote
      and Tailnet Gateways and allows slow valid handshakes more time to show the
      trust prompt. #98366 Related #98365 . Thanks @joshavant.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Android can now pair with local Gateways advertised by standard cleartext
      .local names while continuing to reject unsafe remote or ambiguous cleartext
      addresses. #98439 Thanks @joshavant.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Scanning a valid Gateway setup QR code on Android now starts pairing immediately
      and advances to recovery or approval instead of leaving users on setup. #98483
      Thanks @joshavant.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Android onboarding now marks Contacts and Calendar ready only after both
      read and write access are available, including when those permissions arrive
      in separate prompts. #99158 Thanks @nianjiuzst.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Android now reports Contacts and Calendar access as granted only when
      both reading and adding entries are authorized, preventing misleading setup
      results. #99204 Thanks @nianjiuzst.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Android users can now read bundled third-party and open-source license
      notices directly from Settings > Licenses. #99299 Thanks @joshavant.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'The Android companion no longer forwards OpenClaw''s own notifications
      back to the Gateway, even when older allowlists still include the app package.
      #99568 Thanks @ly85206559.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Android manual Gateway setup now defaults blank ports to 18789 for ordinary
      TLS and cleartext hosts while retaining port 443 for Tailscale MagicDNS. #99865
      Thanks @ly85206559.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Android push-to-talk now takes exclusive microphone control during Talk
      Mode and resumes the correct realtime listener afterward, preventing duplicate
      capture. #99986 Thanks @nianjiuzst.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Android chat now adds light- and dark-mode syntax highlighting to supported
      fenced code, making code-heavy replies easier to scan without delaying partial
      or oversized messages. #100217'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Saved Android Gateway sessions now reconnect promptly when validated internet
      access returns, without unnecessary retries during captive or partial network
      changes. #100347 Thanks @ly85206559.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Android Gateway settings now give connection details, setup fields, and
      helper text more stable space on phone-sized screens, reducing clipping and
      crowding. #100363 Thanks @iwhatsskill.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Android now presents evenly spaced bottom tabs and avoids the chat-cache
      startup crash that could block entry to the post-onboarding shell. #100382 Thanks
      @iwhatsskill.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Android chat now restores an active response with buffered text after
      reconnecting or reopening, and recovers missed event gaps without duplicating
      transcript rows. #100384'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Android now isolates cached conversations and queued commands when users
      re-pair, sign out, or replace Gateway credentials, preventing a new identity
      from inheriting the previous one''s data. #100454'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Android chat now keeps sent messages and active replies stable through
      reconnects, reconciling delayed history without duplicate turns or stale composer
      activity. #100551'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Android users can now long-press an assistant reply and choose Listen,
      with visible playback status, tap-to-stop, and on-device speech fallback. #100772'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Android Talk Mode now keeps push-to-talk busy until the active turn is
      safely handed off, preventing overlapping microphones, stale playback, or the
      wrong relay resuming. #100786'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Android chats now keep internal reasoning, tool results, and raw operational
      details out of both live conversations and reopened offline caches. #100826
      Thanks @iman-sharif.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Android users can long-press a completed chat message to copy all text,
      select an excerpt, share it, or quote it in a reply without losing their current
      draft. #100879 Thanks @bdhwan.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Android chat users can preview a link''s destination and summary before
      opening it, without messages triggering background lookups and with a clear
      unavailable state when inspection fails. #100898'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Android''s model picker now stays aligned with the active chat and agent,
      and a failed model change no longer sends the next message with the previous
      model. #100985'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Android users can search sessions by name, label, or key beyond the currently
      loaded Recent or Archived window, with cached active-session matches still available
      during a temporary Gateway outage. #101102'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Android users with a physical keyboard can press Enter to send a chat
      message while modified Enter combinations remain available for multiline text.
      #101321 Thanks @3ninyt3nin-creator.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Android users can now see safe page thumbnails in expanded link previews,
      while bad or blocked images quietly leave the text preview intact. #101396'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Android users can now archive a chat session and delete it from the Archived
      view even with the app''s bounded operator permissions. #101522'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Indonesian Android strings ship under Android's recognized locale; the
      same prior-release work also prepared the 2026.6.11 Play version and store text.
      3412318 Thanks @joshavant.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Traditional Chinese users now see localized wording for common native app
      actions, permissions, connection messages, and mobile states. f0d2066
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Android now explains in the selected language how to keep a saved token
      or replace an existing Gateway setup. Sources: 32f3eb3 , 6336762 , eeb0682 ,
      ed72b86 , e376f28 , a6631fe , 283bd82 , 6d5a1db , d3087fc , 8bab3f7 , dfb7bc8
      , 7780e30 , b109b88 , c1b7bf2 , dedb17c , 6f84c10 , a8358e8 , 2501ca3 , 1b40eb9
      , d47308f , 3a2baef .'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Android license notices, acknowledgements, empty states, and open-license
      actions now use the selected language across the translations in this release.
      Sources: 4b8b60f , 3b16c41 , c4966e8 , 116e9db , 1617233 , a598c97 , 3b9e0c8
      , eebbf6c , 4c08ea4 , 21be45c , b415072 , 9eec24d , de23987 , 898564e , 7af800b
      , a47ec8d , fac9e58 , 61e4ef0 , 399f9d6 , 9069f69 , 2e049f5 .'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Android pairing and connection failures now provide localized next steps
      for expired codes, credentials, approvals, and retries. Sources: 48eae1b , f095eb9
      , 714c2b0 , d2b5bb7 , d2551bd , 6b91507 , f1c4476 , 5ef6fb4 , e2e0312 , 7fb70b2
      , d702f5c , 24e6b9f , 7cb41cc , a6040c3 , 5e61da3 , 18360ac , 17a1e3b , adafb56
      , 5b5fadb , 9b30570 , d331a36 .'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Android now explains in the selected language when a scoped IPv6 address
      must be replaced with an unscoped address or LAN hostname. Sources: 5793f73
      , 066e697 , bf35947 , 3385817 , a0a5054 , 66cb9a9 , 3da73a7 , df659ec , 57a3975
      , 141b2cf , b043adf , dcc4fa8 , eade8f1 , 72a8098 , 355fa77 , 8cc1786 , a3ef37b
      , cb9ac50 , cab8147 , 7cc3cb0 , ca258fb .'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Android command search and New Chat labels now use the selected language
      across the translations in this release. Sources: b81c58b , 8929118 , 1eee853
      , a5c9662 , 9035729 , 2e359d4 , 91f4d0a , e785c4a , 2c5a076 , 02250d9 , bf23194
      , 603502f , a837a1a , 26df1fa , c926610 , c312f9f , f4275fa , 69d4657 , 3e66eb9
      , db5057e , 1fee4a5 .'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Supported non-English Android builds now localize offline Gateway queue
      guidance and the Retry and Delete actions for text messages. 660d752
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Android link-preview controls and status messages now appear in the selected
      language across refreshed locales. 9997c53
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: The Android background-location explanation, settings action, and Not Now
      choice now appear in the selected language when Always location mode is offered.
      4c38d89
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Android users with a hardware keyboard can now send from the chat composer
      with Enter, while an unaccepted send still preserves the draft. de8db74 Thanks
      @vincentkoc.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Android users can now connect to Gateways behind Cloudflare Access or
      another authenticating reverse proxy by saving the required credential headers
      in Advanced manual-connection settings. #100765'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Android''s About screen now clearly identifies OpenClaw and provides direct
      links to the website, documentation, source repository, and Discord community.
      #100994'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Android chat now renders top-level display LaTeX as readable equations
      while invalid or still-streaming math remains visible as text. #101435'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'macOS onboarding now translates local Gateway installation, checks, repairs,
      retries, paused setup, and resume guidance across the languages updated in this
      release. Sources: 7a717b7 , 85d31e1 , 27778a7 , cffc6ad , ab0d604 , 972d394
      , edbbdf6 , 863a054 , ef5650f , 5f2e51f , 5769416 , a3aa917 , 2f7bd01 , c54a6f3
      , 9c3ffc5 , 469e707 , d066a81 , 72a3b71 , 63aa909 , b68e2e7 .'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Android and iOS now explain which side needs an update when app and Gateway
      protocol versions differ and avoid offering reconnect attempts that cannot succeed.
      #98385 Related #98384 . Thanks @joshavant.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'iOS and Android users can create empty session groups, rename them once
      across their sessions, and remove a group without deleting the conversations
      inside it. #101234'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: OpenClaw's mascot now uses the same float, blink, antenna, and claw animations
      across web, iOS, and Android surfaces while respecting reduced-motion preferences.
      851156a
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: iOS and Android can now show the Gateway terminal as a focused full-screen
      view with stored credentials and a clear unavailable state instead of embedding
      the full desktop Control UI. 9c78489
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Translated Gateway controls on iOS and approval actions on Apple Watch
      no longer fall back to English in supported locales. #97112 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Native iOS Chat now follows Larger Text and Dynamic Type settings for
      messages, the intro, and composer text with less clipping. #97552 Thanks @jmcte.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'iPhone users pairing with a LAN Gateway now stay authenticated after the
      one-time bootstrap so Chat and the node connection do not immediately disconnect.
      #98066 Related #98064 . Thanks @ooiuuii.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'iOS Chat now keeps one final assistant reply per turn instead of briefly
      showing a duplicate that disappears after history refreshes. #98117 Related
      #98116 . Thanks @joshavant, @ooiuuii.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Paired iOS users can start native ElevenLabs Talk with a SecretRef-backed
      Gateway key without copying the credential into plaintext mobile configuration.
      #98210 Related #98209 . Thanks @joshavant, @ooiuuii.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'After scanning an iOS pairing QR code, users now move to a live connection-progress
      screen instead of returning to Welcome while pairing continues invisibly. #98302
      Related #98297 . Thanks @joelnishanth.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'iOS Chat now preserves intentional line breaks in assistant responses
      and other multiline messages without disrupting normal Markdown rendering. #98304
      Related #98028 . Thanks @jabato01, @joshavant.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'The iOS app now opens to Chat for normal launches while preserving direct
      navigation to Control, Settings, Agent, Talk, and nested destinations. #98353
      Thanks @bsniznd.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'iOS Control, Talk, and Settings are easier to scan with clearer status
      emphasis, safer action styling, calmer idle visuals, and improved large-text
      support. #98423 Related #98397 .'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'iOS now explains secure Gateway connection and certificate-verification
      failures precisely and reliably presents the fingerprint trust prompt for first-time
      HTTPS connections. #98429 Thanks @joshavant.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'iOS connection, warning, and information text is now easier to read in
      light and dark modes, and Appearance settings accurately describe the selected
      behavior. #98443 Related #98440 .'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'OpenAI Realtime Talk on iPhone now uses native WebRTC by default, recovers
      continuous sessions from provider disconnects, and respects speaker, Bluetooth,
      and AirPlay output choices. #98563 Thanks @pollybot13.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'New iPhone users now get clearer QR, setup-code, and manual Gateway choices,
      better nearby and connection status, and a direct handoff to Chat after connecting.
      #98868 Thanks @solvely-colin, @thats2easyyy.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'iOS users can correct gateway details after a failed manual setup and
      retry immediately with the values currently on screen. #99220 Related #99219
      . Thanks @abdullahtas0.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'iPhone users who open Chat from a Control detail can now return to that
      same Overview, Activity, Workboard, or Sessions screen without losing their
      place. #99245 Thanks @solvely-colin.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'iOS users can now read OpenClaw''s bundled third-party license acknowledgements
      from Settings > Licenses. #99290 Thanks @joshavant.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'iOS users can now add contacts and search affected records without crashing
      the app or disconnecting the node. #99475 Thanks @abdullahtas0.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'iOS gateway QR pairing now stays open through trust and approval, avoids
      scanner crashes, and keeps credentials and pending actions with the correct
      gateway during switches. #99572 Thanks @pollybot13.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Apple chat now presents fenced code with theme-aware highlighting and
      GitHub-style tables as aligned native tables on iOS and macOS. #100207'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Repeated iOS Gateway setup links now update the visible settings screen
      with the newest connection instead of being consumed by a hidden view or replaying
      stale details. #100328'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'iOS chat now provides tactile feedback for accepted sends and most completed
      or failed runs, though some abort paths may still omit or misclassify failure
      feedback. #100416'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'iOS users can export the current conversation as a named, readable Markdown
      file and save or send it through the system share sheet. #100417'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Choosing While Using for location access on iOS now remains selected after
      approval and after the app is relaunched. #100512'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Talk and Settings rows on iOS now use consistent title sizing and typography,
      making adjacent options easier to scan. #100515'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'The iOS About screen now presents OpenClaw branding, license information,
      and direct links to the website, documentation, GitHub repository, and Discord
      community. #100531'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Apple Watch pairing and companion status now refresh without restarting
      the iPhone app, while cold-launch actions wait for readiness or return a clear
      WATCH_UNAVAILABLE error. #100732'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'iPhone users can now choose Listen on an assistant reply, follow preparation
      and playback status, stop at any time, and fall back to on-device speech when
      needed. #100771'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Display equations in iOS and macOS chats now appear as readable, accessible
      typeset math, with horizontal scrolling for wide formulas and raw text retained
      for malformed expressions. #100829'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Streaming replies in iOS and macOS chats now reveal text more smoothly
      word by word, while reduced-motion users still receive immediate text and completed
      messages remain unchanged. #100884'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Offline iOS messages now survive relaunch, remain tied to their original
      Gateway and conversation, and send once only when delivery can be confirmed,
      with clear uncertain-delivery status when it cannot. #100942'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'iOS and macOS users can preview a safe link''s title and description inside
      chat before deciding whether to open it. #101198'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Expanded link previews on iOS and macOS can now show a safe page thumbnail,
      with the existing text card retained when image loading fails. #101387'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Finished iOS and macOS chat replies now typeset inline LaTeX formulas
      while streaming text, code, currency, and invalid math remain readable as plain
      text. #101388'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'The iOS screen.record command now finishes more reliably with a nonempty
      MP4 instead of crashing the app and disconnecting the node as recording stops.
      #101550 Thanks @tony-ooo.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'iOS pairing codes can now advertise both local and Tailnet Gateway routes,
      allowing the phone to save the first reachable address when it is away from
      the private LAN. #100317'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'iOS chat and macOS webchat users can search, pin, rename, archive, restore,
      and reopen sessions from the in-chat switcher instead of scrolling a simple
      recent list. #101053'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'macOS remote mode can now connect through explicitly selected managed
      SSH aliases and recover app-owned tunnels when SSH multiplexing or backgrounding
      is enabled. #99661'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Multiple macOS app instances now preserve shared SSH tunnel tracking and
      clean up stale processes more reliably, reducing port conflicts after a crash.
      #100601'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: The macOS onboarding and About mascot now more closely matches openclaw.ai
      with theme-aware colors, glow, hover scaling, and smoother motion that keeps
      its antennae visible. 05c9dcc
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'After a macOS crash or force quit, OpenClaw now reclaims confirmed orphaned
      remote-mode SSH tunnels so relaunches can reuse the preferred local Gateway
      port. #100489'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'When Android Chat cannot reach the Gateway, users can open Gateway Settings
      or copy connection diagnostics directly from the blocked screen. #94566 Thanks
      @tosko4.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Android manual Gateway setup now accepts IPv6 hosts such as ::1 directly
      instead of rejecting an address that works only when entered as a bracketed
      WebSocket URL. #99107 Thanks @ly85206559.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Android manual setup now accepts and preserves complete ws:// , wss://
      , and HTTP Gateway addresses, including embedded ports, so private-LAN onboarding
      reaches the intended server. #99110 Related #87216 . Thanks @cursoragent, @ly85206559,
      @ruben2000de.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Android third-party onboarding now recognizes SMS access when send and
      read permissions are granted in separate prompts, while genuinely missing permissions
      remain unauthorized. #99147 Thanks @nianjiuzst.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Android setup now rejects gateway URLs with unsupported IPv6 interface
      zones and directs users to an unscoped address or LAN hostname before saving.
      #99570 Thanks @ly85206559.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Android now preserves specific Gateway and A2UI error codes containing
      numbers, such as A2UI_HOST_UNAVAILABLE , instead of replacing them with a generic
      failure. #99591 Thanks @ly85206559.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Android Talk Mode now delivers agent-consult answers even when realtime
      completion events arrive out of order, preventing sessions from remaining stuck
      on Thinking... . #100049 Thanks @qingminglong.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Android''s Home overview now uses more consistent card, Talk, and recent-session
      spacing for a calmer, easier-to-tap first screen. #100059 Thanks @iwhatsskill.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Android Gateway settings now show both setup actions as full-width buttons,
      keeping Pair New Gateway readable and easy to tap. #100090 Thanks @iwhatsskill.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Tapping an Android notification created by system.notify now brings OpenClaw
      to the foreground. #100888'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Returning to an already loaded Android chat no longer flashes a loading
      screen, and the Overview recent-session list stays deduplicated and steadier
      during refreshes. #100966 Thanks @solvely-colin.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Android Home''s Recent Sessions section now keeps recently active rows
      in a stable order, collapses duplicates, and preserves labels and timestamps
      during partial live refreshes. #101161 Thanks @solvely-colin.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Android physical-keyboard users can press or hold Enter to send once without
      leaving a stray newline, while Shift+Enter and in-progress input-method composition
      keep working. #101360 Thanks @3ninyt3nin-creator, @joshavant.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'The Android app now respects a user''s disconnect, connect, or gateway-switch
      choice during startup and reports final disconnect failures to fire-and-forget
      callers. #101799'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'iOS Gateway connection errors now appear as one dismissible toast that
      returns for a later failure and visibly reacts instead of stacking when the
      same problem repeats. #98856 Thanks @lokimorty.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Equivalent rows in the iPhone Control and Settings tabs now use the same
      rounded icon treatment, making both lists easier to scan. #98936 Related #98916
      . Thanks @sahilsatralkar.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'The iOS About screen now shows a concise app, device-family, and iOS summary
      without duplicated identity or a raw hardware identifier. #98985 Related #98943
      . Thanks @sahilsatralkar.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'The iOS appearance setting now sits in the normal Settings list, shows
      the current System, Light, or Dark choice at a glance, and behaves consistently
      on iPad. #99052 Related #98995 . Thanks @sahilsatralkar.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Cancelling or interrupting an iOS screen.record request now stops the
      system recorder instead of letting capture continue after the tool call fails.
      #99155 Thanks @nianjiuzst.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'iOS now recognizes Limited Photos access as usable, offers in-app controls
      for requesting or managing the grant, and avoids interrupting gateway requests
      with a surprise prompt. #99350 Related #99046 . Thanks @tony-ooo.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Apple Watch quick replies now survive an unavailable iPhone and reconnect
      later to the intended Gateway without being lost, duplicated, or misrouted.
      #100372 Thanks @nianjiuzst.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Tapping the iPhone status bar now leaves the chat at the top for reading
      older messages until the user chooses Jump to latest. #100502'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Already-paired iPhone users now return to Chat, Talk, and Settings instead
      of being trapped in setup when older onboarding flags are stale. #101481'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Android and iOS Gateway setup now clearly requires Secure TLS for remote
      hosts, warns before trusted LAN use without encryption, and offers actionable
      update guidance for protocol mismatches. #101325 Thanks @joshavant.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Long-running system.run commands on the macOS app node no longer make
      the node appear offline or block unrelated Gateway traffic. #100842 Thanks @lvan185,
      @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'The macOS app no longer mistakes a valid launchd-managed local Gateway
      for an unexpected listener and terminates active assistant or channel work.
      #100867 Thanks @lsr911, @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'The macOS app now keeps the same paired device and node identity across
      upgrades, restarts, and Gateway reconnects instead of repeatedly asking for
      approval or creating stale duplicates. #101105 Thanks @yetval.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Android users can sideload the official signed OpenClaw-Android.apk from
      a stable GitHub release and verify it with the published SHA-256 checksums.
      #101212'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Source and macOS package builds no longer fail when the tsdown configuration
      is loaded from a temporary directory that cannot resolve the runtime package.
      #100499'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Android node reconnects now point users from a failed devices approve
      attempt to the correct openclaw nodes approve &lt;requestId&gt; command, including
      a reminder to reuse connection flags. #98115 Thanks @welfo-beo.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'openclaw doctor on Windows now detects supported Chrome versions accurately
      instead of warning that a working installation could not be identified. #87937
      Thanks @mukundakatta.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Doctor lint can now flag the combination of WhatsApp, a strained Gateway
      event loop, and active local TUI sessions that is associated with delayed replies.
      #98406 Thanks @giodl73-repo.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'After openclaw doctor --fix archives a legacy sidecar, the macOS app no
      longer recreates it or triggers the same migration conflict warning on every
      command or Gateway start. #99039 Related #98917 . Thanks @momothemage, @p51moustache.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Timed-out commands on Windows are less likely to leave child processes
      running when taskkill.exe cannot start. #101392 Thanks @aniruddhaadak80, @zengwen-dt.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'openclaw backup create on Windows now retries live-file archive races
      with fresh temporary paths, reducing locked partial backups and leftover retry
      archives. #101464 Thanks @lilan0125, @zoowh.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'A normal Doctor lint run no longer invokes crontab -l for the optional
      legacy WhatsApp check unless an operator explicitly selects it. #99250 Thanks
      @giodl73-repo.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'The macOS guide now gives users a clearer path from downloading the app
      through first-run setup, Gateway selection, and focused troubleshooting. #97120
      Thanks @romneyda.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'OpenClaw''s mobile documentation now identifies the iOS and Android apps
      as official releases and provides consistent App Store, Google Play, and hosted
      iOS push-relay guidance. #98843 Thanks @joshavant.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Android node operators now have an end-to-end guide for securely mirroring
      and controlling a remote device from macOS, including authorization, troubleshooting,
      and clean disconnection. #100398'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Strengthened WhatsApp QA around messages, reactions, replies, media, polls,
      approvals, and group behavior. #95622 Thanks @mcaxtr.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Prepared WhatsApp group activation settings for future storage changes
      while preserving existing activation behavior. #96530 Thanks @jalehman.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Added translation coverage tracking for Android, iOS, and macOS interface
      text across supported locales. #97110 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Clarified macOS release instructions so maintainers use the correct repositories
      and source revisions for each publishing step. #97116 Thanks @romneyda.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Made macOS packaging logs easier to follow by clearly identifying each
      product and architecture being built. #97151 Thanks @romneyda.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Reduced transient Windows, macOS, and iOS validation failures by retrying
      timed-out source checkouts. #97912 Thanks @romneyda.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Made macOS Swift validation recover from incomplete build caches instead
      of repeating the same failure. #98818'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Expanded shared live-channel QA coverage for Telegram, Slack, WhatsApp,
      and Matrix while preserving each channel''s existing behavior. #99707 Thanks
      @romneyda.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Stabilized local macOS validation so maintainers can prepare releases
      and changes without host-specific false failures. #100069'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Added repeatable Android chat-streaming coverage for duplicate, missing,
      stale, timed-out, and malformed messages. #100200'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Strengthened mobile validation so new Gateway events cannot silently go
      unhandled by iOS or Android. #100206'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Let iOS developers keep debug and release apps installed side by side
      with distinct icons and separate app data. #100222'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Stabilized OpenClawKit contract and chat coverage under parallel macOS
      load, reducing false validation failures. #100243'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Cleaned up iOS and Apple Watch debug icons by removing an unintended white
      outer rim. #100259'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Strengthened mobile protocol validation so native iOS or Android changes
      cannot bypass Gateway event coverage. #100278'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Restored a clean Android formatting baseline so contributors can validate
      and extend recent mobile chat work. #100304'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Completed the release record for landed WhatsApp reconnect, quoted-reply,
      credential-recovery, and delivery-status fixes. #100346 Thanks @bartok9, @leonidaslux,
      @masatohoshino, @vishalj99.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Stabilized load-sensitive Matrix, WhatsApp, and process coverage to reduce
      false failures on busy machines. #100420'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Simplified the iOS development app label while keeping debug and release
      installations easy to distinguish. #100466'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Removed an obsolete macOS onboarding test so the current native test target
      compiles cleanly. #100497 Thanks @steipete-oai.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Recorded that persistent logins in new isolated macOS browser profiles
      survive graceful Browser and Gateway restarts. #100507 Thanks @turbotheturtle.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Strengthened macOS browser proxy test reliability by removing intermittent
      failures that caused needless reruns. #100517'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Expanded the Android release record to include five previously shipped
      app improvements. #100702'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Removed obsolete internal code and legacy Android artifacts, leaving a
      smaller maintenance surface. #100823 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Restored compilation of shared Apple platform tests used to validate iOS
      and macOS chat changes. #100903'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Prevented routine iOS package resolution from leaving unrelated local
      file changes behind. #100961'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Standardized Telegram and WhatsApp command and session checks across shared
      and live QA environments. #101080 Thanks @romneyda.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Restored Android formatting and framework validation, reducing release-blocking
      maintenance noise. #101081 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Made Android development commands find a standard local SDK automatically
      in fresh checkouts. #101273'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Added automatic Android formatting enforcement to prevent cleanup drift
      from reaching the main codebase. #101275'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Modernized Android build dependencies and validation while keeping the
      app''s target behavior unchanged. #101356'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Stabilized Android saved-gateway reconnect coverage to reduce intermittent
      validation failures. #101519'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Removed superseded Android screens and translations, reducing maintenance
      work while leaving active app flows unchanged. #101680 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Restored reliable Android translation validation after an obsolete app
      string was removed. #101689'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 224-mobile-and-desktop-changes-in-v2026-7-1
  source_release: openclaw-2026-07-13-v2026-7-1-c2063718
  source_type: openclaw_changelog
  theme: mobile-desktop
  title: 224 Mobile and Desktop changes in v2026.7.1
  type: change
related_changes:
- '[[Changes/OpenCode/2026-07-09-2-mobile-and-desktop-changes-in-v1-17-18-1|2 Mobile
  and Desktop changes in v1.17.18 + 1]]'
- '[[Changes/OpenCode/2026-07-09-12-mobile-and-desktop-changes-in-v1-17-16|12 Mobile
  and Desktop changes in v1.17.16]]'
- '[[Changes/OpenClaw/2026-07-13-whatsapp-and-telegram-default-account-routing-warnings-are-now-available-through|WhatsApp
  and Telegram default-account routing warnings are now available through…]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-07-13-v2026-7-1-c2063718|openclaw-2026-07-13-v2026-7-1-c2063718]]'
source_type: openclaw_changelog
theme: mobile-desktop
title: 224 Mobile and Desktop changes in v2026.7.1
type: change
---

<!-- chronolog:begin region="header" -->
# 224 Mobile and Desktop changes in v2026.7.1

**OpenClaw** · 2026-07-13 · [[Themes/mobile-desktop|Mobile and Desktop]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.7.1) · from [[Releases/OpenClaw/openclaw-2026-07-13-v2026-7-1-c2063718|v2026.7.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Mobile pairing, Gateway health, desktop-node approvals, linked GitHub work, workspace files, scheduled jobs, worktrees, Workboard items, and background tasks are now available closer to the conversation. Their status, permissions, and next steps are also clearer.

> Paired administrators can now create a mobile setup QR or copyable code from Control UI Nodes and use it to connect an official iOS or Android app. #94672 Thanks @bkudiess, @douhualili.

> The redesigned Control UI composer keeps attachments, provider and model selection, voice, run state, and message actions clearer and more stable across mobile and desktop layouts. #100461 Thanks @fuller-stack-dev.

> Session lists across web and mobile now support pinned and custom groups, shared read and unread status, background-output indicators, transcript forking, and in-place rename, archive, move, and delete actions. #100814

> Expired mobile-pairing codes now explain how to run /pair qr again in the selected language. Sources: bb4afe4 , da9308d , dfaec18 , 6b7986e , 21af6e7 , 4e62124 , 6cd0106 , a72a641 , a143ae4 , cd30b1c , f69e27a , ccddbee , 9ed03df , f84243f , 3d06ee9 , 9bd071e , 405b7a5 , 1a160ce .

> The Control UI now stays fixed during trackpad overscroll on Mac and desktop browsers while chat threads and lists continue scrolling normally. #99830

> Administrators can now open mobile pairing from any Control UI page or Quick Settings, while non-admin operators continue to see the action disabled with an access explanation. #100157

> The Control UI now shows a ready mobile-pairing QR code immediately even when the pending-device list is slow, then adds approval requests when they arrive. #100179

> Desktop Control UI users can choose whether Enter sends or inserts a new line, with Command+Enter or Ctrl+Enter available as the send shortcut and the choice retained for that Gateway. #100810 Thanks @moomx, @vincentkoc.

> The Control UI mobile-pairing flow now appears in the selected language across 18 supported locales instead of mixing localized screens with English setup text. c78b0d5

> The Control UI now shows execution approvals for supported desktop nodes and rejects pending, unsupported, or policy-blocked requests before they reach the node. #100505 Thanks @vincentkoc.

> The Control UI mobile-pairing flow is now fully localized for Hindi and Russian users, from setup-code creation through pending-device management. #100040

> Control UI tool-call bubbles and error badges now share clean right-edge alignment, so failed activity is easier to scan on phone-sized and desktop chats. #100163 Thanks @steipete-oai.

> Desktop Control UI users can hover a shortened recent-session name to reveal its hidden tail and distinguish similar conversations without opening each one. #100276

> Long /btw answers in the desktop Control UI now stay within the browser window and scroll inside the result card, while mobile retains full-card scrolling. #101169 Thanks @snoutfirst.

> New Android users now get a guided first-run path through setup-code or QR entry, Gateway pairing, node approval, permissions, recovery steps, and confirmed phone readiness before onboarding completes. #98752 Thanks @jesse-merhi.

> macOS onboarding now offers the Gateway's supported text-inference provider catalog instead of only Anthropic, OpenAI, and Google, and tests credentials before saving them. #101132

> These improvements also bring the native clients closer together. Mobile queues survive app restarts, the macOS app gains fuller session and transcript tools, and each client refreshes the same conversation when the Gateway returns.

> iOS and Android chats now preserve the reader's scroll position as new messages and tool activity arrive, with a clear way to return to the latest reply. #98258 Related #98255 . Thanks @christopheraaronhogg.

> iOS users can queue chat messages while disconnected, keep them through app restarts, and send them in order after reconnection with clear retry and delete controls. #100331

> Apple Watch users can dictate a message and hear OpenClaw's final reply on the Watch, with separate silent-send, cancel, and stop controls. #100283

> Android chat now shows the last known transcript immediately and keeps recent cached conversations readable during a Gateway outage, then refreshes them after reconnection. #100227

> Android users can queue text while the Gateway is offline, keep it through an app restart, and send it in order after reconnection with Retry and Delete controls for failures. #100290

> OpenClaw agents can now run short tasks on chat-capable Ollama models installed on paired macOS, Linux, or Windows nodes, with a separate control for disabling node inference. #99234 Related #99228 .

> WhatsApp reconnects and overlapping replies are less likely to lose, skip, or disorder messages. Logged-out accounts remain stopped until they are deliberately reconnected, while accepted messages and completed replies continue more reliably through brief connection changes.

> Logged-out or replaced WhatsApp accounts now stay stopped until reconnection instead of entering repeated restart loops that can consume resources and slow other accounts. #78511 Thanks @openperf.

> Eligible WhatsApp messages received during a brief reconnect now reach OpenClaw for an automatic reply instead of being marked read and silently skipped. #80642 Thanks @vishalj99.

> Concurrent WhatsApp Web replies, media, reactions, and queued messages now send one at a time per account, reducing interference and unpredictable delivery order. #99050 Thanks @ooiuuii.

> Completed WhatsApp replies now continue delivering when another message arrives mid-delivery, so overlapping conversations are less likely to go unexpectedly silent. #100205

> Scheduled work can wake when a command finishes or a watched condition changes, remote browser control can pair selected signed-in tabs and save completed downloads safely, and guarded workspace terminals are available across web and mobile.

> The bundled Chrome extension now lets users control selected signed-in tabs from a phone or another channel without someone approving remote debugging at the desktop, and removing a tab revokes access. #100619

> Authenticated operators can open a guarded workspace terminal from the Control UI , iOS, or Android without leaving the current workspace. Sessions use the selected agent's workspace and configured shell, can be disabled by policy, and follow the Gateway protocol controls for ownership and connection state. Browser terminals can dock, resize, and run side by side, while iOS and Android provide focused entry points with clear connection guidance.

> Android users can open an agent-workspace shell from Settings > Terminal, with clear connection guidance and Gateway credentials passed without placing the token in the URL when supported. fcd7eb6

> Replies and media now stay attached to the intended conversation more consistently across workspace, mobile, and community channels. Telegram handles albums, progress, retries, topics, routing, and delivery with fewer dropped, duplicated, stale, or hard-to-read results.

> WhatsApp group owners can reliably use /new , /stop , /status , and similar commands even when their sender identity arrives as an internal LID. #93379 Related #77755 . Thanks @jiveshkalra, @xialonglee.

> Attachment download failures across WhatsApp, LINE, Signal, iMessage, Teams, Feishu, Mattermost, and Zalo now remain visible and actionable instead of disappearing or masquerading as successful media. #100119

> Noisy phone numbers with extra plus signs now match the intended Signal, iMessage, or WhatsApp contact, while identities with no digits are rejected safely. #100467 Thanks @morluto.

> Direct WhatsApp polls now honor the same outreach timelock as other sends instead of reaching recipients during a blocked window. 1d128b4 Thanks @vincentkoc.

> Replies to OpenClaw-authored WhatsApp group messages now remain visible on WhatsApp Desktop and other multi-device clients with their quote context intact. #94879 Thanks @bartok9.

> WhatsApp direct sends and automatic replies now render combined bold-and-italic Markdown without stray asterisks, including when the formatted text contains emoji. #96570 Thanks @llagy007, @weeli-009.

> Long WhatsApp auto-reply and inbound-message previews now preserve emoji and report the truncated character count accurately, making affected diagnostics readable without changing delivery. #96580 Thanks @llagy007, @weeli-009.

> Signal QuickStart on macOS now installs signal-cli through Homebrew instead of downloading an incompatible Linux package, and gives platform-specific guidance when Homebrew is unavailable. #96909 Thanks @romneyda.

> Invalid OPENCLAW_WHATSAPP_WEB_SOCKET_URL values now fail immediately with a clear configuration error instead of breaking later during socket startup. #97697 Thanks @romneyda.

> WhatsApp can now restore a saved linked-device session from a valid credential backup when the primary file is interrupted or corrupted, avoiding an unnecessary QR re-pair. #99070 Thanks @leonidaslux.

> A WhatsApp message interrupted by a temporary reply-session conflict can now be retried instead of being marked delivered and silently ignored on redelivery. #101106 Thanks @andersonjeccel.

> WhatsApp direct messages blocked by a reachout timelock now fail immediately with an explicit explanation instead of appearing accepted before a later delivery error. #101264 Thanks @mcaxtr.

> OpenClaw can use a trusted override to point the normal Baileys socket at a compatible local WebSocket endpoint, while normal WhatsApp connections continue using the default path unless explicitly overridden. #97155 Thanks @romneyda.

> Managed Codex users on macOS, Linux, and Windows now receive app-server 0.144.1 instead of 0.144.0. 5dcba9f Thanks @vincentkoc.

> Mobile, WebChat, consult, and other chat.send clients can apply a one-time thinking level without losing the assistant reply or having the message mistaken for a text command. #98855 Thanks @jesse-merhi.

> Codex desktop notifications now shorten long assistant previews containing emoji or CJK text without malformed characters. #101534 Thanks @lsr911.

> Gateway service regeneration now keeps environment-backed secrets out of Linux unit definitions and preserves resolved provider and channel credentials on macOS. #96065 Thanks @darren2030, @obviyus.

> The /pair mobile setup flow now accepts local IPv6 ULA and link-local Gateway addresses without requiring TLS or a different advertised host, while public cleartext URLs remain blocked. #101008 Thanks @zhangguiping-xydt.

> Repeated pairing repair attempts now produce one usable macOS approval prompt per device instead of stacking stale alerts that cannot complete approval. #100976

> Android notification forwarding now leaves WhatsApp, Telegram, Discord, and Signal messages with their dedicated channel sessions, preventing duplicate or wrong-conversation replies while other selected apps continue to follow forwarding rules. #101170

> Android users in supported languages now see key Gateway setup, connection, trust, shell, and recovery prompts in their device language. #97111 Thanks @vincentkoc.

> The iOS Control, Chat, Talk, Agent, Settings, Gateway, and Overview screens now use clearer navigation, status cues, controls, and a compact expanding chat composer. #98452 Thanks @joelnishanth.

> The iOS Control, Agents, and Settings screens are now easier to scan, with fewer duplicate destinations, more compact controls, standard navigation, and a direct Gateway shortcut from detail views. #98811 Related #98803 .

> Native iOS Chat now gives the conversation more room, uses a compact composer that grows with longer drafts, and keeps attachment, Talk, and send controls comfortably tappable. #98953 Related #98929 .

> Android can now keep multiple Gateways paired and switch among them without repeating setup, while each Gateway retains its own credentials, chat state, queued messages, and removable local data. #100947

> iOS users can pair multiple Gateways once and switch among them while keeping credentials, trust, chats, preferences, device access, and push registration attached to the correct Gateway. #100948

> Android Chat now lets users choose and verify the configured agent for new messages, with Chat, Talk mode, and the home canvas staying aligned to that selection. #80422 Thanks @bcperry.

> Android chats now render links, lists, quotes, emphasis, code, and plain text consistently through the shared Markdown renderer. #88899 Related #88014 . Thanks @iman-sharif, @pluviobyte.

> Android users can open a scheduled job to inspect its timing, payload, delivery state, recent results, errors, and exact ID. #95107 Thanks @tosko4.

> Android background push-to-talk requests now return NODE_BACKGROUND_UNAVAILABLE instead of attempting a microphone start that the operating system may reject. #98055 Thanks @nianjiuzst.

> Android Gateway actions now stop promptly when their connection closes, while requests started after reconnect are not cancelled by old cleanup. #98067 Thanks @nianjiuzst.

> Android can reconnect to the same Gateway without erasing saved access when credential fields are blank, while endpoint and setup-code changes avoid carrying stale credentials silently. #98277 Thanks @solvely-colin.

> Android now gives clearer TLS verification guidance for reachable remote and Tailnet Gateways and allows slow valid handshakes more time to show the trust prompt. #98366 Related #98365 . Thanks @joshavant.

> Android can now pair with local Gateways advertised by standard cleartext .local names while continuing to reject unsafe remote or ambiguous cleartext addresses. #98439 Thanks @joshavant.

> Scanning a valid Gateway setup QR code on Android now starts pairing immediately and advances to recovery or approval instead of leaving users on setup. #98483 Thanks @joshavant.

> Android onboarding now marks Contacts and Calendar ready only after both read and write access are available, including when those permissions arrive in separate prompts. #99158 Thanks @nianjiuzst.

> Android now reports Contacts and Calendar access as granted only when both reading and adding entries are authorized, preventing misleading setup results. #99204 Thanks @nianjiuzst.

> Android users can now read bundled third-party and open-source license notices directly from Settings > Licenses. #99299 Thanks @joshavant.

> The Android companion no longer forwards OpenClaw's own notifications back to the Gateway, even when older allowlists still include the app package. #99568 Thanks @ly85206559.

> Android manual Gateway setup now defaults blank ports to 18789 for ordinary TLS and cleartext hosts while retaining port 443 for Tailscale MagicDNS. #99865 Thanks @ly85206559.

> Android push-to-talk now takes exclusive microphone control during Talk Mode and resumes the correct realtime listener afterward, preventing duplicate capture. #99986 Thanks @nianjiuzst.

> Android chat now adds light- and dark-mode syntax highlighting to supported fenced code, making code-heavy replies easier to scan without delaying partial or oversized messages. #100217

> Saved Android Gateway sessions now reconnect promptly when validated internet access returns, without unnecessary retries during captive or partial network changes. #100347 Thanks @ly85206559.

> Android Gateway settings now give connection details, setup fields, and helper text more stable space on phone-sized screens, reducing clipping and crowding. #100363 Thanks @iwhatsskill.

> Android now presents evenly spaced bottom tabs and avoids the chat-cache startup crash that could block entry to the post-onboarding shell. #100382 Thanks @iwhatsskill.

> Android chat now restores an active response with buffered text after reconnecting or reopening, and recovers missed event gaps without duplicating transcript rows. #100384

> Android now isolates cached conversations and queued commands when users re-pair, sign out, or replace Gateway credentials, preventing a new identity from inheriting the previous one's data. #100454

> Android chat now keeps sent messages and active replies stable through reconnects, reconciling delayed history without duplicate turns or stale composer activity. #100551

> Android users can now long-press an assistant reply and choose Listen, with visible playback status, tap-to-stop, and on-device speech fallback. #100772

> Android Talk Mode now keeps push-to-talk busy until the active turn is safely handed off, preventing overlapping microphones, stale playback, or the wrong relay resuming. #100786

> Android chats now keep internal reasoning, tool results, and raw operational details out of both live conversations and reopened offline caches. #100826 Thanks @iman-sharif.

> Android users can long-press a completed chat message to copy all text, select an excerpt, share it, or quote it in a reply without losing their current draft. #100879 Thanks @bdhwan.

> Android chat users can preview a link's destination and summary before opening it, without messages triggering background lookups and with a clear unavailable state when inspection fails. #100898

> Android's model picker now stays aligned with the active chat and agent, and a failed model change no longer sends the next message with the previous model. #100985

> Android users can search sessions by name, label, or key beyond the currently loaded Recent or Archived window, with cached active-session matches still available during a temporary Gateway outage. #101102

> Android users with a physical keyboard can press Enter to send a chat message while modified Enter combinations remain available for multiline text. #101321 Thanks @3ninyt3nin-creator.

> Android users can now see safe page thumbnails in expanded link previews, while bad or blocked images quietly leave the text preview intact. #101396

> Android users can now archive a chat session and delete it from the Archived view even with the app's bounded operator permissions. #101522

> Indonesian Android strings ship under Android's recognized locale; the same prior-release work also prepared the 2026.6.11 Play version and store text. 3412318 Thanks @joshavant.

> Traditional Chinese users now see localized wording for common native app actions, permissions, connection messages, and mobile states. f0d2066

> Android now explains in the selected language how to keep a saved token or replace an existing Gateway setup. Sources: 32f3eb3 , 6336762 , eeb0682 , ed72b86 , e376f28 , a6631fe , 283bd82 , 6d5a1db , d3087fc , 8bab3f7 , dfb7bc8 , 7780e30 , b109b88 , c1b7bf2 , dedb17c , 6f84c10 , a8358e8 , 2501ca3 , 1b40eb9 , d47308f , 3a2baef .

> Android license notices, acknowledgements, empty states, and open-license actions now use the selected language across the translations in this release. Sources: 4b8b60f , 3b16c41 , c4966e8 , 116e9db , 1617233 , a598c97 , 3b9e0c8 , eebbf6c , 4c08ea4 , 21be45c , b415072 , 9eec24d , de23987 , 898564e , 7af800b , a47ec8d , fac9e58 , 61e4ef0 , 399f9d6 , 9069f69 , 2e049f5 .

> Android pairing and connection failures now provide localized next steps for expired codes, credentials, approvals, and retries. Sources: 48eae1b , f095eb9 , 714c2b0 , d2b5bb7 , d2551bd , 6b91507 , f1c4476 , 5ef6fb4 , e2e0312 , 7fb70b2 , d702f5c , 24e6b9f , 7cb41cc , a6040c3 , 5e61da3 , 18360ac , 17a1e3b , adafb56 , 5b5fadb , 9b30570 , d331a36 .

> Android now explains in the selected language when a scoped IPv6 address must be replaced with an unscoped address or LAN hostname. Sources: 5793f73 , 066e697 , bf35947 , 3385817 , a0a5054 , 66cb9a9 , 3da73a7 , df659ec , 57a3975 , 141b2cf , b043adf , dcc4fa8 , eade8f1 , 72a8098 , 355fa77 , 8cc1786 , a3ef37b , cb9ac50 , cab8147 , 7cc3cb0 , ca258fb .

> Android command search and New Chat labels now use the selected language across the translations in this release. Sources: b81c58b , 8929118 , 1eee853 , a5c9662 , 9035729 , 2e359d4 , 91f4d0a , e785c4a , 2c5a076 , 02250d9 , bf23194 , 603502f , a837a1a , 26df1fa , c926610 , c312f9f , f4275fa , 69d4657 , 3e66eb9 , db5057e , 1fee4a5 .

> Supported non-English Android builds now localize offline Gateway queue guidance and the Retry and Delete actions for text messages. 660d752

> Android link-preview controls and status messages now appear in the selected language across refreshed locales. 9997c53

> The Android background-location explanation, settings action, and Not Now choice now appear in the selected language when Always location mode is offered. 4c38d89

> Android users with a hardware keyboard can now send from the chat composer with Enter, while an unaccepted send still preserves the draft. de8db74 Thanks @vincentkoc.

> Android users can now connect to Gateways behind Cloudflare Access or another authenticating reverse proxy by saving the required credential headers in Advanced manual-connection settings. #100765

> Android's About screen now clearly identifies OpenClaw and provides direct links to the website, documentation, source repository, and Discord community. #100994

> Android chat now renders top-level display LaTeX as readable equations while invalid or still-streaming math remains visible as text. #101435

> macOS onboarding now translates local Gateway installation, checks, repairs, retries, paused setup, and resume guidance across the languages updated in this release. Sources: 7a717b7 , 85d31e1 , 27778a7 , cffc6ad , ab0d604 , 972d394 , edbbdf6 , 863a054 , ef5650f , 5f2e51f , 5769416 , a3aa917 , 2f7bd01 , c54a6f3 , 9c3ffc5 , 469e707 , d066a81 , 72a3b71 , 63aa909 , b68e2e7 .

> Android and iOS now explain which side needs an update when app and Gateway protocol versions differ and avoid offering reconnect attempts that cannot succeed. #98385 Related #98384 . Thanks @joshavant.

> iOS and Android users can create empty session groups, rename them once across their sessions, and remove a group without deleting the conversations inside it. #101234

> OpenClaw's mascot now uses the same float, blink, antenna, and claw animations across web, iOS, and Android surfaces while respecting reduced-motion preferences. 851156a

> iOS and Android can now show the Gateway terminal as a focused full-screen view with stored credentials and a clear unavailable state instead of embedding the full desktop Control UI. 9c78489

> Translated Gateway controls on iOS and approval actions on Apple Watch no longer fall back to English in supported locales. #97112 Thanks @vincentkoc.

> Native iOS Chat now follows Larger Text and Dynamic Type settings for messages, the intro, and composer text with less clipping. #97552 Thanks @jmcte.

> iPhone users pairing with a LAN Gateway now stay authenticated after the one-time bootstrap so Chat and the node connection do not immediately disconnect. #98066 Related #98064 . Thanks @ooiuuii.

> iOS Chat now keeps one final assistant reply per turn instead of briefly showing a duplicate that disappears after history refreshes. #98117 Related #98116 . Thanks @joshavant, @ooiuuii.

> Paired iOS users can start native ElevenLabs Talk with a SecretRef-backed Gateway key without copying the credential into plaintext mobile configuration. #98210 Related #98209 . Thanks @joshavant, @ooiuuii.

> After scanning an iOS pairing QR code, users now move to a live connection-progress screen instead of returning to Welcome while pairing continues invisibly. #98302 Related #98297 . Thanks @joelnishanth.

> iOS Chat now preserves intentional line breaks in assistant responses and other multiline messages without disrupting normal Markdown rendering. #98304 Related #98028 . Thanks @jabato01, @joshavant.

> The iOS app now opens to Chat for normal launches while preserving direct navigation to Control, Settings, Agent, Talk, and nested destinations. #98353 Thanks @bsniznd.

> iOS Control, Talk, and Settings are easier to scan with clearer status emphasis, safer action styling, calmer idle visuals, and improved large-text support. #98423 Related #98397 .

> iOS now explains secure Gateway connection and certificate-verification failures precisely and reliably presents the fingerprint trust prompt for first-time HTTPS connections. #98429 Thanks @joshavant.

> iOS connection, warning, and information text is now easier to read in light and dark modes, and Appearance settings accurately describe the selected behavior. #98443 Related #98440 .

> OpenAI Realtime Talk on iPhone now uses native WebRTC by default, recovers continuous sessions from provider disconnects, and respects speaker, Bluetooth, and AirPlay output choices. #98563 Thanks @pollybot13.

> New iPhone users now get clearer QR, setup-code, and manual Gateway choices, better nearby and connection status, and a direct handoff to Chat after connecting. #98868 Thanks @solvely-colin, @thats2easyyy.

> iOS users can correct gateway details after a failed manual setup and retry immediately with the values currently on screen. #99220 Related #99219 . Thanks @abdullahtas0.

> iPhone users who open Chat from a Control detail can now return to that same Overview, Activity, Workboard, or Sessions screen without losing their place. #99245 Thanks @solvely-colin.

> iOS users can now read OpenClaw's bundled third-party license acknowledgements from Settings > Licenses. #99290 Thanks @joshavant.

> iOS users can now add contacts and search affected records without crashing the app or disconnecting the node. #99475 Thanks @abdullahtas0.

> iOS gateway QR pairing now stays open through trust and approval, avoids scanner crashes, and keeps credentials and pending actions with the correct gateway during switches. #99572 Thanks @pollybot13.

> Apple chat now presents fenced code with theme-aware highlighting and GitHub-style tables as aligned native tables on iOS and macOS. #100207

> Repeated iOS Gateway setup links now update the visible settings screen with the newest connection instead of being consumed by a hidden view or replaying stale details. #100328

> iOS chat now provides tactile feedback for accepted sends and most completed or failed runs, though some abort paths may still omit or misclassify failure feedback. #100416

> iOS users can export the current conversation as a named, readable Markdown file and save or send it through the system share sheet. #100417

> Choosing While Using for location access on iOS now remains selected after approval and after the app is relaunched. #100512

> Talk and Settings rows on iOS now use consistent title sizing and typography, making adjacent options easier to scan. #100515

> The iOS About screen now presents OpenClaw branding, license information, and direct links to the website, documentation, GitHub repository, and Discord community. #100531

> Apple Watch pairing and companion status now refresh without restarting the iPhone app, while cold-launch actions wait for readiness or return a clear WATCH_UNAVAILABLE error. #100732

> iPhone users can now choose Listen on an assistant reply, follow preparation and playback status, stop at any time, and fall back to on-device speech when needed. #100771

> Display equations in iOS and macOS chats now appear as readable, accessible typeset math, with horizontal scrolling for wide formulas and raw text retained for malformed expressions. #100829

> Streaming replies in iOS and macOS chats now reveal text more smoothly word by word, while reduced-motion users still receive immediate text and completed messages remain unchanged. #100884

> Offline iOS messages now survive relaunch, remain tied to their original Gateway and conversation, and send once only when delivery can be confirmed, with clear uncertain-delivery status when it cannot. #100942

> iOS and macOS users can preview a safe link's title and description inside chat before deciding whether to open it. #101198

> Expanded link previews on iOS and macOS can now show a safe page thumbnail, with the existing text card retained when image loading fails. #101387

> Finished iOS and macOS chat replies now typeset inline LaTeX formulas while streaming text, code, currency, and invalid math remain readable as plain text. #101388

> The iOS screen.record command now finishes more reliably with a nonempty MP4 instead of crashing the app and disconnecting the node as recording stops. #101550 Thanks @tony-ooo.

> iOS pairing codes can now advertise both local and Tailnet Gateway routes, allowing the phone to save the first reachable address when it is away from the private LAN. #100317

> iOS chat and macOS webchat users can search, pin, rename, archive, restore, and reopen sessions from the in-chat switcher instead of scrolling a simple recent list. #101053

> macOS remote mode can now connect through explicitly selected managed SSH aliases and recover app-owned tunnels when SSH multiplexing or backgrounding is enabled. #99661

> Multiple macOS app instances now preserve shared SSH tunnel tracking and clean up stale processes more reliably, reducing port conflicts after a crash. #100601

> The macOS onboarding and About mascot now more closely matches openclaw.ai with theme-aware colors, glow, hover scaling, and smoother motion that keeps its antennae visible. 05c9dcc

> After a macOS crash or force quit, OpenClaw now reclaims confirmed orphaned remote-mode SSH tunnels so relaunches can reuse the preferred local Gateway port. #100489

> When Android Chat cannot reach the Gateway, users can open Gateway Settings or copy connection diagnostics directly from the blocked screen. #94566 Thanks @tosko4.

> Android manual Gateway setup now accepts IPv6 hosts such as ::1 directly instead of rejecting an address that works only when entered as a bracketed WebSocket URL. #99107 Thanks @ly85206559.

> Android manual setup now accepts and preserves complete ws:// , wss:// , and HTTP Gateway addresses, including embedded ports, so private-LAN onboarding reaches the intended server. #99110 Related #87216 . Thanks @cursoragent, @ly85206559, @ruben2000de.

> Android third-party onboarding now recognizes SMS access when send and read permissions are granted in separate prompts, while genuinely missing permissions remain unauthorized. #99147 Thanks @nianjiuzst.

> Android setup now rejects gateway URLs with unsupported IPv6 interface zones and directs users to an unscoped address or LAN hostname before saving. #99570 Thanks @ly85206559.

> Android now preserves specific Gateway and A2UI error codes containing numbers, such as A2UI_HOST_UNAVAILABLE , instead of replacing them with a generic failure. #99591 Thanks @ly85206559.

> Android Talk Mode now delivers agent-consult answers even when realtime completion events arrive out of order, preventing sessions from remaining stuck on Thinking... . #100049 Thanks @qingminglong.

> Android's Home overview now uses more consistent card, Talk, and recent-session spacing for a calmer, easier-to-tap first screen. #100059 Thanks @iwhatsskill.

> Android Gateway settings now show both setup actions as full-width buttons, keeping Pair New Gateway readable and easy to tap. #100090 Thanks @iwhatsskill.

> Tapping an Android notification created by system.notify now brings OpenClaw to the foreground. #100888

> Returning to an already loaded Android chat no longer flashes a loading screen, and the Overview recent-session list stays deduplicated and steadier during refreshes. #100966 Thanks @solvely-colin.

> Android Home's Recent Sessions section now keeps recently active rows in a stable order, collapses duplicates, and preserves labels and timestamps during partial live refreshes. #101161 Thanks @solvely-colin.

> Android physical-keyboard users can press or hold Enter to send once without leaving a stray newline, while Shift+Enter and in-progress input-method composition keep working. #101360 Thanks @3ninyt3nin-creator, @joshavant.

> The Android app now respects a user's disconnect, connect, or gateway-switch choice during startup and reports final disconnect failures to fire-and-forget callers. #101799

> iOS Gateway connection errors now appear as one dismissible toast that returns for a later failure and visibly reacts instead of stacking when the same problem repeats. #98856 Thanks @lokimorty.

> Equivalent rows in the iPhone Control and Settings tabs now use the same rounded icon treatment, making both lists easier to scan. #98936 Related #98916 . Thanks @sahilsatralkar.

> The iOS About screen now shows a concise app, device-family, and iOS summary without duplicated identity or a raw hardware identifier. #98985 Related #98943 . Thanks @sahilsatralkar.

> The iOS appearance setting now sits in the normal Settings list, shows the current System, Light, or Dark choice at a glance, and behaves consistently on iPad. #99052 Related #98995 . Thanks @sahilsatralkar.

> Cancelling or interrupting an iOS screen.record request now stops the system recorder instead of letting capture continue after the tool call fails. #99155 Thanks @nianjiuzst.

> iOS now recognizes Limited Photos access as usable, offers in-app controls for requesting or managing the grant, and avoids interrupting gateway requests with a surprise prompt. #99350 Related #99046 . Thanks @tony-ooo.

> Apple Watch quick replies now survive an unavailable iPhone and reconnect later to the intended Gateway without being lost, duplicated, or misrouted. #100372 Thanks @nianjiuzst.

> Tapping the iPhone status bar now leaves the chat at the top for reading older messages until the user chooses Jump to latest. #100502

> Already-paired iPhone users now return to Chat, Talk, and Settings instead of being trapped in setup when older onboarding flags are stale. #101481

> Android and iOS Gateway setup now clearly requires Secure TLS for remote hosts, warns before trusted LAN use without encryption, and offers actionable update guidance for protocol mismatches. #101325 Thanks @joshavant.

> Long-running system.run commands on the macOS app node no longer make the node appear offline or block unrelated Gateway traffic. #100842 Thanks @lvan185, @vincentkoc.

> The macOS app no longer mistakes a valid launchd-managed local Gateway for an unexpected listener and terminates active assistant or channel work. #100867 Thanks @lsr911, @vincentkoc.

> The macOS app now keeps the same paired device and node identity across upgrades, restarts, and Gateway reconnects instead of repeatedly asking for approval or creating stale duplicates. #101105 Thanks @yetval.

> Android users can sideload the official signed OpenClaw-Android.apk from a stable GitHub release and verify it with the published SHA-256 checksums. #101212

> Source and macOS package builds no longer fail when the tsdown configuration is loaded from a temporary directory that cannot resolve the runtime package. #100499

> Android node reconnects now point users from a failed devices approve attempt to the correct openclaw nodes approve &lt;requestId&gt; command, including a reminder to reuse connection flags. #98115 Thanks @welfo-beo.

> openclaw doctor on Windows now detects supported Chrome versions accurately instead of warning that a working installation could not be identified. #87937 Thanks @mukundakatta.

> Doctor lint can now flag the combination of WhatsApp, a strained Gateway event loop, and active local TUI sessions that is associated with delayed replies. #98406 Thanks @giodl73-repo.

> After openclaw doctor --fix archives a legacy sidecar, the macOS app no longer recreates it or triggers the same migration conflict warning on every command or Gateway start. #99039 Related #98917 . Thanks @momothemage, @p51moustache.

> Timed-out commands on Windows are less likely to leave child processes running when taskkill.exe cannot start. #101392 Thanks @aniruddhaadak80, @zengwen-dt.

> openclaw backup create on Windows now retries live-file archive races with fresh temporary paths, reducing locked partial backups and leftover retry archives. #101464 Thanks @lilan0125, @zoowh.

> A normal Doctor lint run no longer invokes crontab -l for the optional legacy WhatsApp check unless an operator explicitly selects it. #99250 Thanks @giodl73-repo.

> The macOS guide now gives users a clearer path from downloading the app through first-run setup, Gateway selection, and focused troubleshooting. #97120 Thanks @romneyda.

> OpenClaw's mobile documentation now identifies the iOS and Android apps as official releases and provides consistent App Store, Google Play, and hosted iOS push-relay guidance. #98843 Thanks @joshavant.

> Android node operators now have an end-to-end guide for securely mirroring and controlling a remote device from macOS, including authorization, troubleshooting, and clean disconnection. #100398

> Strengthened WhatsApp QA around messages, reactions, replies, media, polls, approvals, and group behavior. #95622 Thanks @mcaxtr.

> Prepared WhatsApp group activation settings for future storage changes while preserving existing activation behavior. #96530 Thanks @jalehman.

> Added translation coverage tracking for Android, iOS, and macOS interface text across supported locales. #97110 Thanks @vincentkoc.

> Clarified macOS release instructions so maintainers use the correct repositories and source revisions for each publishing step. #97116 Thanks @romneyda.

> Made macOS packaging logs easier to follow by clearly identifying each product and architecture being built. #97151 Thanks @romneyda.

> Reduced transient Windows, macOS, and iOS validation failures by retrying timed-out source checkouts. #97912 Thanks @romneyda.

> Made macOS Swift validation recover from incomplete build caches instead of repeating the same failure. #98818

> Expanded shared live-channel QA coverage for Telegram, Slack, WhatsApp, and Matrix while preserving each channel's existing behavior. #99707 Thanks @romneyda.

> Stabilized local macOS validation so maintainers can prepare releases and changes without host-specific false failures. #100069

> Added repeatable Android chat-streaming coverage for duplicate, missing, stale, timed-out, and malformed messages. #100200

> Strengthened mobile validation so new Gateway events cannot silently go unhandled by iOS or Android. #100206

> Let iOS developers keep debug and release apps installed side by side with distinct icons and separate app data. #100222

> Stabilized OpenClawKit contract and chat coverage under parallel macOS load, reducing false validation failures. #100243

> Cleaned up iOS and Apple Watch debug icons by removing an unintended white outer rim. #100259

> Strengthened mobile protocol validation so native iOS or Android changes cannot bypass Gateway event coverage. #100278

> Restored a clean Android formatting baseline so contributors can validate and extend recent mobile chat work. #100304

> Completed the release record for landed WhatsApp reconnect, quoted-reply, credential-recovery, and delivery-status fixes. #100346 Thanks @bartok9, @leonidaslux, @masatohoshino, @vishalj99.

> Stabilized load-sensitive Matrix, WhatsApp, and process coverage to reduce false failures on busy machines. #100420

> Simplified the iOS development app label while keeping debug and release installations easy to distinguish. #100466

> Removed an obsolete macOS onboarding test so the current native test target compiles cleanly. #100497 Thanks @steipete-oai.

> Recorded that persistent logins in new isolated macOS browser profiles survive graceful Browser and Gateway restarts. #100507 Thanks @turbotheturtle.

> Strengthened macOS browser proxy test reliability by removing intermittent failures that caused needless reruns. #100517

> Expanded the Android release record to include five previously shipped app improvements. #100702

> Removed obsolete internal code and legacy Android artifacts, leaving a smaller maintenance surface. #100823 Thanks @vincentkoc.

> Restored compilation of shared Apple platform tests used to validate iOS and macOS chat changes. #100903

> Prevented routine iOS package resolution from leaving unrelated local file changes behind. #100961

> Standardized Telegram and WhatsApp command and session checks across shared and live QA environments. #101080 Thanks @romneyda.

> Restored Android formatting and framework validation, reducing release-blocking maintenance noise. #101081 Thanks @vincentkoc.

> Made Android development commands find a standard local SDK automatically in fresh checkouts. #101273

> Added automatic Android formatting enforcement to prevent cleanup drift from reaching the main codebase. #101275

> Modernized Android build dependencies and validation while keeping the app's target behavior unchanged. #101356

> Stabilized Android saved-gateway reconnect coverage to reduce intermittent validation failures. #101519

> Removed superseded Android screens and translations, reducing maintenance work while leaving active app flows unchanged. #101680 Thanks @vincentkoc.

> Restored reliable Android translation validation after an obsolete app string was removed. #101689

Source: https://docs.openclaw.ai/releases/2026.7.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-07-13-5-projects-and-workspaces-changes-in-v2026-7-1|5 Projects and Workspaces changes in v2026.7.1]] · Projects and Workspaces
- [[Changes/OpenClaw/2026-07-13-99-developer-workflow-changes-in-v2026-7-1|99 Developer Workflow changes in v2026.7.1]] · Developer Workflow
- [[Changes/OpenClaw/2026-07-13-69-context-window-changes-in-v2026-7-1|69 Context Window changes in v2026.7.1]] · Context Window
- [[Changes/OpenClaw/2026-07-13-10-accessibility-and-localization-changes-in-v2026-7-1|10 Accessibility and Localization changes in v2026.7.1]] · Accessibility and Localization
- [[Changes/OpenClaw/2026-07-13-64-interface-experience-changes-in-v2026-7-1|64 Interface Experience changes in v2026.7.1]] · Interface Experience
- [[Changes/OpenClaw/2026-07-13-whatsapp-and-telegram-default-account-routing-warnings-are-now-available-through|WhatsApp and Telegram default-account routing warnings are now available through…]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-07-13-132-agent-mode-changes-in-v2026-7-1|132 Agent Mode changes in v2026.7.1]] · Agent Mode
- [[Changes/OpenClaw/2026-07-13-after-one-generated-video-clip-is-ready-a-different-next-clip-can-start-immediat|After one generated video clip is ready, a different next clip can start immediately…]] · Video Generation
- [[Changes/OpenClaw/2026-07-13-79-automation-and-scheduling-changes-in-v2026-7-1|79 Automation and Scheduling changes in v2026.7.1]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-07-13-130-model-support-changes-in-v2026-7-1|130 Model Support changes in v2026.7.1]] · Model Support
- [[Changes/OpenClaw/2026-07-13-69-account-and-access-changes-in-v2026-7-1|69 Account and Access changes in v2026.7.1]] · Account and Access
- [[Changes/OpenClaw/2026-07-13-59-safety-and-privacy-changes-in-v2026-7-1|59 Safety and Privacy changes in v2026.7.1]] · Safety and Privacy
- [[Changes/OpenClaw/2026-07-13-83-voice-and-audio-changes-in-v2026-7-1|83 Voice and Audio changes in v2026.7.1]] · Voice and Audio
- [[Changes/OpenClaw/2026-07-13-18-pricing-model-changes-in-v2026-7-1|18 Pricing Model changes in v2026.7.1]] · Pricing Model
- [[Changes/OpenClaw/2026-07-13-21-editor-experience-changes-in-v2026-7-1|21 Editor Experience changes in v2026.7.1]] · Editor Experience
- [[Changes/OpenClaw/2026-07-13-7-image-generation-changes-in-v2026-7-1|7 Image Generation changes in v2026.7.1]] · Image Generation
- [[Changes/OpenClaw/2026-07-13-channel-setup-warnings-are-now-available-as-structured-doctor-lint-findings-with|Channel setup warnings are now available as structured Doctor lint findings…]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-07-13-4-enterprise-and-administration-changes-in-v2026-7-1|4 Enterprise and Administration changes in v2026.7.1]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-07-13-2-presentation-creation-changes-in-v2026-7-1|2 Presentation Creation changes in v2026.7.1]] · Presentation Creation
- [[Changes/OpenClaw/2026-07-13-136-memory-and-personalization-changes-in-v2026-7-1|136 Memory and Personalization changes in v2026.7.1]] · Memory and Personalization
- [[Changes/OpenClaw/2026-07-13-213-apps-and-integrations-changes-in-v2026-7-1|213 Apps and Integrations changes in v2026.7.1]] · Apps and Integrations
- [[Changes/OpenClaw/2026-07-13-8-search-and-browsing-changes-in-v2026-7-1|8 Search and Browsing changes in v2026.7.1]] · Search and Browsing
- [[Changes/OpenClaw/2026-07-13-20-collaboration-changes-in-v2026-7-1|20 Collaboration changes in v2026.7.1]] · Collaboration
- [[Changes/OpenClaw/2026-07-13-13-files-and-data-changes-in-v2026-7-1|13 Files and Data changes in v2026.7.1]] · Files and Data
- [[Changes/OpenClaw/2026-07-13-19-multimodal-input-changes-in-v2026-7-1|19 Multimodal Input changes in v2026.7.1]] · Multimodal Input
- [[Changes/OpenClaw/2026-07-13-38-reliability-and-performance-changes-in-v2026-7-1|38 Reliability and Performance changes in v2026.7.1]] · Reliability and Performance
- [[Changes/OpenClaw/2026-07-13-686-other-changes-in-v2026-7-1|686 other changes in v2026.7.1]] · Other changes
- [[Changes/OpenClaw/2026-07-13-official-openclaw-container-images-are-now-available-from-docker-hub-as-well-as|Official OpenClaw container images are now available from Docker Hub as well…]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Mobile and Desktop

- Earlier: 2026-07-09 · OpenCode · [[Changes/OpenCode/2026-07-09-12-mobile-and-desktop-changes-in-v1-17-16|12 Mobile and Desktop changes in v1.17.16]]
- Later: 2026-07-13 · OpenCode · [[Changes/OpenCode/2026-07-13-9-mobile-and-desktop-changes-in-v1-17-20-1|9 Mobile and Desktop changes in v1.17.20 + 1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-14 · Cursor · [[Changes/Cursor/2023-03-14-windows-and-linux-support|Windows and Linux support 🥳]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-07-13-a77324&body=Card%3A%20Changes%2FOpenClaw%2F2026-07-13-224-mobile-and-desktop-changes-in-v2026-7-1.md%0ACard%20ID%3A%20openclaw-2026-07-13-a77324%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.7.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->