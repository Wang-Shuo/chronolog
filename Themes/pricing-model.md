---
created: '2022-12-15'
date: '2026-09-29'
machine_hash: 6723afdd92b9b4e2313410bd1cb9e0c23621259441e3b02bc7449e7b35c921e6
modified: '2026-09-29'
products_involved:
- ChatGPT
- Claude Code
- Cursor
publication: active
status: official
tags:
- theme
- moc
theme: pricing-model
title: Pricing Model
---

# Theme: pricing-model

## Research summary
<!-- chronolog:begin region="narrative" -->
**Research question: what is being charged for, and what does a plan unlock?**

Cursor's [2025-05-15 announcement](https://cursor.com/changelog/0-50) distinguishes request-based ordinary usage from token-based Max Mode and says plan quotas were unchanged at that time. It is a dated mechanism change, not a current price list.

ChatGPT's [2026-04-09 Pro changes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes#new-pro-plan-options) introduce a $100/month Pro option alongside $200/month Pro and describe usage allowances. The [2026-09-29 Pro 500 announcement](https://help.openai.com/en/articles/6825453-chatgpt-release-notes#a-new-pro-plan-with-astra-ultrafast) adds a $500/month tier and gates Ultrafast to that tier: buying credits on Pro 100 or Pro 200 does not unlock it. Included allowances and purchased credits are distinct from feature eligibility.

Claude Code's [v2.1.296](https://github.com/anthropics/claude-code/releases/tag/v2.1.296) updates displayed Sonnet 5.5 cache-read cost figures from $0.20 to $0.10 per million tokens in cost reporting and budget controls. A client cost-accounting update is not evidence of a new Claude subscription price or of every user's billed price.

**Uncertainty and scope:** tracked-products-only. Subscriptions, requests, token metering, credits and client cost estimates are different mechanisms. Prices are historical statements with plan and rollout qualifications. This evidence does not support “one product followed another,” universal price comparisons, or claims about current invoices. References to shopping prices are outside this theme unless they change the AI product's own charging mechanism.
<!-- chronolog:end -->

## Cross-Product Timeline
<!-- chronolog:begin region="timeline" -->
Scope: tracked-products-only. Entries show same-theme chronology; they do not establish equivalent capabilities, adoption, or causation.

### 2026

- 2026-09-29 · ChatGPT: [[Changes/ChatGPT/2026-09-29-among-pro-plans-ultrafast-is-available-only-with-pro-500-buying-credits-on-pro-1|Among Pro plans, Ultrafast is available only with Pro 500. Buying credits on Pro]]
- 2026-09-29 · ChatGPT: [[Changes/ChatGPT/2026-09-29-we-re-introducing-pro-500-a-new-500-month-plan-with-the-highest-included-usage-o|We’re introducing Pro 500, a new USD 500/month plan with the highest included usage]]
- 2026-09-29 · ChatGPT: [[Changes/ChatGPT/2026-09-29-included-usage-allowances-are-changing-users-affected-by-these-changes-will-rece|Included usage allowances are changing. Users affected by these changes will rec]]
- 2026-09-29 · ChatGPT: [[Changes/ChatGPT/2026-09-29-pro-200-is-available-for-new-subscriptions-again-at-200-month|Pro 200 is available for new subscriptions again at USD 200/month.]]
- 2026-09-28 · Claude Code: [[Changes/Claude Code/2026-09-28-added-dollar-amounts-to-the-claude-apps-gateway-spend-limit-in-usage-and-the-sta|Added dollar amounts to the Claude apps gateway spend limit in /usage and the]]
- 2026-09-19 · Claude Code: [[Changes/Claude Code/2026-09-19-changed-auto-mode-for-claude-api-and-enterprise-users-and-on-bedrock-vertex-foun|Changed auto mode for Claude API and Enterprise users, and on Bedrock, Vertex, F]]
- 2026-09-10 · Claude Code: [[Changes/Claude Code/2026-09-10-added-to-the-claude-apps-gateway-with-pricing-set-in-gateway-yaml-signed-in-clau|Added to the Claude apps gateway: with pricing: set in gateway.yaml, signed-]]
- 2026-09-09 · ChatGPT: [[Changes/ChatGPT/2026-09-09-pro-100-month-up-to-15-hours-with-gpt-live-1|Pro (USD 100/month): Up to 15 hours with GPT-Live-1.]]
- 2026-08-28 · Claude Code: [[Changes/Claude Code/2026-08-28-added-a-per-session-prompt-cache-line-to-cost-hit-ratio-misses-tokens-re-cached|Added a per-session prompt-cache line to /cost (hit ratio, misses, tokens re-c]]
- 2026-07-29 · ChatGPT: [[Changes/ChatGPT/2026-07-29-research-rarely-happens-alone-chatgpt-for-academic-researchers-gives-faculty-and|Research rarely happens alone. ChatGPT for Academic Researchers gives faculty an]]
- 2026-07-28 · Cursor: [[Changes/Cursor/2026-07-28-start-bills-monthly-with-auto-renewal-and-is-available-from-july-28-2026|Start bills monthly with auto-renewal and is available from July 28, 2026.]]
- 2026-07-28 · Cursor: [[Changes/Cursor/2026-07-28-we-re-introducing-cursor-start-a-new-649-monthly-plan-for-developers-in-india-ma|We're introducing Cursor Start, a new ₹649 monthly plan for developers in India,]]
- 2026-07-22 · Cursor: [[Changes/Cursor/2026-07-22-cost-good-quality-reaching-the-highest-available-intelligence-while-optimizing-t|Cost: Good quality, reaching the highest available intelligence while optimizing]]
- 2026-05-19 · Claude Code: [[Changes/Claude Code/2026-05-19-renamed-extra-usage-to-usage-credits-across-cli-copy-extra-usage-is-now-usage-cr|Renamed "extra usage" to "usage credits" across CLI copy; /extra-usage is now]]
- 2026-05-18 · Cursor: [[Changes/Cursor/2026-05-18-standard-0-50-m-input-2-50-m-output-tokens|Standard: USD 0.50/M input, USD 2.50/M output tokens]]
- 2026-05-18 · Cursor: [[Changes/Cursor/2026-05-18-fast-default-3-00-m-input-15-00-m-output-tokens|Fast (default): USD 3.00/M input, USD 15.00/M output tokens]]
- 2026-05-15 · Claude Code: [[Changes/Claude Code/2026-05-15-added-projected-context-cost-per-turn-and-per-invocation-token-estimates-to-the|Added projected context cost (per-turn and per-invocation token estimates) to th]]
- 2026-05-11 · Cursor: [[Changes/Cursor/2026-05-11-customers-must-be-on-usage-based-billing-for-bugbot-to-customize-effort-levels-l|Customers must be on usage-based billing for Bugbot to customize effort levels.]]
- 2026-04-09 · ChatGPT: [[Changes/ChatGPT/2026-04-09-you-can-upgrade-switch-or-cancel-your-plan-from-settings-my-plan-or-from-the-pri|You can upgrade, switch, or cancel your plan from Settings  My Plan or from the]]
- 2026-04-09 · ChatGPT: [[Changes/ChatGPT/2026-04-09-pro-200-month-our-highest-usage-option-remains-available-and-continues-on-its-cu|Pro (USD 200/month): Our highest-usage option remains available and continues on it]]
- 2026-04-09 · ChatGPT: [[Changes/ChatGPT/2026-04-09-plus-20-month-plus-remains-best-for-steady-day-to-day-use-as-the-temporary-codex|Plus (USD 20/month): Plus remains best for steady, day-to-day use. As the temporary]]
- 2026-04-09 · ChatGPT: [[Changes/ChatGPT/2026-04-09-we-re-introducing-a-new-100-month-pro-plan-and-updating-how-codex-usage-works-ac|We’re introducing a new USD 100/month Pro plan and updating how Codex usage works a]]
- 2026-04-09 · ChatGPT: [[Changes/ChatGPT/2026-04-09-pro-100-month-built-for-longer-high-intensity-codex-sessions-it-includes-unlimit|Pro (USD 100/month): Built for longer, high-intensity Codex sessions. It includes u]]
- 2026-04-04 · Claude Code: [[Changes/Claude Code/2026-04-04-added-per-model-and-cache-hit-breakdown-to-cost-for-subscription-users|Added per-model and cache-hit breakdown to /cost for subscription users]]
- 2026-03-19 · Cursor: [[Changes/Cursor/2026-03-19-fast-default-1-50-m-input-7-50-m-output-tokens|Fast (default): USD 1.50/M input, USD 7.50/M output tokens]]
- 2026-03-19 · Cursor: [[Changes/Cursor/2026-03-19-standard-0-50-m-input-2-50-m-output-tokens|Standard: USD 0.50/M input, USD 2.50/M output tokens]]
- 2026-03-10 · ChatGPT: [[Changes/ChatGPT/2026-03-10-eligible-chatgpt-plus-and-pro-users-can-now-turn-on-auto-top-up-for-credits-used|Eligible ChatGPT Plus and Pro users can now turn on auto top-up for credits used]]
- 2026-03-10 · ChatGPT: [[Changes/ChatGPT/2026-03-10-you-can-manage-auto-top-up-from-codex-settings-usage-dashboard-auto-top-up-appli|You can manage auto top-up from Codex Settings → Usage Dashboard. Auto top-up ap]]

### 2025

- 2025-11-03 · ChatGPT: [[Changes/ChatGPT/2025-11-03-eligible-customers-in-india-can-now-get-12-months-of-chatgpt-go-at-no-cost-new-u|Eligible customers in India can now get 12 months of ChatGPT Go at no cost. New]]
- 2025-10-30 · ChatGPT: [[Changes/ChatGPT/2025-10-30-we-re-excited-to-announce-that-chatgpt-go-our-low-cost-subscription-plan-is-now-44be9d|We're excited to announce that ChatGPT Go, our low cost subscription plan, is no]]
- 2025-10-28 · ChatGPT: [[Changes/ChatGPT/2025-10-28-we-re-launching-chatgpt-go-our-low-cost-subscription-plan-in-brazil-chatgpt-go-p|We're launching ChatGPT Go, our low cost subscription plan, in Brazil. ChatGPT G]]
- 2025-10-14 · ChatGPT: [[Changes/ChatGPT/2025-10-14-we-re-excited-to-announce-that-chatgpt-go-our-low-cost-subscription-plan-is-now-d58cbb|We're excited to announce that ChatGPT Go, our low cost subscription plan, is no]]
- 2025-10-08 · ChatGPT: [[Changes/ChatGPT/2025-10-08-we-re-excited-to-announce-that-chatgpt-go-our-low-cost-subscription-plan-is-now|We're excited to announce that ChatGPT Go, our low cost subscription plan, is no]]
- 2025-09-22 · ChatGPT: [[Changes/ChatGPT/2025-09-22-we-re-launching-chatgpt-go-our-low-cost-subscription-plan-in-indonesia-for-rp-75|We're launching ChatGPT Go, our low cost subscription plan, in Indonesia.For Rp]]
- 2025-08-18 · ChatGPT: [[Changes/ChatGPT/2025-08-18-we-re-launching-chatgpt-go-a-new-low-cost-subscription-plan-this-will-initially-e5f740|We’re launching ChatGPT Go, a new low-cost subscription plan. This will initiall]]
- 2025-05-15 · Cursor: [[Changes/Cursor/2025-05-15-all-model-usage-is-now-unified-into-request-based-pricing|All model usage is now unified into request-based pricing]]
- 2025-05-15 · Cursor: [[Changes/Cursor/2025-05-15-introducing-unified-request-based-pricing-max-mode-for-all-top-models-and-backgr|Introducing unified request-based pricing, Max Mode for all top models, and Back]]
- 2025-05-15 · Cursor: [[Changes/Cursor/2025-05-15-we-ve-heard-your-feedback-and-are-rolling-out-a-unified-pricing-model-to-make-it|We’ve heard your feedback and are rolling out a unified pricing model to make it]]
- 2025-05-15 · Cursor: [[Changes/Cursor/2025-05-15-max-mode-now-uses-token-based-pricing-similar-to-how-models-api-pricing-works|Max mode now uses token-based pricing (similar to how models API pricing works)]]
- 2025-03-23 · Cursor: [[Changes/Cursor/2025-03-23-chat-will-now-display-a-notification-about-usage-based-pricing-when-approaching|Chat will now display a notification about usage-based pricing when approaching]]

### 2023

- 2023-11-03 · Cursor: [[Changes/Cursor/2023-11-03-pro-plan-if-you-hit-your-fast-request-limit-and-prefer-to-purchase-more-you-now|Pro++ plan: if you hit your fast request limit and prefer to purchase more, you]]
- 2023-04-19 · Cursor: [[Changes/Cursor/2023-04-19-150k-gpt-4-tokens-included|150k GPT-4 tokens included]]
- 2023-03-27 · Cursor: [[Changes/Cursor/2023-03-27-adds-an-optional-paid-plan-if-you-d-like-to-avoid-the-server-capacity-rate-limit|Adds an optional paid plan if you'd like to avoid the server capacity rate limit]]
- 2023-02-13 · ChatGPT: [[Changes/ChatGPT/2023-02-13-we-rolled-out-the-ability-to-purchase-chatgpt-plus-internationally|We rolled out the ability to purchase ChatGPT Plus internationally.]]

### 2022

- 2022-12-15 · ChatGPT: [[Changes/ChatGPT/2022-12-15-daily-limit-to-ensure-a-high-quality-experience-for-all-chatgpt-users-we-are-exp|Daily limit: To ensure a high-quality experience for all ChatGPT users, we are e]]
<!-- chronolog:end -->

## Change Cards
<!-- chronolog:begin region="cards" -->
Active changes: 45. Use the dated links above to inspect each card.
<!-- chronolog:end -->