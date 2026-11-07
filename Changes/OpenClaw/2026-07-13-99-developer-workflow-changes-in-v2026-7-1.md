---
card_id: openclaw-2026-07-13-1a1ae3
date: '2026-07-13'
description: 'OpenClaw · 2026-07-13 · Developer Workflow: 99 changes in v2026.7.1
  — Hovering or keyboard-focusing a public GitHub issue or pull request in Control
  UI chat…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1213
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: c622a488a4e9df7568b02a8b9aea56704a83c241cc6832a468c6be8dc297ca77
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-07-13-1a1ae3
  comparison: ''
  date: '2026-07-13'
  description: 'OpenClaw — v2026.7.1: 99 Developer Workflow changes'
  evidence:
  - quote: 'Hovering or keyboard-focusing a public GitHub issue or pull request in
      Control UI chat now previews its status, title, author, activity, comments,
      and change size without leaving the conversation. #100434'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Control UI sessions using full verbose output now open tool inputs and
      results by default, reducing repeated clicks during debugging and review. #74398
      Thanks @samrusani.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Control UI and WebChat no longer let a non-terminal internal tool failure
      dominate the transcript with a red error banner after the assistant has already
      produced a normal final answer. #90122 Thanks @harjothkhara.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Control UI build errors now keep emoji and other supplementary characters
      intact when command output is shortened for display. #101591 Thanks @maweibin.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'The CLI now guides fresh installs through setup, opens configured installs
      directly in the TUI, preserves existing choices on reruns, and finishes onboarding
      in a usable terminal chat. #98218 Thanks @fuller-stack-dev.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Control UI admins can now keep chat, session controls, and live shells
      together by opening multiple dockable, resizable terminal tabs inside the browser
      workspace. ec72de4
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: iOS users can open Terminal directly from the Control hub, see a Gateway
      setup prompt when disconnected, and keep active shell sessions running through
      unrelated screen updates. 211e0d7
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Opt-in Control UI terminal sessions can now survive page reloads, sleep,
      and brief network drops, letting operators reattach and replay recent output
      instead of losing running commands. #100089'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Opening a new Control UI terminal after closing the final tab now starts
      with a blank fresh shell instead of restoring the closed terminal output. #100665'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Control UI terminal tabs now close cleanly while opening, follow theme
      changes, and reopen at a usable size instead of leaving hidden sessions, stale
      colors, or unreachable controls. 2399ce7
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: An already-open Control UI page now notices when terminal support is enabled
      and makes the terminal available without requiring a manual refresh. 3f976f9
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Opening a new Control UI terminal tab after closing another no longer inherits
      an old exited state. 3c03389
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: The Control UI terminal no longer crashes when its web component is loaded
      more than once in a shared browser registry. f2e5159
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'The Control UI integrated terminal now shows one cursor instead of overlapping
      Chrome and terminal carets, making focus and typing state clearer. #100240'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'The Control UI terminal''s new-session button now aligns with the surrounding
      tabs for a cleaner, easier-to-scan tab bar. #100256'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Telegram users still receive a plain-text reply when rich formatting for
      an email, URL, mention, hashtag, command, phone number, bank card, or similar
      entity is rejected, instead of the bot going silent. #96642 Thanks @moguangyu5-design.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Skill command descriptions now remain fuller where supported and stay
      valid in Discord and Mattermost when emoji appears near a platform limit. #99593
      Thanks @pick-cat.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Matrix dependency setup now stops its child process predictably and reports
      the failure when a local command''s output pipe breaks. #101597 Thanks @alix-007.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: A Telegram reply that has already started is no longer unexpectedly cancelled
      when another authorized command arrives. 52a3314 Thanks @vincentkoc.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Claude Code 2.1 users can again approve and run Bash, WebFetch, Grep,
      Glob, AskUserQuestion, and other native tools in claude-cli sessions. #98665
      Related #95171 . Thanks @carterdawson, @yetval.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Scheduled and CLI Codex runs with an explicit timeout longer than 30 minutes
      can now use that full budget instead of being stopped by the terminal-idle guard.
      #85296 Thanks @alkor2000, @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Long, tool-heavy agent sessions now preserve the newest command, file,
      or browser result for the model while shortening older history first. #99756
      Thanks @acosx.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: A first command-only interaction in an auto-reply flow now keeps its session
      update even when no session row existed beforehand. 76d686c
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Debug-proxy ACP runs now shut down cleanly, mark capture sessions finished,
      and close their capture databases without reporting a spurious database error.
      #100827 Thanks @amknight.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Interactive chat requests that end in a terminal failure now receive one
      visible error response instead of appearing to be ignored. #99304 Thanks @grox2012,
      @moeedahmed.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Shell snapshot capture and validation no longer crash OpenClaw when an
      unused helper-process output pipe reports a stream error. #100744 Thanks @lsr911,
      @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Long status messages and command output now stay readable when shortened,
      without splitting emoji or non-English characters into corrupted text. 2e7ffca
      Thanks @vincentkoc.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Developers can build against and consume managed-worktree session results
      from the Gateway protocol package without duplicate-name failures. 8ce620f Thanks
      @vincentkoc.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Gateway logs now reveal when OpenClaw cannot save a terminal session''s
      final lifecycle state, making silent persistence failures diagnosable. #97839
      Related #97795 . Thanks @aniruddhaadak80, @lzy3538.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Bare Fireworks API keys are now masked in logs, provider errors, command
      details, tool output, and Control UI diagnostics even without a nearby sensitive-field
      label. #98226 Related #98225 . Thanks @ooiuuii.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Auto-reply diagnostics now remain owner-only instead of allowing non-owner
      participants to run the command. 170bf72 Thanks @joshavant.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Terminal requests with an unknown agent ID now fail clearly instead of
      falling back to global defaults and potentially opening a host shell outside
      the intended agent boundary. 3601dca
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Managed deployments can now require entries such as system.run in gateway.nodes.denyCommands
      , and Policy doctor warns when configuration drift leaves a privileged node
      command available. #99121 Thanks @giodl73-repo.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Managed host tools no longer inherit the active Conda environment from
      the shell that launched OpenClaw, avoiding unintended Python and package-manager
      behavior. #99425 Related #99424 . Thanks @krissding, @ooiuuii.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Exec approval prompts now display and transmit long command text containing
      emoji or malformed Unicode without broken characters or encoding failures. #99566
      Thanks @mikasa0818.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'The Control UI terminal is now explicit opt-in, opens tabs under the selected
      agent''s workspace and policy, and closes affected shells when accepted access
      restrictions tighten. #100081 Thanks @rayncc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Always-allow approvals for npm exec , npx , pnpm , and yarn wrappers now
      apply to the actual command rather than unintentionally trusting different future
      payloads. #102035 Thanks @pgondhi987.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Copied provider keys and tokens now have hidden terminal control characters
      removed before request headers are prepared, while intentional spaces remain
      intact. #96444 Thanks @lin-hongkuan.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Trajectory exports from chat now require owner authority, preventing other
      command-authorized channel users from retrieving sensitive session artifacts.
      #97840 Thanks @pgondhi987.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Hidden control characters can no longer break terminal hyperlink boundaries
      or inject control behavior through documentation link text. #96440 Thanks @lin-hongkuan.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Long Codex app-server approval details and command previews now preserve
      emoji and extended Unicode characters instead of showing corrupted text. #100177
      Thanks @xialonglee.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Terminal conversations remain open with useful errors, session lists preserve
      readable previews, and Diffs actions stay attached to the comparison currently
      on screen.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: New-chat and worktree-chat entry points now appear in the selected language
      across supported Android and Apple app locales. 24bca38
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Supported non-English native apps now cover more Gateway setup, session,
      provider, health, messaging, terminal, and device text without English gaps.
      52f1e05
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Native app command search now translates loading, unavailable, retry,
      and no-result states across the languages updated in this release. Sources:
      745d2d0 , 7f7bec7 , 35be1c8 , 7db67ab , 4bc5766 , 0672720 , 2a8cd44 , fd648fb
      , 00b0b40 , a67990a , 7640f67 , 15f4819 , 4d1d720 , d1d3a27 , c2737d5 , bd3263d
      , 127ce63 , 0c960cd , e6c3ad9 , 84c86f7 , e7aea60 .'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Supported non-English native apps now translate the new Terminal destination,
      Gateway setup guidance, Back action, connection messages, and OpenClaw branding.
      e069cb2
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Shortened exec and bash summaries now keep emoji and other supplementary
      characters intact around the ellipsis instead of displaying a broken replacement
      glyph. #96963 Thanks @bartok9, @ly-wang19, @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Replies triggered through Telegram or another external channel now appear
      only once in the terminal UI after history refreshes, while resets, session
      switches, delayed events, and in-progress recovery continue normally. #96980
      Thanks @xialonglee.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'The TUI now directs users to the pending device or scope-upgrade approval
      command instead of incorrectly sending them through chat-DM pairing. #98144
      Thanks @romneyda.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Embedded and local TUI sessions now contain event-consumer errors instead
      of terminating the terminal. #100117 Thanks @cxbasdev.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: The iOS and Android terminal pages now receive the operator credential
      from the connected device session, so authenticated users do not land on a terminal
      that cannot connect. 451190d Thanks @vincentkoc.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Android''s "New chat in worktree" action is now translated across supported
      non-English locales instead of appearing with a missing resource. #100805 Thanks
      @amknight.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Terminal Hatch onboarding and other TUI connections now show starting
      up until session loading finishes, with accurate running indicators after reconnects.
      #93999 Thanks @ml12580.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Workspace skill approvals started in the TUI now appear in that terminal,
      so users can review and unblock the run without switching to Telegram. #100251
      Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'The terminal UI now stays open and shows a safe, useful error when a local
      shell command, slash command, or message submission fails. #100340 Thanks @cxbasdev.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Windows command lookup now honors the caller''s PATHEXT , allowing valid
      PowerShell scripts and executables to resolve in containers, CI, and isolated
      environments. #98093 Thanks @wendy-chsy.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'openclaw doctor now gives a missing-transcript preview command that actually
      shows the entries eligible for removal before users choose to enforce cleanup.
      #83630 Thanks @yuanhanzhong.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'An invalid openclaw nodes approve &lt;requestId&gt; now shows available
      pending IDs and the openclaw nodes pending recovery command instead of a raw
      client error. #94452 Thanks @mushuiyu886.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Control UI, pairing, setup-code, QR, and status links now prefer a reachable
      LAN address on hosts with VPNs, virtual adapters, WSL, Hyper-V, or multiple
      networks. #98482 Thanks @joshavant.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Crestodian setup and repair chats no longer destabilize the local TUI
      when a terminal event consumer fails during response delivery. #100341 Thanks
      @cxbasdev, @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Browser CLI commands now accept --browser-profile before or after the
      subcommand, restoring existing remote-browser and WSL2 command patterns. #94431
      Thanks @ml12580.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Failed openclaw --help and openclaw --version startup now returns exit
      code 1 promptly instead of leaving the terminal process stuck. #97807 Thanks
      @aniruddhaadak80, @maweibin.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'openclaw --help now matches command-specific help and completions, with
      config patch and config schema visible from the main command list. #100670 Thanks
      @amirf194, @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Terminal-rendered links containing balanced parentheses now remain clickable
      through the complete intended URL instead of being shortened or misdirected.
      #100697 Thanks @aniruddhaadak80, @zoowh.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Windows Gateway restarts no longer depend on the findstr check that could
      leave a visible or hung command window blocking the handoff. #101366 Thanks
      @deepujain.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Git installs now create an openclaw launcher that keeps using the intended
      Node.js runtime even after the user's PATH changes. be7198f
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Terminal and setup documentation links now resolve correctly when relative
      paths begin with http or absolute HTTP schemes use uppercase letters. #96439
      Thanks @lin-hongkuan.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Terminal notes, Doctor output, and diagnostics now wrap long runs of CJK,
      full-width, or emoji characters within the requested width instead of spilling
      across columns. #96746 Thanks @ly-wang19.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Pending exec approval cards now describe only the approval state, and
      the foreground-fallback warning appears only after a command actually runs that
      way. #101561 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Official operating guidance now matches shipped commands, configuration,
      setup, status output, placeholders, and recovery behavior more closely. Generated
      documentation maps also preserve literal command parameters, reducing the chance
      that a reader follows an example whose identifiers were stripped or whose workflow
      no longer matches the product.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Users can now start a chat in its own managed worktree from the Control
      UI or mobile app, isolating parallel coding while preserving dirty work and
      cleaning safe idle checkouts automatically. #100788'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Exec and finished background-session results now include signals, timeout
      flags, failure kinds, and exit reasons so users can tell why a command stopped.
      #89104 Thanks @yu-xin-c.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Crestodian setup and local-tool checks no longer terminate OpenClaw when
      a probed command encounters a rare output-stream read failure. #100741 Thanks
      @lsr911.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Agents can now screenshot a selected background Chromium tab without waiting
      for the browser command to time out, though capture may bring that tab forward.
      #100857 Thanks @spencer2211.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Terminal task lists now shorten emoji-heavy summaries without leaving
      broken replacement characters in the row. #101600 Thanks @maweibin.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Progress summaries for inline scripts and generated files no longer present
      heredoc content as extra shell commands that ran. #99379 Thanks @zengwen-dt.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Added regression coverage so code identifiers with underscores remain
      readable in the terminal interface. #95211 Thanks @zhangguiping-xydt.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Prevented pre-commit formatting from unexpectedly rewriting files during
      merges, rebases, cherry-picks, and reverts. #95842 Thanks @nxmxbbd, @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Made pull-request smoke testing faster and more predictable while retaining
      broader release coverage. #96320 Thanks @romneyda.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Improved cleanup across command tests, reducing leftover temporary data
      in local and automated runs. #96359 Thanks @xialonglee.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Strengthened coverage for verbose command-line logging to reduce future
      regressions. #96735 Thanks @dwc1997, @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Added coverage for terminal output and non-exiting command behavior, improving
      maintainability without changing the interface. #96736 Thanks @dwc1997.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Added regression coverage for numeric command-line and configuration options,
      including defaults and boundary values. #97802 Thanks @dwc1997.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Made maintainer bug sweeps support requested batch sizes and specific
      pull request lists while preserving existing readiness standards. #98494 Thanks
      @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Restored documentation and test type checks without changing the attach
      command''s behavior. #98792'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Reduced false QA failures by giving native stop-command recovery the full
      expected turn time. #99656 Related #99655 . Thanks @romneyda.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Consolidated internal text cleanup while preserving terminal formatting
      and outbound-message safety. #99718 Thanks @romneyda.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Reduced false validation timeouts for native command session targeting
      under busy conditions. #99743 Thanks @romneyda.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Corrected command output shortening so zero or invalid length limits no
      longer produce text beyond the requested size. #99917 Thanks @super-cabbage.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Sped up update-command coverage while retaining validation of managed-service
      restart failures. #99945'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Reduced interruptions during bounded maintainer cleanup by allowing larger
      approved batches of stale pull requests. #100253'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Prevented pull-request landing validation from exhausting shared service
      limits while preserving trustworthy results. #100332'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Documented the shipped Control UI previews that reveal useful GitHub issue
      and pull request details. #100555'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Reduced unnecessary repeat validation when concurrent pull requests land
      without changing the prepared patch. #100593'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Completed changelog coverage for five shipped Control UI and terminal
      interface fixes. #100599 Thanks @goutamadwant, @haishmg, @ml12580, @ruanrrn,
      @vincentkoc, @zengwen-dt.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Completed developer support and validation for integrations using managed-worktree
      session results. #100793'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Made managed-worktree session results available through the supported
      developer interface. #100804'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Kept the local debug proxy available and its errors honest when an upstream
      server ends a response early. #101315 Thanks @sebtardif.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Narrowed internal terminal interfaces in the gateway while preserving
      existing terminal behavior. #101941 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 99-developer-workflow-changes-in-v2026-7-1
  source_release: openclaw-2026-07-13-v2026-7-1-c2063718
  source_type: openclaw_changelog
  theme: developer-workflow
  title: 99 Developer Workflow changes in v2026.7.1
  type: change
related_changes:
- '[[Changes/Claude Code/2026-07-10-4-developer-workflow-changes-in-v2-1-206|4 Developer
  Workflow changes in v2.1.206]]'
- '[[Changes/GitHub Copilot CLI/2026-07-10-3-developer-workflow-changes-in-v1-0-70|3
  Developer Workflow changes in v1.0.70]]'
- '[[Changes/Codex CLI/2026-07-13-published-a-version-only-release-with-no-merged-pull-request-changes-since-rust|Published
  a version-only release with no merged pull request changes since rust-v0.144.2]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-07-13-v2026-7-1-c2063718|openclaw-2026-07-13-v2026-7-1-c2063718]]'
source_type: openclaw_changelog
theme: developer-workflow
title: 99 Developer Workflow changes in v2026.7.1
type: change
---

<!-- chronolog:begin region="header" -->
# 99 Developer Workflow changes in v2026.7.1

**OpenClaw** · 2026-07-13 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.7.1) · from [[Releases/OpenClaw/openclaw-2026-07-13-v2026-7-1-c2063718|v2026.7.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Hovering or keyboard-focusing a public GitHub issue or pull request in Control UI chat now previews its status, title, author, activity, comments, and change size without leaving the conversation. #100434

> Control UI sessions using full verbose output now open tool inputs and results by default, reducing repeated clicks during debugging and review. #74398 Thanks @samrusani.

> Control UI and WebChat no longer let a non-terminal internal tool failure dominate the transcript with a red error banner after the assistant has already produced a normal final answer. #90122 Thanks @harjothkhara.

> Control UI build errors now keep emoji and other supplementary characters intact when command output is shortened for display. #101591 Thanks @maweibin.

> The CLI now guides fresh installs through setup, opens configured installs directly in the TUI, preserves existing choices on reruns, and finishes onboarding in a usable terminal chat. #98218 Thanks @fuller-stack-dev.

> Control UI admins can now keep chat, session controls, and live shells together by opening multiple dockable, resizable terminal tabs inside the browser workspace. ec72de4

> iOS users can open Terminal directly from the Control hub, see a Gateway setup prompt when disconnected, and keep active shell sessions running through unrelated screen updates. 211e0d7

> Opt-in Control UI terminal sessions can now survive page reloads, sleep, and brief network drops, letting operators reattach and replay recent output instead of losing running commands. #100089

> Opening a new Control UI terminal after closing the final tab now starts with a blank fresh shell instead of restoring the closed terminal output. #100665

> Control UI terminal tabs now close cleanly while opening, follow theme changes, and reopen at a usable size instead of leaving hidden sessions, stale colors, or unreachable controls. 2399ce7

> An already-open Control UI page now notices when terminal support is enabled and makes the terminal available without requiring a manual refresh. 3f976f9

> Opening a new Control UI terminal tab after closing another no longer inherits an old exited state. 3c03389

> The Control UI terminal no longer crashes when its web component is loaded more than once in a shared browser registry. f2e5159

> The Control UI integrated terminal now shows one cursor instead of overlapping Chrome and terminal carets, making focus and typing state clearer. #100240

> The Control UI terminal's new-session button now aligns with the surrounding tabs for a cleaner, easier-to-scan tab bar. #100256

> Telegram users still receive a plain-text reply when rich formatting for an email, URL, mention, hashtag, command, phone number, bank card, or similar entity is rejected, instead of the bot going silent. #96642 Thanks @moguangyu5-design.

> Skill command descriptions now remain fuller where supported and stay valid in Discord and Mattermost when emoji appears near a platform limit. #99593 Thanks @pick-cat.

> Matrix dependency setup now stops its child process predictably and reports the failure when a local command's output pipe breaks. #101597 Thanks @alix-007.

> A Telegram reply that has already started is no longer unexpectedly cancelled when another authorized command arrives. 52a3314 Thanks @vincentkoc.

> Claude Code 2.1 users can again approve and run Bash, WebFetch, Grep, Glob, AskUserQuestion, and other native tools in claude-cli sessions. #98665 Related #95171 . Thanks @carterdawson, @yetval.

> Scheduled and CLI Codex runs with an explicit timeout longer than 30 minutes can now use that full budget instead of being stopped by the terminal-idle guard. #85296 Thanks @alkor2000, @vincentkoc.

> Long, tool-heavy agent sessions now preserve the newest command, file, or browser result for the model while shortening older history first. #99756 Thanks @acosx.

> A first command-only interaction in an auto-reply flow now keeps its session update even when no session row existed beforehand. 76d686c

> Debug-proxy ACP runs now shut down cleanly, mark capture sessions finished, and close their capture databases without reporting a spurious database error. #100827 Thanks @amknight.

> Interactive chat requests that end in a terminal failure now receive one visible error response instead of appearing to be ignored. #99304 Thanks @grox2012, @moeedahmed.

> Shell snapshot capture and validation no longer crash OpenClaw when an unused helper-process output pipe reports a stream error. #100744 Thanks @lsr911, @vincentkoc.

> Long status messages and command output now stay readable when shortened, without splitting emoji or non-English characters into corrupted text. 2e7ffca Thanks @vincentkoc.

> Developers can build against and consume managed-worktree session results from the Gateway protocol package without duplicate-name failures. 8ce620f Thanks @vincentkoc.

> Gateway logs now reveal when OpenClaw cannot save a terminal session's final lifecycle state, making silent persistence failures diagnosable. #97839 Related #97795 . Thanks @aniruddhaadak80, @lzy3538.

> Bare Fireworks API keys are now masked in logs, provider errors, command details, tool output, and Control UI diagnostics even without a nearby sensitive-field label. #98226 Related #98225 . Thanks @ooiuuii.

> Auto-reply diagnostics now remain owner-only instead of allowing non-owner participants to run the command. 170bf72 Thanks @joshavant.

> Terminal requests with an unknown agent ID now fail clearly instead of falling back to global defaults and potentially opening a host shell outside the intended agent boundary. 3601dca

> Managed deployments can now require entries such as system.run in gateway.nodes.denyCommands , and Policy doctor warns when configuration drift leaves a privileged node command available. #99121 Thanks @giodl73-repo.

> Managed host tools no longer inherit the active Conda environment from the shell that launched OpenClaw, avoiding unintended Python and package-manager behavior. #99425 Related #99424 . Thanks @krissding, @ooiuuii.

> Exec approval prompts now display and transmit long command text containing emoji or malformed Unicode without broken characters or encoding failures. #99566 Thanks @mikasa0818.

> The Control UI terminal is now explicit opt-in, opens tabs under the selected agent's workspace and policy, and closes affected shells when accepted access restrictions tighten. #100081 Thanks @rayncc.

> Always-allow approvals for npm exec , npx , pnpm , and yarn wrappers now apply to the actual command rather than unintentionally trusting different future payloads. #102035 Thanks @pgondhi987.

> Copied provider keys and tokens now have hidden terminal control characters removed before request headers are prepared, while intentional spaces remain intact. #96444 Thanks @lin-hongkuan.

> Trajectory exports from chat now require owner authority, preventing other command-authorized channel users from retrieving sensitive session artifacts. #97840 Thanks @pgondhi987.

> Hidden control characters can no longer break terminal hyperlink boundaries or inject control behavior through documentation link text. #96440 Thanks @lin-hongkuan.

> Long Codex app-server approval details and command previews now preserve emoji and extended Unicode characters instead of showing corrupted text. #100177 Thanks @xialonglee.

> Terminal conversations remain open with useful errors, session lists preserve readable previews, and Diffs actions stay attached to the comparison currently on screen.

> New-chat and worktree-chat entry points now appear in the selected language across supported Android and Apple app locales. 24bca38

> Supported non-English native apps now cover more Gateway setup, session, provider, health, messaging, terminal, and device text without English gaps. 52f1e05

> Native app command search now translates loading, unavailable, retry, and no-result states across the languages updated in this release. Sources: 745d2d0 , 7f7bec7 , 35be1c8 , 7db67ab , 4bc5766 , 0672720 , 2a8cd44 , fd648fb , 00b0b40 , a67990a , 7640f67 , 15f4819 , 4d1d720 , d1d3a27 , c2737d5 , bd3263d , 127ce63 , 0c960cd , e6c3ad9 , 84c86f7 , e7aea60 .

> Supported non-English native apps now translate the new Terminal destination, Gateway setup guidance, Back action, connection messages, and OpenClaw branding. e069cb2

> Shortened exec and bash summaries now keep emoji and other supplementary characters intact around the ellipsis instead of displaying a broken replacement glyph. #96963 Thanks @bartok9, @ly-wang19, @vincentkoc.

> Replies triggered through Telegram or another external channel now appear only once in the terminal UI after history refreshes, while resets, session switches, delayed events, and in-progress recovery continue normally. #96980 Thanks @xialonglee.

> The TUI now directs users to the pending device or scope-upgrade approval command instead of incorrectly sending them through chat-DM pairing. #98144 Thanks @romneyda.

> Embedded and local TUI sessions now contain event-consumer errors instead of terminating the terminal. #100117 Thanks @cxbasdev.

> The iOS and Android terminal pages now receive the operator credential from the connected device session, so authenticated users do not land on a terminal that cannot connect. 451190d Thanks @vincentkoc.

> Android's "New chat in worktree" action is now translated across supported non-English locales instead of appearing with a missing resource. #100805 Thanks @amknight.

> Terminal Hatch onboarding and other TUI connections now show starting up until session loading finishes, with accurate running indicators after reconnects. #93999 Thanks @ml12580.

> Workspace skill approvals started in the TUI now appear in that terminal, so users can review and unblock the run without switching to Telegram. #100251 Thanks @vincentkoc.

> The terminal UI now stays open and shows a safe, useful error when a local shell command, slash command, or message submission fails. #100340 Thanks @cxbasdev.

> Windows command lookup now honors the caller's PATHEXT , allowing valid PowerShell scripts and executables to resolve in containers, CI, and isolated environments. #98093 Thanks @wendy-chsy.

> openclaw doctor now gives a missing-transcript preview command that actually shows the entries eligible for removal before users choose to enforce cleanup. #83630 Thanks @yuanhanzhong.

> An invalid openclaw nodes approve &lt;requestId&gt; now shows available pending IDs and the openclaw nodes pending recovery command instead of a raw client error. #94452 Thanks @mushuiyu886.

> Control UI, pairing, setup-code, QR, and status links now prefer a reachable LAN address on hosts with VPNs, virtual adapters, WSL, Hyper-V, or multiple networks. #98482 Thanks @joshavant.

> Crestodian setup and repair chats no longer destabilize the local TUI when a terminal event consumer fails during response delivery. #100341 Thanks @cxbasdev, @vincentkoc.

> Browser CLI commands now accept --browser-profile before or after the subcommand, restoring existing remote-browser and WSL2 command patterns. #94431 Thanks @ml12580.

> Failed openclaw --help and openclaw --version startup now returns exit code 1 promptly instead of leaving the terminal process stuck. #97807 Thanks @aniruddhaadak80, @maweibin.

> openclaw --help now matches command-specific help and completions, with config patch and config schema visible from the main command list. #100670 Thanks @amirf194, @vincentkoc.

> Terminal-rendered links containing balanced parentheses now remain clickable through the complete intended URL instead of being shortened or misdirected. #100697 Thanks @aniruddhaadak80, @zoowh.

> Windows Gateway restarts no longer depend on the findstr check that could leave a visible or hung command window blocking the handoff. #101366 Thanks @deepujain.

> Git installs now create an openclaw launcher that keeps using the intended Node.js runtime even after the user's PATH changes. be7198f

> Terminal and setup documentation links now resolve correctly when relative paths begin with http or absolute HTTP schemes use uppercase letters. #96439 Thanks @lin-hongkuan.

> Terminal notes, Doctor output, and diagnostics now wrap long runs of CJK, full-width, or emoji characters within the requested width instead of spilling across columns. #96746 Thanks @ly-wang19.

> Pending exec approval cards now describe only the approval state, and the foreground-fallback warning appears only after a command actually runs that way. #101561 Thanks @vincentkoc.

> Official operating guidance now matches shipped commands, configuration, setup, status output, placeholders, and recovery behavior more closely. Generated documentation maps also preserve literal command parameters, reducing the chance that a reader follows an example whose identifiers were stripped or whose workflow no longer matches the product.

> Users can now start a chat in its own managed worktree from the Control UI or mobile app, isolating parallel coding while preserving dirty work and cleaning safe idle checkouts automatically. #100788

> Exec and finished background-session results now include signals, timeout flags, failure kinds, and exit reasons so users can tell why a command stopped. #89104 Thanks @yu-xin-c.

> Crestodian setup and local-tool checks no longer terminate OpenClaw when a probed command encounters a rare output-stream read failure. #100741 Thanks @lsr911.

> Agents can now screenshot a selected background Chromium tab without waiting for the browser command to time out, though capture may bring that tab forward. #100857 Thanks @spencer2211.

> Terminal task lists now shorten emoji-heavy summaries without leaving broken replacement characters in the row. #101600 Thanks @maweibin.

> Progress summaries for inline scripts and generated files no longer present heredoc content as extra shell commands that ran. #99379 Thanks @zengwen-dt.

> Added regression coverage so code identifiers with underscores remain readable in the terminal interface. #95211 Thanks @zhangguiping-xydt.

> Prevented pre-commit formatting from unexpectedly rewriting files during merges, rebases, cherry-picks, and reverts. #95842 Thanks @nxmxbbd, @vincentkoc.

> Made pull-request smoke testing faster and more predictable while retaining broader release coverage. #96320 Thanks @romneyda.

> Improved cleanup across command tests, reducing leftover temporary data in local and automated runs. #96359 Thanks @xialonglee.

> Strengthened coverage for verbose command-line logging to reduce future regressions. #96735 Thanks @dwc1997, @vincentkoc.

> Added coverage for terminal output and non-exiting command behavior, improving maintainability without changing the interface. #96736 Thanks @dwc1997.

> Added regression coverage for numeric command-line and configuration options, including defaults and boundary values. #97802 Thanks @dwc1997.

> Made maintainer bug sweeps support requested batch sizes and specific pull request lists while preserving existing readiness standards. #98494 Thanks @vincentkoc.

> Restored documentation and test type checks without changing the attach command's behavior. #98792

> Reduced false QA failures by giving native stop-command recovery the full expected turn time. #99656 Related #99655 . Thanks @romneyda.

> Consolidated internal text cleanup while preserving terminal formatting and outbound-message safety. #99718 Thanks @romneyda.

> Reduced false validation timeouts for native command session targeting under busy conditions. #99743 Thanks @romneyda.

> Corrected command output shortening so zero or invalid length limits no longer produce text beyond the requested size. #99917 Thanks @super-cabbage.

> Sped up update-command coverage while retaining validation of managed-service restart failures. #99945

> Reduced interruptions during bounded maintainer cleanup by allowing larger approved batches of stale pull requests. #100253

> Prevented pull-request landing validation from exhausting shared service limits while preserving trustworthy results. #100332

> Documented the shipped Control UI previews that reveal useful GitHub issue and pull request details. #100555

> Reduced unnecessary repeat validation when concurrent pull requests land without changing the prepared patch. #100593

> Completed changelog coverage for five shipped Control UI and terminal interface fixes. #100599 Thanks @goutamadwant, @haishmg, @ml12580, @ruanrrn, @vincentkoc, @zengwen-dt.

> Completed developer support and validation for integrations using managed-worktree session results. #100793

> Made managed-worktree session results available through the supported developer interface. #100804

> Kept the local debug proxy available and its errors honest when an upstream server ends a response early. #101315 Thanks @sebtardif.

> Narrowed internal terminal interfaces in the gateway while preserving existing terminal behavior. #101941 Thanks @vincentkoc.

Source: https://docs.openclaw.ai/releases/2026.7.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-07-13-5-projects-and-workspaces-changes-in-v2026-7-1|5 Projects and Workspaces changes in v2026.7.1]] · Projects and Workspaces
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
## Nearby in Developer Workflow

- Earlier: 2026-07-13 · Codex CLI · [[Changes/Codex CLI/2026-07-13-published-a-version-only-release-with-no-merged-pull-request-changes-since-rust|Published a version-only release with no merged pull request changes since rust-v0.144.2]]
- Later: 2026-07-13 · OpenCode · [[Changes/OpenCode/2026-07-13-2-developer-workflow-changes-in-v1-17-20-1|2 Developer Workflow changes in v1.17.20 + 1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-18 · Cursor · [[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-07-13-1a1ae3&body=Card%3A%20Changes%2FOpenClaw%2F2026-07-13-99-developer-workflow-changes-in-v2026-7-1.md%0ACard%20ID%3A%20openclaw-2026-07-13-1a1ae3%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.7.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->