---
card_id: github-copilot-cli-2026-05-23-0b2f6a
date: '2026-05-23'
description: 'GitHub Copilot CLI · 2026-05-23 · Other changes: 6 changes in 1.0.52
  — Sessions now resume in their saved working directory; pass -C <dir> to override.
  Flags…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: d6a6d23966b9fedb82eb6942e3184cf1499a018cde85d836924265379a31a0e8
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-05-23-0b2f6a
  comparison: ''
  date: '2026-05-23'
  description: 'GitHub Copilot CLI — 1.0.52: 6 other changes'
  evidence:
  - quote: Sessions now resume in their saved working directory; pass -C <dir> to
      override. Flags whose values are relative paths (e.g. --attachment, --log-dir)
      resolve from the saved cwd.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.52
  - quote: Sessions containing events with non-URL strings in URL/URI fields resume
      without a 'Session file is corrupted' error
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.52
  - quote: Requests that time out due to an HTTP/2 upload stall automatically retry
      over HTTP/1.1
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.52
  - quote: Gray background bar no longer appears behind user messages on terminals
      without truecolor support
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.52
  - quote: /restart and /update preserve the current session ID after restarting
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.52
  - quote: /usage shows quota progress bars for session and weekly limits
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.52
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 6-other-changes-in-v1-0-52
  source_release: github-copilot-cli-2026-05-23-v1-0-52-github-328402909-801444d4
  source_type: github_releases
  theme: uncategorized
  title: 6 other changes in v1.0.52
  type: change
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-05-23-v1-0-52-github-328402909-801444d4|github-copilot-cli-2026-05-23-v1-0-52-github-328402909-801444d4]]'
source_type: github_releases
theme: uncategorized
title: 6 other changes in v1.0.52
type: change
---

<!-- chronolog:begin region="header" -->
# 6 other changes in v1.0.52

**GitHub Copilot CLI** · 2026-05-23 · Other changes · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.52) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-05-23-v1-0-52-github-328402909-801444d4|1.0.52]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Sessions now resume in their saved working directory; pass -C \<dir> to override. Flags whose values are relative paths (e.g. --attachment, --log-dir) resolve from the saved cwd.

> Sessions containing events with non-URL strings in URL/URI fields resume without a 'Session file is corrupted' error

> Requests that time out due to an HTTP/2 upload stall automatically retry over HTTP/1.1

> Gray background bar no longer appears behind user messages on terminals without truecolor support

> /restart and /update preserve the current session ID after restarting

> /usage shows quota progress bars for session and weekly limits

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.52
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-05-23-automatically-prune-old-process-log-files-from-copilot-logs-at-startup-to-preven|Automatically prune old process log files from ~/.copilot/logs/ at startup…]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-05-23-2-mobile-and-desktop-changes-in-v1-0-52|2 Mobile and Desktop changes in v1.0.52]] · Mobile and Desktop
- [[Changes/GitHub Copilot CLI/2026-05-23-2-account-and-access-changes-in-v1-0-52|2 Account and Access changes in v1.0.52]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-05-23-6-interface-experience-changes-in-v1-0-52|6 Interface Experience changes in v1.0.52]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-05-23-general-purpose-subagents-use-gpt-5-4-or-gpt-5-5-when-available|General-purpose subagents use GPT-5.4 or GPT-5.5 when available]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-05-23-custom-agents-support-opt-in-deferred-tool-loading-via-deferred-tool-loading-in|Custom agents support opt-in deferred tool loading via deferred-tool-loading…]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-05-23-2-apps-and-integrations-changes-in-v1-0-52|2 Apps and Integrations changes in v1.0.52]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-05-23-3-pricing-model-changes-in-v1-0-52|3 Pricing Model changes in v1.0.52]] · Pricing Model
- [[Changes/GitHub Copilot CLI/2026-05-23-4-context-window-changes-in-v1-0-52|4 Context Window changes in v1.0.52]] · Context Window
- [[Changes/GitHub Copilot CLI/2026-05-23-2-safety-and-privacy-changes-in-v1-0-52|2 Safety and Privacy changes in v1.0.52]] · Safety and Privacy
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-05-23-0b2f6a&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-05-23-6-other-changes-in-v1-0-52.md%0ACard%20ID%3A%20github-copilot-cli-2026-05-23-0b2f6a%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.52%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->