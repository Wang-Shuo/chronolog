---
card_id: openclaw-2026-07-13-482325
date: '2026-07-13'
description: 'OpenClaw · 2026-07-13 · Interface Experience: 64 changes in v2026.7.1
  — New Control UI chats now receive concise sidebar titles from their first message,
  and…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-stop-generating-based-on-your-feedback-we-ve-added-the-ability-to-stop-generatin|Stop
    generating: Based on your feedback, we''ve added the ability to stop generating…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1281
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: interface-experience
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 1250706357cc0a273022b8204bcedf73603227e2bd4e824de87017e4c1979217
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-07-13-482325
  comparison: ''
  date: '2026-07-13'
  description: 'OpenClaw — v2026.7.1: 64 Interface Experience changes'
  evidence:
  - quote: 'New Control UI chats now receive concise sidebar titles from their first
      message, and operators can route dashboard, Telegram topic, and Discord thread
      title generation through a smaller utilityModel . #87643 Thanks @juliangsm,
      @zhangguiping-xydt.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'The Control UI sidebar now focuses on sessions and a few default destinations
      while letting users pin their preferred pages and keep those choices across
      reloads. #100296'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: '/pair qr now delivers a scannable code in Telegram and Control UI or a
      readable code in the TUI without storing the one-time setup secret in chat history.
      #97933 Thanks @joshavant.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'The Control UI workspace rail now gives long Project files lists their
      own scrollbar so files remain browsable without spilling off screen. #98646
      Related #98566 . Thanks @645648406-max, @wuqxuan.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Control UI users can select and copy tool activity without toggling its
      row, and failed tools no longer repeat redundant error indicators. #100199 Thanks
      @steipete-oai.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'The Control UI sidebar now keeps all pinned chats visible alongside nine
      ordinary recent chats in a more compact, conversation-focused desktop and tablet
      layout. #100386'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'The Control UI sidebar now keeps recent chats in place while switching,
      combines search entry points, supports touch session actions, and reduces unnecessary
      chrome. #100648'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Images received through Telegram, iMessage, and other channels now reappear
      inline when users revisit Control UI chat history after a reload. #100725 Thanks
      @sweetcornna, @vergissberlin.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Switching Control UI chats no longer unexpectedly moves the selected session
      to the top, and users can choose stable creation order or recently updated order
      for the sidebar. #100927 Thanks @shakkernerd, @vyctorbrzezowski.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Control UI navigation now places branding, search, and sidebar controls
      where desktop and mobile users expect them, with clearer active sessions, compact
      timestamps, and easier terminal access. #101017 Thanks @shakkernerd, @vyctorbrzezowski.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'The Control UI sidebar collapse control now sits in the sidebar it affects
      instead of looking like an unrelated topbar or terminal button. #101038'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Sidebar session groups can now be renamed, removed without deleting sessions,
      created while empty, or disabled to restore one flat recent-session list. #101117'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'The Control UI now shows Workboard navigation only when Workboard is enabled
      and presents a cleaner collapsed sidebar with clearer icons and status spacing.
      #101123'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'The All Sessions sidebar label now uses the selected language across the
      supported Control UI translations in this release. Sources: b2c3dc2 , 61347a5
      , a2674b6 , bbabad4 , 8909289 , 22552d6 , 96e3615 , 452351c , 5e9a62c , 0a9648b
      , a803589 , 7c30ff8 , e3d2878 , 620f2e3 , aa0f36c , c336256 , 64dd688 , e2ecbc8
      .'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: The web sidebar now reliably fills pinned and overflow navigation routes,
      keeping destinations such as Worktrees available. 55a0012 Thanks @vincentkoc.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: The Control UI sidebar now builds cleanly with session grouping and drag-to-split
      behavior intact after stray merge-conflict text was removed. 0e3ce24
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'On phones and other short landscape screens, the Control UI composer now
      scrolls within a bounded area so chat history and all composing controls remain
      accessible. #98683 Related #98615 . Thanks @jin-li, @qingminglong.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Control UI chat history now hides only exact duplicate final delivery
      mirrors, leaving legitimate repeated sends, forwards, and distinct replies visible.
      #100136'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'OpenAI users now see only the supported Standard and Fast choices in the
      Control UI speed picker, with inherited Fast mode shown correctly. #100190'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Short drafts in the Control UI composer no longer show an unnecessary
      scrollbar gutter, while long drafts still scroll when needed. #100252'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'The expanded Control UI sidebar no longer repeats provider quota information
      already available in chat, Overview, and Usage views. #100356 Thanks @shakkernerd.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'New Control UI sessions now stay visible at the front of the sidebar after
      users switch to another chat, without requiring a page refresh. #100981 Thanks
      @shakkernerd.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Worktrees management now lives under Control UI Settings instead of occupying
      a top-level sidebar item, while existing deep links remain valid. #100995'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Finished chats no longer remain stuck with a busy spinner in the Control
      UI sidebar, even when an older Gateway update arrives afterward. #101293 Thanks
      @fuller-stack-dev.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Typing anywhere in the active Control UI chat now places the first character
      in the message composer without stealing input from the command palette. #102210
      Thanks @shakkernerd.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'The official iOS , Android , and macOS apps received substantial updates
      across setup, navigation, chat, voice, Apple Watch, permissions, localization,
      files, scheduled work, native session controls, and Gateway recovery. Recent
      conversations remain useful through temporary disconnects: cached sessions and
      transcripts stay available for reading, supported text sends can wait for reconnection
      in the correct chat, and long conversations are easier to resume without losing
      the current place or mistaking an offline view for live history.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'With channels.whatsapp.actions.calls , MeowCaller, and telephony TTS configured,
      a WhatsApp agent can now call the requester and speak a short task-completion
      or urgent message. #99635'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Discord''s recent-model buttons now shorten long names without breaking
      emoji or producing invalid picker payloads. #97600 Thanks @llagy007, @weeli-009.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Telegram onboarding now offers both the classic BotFather chat flow and
      the official web interface for creating a bot and copying its token into OpenClaw.
      #100540'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Repaired plain-text tool calls from LM Studio, xAI, and Ollama now emit
      a final completion event so plugins and other streaming consumers can finish
      them reliably. #104714'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'New or updated provider credentials entered through the CLI now appear
      in the running Gateway and Control UI model picker without a manual secrets
      reload or restart. #101256 Thanks @fuller-stack-dev.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Provider onboarding no longer writes an empty request block when no request
      overrides were supplied. 3a0a736 Thanks @vincentkoc.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Claude CLI chat history reloads no longer display OpenClaw''s internal
      reseed wrapper as if it were a message the user typed. #99653 Related #99646
      . Thanks @harjothkhara, @jeehut, @vincentkoc, @zoowh.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Subagent completion notices now arrive once instead of being repeated
      when the requesting session changes during delivery. #92274 Related #91527 .
      Thanks @fsdwen, @obviyus, @zackchiutw.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Successfully started subagents now remain visible in /subagents list and
      subagents(action="list") , including when different sessions own control and
      completion. #99410 Related #75593 . Thanks @aaajiao, @sheyanmin.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: A yielded Codex native subagent's completion now reaches its parent run
      before the shared app-server connection is cleaned up. 2f89de8 Thanks @vincentkoc.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Stopping a subagent now clears its running task reliably and prevents
      late completion races from reviving or overwriting the canceled state. #99806
      Thanks @masatohoshino, @timofa.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Parent sessions no longer repeat an earlier child-agent progress message
      when the child later reports completion. #101042 Thanks @mushuiyu886.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Operators now receive payload.large or truncated diagnostics and an accurate
      count whenever chat.history omits older messages, making hidden history trimming
      visible without changing client responses. #96788 Thanks @zengwen-dt.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Chat, Talk, Settings, navigation, and onboarding on iPhone and iPad now
      use more consistent native controls, appearance, and back behavior. #99231 Related
      #99195 . Thanks @marvkr.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Native app onboarding and AI connection guidance now reflects Crestodian
      and the current setup flow across supported non-English locales. Sources: ad4809f
      , f0ecc16 .'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'The Diffs viewer now provides a multi-file overview and direct file navigation,
      while PNG and PDF exports omit controls that cannot be used. #100753'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Native Gateway connection, diagnostics, permissions, onboarding, Chat,
      and Talk guidance now uses the selected language across the translations in
      this release. Sources: 3b27bb4 , e296d14 , 5516775 , 6ec4962 , 291f2a4 , 7e2d41b
      , 81bc96f , 574556c , 8bb44e6 , ae09908 , 42fc19d , 28bbb43 , 6ff9185 , 4be0be6
      , 0f1fbbe , d893a72 , f5cb29b .'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'On iPad, selecting Overview, Chat, Talk, or another sidebar destination
      now leaves the current Settings detail and opens the requested screen. #94991
      Thanks @solvely-colin.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: The Mac app now shows the animated OpenClaw mascot in onboarding and About,
      while Reduce Motion keeps it still. f052a2f
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Android''s thread picker now prioritizes real conversations, hides internal
      setup and device sessions, and still makes valid older chats available through
      All. #99557 Thanks @ly85206559.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Android''s command palette now keeps action and session rows visually
      aligned, with consistent icons, navigation spacing, and clean truncation for
      long labels. #101072 Thanks @iwhatsskill.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Opening OpenClaw again from the macOS Dock or Finder now brings up the
      dashboard or its failure window even when the menu-bar app is already running.
      #97637 Thanks @solvely-colin.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'The iPhone Control destination list is now denser and easier to scan without
      changing navigation or status information. #99468 Related #99439 . Thanks @sahilsatralkar.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: The supported installation and update paths preserve working state more
      carefully across packages, containers, and daemons. Onboarding and doctor retain
      choices through interrupted setup and migrations, surface actionable repair
      steps, and avoid silently continuing with stale services, missing plugins, or
      unusable model configuration.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'openclaw onboard now explains up front what setup covers, why full onboarding
      can take longer, and which optional steps can be postponed. #97482 Thanks @ly85206559.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Gateway status, Doctor, and onboarding diagnostics now read large logs
      within fixed bounds and surface recent useful failures instead of stale noise.
      #99407 Thanks @sunlit-deng.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'The CLI and full-screen TUI now open with a clear recovery message when
      their launch directory has been deleted instead of crashing before startup.
      #93636 Thanks @ml12580.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: The onboarding reference now gives accurate signal-cli, Gateway runtime,
      and channel allowlist guidance, including Windows limits and the IDs expected
      for direct messages. aaaa803
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Generated documentation navigation now preserves complete headings with
      command placeholders such as &lt;id&gt; and &lt;deviceId&gt; instead of hiding
      required arguments. #99099 Thanks @hxy91819.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'CDP-backed browser navigation to CSV, PDF, and other attachment URLs now
      returns a safely saved managed file with its URL and suggested filename. #89416
      Thanks @zhangguiping-xydt.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Browser uploads on re-rendering pages now recover more reliably and expose
      the real stale-reference or action error instead of a generic timeout. #101465
      Thanks @diwakarrankawat, @m13v, @tigicion.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Added a generated documentation map so contributors can locate relevant
      guides quickly and detect stale navigation. #95954 Thanks @glenn-agent.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Contributed to the fix that keeps long workspace file lists scrollable
      in the chat sidebar. #98611 Related #98566 . Thanks @645648406-max, @zw-xysk.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Made Control UI chat styling more predictable to update, with no intended
      visual change and less risk of regressions. #99900'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Restructured the Control UI for more predictable navigation, cleaner page
      transitions, and less unnecessary screen updating. #100024 Thanks @shakkernerd.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Simplified Control UI navigation maintenance while preserving saved sidebar
      choices and existing behavior. #100612'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Corrected QA smoke selection so routine runs could start instead of failing
      during setup. #101173 Thanks @romneyda.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Prepared chat history handling for future storage changes while preserving
      existing message and transcript behavior. #101688 Thanks @jalehman.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 64-interface-experience-changes-in-v2026-7-1
  source_release: openclaw-2026-07-13-v2026-7-1-c2063718
  source_type: openclaw_changelog
  theme: interface-experience
  title: 64 Interface Experience changes in v2026.7.1
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-07-10-4-interface-experience-changes-in-v1-0-70|4
  Interface Experience changes in v1.0.70]]'
- '[[Changes/Claude Code/2026-07-11-improved-agent-view-pasting-the-same-text-again-now-expands-the-collapsed-pasted|Improved
  agent view]]'
- '[[Changes/Google Antigravity/2026-07-13-added-support-for-attaching-and-rendering-plain-text-txt-files-in-conversations|Added
  support for attaching and rendering plain text (.txt) files in conversations…]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-07-13-v2026-7-1-c2063718|openclaw-2026-07-13-v2026-7-1-c2063718]]'
source_type: openclaw_changelog
theme: interface-experience
title: 64 Interface Experience changes in v2026.7.1
type: change
---

<!-- chronolog:begin region="header" -->
# 64 Interface Experience changes in v2026.7.1

**OpenClaw** · 2026-07-13 · [[Themes/interface-experience|Interface Experience]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.7.1) · from [[Releases/OpenClaw/openclaw-2026-07-13-v2026-7-1-c2063718|v2026.7.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> New Control UI chats now receive concise sidebar titles from their first message, and operators can route dashboard, Telegram topic, and Discord thread title generation through a smaller utilityModel . #87643 Thanks @juliangsm, @zhangguiping-xydt.

> The Control UI sidebar now focuses on sessions and a few default destinations while letting users pin their preferred pages and keep those choices across reloads. #100296

> /pair qr now delivers a scannable code in Telegram and Control UI or a readable code in the TUI without storing the one-time setup secret in chat history. #97933 Thanks @joshavant.

> The Control UI workspace rail now gives long Project files lists their own scrollbar so files remain browsable without spilling off screen. #98646 Related #98566 . Thanks @645648406-max, @wuqxuan.

> Control UI users can select and copy tool activity without toggling its row, and failed tools no longer repeat redundant error indicators. #100199 Thanks @steipete-oai.

> The Control UI sidebar now keeps all pinned chats visible alongside nine ordinary recent chats in a more compact, conversation-focused desktop and tablet layout. #100386

> The Control UI sidebar now keeps recent chats in place while switching, combines search entry points, supports touch session actions, and reduces unnecessary chrome. #100648

> Images received through Telegram, iMessage, and other channels now reappear inline when users revisit Control UI chat history after a reload. #100725 Thanks @sweetcornna, @vergissberlin.

> Switching Control UI chats no longer unexpectedly moves the selected session to the top, and users can choose stable creation order or recently updated order for the sidebar. #100927 Thanks @shakkernerd, @vyctorbrzezowski.

> Control UI navigation now places branding, search, and sidebar controls where desktop and mobile users expect them, with clearer active sessions, compact timestamps, and easier terminal access. #101017 Thanks @shakkernerd, @vyctorbrzezowski.

> The Control UI sidebar collapse control now sits in the sidebar it affects instead of looking like an unrelated topbar or terminal button. #101038

> Sidebar session groups can now be renamed, removed without deleting sessions, created while empty, or disabled to restore one flat recent-session list. #101117

> The Control UI now shows Workboard navigation only when Workboard is enabled and presents a cleaner collapsed sidebar with clearer icons and status spacing. #101123

> The All Sessions sidebar label now uses the selected language across the supported Control UI translations in this release. Sources: b2c3dc2 , 61347a5 , a2674b6 , bbabad4 , 8909289 , 22552d6 , 96e3615 , 452351c , 5e9a62c , 0a9648b , a803589 , 7c30ff8 , e3d2878 , 620f2e3 , aa0f36c , c336256 , 64dd688 , e2ecbc8 .

> The web sidebar now reliably fills pinned and overflow navigation routes, keeping destinations such as Worktrees available. 55a0012 Thanks @vincentkoc.

> The Control UI sidebar now builds cleanly with session grouping and drag-to-split behavior intact after stray merge-conflict text was removed. 0e3ce24

> On phones and other short landscape screens, the Control UI composer now scrolls within a bounded area so chat history and all composing controls remain accessible. #98683 Related #98615 . Thanks @jin-li, @qingminglong.

> Control UI chat history now hides only exact duplicate final delivery mirrors, leaving legitimate repeated sends, forwards, and distinct replies visible. #100136

> OpenAI users now see only the supported Standard and Fast choices in the Control UI speed picker, with inherited Fast mode shown correctly. #100190

> Short drafts in the Control UI composer no longer show an unnecessary scrollbar gutter, while long drafts still scroll when needed. #100252

> The expanded Control UI sidebar no longer repeats provider quota information already available in chat, Overview, and Usage views. #100356 Thanks @shakkernerd.

> New Control UI sessions now stay visible at the front of the sidebar after users switch to another chat, without requiring a page refresh. #100981 Thanks @shakkernerd.

> Worktrees management now lives under Control UI Settings instead of occupying a top-level sidebar item, while existing deep links remain valid. #100995

> Finished chats no longer remain stuck with a busy spinner in the Control UI sidebar, even when an older Gateway update arrives afterward. #101293 Thanks @fuller-stack-dev.

> Typing anywhere in the active Control UI chat now places the first character in the message composer without stealing input from the command palette. #102210 Thanks @shakkernerd.

> The official iOS , Android , and macOS apps received substantial updates across setup, navigation, chat, voice, Apple Watch, permissions, localization, files, scheduled work, native session controls, and Gateway recovery. Recent conversations remain useful through temporary disconnects: cached sessions and transcripts stay available for reading, supported text sends can wait for reconnection in the correct chat, and long conversations are easier to resume without losing the current place or mistaking an offline view for live history.

> With channels.whatsapp.actions.calls , MeowCaller, and telephony TTS configured, a WhatsApp agent can now call the requester and speak a short task-completion or urgent message. #99635

> Discord's recent-model buttons now shorten long names without breaking emoji or producing invalid picker payloads. #97600 Thanks @llagy007, @weeli-009.

> Telegram onboarding now offers both the classic BotFather chat flow and the official web interface for creating a bot and copying its token into OpenClaw. #100540

> Repaired plain-text tool calls from LM Studio, xAI, and Ollama now emit a final completion event so plugins and other streaming consumers can finish them reliably. #104714

> New or updated provider credentials entered through the CLI now appear in the running Gateway and Control UI model picker without a manual secrets reload or restart. #101256 Thanks @fuller-stack-dev.

> Provider onboarding no longer writes an empty request block when no request overrides were supplied. 3a0a736 Thanks @vincentkoc.

> Claude CLI chat history reloads no longer display OpenClaw's internal reseed wrapper as if it were a message the user typed. #99653 Related #99646 . Thanks @harjothkhara, @jeehut, @vincentkoc, @zoowh.

> Subagent completion notices now arrive once instead of being repeated when the requesting session changes during delivery. #92274 Related #91527 . Thanks @fsdwen, @obviyus, @zackchiutw.

> Successfully started subagents now remain visible in /subagents list and subagents(action="list") , including when different sessions own control and completion. #99410 Related #75593 . Thanks @aaajiao, @sheyanmin.

> A yielded Codex native subagent's completion now reaches its parent run before the shared app-server connection is cleaned up. 2f89de8 Thanks @vincentkoc.

> Stopping a subagent now clears its running task reliably and prevents late completion races from reviving or overwriting the canceled state. #99806 Thanks @masatohoshino, @timofa.

> Parent sessions no longer repeat an earlier child-agent progress message when the child later reports completion. #101042 Thanks @mushuiyu886.

> Operators now receive payload.large or truncated diagnostics and an accurate count whenever chat.history omits older messages, making hidden history trimming visible without changing client responses. #96788 Thanks @zengwen-dt.

> Chat, Talk, Settings, navigation, and onboarding on iPhone and iPad now use more consistent native controls, appearance, and back behavior. #99231 Related #99195 . Thanks @marvkr.

> Native app onboarding and AI connection guidance now reflects Crestodian and the current setup flow across supported non-English locales. Sources: ad4809f , f0ecc16 .

> The Diffs viewer now provides a multi-file overview and direct file navigation, while PNG and PDF exports omit controls that cannot be used. #100753

> Native Gateway connection, diagnostics, permissions, onboarding, Chat, and Talk guidance now uses the selected language across the translations in this release. Sources: 3b27bb4 , e296d14 , 5516775 , 6ec4962 , 291f2a4 , 7e2d41b , 81bc96f , 574556c , 8bb44e6 , ae09908 , 42fc19d , 28bbb43 , 6ff9185 , 4be0be6 , 0f1fbbe , d893a72 , f5cb29b .

> On iPad, selecting Overview, Chat, Talk, or another sidebar destination now leaves the current Settings detail and opens the requested screen. #94991 Thanks @solvely-colin.

> The Mac app now shows the animated OpenClaw mascot in onboarding and About, while Reduce Motion keeps it still. f052a2f

> Android's thread picker now prioritizes real conversations, hides internal setup and device sessions, and still makes valid older chats available through All. #99557 Thanks @ly85206559.

> Android's command palette now keeps action and session rows visually aligned, with consistent icons, navigation spacing, and clean truncation for long labels. #101072 Thanks @iwhatsskill.

> Opening OpenClaw again from the macOS Dock or Finder now brings up the dashboard or its failure window even when the menu-bar app is already running. #97637 Thanks @solvely-colin.

> The iPhone Control destination list is now denser and easier to scan without changing navigation or status information. #99468 Related #99439 . Thanks @sahilsatralkar.

> The supported installation and update paths preserve working state more carefully across packages, containers, and daemons. Onboarding and doctor retain choices through interrupted setup and migrations, surface actionable repair steps, and avoid silently continuing with stale services, missing plugins, or unusable model configuration.

> openclaw onboard now explains up front what setup covers, why full onboarding can take longer, and which optional steps can be postponed. #97482 Thanks @ly85206559.

> Gateway status, Doctor, and onboarding diagnostics now read large logs within fixed bounds and surface recent useful failures instead of stale noise. #99407 Thanks @sunlit-deng.

> The CLI and full-screen TUI now open with a clear recovery message when their launch directory has been deleted instead of crashing before startup. #93636 Thanks @ml12580.

> The onboarding reference now gives accurate signal-cli, Gateway runtime, and channel allowlist guidance, including Windows limits and the IDs expected for direct messages. aaaa803

> Generated documentation navigation now preserves complete headings with command placeholders such as &lt;id&gt; and &lt;deviceId&gt; instead of hiding required arguments. #99099 Thanks @hxy91819.

> CDP-backed browser navigation to CSV, PDF, and other attachment URLs now returns a safely saved managed file with its URL and suggested filename. #89416 Thanks @zhangguiping-xydt.

> Browser uploads on re-rendering pages now recover more reliably and expose the real stale-reference or action error instead of a generic timeout. #101465 Thanks @diwakarrankawat, @m13v, @tigicion.

> Added a generated documentation map so contributors can locate relevant guides quickly and detect stale navigation. #95954 Thanks @glenn-agent.

> Contributed to the fix that keeps long workspace file lists scrollable in the chat sidebar. #98611 Related #98566 . Thanks @645648406-max, @zw-xysk.

> Made Control UI chat styling more predictable to update, with no intended visual change and less risk of regressions. #99900

> Restructured the Control UI for more predictable navigation, cleaner page transitions, and less unnecessary screen updating. #100024 Thanks @shakkernerd.

> Simplified Control UI navigation maintenance while preserving saved sidebar choices and existing behavior. #100612

> Corrected QA smoke selection so routine runs could start instead of failing during setup. #101173 Thanks @romneyda.

> Prepared chat history handling for future storage changes while preserving existing message and transcript behavior. #101688 Thanks @jalehman.

Source: https://docs.openclaw.ai/releases/2026.7.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-07-13-5-projects-and-workspaces-changes-in-v2026-7-1|5 Projects and Workspaces changes in v2026.7.1]] · Projects and Workspaces
- [[Changes/OpenClaw/2026-07-13-99-developer-workflow-changes-in-v2026-7-1|99 Developer Workflow changes in v2026.7.1]] · Developer Workflow
- [[Changes/OpenClaw/2026-07-13-69-context-window-changes-in-v2026-7-1|69 Context Window changes in v2026.7.1]] · Context Window
- [[Changes/OpenClaw/2026-07-13-10-accessibility-and-localization-changes-in-v2026-7-1|10 Accessibility and Localization changes in v2026.7.1]] · Accessibility and Localization
- [[Changes/OpenClaw/2026-07-13-whatsapp-and-telegram-default-account-routing-warnings-are-now-available-through|WhatsApp and Telegram default-account routing warnings are now available through…]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-07-13-132-agent-mode-changes-in-v2026-7-1|132 Agent Mode changes in v2026.7.1]] · Agent Mode
- [[Changes/OpenClaw/2026-07-13-after-one-generated-video-clip-is-ready-a-different-next-clip-can-start-immediat|After one generated video clip is ready, a different next clip can start immediately…]] · Video Generation
- [[Changes/OpenClaw/2026-07-13-79-automation-and-scheduling-changes-in-v2026-7-1|79 Automation and Scheduling changes in v2026.7.1]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-07-13-130-model-support-changes-in-v2026-7-1|130 Model Support changes in v2026.7.1]] · Model Support
- [[Changes/OpenClaw/2026-07-13-69-account-and-access-changes-in-v2026-7-1|69 Account and Access changes in v2026.7.1]] · Account and Access
- [[Changes/OpenClaw/2026-07-13-59-safety-and-privacy-changes-in-v2026-7-1|59 Safety and Privacy changes in v2026.7.1]] · Safety and Privacy
- [[Changes/OpenClaw/2026-07-13-224-mobile-and-desktop-changes-in-v2026-7-1|224 Mobile and Desktop changes in v2026.7.1]] · Mobile and Desktop
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
## Nearby in Interface Experience

- Earlier: 2026-07-13 · Google Antigravity · [[Changes/Google Antigravity/2026-07-13-added-support-for-attaching-and-rendering-plain-text-txt-files-in-conversations|Added support for attaching and rendering plain text (.txt) files in conversations…]]
- Later: 2026-07-14 · Claude Code · [[Changes/Claude Code/2026-07-14-added-mouse-click-support-for-multi-select-menus-and-other-input-rows-in-fullscr|Added mouse-click support for multi-select menus and "Other" input rows in fullscreen mode]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-stop-generating-based-on-your-feedback-we-ve-added-the-ability-to-stop-generatin|Stop generating: Based on your feedback, we've added the ability to stop generating…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-07-13-482325&body=Card%3A%20Changes%2FOpenClaw%2F2026-07-13-64-interface-experience-changes-in-v2026-7-1.md%0ACard%20ID%3A%20openclaw-2026-07-13-482325%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.7.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->