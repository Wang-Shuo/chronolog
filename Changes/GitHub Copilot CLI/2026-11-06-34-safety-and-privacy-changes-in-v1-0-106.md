---
card_id: github-copilot-cli-2026-11-06-5f59c4
date: '2026-11-06'
description: 'GitHub Copilot CLI · 2026-11-06 · Safety and Privacy: 34 changes in
  1.0.106 — Add a Sandbox extensions setting to run extension processes inside the
  sandbox'
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke
    Application Access]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2292
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 523d45fdc6f1eb3ba8eb137c35382dc745ec9bbab7e2c357a7a1588b3b388d4c
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-11-06-5f59c4
  comparison: ''
  date: '2026-11-06'
  description: 'GitHub Copilot CLI — 1.0.106: 34 Safety and Privacy changes'
  evidence:
  - quote: Add a Sandbox extensions setting to run extension processes inside the
      sandbox
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: The footer keeps the "N scheduled", sandbox, YOLO and CI status items whole
      on narrow terminals by shortening the directory and branch first, instead of
      cutting the items off the end of the row.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: LSP rename asks for every file's write permission before changing anything,
      so declining one file leaves all files untouched. It also no longer corrupts
      a file the language server lists more than once, keeps inserts at the same position
      in order, preserves bytes that are not valid UTF-8, and says when it skipped
      a file create, rename or delete
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: apply_patch no longer counts one extra line for each file it adds or deletes,
      so the timeline summary, permission prompt, /usage and exit summary show the
      real line counts
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Managed sandbox policy errors now tell you to contact your administrator
      and include the failed sandbox test command when it cannot start.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Unchanged cached MCP tools remain callable when another tool refreshes
      while permission is pending
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: File diffs in permission prompts and /diff show control characters from
      the file as visible symbols instead of letting escape sequences restyle or hide
      lines.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: On narrow terminals the footer no longer leaves a stray separator where
      a hint did not fit or cuts the permission mode mid-name.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: A hook's permission message and the reason a hook queues as the next message
      no longer pass escape sequences to the terminal, so they cannot hide text or
      start a link in the hook prompt or the queued-message list.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Shell safety warnings no longer appear twice in the timeline during command
      approvals.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: In `/sandbox`, pressing Enter right after Tab opens a folder in the add-path
      picker now keeps that folder, and Esc after Tab on an empty path cancels at
      once.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: The web fetch permission prompt shows control characters in the requested
      URL instead of letting escape sequences hide text, add a link or split the URL
      across lines.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Extensions no longer prompt for permission after their connection closes
      during initialization
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Permission prompts keep your current selection when options update during
      loading
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Permission prompts show the control characters in a directory or file name
      instead of letting its escape sequences restyle the path or its line feeds split
      the row
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: The `/permissions` picker keeps its title, the highlighted mode, the Assisted
      Permissions security statement and its key hints on screen on short terminals,
      such as 80x12 or 60x14, instead of pushing the title and the first modes above
      the top of the screen.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Typing `?` in Ctrl+R reverse search or at a permission prompt no longer
      opens quick help, and pressing it twice no longer leaves a stray `?` in the
      prompt.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: copilot --resume and --continue now fail at once with the permission error
      when the session store cannot be read, instead of printing nothing and never
      exiting.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: copilot sandbox ca trust --allow-host '\*' now reports an invalid host
      rule, like other invalid hosts, instead of an unrelated masked-credential error
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: 'The /sandbox dialog now fits short terminals: it keeps its title, its
      tabs, the highlighted setting and its key hints on screen and scrolls the settings
      instead of cutting them off.'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Fix URL permission prompts to keep ${VAR} placeholders in extracted URLs
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Detected az commands can access Azure CLI configuration in sandbox when
      allowDevToolAccess is enabled
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Linux and macOS ignore Windows-absolute deniedPaths, readonlyPaths, and
      readwritePaths entries in sandbox policies
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Sandbox proxy and runtime checks use allowLocalNetwork only for loopback;
      private-network destinations follow allowOutbound and host rules
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: /fleet, /research, /review, /rubber-duck, /security-review and /blame keep
      a multi-line prompt's line breaks, indentation and spacing instead of flattening
      it into one line
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Update permission failures include actionable reinstall and PATH guidance
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Read-only sandbox denials now correctly trigger bypass guidance for failed
      global installs.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Device-code sign-in no longer restarts after plaintext-storage consent
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Sandbox denials now recognize Go-style open and dial unix permission errors
      and suggest the correct path grant.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Rejecting one tool permission in a parallel batch now cancels sibling prompts
      and carries your feedback for replanning.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Sandbox onboarding now points to /sandbox policy for outbound network status
      instead of claiming access is allowed
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Support glob patterns in sandbox filesystem deny rules, resolved when each
      policy is built.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: /add-dir now explains that sandbox read-write grants are session-scoped,
      subject to managed-policy restrictions, and do not change saved sandbox settings
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Stop /sandbox from adding a read/write drive root such as C:\ as a path
      grant on Windows, because it doesn't give sandboxed commands access to the files
      inside it. Read-Only still works.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 34-safety-and-privacy-changes-in-v1-0-106
  source_release: github-copilot-cli-2026-11-06-v1-0-106-github-435988160-ec5b15d4
  source_type: github_releases
  theme: safety-privacy
  title: 34 Safety and Privacy changes in v1.0.106
  type: change
related_changes:
- '[[Changes/OpenClaw/2026-11-05-2-safety-and-privacy-changes-in-v2026-11-1|2 Safety
  and Privacy changes in v2026.11.1]]'
- '[[Changes/Qoder/2026-11-05-local-extension-installation-install-plugins-and-skills-by-dragging-or-pasting-f|Local
  extension installation: Install plugins and Skills by dragging or pasting files]]'
- '[[Changes/Codex CLI/2026-11-06-57985-skip-read-only-volume-root-expansion-in-the-mxc-sandbox-iceweasel-oai|♯57985
  Skip read-only volume-root expansion in the MXC sandbox @iceweasel-oai]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-11-06-v1-0-106-github-435988160-ec5b15d4|github-copilot-cli-2026-11-06-v1-0-106-github-435988160-ec5b15d4]]'
source_type: github_releases
theme: safety-privacy
title: 34 Safety and Privacy changes in v1.0.106
type: change
---

<!-- chronolog:begin region="header" -->
# 34 Safety and Privacy changes in v1.0.106

**GitHub Copilot CLI** · 2026-11-06 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.106) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-11-06-v1-0-106-github-435988160-ec5b15d4|1.0.106]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Add a Sandbox extensions setting to run extension processes inside the sandbox

> The footer keeps the "N scheduled", sandbox, YOLO and CI status items whole on narrow terminals by shortening the directory and branch first, instead of cutting the items off the end of the row.

> LSP rename asks for every file's write permission before changing anything, so declining one file leaves all files untouched. It also no longer corrupts a file the language server lists more than once, keeps inserts at the same position in order, preserves bytes that are not valid UTF-8, and says when it skipped a file create, rename or delete

> apply_patch no longer counts one extra line for each file it adds or deletes, so the timeline summary, permission prompt, /usage and exit summary show the real line counts

> Managed sandbox policy errors now tell you to contact your administrator and include the failed sandbox test command when it cannot start.

> Unchanged cached MCP tools remain callable when another tool refreshes while permission is pending

> File diffs in permission prompts and /diff show control characters from the file as visible symbols instead of letting escape sequences restyle or hide lines.

> On narrow terminals the footer no longer leaves a stray separator where a hint did not fit or cuts the permission mode mid-name.

> A hook's permission message and the reason a hook queues as the next message no longer pass escape sequences to the terminal, so they cannot hide text or start a link in the hook prompt or the queued-message list.

> Shell safety warnings no longer appear twice in the timeline during command approvals.

> In `/sandbox`, pressing Enter right after Tab opens a folder in the add-path picker now keeps that folder, and Esc after Tab on an empty path cancels at once.

> The web fetch permission prompt shows control characters in the requested URL instead of letting escape sequences hide text, add a link or split the URL across lines.

> Extensions no longer prompt for permission after their connection closes during initialization

> Permission prompts keep your current selection when options update during loading

> Permission prompts show the control characters in a directory or file name instead of letting its escape sequences restyle the path or its line feeds split the row

> The `/permissions` picker keeps its title, the highlighted mode, the Assisted Permissions security statement and its key hints on screen on short terminals, such as 80x12 or 60x14, instead of pushing the title and the first modes above the top of the screen.

> Typing `?` in Ctrl+R reverse search or at a permission prompt no longer opens quick help, and pressing it twice no longer leaves a stray `?` in the prompt.

> copilot --resume and --continue now fail at once with the permission error when the session store cannot be read, instead of printing nothing and never exiting.

> copilot sandbox ca trust --allow-host '\*' now reports an invalid host rule, like other invalid hosts, instead of an unrelated masked-credential error

> The /sandbox dialog now fits short terminals: it keeps its title, its tabs, the highlighted setting and its key hints on screen and scrolls the settings instead of cutting them off.

> Fix URL permission prompts to keep ${VAR} placeholders in extracted URLs

> Detected az commands can access Azure CLI configuration in sandbox when allowDevToolAccess is enabled

> Linux and macOS ignore Windows-absolute deniedPaths, readonlyPaths, and readwritePaths entries in sandbox policies

> Sandbox proxy and runtime checks use allowLocalNetwork only for loopback; private-network destinations follow allowOutbound and host rules

> /fleet, /research, /review, /rubber-duck, /security-review and /blame keep a multi-line prompt's line breaks, indentation and spacing instead of flattening it into one line

> Update permission failures include actionable reinstall and PATH guidance

> Read-only sandbox denials now correctly trigger bypass guidance for failed global installs.

> Device-code sign-in no longer restarts after plaintext-storage consent

> Sandbox denials now recognize Go-style open and dial unix permission errors and suggest the correct path grant.

> Rejecting one tool permission in a parallel batch now cancels sibling prompts and carries your feedback for replanning.

> Sandbox onboarding now points to /sandbox policy for outbound network status instead of claiming access is allowed

> Support glob patterns in sandbox filesystem deny rules, resolved when each policy is built.

> /add-dir now explains that sandbox read-write grants are session-scoped, subject to managed-policy restrictions, and do not change saved sandbox settings

> Stop /sandbox from adding a read/write drive root such as C:\ as a path grant on Windows, because it doesn't give sandboxed commands access to the files inside it. Read-Only still works.

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
- [[Changes/GitHub Copilot CLI/2026-11-06-23-account-and-access-changes-in-v1-0-106|23 Account and Access changes in v1.0.106]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-11-06-172-other-changes-in-v1-0-106|172 other changes in v1.0.106]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-11-06 · Codex CLI · [[Changes/Codex CLI/2026-11-06-57985-skip-read-only-volume-root-expansion-in-the-mxc-sandbox-iceweasel-oai|♯57985 Skip read-only volume-root expansion in the MXC sandbox @iceweasel-oai]]
- Later: 2026-11-06 · OpenCode · [[Changes/OpenCode/2026-11-06-3-safety-and-privacy-changes-in-v2-2-6|3 Safety and Privacy changes in v2.2.6]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Descript · [[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke Application Access]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-11-06-5f59c4&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-11-06-34-safety-and-privacy-changes-in-v1-0-106.md%0ACard%20ID%3A%20github-copilot-cli-2026-11-06-5f59c4%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.106%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->