---
card_id: kimi-code-2026-05-26-732988
date: '2026-05-26'
description: 'Kimi Code · 2026-05-26 · Developer Workflow: Exit promptly when the
  controlling terminal goes away. The TUI now handles `SIGHUP` / `SIGTERM` and stdout/stderr…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter
    Colors]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2814
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: change
machine_hash: ff22a185687be02ee8c189ab5b37b0eb28557af02131e3f446293817eac022ed
product: kimi-code
product_name: Kimi Code
record:
  card_id: kimi-code-2026-05-26-732988
  comparison: ''
  date: '2026-05-26'
  description: 'Kimi Code — Kimi Code 0.3.0 (2026-05-26): Exit promptly when the controlling
    terminal goes away. The TUI now handles `SIGHUP` / `SIGTERM` and stdout/stderr
    `EIO` / `EPIPE` / `ENOTCONN` errors, preventing leftover `kimi` processes that
    pin a CPU core after the parent shell or multiplexer dies unexpectedly.'
  evidence:
  - quote: Exit promptly when the controlling terminal goes away. The TUI now handles
      `SIGHUP` / `SIGTERM` and stdout/stderr `EIO` / `EPIPE` / `ENOTCONN` errors,
      preventing leftover `kimi` processes that pin a CPU core after the parent shell
      or multiplexer dies unexpectedly.
    source_release: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
  extractor_version: fallback-v5
  impact: incremental
  kind: change
  product: kimi-code
  product_name: Kimi Code
  slug: exit-promptly-when-the-controlling-terminal-goes-away-the-tui-now-handles-sighup
  source_release: kimi-code-2026-05-26-0-3-0-92e16055
  source_type: kimi_code_changelog
  theme: developer-workflow
  title: Exit promptly when the controlling terminal goes away
  type: change
related_changes:
- '[[Changes/OpenCode/2026-05-22-3-developer-workflow-changes-in-v1-15-9|3 Developer
  Workflow changes in v1.15.9]]'
- '[[Changes/GitHub Copilot CLI/2026-05-24-bash-shell-sessions-no-longer-hang-when-ps0-or-prompt-command-is-set-in-the-envi|Bash
  shell sessions no longer hang when PS0 or PROMPT_COMMAND is set in the environment]]'
- '[[Changes/Kimi Code/2026-05-26-persist-model-selections-from-the-terminal-ui-to-the-default-configuration-and-h|Persist
  model selections from the terminal UI to the default configuration…]]'
source_release: '[[Releases/Kimi Code/kimi-code-2026-05-26-0-3-0-92e16055|kimi-code-2026-05-26-0-3-0-92e16055]]'
source_type: kimi_code_changelog
theme: developer-workflow
title: Exit promptly when the controlling terminal goes away
type: change
---

<!-- chronolog:begin region="header" -->
# Exit promptly when the controlling terminal goes away

**Kimi Code** · 2026-05-26 · [[Themes/developer-workflow|Developer Workflow]] · [Official source](https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md) · from [[Releases/Kimi Code/kimi-code-2026-05-26-0-3-0-92e16055|Kimi Code 0.3.0 (2026-05-26)]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Exit promptly when the controlling terminal goes away. The TUI now handles `SIGHUP` / `SIGTERM` and stdout/stderr `EIO` / `EPIPE` / `ENOTCONN` errors, preventing leftover `kimi` processes that pin a CPU core after the parent shell or multiplexer dies unexpectedly.
>
> Source: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Kimi Code/2026-05-26-2-agent-mode-changes-in-kimi-code-0-3-0|2 Agent Mode changes in Kimi Code 0.3.0]] · Agent Mode
- [[Changes/Kimi Code/2026-05-26-prevent-running-the-model-and-sessions-slash-commands-while-streaming-or-compact|Prevent running the /model and /sessions slash commands while streaming…]] · Context Window
- [[Changes/Kimi Code/2026-05-26-2-model-support-changes-in-kimi-code-0-3-0|2 Model Support changes in Kimi Code 0.3.0]] · Model Support
- [[Changes/Kimi Code/2026-05-26-avoid-overly-small-local-completion-caps-that-can-truncate-reasoning-before-summ|Avoid overly small local completion caps that can truncate reasoning before…]] · Editor Experience
- [[Changes/Kimi Code/2026-05-26-logout-now-opens-a-picker-so-you-can-choose-which-provider-to-log-out-of-instead|/logout now opens a picker so you can choose which provider to log out of, instead…]] · Interface Experience
- [[Changes/Kimi Code/2026-05-26-3-other-changes-in-kimi-code-0-3-0|3 other changes in Kimi Code 0.3.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-05-26 · Kimi Code · [[Changes/Kimi Code/2026-05-26-persist-model-selections-from-the-terminal-ui-to-the-default-configuration-and-h|Persist model selections from the terminal UI to the default configuration…]]
- Later: 2026-05-27 · Claude Code · [[Changes/Claude Code/2026-05-27-2-developer-workflow-changes-in-v2-1-152|2 Developer Workflow changes in v2.1.152]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-09-11 · Descript · [[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter Colors]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20kimi-code-2026-05-26-732988&body=Card%3A%20Changes%2FKimi%20Code%2F2026-05-26-exit-promptly-when-the-controlling-terminal-goes-away-the-tui-now-handles-sighup.md%0ACard%20ID%3A%20kimi-code-2026-05-26-732988%0ASource%3A%20https%3A%2F%2Fgithub.com%2FMoonshotAI%2Fkimi-code%2Fblob%2Fmain%2Fdocs%2Fen%2Frelease-notes%2Fchangelog.md%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->