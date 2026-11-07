---
card_id: github-copilot-cli-2026-09-16-a42574
date: '2026-09-16'
description: 'GitHub Copilot CLI · 2026-09-16 · Mobile and Desktop: 4 changes in 1.0.85
  — Restore keyboard input and screen output on macOS and Linux when you return from
  an…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-11-11-command-r-to-insert-a-speaker-label-ctrl-r-on-windows|command
    + R to insert a speaker label (ctrl + R on Windows)]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2866
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: mobile-desktop
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 1c9029f19f577362dbc32d6df282f04de029e52db9159616fb16b13bbc066b2a
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-09-16-a42574
  comparison: ''
  date: '2026-09-16'
  description: 'GitHub Copilot CLI — 1.0.85: 4 Mobile and Desktop changes'
  evidence:
  - quote: Restore keyboard input and screen output on macOS and Linux when you return
      from an external editor that reset the terminal
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  - quote: Indexed search on Windows prevents new disk-space leaks when updating indexes
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  - quote: Indexed search shows when enabled, works on Windows ReFS volumes, supports
      explicit cloud-sync overrides, and keeps refreshing on Linux when native file
      watches are exhausted.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  - quote: On Windows, a sandboxed command that runs git without naming it — a hook,
      a build tool, or an npm install that clones over HTTPS — no longer dies inside
      the credential helper's MSYS2 shell.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.85
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 4-mobile-and-desktop-changes-in-v1-0-85
  source_release: github-copilot-cli-2026-09-16-v1-0-85-github-389603482-889a46d9
  source_type: github_releases
  theme: mobile-desktop
  title: 4 Mobile and Desktop changes in v1.0.85
  type: change
related_changes:
- '[[Changes/Lovable/2026-09-15-connect-your-app-to-whatsapp-business|Connect your
  app to WhatsApp Business]]'
- '[[Changes/Ollama/2026-09-15-added-ollama-apps-to-open-the-desktop-app-s-apps-page-directly-on-macos-and-wind|Added
  ollama://apps to open the desktop app’s Apps page directly on macOS and Windows]]'
- '[[Changes/Windsurf/2026-09-15-devin-desktop|Devin Desktop]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-09-16-v1-0-85-github-389603482-889a46d9|github-copilot-cli-2026-09-16-v1-0-85-github-389603482-889a46d9]]'
source_type: github_releases
theme: mobile-desktop
title: 4 Mobile and Desktop changes in v1.0.85
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Mobile and Desktop changes in v1.0.85

**GitHub Copilot CLI** · 2026-09-16 · [[Themes/mobile-desktop|Mobile and Desktop]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.85) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-09-16-v1-0-85-github-389603482-889a46d9|1.0.85]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Restore keyboard input and screen output on macOS and Linux when you return from an external editor that reset the terminal

> Indexed search on Windows prevents new disk-space leaks when updating indexes

> Indexed search shows when enabled, works on Windows ReFS volumes, supports explicit cloud-sync overrides, and keeps refreshing on Linux when native file watches are exhausted.

> On Windows, a sandboxed command that runs git without naming it — a hook, a build tool, or an npm install that clones over HTTPS — no longer dies inside the credential helper's MSYS2 shell.

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
- [[Changes/GitHub Copilot CLI/2026-09-16-add-json-to-copilot-plugin-list-copilot-plugin-marketplace-list-and-copilot-plug|Add --json to copilot plugin list, copilot plugin marketplace list…]] · Search and Browsing
- [[Changes/GitHub Copilot CLI/2026-09-16-3-context-window-changes-in-v1-0-85|3 Context Window changes in v1.0.85]] · Context Window
- [[Changes/GitHub Copilot CLI/2026-09-16-2-agent-mode-changes-in-v1-0-85|2 Agent Mode changes in v1.0.85]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-09-16-20-apps-and-integrations-changes-in-v1-0-85|20 Apps and Integrations changes in v1.0.85]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-09-16-share-notes-md-now-writes-the-exported-session-to-your-home-directory-instead-of|--share=~/notes.md now writes the exported session to your home directory instead…]] · Collaboration
- [[Changes/GitHub Copilot CLI/2026-09-16-when-session-history-is-truncated-or-compacted-just-as-a-turn-finishes-the-worki|When session history is truncated or compacted just as a turn finishes…]] · Projects and Workspaces
- [[Changes/GitHub Copilot CLI/2026-09-16-3-interface-experience-changes-in-v1-0-85|3 Interface Experience changes in v1.0.85]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-09-16-19-other-changes-in-v1-0-85|19 other changes in v1.0.85]] · Other changes
- [[Changes/GitHub Copilot CLI/2026-09-16-vim-mode-is-now-available-to-everyone-turn-it-on-with-vim-or-by-setting-editormo|Vim mode is now available to everyone]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Mobile and Desktop

- Earlier: 2026-09-15 · Windsurf · [[Changes/Windsurf/2026-09-15-devin-desktop|Devin Desktop]]
- Later: 2026-09-16 · Windsurf · [[Changes/Windsurf/2026-09-16-devin-desktop|Devin Desktop]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-11-11 · Descript · [[Changes/Descript/2018-11-11-command-r-to-insert-a-speaker-label-ctrl-r-on-windows|command + R to insert a speaker label (ctrl + R on Windows)]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-09-16-a42574&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-09-16-4-mobile-and-desktop-changes-in-v1-0-85.md%0ACard%20ID%3A%20github-copilot-cli-2026-09-16-a42574%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.85%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->