---
card_id: github-copilot-cli-2026-08-27-4bdc24
date: '2026-08-27'
description: 'GitHub Copilot CLI · 2026-08-27 · Apps and Integrations: 12 changes
  in 1.0.81 — The plugins dashboard is available to everyone: run `/plugin`, `/mcp`,
  or…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If
    you have a recording with each speaker with a different microphone, or saved…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2813
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 8635ae55a9a7fbfa8c234946762b13103e86834a1a7032be1c70dd47519e6c39
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-08-27-4bdc24
  comparison: ''
  date: '2026-08-27'
  description: 'GitHub Copilot CLI — 1.0.81: 12 Apps and Integrations changes'
  evidence:
  - quote: 'The plugins dashboard is available to everyone: run `/plugin`, `/mcp`,
      or `/skills`. Set `PLUGINS_DASHBOARD=false` to opt out of it and the `copilot
      plugins` command.'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.81
  - quote: An MCP server blocked by an enterprise policy now shows as blocked in /mcp
      instead of spinning as pending forever
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.81
  - quote: The startup status finishes after extension configuration during plugin
      reconciliation
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.81
  - quote: 'A failed tool call no longer stacks its `(MCP: server)` label one character
      per line down the timeline — the label and the error now share the row, with
      the longer side truncating'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.81
  - quote: Agents, skills and MCP servers contributed by installed plugins are no
      longer dropped in non-interactive (-p) runs, so --agent <plugin>:<agent> works
      headlessly without --plugin-dir
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.81
  - quote: /plugin now flags installed plugins and marketplaces that have a newer
      version upstream, and offers an Update action to pull it
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.81
  - quote: Path-sourced plugins in a local (directory-source) marketplace now load
      live from their real directory, so editing one takes effect on `/restart` or
      a new session — no `/plugin update`
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.81
  - quote: 'forceRemoteSettingsRefresh now fails closed: when set, the cached managed-settings
      policy is never served or used as a fetch-failure fallback (skipping both the
      1h fast path and the 24h stale fallback), so a failed startup fetch blocks on
      the unconfirmed policy instead of reverting to a possibly-stale cached one.
      Concretely, until a fresh policy is fetched the session applies the restrictive
      undetermined-policy posture: non-default MCP servers are blocked, bypass-permissions
      mode cannot be enabled, and policy-gated plugin install/update mutations are
      blocked'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.81
  - quote: Managed settings now win per entry for enabledPlugins and extraKnownMarketplaces,
      so a plugin or marketplace your organization pins can't be overridden locally
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.81
  - quote: Removed the `PLUGINS_DASHBOARD` opt-out and the legacy skills picker it
      kept alive. `/skills`, bare `/mcp`, and `/mcp show` (with no server name) always
      open the dashboard; `/mcp config` still opens the dedicated MCP wizard.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.81
  - quote: Removed `/plugins`; its resources moved to `/plugin`, `/mcp` and `/skills`,
      with `/subagents` and `/instructions` for agents and instructions.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.81
  - quote: 'Enabling and disabling hooks and LSP servers is temporarily unavailable:
      those toggles existed only in the `/plugins` dashboard that this release removes.'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.81
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 12-apps-and-integrations-changes-in-v1-0-81
  source_release: github-copilot-cli-2026-08-27-v1-0-81-github-377993714-523d567a
  source_type: github_releases
  theme: apps-integrations
  title: 12 Apps and Integrations changes in v1.0.81
  type: change
related_changes:
- '[[Changes/Lovable/2026-08-26-connect-github-api-by-signing-in-with-your-github-account|Connect
  GitHub API by signing in with your GitHub account]]'
- '[[Changes/Lovable/2026-08-26-chat-with-lovable-in-slack|Chat with Lovable in Slack]]'
- '[[Changes/Claude Code/2026-08-27-improved-managed-settings-client-side-timeout-mcp-startup-mode-and-stream-watchd|Improved
  managed settings]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-08-27-v1-0-81-github-377993714-523d567a|github-copilot-cli-2026-08-27-v1-0-81-github-377993714-523d567a]]'
source_type: github_releases
theme: apps-integrations
title: 12 Apps and Integrations changes in v1.0.81
type: change
---

<!-- chronolog:begin region="header" -->
# 12 Apps and Integrations changes in v1.0.81

**GitHub Copilot CLI** · 2026-08-27 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.81) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-08-27-v1-0-81-github-377993714-523d567a|1.0.81]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> The plugins dashboard is available to everyone: run `/plugin`, `/mcp`, or `/skills`. Set `PLUGINS_DASHBOARD=false` to opt out of it and the `copilot plugins` command.

> An MCP server blocked by an enterprise policy now shows as blocked in /mcp instead of spinning as pending forever

> The startup status finishes after extension configuration during plugin reconciliation

> A failed tool call no longer stacks its `(MCP: server)` label one character per line down the timeline — the label and the error now share the row, with the longer side truncating

> Agents, skills and MCP servers contributed by installed plugins are no longer dropped in non-interactive (-p) runs, so --agent \<plugin>:\<agent> works headlessly without --plugin-dir

> /plugin now flags installed plugins and marketplaces that have a newer version upstream, and offers an Update action to pull it

> Path-sourced plugins in a local (directory-source) marketplace now load live from their real directory, so editing one takes effect on `/restart` or a new session — no `/plugin update`

> forceRemoteSettingsRefresh now fails closed: when set, the cached managed-settings policy is never served or used as a fetch-failure fallback (skipping both the 1h fast path and the 24h stale fallback), so a failed startup fetch blocks on the unconfirmed policy instead of reverting to a possibly-stale cached one. Concretely, until a fresh policy is fetched the session applies the restrictive undetermined-policy posture: non-default MCP servers are blocked, bypass-permissions mode cannot be enabled, and policy-gated plugin install/update mutations are blocked

> Managed settings now win per entry for enabledPlugins and extraKnownMarketplaces, so a plugin or marketplace your organization pins can't be overridden locally

> Removed the `PLUGINS_DASHBOARD` opt-out and the legacy skills picker it kept alive. `/skills`, bare `/mcp`, and `/mcp show` (with no server name) always open the dashboard; `/mcp config` still opens the dedicated MCP wizard.

> Removed `/plugins`; its resources moved to `/plugin`, `/mcp` and `/skills`, with `/subagents` and `/instructions` for agents and instructions.

> Enabling and disabling hooks and LSP servers is temporarily unavailable: those toggles existed only in the `/plugins` dashboard that this release removes.

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.81
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-08-27-resume-large-sessions-faster-by-showing-recent-history-first-while-older-message|Resume large sessions faster by showing recent history first while older messages load]] · Reliability and Performance
- [[Changes/GitHub Copilot CLI/2026-08-27-2-enterprise-and-administration-changes-in-v1-0-81|2 Enterprise and Administration changes in v1.0.81]] · Enterprise and Administration
- [[Changes/GitHub Copilot CLI/2026-08-27-sandboxed-builds-on-windows-create-their-scratch-caches-on-first-run-so-cargo-go|Sandboxed builds on Windows create their scratch caches on first run, so cargo, go…]] · Mobile and Desktop
- [[Changes/GitHub Copilot CLI/2026-08-27-5-developer-workflow-changes-in-v1-0-81|5 Developer Workflow changes in v1.0.81]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-08-27-3-interface-experience-changes-in-v1-0-81|3 Interface Experience changes in v1.0.81]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-08-27-8-agent-mode-changes-in-v1-0-81|8 Agent Mode changes in v1.0.81]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-08-27-hooks-can-now-receive-the-current-opentelemetry-trace-context-and-emit-correlate|Hooks can now receive the current OpenTelemetry trace context and emit correlated spans]] · Context Window
- [[Changes/GitHub Copilot CLI/2026-08-27-ship-mcp-2026-07-28-support-to-cli-sdk-ide-and-in-memory-clients|Ship MCP 2026-07-28 support to CLI, SDK, IDE, and in-memory clients]] · Memory and Personalization
- [[Changes/GitHub Copilot CLI/2026-08-27-add-copilot-app-to-open-the-github-copilot-app-in-the-current-directory|Add copilot app to open the GitHub Copilot app in the current directory]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-08-27-2-account-and-access-changes-in-v1-0-81|2 Account and Access changes in v1.0.81]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-08-27-use-x-to-remove-scheduled-every-and-after-prompts-in-schedule-manager|Use x to remove scheduled /every and /after prompts in Schedule Manager]] · Automation and Scheduling
- [[Changes/GitHub Copilot CLI/2026-08-27-canvas-windows-open-and-refresh-in-the-background-instead-of-stealing-focus-from|Canvas windows open and refresh in the background instead of stealing focus…]] · Files and Data
- [[Changes/GitHub Copilot CLI/2026-08-27-4-model-support-changes-in-v1-0-81|4 Model Support changes in v1.0.81]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-08-27-5-safety-and-privacy-changes-in-v1-0-81|5 Safety and Privacy changes in v1.0.81]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-08-27-use-ctrl-space-to-toggle-voice-dictation|Use Ctrl+Space to toggle voice dictation]] · Voice and Audio
- [[Changes/GitHub Copilot CLI/2026-08-27-6-other-changes-in-v1-0-81|6 other changes in v1.0.81]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-08-27 · Claude Code · [[Changes/Claude Code/2026-08-27-improved-managed-settings-client-side-timeout-mcp-startup-mode-and-stream-watchd|Improved managed settings]]
- Later: 2026-08-27 · Kimi Code · [[Changes/Kimi Code/2026-08-27-2-apps-and-integrations-changes-in-kimi-code-0-39-0|2 Apps and Integrations changes in Kimi Code 0.39.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-12-14 · Descript · [[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If you have a recording with each speaker with a different microphone, or saved…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-08-27-4bdc24&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-08-27-12-apps-and-integrations-changes-in-v1-0-81.md%0ACard%20ID%3A%20github-copilot-cli-2026-08-27-4bdc24%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.81%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->