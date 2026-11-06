---
card_id: github-copilot-cli-2026-06-30-6e1756
date: '2026-06-30'
description: 'GitHub Copilot CLI · 2026-06-30 · Other changes: 33 changes in 1.0.66
  — Avoid blocking commands that contain Windows-style path fragments'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: c868ee46b99466555e825164ad77af34b5b18caadaf223b8920a6ebe4a6b866b
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-06-30-6e1756
  comparison: ''
  date: '2026-06-30'
  description: 'GitHub Copilot CLI — 1.0.66: 33 other changes'
  evidence:
  - quote: Avoid blocking commands that contain Windows-style path fragments
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.66
  - quote: Large output handling now respects custom output directories and a disable
      setting
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.66
  - quote: Prevent PR description generation from crashing on empty assistant responses
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.66
  - quote: 'Add @ file and # GitHub ref completions in relay sessions'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.66
  - quote: Show the correct session age when filesystem birthtime is missing
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.66
  - quote: Show a (sandboxed) badge on compact Search timeline entries
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.66
  - quote: Show quota snapshots for WebSocket Responses requests
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.66
  - quote: Skip synchronized output under tmux to avoid mouse pointer flicker
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.66
  - quote: Session limits now apply across the current conversation, reset on /clear,
      and use the sessionLimits option key.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.66
  - quote: Prompt to install gh CLI when it is missing in GitHub repositories
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.66
  - quote: Extension toggles preserve the selected mode
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.66
  - quote: Preserve newlines in /after and /every scheduled prompts
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.66
  - quote: Show submit times next to user prompts in the timeline
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.66
  - quote: Make /pr auto keep working through CI, review, and merge queue
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.66
  - quote: Clicking to expand a compact timeline entry holds it in place and reveals
      its content downward
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.66
  - quote: Add `/chronicle skills review` for reviewing proposed draft skill changes,
      with options to accept, reject, or defer each draft
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.66
  - quote: Snapshot creation retries transient HEAD lookup failures instead of crashing
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.66
  - quote: Keep `/chronicle reindex` responsive and show progress in the timeline
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.66
  - quote: Keep queued messages from getting stuck behind background work
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.66
  - quote: Retry managed settings fetch after transient connection-pool errors
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.66
  - quote: Collapse multi-line sub-items into one inline line in compact timeline
      rows
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.66
  - quote: Inline hook settings now handle nested Claude-style hook groups correctly
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.66
  - quote: Keep the CLI responsive during secret filtering
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.66
  - quote: Search inputs match queries that have leading or trailing whitespace
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.66
  - quote: Enable /rename in remote-hosted (cloud and relay) sessions
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.66
  - quote: Add experimental response limits controls to CLI settings
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.66
  - quote: Let managed settings configure OpenTelemetry export
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.66
  - quote: Add persisted dynamicRetrieval setting (and --dynamic-retrieval skills=<on|off>
      flag) to enable or disable embeddings-based retrieval of skills
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.66
  - quote: Keep /restart working when shutdown teardown takes too long
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.66
  - quote: Copying wrapped text from the scroll view keeps spacing correct
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.66
  - quote: Keep framed user messages from clipping trailing characters at the right
      edge
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.66
  - quote: Consolidate color palette settings under /settings theme
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.66
  - quote: Store CLI settings and session state more reliably
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.66
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 33-other-changes-in-v1-0-66
  source_release: github-copilot-cli-2026-06-30-v1-0-66-github-346845066-af776740
  source_type: github_releases
  theme: uncategorized
  title: 33 other changes in v1.0.66
  type: change
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-06-30-v1-0-66-github-346845066-af776740|github-copilot-cli-2026-06-30-v1-0-66-github-346845066-af776740]]'
source_type: github_releases
theme: uncategorized
title: 33 other changes in v1.0.66
type: change
---

<!-- chronolog:begin region="header" -->
# 33 other changes in v1.0.66

**GitHub Copilot CLI** · 2026-06-30 · Other changes · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.66) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-06-30-v1-0-66-github-346845066-af776740|1.0.66]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Avoid blocking commands that contain Windows-style path fragments

> Large output handling now respects custom output directories and a disable setting

> Prevent PR description generation from crashing on empty assistant responses

> Add @ file and # GitHub ref completions in relay sessions

> Show the correct session age when filesystem birthtime is missing

> Show a (sandboxed) badge on compact Search timeline entries

> Show quota snapshots for WebSocket Responses requests

> Skip synchronized output under tmux to avoid mouse pointer flicker

> Session limits now apply across the current conversation, reset on /clear, and use the sessionLimits option key.

> Prompt to install gh CLI when it is missing in GitHub repositories

> Extension toggles preserve the selected mode

> Preserve newlines in /after and /every scheduled prompts

> Show submit times next to user prompts in the timeline

> Make /pr auto keep working through CI, review, and merge queue

> Clicking to expand a compact timeline entry holds it in place and reveals its content downward

> Add `/chronicle skills review` for reviewing proposed draft skill changes, with options to accept, reject, or defer each draft

> Snapshot creation retries transient HEAD lookup failures instead of crashing

> Keep `/chronicle reindex` responsive and show progress in the timeline

> Keep queued messages from getting stuck behind background work

> Retry managed settings fetch after transient connection-pool errors

> Collapse multi-line sub-items into one inline line in compact timeline rows

> Inline hook settings now handle nested Claude-style hook groups correctly

> Keep the CLI responsive during secret filtering

> Search inputs match queries that have leading or trailing whitespace

> Enable /rename in remote-hosted (cloud and relay) sessions

> Add experimental response limits controls to CLI settings

> Let managed settings configure OpenTelemetry export

> Add persisted dynamicRetrieval setting (and --dynamic-retrieval skills=\<on|off> flag) to enable or disable embeddings-based retrieval of skills

> Keep /restart working when shutdown teardown takes too long

> Copying wrapped text from the scroll view keeps spacing correct

> Keep framed user messages from clipping trailing characters at the right edge

> Consolidate color palette settings under /settings theme

> Store CLI settings and session state more reliably

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.66
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-06-30-2-editor-experience-changes-in-v1-0-66|2 Editor Experience changes in v1.0.66]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-06-30-voice-mode-turns-itself-off-when-the-engine-fails-to-start-at-boot|Voice mode turns itself off when the engine fails to start at boot]] · Voice and Audio
- [[Changes/GitHub Copilot CLI/2026-06-30-perform-tokenizer-warmup-in-parallel-on-a-background-thread-for-better-startup-p|Perform tokenizer warmup in parallel on a background thread for better startup performance]] · Reliability and Performance
- [[Changes/GitHub Copilot CLI/2026-06-30-2-collaboration-changes-in-v1-0-66|2 Collaboration changes in v1.0.66]] · Collaboration
- [[Changes/GitHub Copilot CLI/2026-06-30-pr-auto-now-starts-a-self-paced-loop-that-fixes-one-thing-per-run-and-paces-itse|/pr auto now starts a self-paced loop that fixes one thing per run and paces itself…]] · Automation and Scheduling
- [[Changes/GitHub Copilot CLI/2026-06-30-3-interface-experience-changes-in-v1-0-66|3 Interface Experience changes in v1.0.66]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-06-30-9-apps-and-integrations-changes-in-v1-0-66|9 Apps and Integrations changes in v1.0.66]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-06-30-match-the-terminal-text-color-to-the-github-theme-canvas|Match the terminal text color to the GitHub theme canvas]] · Files and Data
- [[Changes/GitHub Copilot CLI/2026-06-30-21-developer-workflow-changes-in-v1-0-66|21 Developer Workflow changes in v1.0.66]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-06-30-6-account-and-access-changes-in-v1-0-66|6 Account and Access changes in v1.0.66]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-06-30-configure-subagent-concurrency-and-depth-limits-in-settings-usage-based-billing|Configure subagent concurrency and depth limits in /settings (usage-based billing users)]] · Pricing Model
- [[Changes/GitHub Copilot CLI/2026-06-30-2-mobile-and-desktop-changes-in-v1-0-66|2 Mobile and Desktop changes in v1.0.66]] · Mobile and Desktop
- [[Changes/GitHub Copilot CLI/2026-06-30-3-safety-and-privacy-changes-in-v1-0-66|3 Safety and Privacy changes in v1.0.66]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-06-30-recover-corrupted-session-history-on-load|Recover corrupted session history on load]] · Projects and Workspaces
- [[Changes/GitHub Copilot CLI/2026-06-30-8-agent-mode-changes-in-v1-0-66|8 Agent Mode changes in v1.0.66]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-06-30-keep-session-store-searches-and-context-lookups-responsive|Keep session-store searches and context lookups responsive]] · Context Window
- [[Changes/GitHub Copilot CLI/2026-06-30-5-model-support-changes-in-v1-0-66|5 Model Support changes in v1.0.66]] · Model Support
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-06-30-6e1756&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-06-30-33-other-changes-in-v1-0-66.md%0ACard%20ID%3A%20github-copilot-cli-2026-06-30-6e1756%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.66%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->