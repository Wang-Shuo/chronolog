---
created: '2022-12-15'
date: '2026-11-06'
description: 'Research question: what is being charged for, and what does a plan unlock?'
machine_hash: b8fd9114fba66af495c2d03d81248c15eb09d646dbabf0e9ac2fdfaf915e0bc1
modified: '2026-11-06'
products_involved:
- Aider
- ChatGPT
- Claude Code
- Cline
- Codex CLI
- Cursor
- Gemini CLI
- GitHub Copilot CLI
- OpenHands
- Windsurf
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

149 tracked changes across Aider, ChatGPT, Claude Code, Cline, Codex CLI, Cursor, Gemini CLI, GitHub Copilot CLI, OpenHands and Windsurf · 2022-12-15 → 2026-11-06 · Codex CLI averages 8.0 cards per release, Gemini CLI 7.5, Claude Code 7.0, GitHub Copilot CLI 6.3, Cursor 4.0, OpenHands 3.8, Aider 3.7, Cline 3.0, Windsurf 2.6, ChatGPT 1.7
<!-- chronolog:end -->

## Research summary
<!-- chronolog:begin region="narrative" -->
**Research question: what is being charged for, and what does a plan unlock?**

Cursor's [2025-05-15 announcement](https://cursor.com/changelog/0-50) ([[Releases/Cursor/cursor-2025-05-15-0-50-https-cursor-com-changelog-0-50-dc290998|archived]]) distinguishes request-based ordinary usage from token-based Max Mode and states that plan quotas were unchanged at that time, a dated change of mechanism.

ChatGPT's [2026-04-09 Pro changes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes#new-pro-plan-options) ([[Releases/ChatGPT/chatgpt-2026-04-09-new-pro-plan-options-9eccb9c2|archived]]) introduce a $100/month Pro option alongside $200/month Pro and describe usage allowances. The [2026-09-29 Pro 500 announcement](https://help.openai.com/en/articles/6825453-chatgpt-release-notes#a-new-pro-plan-with-astra-ultrafast) ([[Releases/ChatGPT/chatgpt-2026-09-29-a-new-pro-plan-with-astra-ultrafast-f0c84e90|archived]]) adds a $500/month tier and gates Ultrafast to that tier: buying credits on Pro 100 or Pro 200 does not unlock it. Included allowances and purchased credits are distinct from feature eligibility.

Claude Code's [v2.1.296 on 2026-10-09](https://github.com/anthropics/claude-code/releases/tag/v2.1.296) ([[Releases/Claude Code/claude-code-2026-10-09-v2-1-296-github-408141042-fd950e7a|archived]]) updates displayed Sonnet 5.5 cache-read cost figures from $0.20 to $0.10 per million tokens in cost reporting and budget controls, a client-side cost-accounting update.

**Uncertainty and scope:** this editorial summary covers ChatGPT, Claude Code and Cursor; the timeline includes all tracked products and treats subscriptions, requests, token metering, credits and client cost estimates as different mechanisms; prices are historical statements with plan and rollout qualifications, so this evidence does not support “one product followed another,” universal price comparisons, claims about current price lists or invoices, a new Claude subscription price or every user's billed price, and shopping prices fall outside this theme unless they change the AI product's own charging mechanism.
<!-- chronolog:end -->

## Key moments
<!-- chronolog:begin region="moments" -->
| Quarter | Aider | ChatGPT | Claude Code | Cline | Codex CLI | Cursor | Gemini CLI | GitHub Copilot CLI | OpenHands | Windsurf |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **First in archive** | <time datetime="2023-06-25">2023-06-25</time> [[Changes/Aider/2023-06-25-enables-display-of-cost-info-based-on-openai-advertised-pricing\|Enables display of cost info based on OpenAI advertised pricing]] | <time datetime="2022-12-15">2022-12-15</time> [[Changes/ChatGPT/2022-12-15-daily-limit-to-ensure-a-high-quality-experience-for-all-chatgpt-users-we-are-exp\|Daily limit: To ensure a high-quality experience for all ChatGPT users, we…]] | <time datetime="2026-02-04">2026-02-04</time> [[Changes/Claude Code/2026-02-04-removed-misleading-anthropic-api-pricing-from-model-selector-for-third-party-pro\|Removed misleading Anthropic API pricing from model selector for third-party…]] | <time datetime="2024-09-12">2024-09-12</time> [[Changes/Cline/2024-09-12-openrouter-now-supports-prompt-caching-they-re-still-working-on-reporting-cache\|OpenRouter now supports prompt caching!]] | <time datetime="2025-10-30">2025-10-30</time> [[Changes/Codex CLI/2025-10-30-ability-to-buy-credits-for-more-usage-more-information-https-help-openai-com-en\|Ability to buy credits for more usage]] | <time datetime="2023-03-27">2023-03-27</time> [[Changes/Cursor/2023-03-27-adds-an-optional-paid-plan-if-you-d-like-to-avoid-the-server-capacity-rate-limit\|Adds an optional paid plan if you'd like to avoid the server capacity rate limits]] | <time datetime="2025-07-01">2025-07-01</time> [[Changes/Gemini CLI/2025-07-01-docs-add-a-page-detailing-quota-and-cost-information-by-ptone-in-https-github-co\|Docs: Add a page detailing quota and cost information]] | <time datetime="2025-10-01">2025-10-01</time> [[Changes/GitHub Copilot CLI/2025-10-01-switched-to-using-per-subscription-copilot-api-endpoints-in-accordance-with-gith\|Switched to using per-subscription Copilot API endpoints in accordance…]] | <time datetime="2024-06-04">2024-06-04</time> [[Changes/OpenHands/2024-06-04-add-cost-metrics-to-evaluation-outputs-for-all-benchmarks-by-ryanhoangt-in-https\|Add cost metrics to evaluation outputs for all benchmarks]] | <time datetime="2025-04-20">2025-04-20</time> [[Changes/Windsurf/2025-04-20-we-re-getting-rid-of-flow-action-credits\|We're getting rid of Flow Action Credits]] |
| 2026 Q4 | · | · | <time datetime="2026-10-09">2026-10-09</time> [[Changes/Claude Code/2026-10-09-updated-cost-the-status-line-max-budget-usd-and-the-sdk-s-cost-figures-to-price\|Updated /cost, the status line, --max-budget-usd and the SDK's cost figures…]] | · | · | · | · | · | · | · |
| 2026 Q3 | · | <time datetime="2026-09-29">2026-09-29</time> [[Changes/ChatGPT/2026-09-29-we-re-introducing-pro-500-a-new-500-month-plan-with-the-highest-included-usage-o-e04989\|A new Pro plan with Astra Ultrafast]] | <time datetime="2026-08-27">2026-08-27</time> [[Changes/Claude Code/2026-08-27-added-usage-credits-for-enterprise-organizations-billed-through-aws-marketplace\|Added /usage-credits for Enterprise organizations billed through AWS Marketplace…]] | · | · | <time datetime="2026-07-28">2026-07-28</time> [[Changes/Cursor/2026-07-28-we-re-introducing-cursor-start-a-new-649-monthly-plan-for-developers-in-india-ma\|Cursor introduces Cursor Start, a new ₹649 monthly plan for developers in India…]] | · | · | · | · |
| 2026 Q2 | · | <time datetime="2026-04-09">2026-04-09</time> [[Changes/ChatGPT/2026-04-09-we-re-introducing-a-new-100-month-pro-plan-and-updating-how-codex-usage-works-ac\|We’re introducing a new $100/month Pro plan and updating how Codex usage works…]] | <time datetime="2026-05-19">2026-05-19</time> [[Changes/Claude Code/2026-05-19-renamed-extra-usage-to-usage-credits-across-cli-copy-extra-usage-is-now-usage-cr\|Renamed "extra usage" to "usage credits" across CLI copy]] | · | · | · | · | · | · | · |
| 2026 Q1 | · | · | · | · | · | <time datetime="2026-03-19">2026-03-19</time> [[Changes/Cursor/2026-03-19-fast-default-1-50-m-input-7-50-m-output-tokens\|Fast (default): $1.50/M input, $7.50/M output tokens]] | · | · | · | · |
| 2025 Q4 | · | · | archive begins <time datetime="2025-12-19">2025-12-19</time> | · | · | · | · | · | · | · |
| 2025 Q3 | · | <time datetime="2025-08-18">2025-08-18</time> [[Changes/ChatGPT/2025-08-18-we-re-launching-chatgpt-go-a-new-low-cost-subscription-plan-this-will-initially-e5f740\|ChatGPT launches ChatGPT Go, a new low-cost subscription plan]] | <span class="not-archived">not archived</span> | · | · | · | · | archive begins <time datetime="2025-09-26">2025-09-26</time> | · | · |
| 2025 Q2 | · | · | <span class="not-archived">not archived</span> | · | archive begins <time datetime="2025-06-30">2025-06-30</time> | <time datetime="2025-05-15">2025-05-15</time> [[Changes/Cursor/2025-05-15-simpler-unified-pricing-6a915c\|Simpler, unified pricing]] | archive begins <time datetime="2025-06-28">2025-06-28</time> | <span class="not-archived">not archived</span> | · | archive begins <time datetime="2025-04-02">2025-04-02</time> |
| 2024 Q1 → 2025 Q1 | · | · | <span class="not-archived">not archived</span> | archive begins <time datetime="2024-07-28">2024-07-28</time> | <span class="not-archived">not archived</span> | · | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | archive begins <time datetime="2024-06-04">2024-06-04</time> | <span class="not-archived">not archived</span> |
| 2023 Q4 | · | · | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <time datetime="2023-11-03">2023-11-03</time> [[Changes/Cursor/2023-11-03-pro-plan-if-you-hit-your-fast-request-limit-and-prefer-to-purchase-more-you-now\|Pro++ plan: if you hit your fast request limit and prefer to purchase more, you now can]] | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> |
| 2023 Q2 → 2023 Q3 | archive begins <time datetime="2023-06-07">2023-06-07</time> | · | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | · | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> |
| 2023 Q1 | <span class="not-archived">not archived</span> | <time datetime="2023-02-13">2023-02-13</time> [[Changes/ChatGPT/2023-02-13-we-rolled-out-the-ability-to-purchase-chatgpt-plus-internationally\|We rolled out the ability to purchase ChatGPT Plus internationally]] | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <time datetime="2023-03-27">2023-03-27</time> [[Changes/Cursor/2023-03-27-adds-an-optional-paid-plan-if-you-d-like-to-avoid-the-server-capacity-rate-limit\|Adds an optional paid plan if you'd like to avoid the server capacity rate limits]] | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> |
| 2022 Q4 | <span class="not-archived">not archived</span> | <time datetime="2022-12-15">2022-12-15</time> [[Changes/ChatGPT/2022-12-15-daily-limit-to-ensure-a-high-quality-experience-for-all-chatgpt-users-we-are-exp\|Daily limit: To ensure a high-quality experience for all ChatGPT users, we…]] | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> |

First in archive: each product's earliest tracked change in this theme. "·" marks a quarter without a key moment, and "not archived" a quarter before the product's archive begins. Archives begin: Aider 2023-06-07 · ChatGPT 2022-12-15 · Claude Code 2025-12-19 · Cline 2024-07-28 · Codex CLI 2025-06-30 · Cursor 2023-03-14 · Gemini CLI 2025-06-28 · GitHub Copilot CLI 2025-09-26 · OpenHands 2024-06-04 · Windsurf 2025-04-02.
<!-- chronolog:end -->

<!-- chronolog:begin region="scope" -->
<details class="disclosure">
<summary>How to read this timeline</summary>

Scope: tracked-products-only. Entries show same-theme chronology; they do not establish equivalent capabilities, adoption, or causation.

</details>
<!-- chronolog:end -->

## Timeline
<!-- chronolog:begin region="timeline" -->
<div class="timeline">

Launches, expansions, pricing and policy changes and standalone announcements come first in each year; fixes, digests and other changes are folded beneath them.

<fieldset class="timeline-filter">
<legend>Show</legend>
<label><input type="radio" name="timeline-product" id="tl-only-all" checked> All</label>
<label><input type="radio" name="timeline-product" id="tl-only-1"> Aider</label>
<label><input type="radio" name="timeline-product" id="tl-only-2"> ChatGPT</label>
<label><input type="radio" name="timeline-product" id="tl-only-3"> Claude Code</label>
<label><input type="radio" name="timeline-product" id="tl-only-4"> Cline</label>
<label><input type="radio" name="timeline-product" id="tl-only-5"> Codex CLI</label>
<label><input type="radio" name="timeline-product" id="tl-only-6"> Cursor</label>
<label><input type="radio" name="timeline-product" id="tl-only-7"> Gemini CLI</label>
<label><input type="radio" name="timeline-product" id="tl-only-8"> GitHub Copilot CLI</label>
<label><input type="radio" name="timeline-product" id="tl-only-9"> OpenHands</label>
<label><input type="radio" name="timeline-product" id="tl-only-10"> Windsurf</label>
</fieldset>

<details class="disclosure">
<summary>2026 · 100 entries (ChatGPT 14 · Claude Code 23 · Cline 11 · Codex CLI 14 · Cursor 9 · Gemini CLI 4 · GitHub Copilot CLI 17 · OpenHands 3 · Windsurf 5)</summary>

**2026-10**

- 2026-10-29 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-10-29-56495-add-paginated-channel-subscription-queries-to-the-local-message-board-feli|♯56495 Add paginated channel subscription queries to the local message board @felixxia-oai]] · Pricing
- 2026-10-28 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-10-28-eligible-chatgpt-pro-and-business-subscribers-can-activate-promotional-api-credi|API credits for eligible ChatGPT Pro and Business plans]] · Pricing
- 2026-10-21 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-10-21-you-can-now-use-momo-to-pay-for-chatgpt-go-plus-and-pro-subscriptions-purchased|MoMo payments in Vietnam]] · Pricing
- 2026-10-19 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-10-19-complete-usage-reporting-no-longer-shows-partial-status-or-phantom-unattributed|Complete usage reporting no longer shows partial status or phantom unattributed…]] · Pricing
- 2026-10-15 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-10-15-the-rosalind-academic-plan-helps-eligible-academic-labs-use-chatgpt-for-life-sci|The Rosalind Academic Plan helps eligible academic labs use ChatGPT for life…]] · Pricing
- 2026-10-13 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-10-13-show-billed-ai-credits-in-usage-for-token-billed-sessions-including-after-resume|Show billed AI Credits in /usage for token-billed sessions, including after resume]] · Pricing
- 2026-10-09 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-10-09-updated-cost-the-status-line-max-budget-usd-and-the-sdk-s-cost-figures-to-price|Updated /cost, the status line, --max-budget-usd and the SDK's cost figures…]] · Pricing
- 2026-10-05 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-10-05-plan-usage-reflects-the-current-billing-period-after-quota-resets|Plan usage reflects the current billing period after quota resets]] · Policy
- 2026-10-02 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-10-02-improved-the-usage-credits-message-shown-to-team-and-enterprise-members-whose-or|Improved the /usage-credits message shown to Team and Enterprise members whose…]] · Pricing
- 2026-10-01 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-10-01-49079-update-and-centralize-tui-subscription-labels-etraut-openai|♯49079 Update and centralize TUI subscription labels @etraut-openai]] · Pricing

**2026-09**

- 2026-09-29 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-09-29-pro-200-is-available-for-new-subscriptions-again-at-200-month-5ed430|Pro 200 subscriptions]] · Pricing
- 2026-09-29 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-09-29-we-re-introducing-pro-500-a-new-500-month-plan-with-the-highest-included-usage-o-e04989|A new Pro plan with Astra Ultrafast]] · Launch
- 2026-09-29 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-09-29-claude-tag-added-direct-messages-with-claude-for-members-on-an-enterprise-plan-s|Claude Tag Added direct messages with Claude for members on an Enterprise plan…]] · Pricing
- 2026-09-25 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-09-25-47086-format-analytics-credit-usage-with-consistent-decimal-precision-fcoury-oai|♯47086 Format analytics credit usage with consistent decimal precision @fcoury-oai]] · Pricing
- 2026-09-25 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2026-09-25-feat-scope-openai-subscription-caches-by-backend-by-uczltw6-in-https-github-com|feat: scope OpenAI subscription caches by backend]] · Pricing
- 2026-09-24 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-09-24-updated-the-claude-api-skill-pre-output-refusal-billing-now-links-to-the-how-ref|Updated the claude-api skill]] · Policy
- 2026-09-23 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-09-23-for-the-next-10-days-we-re-including-usage-credits-so-teams-can-try-rollouts-on|For the next 10 days, we're including usage credits so teams can try Rollouts…]] · Pricing
- 2026-09-22 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-09-22-improved-cost-cache-miss-causes-to-name-thinking-mode-and-thinking-display-chang|Improved /cost cache-miss causes to name thinking mode and thinking display changes]] · Pricing
- 2026-09-22 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-09-22-models-that-advertise-a-large-output-limit-now-get-a-bigger-default-output-budge|Models that advertise a large output limit now get a bigger default output budget]] · Pricing
- 2026-09-19 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-09-19-changed-auto-mode-for-claude-api-and-enterprise-users-and-on-bedrock-vertex-foun|Changed auto mode for Claude API and Enterprise users, and on Bedrock, Vertex…]] · Pricing
- 2026-09-18 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-09-18-vscode-added-the-session-s-cost-and-token-usage-to-the-account-usage-dialog-and|VSCode Added the session's cost and token usage to the Account & usage dialog…]] · Pricing
- 2026-09-17 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-09-17-claude-code-on-the-web-changed-a-routine-s-on-hold-notice-when-your-subscription|Claude Code on the web Changed a routine's on-hold notice]] · Pricing
- 2026-09-17 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-09-17-cline-pass-now-defaults-to-a-model-from-your-subscription-rather-than-a-free-one|Cline Pass now defaults to a model from your subscription rather than a free one]] · Pricing
- 2026-09-16 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-09-16-usage-shows-per-model-ai-credit-consumption-in-usage-breakdowns|/usage shows per-model AI Credit consumption in usage breakdowns]] · Pricing
- 2026-09-16 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2026-09-16-test-strengthen-llm-subscription-normalization-by-aivong-openhands-in-https-gith|test: strengthen LLM subscription normalization]] · Pricing
- 2026-09-14 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-09-14-added-support-for-a-multiplier-above-1-up-to-10-in-the-modelpricing-managed-sett|Added support for a multiplier above 1, up to 10, in the modelPricing managed…]] · Pricing
- 2026-09-09 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-09-09-pro-200-month-unlimited-gpt-live-1-usage|Pro ($200/month): Unlimited GPT-Live-1 usage]] · Pricing
- 2026-09-09 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-09-09-pro-100-month-up-to-15-hours-with-gpt-live-1|Pro ($100/month): Up to 15 hours with GPT-Live-1]] · Pricing
- 2026-09-03 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-09-03-41944-https-github-com-openai-codex-pull-41944-emit-turn-cost-telemetry-for-chat|♯41944((source link) Emit turn cost telemetry…]] · Pricing
- 2026-09-02 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-09-02-cost-estimates-no-longer-appear-in-task-history-for-subscription-billed-tasks-cl|Cost estimates no longer appear in task history for subscription-billed tasks…]] · Pricing
- 2026-09-01 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-09-01-rate-limit-banners-offer-actions-for-checking-usage-managing-credits-resetting-l|Rate-limit banners offer actions for checking usage, managing credits, resetting…]] · Pricing

**2026-08**

- 2026-08-28 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-08-28-added-a-per-session-prompt-cache-line-to-cost-hit-ratio-misses-tokens-re-cached|Added a per-session prompt-cache line to /cost…]] · Pricing
- 2026-08-27 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-08-27-added-usage-credits-for-enterprise-organizations-billed-through-aws-marketplace|Added /usage-credits for Enterprise organizations billed through AWS Marketplace…]] · Policy
- 2026-08-26 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-08-26-cost-estimates-are-no-longer-shown-for-providers-billed-by-a-flat-rate-subscript|Cost estimates are no longer shown for providers billed by a flat-rate subscription…]] · Pricing
- 2026-08-26 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-08-26-40488-export-turn-cost-as-an-otel-metric-copyberry|♯40488 Export turn cost as an OTEL metric @copyberry]] · Pricing
- 2026-08-21 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-08-21-persistent-retry-mode-claude-code-retry-watchdog-now-fails-immediately-on-organi|Persistent retry mode (CLAUDE_CODE_RETRY_WATCHDOG) now fails immediately…]] · Pricing
- 2026-08-21 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-08-21-show-the-billed-cost-for-cline-gateway-usage|Show the billed cost for Cline gateway usage]] · Pricing
- 2026-08-20 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-08-20-39006-emit-api-key-turn-cost-telemetry-from-app-server-copyberry|♯39006 Emit API-key turn cost telemetry from app-server @copyberry]] · Pricing
- 2026-08-19 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-08-19-usage-now-shows-the-usage-credits-spend-row-for-team-and-enterprise-members-and|/usage now shows the usage-credits spend row for Team and Enterprise members…]] · Pricing
- 2026-08-18 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-08-18-38650-canonicalize-default-namespaces-in-grpc-subscription-filters-copyberry|♯38650 Canonicalize default namespaces in gRPC subscription filters @copyberry]] · Pricing
- 2026-08-11 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-08-11-report-fable-5-cost-on-vertex-as-unknown-rather-than-applying-anthropic-s-list-p|Report Fable 5 cost on Vertex as unknown rather than applying Anthropic's list…]] · Pricing
- 2026-08-10 · <span class="tl-product tl-p10">**Windsurf**</span> · [[Changes/Windsurf/2026-08-10-devin-cloud|Devin Cloud]] · Pricing
- 2026-08-04 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-08-04-changed-fast-mode-to-report-on-the-stream-when-usage-credits-run-out-mid-session|Changed fast mode to report on the stream when usage credits run out mid-session…]] · Pricing

**2026-07**

- 2026-07-29 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-07-29-research-rarely-happens-alone-chatgpt-for-academic-researchers-gives-faculty-and|ChatGPT for Academic Researchers]] · Pricing
- 2026-07-28 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-07-28-local-pricing-at-649-per-month-tax-inclusive-billed-in-inr-with-upi-or-card|Local pricing at ₹649 per month, tax inclusive, billed in INR with UPI or card]] · Pricing
- 2026-07-28 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-07-28-we-re-introducing-cursor-start-a-new-649-monthly-plan-for-developers-in-india-ma|Cursor introduces Cursor Start, a new ₹649 monthly plan for developers in India…]] · Launch
- 2026-07-22 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-07-22-changed-server-managed-settings-so-benign-feature-and-cost-toggles-no-longer-tri|Changed server-managed settings so benign feature and cost toggles no longer trigger…]] · Pricing
- 2026-07-09 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-07-09-add-a-clinepass-limit-reached-error-with-a-one-click-option-to-switch-to-cline-u|Add a ClinePass limit-reached error with a one-click option to switch to Cline…]] · Pricing
- 2026-07-09 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-07-09-usage-limit-reset-credits-now-show-their-type-and-expiration-and-let-you-choose|Usage-limit reset credits now show their type and expiration, and let you choose…]] · Pricing
- 2026-07-08 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-07-08-28593-codex-suppress-low-usage-remaining-warnings-when-credits-are-available-bro|♯28593 codex suppress low usage remaining warnings when credits are available…]] · Pricing
- 2026-07-07 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-07-07-improve-chronicle-cost-tips-with-more-precise-evidence-backed-recommendations|Improve /chronicle cost-tips with more precise evidence-backed recommendations]] · Pricing
- 2026-07-06 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2026-07-06-refactor-extract-billing-test-fixtures-for-pltf-1269-by-aivong-openhands-in-http|refactor: extract billing test fixtures for PLTF-1269]] · Pricing

**2026-06**

- 2026-06-30 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-06-30-configure-subagent-concurrency-and-depth-limits-in-settings-usage-based-billing|Configure subagent concurrency and depth limits in /settings (usage-based billing users)]] · Pricing
- 2026-06-30 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-06-30-require-session-limits-to-be-at-least-30-ai-credits|Require session limits to be at least 30 AI credits]] · Pricing
- 2026-06-26 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-06-26-add-clinepass-to-the-vs-code-extension-including-onboarding-provider-selection-s|Add ClinePass to the VS Code extension, including onboarding, provider selection…]] · Pricing
- 2026-06-23 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-06-23-display-cache-write-pricing-for-models-that-omit-it|Display cache-write pricing for models that omit it]] · Pricing
- 2026-06-22 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-06-22-usage-can-now-show-and-redeem-earned-usage-limit-reset-credits-with-confirmation|/usage can now show and redeem earned usage-limit reset credits…]] · Pricing
- 2026-06-18 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-06-18-28143-feat-app-server-expose-rate-limit-reset-credits-jayp-oai|♯28143 feat(app-server): expose rate-limit reset credits @jayp-oai]] · Pricing
- 2026-06-06 · <span class="tl-product tl-p10">**Windsurf**</span> · [[Changes/Windsurf/2026-06-06-simplified-model-picker-pricing-view-for-select-enterprise-customers|Simplified model picker pricing view for select enterprise customers]] · Pricing
- 2026-06-05 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-06-05-add-billing-help-topic-with-an-overview-of-ai-credit-usage-features|Add billing help topic with an overview of AI credit usage features]] · Pricing
- 2026-06-04 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-06-04-the-subscription-switch-suggestion-now-shows-in-the-startup-announcement-slot-in|The subscription-switch suggestion now shows in the startup announcement slot…]] · Pricing

**2026-05**

- 2026-05-19 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-05-19-renamed-extra-usage-to-usage-credits-across-cli-copy-extra-usage-is-now-usage-cr|Renamed "extra usage" to "usage credits" across CLI copy]] · Pricing
- 2026-05-18 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-05-18-fast-default-3-00-m-input-15-00-m-output-tokens|Fast (default): $3.00/M input, $15.00/M output tokens]] · Pricing
- 2026-05-18 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-05-18-standard-0-50-m-input-2-50-m-output-tokens|Standard: $0.50/M input, $2.50/M output tokens]] · Pricing
- 2026-05-15 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-05-15-added-projected-context-cost-per-turn-and-per-invocation-token-estimates-to-the|Added projected context cost (per-turn and per-invocation token estimates)…]] · Pricing
- 2026-05-14 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-05-14-model-picker-displays-actual-token-prices-instead-of-dot-indicators-for-token-ba|Model picker displays actual token prices instead of dot indicators for token-based…]] · Pricing
- 2026-05-13 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-05-13-copilot-max-subscribers-see-the-correct-models-available-to-their-subscription-t|Copilot Max subscribers see the correct models available to their subscription tier]] · Pricing
- 2026-05-11 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-05-11-customers-must-be-on-usage-based-billing-for-bugbot-to-customize-effort-levels-l|Customers must be on usage-based billing for Bugbot to customize effort levels]] · Pricing
- 2026-05-06 · <span class="tl-product tl-p10">**Windsurf**</span> · [[Changes/Windsurf/2026-05-06-devin-review-quick-review|Devin Review & Quick Review]] · Pricing

**2026-04**

- 2026-04-22 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-04-22-opentelemetry-user-prompt-events-now-include-command-name-and-command-source-for|OpenTelemetry: user_prompt events now include command_name and command_source…]] · Pricing
- 2026-04-09 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-04-09-pro-100-month-built-for-longer-high-intensity-codex-sessions-it-includes-unlimit|Pro ($100/month): Built for longer, high-intensity Codex sessions]] · Pricing
- 2026-04-09 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-04-09-we-re-introducing-a-new-100-month-pro-plan-and-updating-how-codex-usage-works-ac|We’re introducing a new $100/month Pro plan and updating how Codex usage works…]] · Launch
- 2026-04-09 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-04-09-plus-20-month-plus-remains-best-for-steady-day-to-day-use-as-the-temporary-codex|Plus ($20/month): Plus remains best for steady, day-to-day use]] · Pricing
- 2026-04-09 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-04-09-pro-200-month-our-highest-usage-option-remains-available-and-continues-on-its-cu|Pro ($200/month): Our highest-usage option remains available and continues…]] · Pricing
- 2026-04-09 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-04-09-you-can-upgrade-switch-or-cancel-your-plan-from-settings-my-plan-or-from-the-pri|You can upgrade, switch, or cancel your plan from Settings  My Plan or…]] · Pricing
- 2026-04-08 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-04-08-docs-update-quotas-and-pricing-by-jkcinouye-in-https-github-com-google-gemini-ge|Docs: Update quotas and pricing]] · Policy
- 2026-04-04 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-04-04-added-per-model-and-cache-hit-breakdown-to-cost-for-subscription-users|Added per-model and cache-hit breakdown to /cost for subscription users]] · Pricing

**2026-03**

- 2026-03-31 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-03-31-15934-add-usage-based-business-plan-types-bwanner-oai|♯15934 Add usage-based business plan types @bwanner-oai]] · Pricing
- 2026-03-24 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-03-24-feat-telemetry-add-clearcut-instrumentation-for-ai-credits-billing-events-by-gsq|feat(telemetry): add Clearcut instrumentation for AI credits billing events]] · Pricing
- 2026-03-19 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-03-19-add-missing-fireworks-serverless-models-and-pricing|Add missing Fireworks serverless models and pricing]] · Pricing
- 2026-03-19 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-03-19-standard-0-50-m-input-2-50-m-output-tokens|Standard: $0.50/M input, $2.50/M output tokens]] · Pricing
- 2026-03-19 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-03-19-fast-default-1-50-m-input-7-50-m-output-tokens|Fast (default): $1.50/M input, $7.50/M output tokens]] · Pricing
- 2026-03-19 · <span class="tl-product tl-p10">**Windsurf**</span> · [[Changes/Windsurf/2026-03-19-quota-billing|Quota Billing]] · Policy
- 2026-03-10 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2026-03-10-eligible-chatgpt-plus-and-pro-users-can-now-turn-on-auto-top-up-for-credits-used-5e9d54|Auto top-up for flexible usage credits]] · Pricing
- 2026-03-04 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-03-04-token-cost-updates-now-happen-immediately-as-usage-chunks-arrive-not-after-tool|Token/cost updates now happen immediately as usage chunks arrive, not after tool execution]] · Pricing
- 2026-03-03 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-03-03-feat-billing-implement-g1-ai-credits-overage-flow-with-billing-telemetry-by-gsqu|feat(billing): implement G1 AI credits overage flow with billing telemetry]] · Pricing

**2026-02**

- 2026-02-07 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-02-07-display-warning-when-user-has-no-copilot-subscription|Display warning when user has no Copilot subscription]] · Pricing
- 2026-02-05 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2026-02-05-codex-5-3-through-chatgpt-subscription|Codex-5.3 through ChatGPT subscription]] · Pricing
- 2026-02-04 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-02-04-removed-misleading-anthropic-api-pricing-from-model-selector-for-third-party-pro|Removed misleading Anthropic API pricing from model selector for third-party…]] · Pricing
- 2026-02-04 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2026-02-04-10274-add-credits-tooltip-pakrym-oai|♯10274 Add credits tooltip @pakrym-oai]] · Pricing

<details class="disclosure">
<summary>Fixes, digests and other changes · 10 (Claude Code 2 · Cursor 1 · Gemini CLI 1 · GitHub Copilot CLI 5 · Windsurf 1)</summary>

**2026-11**

- 2026-11-06 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-11-06-5-pricing-model-changes-in-v1-0-106|5 Pricing Model changes in v1.0.106]] · Digest

**2026-09**

- 2026-09-28 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-09-28-2-pricing-model-changes-in-v2-1-284|2 Pricing Model changes in v2.1.284]] · Digest
- 2026-09-10 · <span class="tl-product tl-p3">**Claude Code**</span> · [[Changes/Claude Code/2026-09-10-2-pricing-model-changes-in-v2-1-268|2 Pricing Model changes in v2.1.268]] · Digest

**2026-07**

- 2026-07-22 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2026-07-22-2-pricing-model-changes-in-cursor-router|2 Pricing Model changes in Cursor Router]] · Digest
- 2026-07-16 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-07-16-3-pricing-model-changes-in-v1-0-71|3 Pricing Model changes in v1.0.71]] · Digest

**2026-05**

- 2026-05-28 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-05-28-3-pricing-model-changes-in-v1-0-55|3 Pricing Model changes in v1.0.55]] · Digest
- 2026-05-23 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-05-23-3-pricing-model-changes-in-v1-0-52|3 Pricing Model changes in v1.0.52]] · Digest
- 2026-05-20 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-05-20-2-pricing-model-changes-in-v1-0-51|2 Pricing Model changes in v1.0.51]] · Digest

**2026-04**

- 2026-04-06 · <span class="tl-product tl-p10">**Windsurf**</span> · [[Changes/Windsurf/2026-04-06-updated-model-picker-with-pricing-context|Updated Model Picker with Pricing Context]] · Change

**2026-03**

- 2026-03-17 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-03-17-2-pricing-model-changes-in-v0-34-0|2 Pricing Model changes in v0.34.0]] · Digest

</details>

</details>

<details class="disclosure">
<summary>2025 · 35 entries (Aider 2 · ChatGPT 7 · Cline 7 · Codex CLI 3 · Cursor 7 · Gemini CLI 3 · GitHub Copilot CLI 1 · OpenHands 1 · Windsurf 4)</summary>

**2025-12**

- 2025-12-18 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-12-18-billing-groups|Billing groups]] · Pricing
- 2025-12-04 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-12-04-persisting-credits-if-new-snapshot-does-not-contain-credit-info-7490-zhao-oai|persisting credits if new snapshot does not contain credit info ♯7490 @zhao-oai]] · Pricing

**2025-11**

- 2025-11-19 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-11-19-credits-are-now-visible-in-status|Credits are now visible in /status]] · Pricing
- 2025-11-07 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-11-07-fixing-minor-formatting-issues-in-quota-and-pricing-md-by-hyangah-in-https-githu|fixing minor formatting issues in quota-and-pricing.md]] · Policy
- 2025-11-03 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2025-11-03-eligible-customers-in-india-can-now-get-12-months-of-chatgpt-go-at-no-cost-new-u|ChatGPT Go Promo - India]] · Pricing

**2025-10**

- 2025-10-30 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2025-10-30-we-re-excited-to-announce-that-chatgpt-go-our-low-cost-subscription-plan-is-now-44be9d|ChatGPT Go, our low cost subscription plan, is now available in 8 additional…]] · Expansion
- 2025-10-30 · <span class="tl-product tl-p5">**Codex CLI**</span> · [[Changes/Codex CLI/2025-10-30-ability-to-buy-credits-for-more-usage-more-information-https-help-openai-com-en|Ability to buy credits for more usage]] · Pricing
- 2025-10-28 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2025-10-28-we-re-launching-chatgpt-go-our-low-cost-subscription-plan-in-brazil-chatgpt-go-p|ChatGPT launches ChatGPT Go, our low cost subscription plan, in Brazil]] · Expansion
- 2025-10-14 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2025-10-14-we-re-excited-to-announce-that-chatgpt-go-our-low-cost-subscription-plan-is-now-d58cbb|ChatGPT Go, our low cost subscription plan, is now available in 71 additional…]] · Expansion
- 2025-10-08 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2025-10-08-we-re-excited-to-announce-that-chatgpt-go-our-low-cost-subscription-plan-is-now|ChatGPT Go, our low cost subscription plan, is now available in 16 additional countries]] · Expansion
- 2025-10-01 · <span class="tl-product tl-p8">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2025-10-01-switched-to-using-per-subscription-copilot-api-endpoints-in-accordance-with-gith|Switched to using per-subscription Copilot API endpoints in accordance…]] · Pricing

**2025-09**

- 2025-09-22 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2025-09-22-we-re-launching-chatgpt-go-our-low-cost-subscription-plan-in-indonesia-for-rp-75|ChatGPT launches ChatGPT Go, our low cost subscription plan, in Indonesia]] · Expansion

**2025-08**

- 2025-08-18 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2025-08-18-we-re-launching-chatgpt-go-a-new-low-cost-subscription-plan-this-will-initially-e5f740|ChatGPT launches ChatGPT Go, a new low-cost subscription plan]] · Launch
- 2025-08-18 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-08-18-update-quota-and-pricing-md-to-clarify-billing-by-blanca-delgado-parra-in-https|Update quota-and-pricing.md to clarify billing]] · Policy
- 2025-08-06 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-08-06-usage-and-pricing-visibility|Usage and pricing visibility]] · Pricing

**2025-07**

- 2025-07-31 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-07-31-adding-redirecturl-to-credits-purchasing-experience-by-pashpashpash-in-https-git|adding redirectUrl to credits purchasing experience]] · Pricing
- 2025-07-15 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-07-15-removing-reasoning-ux-for-grok-4-models-and-correct-pricing-by-arafatkatze-in-ht|Removing reasoning UX for Grok 4 models and correct pricing]] · Pricing
- 2025-07-11 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-07-11-supporting-buy-credits-url-response-from-backend-by-pashpashpash-in-https-github|supporting buy_credits_url response from backend]] · Pricing
- 2025-07-09 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-07-09-remove-incorrect-pricing-display-for-sap-ai-core-provider-since-it-uses-non-usd|Remove incorrect pricing display for SAP AI Core provider since it uses non-USD…]] · Pricing
- 2025-07-01 · <span class="tl-product tl-p7">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-07-01-docs-add-a-page-detailing-quota-and-cost-information-by-ptone-in-https-github-co|Docs: Add a page detailing quota and cost information]] · Policy

**2025-05**

- 2025-05-15 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-05-15-simpler-unified-pricing-6a915c|Simpler, unified pricing]] · Pricing
- 2025-05-15 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-05-15-introducing-unified-request-based-pricing-max-mode-for-all-top-models-and-backgr|Introducing unified request-based pricing, Max Mode for all top models…]] · Launch

**2025-04**

- 2025-04-20 · <span class="tl-product tl-p10">**Windsurf**</span> · [[Changes/Windsurf/2025-04-20-we-re-getting-rid-of-flow-action-credits|We're getting rid of Flow Action Credits]] · Pricing
- 2025-04-20 · <span class="tl-product tl-p10">**Windsurf**</span> · [[Changes/Windsurf/2025-04-20-user-prompt-credits|User Prompt Credits]] · Pricing
- 2025-04-20 · <span class="tl-product tl-p10">**Windsurf**</span> · [[Changes/Windsurf/2025-04-20-existing-plans|Existing Plans]] · Pricing
- 2025-04-15 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-04-15-eng-435-xai-provider-cost-issue-by-canvrno-in-https-github-com-cline-cline-pull|ENG-435/xAI provider cost issue]] · Pricing
- 2025-04-04 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2025-04-04-prevent-retrying-api-calls-when-the-provider-reports-insufficient-credits|Prevent retrying API calls when the provider reports insufficient credits]] · Pricing

**2025-03**

- 2025-03-31 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2025-03-31-warn-at-startup-if-stream-and-cache-prompts-are-used-together-as-cost-estimates|Warn at startup if --stream and --cache-prompts are used together, as cost…]] · Pricing
- 2025-03-28 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-03-28-add-cost-calculation-support-for-litellm-provider|Add cost calculation support for LiteLLM provider]] · Pricing
- 2025-03-25 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2025-03-25-display-api-cost-and-token-usage-in-frontend-by-autoltx-in-https-github-com-all|Display API cost and token usage in frontend]] · Pricing
- 2025-03-23 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-03-23-chat-will-now-display-a-notification-about-usage-based-pricing-when-approaching|Chat will now display a notification about usage-based pricing when approaching fast…]] · Policy
- 2025-03-23 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-03-23-usage-based-cost-visibility|Usage-based cost visibility]] · Pricing
- 2025-03-23 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2025-03-23-this-release-introduces-chat-tabs-for-parallel-conversations-a-redesignedmodes-s|Cursor introduces chat tabs for parallel conversations, a redesignedmodes system…]] · Launch

<details class="disclosure">
<summary>Fixes, digests and other changes · 2 (Cline 1 · Windsurf 1)</summary>

**2025-04**

- 2025-04-20 · <span class="tl-product tl-p10">**Windsurf**</span> · [[Changes/Windsurf/2025-04-20-updated-simplified-pricing|Updated & Simplified Pricing]] · Change

**2025-03**

- 2025-03-23 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2025-03-23-2-pricing-model-changes-in-v3-8-0|2 Pricing Model changes in v3.8.0]] · Digest

</details>

</details>

<details class="disclosure">
<summary>2024 · 6 entries (Aider 4 · Cline 1 · OpenHands 1)</summary>

**2024-09**

- 2024-09-12 · <span class="tl-product tl-p4">**Cline**</span> · [[Changes/Cline/2024-09-12-openrouter-now-supports-prompt-caching-they-re-still-working-on-reporting-cache|OpenRouter now supports prompt caching!]] · Pricing

**2024-08**

- 2024-08-20 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2024-08-20-improved-cost-estimate-logic-for-caching|Improved cost estimate logic for caching]] · Pricing
- 2024-08-13 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2024-08-13-improved-token-and-cost-reporting-for-infinite-output|Improved token and cost reporting for infinite output]] · Pricing

**2024-07**

- 2024-07-29 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2024-07-29-enhanced-token-usage-and-cost-reporting-now-works-when-streaming-too|Enhanced token usage and cost reporting]] · Pricing

**2024-06**

- 2024-06-04 · <span class="tl-product tl-p9">**OpenHands**</span> · [[Changes/OpenHands/2024-06-04-add-cost-metrics-to-evaluation-outputs-for-all-benchmarks-by-ryanhoangt-in-https|Add cost metrics to evaluation outputs for all benchmarks]] · Pricing

**2024-02**

- 2024-02-10 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2024-02-10-updated-all-openai-model-names-pricing-info|Updated all OpenAI model names, pricing info]] · Pricing

</details>

<details class="disclosure">
<summary>2023 · 7 entries (Aider 3 · ChatGPT 1 · Cursor 3)</summary>

**2023-11**

- 2023-11-03 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2023-11-03-pro-plan-if-you-hit-your-fast-request-limit-and-prefer-to-purchase-more-you-now|Pro++ plan: if you hit your fast request limit and prefer to purchase more, you now can]] · Policy

**2023-06**

- 2023-06-26 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2023-06-26-enables-display-of-cost-info-based-on-openai-advertised-pricing|Enables display of cost info based on OpenAI advertised pricing]] · Pricing
- 2023-06-26 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2023-06-26-enables-display-of-cost-info-based-on-openai-advertised-pricing-5f5b32|Enables display of cost info based on OpenAI advertised pricing]] · Pricing
- 2023-06-25 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2023-06-25-enables-display-of-cost-info-based-on-openai-advertised-pricing|Enables display of cost info based on OpenAI advertised pricing]] · Pricing

**2023-04**

- 2023-04-19 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2023-04-19-150k-gpt-4-tokens-included|150k GPT-4 tokens included]] · Pricing

**2023-03**

- 2023-03-27 · <span class="tl-product tl-p6">**Cursor**</span> · [[Changes/Cursor/2023-03-27-adds-an-optional-paid-plan-if-you-d-like-to-avoid-the-server-capacity-rate-limit|Adds an optional paid plan if you'd like to avoid the server capacity rate limits]] · Policy

**2023-02**

- 2023-02-13 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2023-02-13-we-rolled-out-the-ability-to-purchase-chatgpt-plus-internationally|We rolled out the ability to purchase ChatGPT Plus internationally]] · Pricing

</details>

<details class="disclosure" open>
<summary>2022 · 1 entry (ChatGPT 1)</summary>

**2022-12**

- 2022-12-15 · <span class="tl-product tl-p2">**ChatGPT**</span> · [[Changes/ChatGPT/2022-12-15-daily-limit-to-ensure-a-high-quality-experience-for-all-chatgpt-users-we-are-exp|Daily limit: To ensure a high-quality experience for all ChatGPT users, we…]] · Policy

</details>

</div>
<!-- chronolog:end -->