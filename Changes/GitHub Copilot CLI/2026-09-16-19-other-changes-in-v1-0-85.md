---
card_id: github-copilot-cli-2026-09-16-354020
date: '2026-09-16'
description: 'GitHub Copilot CLI · 2026-09-16 · Other changes: 19 changes in 1.0.85
  — Set transcriptView to "concise" to group tool activity into expandable work summaries.'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 97bfb75ed5004b86ee8506f2dd388a5dc96d3083cda270cf6160893560fd3cef
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-09-16-354020
  comparison: ''
  date: '2026-09-16'
  description: 'GitHub Copilot CLI — 1.0.85: 19 other changes'
  evidence:
  - quote: Set transcriptView to "concise" to group tool activity into expandable
      work summaries.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  - quote: --add-dir rejects non-directory and inaccessible paths uniformly and aborts
      startup before session initialization
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  - quote: Failed new-session handoffs stop unused clients from polling and preserve
      the current session, schedules, and unsent prompt.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  - quote: Modified chords such as Ctrl+X, Alt+X or capital X no longer trigger the
      /tasks letter shortcuts; only unmodified a, f, x, r, b, j and k respond. Enter,
      Escape, the arrow keys and Ctrl+G / Ctrl+P / Ctrl+N are unaffected
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  - quote: Scheduled prompts show an error when they fail at runtime
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  - quote: CLI retries image prompts without images when providers reject image-limit
      requests
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  - quote: Skills from directories added with --add-dir are no longer missing when
      a skills load races the directory registration
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  - quote: Scrolling the wheel with mouse capture off no longer walks backwards through
      prompt history in terminals that report DEC private mode 1007 (alternate scroll),
      such as Ghostty
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  - quote: Windows CLI artifacts run without requiring the Visual C++ Redistributable
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  - quote: Keep long /ask responses visible after generation completes
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  - quote: Streaming responses preserve message chunk ordering before final output.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  - quote: The remote session timeline entry now advertises ctrl+o to show or hide
      the QR code, matching the key that actually toggles it
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  - quote: Interactive mode starts and submits the initial prompt when using --auth-token-env
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  - quote: Use /settings taskbarPresence false to disable Windows taskbar session
      status. Loader-managed sessions restart immediately; standalone sessions require
      a manual restart.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  - quote: Initial prompts start immediately for Entra-authenticated sessions while
      token refresh runs in the background.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  - quote: Choosing approve-for-location now persists tool approval to avoid repeat
      prompts
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  - quote: Sandboxed runs now use relocated developer-tool caches from env vars and
      tool config files
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  - quote: Show active scheduled prompts in the CLI footer by default
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  - quote: Show trust status, tier, and eligibility details for online resource catalogue
      results
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 19-other-changes-in-v1-0-85
  source_release: github-copilot-cli-2026-09-16-v1-0-85-github-389603482-889a46d9
  source_type: github_releases
  theme: uncategorized
  title: 19 other changes in v1.0.85
  type: change
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-09-16-v1-0-85-github-389603482-889a46d9|github-copilot-cli-2026-09-16-v1-0-85-github-389603482-889a46d9]]'
source_type: github_releases
theme: uncategorized
title: 19 other changes in v1.0.85
type: change
---

<!-- chronolog:begin region="header" -->
# 19 other changes in v1.0.85

**GitHub Copilot CLI** · 2026-09-16 · Other changes · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.85) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-09-16-v1-0-85-github-389603482-889a46d9|1.0.85]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Set transcriptView to "concise" to group tool activity into expandable work summaries.

> --add-dir rejects non-directory and inaccessible paths uniformly and aborts startup before session initialization

> Failed new-session handoffs stop unused clients from polling and preserve the current session, schedules, and unsent prompt.

> Modified chords such as Ctrl+X, Alt+X or capital X no longer trigger the /tasks letter shortcuts; only unmodified a, f, x, r, b, j and k respond. Enter, Escape, the arrow keys and Ctrl+G / Ctrl+P / Ctrl+N are unaffected

> Scheduled prompts show an error when they fail at runtime

> CLI retries image prompts without images when providers reject image-limit requests

> Skills from directories added with --add-dir are no longer missing when a skills load races the directory registration

> Scrolling the wheel with mouse capture off no longer walks backwards through prompt history in terminals that report DEC private mode 1007 (alternate scroll), such as Ghostty

> Windows CLI artifacts run without requiring the Visual C++ Redistributable

> Keep long /ask responses visible after generation completes

> Streaming responses preserve message chunk ordering before final output.

> The remote session timeline entry now advertises ctrl+o to show or hide the QR code, matching the key that actually toggles it

> Interactive mode starts and submits the initial prompt when using --auth-token-env

> Use /settings taskbarPresence false to disable Windows taskbar session status. Loader-managed sessions restart immediately; standalone sessions require a manual restart.

> Initial prompts start immediately for Entra-authenticated sessions while token refresh runs in the background.

> Choosing approve-for-location now persists tool approval to avoid repeat prompts

> Sandboxed runs now use relocated developer-tool caches from env vars and tool config files

> Show active scheduled prompts in the CLI footer by default

> Show trust status, tier, and eligibility details for online resource catalogue results

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.85
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-09-16-4-account-and-access-changes-in-v1-0-85|4 Account and Access changes in v1.0.85]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-09-16-6-developer-workflow-changes-in-v1-0-85|6 Developer Workflow changes in v1.0.85]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-09-16-9-editor-experience-changes-in-v1-0-85|9 Editor Experience changes in v1.0.85]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-09-16-speed-up-startup-when-resuming-an-existing-local-session-by-its-exact-uuid-with|Speed up startup when resuming an existing local session by its exact UUID with --resume]] · Reliability and Performance
- [[Changes/GitHub Copilot CLI/2026-09-16-17-safety-and-privacy-changes-in-v1-0-85|17 Safety and Privacy changes in v1.0.85]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-09-16-13-model-support-changes-in-v1-0-85|13 Model Support changes in v1.0.85]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-09-16-usage-shows-per-model-ai-credit-consumption-in-usage-breakdowns|/usage shows per-model AI Credit consumption in usage breakdowns]] · Pricing Model
- [[Changes/GitHub Copilot CLI/2026-09-16-3-memory-and-personalization-changes-in-v1-0-85|3 Memory and Personalization changes in v1.0.85]] · Memory and Personalization
- [[Changes/GitHub Copilot CLI/2026-09-16-4-mobile-and-desktop-changes-in-v1-0-85|4 Mobile and Desktop changes in v1.0.85]] · Mobile and Desktop
- [[Changes/GitHub Copilot CLI/2026-09-16-add-json-to-copilot-plugin-list-copilot-plugin-marketplace-list-and-copilot-plug|Add --json to copilot plugin list, copilot plugin marketplace list…]] · Search and Browsing
- [[Changes/GitHub Copilot CLI/2026-09-16-3-context-window-changes-in-v1-0-85|3 Context Window changes in v1.0.85]] · Context Window
- [[Changes/GitHub Copilot CLI/2026-09-16-2-agent-mode-changes-in-v1-0-85|2 Agent Mode changes in v1.0.85]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-09-16-20-apps-and-integrations-changes-in-v1-0-85|20 Apps and Integrations changes in v1.0.85]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-09-16-share-notes-md-now-writes-the-exported-session-to-your-home-directory-instead-of|--share=~/notes.md now writes the exported session to your home directory instead…]] · Collaboration
- [[Changes/GitHub Copilot CLI/2026-09-16-when-session-history-is-truncated-or-compacted-just-as-a-turn-finishes-the-worki|When session history is truncated or compacted just as a turn finishes…]] · Projects and Workspaces
- [[Changes/GitHub Copilot CLI/2026-09-16-3-interface-experience-changes-in-v1-0-85|3 Interface Experience changes in v1.0.85]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-09-16-vim-mode-is-now-available-to-everyone-turn-it-on-with-vim-or-by-setting-editormo|Vim mode is now available to everyone]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-09-16-354020&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-09-16-19-other-changes-in-v1-0-85.md%0ACard%20ID%3A%20github-copilot-cli-2026-09-16-354020%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.85%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->