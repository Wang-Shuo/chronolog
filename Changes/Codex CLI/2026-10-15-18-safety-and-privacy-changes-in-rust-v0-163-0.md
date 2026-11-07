---
card_id: codex-cli-2026-10-15-4b6afc
date: '2026-10-15'
description: 'Codex CLI · 2026-10-15 · Safety and Privacy: 18 changes in 0.163.0 —
  The network proxy now checks permission before a DNS lookup, rejects duplicate `Host`…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke
    Application Access]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2270
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: ef4760332d933dc36d7f0aa1c0e74b17b06ee3b55eb467fd72964c131d717ba7
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-10-15-4b6afc
  comparison: ''
  date: '2026-10-15'
  description: 'Codex CLI — 0.163.0: 18 Safety and Privacy changes'
  evidence:
  - quote: 'The network proxy now checks permission before a DNS lookup, rejects duplicate
      `Host` headers, and prevents credential aliases from bypassing inspection hooks.
      (#51650, #52661, #53506)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: Clarified how the Linux sandbox uses bubblewrap for filesystem isolation
      and seccomp for syscall filtering. (#52610)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#51547 Add a Windows MXC sandbox opt-out @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#51678 Move Windows sandbox tests into a dedicated integration binary
      @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#51786 Preserve sandbox overrides across execution requests @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#51819 Migrate the MXC sandbox to the 1.0.0 SDK @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#51831 Add MXC sandbox integrity dependency and policy preparation @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#51840 Add a bubblewrap backend for sandbox integrity checks @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#51841 Add a macOS Seatbelt backend for sandbox integrity @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#51842 Add a sandbox integrity runner with outcome and timing metrics
      @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#51843 Run sandbox integrity checks before commands and filesystem operations
      @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#51896 Preserve native errors in Windows sandbox ACL diagnostics @alishobeiri-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#51974 Log Windows sandbox availability and backend selection @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#52182 Expose a verified sandbox launcher to local MCP servers @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#52610 Align Linux sandbox names and docs with bubblewrap and seccomp
      @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#52682 Validate Windows sandbox accounts before password repair @zm-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#52707 Migrate the Windows MXC sandbox to split MXC crates @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  - quote: '#53709 Separate MCP sandbox policy from launcher metadata @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.163.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 18-safety-and-privacy-changes-in-rust-v0-163-0
  source_release: codex-cli-2026-10-15-rust-v0-163-0-github-414286110-97016fe6
  source_type: github_releases
  theme: safety-privacy
  title: 18 Safety and Privacy changes in rust-v0.163.0
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-10-14-resuming-a-session-now-respects-abandoned-pending-permission-work-and-continues|Resuming
  a session now respects abandoned pending-permission work and continues only…]]'
- "[[Changes/Open WebUI/2026-10-14-rich-ui-embed-console-errors-rich-ui-tool-embeds-no-longer-log-a-security-error|\U0001F9E9
  Rich UI embed console errors. Rich UI tool embeds no longer log a security…]]"
- '[[Changes/Claude Code/2026-10-15-5-safety-and-privacy-changes-in-v2-1-301|5 Safety
  and Privacy changes in v2.1.301]]'
source_release: '[[Releases/Codex CLI/codex-cli-2026-10-15-rust-v0-163-0-github-414286110-97016fe6|codex-cli-2026-10-15-rust-v0-163-0-github-414286110-97016fe6]]'
source_type: github_releases
theme: safety-privacy
title: 18 Safety and Privacy changes in rust-v0.163.0
type: change
---

<!-- chronolog:begin region="header" -->
# 18 Safety and Privacy changes in rust-v0.163.0

**Codex CLI** · 2026-10-15 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.163.0) · from [[Releases/Codex CLI/codex-cli-2026-10-15-rust-v0-163-0-github-414286110-97016fe6|0.163.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> The network proxy now checks permission before a DNS lookup, rejects duplicate `Host` headers, and prevents credential aliases from bypassing inspection hooks. (#51650, #52661, #53506)

> Clarified how the Linux sandbox uses bubblewrap for filesystem isolation and seccomp for syscall filtering. (#52610)

> #51547 Add a Windows MXC sandbox opt-out @iceweasel-oai

> #51678 Move Windows sandbox tests into a dedicated integration binary @jif-oai

> #51786 Preserve sandbox overrides across execution requests @iceweasel-oai

> #51819 Migrate the MXC sandbox to the 1.0.0 SDK @iceweasel-oai

> #51831 Add MXC sandbox integrity dependency and policy preparation @iceweasel-oai

> #51840 Add a bubblewrap backend for sandbox integrity checks @iceweasel-oai

> #51841 Add a macOS Seatbelt backend for sandbox integrity @iceweasel-oai

> #51842 Add a sandbox integrity runner with outcome and timing metrics @iceweasel-oai

> #51843 Run sandbox integrity checks before commands and filesystem operations @iceweasel-oai

> #51896 Preserve native errors in Windows sandbox ACL diagnostics @alishobeiri-oai

> #51974 Log Windows sandbox availability and backend selection @iceweasel-oai

> #52182 Expose a verified sandbox launcher to local MCP servers @bolinfest

> #52610 Align Linux sandbox names and docs with bubblewrap and seccomp @bolinfest

> #52682 Validate Windows sandbox accounts before password repair @zm-oai

> #52707 Migrate the Windows MXC sandbox to split MXC crates @iceweasel-oai

> #53709 Separate MCP sandbox policy from launcher metadata @bolinfest

Source: https://github.com/openai/codex/releases/tag/rust-v0.163.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-10-15-3-mobile-and-desktop-changes-in-rust-v0-163-0|3 Mobile and Desktop changes in rust-v0.163.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-10-15-6-model-support-changes-in-rust-v0-163-0|6 Model Support changes in rust-v0.163.0]] · Model Support
- [[Changes/Codex CLI/2026-10-15-15-apps-and-integrations-changes-in-rust-v0-163-0|15 Apps and Integrations changes in rust-v0.163.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-10-15-4-collaboration-changes-in-rust-v0-163-0|4 Collaboration changes in rust-v0.163.0]] · Collaboration
- [[Changes/Codex CLI/2026-10-15-codex-can-run-independent-read-only-tools-in-parallel-including-skill-memory-and|Codex can run independent read-only tools in parallel, including skill, memory…]] · Memory and Personalization
- [[Changes/Codex CLI/2026-10-15-15-developer-workflow-changes-in-rust-v0-163-0|15 Developer Workflow changes in rust-v0.163.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-10-15-4-voice-and-audio-changes-in-rust-v0-163-0|4 Voice and Audio changes in rust-v0.163.0]] · Voice and Audio
- [[Changes/Codex CLI/2026-10-15-4-editor-experience-changes-in-rust-v0-163-0|4 Editor Experience changes in rust-v0.163.0]] · Editor Experience
- [[Changes/Codex CLI/2026-10-15-16-context-window-changes-in-rust-v0-163-0|16 Context Window changes in rust-v0.163.0]] · Context Window
- [[Changes/Codex CLI/2026-10-15-8-interface-experience-changes-in-rust-v0-163-0|8 Interface Experience changes in rust-v0.163.0]] · Interface Experience
- [[Changes/Codex CLI/2026-10-15-14-agent-mode-changes-in-rust-v0-163-0|14 Agent Mode changes in rust-v0.163.0]] · Agent Mode
- [[Changes/Codex CLI/2026-10-15-53389-use-cached-login-credentials-for-guardian-decisions-swastik-oai|♯53389 Use cached login credentials for Guardian decisions @swastik-oai]] · Account and Access
- [[Changes/Codex CLI/2026-10-15-134-other-changes-in-rust-v0-163-0|134 other changes in rust-v0.163.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-10-15 · Claude Code · [[Changes/Claude Code/2026-10-15-5-safety-and-privacy-changes-in-v2-1-301|5 Safety and Privacy changes in v2.1.301]]
- Later: 2026-10-15 · Google Antigravity · [[Changes/Google Antigravity/2026-10-15-the-review-permissions-dialog-now-wraps-long-commands-and-paths-so-you-can-read|The Review permissions dialog now wraps long commands and paths, so you can read…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Descript · [[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke Application Access]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-10-15-4b6afc&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-10-15-18-safety-and-privacy-changes-in-rust-v0-163-0.md%0ACard%20ID%3A%20codex-cli-2026-10-15-4b6afc%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.163.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->