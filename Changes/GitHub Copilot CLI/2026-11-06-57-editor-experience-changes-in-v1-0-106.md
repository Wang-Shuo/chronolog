---
card_id: github-copilot-cli-2026-11-06-821a41
date: '2026-11-06'
description: 'GitHub Copilot CLI · 2026-11-06 · Editor Experience: 57 changes in 1.0.106
  — Add a Fusion tier setting to `copilot config`.'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-11-11-tab-to-play-pause|TAB to play/pause]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2917
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: editor-experience
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: cf9ce1036f7a69345a419aba825305e651fce562cb5b215dac1e07e62f4493d7
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-11-06-821a41
  comparison: ''
  date: '2026-11-06'
  description: 'GitHub Copilot CLI — 1.0.106: 57 Editor Experience changes'
  evidence:
  - quote: Add a Fusion tier setting to `copilot config`.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: In `copilot -p --plan`, the agent is no longer told to suggest Shift+Tab
      to leave plan mode, which only works in the interactive interface, and is asked
      to include the plan's key points in its reply instead.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: '`copilot --resume <id>` no longer waits with no output and no end when
      the Copilot task service does not respond; the task lookup now gives up after
      10 seconds and resolution continues.'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: '`copilot help config` now lists every setting the settings catalog offers,
      including the ones that were missing from its hand-written text, such as `askUser`,
      `effortLevel`, `planModel`, `toolSearch` and `worktreeBaseRef`'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: The edit tool now fails at once on a named pipe, socket or device instead
      of waiting forever for the other end of a FIFO, which stalled the turn.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: '`copilot help environment` now says a `COPILOT_AUTO_TIER` value of "fast"
      is ignored with a notice rather than rejected, and that `USE_TGREP=true` does
      not override whether indexed search is available for your account or `USE_BUILTIN_RIPGREP=false`.'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: '`copilot help config`, `copilot help environment` and `copilot help acp`
      no longer name the hidden `--prefer-version`, `--server` and `--stdio` options.'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: '`copilot help limits` shows a status example at the real minimum AI credit
      limit and says the final-call warning appears when 10% or less of the limit
      remains'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: '`copilot help monitoring` now says an `http://` OTLP endpoint disables
      export only when an OTLP CA certificate or client certificate/key variable is
      set, not for every `http://` endpoint.'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: '`copilot --help` and `copilot help --help` now list the `acp` help topic,
      and `copilot help --help` no longer prints its description and topic list with
      stray indentation.'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: copilot skill remove and /skills remove now forget the removed skill's
      disabled state, so a skill added later under the same name no longer starts
      disabled.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Keep /diff output intact for Unicode characters like emoji and supplementary
      symbols.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Stopping an npm-installed copilot by signal now cancels the active turn
      and waits for shutdown instead of leaving it running
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: '`copilot config` now warns when a value of the wrong type makes settings.json
      ignored, instead of reading every setting as unset and reporting writes into
      that file as if they took effect'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Deleting text in front of Chinese, Japanese or Korean characters in the
      prompt no longer leaves the line garbled until the next edit.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: The Sessions tab and the home tab bar now respond to keys after Ctrl+X
      / runs /session over a draft with an open slash-command or @ menu, and one Escape
      closes /ide without clearing that draft.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: When a `/settings` JSON value saved from your editor is not valid JSON,
      the error now shows any control characters it quotes from the file instead of
      letting them restyle the dialog.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Prevent /settings external editor save from overwriting concurrent settings
      changes
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: '`copilot sessions import --name ""` is now rejected as an invalid name
      in both `--dry-run` and a real import, instead of passing the dry run and then
      failing with a persistence error.'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Collect debug logs keeps the active invocation and ignores stale completion
      results
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Wrapped lines in the `/ide` dialog now continue under their text instead
      of under the bullet or row number
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: '`copilot sessions import` now reports a second session header as "Only
      the first record may be a session header." and an unknown record type as unsupported,
      instead of asking for a record id and timestamp those lines never needed.'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: When the editor opened with Ctrl+E in /settings saves the file and then
      exits with an error, the edit is now kept in a recovery file and its path is
      shown, instead of being deleted with a message saying the editor did not save.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Copilot's built-in documentation tool now returns the installed CLI's own
      commands, flags and help topics instead of an error line about a missing README
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: The first `@` of a session now highlights the first suggested file instead
      of the working directory, so Tab or Enter inserts that file. A suggestion you
      pick with the arrow keys still stays highlighted while results update.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: 'The autopilot completion check label now matches the decision autopilot
      acts on: a reviewer verdict with non-English text right after the verdict word
      no longer shows as passed.'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: '`copilot -p --output-format json` and `copilot workflow run` no longer
      write 8-bit terminal control characters (C1 and DEL) from model replies, tool
      output or workflow results raw: they are escaped in the JSON, which parses to
      the same values, and `workflow run` failure messages on stderr show them as
      spaces.'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: 'A repository''s .github/copilot/settings.json can no longer color, hide
      or add lines to the startup warning or the /settings Problems explanation that
      reports its invalid settings: keys and values from the file are shown escaped,
      and a setting''s value containing a line feed is no longer shown in the Problems
      explanation.'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Tab-indented files keep their indentation in the expanded file view, in
      expanded grep and glob results, and in the gist details screen, instead of rendering
      every line at column 0.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Show files with non-ASCII names in /diff local-changes output
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: /diff shows each file's own patch when file names include glob characters
      or start with a colon
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Keep @ file completion suggestions open when navigating folders with spaces
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Tool calls that finish after you abort now show their final completion
      status in the timeline
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Keep tab bar arrows and visible tabs on one row in narrow ask-user forms
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Reopening a settings enum editor keeps the cursor on the saved value
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Keep externally edited prompt text in a recovery file when the editor exits
      with an error
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: '`COPILOT_PROVIDER_GHES_HOST` now accepts the instance''s browser address,
      such as `https://ghes.example.com/`, instead of failing with a malformed `https://https//...`
      URL, and a value that is not a host name fails with an error explaining the
      expected format.'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: A copilot -p run stopped by Ctrl+C or a signal now finishes writing the
      session's shutdown record (usage and code-change totals) before it exits
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: copilot update and /update persist explicit stable or prerelease channel
      selections for future update checks
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Tab completion of copilot config keys now works in bash after root options
      written as --option=value, and in bash and zsh after a bare --sync-session
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: copilot config allowedUrls and deniedUrls now refuse a URL pattern the
      CLI cannot apply, as --allow-url and --deny-url do, instead of saving a rule
      that every start ignores
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: /diff now lists new files whose names contain accented or other non-ASCII
      characters, double quotes or backslashes by their real names, with their added
      badge, instead of git escape codes such as caf\303\251.md
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: copilot help no longer crashes with a stack trace when its output is piped
      to a command that exits early
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: /ide now reports when a settings toggle cannot be saved, instead of showing
      the change as applied while settings.json keeps the old value.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: A user message whose only content is an image, such as one brought in with
      `copilot sessions import`, is now shown in the conversation with its image when
      the session is resumed
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: '`copilot instruction list` reports a repository''s own .github/instructions
      rule files as repository instructions when run from the repository root'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: copilot config proxyUrl now refuses a proxy URL that requests cannot use
      (an unsupported scheme such as socks:// or ftp://, a missing host, or an invalid
      port) and names the setting, instead of saving a value that made the CLI connect
      directly or fail every request
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: The /settings Problems tab now reports a settings value that is silently
      ignored, such as an out-of-range commandHistoryMaxSize, instead of saying there
      are no problems
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: The /settings Problems tab shows unrecognised settings keys as inert escaped
      text, so a key in a repository settings file can no longer style the screen
      or forge extra rows
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Diff view keeps Unicode search highlighting accurate and preserves distinguishing
      filename suffixes in narrow layouts
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Vim mode motions and edits correctly treat pasted blocks and emoji as single
      units.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: copilot config now rejects commandHistoryMaxSize values outside 1 to 1000
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Tool results preserve exact source text so follow-up edits and responses
      stay accurate.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: CLI startup preserves installed shell completion files when their content
      is unchanged
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Forked sessions keep file rewind available after resume and restore only
      post-fork file edits
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: /pr completion suggests agentmerge while continuing to accept automerge
      for compatibility
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: 'Inline images now work in herdr panes with no setup: the CLI asks herdr''s
      socket API whether its `experimental.kitty_graphics` renderer is on, replacing
      the `COPILOT_INLINE_IMAGES_HERDR=1` opt-in'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 57-editor-experience-changes-in-v1-0-106
  source_release: github-copilot-cli-2026-11-06-v1-0-106-github-435988160-ec5b15d4
  source_type: github_releases
  theme: editor-experience
  title: 57 Editor Experience changes in v1.0.106
  type: change
related_changes:
- '[[Changes/Descript/2026-11-06-script-text-no-longer-shakes-up-and-down-while-you-edit|Script
  text no longer shakes up and down while you edit]]'
- '[[Changes/Descript/2026-11-06-teach-underlord-your-workflow|Teach Underlord your
  workflow]]'
- '[[Changes/Descript/2026-11-06-upload-to-descript-from-chatgpt|Upload to Descript
  from ChatGPT]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-11-06-v1-0-106-github-435988160-ec5b15d4|github-copilot-cli-2026-11-06-v1-0-106-github-435988160-ec5b15d4]]'
source_type: github_releases
theme: editor-experience
title: 57 Editor Experience changes in v1.0.106
type: change
---

<!-- chronolog:begin region="header" -->
# 57 Editor Experience changes in v1.0.106

**GitHub Copilot CLI** · 2026-11-06 · [[Themes/editor-experience|Editor Experience]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.106) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-11-06-v1-0-106-github-435988160-ec5b15d4|1.0.106]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Add a Fusion tier setting to `copilot config`.

> In `copilot -p --plan`, the agent is no longer told to suggest Shift+Tab to leave plan mode, which only works in the interactive interface, and is asked to include the plan's key points in its reply instead.

> `copilot --resume <id>` no longer waits with no output and no end when the Copilot task service does not respond; the task lookup now gives up after 10 seconds and resolution continues.

> `copilot help config` now lists every setting the settings catalog offers, including the ones that were missing from its hand-written text, such as `askUser`, `effortLevel`, `planModel`, `toolSearch` and `worktreeBaseRef`

> The edit tool now fails at once on a named pipe, socket or device instead of waiting forever for the other end of a FIFO, which stalled the turn.

> `copilot help environment` now says a `COPILOT_AUTO_TIER` value of "fast" is ignored with a notice rather than rejected, and that `USE_TGREP=true` does not override whether indexed search is available for your account or `USE_BUILTIN_RIPGREP=false`.

> `copilot help config`, `copilot help environment` and `copilot help acp` no longer name the hidden `--prefer-version`, `--server` and `--stdio` options.

> `copilot help limits` shows a status example at the real minimum AI credit limit and says the final-call warning appears when 10% or less of the limit remains

> `copilot help monitoring` now says an `http://` OTLP endpoint disables export only when an OTLP CA certificate or client certificate/key variable is set, not for every `http://` endpoint.

> `copilot --help` and `copilot help --help` now list the `acp` help topic, and `copilot help --help` no longer prints its description and topic list with stray indentation.

> copilot skill remove and /skills remove now forget the removed skill's disabled state, so a skill added later under the same name no longer starts disabled.

> Keep /diff output intact for Unicode characters like emoji and supplementary symbols.

> Stopping an npm-installed copilot by signal now cancels the active turn and waits for shutdown instead of leaving it running

> `copilot config` now warns when a value of the wrong type makes settings.json ignored, instead of reading every setting as unset and reporting writes into that file as if they took effect

> Deleting text in front of Chinese, Japanese or Korean characters in the prompt no longer leaves the line garbled until the next edit.

> The Sessions tab and the home tab bar now respond to keys after Ctrl+X / runs /session over a draft with an open slash-command or @ menu, and one Escape closes /ide without clearing that draft.

> When a `/settings` JSON value saved from your editor is not valid JSON, the error now shows any control characters it quotes from the file instead of letting them restyle the dialog.

> Prevent /settings external editor save from overwriting concurrent settings changes

> `copilot sessions import --name ""` is now rejected as an invalid name in both `--dry-run` and a real import, instead of passing the dry run and then failing with a persistence error.

> Collect debug logs keeps the active invocation and ignores stale completion results

> Wrapped lines in the `/ide` dialog now continue under their text instead of under the bullet or row number

> `copilot sessions import` now reports a second session header as "Only the first record may be a session header." and an unknown record type as unsupported, instead of asking for a record id and timestamp those lines never needed.

> When the editor opened with Ctrl+E in /settings saves the file and then exits with an error, the edit is now kept in a recovery file and its path is shown, instead of being deleted with a message saying the editor did not save.

> Copilot's built-in documentation tool now returns the installed CLI's own commands, flags and help topics instead of an error line about a missing README

> The first `@` of a session now highlights the first suggested file instead of the working directory, so Tab or Enter inserts that file. A suggestion you pick with the arrow keys still stays highlighted while results update.

> The autopilot completion check label now matches the decision autopilot acts on: a reviewer verdict with non-English text right after the verdict word no longer shows as passed.

> `copilot -p --output-format json` and `copilot workflow run` no longer write 8-bit terminal control characters (C1 and DEL) from model replies, tool output or workflow results raw: they are escaped in the JSON, which parses to the same values, and `workflow run` failure messages on stderr show them as spaces.

> A repository's .github/copilot/settings.json can no longer color, hide or add lines to the startup warning or the /settings Problems explanation that reports its invalid settings: keys and values from the file are shown escaped, and a setting's value containing a line feed is no longer shown in the Problems explanation.

> Tab-indented files keep their indentation in the expanded file view, in expanded grep and glob results, and in the gist details screen, instead of rendering every line at column 0.

> Show files with non-ASCII names in /diff local-changes output

> /diff shows each file's own patch when file names include glob characters or start with a colon

> Keep @ file completion suggestions open when navigating folders with spaces

> Tool calls that finish after you abort now show their final completion status in the timeline

> Keep tab bar arrows and visible tabs on one row in narrow ask-user forms

> Reopening a settings enum editor keeps the cursor on the saved value

> Keep externally edited prompt text in a recovery file when the editor exits with an error

> `COPILOT_PROVIDER_GHES_HOST` now accepts the instance's browser address, such as `https://ghes.example.com/`, instead of failing with a malformed `https://https//...` URL, and a value that is not a host name fails with an error explaining the expected format.

> A copilot -p run stopped by Ctrl+C or a signal now finishes writing the session's shutdown record (usage and code-change totals) before it exits

> copilot update and /update persist explicit stable or prerelease channel selections for future update checks

> Tab completion of copilot config keys now works in bash after root options written as --option=value, and in bash and zsh after a bare --sync-session

> copilot config allowedUrls and deniedUrls now refuse a URL pattern the CLI cannot apply, as --allow-url and --deny-url do, instead of saving a rule that every start ignores

> /diff now lists new files whose names contain accented or other non-ASCII characters, double quotes or backslashes by their real names, with their added badge, instead of git escape codes such as caf\303\251.md

> copilot help no longer crashes with a stack trace when its output is piped to a command that exits early

> /ide now reports when a settings toggle cannot be saved, instead of showing the change as applied while settings.json keeps the old value.

> A user message whose only content is an image, such as one brought in with `copilot sessions import`, is now shown in the conversation with its image when the session is resumed

> `copilot instruction list` reports a repository's own .github/instructions rule files as repository instructions when run from the repository root

> copilot config proxyUrl now refuses a proxy URL that requests cannot use (an unsupported scheme such as socks:// or ftp://, a missing host, or an invalid port) and names the setting, instead of saving a value that made the CLI connect directly or fail every request

> The /settings Problems tab now reports a settings value that is silently ignored, such as an out-of-range commandHistoryMaxSize, instead of saying there are no problems

> The /settings Problems tab shows unrecognised settings keys as inert escaped text, so a key in a repository settings file can no longer style the screen or forge extra rows

> Diff view keeps Unicode search highlighting accurate and preserves distinguishing filename suffixes in narrow layouts

> Vim mode motions and edits correctly treat pasted blocks and emoji as single units.

> copilot config now rejects commandHistoryMaxSize values outside 1 to 1000

> Tool results preserve exact source text so follow-up edits and responses stay accurate.

> CLI startup preserves installed shell completion files when their content is unchanged

> Forked sessions keep file rewind available after resume and restore only post-fork file edits

> /pr completion suggests agentmerge while continuing to accept automerge for compatibility

> Inline images now work in herdr panes with no setup: the CLI asks herdr's socket API whether its `experimental.kitty_graphics` renderer is on, replacing the `COPILOT_INLINE_IMAGES_HERDR=1` opt-in

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
- [[Changes/GitHub Copilot CLI/2026-11-06-33-model-support-changes-in-v1-0-106|33 Model Support changes in v1.0.106]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-11-06-89-apps-and-integrations-changes-in-v1-0-106|89 Apps and Integrations changes in v1.0.106]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-11-06-2-image-generation-changes-in-v1-0-106|2 Image Generation changes in v1.0.106]] · Image Generation
- [[Changes/GitHub Copilot CLI/2026-11-06-42-interface-experience-changes-in-v1-0-106|42 Interface Experience changes in v1.0.106]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-11-06-5-pricing-model-changes-in-v1-0-106|5 Pricing Model changes in v1.0.106]] · Pricing Model
- [[Changes/GitHub Copilot CLI/2026-11-06-in-the-every-schedule-manager-x-now-removes-the-highlighted-schedule-even-after|In the /every schedule manager, x now removes the highlighted schedule even after…]] · Automation and Scheduling
- [[Changes/GitHub Copilot CLI/2026-11-06-23-account-and-access-changes-in-v1-0-106|23 Account and Access changes in v1.0.106]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-11-06-172-other-changes-in-v1-0-106|172 other changes in v1.0.106]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Editor Experience

- Earlier: 2026-11-06 · Descript · [[Changes/Descript/2026-11-06-upload-to-descript-from-chatgpt|Upload to Descript from ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-11-11 · Descript · [[Changes/Descript/2018-11-11-tab-to-play-pause|TAB to play/pause]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-11-06-821a41&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-11-06-57-editor-experience-changes-in-v1-0-106.md%0ACard%20ID%3A%20github-copilot-cli-2026-11-06-821a41%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.106%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->