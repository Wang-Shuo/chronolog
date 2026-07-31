---
card_id: claude-code-2026-06-25-82838a
date: '2026-06-25'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|chatgpt-2023-01-09-5af3d4]]'
  lag_days: 1263
  role: follower
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-06-19-added-a-warning-when-the-requested-model-is-deprecated-or-automatically-updated|claude-code-2026-06-19-7f158e]]'
extractor_version: fallback-v2
impact: significant
machine_hash: 93cae6d2ea8fc6e63c181ed44d40be1142f7686628a303ca3110d8448558cac6
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-06-12-added-enforceavailablemodels-managed-setting-when-enabled-the-availablemodels-al|claude-code-2026-06-12-f8c57e]]'
- '[[Changes/Claude Code/2026-06-19-added-a-warning-when-the-requested-model-is-deprecated-or-automatically-updated|claude-code-2026-06-19-7f158e]]'
- '[[Changes/ChatGPT/2026-06-24-we-re-updating-gpt-5-5-instant-our-most-used-model-in-chatgpt-to-improve-convers|chatgpt-2026-06-24-0f2a65]]'
source_release: '[[Releases/Claude Code/claude-code-2026-06-25-v2-1-193-github-344922230-0655000d|claude-code-2026-06-25-v2-1-193-github-344922230-0655000d]]'
theme: model-support
type: change
---

# Added `claude_code.assistant_response` OpenTelemetry log event containing the mo

<!-- chronolog:begin region="description" -->
Added `claude_code.assistant_response` OpenTelemetry log event containing the model's response text. Redacted unless `OTEL_LOG_ASSISTANT_RESPONSES=1`; when that var is unset it follows `OTEL_LOG_USER_PROMPTS`, so deployments that already log prompt content will start receiving response content on upgrade — set `OTEL_LOG_ASSISTANT_RESPONSES=0` to keep prompts-only.
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `claude_code.assistant_response` OpenTelemetry log event containing the model's response text. Redacted unless `OTEL_LOG_ASSISTANT_RESPONSES=1`; when that var is unset it follows `OTEL_LOG_USER_PROMPTS`, so deployments that already log prompt content will start receiving response content on upgrade — set `OTEL_LOG_ASSISTANT_RESPONSES=0` to keep prompts-only.
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.193
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-06-19-added-a-warning-when-the-requested-model-is-deprecated-or-automatically-updated|claude-code-2026-06-19-7f158e]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: model-support
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|chatgpt-2023-01-09-5af3d4]]
- Lag Days: 1263
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes