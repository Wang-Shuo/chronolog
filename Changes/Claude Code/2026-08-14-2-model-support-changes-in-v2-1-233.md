---
card_id: claude-code-2026-08-14-aabc3f
date: '2026-08-14'
description: 'Claude Code · 2026-08-14 · Model Support: 2 changes in v2.1.233 — Improved
  print mode diagnostics: a `[claude-code:unrecognized_model]` line is written to…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1313
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: e64b2801e6b7a42702474b657dd88c791b9d115fd7885dd3dbe9b5412b950d37
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-08-14-aabc3f
  comparison: ''
  date: '2026-08-14'
  description: 'Claude Code — v2.1.233: 2 Model Support changes'
  evidence:
  - quote: 'Improved print mode diagnostics: a `[claude-code:unrecognized_model]`
      line is written to stderr when a request goes out for a model ID Claude Code
      doesn''t recognize; map it with `modelOverrides` to silence'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.233
  - quote: Todo/task-tracking tools (TaskCreate/Get/Update/List, TodoWrite) are no
      longer available on Opus 4.8, Sonnet 5, Fable 5, Mythos 5, and newer models;
      set `CLAUDE_CODE_ENABLE_TODO_TOOLS=1` to bring them back
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.233
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: claude-code
  product_name: Claude Code
  slug: 2-model-support-changes-in-v2-1-233
  source_release: claude-code-2026-08-14-v2-1-233-github-370762090-de6823a9
  source_type: github_releases
  theme: model-support
  title: 2 Model Support changes in v2.1.233
  type: change
related_changes:
- '[[Changes/DeepSeek API/2026-08-13-deepseek-v4-pro-update|DeepSeek-V4-Pro Update]]'
- '[[Changes/Lovable/2026-08-13-image-editing-with-openai-models-for-your-app-s-ai-features|Image
  editing with OpenAI models for your app''s AI features]]'
- '[[Changes/OpenCode/2026-08-13-core-fix-xhigh-reasoning-effort-for-xai-models|Core
  Fix xhigh reasoning effort for xai models]]'
source_release: '[[Releases/Claude Code/claude-code-2026-08-14-v2-1-233-github-370762090-de6823a9|claude-code-2026-08-14-v2-1-233-github-370762090-de6823a9]]'
source_type: github_releases
theme: model-support
title: 2 Model Support changes in v2.1.233
type: change
---

<!-- chronolog:begin region="header" -->
# 2 Model Support changes in v2.1.233

**Claude Code** · 2026-08-14 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.233) · from [[Releases/Claude Code/claude-code-2026-08-14-v2-1-233-github-370762090-de6823a9|v2.1.233]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Improved print mode diagnostics: a `[claude-code:unrecognized_model]` line is written to stderr when a request goes out for a model ID Claude Code doesn't recognize; map it with `modelOverrides` to silence

> Todo/task-tracking tools (TaskCreate/Get/Update/List, TodoWrite) are no longer available on Opus 4.8, Sonnet 5, Fable 5, Mythos 5, and newer models; set `CLAUDE_CODE_ENABLE_TODO_TOOLS=1` to bring them back

Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.233
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-08-14-3-safety-and-privacy-changes-in-v2-1-233|3 Safety and Privacy changes in v2.1.233]] · Safety and Privacy
- [[Changes/Claude Code/2026-08-14-improved-screen-reader-mode-the-effort-selector-renders-as-a-numbered-list-with|Improved screen reader mode]] · Accessibility and Localization
- [[Changes/Claude Code/2026-08-14-changed-the-github-app-setup-tip-to-no-longer-appear-in-repositories-whose-origi|Changed the GitHub app setup tip to no longer appear in repositories whose origin…]] · Enterprise and Administration
- [[Changes/Claude Code/2026-08-14-improved-apps-gateway-error-forwarding-400-413-errors-from-vertex-foundry-and-cl|Improved apps gateway error forwarding]] · Context Window
- [[Changes/Claude Code/2026-08-14-improved-claude-self-hosted-runner-session-start-time-the-session-branch-is-now|Improved claude self-hosted-runner session start time]] · Agent Mode
- [[Changes/Claude Code/2026-08-14-added-opt-in-memory-cgroup-support-for-bash-tool-commands-on-linux-claude-code-t|Added opt-in memory cgroup support for Bash tool commands on Linux…]] · Reliability and Performance
- [[Changes/Claude Code/2026-08-14-added-gitlab-merge-request-url-support-to-the-worktree-flag-and-the-claude-agent|Added GitLab merge request URL support to the --worktree flag…]] · Developer Workflow
- [[Changes/Claude Code/2026-08-14-2-apps-and-integrations-changes-in-v2-1-233|2 Apps and Integrations changes in v2.1.233]] · Apps and Integrations
- [[Changes/Claude Code/2026-08-14-added-claude-code-webfetch-cache-ttl-ms-environment-variable-to-configure-the-we|Added CLAUDE_CODE_WEBFETCH_CACHE_TTL_MS environment variable to configure…]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-08-13 · OpenCode · [[Changes/OpenCode/2026-08-13-core-fix-xhigh-reasoning-effort-for-xai-models|Core Fix xhigh reasoning effort for xai models]]
- Later: 2026-08-14 · Cline · [[Changes/Cline/2026-08-14-2-model-support-changes-in-v4-1-10|2 Model Support changes in v4.1.10]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-08-14-aabc3f&body=Card%3A%20Changes%2FClaude%20Code%2F2026-08-14-2-model-support-changes-in-v2-1-233.md%0ACard%20ID%3A%20claude-code-2026-08-14-aabc3f%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.233%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->