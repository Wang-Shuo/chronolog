---
card_id: github-copilot-cli-2026-11-06-95fd7e
date: '2026-11-06'
description: 'GitHub Copilot CLI · 2026-11-06 · Model Support: 33 changes in 1.0.106
  — Add GPT-6.1 Terra as a selectable model under New models when available to your
  account'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1397
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 99b9782d2576af0dfe3b396070b79075304868c055a2d7bb4dc6264dcfe35150
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-11-06-95fd7e
  comparison: ''
  date: '2026-11-06'
  description: 'GitHub Copilot CLI — 1.0.106: 33 Model Support changes'
  evidence:
  - quote: Add GPT-6.1 Terra as a selectable model under New models when available
      to your account
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: 'A model request that Copilot''s service answers with an empty 404 while
      under load is now retried instead of ending the turn with "Execution failed:
      404".'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: web_fetch now decodes an XML document (RSS, Atom or other XML) in the encoding
      its XML declaration names when the server sends no charset, so ISO-8859-1 and
      other non-UTF-8 feeds no longer reach the model with their accented characters
      replaced.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: When a Claude model declines a request after it has started a tool call,
      the fallback retry no longer fails with an unmatched tool_use error and keeps
      its fallback credit.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Quick questions now report an explicit error when the model returns no
      answer text.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Allow --continue and --resume to send prompts when resuming a session with
      no recorded model
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Keep the footer's model display up to date after a session resync
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: /chronicle cost reports count each newly recorded model call once, even
      when its usage event is received again
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: MAI-Code-1.1-Flash requests no longer fail with `unsupported_api_for_model`
      when the model is missing from the model list (for example as a HydraFusion
      constituent); they now use the Responses API.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: A HydraFusion turn that cannot retrieve the model catalog now says so,
      instead of blaming the allowed-model policy
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Long conversations now recover from oversized requests by trimming historical
      reasoning and retrying.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Skill calls explain when model invocation is disabled instead of reporting
      the skill as not found
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Local models added from the /model picker now stay under their provider's
      section when grouped by vendor, instead of moving to Other models
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Fallback retries now succeed when Claude refusals end with reasoning blocks.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: A prompt hook that returns an empty modifiedPrompt or modifiedTransformedPrompt
      no longer sends the model an empty prompt. A hook value that is ignored because
      it is empty or not a string now shows a warning naming the field.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Gemini models automatically defer tools behind search when requests exceed
      the 512-function limit.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Copilot Free signup completes when account setup overlaps model refreshes
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: The Getting started box no longer suggests /model in sessions that use
      a model from your own provider, where /model is not available.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: When `web_fetch` cuts a page at its 10 MiB limit, the model is now told
      the page was truncated even when the cut falls inside a script, style sheet
      or HTML comment.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Restart keeps your current /model selection after switching models in-session
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Auto model routing now preserves your selected Auto tier when account policy
      refreshes during startup
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Text pasted over several lines after `/clear`, `/new`, `/ask`, `/delegate`
      or `/diagnose` keeps its line breaks and indentation instead of reaching the
      model as one line
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: web_fetch now decodes pages in the character encoding they declare (Content-Type
      charset or a meta tag), so ISO-8859-1, windows-1252 and other non-UTF-8 pages
      no longer reach the model with their accented characters replaced.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Return the original refusal when an organization disables a Claude fallback
      model
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: A file edit that fails on a missing file, a read-only file or a directory
      no longer sends the whole edit back to the model; the error names the command,
      the path and the cause.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Keep the original refusal response when a fallback model is unavailable
      during retry
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Recover prompt submission after startup model loading fails once model
      selection succeeds
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Gemini tool calls work when MCP server names include unsupported characters
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Reduce request-size failures for Gemini and Kimi when tool screenshots
      are included
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Gemini 4 Argon now uses safer token estimates to reduce context-overflow
      request failures
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Gemini 400 invalid request body errors now name the MCP servers whose newly
      added or changed tools may have caused them.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Windows local model downloads install llama.cpp automatically and show
      engine installation progress.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Remove retired models from CLI model lists and model picker results
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 33-model-support-changes-in-v1-0-106
  source_release: github-copilot-cli-2026-11-06-v1-0-106-github-435988160-ec5b15d4
  source_type: github_releases
  theme: model-support
  title: 33 Model Support changes in v1.0.106
  type: change
related_changes:
- '[[Changes/Claude Code/2026-10-31-deprecated-fast-mode-for-opus-4-8-as-of-october-30-2026-it-will-be-removed-on-no|Deprecated
  fast mode for Opus 4.8 as of October 30, 2026]]'
- '[[Changes/Gemini CLI/2026-11-04-feat-cli-add-models-command-and-list-models-flag-for-model-discovery-by-urielefr|feat(cli):
  add models command and --list-models flag for model discovery]]'
- '[[Changes/Codex CLI/2026-11-06-7-model-support-changes-in-rust-v0-167-0|7 Model
  Support changes in rust-v0.167.0]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-11-06-v1-0-106-github-435988160-ec5b15d4|github-copilot-cli-2026-11-06-v1-0-106-github-435988160-ec5b15d4]]'
source_type: github_releases
theme: model-support
title: 33 Model Support changes in v1.0.106
type: change
---

<!-- chronolog:begin region="header" -->
# 33 Model Support changes in v1.0.106

**GitHub Copilot CLI** · 2026-11-06 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.106) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-11-06-v1-0-106-github-435988160-ec5b15d4|1.0.106]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Add GPT-6.1 Terra as a selectable model under New models when available to your account

> A model request that Copilot's service answers with an empty 404 while under load is now retried instead of ending the turn with "Execution failed: 404".

> web_fetch now decodes an XML document (RSS, Atom or other XML) in the encoding its XML declaration names when the server sends no charset, so ISO-8859-1 and other non-UTF-8 feeds no longer reach the model with their accented characters replaced.

> When a Claude model declines a request after it has started a tool call, the fallback retry no longer fails with an unmatched tool_use error and keeps its fallback credit.

> Quick questions now report an explicit error when the model returns no answer text.

> Allow --continue and --resume to send prompts when resuming a session with no recorded model

> Keep the footer's model display up to date after a session resync

> /chronicle cost reports count each newly recorded model call once, even when its usage event is received again

> MAI-Code-1.1-Flash requests no longer fail with `unsupported_api_for_model` when the model is missing from the model list (for example as a HydraFusion constituent); they now use the Responses API.

> A HydraFusion turn that cannot retrieve the model catalog now says so, instead of blaming the allowed-model policy

> Long conversations now recover from oversized requests by trimming historical reasoning and retrying.

> Skill calls explain when model invocation is disabled instead of reporting the skill as not found

> Local models added from the /model picker now stay under their provider's section when grouped by vendor, instead of moving to Other models

> Fallback retries now succeed when Claude refusals end with reasoning blocks.

> A prompt hook that returns an empty modifiedPrompt or modifiedTransformedPrompt no longer sends the model an empty prompt. A hook value that is ignored because it is empty or not a string now shows a warning naming the field.

> Gemini models automatically defer tools behind search when requests exceed the 512-function limit.

> Copilot Free signup completes when account setup overlaps model refreshes

> The Getting started box no longer suggests /model in sessions that use a model from your own provider, where /model is not available.

> When `web_fetch` cuts a page at its 10 MiB limit, the model is now told the page was truncated even when the cut falls inside a script, style sheet or HTML comment.

> Restart keeps your current /model selection after switching models in-session

> Auto model routing now preserves your selected Auto tier when account policy refreshes during startup

> Text pasted over several lines after `/clear`, `/new`, `/ask`, `/delegate` or `/diagnose` keeps its line breaks and indentation instead of reaching the model as one line

> web_fetch now decodes pages in the character encoding they declare (Content-Type charset or a meta tag), so ISO-8859-1, windows-1252 and other non-UTF-8 pages no longer reach the model with their accented characters replaced.

> Return the original refusal when an organization disables a Claude fallback model

> A file edit that fails on a missing file, a read-only file or a directory no longer sends the whole edit back to the model; the error names the command, the path and the cause.

> Keep the original refusal response when a fallback model is unavailable during retry

> Recover prompt submission after startup model loading fails once model selection succeeds

> Gemini tool calls work when MCP server names include unsupported characters

> Reduce request-size failures for Gemini and Kimi when tool screenshots are included

> Gemini 4 Argon now uses safer token estimates to reduce context-overflow request failures

> Gemini 400 invalid request body errors now name the MCP servers whose newly added or changed tools may have caused them.

> Windows local model downloads install llama.cpp automatically and show engine installation progress.

> Remove retired models from CLI model lists and model picker results

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
- [[Changes/GitHub Copilot CLI/2026-11-06-34-safety-and-privacy-changes-in-v1-0-106|34 Safety and Privacy changes in v1.0.106]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-11-06-9-collaboration-changes-in-v1-0-106|9 Collaboration changes in v1.0.106]] · Collaboration
- [[Changes/GitHub Copilot CLI/2026-11-06-8-mobile-and-desktop-changes-in-v1-0-106|8 Mobile and Desktop changes in v1.0.106]] · Mobile and Desktop
- [[Changes/GitHub Copilot CLI/2026-11-06-4-projects-and-workspaces-changes-in-v1-0-106|4 Projects and Workspaces changes in v1.0.106]] · Projects and Workspaces
- [[Changes/GitHub Copilot CLI/2026-11-06-8-accessibility-and-localization-changes-in-v1-0-106|8 Accessibility and Localization changes in v1.0.106]] · Accessibility and Localization
- [[Changes/GitHub Copilot CLI/2026-11-06-17-context-window-changes-in-v1-0-106|17 Context Window changes in v1.0.106]] · Context Window
- [[Changes/GitHub Copilot CLI/2026-11-06-57-editor-experience-changes-in-v1-0-106|57 Editor Experience changes in v1.0.106]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-11-06-89-apps-and-integrations-changes-in-v1-0-106|89 Apps and Integrations changes in v1.0.106]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-11-06-2-image-generation-changes-in-v1-0-106|2 Image Generation changes in v1.0.106]] · Image Generation
- [[Changes/GitHub Copilot CLI/2026-11-06-42-interface-experience-changes-in-v1-0-106|42 Interface Experience changes in v1.0.106]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-11-06-5-pricing-model-changes-in-v1-0-106|5 Pricing Model changes in v1.0.106]] · Pricing Model
- [[Changes/GitHub Copilot CLI/2026-11-06-in-the-every-schedule-manager-x-now-removes-the-highlighted-schedule-even-after|In the /every schedule manager, x now removes the highlighted schedule even after…]] · Automation and Scheduling
- [[Changes/GitHub Copilot CLI/2026-11-06-23-account-and-access-changes-in-v1-0-106|23 Account and Access changes in v1.0.106]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-11-06-172-other-changes-in-v1-0-106|172 other changes in v1.0.106]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-11-06 · Codex CLI · [[Changes/Codex CLI/2026-11-06-7-model-support-changes-in-rust-v0-167-0|7 Model Support changes in rust-v0.167.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-11-06-95fd7e&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-11-06-33-model-support-changes-in-v1-0-106.md%0ACard%20ID%3A%20github-copilot-cli-2026-11-06-95fd7e%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.106%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->