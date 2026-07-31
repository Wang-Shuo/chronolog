---
created: '2023-01-09'
date: '2026-07-28'
machine_hash: ed5144c57ac99f5a4ff02543bd283a63f9e447073467bd7d64e524ee95d9a7d0
modified: '2026-07-28'
products_involved:
- ChatGPT
- Claude Code
- Cursor
status: official
tags:
- theme
- moc
theme: interface-experience
---

# Theme: interface-experience

## Cross-Product Timeline
<!-- chronolog:begin region="timeline" -->
```mermaid
timeline
    title interface-experience
    2023-01-09 : ChatGPT : Stop generating: Based on your feedback, we've added the ability to stop generat
    2023-02-09 : ChatGPT : Version selection is made easy with a dedicated dropdown menu at the top of the
    2023-03-18 : Cursor : Can open chat history from the prompt bar
    2023-03-18 : Cursor : Up and down arrow in prompt bar have been mapped to less annoying keybindings
    2023-03-23 : Cursor : Easy to select and copy from chat
    2023-03-23 : Cursor : Chat history saved between sessions
    2023-03-23 : Cursor : Resizable sidebar
    2023-03-27 : Cursor : Changes autoupdate to notify you when there's a new version
    2023-03-30 : Cursor : Cleaned up chat styling
    2023-05-03 : ChatGPT : You can now turn off chat history and export your data from the ChatGPT settings
    2023-05-04 : Cursor : Added the ability to hide the tooltip (Cursor config > Advanced > Chat/Edit Tool
    2023-05-09 : Cursor : Includes some updates to "Option+Enter" in the chat
    2023-05-17 : Cursor : Activity Bar pinning
    2023-05-20 : Cursor : We've added a new feedback button at the top right of the app. - We really do
    2023-06-24 : Cursor : The chat has been revamped! You can now use @ symbols to show files/code/docs to
    2023-06-27 : Cursor : Better @ symbol keyboard ergonomics
    2023-07-03 : Cursor : (Also, you can now use up/down arrows for history in chat.)
    2023-07-07 : Cursor : Chat/Edit tooltip blocks less code
    2023-07-07 : Cursor : Better @ symbol keyboard ergonomics
    2023-07-27 : Cursor : C# and F# now properly render in the chat
    2023-07-28 : Cursor : new completion experience powered by gpt-4. Just press ⌘/^+↩️ and you'll get a l
    2023-08-03 : ChatGPT : Suggested replies: Go deeper with a click. ChatGPT now suggests relevant ways to
    2023-08-03 : ChatGPT : Prompt examples: A blank page can be intimidating. At the beginning of a new cha
    2023-08-17 : Cursor : Keychords now use Cmd+R/Ctrl+R.
    2023-08-21 : Cursor : Activity bar elements can now be reordered with drag-and-drop.
    2023-08-21 : Cursor : Nicer error messages in the chat! Fewer annoying popups.
    2023-08-22 : Cursor : Nicer error messages in the chat! Fewer annoying popups.
    2023-08-30 : Cursor : You can now switch to the VS Code sidebar orientation
    2023-09-11 : ChatGPT : If you've configured your browser to use one of these supported languages, you'l
    2023-11-03 : Cursor : Chat scroll: we got rid of sticky scroll to make the chat easier to read.
    2023-11-03 : Cursor : Styling tweaks: some buttons and hints should look nicer!
    2023-11-10 : Cursor : Command-dot: you can now use the Command-dot menu to have Command-K fix lint err
    2023-11-12 : Cursor : Copilot++ improvements: Includes green highlights to see what Copilot++ has adde
    2023-11-27 : Cursor : Copilot++ Improvements: We've spent some time improving the latency of Copilot++
    2023-12-06 : Cursor : Allows users to provide feedback on the chat response.
    2023-12-06 : Cursor : Minor onboarding changes.
    2023-12-16 : Cursor : @ previews: We made it easier to see what codeblock you're @'ing.
    2024-02-02 : Cursor : You can now drag images into the Command-K prompt bar!
    2024-02-09 : Cursor : Smoother onboarding (fix Windows settings import, option to import folder/window
    2024-02-09 : Cursor : Fine-grained chat replies (start by hovering over the area of the response you w
    2024-03-01 : Cursor : AI Notes enabled by default (hold shift on any symbol), better in-editor chat, a
    2024-04-01 : Cursor : UPDATE (0.31.1–0.31.3): Adds back in AI Review (alpha), fixes the "Cursor Settin
    2024-04-12 : Cursor : Cursor Help Pane (Beta): You can also ask Cursor about Cursor! The Cursor Help P
    2024-05-03 : Cursor : Command-K Autoselect: We've also added automatic selection for Command-K! This m
    2024-07-23 : Cursor : We've also added a file picker, arrow key navigation, and a model toggle to Comp
    2024-11-22 : ChatGPT : A small settings icon was added in larger viewports when the sidebar is not open
    2024-11-22 : ChatGPT : Sidebar redesign
    2024-11-22 : ChatGPT : New floating mode added with soft dismiss behavior
    2024-11-22 : ChatGPT : Recent conversations are now limited in the sidebar, with an unlimited infinite
    2024-11-24 : Cursor : Composer UI in the sidebar with inline diffs
    2025-02-19 : Cursor : 0.46.3: Enhanced download reliability, fixed keybinding issue
    2025-02-28 : ChatGPT : The temporary chat icon is now in top bar to make the temporary chat experience
    2025-03-18 : ChatGPT : Added long press on your message to open menu actions: Copy, Edit.
    2025-03-18 : ChatGPT : Improved response display of nested blockquote content.
    2025-03-23 : Cursor : The vertical sidebar option will temporarily be unavailable for users who opted
    2025-04-15 : Cursor : More accessible history
    2025-05-06 : ChatGPT : No tools are deprecated—access is simply consolidated to clear space and reduce
    2025-09-16 : ChatGPT : Formatting: Answers are better formatted for quick understanding without losing
    2025-09-29 : Cursor : Autocomplete for Agent
    2025-10-29 : Cursor : Manage agents in our new editor, with a sidebar for your agents and plans.
    2025-11-21 : Cursor : You can also ⌘+F to search inside generated plans.
    2025-12-10 : Cursor : Design and code simultaneously with a brand new browser sidebar and component tr
    2025-12-19 : Claude Code : Added syntax highlighting info to theme picker
    2025-12-19 : Claude Code : Added ctrl+t shortcut in `/theme` to toggle syntax highlighting on/off
    2025-12-19 : Claude Code : Added alt-y yank-pop to cycle through kill ring history after ctrl-y yank
    2025-12-19 : Claude Code : Improved `/theme` command to open theme picker directly
    2026-01-09 : Claude Code : Added release channel (`stable` or `latest`) toggle to `/config`
    2026-01-09 : Claude Code : Improved terminal rendering stability by preventing uncontrolled writes from cor
    2026-01-09 : Claude Code : Added Shift+Tab keyboard shortcut in plan mode to quickly select "auto-accept ed
    2026-01-13 : Claude Code : Added Updates section to `/doctor` showing auto-update channel and available npm
    2026-01-14 : Claude Code : Added `showTurnDuration` setting to hide turn duration messages (e.g., "Cooked f
    2026-01-20 : Claude Code : Improved backspace to delete pasted text as a single token instead of one charac
    2026-01-27 : Claude Code : Added PR review status indicator to the prompt footer, showing the current branc
    2026-01-27 : Claude Code : Added arrow key history navigation in vim normal mode when cursor cannot move fu
    2026-01-28 : Claude Code : Improved read/search progress indicators to show "Reading…" while in progress an
    2026-01-29 : Claude Code : Improved terminal rendering performance with optimized screen data layout
    2026-01-29 : Claude Code : Added customizable spinner verbs setting (`spinnerVerbs`)
    2026-01-29 : Claude Code : Changed merged pull requests to show a purple status indicator in the prompt foo
    2026-01-30 : ChatGPT : Responses in ChatGPT are now more visual and easier to scan. For everyday questi
    2026-02-06 : Claude Code : Improved error messages for API connection failures — now shows specific cause (
    2026-02-10 : ChatGPT : We’re introducing improvements to deep research in ChatGPT to help produce more
    2026-02-10 : Claude Code : Improved terminal rendering performance
    2026-02-13 : ChatGPT : Quick tools in the composer. A new quick-tools menu in the message composer make
    2026-02-13 : ChatGPT : Simplified composer. The message composer has been streamlined to reduce visual
    2026-02-13 : Claude Code : Improved narrow terminal layout for prompt footer
    2026-02-17 : Claude Code : Added `spinnerTipsOverride` setting to customize spinner tips — configure `tips`
    2026-02-18 : Cursor : Typing /plan takes you back to your current plan and its action menu. We've also
    2026-02-18 : Cursor : This release introduces the ability to hand off plans from the CLI to the cloud,
    2026-02-26 : Claude Code : Improved ordering of short task lists
    2026-02-26 : Claude Code : Added `/copy` command to show an interactive picker when code blocks are present
    2026-02-27 : ChatGPT : Automatic scroll to latest message. Existing conversations now automatically scr
    2026-03-05 : Claude Code : Added numeric keypad support for selecting options in Claude's interview questio
    2026-03-10 : Claude Code : Added `w` key in `/copy` to write the focused selection directly to a file, bypa
    2026-03-11 : Claude Code : Improved Up arrow after interrupting Claude — now restores the interrupted promp
    2026-03-11 : Claude Code : Added `modelOverrides` setting to map model picker entries to custom provider mo
    2026-03-17 : ChatGPT : The Auto functionality can be accessed by clicking Configure in the model picker
    2026-03-17 : Claude Code : `/copy` now accepts an optional index: `/copy N` copies the Nth-latest assistant
    2026-03-17 : Claude Code : Response text now streams line-by-line as it's generated
    2026-03-18 : Claude Code : Added "Show turn duration" toggle to the `/config` menu
    2026-03-19 : Claude Code : Added `rate_limits` field to statusline scripts for displaying Claude.ai rate li
    2026-04-01 : Claude Code : Added `CLAUDE_CODE_NO_FLICKER=1` environment variable to opt into flicker-free a
    2026-04-04 : Claude Code : `/release-notes` is now an interactive version picker
    2026-04-08 : Claude Code : Added `refreshInterval` status line setting to re-run the status line command ev
    2026-04-10 : Claude Code : Improved focus mode: Claude now writes more self-contained summaries since it kn
    2026-04-13 : Cursor : Expand panes to focus on a conversation, drag agents into tiles, and use keybind
    2026-04-13 : Cursor : Tiled layout
    2026-04-14 : Claude Code : `/undo` is now an alias for `/rewind`
    2026-04-14 : Claude Code : Show thinking hints sooner during long operations
    2026-04-15 : Claude Code : Added `autoScrollEnabled` config to disable conversation auto-scroll in fullscre
    2026-04-15 : Claude Code : Added `/tui` command and `tui` setting — run `/tui fullscreen` to switch to flic
    2026-04-15 : Claude Code : Improved the extended-thinking indicator with a rotating progress hint
    2026-04-16 : Claude Code : `/effort` now opens an interactive slider when called without arguments, with ar
    2026-04-17 : Claude Code : Fullscreen mode: Shift+↑/↓ now scrolls the viewport when extending a selection p
    2026-04-17 : Claude Code : Windows: `Ctrl+Backspace` now deletes the previous word
    2026-04-17 : Claude Code : `Ctrl+A` and `Ctrl+E` now move to the start/end of the current logical line in m
    2026-04-20 : Claude Code : Thinking spinner now shows progress inline ("still thinking", "thinking more", "
    2026-04-20 : Claude Code : Smoother fullscreen scrolling in VS Code, Cursor, and Windsurf terminals — `/ter
    2026-04-23 : Claude Code : Added vim visual mode (`v`) and visual-line mode (`V`) with selection, operators
    2026-04-23 : Claude Code : Added `CLAUDE_CODE_HIDE_CWD` environment variable to hide the working directory
    2026-04-28 : Claude Code : Added a type-to-filter search box to `/skills` so you can find a skill in long l
    2026-04-28 : Claude Code : Fullscreen mode: typing into the prompt no longer jumps scroll back to the botto
    2026-05-04 : Claude Code : Bare `/color` (no args) now picks a random session color
    2026-05-06 : Claude Code : Added `CLAUDE_CODE_FORCE_SYNC_OUTPUT=1` env var to force-enable synchronized out
    2026-05-06 : Claude Code : Added `CLAUDE_CODE_DISABLE_ALTERNATE_SCREEN=1` env var to opt out of the fullscr
    2026-05-06 : Claude Code : Added a "Pasting…" footer hint while a Ctrl+V image paste is being read from the
    2026-05-07 : Claude Code : Improved focus mode behavior
    2026-05-07 : Cursor : The Changes tab makes it easier to navigate larger PRs with a file tree and chan
    2026-05-11 : Claude Code : Added transcript view navigation: `?` for keyboard shortcuts, `{`/`}` to jump be
    2026-05-13 : Cursor : Full screen maximizes the right panel so you can focus on a single tab.
    2026-05-13 : Cursor : Enter and exit full screen by clicking on the expand/contract button in the pane
    2026-05-13 : Cursor : Full-screen tabs
    2026-05-19 : Claude Code : Status line JSON input now includes GitHub repo and PR information when detected
    2026-05-19 : Claude Code : `/model` now changes the model for the current session only; press `d` in the mo
    2026-05-21 : Claude Code : Prompt history no longer records consecutive duplicate entries — recalling a pro
    2026-05-22 : Claude Code : Markdown output now renders GFM task list checkboxes (`- [ ] todo` / `- [x] done
    2026-05-28 : Claude Code : `claude agents`: autocomplete in the dispatch input now suggests native slash co
    2026-06-02 : Claude Code : Fullscreen mode: clipboard now uses `wl-copy`/`xclip`/`xsel` on Linux when avail
    2026-06-03 : Claude Code : Clicking a slash command in the autocomplete menu now fills it into your prompt
    2026-06-04 : Claude Code : Added a "c to copy" shortcut to `/btw` that copies the raw markdown answer to th
    2026-06-05 : Cursor : Multi-select elements
    2026-06-08 : ChatGPT : Improvement to charts, table of contents and full screen writing. Also fixes lon
    2026-06-08 : ChatGPT : Table of contents in longer conversations: Conversations longer than five respon
    2026-06-10 : ChatGPT : We’re updating the model picker to make it easier to choose the balance of speed
    2026-06-12 : Claude Code : Added `footerLinksRegexes` setting for regex-matched link badges in the footer r
    2026-06-12 : Claude Code : Added `wheelScrollAccelerationEnabled` setting to disable mouse-wheel scroll acc
    2026-06-17 : ChatGPT : A new Scheduled page, discoverable in the sidebar, gives users one place to view
    2026-06-17 : Claude Code : Improved streaming of long paragraphs: text now appears line-by-line instead of
    2026-06-19 : Claude Code : Added `/config --help` to list all available shorthand keys for `/config key=val
    2026-06-19 : Claude Code : Changed `/config` toggle behavior: Enter and Space both change the selected sett
    2026-06-23 : Claude Code : Added org-configured model restrictions to the model picker, `--model`, `/model`
    2026-06-23 : Claude Code : Improved `/btw` with ←/→ arrow navigation to step through earlier answers
    2026-06-26 : Claude Code : Added `CLAUDE_CODE_DISABLE_MOUSE_CLICKS` to disable mouse click/drag/hover in fu
    2026-07-03 : Claude Code : Changed `AskUserQuestion` dialogs to no longer auto-continue by default; opt int
    2026-07-10 : Cursor : Conversation search
    2026-07-11 : Claude Code : Improved agent view: pasting the same text again now expands the collapsed `[Pas
    2026-07-14 : ChatGPT : Start searching from the ChatGPT sidebar to find what you need across everything
    2026-07-14 : Claude Code : Added mouse-click support for multi-select menus and "Other" input rows in fulls
    2026-07-14 : Claude Code : Added a live elapsed-time counter to the collapsed tool summary line so long-run
    2026-07-15 : Claude Code : Improved terminal layout and rendering performance
    2026-07-17 : Cursor : Interaction improvements
    2026-07-28 : Cursor : Existing Free users in India can upgrade their plan from the dashboard. New user
```
<!-- chronolog:end -->

## Change Cards
<!-- chronolog:begin region="cards" -->
- 2023-01-09 ChatGPT: [[Changes/ChatGPT/2023-01-09-stop-generating-based-on-your-feedback-we-ve-added-the-ability-to-stop-generatin|Stop generating: Based on your feedback, we've added the ability to stop generat]]
- 2023-02-09 ChatGPT: [[Changes/ChatGPT/2023-02-09-version-selection-is-made-easy-with-a-dedicated-dropdown-menu-at-the-top-of-the|Version selection is made easy with a dedicated dropdown menu at the top of the]]
- 2023-03-18 Cursor: [[Changes/Cursor/2023-03-18-can-open-chat-history-from-the-prompt-bar|Can open chat history from the prompt bar]]
- 2023-03-18 Cursor: [[Changes/Cursor/2023-03-18-up-and-down-arrow-in-prompt-bar-have-been-mapped-to-less-annoying-keybindings|Up and down arrow in prompt bar have been mapped to less annoying keybindings]]
- 2023-03-23 Cursor: [[Changes/Cursor/2023-03-23-easy-to-select-and-copy-from-chat|Easy to select and copy from chat]]
- 2023-03-23 Cursor: [[Changes/Cursor/2023-03-23-chat-history-saved-between-sessions|Chat history saved between sessions]]
- 2023-03-23 Cursor: [[Changes/Cursor/2023-03-23-resizable-sidebar|Resizable sidebar]]
- 2023-03-27 Cursor: [[Changes/Cursor/2023-03-27-changes-autoupdate-to-notify-you-when-there-s-a-new-version|Changes autoupdate to notify you when there's a new version]]
- 2023-03-30 Cursor: [[Changes/Cursor/2023-03-30-cleaned-up-chat-styling|Cleaned up chat styling]]
- 2023-05-03 ChatGPT: [[Changes/ChatGPT/2023-05-03-you-can-now-turn-off-chat-history-and-export-your-data-from-the-chatgpt-settings|You can now turn off chat history and export your data from the ChatGPT settings]]
- 2023-05-04 Cursor: [[Changes/Cursor/2023-05-04-added-the-ability-to-hide-the-tooltip-cursor-config-advanced-chat-edit-tooltip|Added the ability to hide the tooltip (Cursor config > Advanced > Chat/Edit Tool]]
- 2023-05-09 Cursor: [[Changes/Cursor/2023-05-09-includes-some-updates-to-option-enter-in-the-chat|Includes some updates to "Option+Enter" in the chat]]
- 2023-05-17 Cursor: [[Changes/Cursor/2023-05-17-activity-bar-pinning|Activity Bar pinning]]
- 2023-05-20 Cursor: [[Changes/Cursor/2023-05-20-we-ve-added-a-new-feedback-button-at-the-top-right-of-the-app-we-really-do|We've added a new feedback button at the top right of the app. - We really do]]
- 2023-06-24 Cursor: [[Changes/Cursor/2023-06-24-the-chat-has-been-revamped-you-can-now-use-symbols-to-show-files-code-docs-to-th|The chat has been revamped! You can now use @ symbols to show files/code/docs to]]
- 2023-06-27 Cursor: [[Changes/Cursor/2023-06-27-better-symbol-keyboard-ergonomics|Better @ symbol keyboard ergonomics]]
- 2023-07-03 Cursor: [[Changes/Cursor/2023-07-03-also-you-can-now-use-up-down-arrows-for-history-in-chat|(Also, you can now use up/down arrows for history in chat.)]]
- 2023-07-07 Cursor: [[Changes/Cursor/2023-07-07-chat-edit-tooltip-blocks-less-code|Chat/Edit tooltip blocks less code]]
- 2023-07-07 Cursor: [[Changes/Cursor/2023-07-07-better-symbol-keyboard-ergonomics|Better @ symbol keyboard ergonomics]]
- 2023-07-27 Cursor: [[Changes/Cursor/2023-07-27-c-and-f-now-properly-render-in-the-chat|C# and F# now properly render in the chat]]
- 2023-07-28 Cursor: [[Changes/Cursor/2023-07-28-new-completion-experience-powered-by-gpt-4-just-press-and-you-ll-get-a-long-comp|new completion experience powered by gpt-4. Just press ⌘/^+↩️ and you'll get a l]]
- 2023-08-03 ChatGPT: [[Changes/ChatGPT/2023-08-03-suggested-replies-go-deeper-with-a-click-chatgpt-now-suggests-relevant-ways-to-c|Suggested replies: Go deeper with a click. ChatGPT now suggests relevant ways to]]
- 2023-08-03 ChatGPT: [[Changes/ChatGPT/2023-08-03-prompt-examples-a-blank-page-can-be-intimidating-at-the-beginning-of-a-new-chat|Prompt examples: A blank page can be intimidating. At the beginning of a new cha]]
- 2023-08-17 Cursor: [[Changes/Cursor/2023-08-17-keychords-now-use-cmd-r-ctrl-r|Keychords now use Cmd+R/Ctrl+R.]]
- 2023-08-21 Cursor: [[Changes/Cursor/2023-08-21-activity-bar-elements-can-now-be-reordered-with-drag-and-drop|Activity bar elements can now be reordered with drag-and-drop.]]
- 2023-08-21 Cursor: [[Changes/Cursor/2023-08-21-nicer-error-messages-in-the-chat-fewer-annoying-popups|Nicer error messages in the chat! Fewer annoying popups.]]
- 2023-08-22 Cursor: [[Changes/Cursor/2023-08-22-nicer-error-messages-in-the-chat-fewer-annoying-popups|Nicer error messages in the chat! Fewer annoying popups.]]
- 2023-08-30 Cursor: [[Changes/Cursor/2023-08-30-you-can-now-switch-to-the-vs-code-sidebar-orientation|You can now switch to the VS Code sidebar orientation]]
- 2023-09-11 ChatGPT: [[Changes/ChatGPT/2023-09-11-if-you-ve-configured-your-browser-to-use-one-of-these-supported-languages-you-ll|If you've configured your browser to use one of these supported languages, you'l]]
- 2023-11-03 Cursor: [[Changes/Cursor/2023-11-03-chat-scroll-we-got-rid-of-sticky-scroll-to-make-the-chat-easier-to-read|Chat scroll: we got rid of sticky scroll to make the chat easier to read.]]
- 2023-11-03 Cursor: [[Changes/Cursor/2023-11-03-styling-tweaks-some-buttons-and-hints-should-look-nicer|Styling tweaks: some buttons and hints should look nicer!]]
- 2023-11-10 Cursor: [[Changes/Cursor/2023-11-10-command-dot-you-can-now-use-the-command-dot-menu-to-have-command-k-fix-lint-erro|Command-dot: you can now use the Command-dot menu to have Command-K fix lint err]]
- 2023-11-12 Cursor: [[Changes/Cursor/2023-11-12-copilot-improvements-includes-green-highlights-to-see-what-copilot-has-added-the|Copilot++ improvements: Includes green highlights to see what Copilot++ has adde]]
- 2023-11-27 Cursor: [[Changes/Cursor/2023-11-27-copilot-improvements-we-ve-spent-some-time-improving-the-latency-of-copilot-and|Copilot++ Improvements: We've spent some time improving the latency of Copilot++]]
- 2023-12-06 Cursor: [[Changes/Cursor/2023-12-06-allows-users-to-provide-feedback-on-the-chat-response|Allows users to provide feedback on the chat response.]]
- 2023-12-06 Cursor: [[Changes/Cursor/2023-12-06-minor-onboarding-changes|Minor onboarding changes.]]
- 2023-12-16 Cursor: [[Changes/Cursor/2023-12-16-previews-we-made-it-easier-to-see-what-codeblock-you-re-ing|@ previews: We made it easier to see what codeblock you're @'ing.]]
- 2024-02-02 Cursor: [[Changes/Cursor/2024-02-02-you-can-now-drag-images-into-the-command-k-prompt-bar|You can now drag images into the Command-K prompt bar!]]
- 2024-02-09 Cursor: [[Changes/Cursor/2024-02-09-smoother-onboarding-fix-windows-settings-import-option-to-import-folder-window-s|Smoother onboarding (fix Windows settings import, option to import folder/window]]
- 2024-02-09 Cursor: [[Changes/Cursor/2024-02-09-fine-grained-chat-replies-start-by-hovering-over-the-area-of-the-response-you-wa|Fine-grained chat replies (start by hovering over the area of the response you w]]
- 2024-03-01 Cursor: [[Changes/Cursor/2024-03-01-ai-notes-enabled-by-default-hold-shift-on-any-symbol-better-in-editor-chat-auto|AI Notes enabled by default (hold shift on any symbol), better in-editor chat, a]]
- 2024-04-01 Cursor: [[Changes/Cursor/2024-04-01-update-0-31-1-0-31-3-adds-back-in-ai-review-alpha-fixes-the-cursor-settings-menu|UPDATE (0.31.1–0.31.3): Adds back in AI Review (alpha), fixes the "Cursor Settin]]
- 2024-04-12 Cursor: [[Changes/Cursor/2024-04-12-cursor-help-pane-beta-you-can-also-ask-cursor-about-cursor-the-cursor-help-pane|Cursor Help Pane (Beta): You can also ask Cursor about Cursor! The Cursor Help P]]
- 2024-05-03 Cursor: [[Changes/Cursor/2024-05-03-command-k-autoselect-we-ve-also-added-automatic-selection-for-command-k-this-mea|Command-K Autoselect: We've also added automatic selection for Command-K! This m]]
- 2024-07-23 Cursor: [[Changes/Cursor/2024-07-23-we-ve-also-added-a-file-picker-arrow-key-navigation-and-a-model-toggle-to-compos|We've also added a file picker, arrow key navigation, and a model toggle to Comp]]
- 2024-11-22 ChatGPT: [[Changes/ChatGPT/2024-11-22-a-small-settings-icon-was-added-in-larger-viewports-when-the-sidebar-is-not-open|A small settings icon was added in larger viewports when the sidebar is not open]]
- 2024-11-22 ChatGPT: [[Changes/ChatGPT/2024-11-22-sidebar-redesign|Sidebar redesign]]
- 2024-11-22 ChatGPT: [[Changes/ChatGPT/2024-11-22-new-floating-mode-added-with-soft-dismiss-behavior|New floating mode added with soft dismiss behavior]]
- 2024-11-22 ChatGPT: [[Changes/ChatGPT/2024-11-22-recent-conversations-are-now-limited-in-the-sidebar-with-an-unlimited-infinite-s|Recent conversations are now limited in the sidebar, with an unlimited infinite]]
- 2024-11-24 Cursor: [[Changes/Cursor/2024-11-24-composer-ui-in-the-sidebar-with-inline-diffs|Composer UI in the sidebar with inline diffs]]
- 2025-02-19 Cursor: [[Changes/Cursor/2025-02-19-0-46-3-enhanced-download-reliability-fixed-keybinding-issue|0.46.3: Enhanced download reliability, fixed keybinding issue]]
- 2025-02-28 ChatGPT: [[Changes/ChatGPT/2025-02-28-the-temporary-chat-icon-is-now-in-top-bar-to-make-the-temporary-chat-experience|The temporary chat icon is now in top bar to make the temporary chat experience]]
- 2025-03-18 ChatGPT: [[Changes/ChatGPT/2025-03-18-added-long-press-on-your-message-to-open-menu-actions-copy-edit|Added long press on your message to open menu actions: Copy, Edit.]]
- 2025-03-18 ChatGPT: [[Changes/ChatGPT/2025-03-18-improved-response-display-of-nested-blockquote-content|Improved response display of nested blockquote content.]]
- 2025-03-23 Cursor: [[Changes/Cursor/2025-03-23-the-vertical-sidebar-option-will-temporarily-be-unavailable-for-users-who-opted|The vertical sidebar option will temporarily be unavailable for users who opted]]
- 2025-04-15 Cursor: [[Changes/Cursor/2025-04-15-more-accessible-history|More accessible history]]
- 2025-05-06 ChatGPT: [[Changes/ChatGPT/2025-05-06-no-tools-are-deprecated-access-is-simply-consolidated-to-clear-space-and-reduce|No tools are deprecated—access is simply consolidated to clear space and reduce]]
- 2025-09-16 ChatGPT: [[Changes/ChatGPT/2025-09-16-formatting-answers-are-better-formatted-for-quick-understanding-without-losing-d|Formatting: Answers are better formatted for quick understanding without losing]]
- 2025-09-29 Cursor: [[Changes/Cursor/2025-09-29-autocomplete-for-agent|Autocomplete for Agent]]
- 2025-10-29 Cursor: [[Changes/Cursor/2025-10-29-manage-agents-in-our-new-editor-with-a-sidebar-for-your-agents-and-plans|Manage agents in our new editor, with a sidebar for your agents and plans.]]
- 2025-11-21 Cursor: [[Changes/Cursor/2025-11-21-you-can-also-f-to-search-inside-generated-plans|You can also ⌘+F to search inside generated plans.]]
- 2025-12-10 Cursor: [[Changes/Cursor/2025-12-10-design-and-code-simultaneously-with-a-brand-new-browser-sidebar-and-component-tr|Design and code simultaneously with a brand new browser sidebar and component tr]]
- 2025-12-19 Claude Code: [[Changes/Claude Code/2025-12-19-added-syntax-highlighting-info-to-theme-picker|Added syntax highlighting info to theme picker]]
- 2025-12-19 Claude Code: [[Changes/Claude Code/2025-12-19-added-ctrl-t-shortcut-in-theme-to-toggle-syntax-highlighting-on-off|Added ctrl+t shortcut in `/theme` to toggle syntax highlighting on/off]]
- 2025-12-19 Claude Code: [[Changes/Claude Code/2025-12-19-added-alt-y-yank-pop-to-cycle-through-kill-ring-history-after-ctrl-y-yank|Added alt-y yank-pop to cycle through kill ring history after ctrl-y yank]]
- 2025-12-19 Claude Code: [[Changes/Claude Code/2025-12-19-improved-theme-command-to-open-theme-picker-directly|Improved `/theme` command to open theme picker directly]]
- 2026-01-09 Claude Code: [[Changes/Claude Code/2026-01-09-added-release-channel-stable-or-latest-toggle-to-config|Added release channel (`stable` or `latest`) toggle to `/config`]]
- 2026-01-09 Claude Code: [[Changes/Claude Code/2026-01-09-improved-terminal-rendering-stability-by-preventing-uncontrolled-writes-from-cor|Improved terminal rendering stability by preventing uncontrolled writes from cor]]
- 2026-01-09 Claude Code: [[Changes/Claude Code/2026-01-09-added-shift-tab-keyboard-shortcut-in-plan-mode-to-quickly-select-auto-accept-edi|Added Shift+Tab keyboard shortcut in plan mode to quickly select "auto-accept ed]]
- 2026-01-13 Claude Code: [[Changes/Claude Code/2026-01-13-added-updates-section-to-doctor-showing-auto-update-channel-and-available-npm-ve|Added Updates section to `/doctor` showing auto-update channel and available npm]]
- 2026-01-14 Claude Code: [[Changes/Claude Code/2026-01-14-added-showturnduration-setting-to-hide-turn-duration-messages-e-g-cooked-for-1m|Added `showTurnDuration` setting to hide turn duration messages (e.g., "Cooked f]]
- 2026-01-20 Claude Code: [[Changes/Claude Code/2026-01-20-improved-backspace-to-delete-pasted-text-as-a-single-token-instead-of-one-charac|Improved backspace to delete pasted text as a single token instead of one charac]]
- 2026-01-27 Claude Code: [[Changes/Claude Code/2026-01-27-added-pr-review-status-indicator-to-the-prompt-footer-showing-the-current-branch|Added PR review status indicator to the prompt footer, showing the current branc]]
- 2026-01-27 Claude Code: [[Changes/Claude Code/2026-01-27-added-arrow-key-history-navigation-in-vim-normal-mode-when-cursor-cannot-move-fu|Added arrow key history navigation in vim normal mode when cursor cannot move fu]]
- 2026-01-28 Claude Code: [[Changes/Claude Code/2026-01-28-improved-read-search-progress-indicators-to-show-reading-while-in-progress-and-r|Improved read/search progress indicators to show "Reading…" while in progress an]]
- 2026-01-29 Claude Code: [[Changes/Claude Code/2026-01-29-improved-terminal-rendering-performance-with-optimized-screen-data-layout|Improved terminal rendering performance with optimized screen data layout]]
- 2026-01-29 Claude Code: [[Changes/Claude Code/2026-01-29-added-customizable-spinner-verbs-setting-spinnerverbs|Added customizable spinner verbs setting (`spinnerVerbs`)]]
- 2026-01-29 Claude Code: [[Changes/Claude Code/2026-01-29-changed-merged-pull-requests-to-show-a-purple-status-indicator-in-the-prompt-foo|Changed merged pull requests to show a purple status indicator in the prompt foo]]
- 2026-01-30 ChatGPT: [[Changes/ChatGPT/2026-01-30-responses-in-chatgpt-are-now-more-visual-and-easier-to-scan-for-everyday-questio|Responses in ChatGPT are now more visual and easier to scan. For everyday questi]]
- 2026-02-06 Claude Code: [[Changes/Claude Code/2026-02-06-improved-error-messages-for-api-connection-failures-now-shows-specific-cause-e-g|Improved error messages for API connection failures — now shows specific cause (]]
- 2026-02-10 ChatGPT: [[Changes/ChatGPT/2026-02-10-we-re-introducing-improvements-to-deep-research-in-chatgpt-to-help-produce-more|We’re introducing improvements to deep research in ChatGPT to help produce more]]
- 2026-02-10 Claude Code: [[Changes/Claude Code/2026-02-10-improved-terminal-rendering-performance|Improved terminal rendering performance]]
- 2026-02-13 ChatGPT: [[Changes/ChatGPT/2026-02-13-quick-tools-in-the-composer-a-new-quick-tools-menu-in-the-message-composer-makes|Quick tools in the composer. A new quick-tools menu in the message composer make]]
- 2026-02-13 ChatGPT: [[Changes/ChatGPT/2026-02-13-simplified-composer-the-message-composer-has-been-streamlined-to-reduce-visual-c|Simplified composer. The message composer has been streamlined to reduce visual]]
- 2026-02-13 Claude Code: [[Changes/Claude Code/2026-02-13-improved-narrow-terminal-layout-for-prompt-footer|Improved narrow terminal layout for prompt footer]]
- 2026-02-17 Claude Code: [[Changes/Claude Code/2026-02-17-added-spinnertipsoverride-setting-to-customize-spinner-tips-configure-tips-with|Added `spinnerTipsOverride` setting to customize spinner tips — configure `tips`]]
- 2026-02-18 Cursor: [[Changes/Cursor/2026-02-18-typing-plan-takes-you-back-to-your-current-plan-and-its-action-menu-we-ve-also-a|Typing /plan takes you back to your current plan and its action menu. We've also]]
- 2026-02-18 Cursor: [[Changes/Cursor/2026-02-18-this-release-introduces-the-ability-to-hand-off-plans-from-the-cli-to-the-cloud|This release introduces the ability to hand off plans from the CLI to the cloud,]]
- 2026-02-26 Claude Code: [[Changes/Claude Code/2026-02-26-improved-ordering-of-short-task-lists|Improved ordering of short task lists]]
- 2026-02-26 Claude Code: [[Changes/Claude Code/2026-02-26-added-copy-command-to-show-an-interactive-picker-when-code-blocks-are-present-al|Added `/copy` command to show an interactive picker when code blocks are present]]
- 2026-02-27 ChatGPT: [[Changes/ChatGPT/2026-02-27-automatic-scroll-to-latest-message-existing-conversations-now-automatically-scro|Automatic scroll to latest message. Existing conversations now automatically scr]]
- 2026-03-05 Claude Code: [[Changes/Claude Code/2026-03-05-added-numeric-keypad-support-for-selecting-options-in-claude-s-interview-questio|Added numeric keypad support for selecting options in Claude's interview questio]]
- 2026-03-10 Claude Code: [[Changes/Claude Code/2026-03-10-added-w-key-in-copy-to-write-the-focused-selection-directly-to-a-file-bypassing|Added `w` key in `/copy` to write the focused selection directly to a file, bypa]]
- 2026-03-11 Claude Code: [[Changes/Claude Code/2026-03-11-improved-up-arrow-after-interrupting-claude-now-restores-the-interrupted-prompt|Improved Up arrow after interrupting Claude — now restores the interrupted promp]]
- 2026-03-11 Claude Code: [[Changes/Claude Code/2026-03-11-added-modeloverrides-setting-to-map-model-picker-entries-to-custom-provider-mode|Added `modelOverrides` setting to map model picker entries to custom provider mo]]
- 2026-03-17 ChatGPT: [[Changes/ChatGPT/2026-03-17-the-auto-functionality-can-be-accessed-by-clicking-configure-in-the-model-picker|The Auto functionality can be accessed by clicking Configure in the model picker]]
- 2026-03-17 Claude Code: [[Changes/Claude Code/2026-03-17-copy-now-accepts-an-optional-index-copy-n-copies-the-nth-latest-assistant-respon|`/copy` now accepts an optional index: `/copy N` copies the Nth-latest assistant]]
- 2026-03-17 Claude Code: [[Changes/Claude Code/2026-03-17-response-text-now-streams-line-by-line-as-it-s-generated|Response text now streams line-by-line as it's generated]]
- 2026-03-18 Claude Code: [[Changes/Claude Code/2026-03-18-added-show-turn-duration-toggle-to-the-config-menu|Added "Show turn duration" toggle to the `/config` menu]]
- 2026-03-19 Claude Code: [[Changes/Claude Code/2026-03-19-added-rate-limits-field-to-statusline-scripts-for-displaying-claude-ai-rate-limi|Added `rate_limits` field to statusline scripts for displaying Claude.ai rate li]]
- 2026-04-01 Claude Code: [[Changes/Claude Code/2026-04-01-added-claude-code-no-flicker-1-environment-variable-to-opt-into-flicker-free-alt|Added `CLAUDE_CODE_NO_FLICKER=1` environment variable to opt into flicker-free a]]
- 2026-04-04 Claude Code: [[Changes/Claude Code/2026-04-04-release-notes-is-now-an-interactive-version-picker|`/release-notes` is now an interactive version picker]]
- 2026-04-08 Claude Code: [[Changes/Claude Code/2026-04-08-added-refreshinterval-status-line-setting-to-re-run-the-status-line-command-ever|Added `refreshInterval` status line setting to re-run the status line command ev]]
- 2026-04-10 Claude Code: [[Changes/Claude Code/2026-04-10-improved-focus-mode-claude-now-writes-more-self-contained-summaries-since-it-kno|Improved focus mode: Claude now writes more self-contained summaries since it kn]]
- 2026-04-13 Cursor: [[Changes/Cursor/2026-04-13-expand-panes-to-focus-on-a-conversation-drag-agents-into-tiles-and-use-keybindin|Expand panes to focus on a conversation, drag agents into tiles, and use keybind]]
- 2026-04-13 Cursor: [[Changes/Cursor/2026-04-13-tiled-layout|Tiled layout]]
- 2026-04-14 Claude Code: [[Changes/Claude Code/2026-04-14-undo-is-now-an-alias-for-rewind|`/undo` is now an alias for `/rewind`]]
- 2026-04-14 Claude Code: [[Changes/Claude Code/2026-04-14-show-thinking-hints-sooner-during-long-operations|Show thinking hints sooner during long operations]]
- 2026-04-15 Claude Code: [[Changes/Claude Code/2026-04-15-added-autoscrollenabled-config-to-disable-conversation-auto-scroll-in-fullscreen|Added `autoScrollEnabled` config to disable conversation auto-scroll in fullscre]]
- 2026-04-15 Claude Code: [[Changes/Claude Code/2026-04-15-added-tui-command-and-tui-setting-run-tui-fullscreen-to-switch-to-flicker-free-r|Added `/tui` command and `tui` setting — run `/tui fullscreen` to switch to flic]]
- 2026-04-15 Claude Code: [[Changes/Claude Code/2026-04-15-improved-the-extended-thinking-indicator-with-a-rotating-progress-hint|Improved the extended-thinking indicator with a rotating progress hint]]
- 2026-04-16 Claude Code: [[Changes/Claude Code/2026-04-16-effort-now-opens-an-interactive-slider-when-called-without-arguments-with-arrow|`/effort` now opens an interactive slider when called without arguments, with ar]]
- 2026-04-17 Claude Code: [[Changes/Claude Code/2026-04-17-fullscreen-mode-shift-now-scrolls-the-viewport-when-extending-a-selection-past-t|Fullscreen mode: Shift+↑/↓ now scrolls the viewport when extending a selection p]]
- 2026-04-17 Claude Code: [[Changes/Claude Code/2026-04-17-windows-ctrl-backspace-now-deletes-the-previous-word|Windows: `Ctrl+Backspace` now deletes the previous word]]
- 2026-04-17 Claude Code: [[Changes/Claude Code/2026-04-17-ctrl-a-and-ctrl-e-now-move-to-the-start-end-of-the-current-logical-line-in-multi|`Ctrl+A` and `Ctrl+E` now move to the start/end of the current logical line in m]]
- 2026-04-20 Claude Code: [[Changes/Claude Code/2026-04-20-thinking-spinner-now-shows-progress-inline-still-thinking-thinking-more-almost-d|Thinking spinner now shows progress inline ("still thinking", "thinking more", "]]
- 2026-04-20 Claude Code: [[Changes/Claude Code/2026-04-20-smoother-fullscreen-scrolling-in-vs-code-cursor-and-windsurf-terminals-terminal|Smoother fullscreen scrolling in VS Code, Cursor, and Windsurf terminals — `/ter]]
- 2026-04-23 Claude Code: [[Changes/Claude Code/2026-04-23-added-vim-visual-mode-v-and-visual-line-mode-v-with-selection-operators-and-visu|Added vim visual mode (`v`) and visual-line mode (`V`) with selection, operators]]
- 2026-04-23 Claude Code: [[Changes/Claude Code/2026-04-23-added-claude-code-hide-cwd-environment-variable-to-hide-the-working-directory-in|Added `CLAUDE_CODE_HIDE_CWD` environment variable to hide the working directory]]
- 2026-04-28 Claude Code: [[Changes/Claude Code/2026-04-28-added-a-type-to-filter-search-box-to-skills-so-you-can-find-a-skill-in-long-list|Added a type-to-filter search box to `/skills` so you can find a skill in long l]]
- 2026-04-28 Claude Code: [[Changes/Claude Code/2026-04-28-fullscreen-mode-typing-into-the-prompt-no-longer-jumps-scroll-back-to-the-bottom|Fullscreen mode: typing into the prompt no longer jumps scroll back to the botto]]
- 2026-05-04 Claude Code: [[Changes/Claude Code/2026-05-04-bare-color-no-args-now-picks-a-random-session-color|Bare `/color` (no args) now picks a random session color]]
- 2026-05-06 Claude Code: [[Changes/Claude Code/2026-05-06-added-claude-code-force-sync-output-1-env-var-to-force-enable-synchronized-outpu|Added `CLAUDE_CODE_FORCE_SYNC_OUTPUT=1` env var to force-enable synchronized out]]
- 2026-05-06 Claude Code: [[Changes/Claude Code/2026-05-06-added-claude-code-disable-alternate-screen-1-env-var-to-opt-out-of-the-fullscree|Added `CLAUDE_CODE_DISABLE_ALTERNATE_SCREEN=1` env var to opt out of the fullscr]]
- 2026-05-06 Claude Code: [[Changes/Claude Code/2026-05-06-added-a-pasting-footer-hint-while-a-ctrl-v-image-paste-is-being-read-from-the-cl|Added a "Pasting…" footer hint while a Ctrl+V image paste is being read from the]]
- 2026-05-07 Claude Code: [[Changes/Claude Code/2026-05-07-improved-focus-mode-behavior|Improved focus mode behavior]]
- 2026-05-07 Cursor: [[Changes/Cursor/2026-05-07-the-changes-tab-makes-it-easier-to-navigate-larger-prs-with-a-file-tree-and-chan|The Changes tab makes it easier to navigate larger PRs with a file tree and chan]]
- 2026-05-11 Claude Code: [[Changes/Claude Code/2026-05-11-added-transcript-view-navigation-for-keyboard-shortcuts-to-jump-between-user-pro|Added transcript view navigation: `?` for keyboard shortcuts, `{`/`}` to jump be]]
- 2026-05-13 Cursor: [[Changes/Cursor/2026-05-13-full-screen-maximizes-the-right-panel-so-you-can-focus-on-a-single-tab|Full screen maximizes the right panel so you can focus on a single tab.]]
- 2026-05-13 Cursor: [[Changes/Cursor/2026-05-13-enter-and-exit-full-screen-by-clicking-on-the-expand-contract-button-in-the-pane|Enter and exit full screen by clicking on the expand/contract button in the pane]]
- 2026-05-13 Cursor: [[Changes/Cursor/2026-05-13-full-screen-tabs|Full-screen tabs]]
- 2026-05-19 Claude Code: [[Changes/Claude Code/2026-05-19-status-line-json-input-now-includes-github-repo-and-pr-information-when-detected|Status line JSON input now includes GitHub repo and PR information when detected]]
- 2026-05-19 Claude Code: [[Changes/Claude Code/2026-05-19-model-now-changes-the-model-for-the-current-session-only-press-d-in-the-model-pi|`/model` now changes the model for the current session only; press `d` in the mo]]
- 2026-05-21 Claude Code: [[Changes/Claude Code/2026-05-21-prompt-history-no-longer-records-consecutive-duplicate-entries-recalling-a-promp|Prompt history no longer records consecutive duplicate entries — recalling a pro]]
- 2026-05-22 Claude Code: [[Changes/Claude Code/2026-05-22-markdown-output-now-renders-gfm-task-list-checkboxes-todo-x-done-instead-of-plai|Markdown output now renders GFM task list checkboxes (`- [ ] todo` / `- [x] done]]
- 2026-05-28 Claude Code: [[Changes/Claude Code/2026-05-28-claude-agents-autocomplete-in-the-dispatch-input-now-suggests-native-slash-comma|`claude agents`: autocomplete in the dispatch input now suggests native slash co]]
- 2026-06-02 Claude Code: [[Changes/Claude Code/2026-06-02-fullscreen-mode-clipboard-now-uses-wl-copy-xclip-xsel-on-linux-when-available-co|Fullscreen mode: clipboard now uses `wl-copy`/`xclip`/`xsel` on Linux when avail]]
- 2026-06-03 Claude Code: [[Changes/Claude Code/2026-06-03-clicking-a-slash-command-in-the-autocomplete-menu-now-fills-it-into-your-prompt|Clicking a slash command in the autocomplete menu now fills it into your prompt]]
- 2026-06-04 Claude Code: [[Changes/Claude Code/2026-06-04-added-a-c-to-copy-shortcut-to-btw-that-copies-the-raw-markdown-answer-to-the-cli|Added a "c to copy" shortcut to `/btw` that copies the raw markdown answer to th]]
- 2026-06-05 Cursor: [[Changes/Cursor/2026-06-05-multi-select-elements|Multi-select elements]]
- 2026-06-08 ChatGPT: [[Changes/ChatGPT/2026-06-08-improvement-to-charts-table-of-contents-and-full-screen-writing-also-fixes-long|Improvement to charts, table of contents and full screen writing. Also fixes lon]]
- 2026-06-08 ChatGPT: [[Changes/ChatGPT/2026-06-08-table-of-contents-in-longer-conversations-conversations-longer-than-five-respons|Table of contents in longer conversations: Conversations longer than five respon]]
- 2026-06-10 ChatGPT: [[Changes/ChatGPT/2026-06-10-we-re-updating-the-model-picker-to-make-it-easier-to-choose-the-balance-of-speed|We’re updating the model picker to make it easier to choose the balance of speed]]
- 2026-06-12 Claude Code: [[Changes/Claude Code/2026-06-12-added-footerlinksregexes-setting-for-regex-matched-link-badges-in-the-footer-row|Added `footerLinksRegexes` setting for regex-matched link badges in the footer r]]
- 2026-06-12 Claude Code: [[Changes/Claude Code/2026-06-12-added-wheelscrollaccelerationenabled-setting-to-disable-mouse-wheel-scroll-accel|Added `wheelScrollAccelerationEnabled` setting to disable mouse-wheel scroll acc]]
- 2026-06-17 ChatGPT: [[Changes/ChatGPT/2026-06-17-a-new-scheduled-page-discoverable-in-the-sidebar-gives-users-one-place-to-view-a|A new Scheduled page, discoverable in the sidebar, gives users one place to view]]
- 2026-06-17 Claude Code: [[Changes/Claude Code/2026-06-17-improved-streaming-of-long-paragraphs-text-now-appears-line-by-line-instead-of-w|Improved streaming of long paragraphs: text now appears line-by-line instead of]]
- 2026-06-19 Claude Code: [[Changes/Claude Code/2026-06-19-added-config-help-to-list-all-available-shorthand-keys-for-config-key-value|Added `/config --help` to list all available shorthand keys for `/config key=val]]
- 2026-06-19 Claude Code: [[Changes/Claude Code/2026-06-19-changed-config-toggle-behavior-enter-and-space-both-change-the-selected-setting|Changed `/config` toggle behavior: Enter and Space both change the selected sett]]
- 2026-06-23 Claude Code: [[Changes/Claude Code/2026-06-23-added-org-configured-model-restrictions-to-the-model-picker-model-model-and-anth|Added org-configured model restrictions to the model picker, `--model`, `/model`]]
- 2026-06-23 Claude Code: [[Changes/Claude Code/2026-06-23-improved-btw-with-arrow-navigation-to-step-through-earlier-answers|Improved `/btw` with ←/→ arrow navigation to step through earlier answers]]
- 2026-06-26 Claude Code: [[Changes/Claude Code/2026-06-26-added-claude-code-disable-mouse-clicks-to-disable-mouse-click-drag-hover-in-full|Added `CLAUDE_CODE_DISABLE_MOUSE_CLICKS` to disable mouse click/drag/hover in fu]]
- 2026-07-03 Claude Code: [[Changes/Claude Code/2026-07-03-changed-askuserquestion-dialogs-to-no-longer-auto-continue-by-default-opt-into-a|Changed `AskUserQuestion` dialogs to no longer auto-continue by default; opt int]]
- 2026-07-10 Cursor: [[Changes/Cursor/2026-07-10-conversation-search|Conversation search]]
- 2026-07-11 Claude Code: [[Changes/Claude Code/2026-07-11-improved-agent-view-pasting-the-same-text-again-now-expands-the-collapsed-pasted|Improved agent view: pasting the same text again now expands the collapsed `[Pas]]
- 2026-07-14 ChatGPT: [[Changes/ChatGPT/2026-07-14-start-searching-from-the-chatgpt-sidebar-to-find-what-you-need-across-everything|Start searching from the ChatGPT sidebar to find what you need across everything]]
- 2026-07-14 Claude Code: [[Changes/Claude Code/2026-07-14-added-mouse-click-support-for-multi-select-menus-and-other-input-rows-in-fullscr|Added mouse-click support for multi-select menus and "Other" input rows in fulls]]
- 2026-07-14 Claude Code: [[Changes/Claude Code/2026-07-14-added-a-live-elapsed-time-counter-to-the-collapsed-tool-summary-line-so-long-run|Added a live elapsed-time counter to the collapsed tool summary line so long-run]]
- 2026-07-15 Claude Code: [[Changes/Claude Code/2026-07-15-improved-terminal-layout-and-rendering-performance|Improved terminal layout and rendering performance]]
- 2026-07-17 Cursor: [[Changes/Cursor/2026-07-17-interaction-improvements|Interaction improvements]]
- 2026-07-28 Cursor: [[Changes/Cursor/2026-07-28-existing-free-users-in-india-can-upgrade-their-plan-from-the-dashboard-new-users|Existing Free users in India can upgrade their plan from the dashboard. New user]]
<!-- chronolog:end -->