---
created: '2022-12-15'
date: '2026-10-09'
description: 'Research question: what is being charged for, and what does a plan unlock?'
machine_hash: b3fdbfe3a958c1155b168b22c50ccaa25bfe67dee2e1e92ef58a1ebfc2961f19
modified: '2026-10-09'
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

<!-- chronolog:begin region="header" -->
# Pricing Model
<!-- chronolog:end -->

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

- 2026-10-09 · Claude Code: [[Changes/Claude Code/2026-10-09-updated-cost-the-status-line-max-budget-usd-and-the-sdk-s-cost-figures-to-price|Updated /cost, the status line, --max-budget-usd and the SDK's cost figures…]]
- 2026-10-02 · Claude Code: [[Changes/Claude Code/2026-10-02-improved-the-usage-credits-message-shown-to-team-and-enterprise-members-whose-or|Improved the /usage-credits message shown to Team and Enterprise members whose…]]
- 2026-09-29 · ChatGPT: [[Changes/ChatGPT/2026-09-29-we-re-introducing-pro-500-a-new-500-month-plan-with-the-highest-included-usage-o-e04989|A new Pro plan with Astra Ultrafast]]
- 2026-09-29 · ChatGPT: [[Changes/ChatGPT/2026-09-29-pro-200-is-available-for-new-subscriptions-again-at-200-month-5ed430|Pro 200 subscriptions]]
- 2026-09-28 · Claude Code: [[Changes/Claude Code/2026-09-28-2-pricing-model-changes-in-v2-1-284|2 Pricing Model changes in v2.1.284]]
- 2026-09-24 · Claude Code: [[Changes/Claude Code/2026-09-24-updated-the-claude-api-skill-pre-output-refusal-billing-now-links-to-the-how-ref|Updated the claude-api skill]]
- 2026-09-23 · Cursor: [[Changes/Cursor/2026-09-23-for-the-next-10-days-we-re-including-usage-credits-so-teams-can-try-rollouts-on|For the next 10 days, we're including usage credits so teams can try Rollouts…]]
- 2026-09-22 · Claude Code: [[Changes/Claude Code/2026-09-22-improved-cost-cache-miss-causes-to-name-thinking-mode-and-thinking-display-chang|Improved /cost cache-miss causes to name thinking mode and thinking display changes]]
- 2026-09-19 · Claude Code: [[Changes/Claude Code/2026-09-19-changed-auto-mode-for-claude-api-and-enterprise-users-and-on-bedrock-vertex-foun|Changed auto mode for Claude API and Enterprise users, and on Bedrock, Vertex…]]
- 2026-09-18 · Claude Code: [[Changes/Claude Code/2026-09-18-vscode-added-the-session-s-cost-and-token-usage-to-the-account-usage-dialog-and|VSCode Added the session's cost and token usage to the Account & usage dialog…]]
- 2026-09-17 · Claude Code: [[Changes/Claude Code/2026-09-17-claude-code-on-the-web-changed-a-routine-s-on-hold-notice-when-your-subscription|Claude Code on the web Changed a routine's on-hold notice]]
- 2026-09-14 · Claude Code: [[Changes/Claude Code/2026-09-14-added-support-for-a-multiplier-above-1-up-to-10-in-the-modelpricing-managed-sett|Added support for a multiplier above 1, up to 10, in the modelPricing managed…]]
- 2026-09-10 · Claude Code: [[Changes/Claude Code/2026-09-10-2-pricing-model-changes-in-v2-1-268|2 Pricing Model changes in v2.1.268]]
- 2026-09-09 · ChatGPT: [[Changes/ChatGPT/2026-09-09-pro-100-month-up-to-15-hours-with-gpt-live-1|Pro ($100/month): Up to 15 hours with GPT-Live-1]]
- 2026-09-09 · ChatGPT: [[Changes/ChatGPT/2026-09-09-pro-200-month-unlimited-gpt-live-1-usage|Pro ($200/month): Unlimited GPT-Live-1 usage]]
- 2026-08-28 · Claude Code: [[Changes/Claude Code/2026-08-28-added-a-per-session-prompt-cache-line-to-cost-hit-ratio-misses-tokens-re-cached|Added a per-session prompt-cache line to /cost…]]
- 2026-08-27 · Claude Code: [[Changes/Claude Code/2026-08-27-added-usage-credits-for-enterprise-organizations-billed-through-aws-marketplace|Added /usage-credits for Enterprise organizations billed through AWS Marketplace…]]
- 2026-08-21 · Claude Code: [[Changes/Claude Code/2026-08-21-persistent-retry-mode-claude-code-retry-watchdog-now-fails-immediately-on-organi|Persistent retry mode (CLAUDE_CODE_RETRY_WATCHDOG) now fails immediately…]]
- 2026-08-19 · Claude Code: [[Changes/Claude Code/2026-08-19-usage-now-shows-the-usage-credits-spend-row-for-team-and-enterprise-members-and|/usage now shows the usage-credits spend row for Team and Enterprise members…]]
- 2026-08-04 · Claude Code: [[Changes/Claude Code/2026-08-04-changed-fast-mode-to-report-on-the-stream-when-usage-credits-run-out-mid-session|Changed fast mode to report on the stream when usage credits run out mid-session…]]
- 2026-07-29 · ChatGPT: [[Changes/ChatGPT/2026-07-29-research-rarely-happens-alone-chatgpt-for-academic-researchers-gives-faculty-and|ChatGPT for Academic Researchers]]
- 2026-07-28 · Cursor: [[Changes/Cursor/2026-07-28-we-re-introducing-cursor-start-a-new-649-monthly-plan-for-developers-in-india-ma|Cursor introduces Cursor Start, a new ₹649 monthly plan for developers in India…]]
- 2026-07-28 · Cursor: [[Changes/Cursor/2026-07-28-local-pricing-at-649-per-month-tax-inclusive-billed-in-inr-with-upi-or-card|Local pricing at ₹649 per month, tax inclusive, billed in INR with UPI or card]]
- 2026-07-22 · Cursor: [[Changes/Cursor/2026-07-22-2-pricing-model-changes-in-cursor-router|2 Pricing Model changes in Cursor Router]]
- 2026-07-22 · Claude Code: [[Changes/Claude Code/2026-07-22-changed-server-managed-settings-so-benign-feature-and-cost-toggles-no-longer-tri|Changed server-managed settings so benign feature and cost toggles no longer trigger…]]
- 2026-06-04 · Claude Code: [[Changes/Claude Code/2026-06-04-the-subscription-switch-suggestion-now-shows-in-the-startup-announcement-slot-in|The subscription-switch suggestion now shows in the startup announcement slot…]]
- 2026-05-19 · Claude Code: [[Changes/Claude Code/2026-05-19-renamed-extra-usage-to-usage-credits-across-cli-copy-extra-usage-is-now-usage-cr|Renamed "extra usage" to "usage credits" across CLI copy]]
- 2026-05-18 · Cursor: [[Changes/Cursor/2026-05-18-standard-0-50-m-input-2-50-m-output-tokens|Standard: $0.50/M input, $2.50/M output tokens]]
- 2026-05-18 · Cursor: [[Changes/Cursor/2026-05-18-fast-default-3-00-m-input-15-00-m-output-tokens|Fast (default): $3.00/M input, $15.00/M output tokens]]
- 2026-05-15 · Claude Code: [[Changes/Claude Code/2026-05-15-added-projected-context-cost-per-turn-and-per-invocation-token-estimates-to-the|Added projected context cost (per-turn and per-invocation token estimates)…]]
- 2026-05-11 · Cursor: [[Changes/Cursor/2026-05-11-customers-must-be-on-usage-based-billing-for-bugbot-to-customize-effort-levels-l|Customers must be on usage-based billing for Bugbot to customize effort levels]]
- 2026-04-22 · Claude Code: [[Changes/Claude Code/2026-04-22-opentelemetry-user-prompt-events-now-include-command-name-and-command-source-for|OpenTelemetry: user_prompt events now include command_name and command_source…]]
- 2026-04-09 · Claude Code: [[Changes/Claude Code/2026-04-09-fixed-false-bash-permission-prompts-for-cut-d-paste-d-column-s-awk-print-1-file|Fixed false Bash permission prompts for cut -d /, paste -d /, column -s /…]]
- 2026-04-09 · ChatGPT: [[Changes/ChatGPT/2026-04-09-you-can-upgrade-switch-or-cancel-your-plan-from-settings-my-plan-or-from-the-pri|You can upgrade, switch, or cancel your plan from Settings  My Plan or…]]
- 2026-04-09 · ChatGPT: [[Changes/ChatGPT/2026-04-09-pro-200-month-our-highest-usage-option-remains-available-and-continues-on-its-cu|Pro ($200/month): Our highest-usage option remains available and continues…]]
- 2026-04-09 · ChatGPT: [[Changes/ChatGPT/2026-04-09-plus-20-month-plus-remains-best-for-steady-day-to-day-use-as-the-temporary-codex|Plus ($20/month): Plus remains best for steady, day-to-day use]]
- 2026-04-09 · ChatGPT: [[Changes/ChatGPT/2026-04-09-we-re-introducing-a-new-100-month-pro-plan-and-updating-how-codex-usage-works-ac|We’re introducing a new $100/month Pro plan and updating how Codex usage works…]]
- 2026-04-09 · ChatGPT: [[Changes/ChatGPT/2026-04-09-pro-100-month-built-for-longer-high-intensity-codex-sessions-it-includes-unlimit|Pro ($100/month): Built for longer, high-intensity Codex sessions]]
- 2026-04-04 · Claude Code: [[Changes/Claude Code/2026-04-04-added-per-model-and-cache-hit-breakdown-to-cost-for-subscription-users|Added per-model and cache-hit breakdown to /cost for subscription users]]
- 2026-03-19 · Cursor: [[Changes/Cursor/2026-03-19-fast-default-1-50-m-input-7-50-m-output-tokens|Fast (default): $1.50/M input, $7.50/M output tokens]]
- 2026-03-19 · Cursor: [[Changes/Cursor/2026-03-19-standard-0-50-m-input-2-50-m-output-tokens|Standard: $0.50/M input, $2.50/M output tokens]]
- 2026-03-10 · ChatGPT: [[Changes/ChatGPT/2026-03-10-eligible-chatgpt-plus-and-pro-users-can-now-turn-on-auto-top-up-for-credits-used-5e9d54|Auto top-up for flexible usage credits]]
- 2026-02-04 · Claude Code: [[Changes/Claude Code/2026-02-04-removed-misleading-anthropic-api-pricing-from-model-selector-for-third-party-pro|Removed misleading Anthropic API pricing from model selector for third-party…]]

### 2025

- 2025-12-18 · Cursor: [[Changes/Cursor/2025-12-18-billing-groups|Billing groups]]
- 2025-11-03 · ChatGPT: [[Changes/ChatGPT/2025-11-03-eligible-customers-in-india-can-now-get-12-months-of-chatgpt-go-at-no-cost-new-u|ChatGPT Go Promo - India]]
- 2025-10-30 · ChatGPT: [[Changes/ChatGPT/2025-10-30-we-re-excited-to-announce-that-chatgpt-go-our-low-cost-subscription-plan-is-now-44be9d|ChatGPT Go, our low cost subscription plan, is now available in 8 additional…]]
- 2025-10-28 · ChatGPT: [[Changes/ChatGPT/2025-10-28-we-re-launching-chatgpt-go-our-low-cost-subscription-plan-in-brazil-chatgpt-go-p|ChatGPT launches ChatGPT Go, our low cost subscription plan, in Brazil]]
- 2025-10-14 · ChatGPT: [[Changes/ChatGPT/2025-10-14-we-re-excited-to-announce-that-chatgpt-go-our-low-cost-subscription-plan-is-now-d58cbb|ChatGPT Go, our low cost subscription plan, is now available in 71 additional…]]
- 2025-10-08 · ChatGPT: [[Changes/ChatGPT/2025-10-08-we-re-excited-to-announce-that-chatgpt-go-our-low-cost-subscription-plan-is-now|ChatGPT Go, our low cost subscription plan, is now available in 16 additional countries]]
- 2025-09-22 · ChatGPT: [[Changes/ChatGPT/2025-09-22-we-re-launching-chatgpt-go-our-low-cost-subscription-plan-in-indonesia-for-rp-75|ChatGPT launches ChatGPT Go, our low cost subscription plan, in Indonesia]]
- 2025-08-18 · ChatGPT: [[Changes/ChatGPT/2025-08-18-we-re-launching-chatgpt-go-a-new-low-cost-subscription-plan-this-will-initially-e5f740|ChatGPT launches ChatGPT Go, a new low-cost subscription plan]]
- 2025-08-06 · Cursor: [[Changes/Cursor/2025-08-06-usage-and-pricing-visibility|Usage and pricing visibility]]
- 2025-05-15 · Cursor: [[Changes/Cursor/2025-05-15-introducing-unified-request-based-pricing-max-mode-for-all-top-models-and-backgr|Introducing unified request-based pricing, Max Mode for all top models…]]
- 2025-05-15 · Cursor: [[Changes/Cursor/2025-05-15-simpler-unified-pricing-6a915c|Simpler, unified pricing]]
- 2025-03-23 · Cursor: [[Changes/Cursor/2025-03-23-this-release-introduces-chat-tabs-for-parallel-conversations-a-redesignedmodes-s|Cursor introduces chat tabs for parallel conversations, a redesignedmodes system…]]
- 2025-03-23 · Cursor: [[Changes/Cursor/2025-03-23-usage-based-cost-visibility|Usage-based cost visibility]]
- 2025-03-23 · Cursor: [[Changes/Cursor/2025-03-23-chat-will-now-display-a-notification-about-usage-based-pricing-when-approaching|Chat will now display a notification about usage-based pricing when approaching fast…]]

### 2023

- 2023-11-03 · Cursor: [[Changes/Cursor/2023-11-03-pro-plan-if-you-hit-your-fast-request-limit-and-prefer-to-purchase-more-you-now|Pro++ plan: if you hit your fast request limit and prefer to purchase more, you now can]]
- 2023-04-19 · Cursor: [[Changes/Cursor/2023-04-19-150k-gpt-4-tokens-included|150k GPT-4 tokens included]]
- 2023-03-27 · Cursor: [[Changes/Cursor/2023-03-27-adds-an-optional-paid-plan-if-you-d-like-to-avoid-the-server-capacity-rate-limit|Adds an optional paid plan if you'd like to avoid the server capacity rate limits]]
- 2023-02-13 · ChatGPT: [[Changes/ChatGPT/2023-02-13-we-rolled-out-the-ability-to-purchase-chatgpt-plus-internationally|We rolled out the ability to purchase ChatGPT Plus internationally]]

### 2022

- 2022-12-15 · ChatGPT: [[Changes/ChatGPT/2022-12-15-daily-limit-to-ensure-a-high-quality-experience-for-all-chatgpt-users-we-are-exp|Daily limit: To ensure a high-quality experience for all ChatGPT users, we…]]
<!-- chronolog:end -->

## Change Cards
<!-- chronolog:begin region="cards" -->
Active changes: 62. Use the dated links above to inspect each card.
<!-- chronolog:end -->