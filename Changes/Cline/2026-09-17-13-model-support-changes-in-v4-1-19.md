---
card_id: cline-2026-09-17-4e3e44
date: '2026-09-17'
description: 'Cline · 2026-09-17 · Model Support: 13 changes in v4.1.19 — Images attached
  to a model that cannot read them are now flagged instead of silently discarded…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1347
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: e1d8758660af26b4852139372741b07ae2c816d90408b8df56841f77e8744f68
product: cline
product_name: Cline
record:
  card_id: cline-2026-09-17-4e3e44
  comparison: ''
  date: '2026-09-17'
  description: 'Cline — v4.1.19: 13 Model Support changes'
  evidence:
  - quote: Images attached to a model that cannot read them are now flagged instead
      of silently discarded. Thumbnails get a warning badge and the composer explains
      that the images will be ignored, with a button to switch to an image-capable
      model. Previously the thumbnail looked normal and the image was replaced with
      a text placeholder just before the request, so there was no way to tell it had
      been dropped. Model info and the attachment picker also report image support
      accurately for models that declare text-only input without listing capabilities.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.19
  - quote: A model turn that fails mid-stream with a transient provider error is now
      retried up to three times with backoff instead of ending the task. A single
      rate-limit response forwarded by a gateway previously surfaced as a failed task.
      A turn that has already streamed output is never retried, so nothing is duplicated.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.19
  - quote: '`apply_patch` no longer silently overwrites an existing file when the
      model uses "Add File" on a path that already exists. The file''s contents were
      replaced with no error and no record of what was lost.'
    source_release: https://github.com/cline/cline/releases/tag/v4.1.19
  - quote: PowerShell commands the model wrapped in another `powershell -Command "..."`
      are no longer parsed twice. The outer shell consumed `$_` before the inner command
      ran, so pipelines using it emitted an error for every item processed while still
      reporting success.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.19
  - quote: The "Supports Images" checkbox in OpenAI Compatible model settings now
      stays where you put it. The checkbox rendered the last committed value, and
      the re-sync that arrived during the save round-trip was re-emitted as a change
      event that wrote the old value back over your edit.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.19
  - quote: The error shown to the model when an `editor` call omits the text to replace
      now names the file and explains how to recover. The previous message was terse
      enough that some models re-sent the identical call until the task stopped.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.19
  - quote: Cline Pass and free models now show no cost rather than the underlying
      market price, which is not what you are billed for.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.19
  - quote: Model pickers now fall back to the full Recommended, Free, and Subscribed
      lists when the models endpoint cannot be reached. The offline fallback was a
      short hardcoded list with no subscription tier at all.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.19
  - quote: Model lists for providers sharing the built-in catalog now refresh from
      the live catalog, so newly published models appear without an extension update,
      with timeouts so an unresponsive provider endpoint cannot stall the list.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.19
  - quote: The OpenAI Codex (ChatGPT subscription) model list no longer offers models
      the backend rejects, and Codex context limits are applied to every Codex model
      instead of being inherited from the OpenAI API catalog, which inflated both
      the context budget and the usage figures derived from it.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.19
  - quote: Models served by OpenCode Go are now sent over the wire protocol each one
      actually speaks. Every model was sent over the OpenAI chat-completions adapter,
      so models on that endpoint speaking other protocols failed or misbehaved.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.19
  - quote: The `run_commands` tool description now names the PowerShell edition in
      use — `Windows PowerShell (powershell.exe)` versus `PowerShell (pwsh.exe)` —
      quotes its guidance against that executable, and tells the model to run commands
      directly rather than wrapping them in another shell invocation. It also no longer
      describes the environment as Windows when `pwsh` is the configured shell on
      macOS or Linux.
    source_release: https://github.com/cline/cline/releases/tag/v4.1.19
  - quote: 'Refreshed the built-in model catalog. Adds four providers (Infer by Flow7,
      Melious, NaN, and Wallaby) and takes the catalog from 5,788 to 6,079 models.
      This is a wide refresh: the resolved default model changes for 44 providers,
      most of them landing on DeepSeek V4.1 Flash — among them Hugging Face, Fireworks,
      Requesty, Nebius, Cortecs, CrossModel, DigitalOcean, Eden AI, and OpenCode Go.
      Gemini and Vertex now resolve to Gemini 3.8 Flash, GitHub Copilot and Vivgrid
      to GPT-6 Astra, and NVIDIA to GLM 5.3 Flash. If you use a provider without pinning
      a model, expect a different default.'
    source_release: https://github.com/cline/cline/releases/tag/v4.1.19
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: cline
  product_name: Cline
  slug: 13-model-support-changes-in-v4-1-19
  source_release: cline-2026-09-17-v4-1-19-github-390521944-270e9514
  source_type: github_releases
  theme: model-support
  title: 13 Model Support changes in v4.1.19
  type: change
related_changes:
- '[[Changes/OpenHands/2026-09-16-feat-add-gpt-6-astra-model-support-by-neubig-in-https-github-com-openhands-openh|feat:
  add GPT-6 Astra model support]]'
- '[[Changes/Claude Code/2026-09-17-2-model-support-changes-in-v2-1-274|2 Model Support
  changes in v2.1.274]]'
- '[[Changes/Claude Code/2026-09-17-added-a-send-now-key-ctrl-enter-or-ctrl-x-ctrl-s-that-interrupts-the-current-tur|Added
  a send-now key (ctrl+enter, or ctrl+x ctrl+s) that interrupts the current turn…]]'
source_release: '[[Releases/Cline/cline-2026-09-17-v4-1-19-github-390521944-270e9514|cline-2026-09-17-v4-1-19-github-390521944-270e9514]]'
source_type: github_releases
theme: model-support
title: 13 Model Support changes in v4.1.19
type: change
---

<!-- chronolog:begin region="header" -->
# 13 Model Support changes in v4.1.19

**Cline** · 2026-09-17 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/cline/cline/releases/tag/v4.1.19) · from [[Releases/Cline/cline-2026-09-17-v4-1-19-github-390521944-270e9514|v4.1.19]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Images attached to a model that cannot read them are now flagged instead of silently discarded. Thumbnails get a warning badge and the composer explains that the images will be ignored, with a button to switch to an image-capable model. Previously the thumbnail looked normal and the image was replaced with a text placeholder just before the request, so there was no way to tell it had been dropped. Model info and the attachment picker also report image support accurately for models that declare text-only input without listing capabilities.

> A model turn that fails mid-stream with a transient provider error is now retried up to three times with backoff instead of ending the task. A single rate-limit response forwarded by a gateway previously surfaced as a failed task. A turn that has already streamed output is never retried, so nothing is duplicated.

> `apply_patch` no longer silently overwrites an existing file when the model uses "Add File" on a path that already exists. The file's contents were replaced with no error and no record of what was lost.

> PowerShell commands the model wrapped in another `powershell -Command "..."` are no longer parsed twice. The outer shell consumed `$_` before the inner command ran, so pipelines using it emitted an error for every item processed while still reporting success.

> The "Supports Images" checkbox in OpenAI Compatible model settings now stays where you put it. The checkbox rendered the last committed value, and the re-sync that arrived during the save round-trip was re-emitted as a change event that wrote the old value back over your edit.

> The error shown to the model when an `editor` call omits the text to replace now names the file and explains how to recover. The previous message was terse enough that some models re-sent the identical call until the task stopped.

> Cline Pass and free models now show no cost rather than the underlying market price, which is not what you are billed for.

> Model pickers now fall back to the full Recommended, Free, and Subscribed lists when the models endpoint cannot be reached. The offline fallback was a short hardcoded list with no subscription tier at all.

> Model lists for providers sharing the built-in catalog now refresh from the live catalog, so newly published models appear without an extension update, with timeouts so an unresponsive provider endpoint cannot stall the list.

> The OpenAI Codex (ChatGPT subscription) model list no longer offers models the backend rejects, and Codex context limits are applied to every Codex model instead of being inherited from the OpenAI API catalog, which inflated both the context budget and the usage figures derived from it.

> Models served by OpenCode Go are now sent over the wire protocol each one actually speaks. Every model was sent over the OpenAI chat-completions adapter, so models on that endpoint speaking other protocols failed or misbehaved.

> The `run_commands` tool description now names the PowerShell edition in use — `Windows PowerShell (powershell.exe)` versus `PowerShell (pwsh.exe)` — quotes its guidance against that executable, and tells the model to run commands directly rather than wrapping them in another shell invocation. It also no longer describes the environment as Windows when `pwsh` is the configured shell on macOS or Linux.

> Refreshed the built-in model catalog. Adds four providers (Infer by Flow7, Melious, NaN, and Wallaby) and takes the catalog from 5,788 to 6,079 models. This is a wide refresh: the resolved default model changes for 44 providers, most of them landing on DeepSeek V4.1 Flash — among them Hugging Face, Fireworks, Requesty, Nebius, Cortecs, CrossModel, DigitalOcean, Eden AI, and OpenCode Go. Gemini and Vertex now resolve to Gemini 3.8 Flash, GitHub Copilot and Vivgrid to GPT-6 Astra, and NVIDIA to GLM 5.3 Flash. If you use a provider without pinning a model, expect a different default.

Source: https://github.com/cline/cline/releases/tag/v4.1.19
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Cline/2026-09-17-on-windows-opening-a-repository-that-contains-a-file-named-rg-exe-git-exe-or-pow|On Windows, opening a repository that contains a file named rg.exe, git.exe…]] · Mobile and Desktop
- [[Changes/Cline/2026-09-17-2-developer-workflow-changes-in-v4-1-19|2 Developer Workflow changes in v4.1.19]] · Developer Workflow
- [[Changes/Cline/2026-09-17-task-history-no-longer-goes-blank-when-a-task-spawns-many-subagents-subagent-row|Task history no longer goes blank when a task spawns many subagents]] · Agent Mode
- [[Changes/Cline/2026-09-17-long-tasks-now-compact-when-they-actually-need-to-rather-than-running-out-of-roo|Long tasks now compact when they actually need to rather than running out of room]] · Context Window
- [[Changes/Cline/2026-09-17-cline-pass-now-defaults-to-a-model-from-your-subscription-rather-than-a-free-one|Cline Pass now defaults to a model from your subscription rather than a free one]] · Pricing Model
- [[Changes/Cline/2026-09-17-web-search-is-now-enabled-by-default-on-models-that-support-it-outside-yolo-mode|Web search is now enabled by default on models that support it, outside YOLO mode]] · Search and Browsing
- [[Changes/Cline/2026-09-17-cline-s-logo-and-icons-have-been-refreshed-throughout-the-extension-including-th|Cline's logo and icons have been refreshed throughout the extension, including…]] · Interface Experience
- [[Changes/Cline/2026-09-17-terminal-commands-that-succeed-without-printing-anything-git-add-a-on-a-clean-tr|Terminal commands that succeed without printing anything…]] · Apps and Integrations
- [[Changes/Cline/2026-09-17-5-other-changes-in-v4-1-19|5 other changes in v4.1.19]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-09-17 · Claude Code · [[Changes/Claude Code/2026-09-17-added-a-send-now-key-ctrl-enter-or-ctrl-x-ctrl-s-that-interrupts-the-current-tur|Added a send-now key (ctrl+enter, or ctrl+x ctrl+s) that interrupts the current turn…]]
- Later: 2026-09-17 · Codex CLI · [[Changes/Codex CLI/2026-09-17-13-model-support-changes-in-rust-v0-155-0|13 Model Support changes in rust-v0.155.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20cline-2026-09-17-4e3e44&body=Card%3A%20Changes%2FCline%2F2026-09-17-13-model-support-changes-in-v4-1-19.md%0ACard%20ID%3A%20cline-2026-09-17-4e3e44%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fcline%2Fcline%2Freleases%2Ftag%2Fv4.1.19%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->