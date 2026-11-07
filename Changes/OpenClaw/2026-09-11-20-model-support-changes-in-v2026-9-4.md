---
card_id: openclaw-2026-09-11-d71918
date: '2026-09-11'
description: 'OpenClaw · 2026-09-11 · Model Support: 20 changes in v2026.9.4 — Doctor
  can bring more older settings and saved accounts forward without losing your model…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1341
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 6d29cc76b1765e18f2b0e82067981b3a0cd58d1605f6d3fbb3948595b0e68ced
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-11-d71918
  comparison: ''
  date: '2026-09-11'
  description: 'OpenClaw — v2026.9.4: 20 Model Support changes'
  evidence:
  - quote: Doctor can bring more older settings and saved accounts forward without
      losing your model choices or asking you to edit configuration files by hand.
      It can also recognize a moved workspace and preserve its setup history, while
      leaving uncertain matches for review.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: If you enable Telegram rich messages , links inside lists, quotes, and
      expandable sections stay clickable and keep their styling. Code examples keep
      their spacing in messages and photo captions too. Sticker descriptions now use
      your chosen image model and reach your Claw in time for its first reply.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: Choose “Learn from past conversations” in Skill Workshop to open a chat
      where you can follow the work, add direction, or stop it. Auto lets your Claw
      apply improvements based on what it finds, while Propose leaves suggestions
      for you to approve. Starting this yourself does not turn on automatic self-learning,
      and normal model charges and access permissions still apply.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: If you connect to more than one Gateway, the model list now follows the
      Gateway and agent you selected, so you see the choices for the place where your
      work will run. Browsing the list no longer starts another search for models
      in the background. Refresh checks for new choices, and a failed refresh shows
      a warning while keeping compatible saved choices available. Update the Gateway
      before updating a separate command-line client. Updates to OpenClaw's model-and-price
      reference still need a Gateway restart before they take effect.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: Saved model choices are less likely to change unexpectedly, particularly
      when custom models have almost identical names. Each keeps its own settings
      for images, tools, and the amount of text it can handle. Chats started from
      another chat also show the model they actually inherit, and choosing Default
      stays in place after a restart. Default follows the configured model and its
      backups; explicitly choosing a particular model keeps the chat pinned to that
      choice.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: Searchable model menus make long lists easier to use without changing your
      choice until you select a result. Chat menus follow the account saved for that
      conversation, while New Session lets you preview another account you own. If
      a list fails to load, you can see the problem and try again.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: Editing backup models now preserves an inherited primary model, and removing
      every backup stays that way after a reload. Unavailable saved choices remain
      visible so you can remove them. Global defaults labels help distinguish shared
      settings from an individual agent's choices.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: People using custom AI servers keep the connection settings they entered
      when model lists are refreshed, instead of having another model's settings take
      over. Manually added models also stay in the list. If you use a custom server
      in place of a provider's usual service, you may need to list the models it supports
      explicitly. Integrations must use current sign-in details or explicitly configured
      credentials; old credentials saved only with a downloaded model list no longer
      authorize requests.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: When a model sends broken instructions for a tool, OpenClaw can try again
      instead of immediately abandoning the task. With Anthropic, it can also repair
      certain formatting mistakes. Retries are limited to cases where repeating the
      request is safe and may add cost. If earlier actions already happened, check
      their results before asking your Claw to continue.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: Errors also better distinguish connection problems, rejected sign-ins,
      and requests a provider cannot accept. Explanations stay in chat history, making
      it easier to understand why work stopped or a backup model was not tried.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: Anthropic conversations that use tools can reuse more of the instructions
      and conversation text already processed, instead of repeatedly saving the same
      growing history again. Compatible local models also get a more reusable starting
      prompt when you begin another conversation with the same instructions and tools.
      This can avoid repeated processing, though any effect on waiting time or charges
      depends on the provider and workload.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: If you run models on your own server, OpenClaw now uses the conversation
      size reported by vLLM, SGLang, and compatible services instead of falling back
      to a potentially wrong limit. That helps it budget how much text to send to
      the model, while any limit you entered yourself still takes priority. Opening
      vLLM model information for the first time also avoids some unnecessary loading
      work.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: Tencent users can choose Hy4 preview through TokenHub or TokenPlan, and
      new setups select it by default when the account has access. Existing model
      choices stay in place, so an upgrade does not silently switch you to the preview.
      Its thinking options are Off or High; selecting an intermediate level such as
      Low uses High, which can affect waiting time and usage.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: If you use Arcee through OpenRouter, OpenClaw now uses your matching saved
      OpenRouter account instead of asking for a separate Arcee credential. Your model
      settings stay attached to that choice, and different spellings of the same Arcee
      model stop looking like an unexpected model switch.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: When Kimi explicitly reports that you have used up a weekly allowance,
      OpenClaw no longer treats your valid key as broken. It can try a configured
      backup without unnecessarily blocking the provider's other models. Changing
      the key will not restore the allowance, though; wait for Kimi's quota window
      or use another provider with available capacity.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: Gemini web search now uses Gemini 3.6 Flash unless you chose a specific
      search model, helping accounts that could no longer use the old default. Your
      main chat model stays unchanged. Check the billing difference when upgrading,
      because Gemini 3 charges for each search query rather than once per prompt.
      There is also clearer help for setting up Kimi search and using Ollama cloud
      search while keeping model conversations local .
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: Setting up an account or checking a provider's options is easier in the
      reorganized OpenAI and model-provider guides . Shorter pages take you straight
      to the relevant instructions, and old bookmarks still point you toward the material
      that moved.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: If you track model usage, completed /btw side answers can now include their
      reported usage in your configured diagnostics. Those side questions still sit
      outside the conversation’s /usage cost total.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: Your Claw can recover a missing final reply in more cases where the work
      finished but the answer never arrived, including after a lost model connection
      or an earlier tool error. It asks the model for an explanation without repeating
      completed actions, giving you another chance to see what was done.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: Exported conversations keep file-read results that were incorrectly removed,
      including instructions for reading the next part of a file. With the relevant
      diagnostic recording enabled, records also include actions taken after switching
      to a backup model and partial responses received before an interruption. Sensitive
      information is still removed, and recording size limits still apply.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 20-model-support-changes-in-v2026-9-4
  source_release: openclaw-2026-09-11-v2026-9-4-6cdeafb2
  source_type: openclaw_changelog
  theme: model-support
  title: 20 Model Support changes in v2026.9.4
  type: change
related_changes:
- '[[Changes/Raycast/2026-09-10-ai-models-are-now-grouped-more-consistently-by-provider-including-models-from-ve|AI:
  Models are now grouped more consistently by provider, including models…]]'
- '[[Changes/Claude Code/2026-09-11-added-claude-code-gateway-model-discovery-timeout-ms-to-extend-the-llm-gateway-v|Added
  CLAUDE_CODE_GATEWAY_MODEL_DISCOVERY_TIMEOUT_MS to extend the LLM gateway…]]'
- '[[Changes/ElevenLabs/2026-09-11-scribe-v2-medical|Scribe v2 Medical]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-11-v2026-9-4-6cdeafb2|openclaw-2026-09-11-v2026-9-4-6cdeafb2]]'
source_type: openclaw_changelog
theme: model-support
title: 20 Model Support changes in v2026.9.4
type: change
---

<!-- chronolog:begin region="header" -->
# 20 Model Support changes in v2026.9.4

**OpenClaw** · 2026-09-11 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.4) · from [[Releases/OpenClaw/openclaw-2026-09-11-v2026-9-4-6cdeafb2|v2026.9.4]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Doctor can bring more older settings and saved accounts forward without losing your model choices or asking you to edit configuration files by hand. It can also recognize a moved workspace and preserve its setup history, while leaving uncertain matches for review.

> If you enable Telegram rich messages , links inside lists, quotes, and expandable sections stay clickable and keep their styling. Code examples keep their spacing in messages and photo captions too. Sticker descriptions now use your chosen image model and reach your Claw in time for its first reply.

> Choose “Learn from past conversations” in Skill Workshop to open a chat where you can follow the work, add direction, or stop it. Auto lets your Claw apply improvements based on what it finds, while Propose leaves suggestions for you to approve. Starting this yourself does not turn on automatic self-learning, and normal model charges and access permissions still apply.

> If you connect to more than one Gateway, the model list now follows the Gateway and agent you selected, so you see the choices for the place where your work will run. Browsing the list no longer starts another search for models in the background. Refresh checks for new choices, and a failed refresh shows a warning while keeping compatible saved choices available. Update the Gateway before updating a separate command-line client. Updates to OpenClaw's model-and-price reference still need a Gateway restart before they take effect.

> Saved model choices are less likely to change unexpectedly, particularly when custom models have almost identical names. Each keeps its own settings for images, tools, and the amount of text it can handle. Chats started from another chat also show the model they actually inherit, and choosing Default stays in place after a restart. Default follows the configured model and its backups; explicitly choosing a particular model keeps the chat pinned to that choice.

> Searchable model menus make long lists easier to use without changing your choice until you select a result. Chat menus follow the account saved for that conversation, while New Session lets you preview another account you own. If a list fails to load, you can see the problem and try again.

> Editing backup models now preserves an inherited primary model, and removing every backup stays that way after a reload. Unavailable saved choices remain visible so you can remove them. Global defaults labels help distinguish shared settings from an individual agent's choices.

> People using custom AI servers keep the connection settings they entered when model lists are refreshed, instead of having another model's settings take over. Manually added models also stay in the list. If you use a custom server in place of a provider's usual service, you may need to list the models it supports explicitly. Integrations must use current sign-in details or explicitly configured credentials; old credentials saved only with a downloaded model list no longer authorize requests.

> When a model sends broken instructions for a tool, OpenClaw can try again instead of immediately abandoning the task. With Anthropic, it can also repair certain formatting mistakes. Retries are limited to cases where repeating the request is safe and may add cost. If earlier actions already happened, check their results before asking your Claw to continue.

> Errors also better distinguish connection problems, rejected sign-ins, and requests a provider cannot accept. Explanations stay in chat history, making it easier to understand why work stopped or a backup model was not tried.

> Anthropic conversations that use tools can reuse more of the instructions and conversation text already processed, instead of repeatedly saving the same growing history again. Compatible local models also get a more reusable starting prompt when you begin another conversation with the same instructions and tools. This can avoid repeated processing, though any effect on waiting time or charges depends on the provider and workload.

> If you run models on your own server, OpenClaw now uses the conversation size reported by vLLM, SGLang, and compatible services instead of falling back to a potentially wrong limit. That helps it budget how much text to send to the model, while any limit you entered yourself still takes priority. Opening vLLM model information for the first time also avoids some unnecessary loading work.

> Tencent users can choose Hy4 preview through TokenHub or TokenPlan, and new setups select it by default when the account has access. Existing model choices stay in place, so an upgrade does not silently switch you to the preview. Its thinking options are Off or High; selecting an intermediate level such as Low uses High, which can affect waiting time and usage.

> If you use Arcee through OpenRouter, OpenClaw now uses your matching saved OpenRouter account instead of asking for a separate Arcee credential. Your model settings stay attached to that choice, and different spellings of the same Arcee model stop looking like an unexpected model switch.

> When Kimi explicitly reports that you have used up a weekly allowance, OpenClaw no longer treats your valid key as broken. It can try a configured backup without unnecessarily blocking the provider's other models. Changing the key will not restore the allowance, though; wait for Kimi's quota window or use another provider with available capacity.

> Gemini web search now uses Gemini 3.6 Flash unless you chose a specific search model, helping accounts that could no longer use the old default. Your main chat model stays unchanged. Check the billing difference when upgrading, because Gemini 3 charges for each search query rather than once per prompt. There is also clearer help for setting up Kimi search and using Ollama cloud search while keeping model conversations local .

> Setting up an account or checking a provider's options is easier in the reorganized OpenAI and model-provider guides . Shorter pages take you straight to the relevant instructions, and old bookmarks still point you toward the material that moved.

> If you track model usage, completed /btw side answers can now include their reported usage in your configured diagnostics. Those side questions still sit outside the conversation’s /usage cost total.

> Your Claw can recover a missing final reply in more cases where the work finished but the answer never arrived, including after a lost model connection or an earlier tool error. It asks the model for an explanation without repeating completed actions, giving you another chance to see what was done.

> Exported conversations keep file-read results that were incorrectly removed, including instructions for reading the next part of a file. With the relevant diagnostic recording enabled, records also include actions taken after switching to a backup model and partial responses received before an interruption. Sensitive information is still removed, and recording size limits still apply.

Source: https://docs.openclaw.ai/releases/2026.9.4
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-09-11-messages-arriving-while-openclaw-is-paused-now-wait-until-it-is-ready-again-and|Messages arriving while OpenClaw is paused now wait until it is ready again…]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-09-11-images-you-send-stay-visible-while-the-conversation-updates-and-scrolling-back-t|Images you send stay visible while the conversation updates, and scrolling back…]] · Files and Data
- [[Changes/OpenClaw/2026-09-11-7-automation-and-scheduling-changes-in-v2026-9-4|7 Automation and Scheduling changes in v2026.9.4]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-09-11-with-diagnostic-recording-enabled-openrouter-can-return-finished-music-or-a-usag|With diagnostic recording enabled, OpenRouter can return finished music…]] · Music Generation
- [[Changes/OpenClaw/2026-09-11-18-developer-workflow-changes-in-v2026-9-4|18 Developer Workflow changes in v2026.9.4]] · Developer Workflow
- [[Changes/OpenClaw/2026-09-11-2-reliability-and-performance-changes-in-v2026-9-4|2 Reliability and Performance changes in v2026.9.4]] · Reliability and Performance
- [[Changes/OpenClaw/2026-09-11-16-mobile-and-desktop-changes-in-v2026-9-4|16 Mobile and Desktop changes in v2026.9.4]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-09-11-the-bundled-video-frames-skill-and-its-helper-script-have-been-removed-if-you-us|The bundled video-frames skill and its helper script have been removed]] · Multimodal Input
- [[Changes/OpenClaw/2026-09-11-5-interface-experience-changes-in-v2026-9-4|5 Interface Experience changes in v2026.9.4]] · Interface Experience
- [[Changes/OpenClaw/2026-09-11-14-memory-and-personalization-changes-in-v2026-9-4|14 Memory and Personalization changes in v2026.9.4]] · Memory and Personalization
- [[Changes/OpenClaw/2026-09-11-you-can-now-answer-your-claw-s-questions-and-enter-secrets-from-the-terminal-wit|Answer your Claw’s questions and enter secrets from the terminal, with clearer…]] · Developer Workflow
- [[Changes/OpenClaw/2026-09-11-2-image-generation-changes-in-v2026-9-4|2 Image Generation changes in v2026.9.4]] · Image Generation
- [[Changes/OpenClaw/2026-09-11-3-pricing-model-changes-in-v2026-9-4|3 Pricing Model changes in v2026.9.4]] · Pricing Model
- [[Changes/OpenClaw/2026-09-11-you-can-now-reach-the-official-app-store-listing-straight-from-the-iphone-setup|Reach the official App Store listing straight from the iPhone setup guide]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-09-11-5-editor-experience-changes-in-v2026-9-4|5 Editor Experience changes in v2026.9.4]] · Editor Experience
- [[Changes/OpenClaw/2026-09-11-you-can-now-choose-deepgram-flux-to-turn-incoming-voice-notes-into-text-your-cla|Choose Deepgram Flux to turn incoming voice notes into text your Claw can use…]] · Voice and Audio
- [[Changes/OpenClaw/2026-09-11-8-voice-and-audio-changes-in-v2026-9-4|8 Voice and Audio changes in v2026.9.4]] · Voice and Audio
- [[Changes/OpenClaw/2026-09-11-12-safety-and-privacy-changes-in-v2026-9-4|12 Safety and Privacy changes in v2026.9.4]] · Safety and Privacy
- [[Changes/OpenClaw/2026-09-11-22-apps-and-integrations-changes-in-v2026-9-4|22 Apps and Integrations changes in v2026.9.4]] · Apps and Integrations
- [[Changes/OpenClaw/2026-09-11-14-account-and-access-changes-in-v2026-9-4|14 Account and Access changes in v2026.9.4]] · Account and Access
- [[Changes/OpenClaw/2026-09-11-you-can-now-search-installed-and-available-plugins-together-browse-by-purpose-an|Search installed and available plugins together, browse by purpose, and keep…]] · Apps and Integrations
- [[Changes/OpenClaw/2026-09-11-3-search-and-browsing-changes-in-v2026-9-4|3 Search and Browsing changes in v2026.9.4]] · Search and Browsing
- [[Changes/OpenClaw/2026-09-11-you-can-now-enable-desktop-access-for-azure-cloud-workers-whether-openclaw-manag|Enable desktop access for Azure cloud workers , whether OpenClaw manages them…]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-09-11-3-collaboration-changes-in-v2026-9-4|3 Collaboration changes in v2026.9.4]] · Collaboration
- [[Changes/OpenClaw/2026-09-11-25-agent-mode-changes-in-v2026-9-4|25 Agent Mode changes in v2026.9.4]] · Agent Mode
- [[Changes/OpenClaw/2026-09-11-2-context-window-changes-in-v2026-9-4|2 Context Window changes in v2026.9.4]] · Context Window
- [[Changes/OpenClaw/2026-09-11-56-other-changes-in-v2026-9-4|56 other changes in v2026.9.4]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-09-11 · ElevenLabs · [[Changes/ElevenLabs/2026-09-11-scribe-v2-medical|Scribe v2 Medical]]
- Later: 2026-09-11 · Raycast · [[Changes/Raycast/2026-09-11-bring-your-own-subscriptions|Bring Your Own Subscriptions]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-11-d71918&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-11-20-model-support-changes-in-v2026-9-4.md%0ACard%20ID%3A%20openclaw-2026-09-11-d71918%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.4%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->