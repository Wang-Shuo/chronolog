---
card_id: claude-code-2026-09-14-c2bf88
date: '2026-09-14'
description: 'Claude Code · 2026-09-14 · Other changes: 9 changes in v2.1.271 — Added
  fast mode in Claude Code Remote sessions (cloud and self-hosted runners): the host''s…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 16d311a15f7706edea012003eb4169d92d2e164ae28cf55021260c64e3ecc0be
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-09-14-c2bf88
  comparison: ''
  date: '2026-09-14'
  description: 'Claude Code — v2.1.271: 9 other changes'
  evidence:
  - quote: 'Added fast mode in Claude Code Remote sessions (cloud and self-hosted
      runners): the host''s fast-mode setting or `/fast` typed in the session applies
      where your organization allows it'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.271
  - quote: 'Added `claude self-hosted-runner --drain-marker-file <path>`: when that
      file exists at a SIGTERM drain, the runner reports its exit to the server as
      a host drain (telemetry only)'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.271
  - quote: 'Improved Artifact tool publish errors: a publish with no file now says
      to write the page to a file first, and an unsupported file type is reported
      before a missing favicon'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.271
  - quote: 'Improved the Artifact tool''s error when a page declares a capability
      its contract version lacks: it now lists every supported capability and notes
      when a newer contract version has it'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.271
  - quote: 'Improved artifact watching: a session can now watch up to 10 published
      artifacts at once for republishes made elsewhere, up from 5'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.271
  - quote: Changed Monitor watches to always have a deadline (at most 30 minutes;
      10 in single-prompt `-p` runs) and notify Claude to re-arm, replacing the no-timeout
      `persistent` option
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.271
  - quote: '[VSCode] Added an Attach Open File setting that, when turned off, stops
      the open file from being added to messages; selected text is still attached'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.271
  - quote: '[Claude Code on the web] Changed the Routines page on claude.ai/code to
      a new layout with Yours and Templates tabs and two-column routine cards that
      show run status, and removed its calendar view'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.271
  - quote: '[Claude Code on the web] Improved the Cloud environments admin page: it
      shows the default environment for Claude Tag and Claude Code, with a link to
      change it, and marks the recommended kind to create'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.271
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 9-other-changes-in-v2-1-271
  source_release: claude-code-2026-09-14-v2-1-271-github-388664071-570fd44f
  source_type: github_releases
  theme: uncategorized
  title: 9 other changes in v2.1.271
  type: change
source_release: '[[Releases/Claude Code/claude-code-2026-09-14-v2-1-271-github-388664071-570fd44f|claude-code-2026-09-14-v2-1-271-github-388664071-570fd44f]]'
source_type: github_releases
theme: uncategorized
title: 9 other changes in v2.1.271
type: change
---

<!-- chronolog:begin region="header" -->
# 9 other changes in v2.1.271

**Claude Code** · 2026-09-14 · Other changes · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.271) · from [[Releases/Claude Code/claude-code-2026-09-14-v2-1-271-github-388664071-570fd44f|v2.1.271]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Added fast mode in Claude Code Remote sessions (cloud and self-hosted runners): the host's fast-mode setting or `/fast` typed in the session applies where your organization allows it

> Added `claude self-hosted-runner --drain-marker-file <path>`: when that file exists at a SIGTERM drain, the runner reports its exit to the server as a host drain (telemetry only)

> Improved Artifact tool publish errors: a publish with no file now says to write the page to a file first, and an unsupported file type is reported before a missing favicon

> Improved the Artifact tool's error when a page declares a capability its contract version lacks: it now lists every supported capability and notes when a newer contract version has it

> Improved artifact watching: a session can now watch up to 10 published artifacts at once for republishes made elsewhere, up from 5

> Changed Monitor watches to always have a deadline (at most 30 minutes; 10 in single-prompt `-p` runs) and notify Claude to re-arm, replacing the no-timeout `persistent` option

> [VSCode] Added an Attach Open File setting that, when turned off, stops the open file from being added to messages; selected text is still attached

> [Claude Code on the web] Changed the Routines page on claude.ai/code to a new layout with Yours and Templates tabs and two-column routine cards that show run status, and removed its calendar view

> [Claude Code on the web] Improved the Cloud environments admin page: it shows the default environment for Claude Tag and Claude Code, with a link to change it, and marks the recommended kind to create

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.271
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-09-14-changed-claude-apps-gateway-bedrock-vertex-ai-and-foundry-sessions-so-that-they|Changed Claude apps gateway, Bedrock, Vertex AI, and Foundry sessions so that they…]] · Account and Access
- [[Changes/Claude Code/2026-09-14-added-support-for-a-multiplier-above-1-up-to-10-in-the-modelpricing-managed-sett|Added support for a multiplier above 1, up to 10, in the modelPricing managed…]] · Pricing Model
- [[Changes/Claude Code/2026-09-14-2-files-and-data-changes-in-v2-1-271|2 Files and Data changes in v2.1.271]] · Files and Data
- [[Changes/Claude Code/2026-09-14-5-apps-and-integrations-changes-in-v2-1-271|5 Apps and Integrations changes in v2.1.271]] · Apps and Integrations
- [[Changes/Claude Code/2026-09-14-3-editor-experience-changes-in-v2-1-271|3 Editor Experience changes in v2.1.271]] · Editor Experience
- [[Changes/Claude Code/2026-09-14-2-model-support-changes-in-v2-1-271|2 Model Support changes in v2.1.271]] · Model Support
- [[Changes/Claude Code/2026-09-14-7-safety-and-privacy-changes-in-v2-1-271|7 Safety and Privacy changes in v2.1.271]] · Safety and Privacy
- [[Changes/Claude Code/2026-09-14-improved-the-spinner-status-during-long-thinking-it-now-reads-deep-in-thought-af|Improved the spinner status during long thinking]] · Context Window
- [[Changes/Claude Code/2026-09-14-7-agent-mode-changes-in-v2-1-271|7 Agent Mode changes in v2.1.271]] · Agent Mode
- [[Changes/Claude Code/2026-09-14-improved-terminal-rendering-performance-large-diffs-and-long-transcripts-render|Improved terminal rendering performance]] · Reliability and Performance
- [[Changes/Claude Code/2026-09-14-3-interface-experience-changes-in-v2-1-271|3 Interface Experience changes in v2.1.271]] · Interface Experience
- [[Changes/Claude Code/2026-09-14-improved-mobile-to-show-a-single-qr-code-for-claude-ai-mobile-which-opens-the-ri|Improved /mobile to show a single QR code for claude.ai/mobile, which opens…]] · Mobile and Desktop
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-09-14-c2bf88&body=Card%3A%20Changes%2FClaude%20Code%2F2026-09-14-9-other-changes-in-v2-1-271.md%0ACard%20ID%3A%20claude-code-2026-09-14-c2bf88%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.271%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->