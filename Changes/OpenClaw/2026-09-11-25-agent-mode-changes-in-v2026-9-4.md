---
card_id: openclaw-2026-09-11-fc4b8d
date: '2026-09-11'
description: 'OpenClaw · 2026-09-11 · Agent Mode: 25 changes in v2026.9.4 — OpenClaw
  can help you get past a Node version problem without replacing your computer''s
  existing…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1163
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: b3a5aee3cc7bba1960dfd28e7c58a538c75fd2156216d5e2871ff592e5d4cee8
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-11-fc4b8d
  comparison: ''
  date: '2026-09-11'
  description: 'OpenClaw — v2026.9.4: 25 Agent Mode changes'
  evidence:
  - quote: OpenClaw can help you get past a Node version problem without replacing
      your computer's existing Node installation. New-agent setup also works with
      securely saved API keys, and the instructions for connecting a phone or removing
      OpenClaw now fill in steps that were missing.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: If you have several agents, guided messaging setup now lets you choose
      whose workspace to configure before separately choosing who should receive the
      messages. You can also choose an agent when managing setup recommendations ,
      so you work with the intended workspace. Setup scripts still need an explicit
      --agent choice when no default is configured. The device setup instructions
      also explain that connecting a device and approving the commands it can run
      are separate steps.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: The first-run help separates getting started from choosing a provider or
      hosting service, so you can find the answer for the step you are on. Setup examples
      also fill in missing tools, credentials, and commands, including how to match
      the Mac app with the right command-line version. When you ask the setup agent
      to inspect a setting, it can now find names containing dots or brackets that
      it previously reported as missing, while keeping secret values hidden.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: In the web app, you can preview an earlier message before jumping back
      to it, bring a quote into your next reply, and see what Codex's helper agents
      did while working on your request. There are also fixes for the interruptions
      that make a conversation harder to follow, from disappearing image previews
      to finished tasks that still look busy.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: Files keeps search and filters within reach while you scroll through long
      lists. You can find files the agent changed, read, or created, and a failed
      preview explains why the file could not open. Phone previews also leave more
      room for the document while keeping its name visible.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: If an agent file changes after you open it for editing, Save now warns
      you and keeps your draft. Choose Reload to use the newer file, or Overwrite
      to replace it with your version. Overwrite discards the newer changes rather
      than combining them, and the warning cannot catch every simultaneous edit made
      by another program.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: Open a Codex helper agent in Tasks to read its conversation, see its work,
      and load earlier messages. You can look at a file and return without making
      the conversation load again. Newly created tasks also stay readable as the main
      chat continues, although some older tasks still lack readable history, and resetting
      the chat or changing Codex accounts can prevent access.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: Finished and cancelled helper tasks stop showing their old working messages,
      while their summaries of changed files remain available. Long reports stay readable
      without hiding the button back to the conversation that started the task, and
      short progress updates no longer show stray formatting symbols. Agents also
      get clearer instructions to skip progress cards for quick questions and save
      them for substantial work.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: Click the Dashboard tab to give it the full task area, then click again
      to return to your previous layout. Your draft and anything entered into the
      dashboard stay in place. Dashboard progress also follows the conversation it
      belongs to, so selecting a different agent elsewhere does not make running work
      look paused.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: Usage keeps conversation details with the correct agent and counts the
      conversations actually shown in the list, with the total displayed separately.
      If you run OpenClaw on Linux with Bun, System busyness can show CPU and delay
      readings again instead of leaving permanent dashes. A dash just after starting
      still means the first reading is not ready.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: OpenClaw can catch some coding mistakes in widgets , the small interactive
      apps an agent can place in chat, before they appear. If a recent card fails
      while you use it, the web app can show a Script error notice and tell the agent
      what happened, giving it a chance to help you recover.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: If an update fails but the previous installation is restored and checked,
      the menu defaults to Exit. You can choose to investigate or preview a report
      before sending it. For other interactive update failures, the repair prompt
      tells you which AI agent will run and that it uses your account allowance or
      paid tokens. You can decline, but pressing Enter accepts and leaving the prompt
      unanswered starts the agent after 30 seconds.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: Claude-assisted repairs start without project customizations that could
      delay them. If your repair needs those custom tools or instructions, use the
      manual command provided instead. The repair-agent guide explains the choices
      and Claude requirements.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: Telegram recognizes mentions that tag the bot’s account in messages and
      photo captions. If you have native commands turned off, you can write /think
      high on one line and your request below it without losing the request. The /think
      menu also shows the setting for the agent handling that chat, and canceled attempts
      no longer leave a misleading “stalled” reaction afterward.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: Account lists and health checks more accurately show which accounts your
      agents use. Removing an account now reports when nothing was removed, and message-command
      errors explain how to choose an agent when one is needed.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: The Skills page now searches your installed skills and ClawHub together,
      so you can see what you already have and what you can add without checking separate
      places. Cards show which skills are ready or need setup, and switching agents
      shows the skills available to that agent. You can also browse popular skills
      without typing a search, while clearer titles and readable descriptions make
      it easier to choose.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: Doctor can repair several known Workshop problems that stopped upgrades
      or prevented OpenClaw from starting. Run openclaw doctor --fix when startup
      asks for it. Proposals and backups that need you to identify their agent remain
      available for review while other repairs continue. Some older review history
      may be discarded if its agent cannot be identified, and affected proposals may
      need reviewing again.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: Returning to a Claude conversation keeps its original chat connection and
      avoids a repeated user message in the affected resume cases. Claude can also
      stay running between turns when a skill check finds that nothing changed. In
      Codex chats with a fixed model choice, pasted text now reaches the agent instead
      of being lost.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: If you use A2A to connect agents , incoming requests now reach the agent
      assigned to that connection even when a new conversation begins. You can still
      choose a different agent for a particular conversation, and separate conversations
      keep their own history.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: Your Claw can make more decisions about routine commands without interrupting
      you, while still asking for approval when needed. There are also fixes for keeping
      file access within the permissions you chose, protecting shared conversation
      history when deleting an agent, and keeping private update records out of backups
      and support bundles.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: Automatic command review can now let suitable routine commands run, refuse
      a command with an explanation, or ask you to decide. This takes effect in existing
      automatic and workspace modes. In OpenClaw's built-in agent, the reviewer can
      use part of your conversation to check whether a command fits your request.
      High-risk actions still need human approval, and settings that always ask remain
      in force.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: Deleting an agent now stops if another agent needs it to read shared history.
      Moving that history is not yet supported, so keep the agent configured. If deletion
      fails partway through, fix the reported storage problem and retry. Before deleting
      a workspace that links to a neighboring folder, check what will be removed.
      Deletion through the Gateway may move that linked folder to Trash too; the offline
      command removes only the link.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: When a long AGENTS.md instruction file has to be shortened, an example
      keeps the line directly above it that explains what it is, helping keep a quotation
      from looking like a new instruction. The shortened instructions also recognize
      more Traditional Chinese rules, although the available space still limits what
      can be included.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: Subagents are helpers your Claw can send to work on part of a task. Helpers
      with visible conversations now get the time selected for their first task, so
      longer work is not cut short by the ordinary deadline. Later messages use the
      normal time limit. A separate fix helps finished results return to the right
      agent after a restart when several agents share one Gateway.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  - quote: Starting over with /new or /reset avoids unnecessary waits, especially
      in conversations where your Claw has handed work to other agents, and canceled
      tasks stay stopped when late results arrive. Your saved history and other conversations
      remain available.
    source_release: https://docs.openclaw.ai/releases/2026.9.4
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 25-agent-mode-changes-in-v2026-9-4
  source_release: openclaw-2026-09-11-v2026-9-4-6cdeafb2
  source_type: openclaw_changelog
  theme: agent-mode
  title: 25 Agent Mode changes in v2026.9.4
  type: change
related_changes:
- '[[Changes/Dify/2026-09-10-42-agent-mode-changes-in-1-17-1|42 Agent Mode changes
  in 1.17.1]]'
- '[[Changes/Runway/2026-09-10-agent-can-now-create-and-edit-brand-kits-for-you-right-in-the-conversation-group|Agent
  Brand Kits]]'
- '[[Changes/Claude Code/2026-09-11-2-agent-mode-changes-in-v2-1-269|2 Agent Mode
  changes in v2.1.269]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-11-v2026-9-4-6cdeafb2|openclaw-2026-09-11-v2026-9-4-6cdeafb2]]'
source_type: openclaw_changelog
theme: agent-mode
title: 25 Agent Mode changes in v2026.9.4
type: change
---

<!-- chronolog:begin region="header" -->
# 25 Agent Mode changes in v2026.9.4

**OpenClaw** · 2026-09-11 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.4) · from [[Releases/OpenClaw/openclaw-2026-09-11-v2026-9-4-6cdeafb2|v2026.9.4]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> OpenClaw can help you get past a Node version problem without replacing your computer's existing Node installation. New-agent setup also works with securely saved API keys, and the instructions for connecting a phone or removing OpenClaw now fill in steps that were missing.

> If you have several agents, guided messaging setup now lets you choose whose workspace to configure before separately choosing who should receive the messages. You can also choose an agent when managing setup recommendations , so you work with the intended workspace. Setup scripts still need an explicit --agent choice when no default is configured. The device setup instructions also explain that connecting a device and approving the commands it can run are separate steps.

> The first-run help separates getting started from choosing a provider or hosting service, so you can find the answer for the step you are on. Setup examples also fill in missing tools, credentials, and commands, including how to match the Mac app with the right command-line version. When you ask the setup agent to inspect a setting, it can now find names containing dots or brackets that it previously reported as missing, while keeping secret values hidden.

> In the web app, you can preview an earlier message before jumping back to it, bring a quote into your next reply, and see what Codex's helper agents did while working on your request. There are also fixes for the interruptions that make a conversation harder to follow, from disappearing image previews to finished tasks that still look busy.

> Files keeps search and filters within reach while you scroll through long lists. You can find files the agent changed, read, or created, and a failed preview explains why the file could not open. Phone previews also leave more room for the document while keeping its name visible.

> If an agent file changes after you open it for editing, Save now warns you and keeps your draft. Choose Reload to use the newer file, or Overwrite to replace it with your version. Overwrite discards the newer changes rather than combining them, and the warning cannot catch every simultaneous edit made by another program.

> Open a Codex helper agent in Tasks to read its conversation, see its work, and load earlier messages. You can look at a file and return without making the conversation load again. Newly created tasks also stay readable as the main chat continues, although some older tasks still lack readable history, and resetting the chat or changing Codex accounts can prevent access.

> Finished and cancelled helper tasks stop showing their old working messages, while their summaries of changed files remain available. Long reports stay readable without hiding the button back to the conversation that started the task, and short progress updates no longer show stray formatting symbols. Agents also get clearer instructions to skip progress cards for quick questions and save them for substantial work.

> Click the Dashboard tab to give it the full task area, then click again to return to your previous layout. Your draft and anything entered into the dashboard stay in place. Dashboard progress also follows the conversation it belongs to, so selecting a different agent elsewhere does not make running work look paused.

> Usage keeps conversation details with the correct agent and counts the conversations actually shown in the list, with the total displayed separately. If you run OpenClaw on Linux with Bun, System busyness can show CPU and delay readings again instead of leaving permanent dashes. A dash just after starting still means the first reading is not ready.

> OpenClaw can catch some coding mistakes in widgets , the small interactive apps an agent can place in chat, before they appear. If a recent card fails while you use it, the web app can show a Script error notice and tell the agent what happened, giving it a chance to help you recover.

> If an update fails but the previous installation is restored and checked, the menu defaults to Exit. You can choose to investigate or preview a report before sending it. For other interactive update failures, the repair prompt tells you which AI agent will run and that it uses your account allowance or paid tokens. You can decline, but pressing Enter accepts and leaving the prompt unanswered starts the agent after 30 seconds.

> Claude-assisted repairs start without project customizations that could delay them. If your repair needs those custom tools or instructions, use the manual command provided instead. The repair-agent guide explains the choices and Claude requirements.

> Telegram recognizes mentions that tag the bot’s account in messages and photo captions. If you have native commands turned off, you can write /think high on one line and your request below it without losing the request. The /think menu also shows the setting for the agent handling that chat, and canceled attempts no longer leave a misleading “stalled” reaction afterward.

> Account lists and health checks more accurately show which accounts your agents use. Removing an account now reports when nothing was removed, and message-command errors explain how to choose an agent when one is needed.

> The Skills page now searches your installed skills and ClawHub together, so you can see what you already have and what you can add without checking separate places. Cards show which skills are ready or need setup, and switching agents shows the skills available to that agent. You can also browse popular skills without typing a search, while clearer titles and readable descriptions make it easier to choose.

> Doctor can repair several known Workshop problems that stopped upgrades or prevented OpenClaw from starting. Run openclaw doctor --fix when startup asks for it. Proposals and backups that need you to identify their agent remain available for review while other repairs continue. Some older review history may be discarded if its agent cannot be identified, and affected proposals may need reviewing again.

> Returning to a Claude conversation keeps its original chat connection and avoids a repeated user message in the affected resume cases. Claude can also stay running between turns when a skill check finds that nothing changed. In Codex chats with a fixed model choice, pasted text now reaches the agent instead of being lost.

> If you use A2A to connect agents , incoming requests now reach the agent assigned to that connection even when a new conversation begins. You can still choose a different agent for a particular conversation, and separate conversations keep their own history.

> Your Claw can make more decisions about routine commands without interrupting you, while still asking for approval when needed. There are also fixes for keeping file access within the permissions you chose, protecting shared conversation history when deleting an agent, and keeping private update records out of backups and support bundles.

> Automatic command review can now let suitable routine commands run, refuse a command with an explanation, or ask you to decide. This takes effect in existing automatic and workspace modes. In OpenClaw's built-in agent, the reviewer can use part of your conversation to check whether a command fits your request. High-risk actions still need human approval, and settings that always ask remain in force.

> Deleting an agent now stops if another agent needs it to read shared history. Moving that history is not yet supported, so keep the agent configured. If deletion fails partway through, fix the reported storage problem and retry. Before deleting a workspace that links to a neighboring folder, check what will be removed. Deletion through the Gateway may move that linked folder to Trash too; the offline command removes only the link.

> When a long AGENTS.md instruction file has to be shortened, an example keeps the line directly above it that explains what it is, helping keep a quotation from looking like a new instruction. The shortened instructions also recognize more Traditional Chinese rules, although the available space still limits what can be included.

> Subagents are helpers your Claw can send to work on part of a task. Helpers with visible conversations now get the time selected for their first task, so longer work is not cut short by the ordinary deadline. Later messages use the normal time limit. A separate fix helps finished results return to the right agent after a restart when several agents share one Gateway.

> Starting over with /new or /reset avoids unnecessary waits, especially in conversations where your Claw has handed work to other agents, and canceled tasks stay stopped when late results arrive. Your saved history and other conversations remain available.

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
- [[Changes/OpenClaw/2026-09-11-20-model-support-changes-in-v2026-9-4|20 Model Support changes in v2026.9.4]] · Model Support
- [[Changes/OpenClaw/2026-09-11-14-account-and-access-changes-in-v2026-9-4|14 Account and Access changes in v2026.9.4]] · Account and Access
- [[Changes/OpenClaw/2026-09-11-you-can-now-search-installed-and-available-plugins-together-browse-by-purpose-an|Search installed and available plugins together, browse by purpose, and keep…]] · Apps and Integrations
- [[Changes/OpenClaw/2026-09-11-3-search-and-browsing-changes-in-v2026-9-4|3 Search and Browsing changes in v2026.9.4]] · Search and Browsing
- [[Changes/OpenClaw/2026-09-11-you-can-now-enable-desktop-access-for-azure-cloud-workers-whether-openclaw-manag|Enable desktop access for Azure cloud workers , whether OpenClaw manages them…]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-09-11-3-collaboration-changes-in-v2026-9-4|3 Collaboration changes in v2026.9.4]] · Collaboration
- [[Changes/OpenClaw/2026-09-11-2-context-window-changes-in-v2026-9-4|2 Context Window changes in v2026.9.4]] · Context Window
- [[Changes/OpenClaw/2026-09-11-56-other-changes-in-v2026-9-4|56 other changes in v2026.9.4]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-09-11 · Claude Code · [[Changes/Claude Code/2026-09-11-2-agent-mode-changes-in-v2-1-269|2 Agent Mode changes in v2.1.269]]
- Later: 2026-09-14 · Claude Code · [[Changes/Claude Code/2026-09-14-7-agent-mode-changes-in-v2-1-271|7 Agent Mode changes in v2.1.271]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-11-fc4b8d&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-11-25-agent-mode-changes-in-v2026-9-4.md%0ACard%20ID%3A%20openclaw-2026-09-11-fc4b8d%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.4%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->