---
card_id: kimi-code-2026-06-26-779440
date: '2026-06-26'
description: 'Kimi Code · 2026-06-26 · Apps and Integrations: 4 changes in Kimi Code
  0.20.0 (2026-06-26) — Redesign `/plugins` as a single tabbed panel: **Installed**…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If
    you have a recording with each speaker with a different microphone, or saved…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2751
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: abbcad4957bfc61a37897753412404101c02be002c818a4c191230b61994669e
product: kimi-code
product_name: Kimi Code
record:
  card_id: kimi-code-2026-06-26-779440
  comparison: ''
  date: '2026-06-26'
  description: 'Kimi Code — Kimi Code 0.20.0 (2026-06-26): 4 Apps and Integrations
    changes'
  evidence:
  - quote: 'Redesign `/plugins` as a single tabbed panel: **Installed** (manage installed
      plugins — toggle, remove, MCP, details, reload), **Official** (Kimi-maintained
      marketplace plugins), **Third-party** (marketplace plugins from other publishers),
      and **Custom** (install straight from a GitHub URL, zip URL, or local path).
      Use `Tab` / `Shift-Tab` to switch tabs.'
    source_release: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
  - quote: '`/reload` now refreshes the assistant''s view of plugin skills, so plugin
      changes take effect in the current session instead of requiring a new one.'
    source_release: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
  - quote: Add a confirmation prompt before installing third-party plugins.
    source_release: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
  - quote: Show update badges on the `/plugins` Installed tab, where Enter now installs
      the available update and I opens plugin details.
    source_release: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: kimi-code
  product_name: Kimi Code
  slug: 4-apps-and-integrations-changes-in-kimi-code-0-20-0
  source_release: kimi-code-2026-06-26-0-20-0-920cae87
  source_type: kimi_code_changelog
  theme: apps-integrations
  title: 4 Apps and Integrations changes in Kimi Code 0.20.0
  type: change
related_changes:
- '[[Changes/Ollama/2026-06-25-docs-redesign-docs-landing-and-integrations-overview-by-hoyyeva-in-https-github|docs:
  redesign docs landing and integrations overview]]'
- '[[Changes/Cline/2026-06-26-13-apps-and-integrations-changes-in-v4-0-0|13 Apps and
  Integrations changes in v4.0.0]]'
- '[[Changes/Kimi Code/2026-06-26-plugins-now-support-declaring-lifecycle-hooks-in-kimi-plugin-json-to-run-scripts|Plugins
  now support declaring lifecycle hooks in kimi.plugin.json to run scripts…]]'
source_release: '[[Releases/Kimi Code/kimi-code-2026-06-26-0-20-0-920cae87|kimi-code-2026-06-26-0-20-0-920cae87]]'
source_type: kimi_code_changelog
theme: apps-integrations
title: 4 Apps and Integrations changes in Kimi Code 0.20.0
type: change
---

<!-- chronolog:begin region="header" -->
# 4 Apps and Integrations changes in Kimi Code 0.20.0

**Kimi Code** · 2026-06-26 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md) · from [[Releases/Kimi Code/kimi-code-2026-06-26-0-20-0-920cae87|Kimi Code 0.20.0 (2026-06-26)]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Redesign `/plugins` as a single tabbed panel: **Installed** (manage installed plugins — toggle, remove, MCP, details, reload), **Official** (Kimi-maintained marketplace plugins), **Third-party** (marketplace plugins from other publishers), and **Custom** (install straight from a GitHub URL, zip URL, or local path). Use `Tab` / `Shift-Tab` to switch tabs.

> `/reload` now refreshes the assistant's view of plugin skills, so plugin changes take effect in the current session instead of requiring a new one.

> Add a confirmation prompt before installing third-party plugins.

> Show update badges on the `/plugins` Installed tab, where Enter now installs the available update and I opens plugin details.

Source: https://github.com/MoonshotAI/kimi-code/blob/main/docs/en/release-notes/changelog.md
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Kimi Code/2026-06-26-preserve-full-tool-output-logs-when-previews-are-truncated-and-link-background-t|Preserve full tool output logs when previews are truncated and link background task…]] · Editor Experience
- [[Changes/Kimi Code/2026-06-26-add-a-hint-to-the-per-turn-step-limit-error-pointing-users-to-the-loop-control-m|Add a hint to the per-turn step limit error pointing users…]] · Automation and Scheduling
- [[Changes/Kimi Code/2026-06-26-reduce-streaming-redraw-cost-for-long-assistant-messages-with-code-blocks|Reduce streaming redraw cost for long assistant messages with code blocks]] · Pricing Model
- [[Changes/Kimi Code/2026-06-26-add-a-host-cli-option-so-kimi-web-host-can-expose-the-server-to-the-internet-wit|Add a --host CLI option so kimi web --host can expose the server…]] · Safety and Privacy
- [[Changes/Kimi Code/2026-06-26-add-shell-mode-to-the-tui-type-in-the-input-box-to-enable-it-for-long-running-co|Add shell mode to the TUI]] · Account and Access
- [[Changes/Kimi Code/2026-06-26-3-agent-mode-changes-in-kimi-code-0-20-0|3 Agent Mode changes in Kimi Code 0.20.0]] · Agent Mode
- [[Changes/Kimi Code/2026-06-26-keep-the-web-session-sidebar-from-re-rendering-on-every-streaming-token-to-impro|Keep the web session sidebar from re-rendering on every streaming token to improve…]] · Interface Experience
- [[Changes/Kimi Code/2026-06-26-9-other-changes-in-kimi-code-0-20-0|9 other changes in Kimi Code 0.20.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-06-26 · Kimi Code · [[Changes/Kimi Code/2026-06-26-plugins-now-support-declaring-lifecycle-hooks-in-kimi-plugin-json-to-run-scripts|Plugins now support declaring lifecycle hooks in kimi.plugin.json to run scripts…]]
- Later: 2026-06-26 · Lovable · [[Changes/Lovable/2026-06-26-app-connectors-klipy-and-logo-dev|App connectors: KLIPY and Logo.dev]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-12-14 · Descript · [[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If you have a recording with each speaker with a different microphone, or saved…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20kimi-code-2026-06-26-779440&body=Card%3A%20Changes%2FKimi%20Code%2F2026-06-26-4-apps-and-integrations-changes-in-kimi-code-0-20-0.md%0ACard%20ID%3A%20kimi-code-2026-06-26-779440%0ASource%3A%20https%3A%2F%2Fgithub.com%2FMoonshotAI%2Fkimi-code%2Fblob%2Fmain%2Fdocs%2Fen%2Frelease-notes%2Fchangelog.md%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->