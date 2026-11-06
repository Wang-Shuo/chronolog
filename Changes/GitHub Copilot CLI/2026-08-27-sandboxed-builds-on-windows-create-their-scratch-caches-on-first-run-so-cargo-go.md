---
card_id: github-copilot-cli-2026-08-27-382a86
date: '2026-08-27'
description: 'GitHub Copilot CLI · 2026-08-27 · Mobile and Desktop: Sandboxed builds
  on Windows create their scratch caches on first run, so cargo, go, Gradle, and ccache…'
diffusion:
  first_in_tracked: "[[Changes/Cursor/2023-03-14-windows-and-linux-support|Windows
    and Linux support \U0001F973]]"
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1262
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: mobile-desktop
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: change
machine_hash: 88058b88de931af78f10003376cf500b526da0a6ac8c0c848fd7466116b4a623
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-08-27-382a86
  comparison: ''
  date: '2026-08-27'
  description: 'GitHub Copilot CLI — 1.0.81: Sandboxed builds on Windows create their
    scratch caches on first run, so cargo, go, Gradle, and ccache work without a warm
    cache'
  evidence:
  - quote: Sandboxed builds on Windows create their scratch caches on first run, so
      cargo, go, Gradle, and ccache work without a warm cache
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.81
  extractor_version: fallback-v5
  impact: incremental
  kind: change
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: sandboxed-builds-on-windows-create-their-scratch-caches-on-first-run-so-cargo-go
  source_release: github-copilot-cli-2026-08-27-v1-0-81-github-377993714-523d567a
  source_type: github_releases
  theme: mobile-desktop
  theme_matches: []
  theme_resolution: manual-semantic-rule-v1
  title: Sandboxed builds on Windows create their scratch caches on first run, so
    cargo, go…
  type: change
related_changes:
- '[[Changes/Windsurf/2026-08-21-devin-desktop|Devin Desktop]]'
- '[[Changes/Claude Code/2026-08-25-windows-macos-fixed-headless-sessions-not-cleaning-up-stale-entries-in-claude-se|Windows/macOS:
  Fixed headless sessions not cleaning up stale entries…]]'
- '[[Changes/Codex CLI/2026-08-26-39811-restrict-macos-preference-reads-to-full-disk-policies-copyberry|♯39811
  Restrict macOS preference reads to full-disk policies @copyberry]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-08-27-v1-0-81-github-377993714-523d567a|github-copilot-cli-2026-08-27-v1-0-81-github-377993714-523d567a]]'
source_type: github_releases
theme: mobile-desktop
title: Sandboxed builds on Windows create their scratch caches on first run, so cargo,
  go…
type: change
---

<!-- chronolog:begin region="header" -->
# Sandboxed builds on Windows create their scratch caches on first run, so cargo, go…

**GitHub Copilot CLI** · 2026-08-27 · [[Themes/mobile-desktop|Mobile and Desktop]] · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.81) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-08-27-v1-0-81-github-377993714-523d567a|1.0.81]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Sandboxed builds on Windows create their scratch caches on first run, so cargo, go, Gradle, and ccache work without a warm cache
>
> Source: https://github.com/github/copilot-cli/releases/tag/v1.0.81
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-08-27-resume-large-sessions-faster-by-showing-recent-history-first-while-older-message|Resume large sessions faster by showing recent history first while older messages load]] · Reliability and Performance
- [[Changes/GitHub Copilot CLI/2026-08-27-2-enterprise-and-administration-changes-in-v1-0-81|2 Enterprise and Administration changes in v1.0.81]] · Enterprise and Administration
- [[Changes/GitHub Copilot CLI/2026-08-27-5-developer-workflow-changes-in-v1-0-81|5 Developer Workflow changes in v1.0.81]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-08-27-3-interface-experience-changes-in-v1-0-81|3 Interface Experience changes in v1.0.81]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-08-27-12-apps-and-integrations-changes-in-v1-0-81|12 Apps and Integrations changes in v1.0.81]] · Apps and Integrations
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
## Nearby in Mobile and Desktop

- Earlier: 2026-08-26 · Codex CLI · [[Changes/Codex CLI/2026-08-26-39811-restrict-macos-preference-reads-to-full-disk-policies-copyberry|♯39811 Restrict macOS preference reads to full-disk policies @copyberry]]
- Later: 2026-08-27 · OpenHands · [[Changes/OpenHands/2026-08-27-feat-add-linux-desktop-installer-build-ci-deb-maintainer-fix-by-georgeglarson-in|feat: add linux desktop installer build (CI + deb maintainer fix)]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-14 · Cursor · [[Changes/Cursor/2023-03-14-windows-and-linux-support|Windows and Linux support 🥳]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-08-27-382a86&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-08-27-sandboxed-builds-on-windows-create-their-scratch-caches-on-first-run-so-cargo-go.md%0ACard%20ID%3A%20github-copilot-cli-2026-08-27-382a86%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.81%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->