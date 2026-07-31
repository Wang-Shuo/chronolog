---
card_id: chatgpt-2026-07-06-367b99
date: '2026-07-06'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|chatgpt-2023-01-09-5af3d4]]'
  lag_days: 1274
  role: variant
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 3
evolves_from:
- '[[Changes/ChatGPT/2026-06-26-as-of-june-26-2026-gpt-4-5-is-no-longer-available-in-chatgpt-including-for-custo|chatgpt-2026-06-26-46ba84]]'
extractor_version: fallback-v2
impact: significant
machine_hash: d3405ad7ff8a5286582a2c57a541e2c10e1147cdcd629f3da9f01b0764da577a
product: chatgpt
product_name: ChatGPT
related_changes:
- '[[Changes/Claude Code/2026-06-29-added-support-for-organization-default-models-admins-set-it-in-the-org-console-i|claude-code-2026-06-29-34190b]]'
- '[[Changes/Claude Code/2026-07-01-gateway-added-claude-platform-on-aws-anthropicaws-as-an-upstream-provider-model|claude-code-2026-07-01-d0f0de]]'
- '[[Changes/Claude Code/2026-07-03-claude-sonnet-5-sessions-no-longer-use-the-mid-conversation-system-role-for-harn|claude-code-2026-07-03-8405a6]]'
source_release: '[[Releases/ChatGPT/chatgpt-2026-07-06-gpt-5-5-instant-mini-in-chatgpt-1ce53754|chatgpt-2026-07-06-gpt-5-5-instant-mini-in-chatgpt-1ce53754]]'
theme: model-support
type: change
---

# We’re rolling out GPT-5.5 Instant Mini in ChatGPT. It replaces GPT-5.3 Instant M

<!-- chronolog:begin region="description" -->
We’re rolling out GPT-5.5 Instant Mini in ChatGPT. It replaces GPT-5.3 Instant Mini as the fallback model users reach after hitting their GPT-5.5 Instant or Auto rate limits. Because it serves as a fallback, it won’t appear in the model picker. This update does not affect the API or Codex. Compared with GPT-5.3 Instant Mini, GPT-5.5 Instant Mini better tracks evolving user intent, calibrates tone, and avoids repetitive or overly structured responses. Testing also showed stronger personalization and fewer factual issues.
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> We’re rolling out GPT-5.5 Instant Mini in ChatGPT. It replaces GPT-5.3 Instant Mini as the fallback model users reach after hitting their GPT-5.5 Instant or Auto rate limits. Because it serves as a fallback, it won’t appear in the model picker. This update does not affect the API or Codex. Compared with GPT-5.3 Instant Mini, GPT-5.5 Instant Mini better tracks evolving user intent, calibrates tone, and avoids repetitive or overly structured responses. Testing also showed stronger personalization and fewer factual issues.
>
> Source: https://help.openai.com/en/articles/6825453-chatgpt-release-notes#gpt-55-instant-mini-in-chatgpt
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/ChatGPT/2026-06-26-as-of-june-26-2026-gpt-4-5-is-no-longer-available-in-chatgpt-including-for-custo|chatgpt-2026-06-26-46ba84]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: model-support
- Scope: tracked-products-only
- Role: variant
- First In Tracked: [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|chatgpt-2023-01-09-5af3d4]]
- Lag Days: 1274
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes