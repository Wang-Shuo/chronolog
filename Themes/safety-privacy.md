---
created: '2020-07-28'
date: '2026-11-06'
description: 'Research question: which safeguards and privacy controls do the tracked
  products add, and for whom?'
machine_hash: cfc15e8bd76dbac95418cd0e79e793934949cebe5374ebfccde28f8b13190553
modified: '2026-11-06'
products_involved:
- Aider
- AnythingLLM
- ChatGPT
- Claude
- Claude Code
- Cline
- Codex CLI
- Cursor
- Descript
- Devin
- Dify
- ElevenLabs
- Gemini
- Gemini CLI
- GitHub Copilot CLI
- Google Antigravity
- Granola
- HeyGen
- Kimi Code
- LM Studio
- Lovable
- Manus
- Microsoft 365 Copilot
- Notion
- Ollama
- Open WebUI
- OpenClaw
- OpenCode
- OpenHands
- Qoder
- Raycast
- Replit
- Runway
- Superwhisper
- Synthesia
- Windsurf
- Wispr Flow
- Z.ai API
- v0
publication: active
status: official
tags:
- theme
- moc
theme: safety-privacy
title: Safety and Privacy
---

<!-- chronolog:begin region="header" -->
# Safety and Privacy

941 tracked changes across Aider, AnythingLLM, ChatGPT, Claude, Claude Code, Cline, Codex CLI, Cursor, Descript, Devin, Dify, ElevenLabs, Gemini, Gemini CLI, GitHub Copilot CLI, Google Antigravity, Granola, HeyGen, Kimi Code, LM Studio, Lovable, Manus, Microsoft 365 Copilot, Notion, Ollama, Open WebUI, OpenClaw, OpenCode, OpenHands, Qoder, Raycast, Replit, Runway, Superwhisper, Synthesia, Windsurf, Wispr Flow, Z.ai API and v0 · 2020-07-28 → 2026-11-06 · OpenClaw averages 18.4 cards per release, Microsoft 365 Copilot 11.2, ElevenLabs 8.1, Codex CLI 8.0, Open WebUI 7.6, Gemini CLI 7.5, Devin 7.5, AnythingLLM 7.3, Dify 7.2, Claude Code 7.0, GitHub Copilot CLI 6.3, OpenCode 6.0, HeyGen 5.3, Raycast 5.2, Google Antigravity 5.0, Replit 4.9, Kimi Code 4.5, Qoder 4.2, Cursor 4.0, Lovable 3.9, OpenHands 3.8, Wispr Flow 3.8, Aider 3.7, Notion 3.6, LM Studio 3.3, Cline 3.0, Ollama 3.0, Descript 2.9, v0 2.9, Windsurf 2.6, Superwhisper 2.1, Z.ai API 2.1, ChatGPT 1.7, Gemini 1.5, Claude 1.3, Manus 1.2, Granola 1.0, Runway 1.0, Synthesia 1.0
<!-- chronolog:end -->

## Research summary
<!-- chronolog:begin region="narrative" -->
**Research question: which safeguards and privacy controls do the tracked products add, and for whom?**

ChatGPT's [2023-08-28 Enterprise launch](https://help.openai.com/en/articles/6825453-chatgpt-release-notes#introducing-chatgpt-enterprise) ([[Releases/ChatGPT/chatgpt-2023-08-28-introducing-chatgpt-enterprise-eb7127e6|archived]]) offers enterprise-grade security and privacy. The [2025-09-29 note](https://help.openai.com/en/articles/6825453-chatgpt-release-notes#parental-controls) ([[Releases/ChatGPT/chatgpt-2025-09-29-parental-controls-8b95b69a|archived]]) rolls out parental controls globally, with teen accounts connected to a parent's account, and the [2026-01-20 note](https://help.openai.com/en/articles/6825453-chatgpt-release-notes#rolling-out-age-prediction) ([[Releases/ChatGPT/chatgpt-2026-01-20-rolling-out-age-prediction-2382655a|archived]]) adds an age prediction model on consumer plans that estimates whether an account likely belongs to someone under 18. [Lockdown Mode on 2026-06-04](https://help.openai.com/en/articles/6825453-chatgpt-release-notes#lockdown-mode-is-now-available-to-all-logged-in-users) ([[Releases/ChatGPT/chatgpt-2026-06-04-lockdown-mode-is-now-available-to-all-logged-in-users-f7dcb357|archived]]) becomes available to all logged-in users as an opt-in setting that limits web and external-service access to reduce the risk of data exfiltration from prompt injection, and the [2026-09-21 Privacy Center](https://help.openai.com/en/articles/6825453-chatgpt-release-notes#privacy-center-in-chatgpt) ([[Releases/ChatGPT/chatgpt-2026-09-21-privacy-center-in-chatgpt-ecef9fba|archived]]) gathers information about chat privacy, memory, data use, connected apps and account security for Free, Go, Plus and Pro users.

Cursor's [2023-04-16 release](https://cursor.com/changelog/0-2-4) ([[Releases/Cursor/cursor-2023-04-16-0-2-4-https-cursor-com-changelog-0-2-4-1ed55ed8|archived]]) adds Ghost mode for opting out of storing any kind of data on Cursor's servers. The [2025-09-29 release](https://cursor.com/changelog/1-7) ([[Releases/Cursor/cursor-2025-09-29-1-7-https-cursor-com-changelog-1-7-0a03c0ae|archived]]) runs non-allowlisted commands in a sandbox with read/write access to the workspace and no internet access, which [Cursor 2.0 on 2025-10-29](https://cursor.com/changelog/2-0) ([[Releases/Cursor/cursor-2025-10-29-2-0-https-cursor-com-changelog-2-0-66a8e76e|archived]]) makes the default for agent commands on macOS, and the [2026-02-17 release](https://cursor.com/changelog/2-5) ([[Releases/Cursor/cursor-2026-02-17-2-5-https-cursor-com-changelog-2-5-82892320|archived]]) adds granular network and filesystem access controls to the sandbox. The [2026-04-30 release](https://cursor.com/changelog/04-30-26) ([[Releases/Cursor/cursor-2026-04-30-cursor-security-review-https-cursor-com-changelog-04-30-26-640898b1|archived]]) adds a Security Reviewer, in beta for Teams and Enterprise, that checks every pull request for security vulnerabilities, privacy and data-handling risks and prompt injection.

Claude Code's [v2.1.83 on 2026-03-25](https://github.com/anthropics/claude-code/releases/tag/v2.1.83) ([[Releases/Claude Code/claude-code-2026-03-25-v2-1-83-github-301019202-ba6a8317|archived]]) adds a setting that strips Anthropic and cloud-provider credentials from subprocess environments, and [v2.1.136 on 2026-05-08](https://github.com/anthropics/claude-code/releases/tag/v2.1.136) ([[Releases/Claude Code/claude-code-2026-05-08-v2-1-136-github-319609716-58f21368|archived]]) adds auto mode classifier rules that block actions unconditionally. [v2.1.187 on 2026-06-23](https://github.com/anthropics/claude-code/releases/tag/v2.1.187) ([[Releases/Claude Code/claude-code-2026-06-23-v2-1-187-github-343665388-744f9775|archived]]) blocks sandboxed commands from reading credential files and secret environment variables, [v2.1.200 on 2026-07-03](https://github.com/anthropics/claude-code/releases/tag/v2.1.200) ([[Releases/Claude Code/claude-code-2026-07-03-v2-1-200-github-348415228-64d6d68d|archived]]) renames the “default” permission mode to “Manual”, and [v2.1.284 on 2026-09-28](https://github.com/anthropics/claude-code/releases/tag/v2.1.284) ([[Releases/Claude Code/claude-code-2026-09-28-v2-1-284-github-398457074-cbb49e49|archived]]) starts interactive terminal and VS Code sessions in auto mode when no permission mode is configured, on every plan and provider.

**Uncertainty and scope:** this editorial summary covers ChatGPT, Claude Code and Cursor; the timeline includes all tracked products and Claude Code coverage starts on 2025-12-19; the controls serve different users, from families and workspace admins to developers running agents, and rollouts vary by plan and region, so the announcements neither measure how well a safeguard works nor compare protection across products.
<!-- chronolog:end -->

## Key moments
<!-- chronolog:begin region="moments" -->
Selected automatically from launches and standalone announcements.

| Quarter | Aider | AnythingLLM | ChatGPT | Claude | Claude Code | Cline | Codex CLI | Cursor | Descript | Devin | Dify | ElevenLabs | Gemini | Gemini CLI | GitHub Copilot CLI | Google Antigravity | Granola | HeyGen | Kimi Code | LM Studio | Lovable | Manus | Microsoft 365 Copilot | Notion | Ollama | Open WebUI | OpenClaw | OpenCode | OpenHands | Qoder | Raycast | Replit | Runway | Superwhisper | Synthesia | Windsurf | Wispr Flow | Z.ai API | v0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **First in archive** | <time datetime="2023-07-24">2023-07-24</time> [[Changes/Aider/2023-07-24-encourage-gpt-to-use-language-like-add-files-to-the-chat-to-ask-users-for-permis\|Encourage GPT to use language like "add files to the chat" to ask users…]] | <time datetime="2024-07-26">2024-07-26</time> [[Changes/AnythingLLM/2024-07-26-3-safety-and-privacy-changes-in-v1-0-0\|3 Safety and Privacy changes in v1.0.0]] | <time datetime="2023-08-28">2023-08-28</time> [[Changes/ChatGPT/2023-08-28-today-we-re-launching-chatgpt-enterprise-which-offers-enterprise-grade-security-4958cf\|Introducing ChatGPT Enterprise]] | <time datetime="2025-08-06">2025-08-06</time> [[Changes/Claude/2025-08-06-claude-code-security-reviews\|Claude Code Security Reviews]] | <time datetime="2026-01-09">2026-01-09</time> [[Changes/Claude Code/2026-01-09-2-safety-and-privacy-changes-in-v2-1-2\|2 Safety and Privacy changes in v2.1.2]] | <time datetime="2024-12-18">2024-12-18</time> [[Changes/Cline/2024-12-18-cline-s-most-requested-feature-is-here-you-can-now-let-cline-work-more-autonomou\|Cline's most requested feature is here 🎉 You can now let Cline work more…]] | <time datetime="2025-07-08">2025-07-08</time> [[Changes/Codex CLI/2025-07-08-adds-support-for-a-sandbox-flag-and-makes-some-breaking-changes-to-config-toml-a\|Adds support for a --sandbox flag and makes some breaking changes to config.toml…]] | <time datetime="2023-04-16">2023-04-16</time> [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers\|Ghost mode for opting out of storing any kind of data on our servers]] | <time datetime="2020-07-28">2020-07-28</time> [[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc\|Revoke Application Access]] | <time datetime="2025-08-12">2025-08-12</time> [[Changes/Devin/2025-08-12-vpc-repo-indexing\|VPC Repo Indexing]] | <time datetime="2023-08-15">2023-08-15</time> [[Changes/Dify/2023-08-15-fix-frontend-permission-check-by-matriq-in-https-github-com-langgenius-dify-pull\|fix: frontend permission check]] | <time datetime="2025-04-14">2025-04-14</time> [[Changes/ElevenLabs/2025-04-14-pronunciation-dictionaries\|Pronunciation Dictionaries]] | <time datetime="2023-12-18">2023-12-18</time> [[Changes/Gemini/2023-12-18-expanding-bard-extensions-to-new-languages\|Expanding Bard Extensions to new languages]] | <time datetime="2025-07-01">2025-07-01</time> [[Changes/Gemini CLI/2025-07-01-esc-to-exit-privacy-screen-in-error-state-by-scidomino-in-https-github-com-googl\|Esc to exit privacy screen in error state]] | <time datetime="2025-09-26">2025-09-26</time> [[Changes/GitHub Copilot CLI/2025-09-26-improved-the-error-message-received-when-using-a-pat-that-is-missing-the-copilot\|Improved the error message received when using a PAT that is missing…]] | <time datetime="2025-12-08">2025-12-08</time> [[Changes/Google Antigravity/2025-12-08-various-security-fixes\|Various security fixes]] | <time datetime="2025-07-07">2025-07-07</time> [[Changes/Granola/2025-07-07-we-ve-shown-independent-auditors-that-our-security-practices-meet-soc2-type-2-st\|Granola is SOC2 compliant]] | <time datetime="2026-01-14">2026-01-14</time> [[Changes/HeyGen/2026-01-14-what-s-new-a-new-guided-flow-lets-you-create-your-avatar-with-a-single-15-second\|What's new: A new guided flow lets you create your avatar with a single 15-second…]] | <time datetime="2026-05-28">2026-05-28</time> [[Changes/Kimi Code/2026-05-28-add-auto-slash-command-and-auto-cli-flag-for-auto-permission-mode\|Add /auto slash command and --auto CLI flag for auto permission mode]] | <time datetime="2025-06-25">2025-06-25</time> [[Changes/LM Studio/2025-06-25-fixed-a-bug-where-tool-permission-dialog-wouldn-t-auto-scroll-to-the-bottom-of-t\|Fixed a bug where tool permission dialog wouldn't auto-scroll to the bottom of the chat]] | <time datetime="2025-01-18">2025-01-18</time> [[Changes/Lovable/2025-01-18-sandbox-issues-are-resolved-and-the-service-is-fully-operational-again\|Sandbox issues are resolved, and the service is fully operational again]] | <time datetime="2025-06-20">2025-06-20</time> [[Changes/Manus/2025-06-20-open-the-browser-in-a-session-log-in-manually-once-we-encrypt-save-your-login-st\|Introducing Manus Cloud Browser]] | <time datetime="2026-01-13">2026-01-13</time> [[Changes/Microsoft 365 Copilot/2026-01-13-simplified-servicenow-tickets-setup-with-per-table-acl-rules-web-microsoft-365-c\|Simplified ServiceNow tickets setup with per-table ACL rules…]] | <time datetime="2020-11-11">2020-11-11</time> [[Changes/Notion/2020-11-11-flexible-sub-page-permissions\|Flexible sub-page permissions 📑]] | <time datetime="2023-11-17">2023-11-17</time> [[Changes/Ollama/2023-11-17-fix-permission-denied-issues-when-running-ollama-create-on-linux\|Fix permission denied issues when running ollama create on Linux]] | <time datetime="2024-04-04">2024-04-04</time> [[Changes/Open WebUI/2024-04-04-security-patches-applied-necessary-security-patches\|🔒 Security Patches: Applied necessary security patches]] | <time datetime="2026-06-30">2026-06-30</time> [[Changes/OpenClaw/2026-06-30-6-safety-and-privacy-changes-in-v2026-6-11\|6 Safety and Privacy changes in v2026.6.11]] | <time datetime="2026-01-04">2026-01-04</time> [[Changes/OpenCode/2026-01-04-13-safety-and-privacy-changes-in-v1-1-1\|13 Safety and Privacy changes in v1.1.1]] | <time datetime="2024-06-04">2024-06-04</time> [[Changes/OpenHands/2024-06-04-2-safety-and-privacy-changes-in-0-6-1\|2 Safety and Privacy changes in 0.6.1]] | <time datetime="2026-08-27">2026-08-27</time> [[Changes/Qoder/2026-08-27-harness-for-complex-tasks-qoder-s-harness-keeps-planning-execution-verification\|Harness for complex tasks]] | <time datetime="2020-10-16">2020-10-16</time> [[Changes/Raycast/2020-10-16-important-we-changed-permission-scopes-required-to-use-github-so-you-will-be-ask\|⚠️ Important: We changed permission scopes required to use GitHub so you will…]] | <time datetime="2025-04-25">2025-04-25</time> [[Changes/Replit/2025-04-25-advanced-privacy-settings-for-teams\|Advanced privacy settings for teams]] | <time datetime="2024-06-14">2024-06-14</time> [[Changes/Runway/2024-06-14-creating-a-custom-voice-will-now-require-explicit-user-consent\|Voice Verification]] | <time datetime="2024-03-13">2024-03-13</time> [[Changes/Superwhisper/2024-03-13-if-user-has-completed-onboarding-do-not-continue-prompting-for-accessiblity-perm\|If user has completed onboarding, do not continue prompting for accessiblity permission]] | <time datetime="2026-05-29">2026-05-29</time> [[Changes/Synthesia/2026-05-29-members-on-free-and-restricted-licenses-can-now-edit-scripts-and-add-screen-reco\|Let free workspace members help you edit]] | <time datetime="2026-09-10">2026-09-10</time> [[Changes/Windsurf/2026-09-10-devin-cloud\|Devin Cloud]] | <time datetime="2026-03-31">2026-03-31</time> [[Changes/Wispr Flow/2026-03-31-security-privacy-desktop\|Security & Privacy (Desktop)]] | <time datetime="2026-08-18">2026-08-18</time> [[Changes/Z.ai API/2026-08-18-emergent-cybersecurity-capabilities-glm-5-3-matches-mythos-5-in-white-box-code-r\|Emergent Cybersecurity Capabilities]] | <time datetime="2025-12-12">2025-12-12</time> [[Changes/v0/2025-12-12-cve-2025-55184-denial-of-service-dos-vulnerability\|CVE-2025-55184 : Denial of Service (DoS) vulnerability]] |
| 2026 Q4 | · | · | · | · | · | · | · | · | · | <time datetime="2026-10-30">2026-10-30</time> [[Changes/Devin/2026-10-30-pylon-setup-dialog\|Pylon Setup Dialog]]<br><time datetime="2026-10-14">2026-10-14</time> [[Changes/Devin/2026-10-14-manage-devin-review-permission\|Manage Devin Review Permission]] | · | · | · | · | · | <time datetime="2026-10-22">2026-10-22</time> [[Changes/Google Antigravity/2026-10-22-notifications-settings-docked-question-prompts-and-conversation-palette-filters\|Notifications settings, docked question prompts, and conversation palette filters]] | · | <time datetime="2026-10-13">2026-10-13</time> [[Changes/HeyGen/2026-10-13-admin-billing-and-security\|Admin, billing and security]] | · | · | <time datetime="2026-11-03">2026-11-03</time> [[Changes/Lovable/2026-11-03-redesigned-privacy-security-settings\|Redesigned Privacy & security settings]]<br><time datetime="2026-11-02">2026-11-02</time> [[Changes/Lovable/2026-11-02-redesigned-action-center-reviews\|Redesigned Action center reviews]] | · | · | · | · | · | · | <time datetime="2026-10-22">2026-10-22</time> [[Changes/OpenCode/2026-10-22-upgraded-the-bundled-bun-runtime-to-1-4-4\|Upgraded the bundled Bun runtime to 1.4.4]] | · | · | · | · | · | · | · | · | <time datetime="2026-10-02">2026-10-02</time> [[Changes/Wispr Flow/2026-10-02-for-teams-enterprise-all-platforms\|For Teams & Enterprise: (All platforms)]] | · | · |
| 2026 Q3 | · | · | <time datetime="2026-09-25">2026-09-25</time> [[Changes/ChatGPT/2026-09-25-we-re-introducing-security-history-a-new-way-to-review-recent-security-activity-6f32cc\|Security history in ChatGPT]] | · | · | · | · | <time datetime="2026-09-23">2026-09-23</time> [[Changes/Cursor/2026-09-23-today-we-re-launching-two-cursor-bots-for-the-last-mile-of-shipping-code-rollout-af394f\|Cursor launches two Cursor bots for the last mile of shipping code]] | · | · | <time datetime="2026-07-17">2026-07-17</time> [[Changes/Dify/2026-07-17-agent-app-enters-open-beta-and-is-now-enabled-by-default-for-all-users-it-introd\|Agent App enters open beta and is now enabled by default for all users]] | <time datetime="2026-08-24">2026-08-24</time> [[Changes/ElevenLabs/2026-08-24-packages\|Packages]] | · | · | · | <time datetime="2026-09-19">2026-09-19</time> [[Changes/Google Antigravity/2026-09-19-windows-sandbox-support\|Windows sandbox support]] | · | <time datetime="2026-09-04">2026-09-04</time> [[Changes/HeyGen/2026-09-04-identity-verification-ui-update\|Identity verification UI update]] | · | · | · | · | <time datetime="2026-07-01">2026-07-01</time> [[Changes/Microsoft 365 Copilot/2026-07-01-edit-capability-for-selecting-permission-reading-option-for-existing-servicenow\|Edit capability for selecting permission reading option for existing ServiceNow…]] | · | · | · | · | · | · | archive begins <time datetime="2026-08-27">2026-08-27</time> | · | <time datetime="2026-09-25">2026-09-25</time> [[Changes/Replit/2026-09-25-control-access-to-design-systems-and-slide-templates\|Control access to design systems and slide templates]]<br><time datetime="2026-09-18">2026-09-18</time> [[Changes/Replit/2026-09-18-investigate-with-expanded-audit-logs\|Investigate with expanded audit logs]] | · | · | · | <time datetime="2026-09-10">2026-09-10</time> [[Changes/Windsurf/2026-09-10-devin-cloud\|Devin Cloud]] | · | · | · |
| 2026 Q2 | · | · | <time datetime="2026-06-04">2026-06-04</time> [[Changes/ChatGPT/2026-06-04-lockdown-mode-is-now-available-to-all-logged-in-users-across-account-types-and-w\|Lockdown Mode is now available to all logged-in users]] | <time datetime="2026-05-21">2026-05-21</time> [[Changes/Claude/2026-05-21-claude-now-works-with-more-security-and-compliance-tools\|Claude now works with more security and compliance tools]] | <time datetime="2026-04-16">2026-04-16</time> [[Changes/Claude Code/2026-04-16-added-less-permission-prompts-skill-scans-transcripts-for-common-read-only-bash\|Added /less-permission-prompts skill]] | · | · | <time datetime="2026-06-10">2026-06-10</time> [[Changes/Cursor/2026-06-10-run-bugbot-before-you-push-3e5964\|Run Bugbot before you push]] | · | · | · | · | · | · | <time datetime="2026-04-27">2026-04-27</time> [[Changes/GitHub Copilot CLI/2026-04-27-location-based-permission-persistence-is-now-enabled-by-default-so-approvals-car\|Location-based permission persistence is now enabled by default, so approvals carry…]] | · | · | · | archive begins <time datetime="2026-05-26">2026-05-26</time> | · | · | · | · | <time datetime="2026-05-13">2026-05-13</time> [[Changes/Notion/2026-05-13-meet-your-notion-workers\|Meet your Notion Workers]] | · | · | archive begins <time datetime="2026-06-30">2026-06-30</time> | · | · | <span class="not-archived">not archived</span> | · | · | · | · | · | · | · | · | · |
| 2026 Q1 | · | · | · | · | · | · | · | · | · | · | · | · | <time datetime="2026-01-20">2026-01-20</time> [[Changes/Gemini/2026-01-20-gemini-introduces-personal-intelligence\|Gemini introduces Personal Intelligence]] | · | · | · | · | · | <span class="not-archived">not archived</span> | · | · | · | archive begins <time datetime="2026-01-13">2026-01-13</time> | · | · | · | <span class="not-archived">not archived</span> | · | <time datetime="2026-03-30">2026-03-30</time> [[Changes/OpenHands/2026-03-30-added-clear-command-for-v1-conversations-typing-clear-in-the-chat-creates-a-new\|Added /clear command for V1 conversations]] | <span class="not-archived">not archived</span> | · | · | · | · | · | · | archive begins <time datetime="2026-03-31">2026-03-31</time> | · | · |
| 2025 Q4 | · | · | · | · | archive begins <time datetime="2025-12-19">2025-12-19</time> | · | · | · | · | · | · | · | · | · | · | archive begins <time datetime="2025-11-18">2025-11-18</time> | · | archive begins <time datetime="2025-11-29">2025-11-29</time> | <span class="not-archived">not archived</span> | · | · | · | <span class="not-archived">not archived</span> | · | · | <time datetime="2025-11-24">2025-11-24</time> [[Changes/Open WebUI/2025-11-24-granular-sharing-permissions-are-now-available-with-two-tiered-control-separatin\|🔐 Granular sharing permissions are now available with two-tiered control separating…]] | <span class="not-archived">not archived</span> | archive begins <time datetime="2025-12-19">2025-12-19</time> | · | <span class="not-archived">not archived</span> | · | · | · | · | · | · | <span class="not-archived">not archived</span> | · | archive begins <time datetime="2025-10-01">2025-10-01</time> |
| 2025 Q3 | · | · | · | archive begins <time datetime="2025-08-01">2025-08-01</time> | <span class="not-archived">not archived</span> | · | · | · | · | · | · | · | · | · | archive begins <time datetime="2025-09-26">2025-09-26</time> | <span class="not-archived">not archived</span> | · | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | · | · | · | <span class="not-archived">not archived</span> | · | · | · | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | · | <span class="not-archived">not archived</span> | · | · | · | · | · | · | <span class="not-archived">not archived</span> | archive begins <time datetime="2025-09-30">2025-09-30</time> | <span class="not-archived">not archived</span> |
| 2025 Q2 | · | · | · | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | · | archive begins <time datetime="2025-06-30">2025-06-30</time> | · | · | · | · | · | · | archive begins <time datetime="2025-06-28">2025-06-28</time> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | · | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | · | · | <time datetime="2025-06-20">2025-06-20</time> [[Changes/Manus/2025-06-20-open-the-browser-in-a-session-log-in-manually-once-we-encrypt-save-your-login-st\|Introducing Manus Cloud Browser]] | <span class="not-archived">not archived</span> | · | · | · | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | · | <span class="not-archived">not archived</span> | · | · | · | · | · | archive begins <time datetime="2025-04-02">2025-04-02</time> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> |
| 2024 Q3 → 2025 Q1 | · | archive begins <time datetime="2024-07-26">2024-07-26</time> | · | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | archive begins <time datetime="2024-07-28">2024-07-28</time> | <span class="not-archived">not archived</span> | · | · | · | · | archive begins <time datetime="2024-10-13">2024-10-13</time> | · | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | · | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | archive begins <time datetime="2024-10-22">2024-10-22</time> | archive begins <time datetime="2024-12-03">2024-12-03</time> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | · | · | · | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | · | <span class="not-archived">not archived</span> | · | archive begins <time datetime="2024-12-13">2024-12-13</time> | · | · | · | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> |
| 2024 Q2 | · | <span class="not-archived">not archived</span> | · | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | · | <time datetime="2024-05-07">2024-05-07</time> [[Changes/Descript/2024-05-07-descript-for-web-now-with-recording-beta\|Descript for Web now with Recording (Beta)]] | archive begins <time datetime="2024-05-13">2024-05-13</time> | · | <span class="not-archived">not archived</span> | · | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | archive begins <time datetime="2024-05-22">2024-05-22</time> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | · | · | · | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | archive begins <time datetime="2024-06-04">2024-06-04</time> | <span class="not-archived">not archived</span> | · | <span class="not-archived">not archived</span> | · | · | · | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> |
| 2021 Q1 → 2024 Q1 | archive begins <time datetime="2023-06-07">2023-06-07</time> | <span class="not-archived">not archived</span> | archive begins <time datetime="2022-12-15">2022-12-15</time> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | archive begins <time datetime="2023-03-14">2023-03-14</time> | · | <span class="not-archived">not archived</span> | archive begins <time datetime="2023-05-15">2023-05-15</time> | <span class="not-archived">not archived</span> | archive begins <time datetime="2023-04-10">2023-04-10</time> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | · | archive begins <time datetime="2023-07-08">2023-07-08</time> | archive begins <time datetime="2024-02-23">2024-02-23</time> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | · | <span class="not-archived">not archived</span> | archive begins <time datetime="2024-01-08">2024-01-08</time> | archive begins <time datetime="2023-08-03">2023-08-03</time> | · | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> |
| 2020 Q4 | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | · | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | · | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <time datetime="2020-12-02">2020-12-02</time> [[Changes/Raycast/2020-12-02-script-commands-improvements\|Script Commands Improvements]] | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | archive begins <time datetime="2020-10-13">2020-10-13</time> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> | <span class="not-archived">not archived</span> |

First in archive: each product's earliest tracked change in this theme. "·" marks a quarter without a key moment, and "not archived" a quarter before the product's archive begins. Archives begin: Aider 2023-06-07 · AnythingLLM 2024-07-26 · ChatGPT 2022-12-15 · Claude 2025-08-01 · Claude Code 2025-12-19 · Cline 2024-07-28 · Codex CLI 2025-06-30 · Cursor 2023-03-14 · Descript 2018-07-07 · Devin 2024-05-13 · Dify 2023-05-15 · ElevenLabs 2024-10-13 · Gemini 2023-04-10 · Gemini CLI 2025-06-28 · GitHub Copilot CLI 2025-09-26 · Google Antigravity 2025-11-18 · Granola 2024-05-22 · HeyGen 2025-11-29 · Kimi Code 2026-05-26 · LM Studio 2024-10-22 · Lovable 2024-12-03 · Manus 2025-05-11 · Microsoft 365 Copilot 2026-01-13 · Notion 2020-01-09 · Ollama 2023-07-08 · Open WebUI 2024-02-23 · OpenClaw 2026-06-30 · OpenCode 2025-12-19 · OpenHands 2024-06-04 · Qoder 2026-08-27 · Raycast 2020-08-03 · Replit 2024-12-13 · Runway 2024-01-08 · Superwhisper 2023-08-03 · Synthesia 2020-10-13 · Windsurf 2025-04-02 · Wispr Flow 2026-03-31 · Z.ai API 2025-09-30 · v0 2025-10-01.
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
<label><input type="radio" name="timeline-product" id="tl-only-2"> AnythingLLM</label>
<label><input type="radio" name="timeline-product" id="tl-only-3"> ChatGPT</label>
<label><input type="radio" name="timeline-product" id="tl-only-4"> Claude</label>
<label><input type="radio" name="timeline-product" id="tl-only-5"> Claude Code</label>
<label><input type="radio" name="timeline-product" id="tl-only-6"> Cline</label>
<label><input type="radio" name="timeline-product" id="tl-only-7"> Codex CLI</label>
<label><input type="radio" name="timeline-product" id="tl-only-8"> Cursor</label>
<label><input type="radio" name="timeline-product" id="tl-only-9"> Descript</label>
<label><input type="radio" name="timeline-product" id="tl-only-10"> Devin</label>
<label><input type="radio" name="timeline-product" id="tl-only-11"> Dify</label>
<label><input type="radio" name="timeline-product" id="tl-only-12"> ElevenLabs</label>
<label><input type="radio" name="timeline-product" id="tl-only-13"> Gemini</label>
<label><input type="radio" name="timeline-product" id="tl-only-14"> Gemini CLI</label>
<label><input type="radio" name="timeline-product" id="tl-only-15"> GitHub Copilot CLI</label>
<label><input type="radio" name="timeline-product" id="tl-only-16"> Google Antigravity</label>
<label><input type="radio" name="timeline-product" id="tl-only-17"> Granola</label>
<label><input type="radio" name="timeline-product" id="tl-only-18"> HeyGen</label>
<label><input type="radio" name="timeline-product" id="tl-only-19"> Kimi Code</label>
<label><input type="radio" name="timeline-product" id="tl-only-20"> LM Studio</label>
<label><input type="radio" name="timeline-product" id="tl-only-21"> Lovable</label>
<label><input type="radio" name="timeline-product" id="tl-only-22"> Manus</label>
<label><input type="radio" name="timeline-product" id="tl-only-23"> Microsoft 365 Copilot</label>
<label><input type="radio" name="timeline-product" id="tl-only-24"> Notion</label>
<label><input type="radio" name="timeline-product" id="tl-only-25"> Ollama</label>
<label><input type="radio" name="timeline-product" id="tl-only-26"> Open WebUI</label>
<label><input type="radio" name="timeline-product" id="tl-only-27"> OpenClaw</label>
<label><input type="radio" name="timeline-product" id="tl-only-28"> OpenCode</label>
<label><input type="radio" name="timeline-product" id="tl-only-29"> OpenHands</label>
<label><input type="radio" name="timeline-product" id="tl-only-30"> Qoder</label>
<label><input type="radio" name="timeline-product" id="tl-only-31"> Raycast</label>
<label><input type="radio" name="timeline-product" id="tl-only-32"> Replit</label>
<label><input type="radio" name="timeline-product" id="tl-only-33"> Runway</label>
<label><input type="radio" name="timeline-product" id="tl-only-34"> Superwhisper</label>
<label><input type="radio" name="timeline-product" id="tl-only-35"> Synthesia</label>
<label><input type="radio" name="timeline-product" id="tl-only-36"> Windsurf</label>
<label><input type="radio" name="timeline-product" id="tl-only-37"> Wispr Flow</label>
<label><input type="radio" name="timeline-product" id="tl-only-38"> Z.ai API</label>
<label><input type="radio" name="timeline-product" id="tl-only-39"> v0</label>
</fieldset>

<details class="disclosure">
<summary>2026 · 666 entries (AnythingLLM 2 · ChatGPT 10 · Claude 1 · Claude Code 149 · Cline 8 · Codex CLI 76 · Cursor 19 · Devin 42 · Dify 16 · ElevenLabs 7 · Gemini 1 · Gemini CLI 26 · GitHub Copilot CLI 64 · Google Antigravity 21 · HeyGen 8 · Kimi Code 18 · LM Studio 3 · Lovable 42 · Microsoft 365 Copilot 3 · Notion 4 · Ollama 3 · Open WebUI 26 · OpenClaw 21 · OpenCode 44 · OpenHands 12 · Qoder 3 · Raycast 11 · Replit 9 · Superwhisper 2 · Synthesia 1 · Windsurf 2 · Wispr Flow 3 · Z.ai API 1 · v0 8)</summary>

**2026-11**

- 2026-11-03 · <span class="tl-product tl-p21">**Lovable**</span> · [[Changes/Lovable/2026-11-03-redesigned-privacy-security-settings|Redesigned Privacy & security settings]] · Launch
- 2026-11-03 · <span class="tl-product tl-p21">**Lovable**</span> · [[Changes/Lovable/2026-11-03-protect-a-project-from-abandonment-cleanup|Protect a project from abandonment cleanup]] · Launch
- 2026-11-02 · <span class="tl-product tl-p21">**Lovable**</span> · [[Changes/Lovable/2026-11-02-redesigned-action-center-reviews|Redesigned Action center reviews]] · Launch
- 2026-11-01 · <span class="tl-product tl-p21">**Lovable**</span> · [[Changes/Lovable/2026-11-01-download-an-sbom-for-your-project|Download an SBOM for your project]] · Launch

**2026-10**

- 2026-10-30 · <span class="tl-product tl-p10">**Devin**</span> · [[Changes/Devin/2026-10-30-pylon-setup-dialog|Pylon Setup Dialog]] · Launch
- 2026-10-30 · <span class="tl-product tl-p10">**Devin**</span> · [[Changes/Devin/2026-10-30-new-security-connections-sonarqube-linear-and-vanta|New Security Connections: SonarQube, Linear and Vanta]] · Launch
- 2026-10-29 · <span class="tl-product tl-p21">**Lovable**</span> · [[Changes/Lovable/2026-10-29-run-a-deep-scan-from-the-project-chat|Run a Deep scan from the project chat]] · Launch
- 2026-10-22 · <span class="tl-product tl-p16">**Google Antigravity**</span> · [[Changes/Google Antigravity/2026-10-22-notifications-settings-docked-question-prompts-and-conversation-palette-filters|Notifications settings, docked question prompts, and conversation palette filters]] · Launch
- 2026-10-22 · <span class="tl-product tl-p21">**Lovable**</span> · [[Changes/Lovable/2026-10-22-clearer-privacy-security-settings|Clearer Privacy & security settings]] · Launch
- 2026-10-22 · <span class="tl-product tl-p28">**OpenCode**</span> · [[Changes/OpenCode/2026-10-22-upgraded-the-bundled-bun-runtime-to-1-4-4|Upgraded the bundled Bun runtime to 1.4.4]] · Launch
- 2026-10-16 · <span class="tl-product tl-p21">**Lovable**</span> · [[Changes/Lovable/2026-10-16-lovable-writes-and-runs-tests-for-the-rules-you-change|Lovable writes and runs tests for the rules you change]] · Launch
- 2026-10-16 · <span class="tl-product tl-p21">**Lovable**</span> · [[Changes/Lovable/2026-10-16-require-approval-or-block-publishing-with-workspace-policies|Require approval or block publishing with workspace policies]] · Launch
- 2026-10-14 · <span class="tl-product tl-p10">**Devin**</span> · [[Changes/Devin/2026-10-14-manage-devin-review-permission|Manage Devin Review Permission]] · Launch
- 2026-10-13 · <span class="tl-product tl-p18">**HeyGen**</span> · [[Changes/HeyGen/2026-10-13-admin-billing-and-security|Admin, billing and security]] · Launch
- 2026-10-13 · <span class="tl-product tl-p18">**HeyGen**</span> · [[Changes/HeyGen/2026-10-13-sso-join-controls|SSO join controls]] · Launch
- 2026-10-09 · <span class="tl-product tl-p10">**Devin**</span> · [[Changes/Devin/2026-10-09-create-scan-and-create-profile-with-devin|Create scan and Create profile with Devin]] · Launch
- 2026-10-09 · <span class="tl-product tl-p10">**Devin**</span> · [[Changes/Devin/2026-10-09-manage-findings-permission|Manage findings permission]] · Launch
- 2026-10-07 · <span class="tl-product tl-p10">**Devin**</span> · [[Changes/Devin/2026-10-07-security-profiles-teams-group-chats|Security Profiles: Teams Group Chats]] · Launch
- 2026-10-07 · <span class="tl-product tl-p10">**Devin**</span> · [[Changes/Devin/2026-10-07-devin-review-permissions|Devin Review Permissions]] · Launch
- 2026-10-06 · <span class="tl-product tl-p21">**Lovable**</span> · [[Changes/Lovable/2026-10-06-connect-your-app-to-klaviyo|Connect your app to Klaviyo]] · Launch
- 2026-10-05 · <span class="tl-product tl-p10">**Devin**</span> · [[Changes/Devin/2026-10-05-repository-access-without-devin-review-permission|Repository Access Without Devin Review Permission]] · Launch
- 2026-10-02 · <span class="tl-product tl-p10">**Devin**</span> · [[Changes/Devin/2026-10-02-select-all-findings-of-a-severity|Select All Findings of a Severity]] · Launch
- 2026-10-02 · <span class="tl-product tl-p37">**Wispr Flow**</span> · [[Changes/Wispr Flow/2026-10-02-for-teams-enterprise-all-platforms|For Teams & Enterprise: (All platforms)]] · Launch
- 2026-10-01 · <span class="tl-product tl-p21">**Lovable**</span> · [[Changes/Lovable/2026-10-01-keep-your-workspace-s-ai-processing-in-the-eu|Keep your workspace's AI processing in the EU]] · Launch

**2026-09**

- 2026-09-30 · <span class="tl-product tl-p10">**Devin**</span> · [[Changes/Devin/2026-09-30-hardware-accelerated-emulators-in-sessions|Hardware-Accelerated Emulators in Sessions]] · Launch
- 2026-09-30 · <span class="tl-product tl-p21">**Lovable**</span> · [[Changes/Lovable/2026-09-30-rotate-your-cloud-database-password-from-chat|Rotate your Cloud database password from chat]] · Launch
- 2026-09-25 · <span class="tl-product tl-p3">**ChatGPT**</span> · [[Changes/ChatGPT/2026-09-25-we-re-introducing-security-history-a-new-way-to-review-recent-security-activity-6f32cc|Security history in ChatGPT]] · Launch
- 2026-09-25 · <span class="tl-product tl-p10">**Devin**</span> · [[Changes/Devin/2026-09-25-github-enterprise-server-role-mirroring-and-team-sync|GitHub Enterprise Server: Role Mirroring and Team Sync]] · Launch
- 2026-09-25 · <span class="tl-product tl-p10">**Devin**</span> · [[Changes/Devin/2026-09-25-runtime-validation-evidence-in-scan-reports|Runtime-Validation Evidence in Scan Reports]] · Launch
- 2026-09-25 · <span class="tl-product tl-p21">**Lovable**</span> · [[Changes/Lovable/2026-09-25-account-settings-have-moved-to-their-own-dialog|Account settings have moved to their own dialog]] · Launch
- 2026-09-25 · <span class="tl-product tl-p32">**Replit**</span> · [[Changes/Replit/2026-09-25-control-access-to-design-systems-and-slide-templates|Control access to design systems and slide templates]] · Launch
- 2026-09-23 · <span class="tl-product tl-p8">**Cursor**</span> · [[Changes/Cursor/2026-09-23-today-we-re-launching-two-cursor-bots-for-the-last-mile-of-shipping-code-rollout-af394f|Cursor launches two Cursor bots for the last mile of shipping code]] · Launch
- 2026-09-23 · <span class="tl-product tl-p8">**Cursor**</span> · [[Changes/Cursor/2026-09-23-security-review|Security Review]] · Launch
- 2026-09-23 · <span class="tl-product tl-p8">**Cursor**</span> · [[Changes/Cursor/2026-09-23-findings|Findings]] · Launch
- 2026-09-23 · <span class="tl-product tl-p10">**Devin**</span> · [[Changes/Devin/2026-09-23-microsoft-teams-without-tenant-wide-admin-consent|Microsoft Teams Without Tenant-Wide Admin Consent]] · Launch
- 2026-09-23 · <span class="tl-product tl-p10">**Devin**</span> · [[Changes/Devin/2026-09-23-security-profiles-for-snapshot-builds|Security Profiles for Snapshot Builds]] · Launch
- 2026-09-23 · <span class="tl-product tl-p10">**Devin**</span> · [[Changes/Devin/2026-09-23-outposts-permissions|Outposts Permissions]] · Launch
- 2026-09-23 · <span class="tl-product tl-p10">**Devin**</span> · [[Changes/Devin/2026-09-23-devin-resumes-right-after-permission-responses|Devin Resumes Right After Permission Responses]] · Launch
- 2026-09-23 · <span class="tl-product tl-p21">**Lovable**</span> · [[Changes/Lovable/2026-09-23-redesigned-project-security-view|Redesigned project Security view]] · Launch
- 2026-09-21 · <span class="tl-product tl-p21">**Lovable**</span> · [[Changes/Lovable/2026-09-21-use-your-connected-tools-from-lovable-in-telegram|Use your connected tools from Lovable in Telegram]] · Launch
- 2026-09-19 · <span class="tl-product tl-p16">**Google Antigravity**</span> · [[Changes/Google Antigravity/2026-09-19-windows-sandbox-support|Windows sandbox support]] · Launch
- 2026-09-18 · <span class="tl-product tl-p10">**Devin**</span> · [[Changes/Devin/2026-09-18-email-notifications-for-enterprise-and-security-profile-organizations|Email Notifications for Enterprise and Security-Profile Organizations]] · Launch
- 2026-09-18 · <span class="tl-product tl-p32">**Replit**</span> · [[Changes/Replit/2026-09-18-investigate-with-expanded-audit-logs|Investigate with expanded audit logs]] · Launch
- 2026-09-16 · <span class="tl-product tl-p10">**Devin**</span> · [[Changes/Devin/2026-09-16-security-bugs-are-always-checked-in-devin-review|Security Bugs Are Always Checked in Devin Review]] · Launch
- 2026-09-10 · <span class="tl-product tl-p36">**Windsurf**</span> · [[Changes/Windsurf/2026-09-10-devin-cloud|Devin Cloud]] · Launch
- 2026-09-04 · <span class="tl-product tl-p18">**HeyGen**</span> · [[Changes/HeyGen/2026-09-04-identity-verification-ui-update|Identity verification UI update]] · Launch

**2026-08**

- 2026-08-28 · <span class="tl-product tl-p10">**Devin**</span> · [[Changes/Devin/2026-08-28-new-org-permission-manage-personal-automations|New Org Permission: Manage Personal Automations]] · Launch
- 2026-08-27 · <span class="tl-product tl-p21">**Lovable**</span> · [[Changes/Lovable/2026-08-27-restrict-external-invites-to-verified-email-domains|Restrict external invites to verified email domains]] · Launch
- 2026-08-26 · <span class="tl-product tl-p10">**Devin**</span> · [[Changes/Devin/2026-08-26-security-section|Security Section]] · Launch
- 2026-08-26 · <span class="tl-product tl-p21">**Lovable**</span> · [[Changes/Lovable/2026-08-26-log-out-everywhere|Log out everywhere]] · Launch
- 2026-08-24 · <span class="tl-product tl-p12">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-08-24-packages|Packages]] · Launch
- 2026-08-21 · <span class="tl-product tl-p10">**Devin**</span> · [[Changes/Devin/2026-08-21-change-a-scan-s-profile|Change a Scan's Profile]] · Launch
- 2026-08-21 · <span class="tl-product tl-p32">**Replit**</span> · [[Changes/Replit/2026-08-21-run-black-box-pen-tests|Run black-box pen tests]] · Launch
- 2026-08-19 · <span class="tl-product tl-p21">**Lovable**</span> · [[Changes/Lovable/2026-08-19-a-simpler-publish-dialog|A simpler Publish dialog]] · Launch
- 2026-08-17 · <span class="tl-product tl-p21">**Lovable**</span> · [[Changes/Lovable/2026-08-17-workspace-insights-is-now-security-insights|Workspace insights is now Security insights]] · Launch
- 2026-08-14 · <span class="tl-product tl-p10">**Devin**</span> · [[Changes/Devin/2026-08-14-unified-workflow-permission-preview|Unified Workflow Permission Preview]] · Launch
- 2026-08-12 · <span class="tl-product tl-p10">**Devin**</span> · [[Changes/Devin/2026-08-12-security-profile-safeguards-in-the-automation-editor|Security Profile Safeguards in the Automation Editor]] · Launch
- 2026-08-11 · <span class="tl-product tl-p21">**Lovable**</span> · [[Changes/Lovable/2026-08-11-limit-on-free-fixes|Limit on free fixes]] · Launch
- 2026-08-10 · <span class="tl-product tl-p21">**Lovable**</span> · [[Changes/Lovable/2026-08-10-security-scan-setting-removed-from-workspace-settings|Security scan setting removed from workspace settings]] · Launch
- 2026-08-07 · <span class="tl-product tl-p10">**Devin**</span> · [[Changes/Devin/2026-08-07-security-profiles|Security Profiles]] · Launch
- 2026-08-07 · <span class="tl-product tl-p18">**HeyGen**</span> · [[Changes/HeyGen/2026-08-07-why-it-matters-c18403|Why it matters]] · Launch
- 2026-08-07 · <span class="tl-product tl-p21">**Lovable**</span> · [[Changes/Lovable/2026-08-07-trust-center-for-your-published-app|Trust Center for your published app]] · Launch
- 2026-08-07 · <span class="tl-product tl-p32">**Replit**</span> · [[Changes/Replit/2026-08-07-security-scan-while-you-build|Security scan while you build]] · Launch

**2026-07**

- 2026-07-29 · <span class="tl-product tl-p21">**Lovable**</span> · [[Changes/Lovable/2026-07-29-fewer-false-alarms-in-dependency-scans|Fewer false alarms in dependency scans]] · Launch
- 2026-07-23 · <span class="tl-product tl-p21">**Lovable**</span> · [[Changes/Lovable/2026-07-23-payments-is-always-visible-in-your-project|Payments is always visible in your project]] · Launch
- 2026-07-17 · <span class="tl-product tl-p11">**Dify**</span> · [[Changes/Dify/2026-07-17-agent-app-enters-open-beta-and-is-now-enabled-by-default-for-all-users-it-introd|Agent App enters open beta and is now enabled by default for all users]] · Change
- 2026-07-16 · <span class="tl-product tl-p21">**Lovable**</span> · [[Changes/Lovable/2026-07-16-choose-which-wiz-policies-run-during-security-scans|Choose which Wiz policies run during security scans]] · Launch
- 2026-07-15 · <span class="tl-product tl-p21">**Lovable**</span> · [[Changes/Lovable/2026-07-15-automatically-delete-abandoned-projects|Automatically delete abandoned projects]] · Launch
- 2026-07-13 · <span class="tl-product tl-p21">**Lovable**</span> · [[Changes/Lovable/2026-07-13-redesigned-settings|Redesigned settings]] · Launch
- 2026-07-08 · <span class="tl-product tl-p18">**HeyGen**</span> · [[Changes/HeyGen/2026-07-08-why-it-matters-d8b8a5|Why it matters]] · Launch
- 2026-07-03 · <span class="tl-product tl-p10">**Devin**</span> · [[Changes/Devin/2026-07-03-security-scan-remediation-api|Security Scan Remediation API]] · Launch
- 2026-07-03 · <span class="tl-product tl-p10">**Devin**</span> · [[Changes/Devin/2026-07-03-blueprint-permission-descriptions|Blueprint Permission Descriptions]] · Launch
- 2026-07-01 · <span class="tl-product tl-p10">**Devin**</span> · [[Changes/Devin/2026-07-01-read-only-scan-profiles|Read-Only Scan Profiles]] · Launch
- 2026-07-01 · <span class="tl-product tl-p10">**Devin**</span> · [[Changes/Devin/2026-07-01-no-access-permission-popover|No-Access Permission Popover]] · Launch
- 2026-07-01 · <span class="tl-product tl-p23">**Microsoft 365 Copilot**</span> · [[Changes/Microsoft 365 Copilot/2026-07-01-edit-capability-for-selecting-permission-reading-option-for-existing-servicenow|Edit capability for selecting permission reading option for existing ServiceNow…]] · Launch

**2026-06**

- 2026-06-29 · <span class="tl-product tl-p21">**Lovable**</span> · [[Changes/Lovable/2026-06-29-set-a-default-data-hosting-region-for-new-projects|Set a default data hosting region for new projects]] · Launch
- 2026-06-24 · <span class="tl-product tl-p10">**Devin**</span> · [[Changes/Devin/2026-06-24-security-findings-in-ask-devin|Security Findings in Ask Devin]] · Launch
- 2026-06-23 · <span class="tl-product tl-p21">**Lovable**</span> · [[Changes/Lovable/2026-06-23-restrict-external-collaborators-without-enforcing-sso|Restrict external collaborators without enforcing SSO]] · Launch
- 2026-06-22 · <span class="tl-product tl-p16">**Google Antigravity**</span> · [[Changes/Google Antigravity/2026-06-22-model-quota-screen-and-agent-security-fixes|Model quota screen and agent security fixes]] · Policy
- 2026-06-17 · <span class="tl-product tl-p10">**Devin**</span> · [[Changes/Devin/2026-06-17-devin-review-security-findings|Devin Review: Security Findings]] · Launch
- 2026-06-12 · <span class="tl-product tl-p32">**Replit**</span> · [[Changes/Replit/2026-06-12-choose-which-production-alerts-reach-your-inbox|Choose which production alerts reach your inbox]] · Launch
- 2026-06-12 · <span class="tl-product tl-p32">**Replit**</span> · [[Changes/Replit/2026-06-12-security|Security]] · Launch
- 2026-06-10 · <span class="tl-product tl-p8">**Cursor**</span> · [[Changes/Cursor/2026-06-10-run-bugbot-before-you-push-3e5964|Run Bugbot before you push]] · Launch
- 2026-06-05 · <span class="tl-product tl-p21">**Lovable**</span> · [[Changes/Lovable/2026-06-05-toggle-whois-privacy-after-purchase|Toggle WHOIS privacy after purchase]] · Launch
- 2026-06-04 · <span class="tl-product tl-p3">**ChatGPT**</span> · [[Changes/ChatGPT/2026-06-04-lockdown-mode-is-now-available-to-all-logged-in-users-across-account-types-and-w|Lockdown Mode is now available to all logged-in users]] · Launch
- 2026-06-04 · <span class="tl-product tl-p8">**Cursor**</span> · [[Changes/Cursor/2026-06-04-custom-tools-056918|Custom tools]] · Launch
- 2026-06-03 · <span class="tl-product tl-p10">**Devin**</span> · [[Changes/Devin/2026-06-03-settings-improvements|Settings Improvements]] · Launch
- 2026-06-01 · <span class="tl-product tl-p21">**Lovable**</span> · [[Changes/Lovable/2026-06-01-automatic-fixes-for-basic-scan-findings|Automatic fixes for Basic scan findings]] · Launch
- 2026-06-01 · <span class="tl-product tl-p21">**Lovable**</span> · [[Changes/Lovable/2026-06-01-security-scan-profiles|Security scan profiles]] · Launch
- 2026-06-01 · <span class="tl-product tl-p21">**Lovable**</span> · [[Changes/Lovable/2026-06-01-scheduled-security-scans-enterprise|Scheduled security scans (Enterprise)]] · Launch

**2026-05**

- 2026-05-27 · <span class="tl-product tl-p21">**Lovable**</span> · [[Changes/Lovable/2026-05-27-sensitive-data-scanning|Sensitive data scanning]] · Launch
- 2026-05-22 · <span class="tl-product tl-p10">**Devin**</span> · [[Changes/Devin/2026-05-22-inline-repo-permission-toggle|Inline Repo Permission Toggle]] · Launch
- 2026-05-21 · <span class="tl-product tl-p4">**Claude**</span> · [[Changes/Claude/2026-05-21-claude-now-works-with-more-security-and-compliance-tools|Claude now works with more security and compliance tools]] · Launch
- 2026-05-18 · <span class="tl-product tl-p21">**Lovable**</span> · [[Changes/Lovable/2026-05-18-wiz-security-scanning|Wiz security scanning]] · Launch
- 2026-05-18 · <span class="tl-product tl-p21">**Lovable**</span> · [[Changes/Lovable/2026-05-18-admin-and-security-updates|Admin and security updates]] · Launch
- 2026-05-17 · <span class="tl-product tl-p10">**Devin**</span> · [[Changes/Devin/2026-05-17-miscellaneous-improvements|Miscellaneous Improvements]] · Launch
- 2026-05-17 · <span class="tl-product tl-p10">**Devin**</span> · [[Changes/Devin/2026-05-17-slack-security-hardening|Slack Security Hardening]] · Launch
- 2026-05-13 · <span class="tl-product tl-p8">**Cursor**</span> · [[Changes/Cursor/2026-05-13-environment-governance-and-security-controls|Environment governance and security controls]] · Launch
- 2026-05-13 · <span class="tl-product tl-p24">**Notion**</span> · [[Changes/Notion/2026-05-13-meet-your-notion-workers|Meet your Notion Workers]] · Launch
- 2026-05-08 · <span class="tl-product tl-p10">**Devin**</span> · [[Changes/Devin/2026-05-08-service-user-permission-management|Service User Permission Management]] · Launch
- 2026-05-08 · <span class="tl-product tl-p32">**Replit**</span> · [[Changes/Replit/2026-05-08-workspace-security-center-2-0|Workspace Security Center 2.0]] · Launch
- 2026-05-01 · <span class="tl-product tl-p10">**Devin**</span> · [[Changes/Devin/2026-05-01-snapshot-revert-for-declarative-setup|Snapshot Revert for Declarative Setup]] · Launch

**2026-04**

- 2026-04-30 · <span class="tl-product tl-p8">**Cursor**</span> · [[Changes/Cursor/2026-04-30-security-reviewer-checks-every-pr-for-security-vulnerabilities-auth-regressions|Security Reviewer]] · Launch
- 2026-04-30 · <span class="tl-product tl-p8">**Cursor**</span> · [[Changes/Cursor/2026-04-30-vulnerability-scanner-b19b70|Vulnerability Scanner]] · Launch
- 2026-04-27 · <span class="tl-product tl-p15">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-04-27-location-based-permission-persistence-is-now-enabled-by-default-so-approvals-car|Location-based permission persistence is now enabled by default, so approvals carry…]] · Change
- 2026-04-24 · <span class="tl-product tl-p21">**Lovable**</span> · [[Changes/Lovable/2026-04-24-security-updates|Security updates]] · Launch
- 2026-04-22 · <span class="tl-product tl-p10">**Devin**</span> · [[Changes/Devin/2026-04-22-view-consumption-permission|View Consumption Permission]] · Launch
- 2026-04-17 · <span class="tl-product tl-p32">**Replit**</span> · [[Changes/Replit/2026-04-17-custom-groups-for-scim-organizations|Custom groups for SCIM organizations]] · Launch
- 2026-04-16 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-04-16-added-less-permission-prompts-skill-scans-transcripts-for-common-read-only-bash|Added /less-permission-prompts skill]] · Change
- 2026-04-14 · <span class="tl-product tl-p24">**Notion**</span> · [[Changes/Notion/2026-04-14-new-database-permission-can-create-pages|New database permission: “Can create pages”]] · Launch
- 2026-04-08 · <span class="tl-product tl-p10">**Devin**</span> · [[Changes/Devin/2026-04-08-us-privacy-controls|US Privacy Controls]] · Launch
- 2026-04-07 · <span class="tl-product tl-p23">**Microsoft 365 Copilot**</span> · [[Changes/Microsoft 365 Copilot/2026-04-07-fewer-confirmation-prompts-for-copilot-actions-web-microsoft-365-copilot-extensi|Fewer confirmation prompts for Copilot actions Web (Microsoft 365 Copilot extensibility)]] · Launch
- 2026-04-02 · <span class="tl-product tl-p21">**Lovable**</span> · [[Changes/Lovable/2026-04-02-security-updates|Security updates]] · Launch
- 2026-04-02 · <span class="tl-product tl-p21">**Lovable**</span> · [[Changes/Lovable/2026-04-02-app-emails|App emails]] · Launch

**2026-03**

- 2026-03-31 · <span class="tl-product tl-p37">**Wispr Flow**</span> · [[Changes/Wispr Flow/2026-03-31-security-privacy-desktop|Security & Privacy (Desktop)]] · Launch
- 2026-03-31 · <span class="tl-product tl-p37">**Wispr Flow**</span> · [[Changes/Wispr Flow/2026-03-31-banking-app-privacy-protection-50-apps-globally-android|Banking App Privacy Protection (50+ Apps Globally) (Android)]] · Launch
- 2026-03-30 · <span class="tl-product tl-p29">**OpenHands**</span> · [[Changes/OpenHands/2026-03-30-added-clear-command-for-v1-conversations-typing-clear-in-the-chat-creates-a-new|Added /clear command for V1 conversations]] · Change
- 2026-03-09 · <span class="tl-product tl-p12">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-03-09-packages|Packages]] · Launch

**2026-02**

- 2026-02-23 · <span class="tl-product tl-p12">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-02-23-workspaces|Workspaces]] · Launch
- 2026-02-23 · <span class="tl-product tl-p21">**Lovable**</span> · [[Changes/Lovable/2026-02-23-guided-publishing-flow|Guided publishing flow]] · Launch
- 2026-02-17 · <span class="tl-product tl-p8">**Cursor**</span> · [[Changes/Cursor/2026-02-17-sandbox-network-access-controls|Sandbox network access controls]] · Launch
- 2026-02-13 · <span class="tl-product tl-p10">**Devin**</span> · [[Changes/Devin/2026-02-13-secure-mode-for-all-organizations|Secure Mode for All Organizations]] · Launch
- 2026-02-02 · <span class="tl-product tl-p12">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-02-02-workspaces|Workspaces]] · Launch

**2026-01**

- 2026-01-26 · <span class="tl-product tl-p12">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-01-26-workspaces|Workspaces]] · Policy
- 2026-01-22 · <span class="tl-product tl-p10">**Devin**</span> · [[Changes/Devin/2026-01-22-devin-review-launch-https-docs-devin-ai-work-with-devin-devin-review-md|Devin Review Launch((source link)]] · Launch
- 2026-01-20 · <span class="tl-product tl-p13">**Gemini**</span> · [[Changes/Gemini/2026-01-20-gemini-introduces-personal-intelligence|Gemini introduces Personal Intelligence]] · Launch
- 2026-01-16 · <span class="tl-product tl-p21">**Lovable**</span> · [[Changes/Lovable/2026-01-16-dependency-vulnerability-scanning-is-now-available-with-issues-in-project-depend|Dependency vulnerability scanning is now available, with issues in project…]] · Launch
- 2026-01-16 · <span class="tl-product tl-p21">**Lovable**</span> · [[Changes/Lovable/2026-01-16-security-center-v0-1|Security center (v0.1)]] · Launch
- 2026-01-16 · <span class="tl-product tl-p32">**Replit**</span> · [[Changes/Replit/2026-01-16-node-js-security-patch|Node.js security patch]] · Launch
- 2026-01-13 · <span class="tl-product tl-p23">**Microsoft 365 Copilot**</span> · [[Changes/Microsoft 365 Copilot/2026-01-13-simplified-servicenow-tickets-setup-with-per-table-acl-rules-web-microsoft-365-c|Simplified ServiceNow tickets setup with per-table ACL rules…]] · Launch

<details class="disclosure">
<summary>Fixes, digests and other changes · 536 (AnythingLLM 2 · ChatGPT 8 · Claude Code 148 · Cline 8 · Codex CLI 76 · Cursor 10 · Devin 2 · Dify 15 · ElevenLabs 2 · Gemini CLI 26 · GitHub Copilot CLI 63 · Google Antigravity 18 · HeyGen 3 · Kimi Code 18 · LM Studio 3 · Lovable 1 · Notion 2 · Ollama 3 · Open WebUI 26 · OpenClaw 21 · OpenCode 43 · OpenHands 11 · Qoder 3 · Raycast 11 · Superwhisper 2 · Synthesia 1 · Windsurf 1 · Z.ai API 1 · v0 8)</summary>

**2026-11**

- 2026-11-06 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2026-11-06-57985-skip-read-only-volume-root-expansion-in-the-mxc-sandbox-iceweasel-oai|♯57985 Skip read-only volume-root expansion in the MXC sandbox @iceweasel-oai]] · Change
- 2026-11-06 · <span class="tl-product tl-p15">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-11-06-34-safety-and-privacy-changes-in-v1-0-106|34 Safety and Privacy changes in v1.0.106]] · Digest
- 2026-11-06 · <span class="tl-product tl-p28">**OpenCode**</span> · [[Changes/OpenCode/2026-11-06-3-safety-and-privacy-changes-in-v2-2-6|3 Safety and Privacy changes in v2.2.6]] · Digest
- 2026-11-05 · <span class="tl-product tl-p27">**OpenClaw**</span> · [[Changes/OpenClaw/2026-11-05-2-safety-and-privacy-changes-in-v2026-11-1|2 Safety and Privacy changes in v2026.11.1]] · Digest
- 2026-11-05 · <span class="tl-product tl-p30">**Qoder**</span> · [[Changes/Qoder/2026-11-05-local-extension-installation-install-plugins-and-skills-by-dragging-or-pasting-f|Local extension installation: Install plugins and Skills by dragging or pasting files]] · Change
- 2026-11-04 · <span class="tl-product tl-p11">**Dify**</span> · [[Changes/Dify/2026-11-04-4-safety-and-privacy-changes-in-1-19-0|4 Safety and Privacy changes in 1.19.0]] · Digest
- 2026-11-04 · <span class="tl-product tl-p14">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-11-04-fix-acp-include-mcp-server-and-tool-metadata-in-permission-requests-by-duvanka-p|fix(acp): include MCP server and tool metadata in permission requests]] · Change
- 2026-11-03 · <span class="tl-product tl-p16">**Google Antigravity**</span> · [[Changes/Google Antigravity/2026-11-03-2-safety-and-privacy-changes-in-hub-v2-29-0-voice-mode-remote|2 Safety and Privacy changes in HUB v2.29.0 — Voice mode, remote…]] · Digest
- 2026-11-03 · <span class="tl-product tl-p26">**Open WebUI**</span> · [[Changes/Open WebUI/2026-11-03-2-safety-and-privacy-changes-in-v0-13-0|2 Safety and Privacy changes in v0.13.0]] · Digest
- 2026-11-03 · <span class="tl-product tl-p27">**OpenClaw**</span> · [[Changes/OpenClaw/2026-11-03-7-safety-and-privacy-changes-in-v2026-10-10|7 Safety and Privacy changes in v2026.10.10]] · Digest
- 2026-11-02 · <span class="tl-product tl-p12">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-11-02-4-safety-and-privacy-changes-in-elevenlabs-updates-2026-11-02|4 Safety and Privacy changes in ElevenLabs updates — 2026-11-02]] · Digest

**2026-10**

- 2026-10-30 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-10-30-10-safety-and-privacy-changes-in-v2-1-314|10 Safety and Privacy changes in v2.1.314]] · Digest
- 2026-10-30 · <span class="tl-product tl-p28">**OpenCode**</span> · [[Changes/OpenCode/2026-10-30-core-preserved-permission-reasons-and-feedback-in-mcp-failures-and-made-code-mod|Core Preserved permission reasons and feedback in MCP failures, and made Code Mode…]] · Change
- 2026-10-29 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2026-10-29-10-safety-and-privacy-changes-in-rust-v0-166-0|10 Safety and Privacy changes in rust-v0.166.0]] · Digest
- 2026-10-29 · <span class="tl-product tl-p26">**Open WebUI**</span> · [[Changes/Open WebUI/2026-10-29-security-advisory-this-release-contains-security-fixes-we-strongly-recommend-upd|🛡️ Security Advisory: This release contains security fixes]] · Change
- 2026-10-29 · <span class="tl-product tl-p27">**OpenClaw**</span> · [[Changes/OpenClaw/2026-10-29-security-release-v2026-10-9-adds-remediations-for-vulnerable-dependencies-and-re|Security release: v2026.10.9 adds remediations for vulnerable dependencies…]] · Change
- 2026-10-28 · <span class="tl-product tl-p3">**ChatGPT**</span> · [[Changes/ChatGPT/2026-10-28-texting-your-dot-is-starting-to-roll-out-in-beta-to-pro-users-in-the-u-s|Texting your dot]] · Change
- 2026-10-28 · <span class="tl-product tl-p16">**Google Antigravity**</span> · [[Changes/Google Antigravity/2026-10-28-the-marketplace-tab-and-the-pages-of-plugins-from-third-party-developers-now-sho|The Marketplace tab and the pages of plugins from third party developers now show…]] · Change
- 2026-10-28 · <span class="tl-product tl-p34">**Superwhisper**</span> · [[Changes/Superwhisper/2026-10-28-2-safety-and-privacy-changes-in-superwhisper-macos-3-1-0|2 Safety and Privacy changes in Superwhisper macOS 3.1.0]] · Digest
- 2026-10-27 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-10-27-changed-claude-code-to-stop-sending-the-claude-code-safety-event-opentelemetry-e|Changed Claude Code to stop sending the claude_code.safety_event OpenTelemetry event]] · Change
- 2026-10-27 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2026-10-27-3-safety-and-privacy-changes-in-rust-v0-165-0|3 Safety and Privacy changes in rust-v0.165.0]] · Digest
- 2026-10-27 · <span class="tl-product tl-p14">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-10-27-fix-ci-remove-unsupported-members-permission-in-unassign-inactive-assignees-work|fix(ci): remove unsupported members permission in unassign-inactive-assignees workflow]] · Change
- 2026-10-27 · <span class="tl-product tl-p27">**OpenClaw**</span> · [[Changes/OpenClaw/2026-10-27-2-safety-and-privacy-changes-in-v2026-10-8|2 Safety and Privacy changes in v2026.10.8]] · Digest
- 2026-10-27 · <span class="tl-product tl-p28">**OpenCode**</span> · [[Changes/OpenCode/2026-10-27-2-safety-and-privacy-changes-in-v2-2-0|2 Safety and Privacy changes in v2.2.0]] · Digest
- 2026-10-27 · <span class="tl-product tl-p29">**OpenHands**</span> · [[Changes/OpenHands/2026-10-27-feat-sidebar-start-a-new-conversation-in-the-row-s-sandbox-ohe-3689-by-hieptl-in|feat(sidebar): start a new conversation in the row's sandbox (OHE-3689)]] · Change
- 2026-10-26 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-10-26-changed-startup-warnings-about-permission-rules-in-settings-files-to-show-once-p|Changed startup warnings about permission rules in settings files to show once per…]] · Change
- 2026-10-26 · <span class="tl-product tl-p6">**Cline**</span> · [[Changes/Cline/2026-10-26-starting-or-resuming-a-cloud-sandbox-shows-a-progress-card-with-the-repo-branch|Starting or resuming a cloud sandbox shows a progress card with the repo, branch…]] · Change
- 2026-10-26 · <span class="tl-product tl-p12">**ElevenLabs**</span> · [[Changes/ElevenLabs/2026-10-26-voice-cloning-permissions-members-without-the-create-instant-voice-clone-or-crea|Voice cloning permissions]] · Change
- 2026-10-26 · <span class="tl-product tl-p19">**Kimi Code**</span> · [[Changes/Kimi Code/2026-10-26-merge-the-two-repeated-permission-mode-notice-lines-in-the-swarm-and-goal-start|Merge the two repeated permission-mode notice lines in the swarm and goal start…]] · Change
- 2026-10-26 · <span class="tl-product tl-p34">**Superwhisper**</span> · [[Changes/Superwhisper/2026-10-26-security-fixes|Security fixes]] · Change
- 2026-10-25 · <span class="tl-product tl-p26">**Open WebUI**</span> · [[Changes/Open WebUI/2026-10-25-10-safety-and-privacy-changes-in-v0-12-4|10 Safety and Privacy changes in v0.12.4]] · Digest
- 2026-10-23 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-10-23-4-safety-and-privacy-changes-in-v2-1-310|4 Safety and Privacy changes in v2.1.310]] · Digest
- 2026-10-23 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2026-10-23-15-safety-and-privacy-changes-in-rust-v0-164-0|15 Safety and Privacy changes in rust-v0.164.0]] · Digest
- 2026-10-23 · <span class="tl-product tl-p11">**Dify**</span> · [[Changes/Dify/2026-10-23-11-safety-and-privacy-changes-in-1-18-0|11 Safety and Privacy changes in 1.18.0]] · Digest
- 2026-10-23 · <span class="tl-product tl-p19">**Kimi Code**</span> · [[Changes/Kimi Code/2026-10-23-fix-workspace-trust-failures-when-git-bash-is-unavailable-on-windows|Fix workspace trust failures when Git Bash is unavailable on Windows]] · Change
- 2026-10-23 · <span class="tl-product tl-p36">**Windsurf**</span> · [[Changes/Windsurf/2026-10-23-electron-42-11-16-and-node-js-24-22-1-for-the-remote-server-with-the-october-202|Electron 42.11.16 and Node.js 24.22.1 for the remote server, with the October 2026…]] · Change
- 2026-10-22 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-10-22-8-safety-and-privacy-changes-in-v2-1-309|8 Safety and Privacy changes in v2.1.309]] · Digest
- 2026-10-22 · <span class="tl-product tl-p15">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-10-22-3-safety-and-privacy-changes-in-v1-0-103|3 Safety and Privacy changes in v1.0.103]] · Digest
- 2026-10-22 · <span class="tl-product tl-p16">**Google Antigravity**</span> · [[Changes/Google Antigravity/2026-10-22-question-prompts-and-permission-requests-now-dock-above-the-message-box-instead|Question prompts and permission requests now dock above the message box instead…]] · Change
- 2026-10-22 · <span class="tl-product tl-p27">**OpenClaw**</span> · [[Changes/OpenClaw/2026-10-22-security-release-v2026-10-6-adds-remediations-for-the-emudhra-certificate-compro|Security release: v2026.10.6 adds remediations for the eMudhra certificate compromise]] · Change
- 2026-10-22 · <span class="tl-product tl-p30">**Qoder**</span> · [[Changes/Qoder/2026-10-22-dynamic-island-macos-view-task-progress-answer-questions-and-handle-permission-r|Dynamic Island (macOS)]] · Change
- 2026-10-21 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-10-21-added-the-claude-code-safety-event-opentelemetry-event-for-each-tool-call-a-perm|Added the claude_code.safety_event OpenTelemetry event for each tool call…]] · Change
- 2026-10-21 · <span class="tl-product tl-p15">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-10-21-subagents-honor-custom-and-mcp-tool-approvals-avoiding-duplicate-permission-prom|Subagents honor custom and MCP tool approvals, avoiding duplicate permission prompts…]] · Change
- 2026-10-20 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-10-20-3-safety-and-privacy-changes-in-v2-1-305|3 Safety and Privacy changes in v2.1.305]] · Digest
- 2026-10-20 · <span class="tl-product tl-p15">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-10-20-permission-approval-prompts-explain-escalation-causes-and-show-a-request-specifi|Permission approval prompts explain escalation causes and show a request-specific…]] · Change
- 2026-10-19 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-10-19-added-decider-person-to-a-mod-s-tool-check-answer-only-the-permission-dialog-or|Added decider: "person" to a mod's tool.check answer: only the permission dialog…]] · Change
- 2026-10-19 · <span class="tl-product tl-p15">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-10-19-6-safety-and-privacy-changes-in-v1-0-100|6 Safety and Privacy changes in v1.0.100]] · Digest
- 2026-10-19 · <span class="tl-product tl-p29">**OpenHands**</span> · [[Changes/OpenHands/2026-10-19-fix-theme-make-consent-backend-scope-readable-by-enyst-in-https-github-com-openh|fix(theme): make consent backend scope readable]] · Change
- 2026-10-16 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-10-16-2-safety-and-privacy-changes-in-v2-1-302|2 Safety and Privacy changes in v2.1.302]] · Digest
- 2026-10-16 · <span class="tl-product tl-p6">**Cline**</span> · [[Changes/Cline/2026-10-16-cline-cloud-sessions-rolling-out-gradually-run-a-task-in-a-hosted-sandbox-on-a-g|Cline Cloud sessions, rolling out gradually]] · Change
- 2026-10-16 · <span class="tl-product tl-p26">**Open WebUI**</span> · [[Changes/Open WebUI/2026-10-16-2-safety-and-privacy-changes-in-v0-12-3|2 Safety and Privacy changes in v0.12.3]] · Digest
- 2026-10-16 · <span class="tl-product tl-p27">**OpenClaw**</span> · [[Changes/OpenClaw/2026-10-16-2-safety-and-privacy-changes-in-v2026-10-4|2 Safety and Privacy changes in v2026.10.4]] · Digest
- 2026-10-15 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-10-15-5-safety-and-privacy-changes-in-v2-1-301|5 Safety and Privacy changes in v2.1.301]] · Digest
- 2026-10-15 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2026-10-15-18-safety-and-privacy-changes-in-rust-v0-163-0|18 Safety and Privacy changes in rust-v0.163.0]] · Digest
- 2026-10-15 · <span class="tl-product tl-p16">**Google Antigravity**</span> · [[Changes/Google Antigravity/2026-10-15-the-review-permissions-dialog-now-wraps-long-commands-and-paths-so-you-can-read|The Review permissions dialog now wraps long commands and paths, so you can read…]] · Change
- 2026-10-14 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-10-14-2-safety-and-privacy-changes-in-v2-1-300|2 Safety and Privacy changes in v2.1.300]] · Digest
- 2026-10-14 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-10-14-6-safety-and-privacy-changes-in-v2-1-299|6 Safety and Privacy changes in v2.1.299]] · Digest
- 2026-10-14 · <span class="tl-product tl-p15">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-10-14-resuming-a-session-now-respects-abandoned-pending-permission-work-and-continues|Resuming a session now respects abandoned pending-permission work and continues only…]] · Change
- 2026-10-14 · <span class="tl-product tl-p26">**Open WebUI**</span> · [[Changes/Open WebUI/2026-10-14-rich-ui-embed-console-errors-rich-ui-tool-embeds-no-longer-log-a-security-error|🧩 Rich UI embed console errors. Rich UI tool embeds no longer log a security…]] · Change
- 2026-10-13 · <span class="tl-product tl-p8">**Cursor**</span> · [[Changes/Cursor/2026-10-13-origin-now-integrates-with-over-20-apps-for-deployments-ci-code-review-security-99509e|Origin now integrates with over 20 apps for deployments, CI, code review, security…]] · Change
- 2026-10-13 · <span class="tl-product tl-p15">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-10-13-3-safety-and-privacy-changes-in-v1-0-97|3 Safety and Privacy changes in v1.0.97]] · Digest
- 2026-10-13 · <span class="tl-product tl-p27">**OpenClaw**</span> · [[Changes/OpenClaw/2026-10-13-3-safety-and-privacy-changes-in-v2026-10-3|3 Safety and Privacy changes in v2026.10.3]] · Digest
- 2026-10-12 · <span class="tl-product tl-p15">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-10-12-3-safety-and-privacy-changes-in-v1-0-96|3 Safety and Privacy changes in v1.0.96]] · Digest
- 2026-10-12 · <span class="tl-product tl-p16">**Google Antigravity**</span> · [[Changes/Google Antigravity/2026-10-12-permission-prompts-for-commands-that-run-a-program-from-an-installed-plugin-now|Permission prompts for commands that run a program from an installed plugin now show…]] · Change
- 2026-10-12 · <span class="tl-product tl-p25">**Ollama**</span> · [[Changes/Ollama/2026-10-12-updated-readme-and-documentation-with-clearer-privacy-and-cloud-services-wording|Updated README and documentation with clearer privacy and cloud-services wording]] · Change
- 2026-10-12 · <span class="tl-product tl-p27">**OpenClaw**</span> · [[Changes/OpenClaw/2026-10-12-plugin-approval-waits-affected-plugin-tools-can-wait-for-your-approval-for-the-e|Plugin approval waits]] · Change
- 2026-10-12 · <span class="tl-product tl-p29">**OpenHands**</span> · [[Changes/OpenHands/2026-10-12-fix-telemetry-retry-automation-consent-sync-by-enyst-in-https-github-com-openhan|fix(telemetry): retry automation consent sync]] · Change
- 2026-10-10 · <span class="tl-product tl-p26">**Open WebUI**</span> · [[Changes/Open WebUI/2026-10-10-6-safety-and-privacy-changes-in-v0-12-0|6 Safety and Privacy changes in v0.12.0]] · Digest
- 2026-10-10 · <span class="tl-product tl-p27">**OpenClaw**</span> · [[Changes/OpenClaw/2026-10-10-20-safety-and-privacy-changes-in-v2026-10-1|20 Safety and Privacy changes in v2026.10.1]] · Digest
- 2026-10-09 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-10-09-4-safety-and-privacy-changes-in-v2-1-296|4 Safety and Privacy changes in v2.1.296]] · Digest
- 2026-10-09 · <span class="tl-product tl-p15">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-10-09-copilot-config-supports-sandbox-credential-injecthosts-keys-with-key-completion|copilot config supports sandbox credential injectHosts keys, with key completion…]] · Change
- 2026-10-08 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-10-08-5-safety-and-privacy-changes-in-v2-1-295|5 Safety and Privacy changes in v2.1.295]] · Digest
- 2026-10-08 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2026-10-08-13-safety-and-privacy-changes-in-rust-v0-162-0|13 Safety and Privacy changes in rust-v0.162.0]] · Digest
- 2026-10-08 · <span class="tl-product tl-p15">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-10-08-2-safety-and-privacy-changes-in-v1-0-94|2 Safety and Privacy changes in v1.0.94]] · Digest
- 2026-10-08 · <span class="tl-product tl-p27">**OpenClaw**</span> · [[Changes/OpenClaw/2026-10-08-windows-mxc-sandbox-the-optional-mxc-sandbox-can-start-and-run-tools-on-compatib|Windows MXC sandbox]] · Change
- 2026-10-07 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-10-07-3-safety-and-privacy-changes-in-v2-1-293|3 Safety and Privacy changes in v2.1.293]] · Digest
- 2026-10-07 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2026-10-07-9-safety-and-privacy-changes-in-rust-v0-161-0|9 Safety and Privacy changes in rust-v0.161.0]] · Digest
- 2026-10-07 · <span class="tl-product tl-p15">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-10-07-2-safety-and-privacy-changes-in-v1-0-93|2 Safety and Privacy changes in v1.0.93]] · Digest
- 2026-10-07 · <span class="tl-product tl-p16">**Google Antigravity**</span> · [[Changes/Google Antigravity/2026-10-07-on-macos-if-privacy-settings-block-antigravity-from-reading-a-file-or-folder-you|On macOS, if privacy settings block Antigravity from reading a file or folder you…]] · Change
- 2026-10-06 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-10-06-6-safety-and-privacy-changes-in-v2-1-292|6 Safety and Privacy changes in v2.1.292]] · Digest
- 2026-10-06 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-10-06-fixed-a-regression-in-2-1-290-where-cloud-sessions-could-drop-answers-to-permiss|Fixed a regression in 2.1.290 where cloud sessions could drop answers to permission…]] · Fix
- 2026-10-06 · <span class="tl-product tl-p29">**OpenHands**</span> · [[Changes/OpenHands/2026-10-06-fix-consume-consent-aware-website-posthog-handoff-by-malhotra5-in-https-github-c|fix: consume consent-aware website PostHog handoff]] · Fix
- 2026-10-05 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-10-05-19-safety-and-privacy-changes-in-v2-1-290|19 Safety and Privacy changes in v2.1.290]] · Digest
- 2026-10-05 · <span class="tl-product tl-p15">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-10-05-4-safety-and-privacy-changes-in-v1-0-92|4 Safety and Privacy changes in v1.0.92]] · Digest
- 2026-10-02 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-10-02-6-safety-and-privacy-changes-in-v2-1-288|6 Safety and Privacy changes in v2.1.288]] · Digest
- 2026-10-01 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-10-01-6-safety-and-privacy-changes-in-v2-1-287|6 Safety and Privacy changes in v2.1.287]] · Digest
- 2026-10-01 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2026-10-01-7-safety-and-privacy-changes-in-rust-v0-160-0|7 Safety and Privacy changes in rust-v0.160.0]] · Digest
- 2026-10-01 · <span class="tl-product tl-p15">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-10-01-2-safety-and-privacy-changes-in-v1-0-91|2 Safety and Privacy changes in v1.0.91]] · Digest

**2026-09**

- 2026-09-30 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-09-30-4-safety-and-privacy-changes-in-v2-1-286|4 Safety and Privacy changes in v2.1.286]] · Digest
- 2026-09-30 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2026-09-30-2-safety-and-privacy-changes-in-rust-v0-159-3|2 Safety and Privacy changes in rust-v0.159.3]] · Digest
- 2026-09-30 · <span class="tl-product tl-p15">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-09-30-permission-prompts-remain-answerable-after-resuming-interrupted-sessions|Permission prompts remain answerable after resuming interrupted sessions]] · Change
- 2026-09-30 · <span class="tl-product tl-p27">**OpenClaw**</span> · [[Changes/OpenClaw/2026-09-30-21-safety-and-privacy-changes-in-v2026-9-7|21 Safety and Privacy changes in v2026.9.7]] · Digest
- 2026-09-29 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-09-29-9-safety-and-privacy-changes-in-v2-1-285|9 Safety and Privacy changes in v2.1.285]] · Digest
- 2026-09-29 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2026-09-29-3-safety-and-privacy-changes-in-rust-v0-159-0|3 Safety and Privacy changes in rust-v0.159.0]] · Digest
- 2026-09-28 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-09-28-4-safety-and-privacy-changes-in-v2-1-284|4 Safety and Privacy changes in v2.1.284]] · Digest
- 2026-09-28 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2026-09-28-9-safety-and-privacy-changes-in-rust-v0-158-0|9 Safety and Privacy changes in rust-v0.158.0]] · Digest
- 2026-09-28 · <span class="tl-product tl-p15">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-09-28-2-safety-and-privacy-changes-in-v1-0-89|2 Safety and Privacy changes in v1.0.89]] · Digest
- 2026-09-28 · <span class="tl-product tl-p16">**Google Antigravity**</span> · [[Changes/Google Antigravity/2026-09-28-2-safety-and-privacy-changes-in-hub-v2-18-1-manage-install-plugins|2 Safety and Privacy changes in HUB v2.18.1 — Manage & Install plugins…]] · Digest
- 2026-09-25 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-09-25-3-safety-and-privacy-changes-in-v2-1-283|3 Safety and Privacy changes in v2.1.283]] · Digest
- 2026-09-25 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2026-09-25-2-safety-and-privacy-changes-in-rust-v0-157-0|2 Safety and Privacy changes in rust-v0.157.0]] · Digest
- 2026-09-25 · <span class="tl-product tl-p29">**OpenHands**</span> · [[Changes/OpenHands/2026-09-25-fix-mcp-keep-oauth-credentials-on-cloud-saves-and-skip-consent-when-tokens-still|fix(mcp): keep OAuth credentials on cloud saves and skip consent when tokens still work]] · Change
- 2026-09-24 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-09-24-4-safety-and-privacy-changes-in-v2-1-282|4 Safety and Privacy changes in v2.1.282]] · Digest
- 2026-09-24 · <span class="tl-product tl-p6">**Cline**</span> · [[Changes/Cline/2026-09-24-raised-the-minimum-js-yaml-version-to-4-3-2-to-pick-up-a-security-fix-in-the-par|Raised the minimum js-yaml version to 4.3.2 to pick up a security fix in the parser…]] · Change
- 2026-09-23 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-09-23-12-safety-and-privacy-changes-in-v2-1-281|12 Safety and Privacy changes in v2.1.281]] · Digest
- 2026-09-23 · <span class="tl-product tl-p8">**Cursor**</span> · [[Changes/Cursor/2026-09-23-2-safety-and-privacy-changes-in-rollouts-and-security-review|2 Safety and Privacy changes in Rollouts and Security Review]] · Digest
- 2026-09-23 · <span class="tl-product tl-p19">**Kimi Code**</span> · [[Changes/Kimi Code/2026-09-23-harden-workspace-security-block-file-tools-from-accessing-files-outside-the-work|Harden workspace security]] · Change
- 2026-09-23 · <span class="tl-product tl-p27">**OpenClaw**</span> · [[Changes/OpenClaw/2026-09-23-50-safety-and-privacy-changes-in-v2026-9-6|50 Safety and Privacy changes in v2026.9.6]] · Digest
- 2026-09-22 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-09-22-2-safety-and-privacy-changes-in-v2-1-280|2 Safety and Privacy changes in v2.1.280]] · Digest
- 2026-09-22 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2026-09-22-50-safety-and-privacy-changes-in-rust-v0-156-0|50 Safety and Privacy changes in rust-v0.156.0]] · Digest
- 2026-09-22 · <span class="tl-product tl-p15">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-09-22-2-safety-and-privacy-changes-in-v1-0-88|2 Safety and Privacy changes in v1.0.88]] · Digest
- 2026-09-21 · <span class="tl-product tl-p3">**ChatGPT**</span> · [[Changes/ChatGPT/2026-09-21-privacy-center-is-rolling-out-to-signed-in-chatgpt-free-go-plus-and-pro-users-it-0d2f36|Privacy Center in ChatGPT]] · Change
- 2026-09-21 · <span class="tl-product tl-p15">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-09-21-2-safety-and-privacy-changes-in-v1-0-87|2 Safety and Privacy changes in v1.0.87]] · Digest
- 2026-09-21 · <span class="tl-product tl-p26">**Open WebUI**</span> · [[Changes/Open WebUI/2026-09-21-4-safety-and-privacy-changes-in-v0-11-4|4 Safety and Privacy changes in v0.11.4]] · Digest
- 2026-09-19 · <span class="tl-product tl-p27">**OpenClaw**</span> · [[Changes/OpenClaw/2026-09-19-39-safety-and-privacy-changes-in-v2026-9-5|39 Safety and Privacy changes in v2026.9.5]] · Digest
- 2026-09-18 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-09-18-4-safety-and-privacy-changes-in-v2-1-277|4 Safety and Privacy changes in v2.1.277]] · Digest
- 2026-09-18 · <span class="tl-product tl-p16">**Google Antigravity**</span> · [[Changes/Google Antigravity/2026-09-18-fixed-an-issue-where-permission-settings-accumulated-duplicate-entries-which-mad|Fixed an issue where permission settings accumulated duplicate entries, which made…]] · Fix
- 2026-09-18 · <span class="tl-product tl-p19">**Kimi Code**</span> · [[Changes/Kimi Code/2026-09-18-stop-asking-for-approval-of-bash-commands-that-cannot-be-statically-analyzed-in|Stop asking for approval of bash commands that cannot be statically analyzed in Ask…]] · Change
- 2026-09-17 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-09-17-7-safety-and-privacy-changes-in-v2-1-275|7 Safety and Privacy changes in v2.1.275]] · Digest
- 2026-09-17 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-09-17-3-safety-and-privacy-changes-in-v2-1-274|3 Safety and Privacy changes in v2.1.274]] · Digest
- 2026-09-17 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2026-09-17-7-safety-and-privacy-changes-in-rust-v0-155-0|7 Safety and Privacy changes in rust-v0.155.0]] · Digest
- 2026-09-17 · <span class="tl-product tl-p15">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-09-17-sandbox-policy-now-reports-local-network-access-using-your-configured-setting|/sandbox policy now reports local-network access using your configured setting]] · Change
- 2026-09-16 · <span class="tl-product tl-p15">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-09-16-17-safety-and-privacy-changes-in-v1-0-85|17 Safety and Privacy changes in v1.0.85]] · Digest
- 2026-09-16 · <span class="tl-product tl-p29">**OpenHands**</span> · [[Changes/OpenHands/2026-09-16-test-cover-telemetry-consent-banner-by-aivong-openhands-in-https-github-com-open|test: cover telemetry consent banner]] · Change
- 2026-09-15 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-09-15-5-safety-and-privacy-changes-in-v2-1-273|5 Safety and Privacy changes in v2.1.273]] · Digest
- 2026-09-15 · <span class="tl-product tl-p14">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-09-15-2-safety-and-privacy-changes-in-v0-60-0|2 Safety and Privacy changes in v0.60.0]] · Digest
- 2026-09-14 · <span class="tl-product tl-p3">**ChatGPT**</span> · [[Changes/ChatGPT/2026-09-14-if-you-make-no-changes-to-your-plugins-settings-the-default-permission-setting-i|If you make no changes to your Plugins settings, the default permission setting…]] · Change
- 2026-09-14 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-09-14-7-safety-and-privacy-changes-in-v2-1-271|7 Safety and Privacy changes in v2.1.271]] · Digest
- 2026-09-14 · <span class="tl-product tl-p19">**Kimi Code**</span> · [[Changes/Kimi Code/2026-09-14-add-the-kimi-code-permission-mode-reminder-environment-variable-set-it-to-0-to-s|Add the KIMI_CODE_PERMISSION_MODE_REMINDER environment variable]] · Change
- 2026-09-12 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-09-12-fixed-read-only-git-commands-in-bash-unexpectedly-asking-for-permission-after-a|Fixed read-only git commands in Bash unexpectedly asking for permission after…]] · Fix
- 2026-09-11 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-09-11-5-safety-and-privacy-changes-in-v2-1-269|5 Safety and Privacy changes in v2.1.269]] · Digest
- 2026-09-11 · <span class="tl-product tl-p27">**OpenClaw**</span> · [[Changes/OpenClaw/2026-09-11-12-safety-and-privacy-changes-in-v2026-9-4|12 Safety and Privacy changes in v2026.9.4]] · Digest
- 2026-09-11 · <span class="tl-product tl-p31">**Raycast**</span> · [[Changes/Raycast/2026-09-11-ai-tool-confirmations-now-default-to-auto-so-sessions-no-longer-ask-for-permissi|AI : Tool confirmations now default to Auto, so sessions no longer ask…]] · Change
- 2026-09-11 · <span class="tl-product tl-p31">**Raycast**</span> · [[Changes/Raycast/2026-09-11-ai-tool-confirmations-now-default-to-auto-so-sessions-no-longer-ask-for-permissi-9e970d|AI : Tool confirmations now default to Auto, so sessions no longer ask…]] · Change
- 2026-09-10 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-09-10-8-safety-and-privacy-changes-in-v2-1-268|8 Safety and Privacy changes in v2.1.268]] · Digest
- 2026-09-10 · <span class="tl-product tl-p11">**Dify**</span> · [[Changes/Dify/2026-09-10-16-safety-and-privacy-changes-in-1-17-1|16 Safety and Privacy changes in 1.17.1]] · Digest
- 2026-09-09 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-09-09-2-safety-and-privacy-changes-in-v2-1-267|2 Safety and Privacy changes in v2.1.267]] · Digest
- 2026-09-09 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2026-09-09-25-safety-and-privacy-changes-in-rust-v0-154-0|25 Safety and Privacy changes in rust-v0.154.0]] · Digest
- 2026-09-09 · <span class="tl-product tl-p16">**Google Antigravity**</span> · [[Changes/Google Antigravity/2026-09-09-3-safety-and-privacy-changes-in-hub-v2-13-0-introducing-new-documents|3 Safety and Privacy changes in HUB v2.13.0 — Introducing new Documents…]] · Digest
- 2026-09-08 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-09-08-3-safety-and-privacy-changes-in-v2-1-265|3 Safety and Privacy changes in v2.1.265]] · Digest
- 2026-09-08 · <span class="tl-product tl-p14">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-09-08-fix-core-enforce-fail-closed-workspace-trust-and-filter-mcpservers-in-restricted|fix(core): enforce fail-closed workspace trust and filter mcpServers in restricted mode]] · Change
- 2026-09-08 · <span class="tl-product tl-p27">**OpenClaw**</span> · [[Changes/OpenClaw/2026-09-08-14-safety-and-privacy-changes-in-v2026-9-3|14 Safety and Privacy changes in v2026.9.3]] · Digest
- 2026-09-05 · <span class="tl-product tl-p27">**OpenClaw**</span> · [[Changes/OpenClaw/2026-09-05-24-safety-and-privacy-changes-in-v2026-9-2|24 Safety and Privacy changes in v2026.9.2]] · Digest
- 2026-09-04 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-09-04-4-safety-and-privacy-changes-in-v2-1-261|4 Safety and Privacy changes in v2.1.261]] · Digest
- 2026-09-04 · <span class="tl-product tl-p15">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-09-04-5-safety-and-privacy-changes-in-v1-0-83|5 Safety and Privacy changes in v1.0.83]] · Digest
- 2026-09-04 · <span class="tl-product tl-p19">**Kimi Code**</span> · [[Changes/Kimi Code/2026-09-04-3-safety-and-privacy-changes-in-kimi-code-0-41-0|3 Safety and Privacy changes in Kimi Code 0.41.0]] · Digest
- 2026-09-03 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-09-03-7-safety-and-privacy-changes-in-v2-1-260|7 Safety and Privacy changes in v2.1.260]] · Digest
- 2026-09-03 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2026-09-03-6-safety-and-privacy-changes-in-rust-v0-153-0|6 Safety and Privacy changes in rust-v0.153.0]] · Digest
- 2026-09-03 · <span class="tl-product tl-p27">**OpenClaw**</span> · [[Changes/OpenClaw/2026-09-03-10-safety-and-privacy-changes-in-v2026-9-1|10 Safety and Privacy changes in v2026.9.1]] · Digest
- 2026-09-02 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-09-02-4-safety-and-privacy-changes-in-v2-1-259|4 Safety and Privacy changes in v2.1.259]] · Digest
- 2026-09-02 · <span class="tl-product tl-p16">**Google Antigravity**</span> · [[Changes/Google Antigravity/2026-09-02-permission-prompts-again-describe-the-specific-action-being-requested-instead-of|Permission prompts again describe the specific action being requested instead…]] · Change
- 2026-09-02 · <span class="tl-product tl-p19">**Kimi Code**</span> · [[Changes/Kimi Code/2026-09-02-2-safety-and-privacy-changes-in-kimi-code-0-40-0|2 Safety and Privacy changes in Kimi Code 0.40.0]] · Digest
- 2026-09-01 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-09-01-fixed-remote-and-scheduled-sessions-failing-with-user-messages-must-have-non-emp|Fixed remote and scheduled sessions failing…]] · Fix
- 2026-09-01 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-09-01-10-safety-and-privacy-changes-in-v2-1-257|10 Safety and Privacy changes in v2.1.257]] · Digest
- 2026-09-01 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2026-09-01-41227-use-compatible-powershell-for-elevated-windows-sandbox-commands-copyberry|♯41227 Use compatible PowerShell for elevated Windows sandbox commands @copyberry]] · Change
- 2026-09-01 · <span class="tl-product tl-p27">**OpenClaw**</span> · [[Changes/OpenClaw/2026-09-01-7-safety-and-privacy-changes-in-v2026-8-2|7 Safety and Privacy changes in v2026.8.2]] · Digest
- 2026-09-01 · <span class="tl-product tl-p28">**OpenCode**</span> · [[Changes/OpenCode/2026-09-01-core-apply-patch-no-longer-emits-an-empty-move-path-in-permission-metadata|Core apply_patch no longer emits an empty move path in permission metadata]] · Change

**2026-08**

- 2026-08-31 · <span class="tl-product tl-p26">**Open WebUI**</span> · [[Changes/Open WebUI/2026-08-31-security-advisory-this-release-includes-security-and-access-control-fixes-we-rec|🛡️ Security Advisory: This release includes security and access-control fixes]] · Change
- 2026-08-31 · <span class="tl-product tl-p27">**OpenClaw**</span> · [[Changes/OpenClaw/2026-08-31-2-safety-and-privacy-changes-in-v2026-8-1|2 Safety and Privacy changes in v2026.8.1]] · Digest
- 2026-08-29 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2026-08-29-5-safety-and-privacy-changes-in-rust-v0-151-0|5 Safety and Privacy changes in rust-v0.151.0]] · Digest
- 2026-08-28 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-08-28-6-safety-and-privacy-changes-in-v2-1-251|6 Safety and Privacy changes in v2.1.251]] · Digest
- 2026-08-28 · <span class="tl-product tl-p19">**Kimi Code**</span> · [[Changes/Kimi Code/2026-08-28-web-fix-switching-the-permission-mode-in-one-session-changing-it-for-every-sessi|web: Fix switching the permission mode in one session changing it for every session]] · Change
- 2026-08-28 · <span class="tl-product tl-p39">**v0**</span> · [[Changes/v0/2026-08-28-2-safety-and-privacy-changes-in-gpt-5-6-sol-sign-in-inside-previews|2 Safety and Privacy changes in GPT-5.6 Sol, sign-in inside previews…]] · Digest
- 2026-08-27 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-08-27-4-safety-and-privacy-changes-in-v2-1-248|4 Safety and Privacy changes in v2.1.248]] · Digest
- 2026-08-27 · <span class="tl-product tl-p15">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-08-27-5-safety-and-privacy-changes-in-v1-0-81|5 Safety and Privacy changes in v1.0.81]] · Digest
- 2026-08-27 · <span class="tl-product tl-p30">**Qoder**</span> · [[Changes/Qoder/2026-08-27-harness-for-complex-tasks-qoder-s-harness-keeps-planning-execution-verification|Harness for complex tasks]] · Change
- 2026-08-26 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-08-26-2-safety-and-privacy-changes-in-v2-1-247|2 Safety and Privacy changes in v2.1.247]] · Digest
- 2026-08-26 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2026-08-26-12-safety-and-privacy-changes-in-rust-v0-150-0|12 Safety and Privacy changes in rust-v0.150.0]] · Digest
- 2026-08-26 · <span class="tl-product tl-p16">**Google Antigravity**</span> · [[Changes/Google Antigravity/2026-08-26-2-safety-and-privacy-changes-in-hub-v2-11-0-generative-ui-and-ui|2 Safety and Privacy changes in HUB v2.11.0 — Generative UI and UI…]] · Digest
- 2026-08-25 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-08-25-6-safety-and-privacy-changes-in-v2-1-246|6 Safety and Privacy changes in v2.1.246]] · Digest
- 2026-08-25 · <span class="tl-product tl-p11">**Dify**</span> · [[Changes/Dify/2026-08-25-16-safety-and-privacy-changes-in-1-17-0|16 Safety and Privacy changes in 1.17.0]] · Digest
- 2026-08-25 · <span class="tl-product tl-p14">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-08-25-ssr-agent-issue-fix-26120-clarify-privacy-notice-wording-and-selection-options-b|SSR Agent Issue Fix (26120): Clarify privacy notice wording and selection options]] · Change
- 2026-08-25 · <span class="tl-product tl-p26">**Open WebUI**</span> · [[Changes/Open WebUI/2026-08-25-7-safety-and-privacy-changes-in-v0-11-1|7 Safety and Privacy changes in v0.11.1]] · Digest
- 2026-08-21 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-08-21-fixed-fullscreen-mode-answering-a-permission-prompt-or-pressing-a-button-when-yo|Fixed fullscreen mode answering a permission prompt or pressing a button when you…]] · Fix
- 2026-08-21 · <span class="tl-product tl-p28">**OpenCode**</span> · [[Changes/OpenCode/2026-08-21-core-answer-permission-requests-triggered-by-subagents-during-opencode-run|Core Answer permission requests triggered by subagents during opencode run]] · Change
- 2026-08-20 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-08-20-3-safety-and-privacy-changes-in-v2-1-238|3 Safety and Privacy changes in v2.1.238]] · Digest
- 2026-08-20 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2026-08-20-18-safety-and-privacy-changes-in-rust-v0-149-0|18 Safety and Privacy changes in rust-v0.149.0]] · Digest
- 2026-08-19 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-08-19-2-safety-and-privacy-changes-in-v2-1-236|2 Safety and Privacy changes in v2.1.236]] · Digest
- 2026-08-19 · <span class="tl-product tl-p31">**Raycast**</span> · [[Changes/Raycast/2026-08-19-2-safety-and-privacy-changes-in-raycast-macos-0-71|2 Safety and Privacy changes in Raycast macos 0.71]] · Digest
- 2026-08-19 · <span class="tl-product tl-p31">**Raycast**</span> · [[Changes/Raycast/2026-08-19-ai-fixed-answering-a-tool-permission-prompt-doing-nothing-after-quitting-and-reo|AI : Fixed answering a tool permission prompt doing nothing after quitting…]] · Fix
- 2026-08-18 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-08-18-2-safety-and-privacy-changes-in-v2-1-235|2 Safety and Privacy changes in v2.1.235]] · Digest
- 2026-08-18 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2026-08-18-17-safety-and-privacy-changes-in-rust-v0-148-0|17 Safety and Privacy changes in rust-v0.148.0]] · Digest
- 2026-08-18 · <span class="tl-product tl-p38">**Z.ai API**</span> · [[Changes/Z.ai API/2026-08-18-emergent-cybersecurity-capabilities-glm-5-3-matches-mythos-5-in-white-box-code-r|Emergent Cybersecurity Capabilities]] · Change
- 2026-08-17 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-08-17-8-safety-and-privacy-changes-in-v2-1-234|8 Safety and Privacy changes in v2.1.234]] · Digest
- 2026-08-14 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-08-14-3-safety-and-privacy-changes-in-v2-1-233|3 Safety and Privacy changes in v2.1.233]] · Digest
- 2026-08-14 · <span class="tl-product tl-p6">**Cline**</span> · [[Changes/Cline/2026-08-14-reclaim-idle-plugin-sandbox-processes-instead-of-leaving-them-running-for-the-li|Reclaim idle plugin sandbox processes instead of leaving them running for the life…]] · Change
- 2026-08-13 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-08-13-9-safety-and-privacy-changes-in-v2-1-232|9 Safety and Privacy changes in v2.1.232]] · Digest
- 2026-08-13 · <span class="tl-product tl-p6">**Cline**</span> · [[Changes/Cline/2026-08-13-fix-the-claude-code-provider-being-unusable-for-agentic-work-it-now-runs-its-own|Fix the Claude Code provider being unusable for agentic work]] · Change
- 2026-08-13 · <span class="tl-product tl-p19">**Kimi Code**</span> · [[Changes/Kimi Code/2026-08-13-show-project-mcp-launch-targets-in-the-workspace-trust-prompt-default-to-declini|Show project MCP launch targets in the workspace trust prompt, default to declining…]] · Change
- 2026-08-12 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-08-12-improved-sandbox-ipv6-literals-in-network-domain-lists-are-now-bracketed-1-443-a|Improved sandbox: IPv6 literals in network domain lists are now bracketed…]] · Change
- 2026-08-11 · <span class="tl-product tl-p14">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-08-11-fix-a2a-server-enforce-workspace-trust-and-task-isolation-to-prevent-rce-by-luis|fix(a2a-server): enforce workspace trust and task isolation to prevent RCE]] · Change
- 2026-08-10 · <span class="tl-product tl-p15">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-08-10-11-safety-and-privacy-changes-in-v1-0-79|11 Safety and Privacy changes in v1.0.79]] · Digest
- 2026-08-09 · <span class="tl-product tl-p6">**Cline**</span> · [[Changes/Cline/2026-08-09-never-run-a-foreign-compiled-plugin-sandbox-bootstrap-for-a-source-host|Never run a foreign compiled plugin-sandbox bootstrap for a source host]] · Change
- 2026-08-08 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-08-08-2-safety-and-privacy-changes-in-v2-1-225|2 Safety and Privacy changes in v2.1.225]] · Digest
- 2026-08-07 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-08-07-2-safety-and-privacy-changes-in-v2-1-224|2 Safety and Privacy changes in v2.1.224]] · Digest
- 2026-08-07 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2026-08-07-9-safety-and-privacy-changes-in-rust-v0-147-0|9 Safety and Privacy changes in rust-v0.147.0]] · Digest
- 2026-08-07 · <span class="tl-product tl-p16">**Google Antigravity**</span> · [[Changes/Google Antigravity/2026-08-07-steps-waiting-on-your-input-now-show-the-icon-for-the-tool-involved-including-in|Steps waiting on your input now show the icon for the tool involved, including…]] · Change
- 2026-08-06 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-08-06-3-safety-and-privacy-changes-in-v2-1-223|3 Safety and Privacy changes in v2.1.223]] · Digest
- 2026-08-05 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2026-08-05-apply-safer-automatic-review-defaults-for-cyber-capable-models-and-explain-permi|Apply safer automatic-review defaults for cyber-capable models and explain…]] · Change
- 2026-08-04 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-08-04-improved-auto-mode-safety-messages-sent-to-other-agent-sessions-via-sendmessage|Improved auto mode safety]] · Change
- 2026-08-04 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-08-04-7-safety-and-privacy-changes-in-v2-1-221|7 Safety and Privacy changes in v2.1.221]] · Digest
- 2026-08-03 · <span class="tl-product tl-p15">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-08-03-3-safety-and-privacy-changes-in-v1-0-78|3 Safety and Privacy changes in v1.0.78]] · Digest

**2026-07**

- 2026-07-31 · <span class="tl-product tl-p16">**Google Antigravity**</span> · [[Changes/Google Antigravity/2026-07-31-2-safety-and-privacy-changes-in-hub-v2-5-0-enterprise-sign-in-gemini|2 Safety and Privacy changes in HUB v2.5.0 — Enterprise sign-in: Gemini…]] · Digest
- 2026-07-31 · <span class="tl-product tl-p19">**Kimi Code**</span> · [[Changes/Kimi Code/2026-07-31-web-order-permission-modes-from-safest-to-most-permissive-across-settings-surfac|web: Order permission modes from safest to most permissive across settings surfaces…]] · Change
- 2026-07-30 · <span class="tl-product tl-p15">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-07-30-5-safety-and-privacy-changes-in-v1-0-76|5 Safety and Privacy changes in v1.0.76]] · Digest
- 2026-07-30 · <span class="tl-product tl-p15">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-07-30-2-safety-and-privacy-changes-in-v1-0-77|2 Safety and Privacy changes in v1.0.77]] · Digest
- 2026-07-29 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2026-07-29-6-safety-and-privacy-changes-in-rust-v0-146-0|6 Safety and Privacy changes in rust-v0.146.0]] · Digest
- 2026-07-29 · <span class="tl-product tl-p29">**OpenHands**</span> · [[Changes/OpenHands/2026-07-29-fix-revive-local-telemetry-consent-banner-by-malhotra5-in-https-github-com-openh|fix: Revive local telemetry consent banner]] · Fix
- 2026-07-28 · <span class="tl-product tl-p11">**Dify**</span> · [[Changes/Dify/2026-07-28-11-safety-and-privacy-changes-in-1-16-1|11 Safety and Privacy changes in 1.16.1]] · Digest
- 2026-07-28 · <span class="tl-product tl-p14">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-07-28-fix-a2a-server-enforce-workspace-trust-and-task-isolation-to-prevent-rce-by-luis|fix(a2a-server): enforce workspace trust and task isolation to prevent RCE]] · Change
- 2026-07-28 · <span class="tl-product tl-p16">**Google Antigravity**</span> · [[Changes/Google Antigravity/2026-07-28-3-safety-and-privacy-changes-in-hub-v2-4-3-preview-tabs-mcp|3 Safety and Privacy changes in HUB v2.4.3 — Preview tabs, MCP…]] · Digest
- 2026-07-27 · <span class="tl-product tl-p26">**Open WebUI**</span> · [[Changes/Open WebUI/2026-07-27-13-safety-and-privacy-changes-in-v0-11-0|13 Safety and Privacy changes in v0.11.0]] · Digest
- 2026-07-24 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-07-24-2-safety-and-privacy-changes-in-v2-1-219|2 Safety and Privacy changes in v2.1.219]] · Digest
- 2026-07-23 · <span class="tl-product tl-p3">**ChatGPT**</span> · [[Changes/ChatGPT/2026-07-23-health-is-built-with-layered-privacy-and-security-safeguards-connected-medical-r|Health is built with layered privacy and security safeguards]] · Change
- 2026-07-23 · <span class="tl-product tl-p15">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-07-23-show-a-first-run-splash-to-opt-into-the-default-sandbox|Show a first-run splash to opt into the default sandbox]] · Change
- 2026-07-22 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-07-22-3-safety-and-privacy-changes-in-v2-1-218|3 Safety and Privacy changes in v2.1.218]] · Digest
- 2026-07-21 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-07-21-fixed-remote-control-sessions-not-showing-a-pending-permission-prompt-or-dialog|Fixed Remote Control sessions not showing a pending permission prompt or dialog…]] · Fix
- 2026-07-21 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2026-07-21-17-safety-and-privacy-changes-in-rust-v0-145-0|17 Safety and Privacy changes in rust-v0.145.0]] · Digest
- 2026-07-21 · <span class="tl-product tl-p39">**v0**</span> · [[Changes/v0/2026-07-21-typed-prompts-survive-clarifying-questions-permission-approvals-and-queued-submi|Typed prompts survive clarifying questions, permission approvals, and queued…]] · Change
- 2026-07-20 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-07-20-5-safety-and-privacy-changes-in-v2-1-216|5 Safety and Privacy changes in v2.1.216]] · Digest
- 2026-07-20 · <span class="tl-product tl-p15">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-07-20-4-safety-and-privacy-changes-in-v1-0-72|4 Safety and Privacy changes in v1.0.72]] · Digest
- 2026-07-20 · <span class="tl-product tl-p19">**Kimi Code**</span> · [[Changes/Kimi Code/2026-07-20-correct-the-yolo-and-auto-permission-mode-descriptions-yolo-auto-approves-tool-a|Correct the YOLO and Auto permission mode descriptions]] · Change
- 2026-07-20 · <span class="tl-product tl-p19">**Kimi Code**</span> · [[Changes/Kimi Code/2026-07-20-fix-running-subagents-not-observing-permission-mode-switches-made-after-they-sta|Fix running subagents not observing permission mode switches made after they started]] · Change
- 2026-07-20 · <span class="tl-product tl-p31">**Raycast**</span> · [[Changes/Raycast/2026-07-20-dictation-fixed-microphone-permission-issues-when-starting-dictation|Dictation : Fixed microphone permission issues when starting dictation]] · Fix
- 2026-07-18 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-07-18-9-safety-and-privacy-changes-in-v2-1-214|9 Safety and Privacy changes in v2.1.214]] · Digest
- 2026-07-17 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-07-17-3-safety-and-privacy-changes-in-v2-1-212|3 Safety and Privacy changes in v2.1.212]] · Digest
- 2026-07-17 · <span class="tl-product tl-p11">**Dify**</span> · [[Changes/Dify/2026-07-17-20-safety-and-privacy-changes-in-1-16-0|20 Safety and Privacy changes in 1.16.0]] · Digest
- 2026-07-16 · <span class="tl-product tl-p15">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-07-16-2-safety-and-privacy-changes-in-v1-0-71|2 Safety and Privacy changes in v1.0.71]] · Digest
- 2026-07-16 · <span class="tl-product tl-p31">**Raycast**</span> · [[Changes/Raycast/2026-07-16-apple-shortcuts-fixed-running-shortcuts-requiring-already-provided-automation-pe|Apple Shortcuts: Fixed running shortcuts requiring already provided automation permission]] · Fix
- 2026-07-15 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-07-15-2-safety-and-privacy-changes-in-v2-1-211|2 Safety and Privacy changes in v2.1.211]] · Digest
- 2026-07-14 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-07-14-3-safety-and-privacy-changes-in-v2-1-210|3 Safety and Privacy changes in v2.1.210]] · Digest
- 2026-07-14 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-07-14-fixed-multi-second-per-turn-slowdowns-in-sessions-with-many-permission-deny-ask|Fixed multi-second per-turn slowdowns in sessions with many permission deny/ask rules]] · Fix
- 2026-07-14 · <span class="tl-product tl-p19">**Kimi Code**</span> · [[Changes/Kimi Code/2026-07-14-in-auto-permission-mode-plan-exits-are-now-marked-as-auto-approved-instead-of-us|In auto permission mode, plan exits are now marked as auto-approved instead…]] · Change
- 2026-07-14 · <span class="tl-product tl-p28">**OpenCode**</span> · [[Changes/OpenCode/2026-07-14-desktop-kept-permission-auto-accept-state-separate-for-each-server|Desktop Kept permission auto-accept state separate for each server]] · Change
- 2026-07-13 · <span class="tl-product tl-p16">**Google Antigravity**</span> · [[Changes/Google Antigravity/2026-07-13-refined-command-permission-prompting-with-strict-literal-matching-relaxed-redire|Refined command permission prompting with strict literal matching, relaxed…]] · Change
- 2026-07-13 · <span class="tl-product tl-p27">**OpenClaw**</span> · [[Changes/OpenClaw/2026-07-13-59-safety-and-privacy-changes-in-v2026-7-1|59 Safety and Privacy changes in v2026.7.1]] · Digest
- 2026-07-11 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-07-11-2-safety-and-privacy-changes-in-v2-1-207|2 Safety and Privacy changes in v2.1.207]] · Digest
- 2026-07-10 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-07-10-fixed-permission-prompt-tool-pointing-at-an-mcp-server-crashing-with-mcp-tool-no|Fixed --permission-prompt-tool pointing at an MCP server crashing…]] · Fix
- 2026-07-10 · <span class="tl-product tl-p15">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-07-10-5-safety-and-privacy-changes-in-v1-0-70|5 Safety and Privacy changes in v1.0.70]] · Digest
- 2026-07-09 · <span class="tl-product tl-p3">**ChatGPT**</span> · [[Changes/ChatGPT/2026-07-09-on-desktop-work-can-use-local-files-and-desktop-apps-with-your-permission-the-bu-1e4d11|On desktop, Work can use local files and desktop apps with your permission]] · Change
- 2026-07-09 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2026-07-09-4-safety-and-privacy-changes-in-rust-v0-144-0|4 Safety and Privacy changes in rust-v0.144.0]] · Digest
- 2026-07-08 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-07-08-background-task-notifications-now-explicitly-state-that-no-human-input-has-occur|Background task notifications now explicitly state that no human input has occurred…]] · Change
- 2026-07-08 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2026-07-08-13-safety-and-privacy-changes-in-rust-v0-143-0|13 Safety and Privacy changes in rust-v0.143.0]] · Digest
- 2026-07-08 · <span class="tl-product tl-p18">**HeyGen**</span> · [[Changes/HeyGen/2026-07-08-security-login-activity-api-key-creation-email-changes|Security — login activity, API key creation, email changes]] · Change
- 2026-07-07 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-07-07-added-a-grey-badge-to-the-footer-when-in-manual-permission-mode-making-the-activ|Added a grey ⏸ badge to the footer when in manual permission mode, making the active…]] · Change
- 2026-07-07 · <span class="tl-product tl-p15">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-07-07-8-safety-and-privacy-changes-in-v1-0-69|8 Safety and Privacy changes in v1.0.69]] · Digest
- 2026-07-07 · <span class="tl-product tl-p19">**Kimi Code**</span> · [[Changes/Kimi Code/2026-07-07-2-safety-and-privacy-changes-in-kimi-code-0-23-1|2 Safety and Privacy changes in Kimi Code 0.23.1]] · Digest
- 2026-07-07 · <span class="tl-product tl-p39">**v0**</span> · [[Changes/v0/2026-07-07-5-safety-and-privacy-changes-in-grouped-tool-approvals-richer-mcp|5 Safety and Privacy changes in Grouped tool approvals, richer MCP…]] · Digest
- 2026-07-06 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-07-06-fixed-remote-control-sessions-showing-the-wrong-permission-mode-in-the-mobile-an|Fixed /remote-control sessions showing the wrong permission mode in the mobile…]] · Fix
- 2026-07-06 · <span class="tl-product tl-p29">**OpenHands**</span> · [[Changes/OpenHands/2026-07-06-4-safety-and-privacy-changes-in-1-9-0|4 Safety and Privacy changes in 1.9.0]] · Digest
- 2026-07-03 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-07-03-changed-the-default-permission-mode-to-manual-across-the-cli-help-vs-code-and-je|Changed the "default" permission mode to "Manual" across the CLI, --help, VS Code…]] · Change
- 2026-07-01 · <span class="tl-product tl-p15">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-07-01-4-safety-and-privacy-changes-in-v1-0-68|4 Safety and Privacy changes in v1.0.68]] · Digest
- 2026-07-01 · <span class="tl-product tl-p26">**Open WebUI**</span> · [[Changes/Open WebUI/2026-07-01-3-safety-and-privacy-changes-in-v0-10-2|3 Safety and Privacy changes in v0.10.2]] · Digest

**2026-06**

- 2026-06-30 · <span class="tl-product tl-p15">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-06-30-disabling-the-sandbox-for-the-rest-of-the-session-now-takes-effect-immediately-s|Disabling the sandbox for the rest of the session now takes effect immediately…]] · Change
- 2026-06-30 · <span class="tl-product tl-p15">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-06-30-3-safety-and-privacy-changes-in-v1-0-66|3 Safety and Privacy changes in v1.0.66]] · Digest
- 2026-06-30 · <span class="tl-product tl-p27">**OpenClaw**</span> · [[Changes/OpenClaw/2026-06-30-6-safety-and-privacy-changes-in-v2026-6-11|6 Safety and Privacy changes in v2026.6.11]] · Digest
- 2026-06-30 · <span class="tl-product tl-p28">**OpenCode**</span> · [[Changes/OpenCode/2026-06-30-sdk-add-session-permission-request-create-and-fetch-endpoints|SDK Add session permission request create and fetch endpoints]] · Change
- 2026-06-29 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-06-29-security-claude-mcp-list-get-no-longer-spawn-mcp-json-servers-that-a-repo-self-a|Security: claude mcp list/get no longer spawn .mcp.json servers that a repo…]] · Change
- 2026-06-29 · <span class="tl-product tl-p26">**Open WebUI**</span> · [[Changes/Open WebUI/2026-06-29-16-safety-and-privacy-changes-in-v0-10-0|16 Safety and Privacy changes in v0.10.0]] · Digest
- 2026-06-26 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-06-26-fixed-external-plugins-enabled-only-by-project-claude-settings-json-not-requirin|Fixed external plugins enabled only by project .claude/settings.json not requiring…]] · Fix
- 2026-06-26 · <span class="tl-product tl-p19">**Kimi Code**</span> · [[Changes/Kimi Code/2026-06-26-add-a-host-cli-option-so-kimi-web-host-can-expose-the-server-to-the-internet-wit|Add a --host CLI option so kimi web --host can expose the server…]] · Change
- 2026-06-25 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2026-06-25-2-safety-and-privacy-changes-in-rust-v0-142-2|2 Safety and Privacy changes in rust-v0.142.2]] · Digest
- 2026-06-25 · <span class="tl-product tl-p11">**Dify**</span> · [[Changes/Dify/2026-06-25-14-safety-and-privacy-changes-in-1-15-0|14 Safety and Privacy changes in 1.15.0]] · Digest
- 2026-06-25 · <span class="tl-product tl-p16">**Google Antigravity**</span> · [[Changes/Google Antigravity/2026-06-25-3-safety-and-privacy-changes-in-hub-v2-2-1-antigravity-guide-audio|3 Safety and Privacy changes in HUB v2.2.1 — Antigravity Guide, audio…]] · Digest
- 2026-06-24 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-06-24-improved-sandbox-network-permission-dialog-hosts-you-allow-with-yes-are-now-reme|Improved sandbox network permission dialog]] · Change
- 2026-06-24 · <span class="tl-product tl-p15">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-06-24-commands-with-slash-prefixed-string-arguments-e-g-body-azp-run-no-longer-trigger|Commands with slash-prefixed string arguments (e.g. --body "/azp run") no longer…]] · Change
- 2026-06-23 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-06-23-2-safety-and-privacy-changes-in-v2-1-187|2 Safety and Privacy changes in v2.1.187]] · Digest
- 2026-06-23 · <span class="tl-product tl-p15">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-06-23-6-safety-and-privacy-changes-in-v1-0-64|6 Safety and Privacy changes in v1.0.64]] · Digest
- 2026-06-22 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-06-22-2-safety-and-privacy-changes-in-v2-1-186|2 Safety and Privacy changes in v2.1.186]] · Digest
- 2026-06-22 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2026-06-22-12-safety-and-privacy-changes-in-rust-v0-142-0|12 Safety and Privacy changes in rust-v0.142.0]] · Digest
- 2026-06-22 · <span class="tl-product tl-p16">**Google Antigravity**</span> · [[Changes/Google Antigravity/2026-06-22-fixed-agent-permission-issue-fixed-the-bug-where-changes-to-the-agent-security-m|Fixed Agent Permission Issue]] · Fix
- 2026-06-19 · <span class="tl-product tl-p39">**v0**</span> · [[Changes/v0/2026-06-19-responding-to-an-agent-prompt-for-an-environment-variable-permission-question-or|Responding to an agent prompt for an environment variable, permission, question…]] · Change
- 2026-06-18 · <span class="tl-product tl-p3">**ChatGPT**</span> · [[Changes/ChatGPT/2026-06-18-app-permission-controls-you-can-now-choose-when-chatgpt-asks-before-using-connec|App permission controls: You can now choose when ChatGPT asks before using connected apps]] · Change
- 2026-06-18 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2026-06-18-7-safety-and-privacy-changes-in-rust-v0-141-0|7 Safety and Privacy changes in rust-v0.141.0]] · Digest
- 2026-06-18 · <span class="tl-product tl-p31">**Raycast**</span> · [[Changes/Raycast/2026-06-18-apple-shortcuts-fixed-missing-apple-shortcuts-and-improve-fallback-when-shortcut|Apple Shortcuts : Fixed missing Apple Shortcuts and improve fallback when Shortcuts…]] · Fix
- 2026-06-17 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-06-17-added-sandbox-allowappleevents-opt-in-setting-that-lets-sandboxed-commands-send|Added sandbox.allowAppleEvents opt-in setting that lets sandboxed commands send…]] · Change
- 2026-06-15 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-06-15-2-safety-and-privacy-changes-in-v2-1-178|2 Safety and Privacy changes in v2.1.178]] · Digest
- 2026-06-15 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2026-06-15-27490-remove-tui-legacy-windows-sandbox-dependency-etraut-openai|♯27490 Remove TUI legacy Windows sandbox dependency @etraut-openai]] · Change
- 2026-06-13 · <span class="tl-product tl-p15">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-06-13-2-safety-and-privacy-changes-in-v1-0-62|2 Safety and Privacy changes in v1.0.62]] · Digest
- 2026-06-12 · <span class="tl-product tl-p31">**Raycast**</span> · [[Changes/Raycast/2026-06-12-ai-tool-call-permission-description-is-parsed-as-markdown-allowing-for-richer-co|AI : Tool call permission description is parsed as Markdown, allowing for richer content]] · Change
- 2026-06-12 · <span class="tl-product tl-p31">**Raycast**</span> · [[Changes/Raycast/2026-06-12-ai-tool-call-permission-description-is-parsed-as-markdown-allowing-for-richer-co-eb1600|AI : Tool call permission description is parsed as Markdown, allowing for richer content]] · Change
- 2026-06-10 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-06-10-2-safety-and-privacy-changes-in-v2-1-172|2 Safety and Privacy changes in v2.1.172]] · Digest
- 2026-06-10 · <span class="tl-product tl-p29">**OpenHands**</span> · [[Changes/OpenHands/2026-06-10-users-can-select-the-sandbox-grouping-strategy-by-tofarr-in-https-github-com-ope|Users can select the sandbox grouping strategy]] · Change
- 2026-06-09 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2026-06-09-5-safety-and-privacy-changes-in-rust-v0-139-0|5 Safety and Privacy changes in rust-v0.139.0]] · Digest
- 2026-06-09 · <span class="tl-product tl-p15">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-06-09-pasted-images-no-longer-leak-into-the-main-prompt-after-a-permission-dialog-clos|Pasted images no longer leak into the main prompt after a permission dialog closes]] · Change
- 2026-06-09 · <span class="tl-product tl-p19">**Kimi Code**</span> · [[Changes/Kimi Code/2026-06-09-fix-acp-slash-skill-routing-bootstrap-context-reads-file-and-permission-edge-cas|Fix ACP slash skill routing, bootstrap context reads, file and permission edge…]] · Change
- 2026-06-08 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-06-08-2-safety-and-privacy-changes-in-v2-1-169|2 Safety and Privacy changes in v2.1.169]] · Digest
- 2026-06-08 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2026-06-08-6-safety-and-privacy-changes-in-rust-v0-138-0|6 Safety and Privacy changes in rust-v0.138.0]] · Digest
- 2026-06-08 · <span class="tl-product tl-p20">**LM Studio**</span> · [[Changes/LM Studio/2026-06-08-security-hardening|Security hardening]] · Change
- 2026-06-06 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-06-06-hardened-cross-session-messaging-messages-relayed-via-sendmessage-from-other-cla|Hardened cross-session messaging]] · Change
- 2026-06-05 · <span class="tl-product tl-p15">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-06-05-2-safety-and-privacy-changes-in-v1-0-60|2 Safety and Privacy changes in v1.0.60]] · Digest
- 2026-06-05 · <span class="tl-product tl-p28">**OpenCode**</span> · [[Changes/OpenCode/2026-06-05-2-safety-and-privacy-changes-in-v1-16-2|2 Safety and Privacy changes in v1.16.2]] · Digest
- 2026-06-04 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-06-04-fixed-org-managed-permission-rules-not-applying-for-the-entire-session-when-the|Fixed org-managed permission rules not applying for the entire session…]] · Fix
- 2026-06-04 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2026-06-04-8-safety-and-privacy-changes-in-rust-v0-137-0|8 Safety and Privacy changes in rust-v0.137.0]] · Digest
- 2026-06-03 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-06-03-4-safety-and-privacy-changes-in-v2-1-162|4 Safety and Privacy changes in v2.1.162]] · Digest
- 2026-06-03 · <span class="tl-product tl-p6">**Cline**</span> · [[Changes/Cline/2026-06-03-update-vs-code-extension-dependencies-to-resolve-security-issues-in-xmldom-xmldo|Update VS Code extension dependencies to resolve security issues…]] · Change
- 2026-06-03 · <span class="tl-product tl-p8">**Cursor**</span> · [[Changes/Cursor/2026-06-03-enterprise-customers-can-now-manage-multiple-cursor-teams-from-one-place-with-di|Enterprise customers can now manage multiple Cursor teams from one place…]] · Change
- 2026-06-02 · <span class="tl-product tl-p3">**ChatGPT**</span> · [[Changes/ChatGPT/2026-06-02-we-re-rolling-out-active-sessions-a-new-security-feature-in-chatgpt-that-helps-u-51e977|ChatGPT rolls out Active sessions, a new security feature that helps users review…]] · Change
- 2026-06-02 · <span class="tl-product tl-p18">**HeyGen**</span> · [[Changes/HeyGen/2026-06-02-we-ve-introduced-a-new-workspace-controls-section-for-admins-bringing-workspace|We've introduced a new Workspace Controls section for admins, bringing workspace…]] · Change
- 2026-06-02 · <span class="tl-product tl-p19">**Kimi Code**</span> · [[Changes/Kimi Code/2026-06-02-add-approval-lifecycle-hook-events-for-observing-pending-and-completed-permissio|Add approval lifecycle hook events for observing pending and completed permission prompts]] · Change
- 2026-06-01 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2026-06-01-11-safety-and-privacy-changes-in-rust-v0-136-0|11 Safety and Privacy changes in rust-v0.136.0]] · Digest
- 2026-06-01 · <span class="tl-product tl-p21">**Lovable**</span> · [[Changes/Lovable/2026-06-01-improvements-and-bug-fixes|Improvements and bug fixes]] · Change
- 2026-06-01 · <span class="tl-product tl-p26">**Open WebUI**</span> · [[Changes/Open WebUI/2026-06-01-7-safety-and-privacy-changes-in-v0-9-6|7 Safety and Privacy changes in v0.9.6]] · Digest

**2026-05**

- 2026-05-29 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-05-29-2-safety-and-privacy-changes-in-v2-1-157|2 Safety and Privacy changes in v2.1.157]] · Digest
- 2026-05-29 · <span class="tl-product tl-p20">**LM Studio**</span> · [[Changes/LM Studio/2026-05-29-security-hardening|Security hardening]] · Change
- 2026-05-29 · <span class="tl-product tl-p35">**Synthesia**</span> · [[Changes/Synthesia/2026-05-29-members-on-free-and-restricted-licenses-can-now-edit-scripts-and-add-screen-reco|Let free workspace members help you edit]] · Change
- 2026-05-28 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-05-28-2-safety-and-privacy-changes-in-v2-1-153|2 Safety and Privacy changes in v2.1.153]] · Digest
- 2026-05-28 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2026-05-28-7-safety-and-privacy-changes-in-rust-v0-135-0|7 Safety and Privacy changes in rust-v0.135.0]] · Digest
- 2026-05-28 · <span class="tl-product tl-p19">**Kimi Code**</span> · [[Changes/Kimi Code/2026-05-28-add-auto-slash-command-and-auto-cli-flag-for-auto-permission-mode|Add /auto slash command and --auto CLI flag for auto permission mode]] · Change
- 2026-05-28 · <span class="tl-product tl-p28">**OpenCode**</span> · [[Changes/OpenCode/2026-05-28-core-handled-acp-next-permission-prompts-correctly|Core Handled acp-next permission prompts correctly]] · Change
- 2026-05-27 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-05-27-2-safety-and-privacy-changes-in-v2-1-152|2 Safety and Privacy changes in v2.1.152]] · Digest
- 2026-05-27 · <span class="tl-product tl-p14">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-05-27-4-safety-and-privacy-changes-in-v0-44-0|4 Safety and Privacy changes in v0.44.0]] · Digest
- 2026-05-26 · <span class="tl-product tl-p2">**AnythingLLM**</span> · [[Changes/AnythingLLM/2026-05-26-this-is-we-believe-a-fundamental-shift-in-how-ai-assistants-work-for-the-first-t|This is, we believe, a fundamental shift in how AI assistants work]] · Change
- 2026-05-26 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2026-05-26-7-safety-and-privacy-changes-in-rust-v0-134-0|7 Safety and Privacy changes in rust-v0.134.0]] · Digest
- 2026-05-23 · <span class="tl-product tl-p15">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-05-23-2-safety-and-privacy-changes-in-v1-0-52|2 Safety and Privacy changes in v1.0.52]] · Digest
- 2026-05-22 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-05-22-2-safety-and-privacy-changes-in-v2-1-149|2 Safety and Privacy changes in v2.1.149]] · Digest
- 2026-05-22 · <span class="tl-product tl-p10">**Devin**</span> · [[Changes/Devin/2026-05-22-automation-sessions-now-appear-in-a-dedicated-automations-involving-you-sidebar|Automation sessions now appear in a dedicated "Automations involving you" sidebar…]] · Change
- 2026-05-22 · <span class="tl-product tl-p14">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-05-22-docs-add-vi-mode-shortcuts-and-clarify-mcp-custom-sandbox-setup-by-chrisjcthomas|docs: add vi mode shortcuts and clarify MCP/custom sandbox setup]] · Change
- 2026-05-21 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2026-05-21-17-safety-and-privacy-changes-in-rust-v0-133-0|17 Safety and Privacy changes in rust-v0.133.0]] · Digest
- 2026-05-20 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2026-05-20-5-safety-and-privacy-changes-in-rust-v0-132-0|5 Safety and Privacy changes in rust-v0.132.0]] · Digest
- 2026-05-20 · <span class="tl-product tl-p15">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-05-20-add-security-review-slash-command-to-review-code-changes-for-security-vulnerabil|Add /security-review slash command to review code changes for security…]] · Change
- 2026-05-20 · <span class="tl-product tl-p28">**OpenCode**</span> · [[Changes/OpenCode/2026-05-20-core-invalid-opencode-permission-json-no-longer-crashes-startup|Core Invalid OPENCODE_PERMISSION JSON no longer crashes startup]] · Change
- 2026-05-20 · <span class="tl-product tl-p31">**Raycast**</span> · [[Changes/Raycast/2026-05-20-permissions-fixed-an-issue-where-raycast-would-not-open-system-settings-when-req|Permissions: Fixed an issue where Raycast would not open System Settings…]] · Fix
- 2026-05-19 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-05-19-fixed-a-permission-prompt-bypass-where-bare-variable-assignments-to-non-allowlis|Fixed a permission-prompt bypass where bare variable assignments to non-allowlisted…]] · Fix
- 2026-05-19 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-05-19-fixed-skill-tool-failing-with-permission-error-in-headless-mode-regression-in-v2|Fixed Skill tool failing with permission error in headless mode (regression in v2.1.141)]] · Fix
- 2026-05-19 · <span class="tl-product tl-p11">**Dify**</span> · [[Changes/Dify/2026-05-19-2-safety-and-privacy-changes-in-1-14-2|2 Safety and Privacy changes in 1.14.2]] · Digest
- 2026-05-19 · <span class="tl-product tl-p15">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-05-19-memory-permission-prompts-now-name-who-can-see-a-stored-memory-user-scope-or-the|Memory permission prompts now name who can see a stored memory]] · Change
- 2026-05-19 · <span class="tl-product tl-p31">**Raycast**</span> · [[Changes/Raycast/2026-05-19-permissions-fixed-an-issue-where-raycast-would-not-open-system-settings-when-req|Permissions: Fixed an issue where Raycast would not open System Settings…]] · Fix
- 2026-05-18 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2026-05-18-17-safety-and-privacy-changes-in-rust-v0-131-0|17 Safety and Privacy changes in rust-v0.131.0]] · Digest
- 2026-05-15 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-05-15-3-safety-and-privacy-changes-in-v2-1-143|3 Safety and Privacy changes in v2.1.143]] · Digest
- 2026-05-15 · <span class="tl-product tl-p39">**v0**</span> · [[Changes/v0/2026-05-15-added-docs-for-the-project-sandbox-terminal-commands-and-permission-modes|Added docs for the project sandbox , terminal commands , and permission modes]] · Change
- 2026-05-14 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-05-14-added-new-claude-agents-flags-add-dir-settings-mcp-config-plugin-dir-permission|Added new claude agents flags]] · Change
- 2026-05-13 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-05-13-5-safety-and-privacy-changes-in-v2-1-141|5 Safety and Privacy changes in v2.1.141]] · Digest
- 2026-05-13 · <span class="tl-product tl-p28">**OpenCode**</span> · [[Changes/OpenCode/2026-05-13-core-preserve-layered-permission-rule-order-in-config-merges|Core Preserve layered permission rule order in config merges]] · Change
- 2026-05-12 · <span class="tl-product tl-p11">**Dify**</span> · [[Changes/Dify/2026-05-12-3-safety-and-privacy-changes-in-1-14-1|3 Safety and Privacy changes in 1.14.1]] · Digest
- 2026-05-12 · <span class="tl-product tl-p14">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-05-12-3-safety-and-privacy-changes-in-v0-42-0|3 Safety and Privacy changes in v0.42.0]] · Digest
- 2026-05-12 · <span class="tl-product tl-p39">**v0**</span> · [[Changes/v0/2026-05-12-v0-can-now-run-terminal-commands-in-your-chats-with-a-permission-prompt-before-e|v0 can now run terminal commands in your chats, with a permission prompt before each one]] · Change
- 2026-05-11 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-05-11-fixed-skill-name-permission-rules-the-wildcard-form-now-works-as-a-prefix-match|Fixed Skill(name ) permission rules]] · Fix
- 2026-05-11 · <span class="tl-product tl-p15">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-05-11-sessions-with-extension-permission-prompts-can-be-resumed-without-a-session-file|Sessions with extension permission prompts can be resumed without…]] · Change
- 2026-05-10 · <span class="tl-product tl-p26">**Open WebUI**</span> · [[Changes/Open WebUI/2026-05-10-6-safety-and-privacy-changes-in-v0-9-5|6 Safety and Privacy changes in v0.9.5]] · Digest
- 2026-05-10 · <span class="tl-product tl-p28">**OpenCode**</span> · [[Changes/OpenCode/2026-05-10-core-read-tool-permission-rules-now-match-worktree-relative-paths-so-read-allowl|Core Read tool permission rules now match worktree-relative paths, so read…]] · Change
- 2026-05-09 · <span class="tl-product tl-p26">**Open WebUI**</span> · [[Changes/Open WebUI/2026-05-09-3-safety-and-privacy-changes-in-v0-9-3|3 Safety and Privacy changes in v0.9.3]] · Digest
- 2026-05-09 · <span class="tl-product tl-p28">**OpenCode**</span> · [[Changes/OpenCode/2026-05-09-core-rejected-invalid-permission-and-question-ids-in-the-http-api|Core Rejected invalid permission and question IDs in the HTTP API]] · Change
- 2026-05-08 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-05-08-2-safety-and-privacy-changes-in-v2-1-136|2 Safety and Privacy changes in v2.1.136]] · Digest
- 2026-05-08 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2026-05-08-2-safety-and-privacy-changes-in-rust-v0-130-0|2 Safety and Privacy changes in rust-v0.130.0]] · Digest
- 2026-05-08 · <span class="tl-product tl-p15">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-05-08-pressing-ctrl-c-while-a-permission-prompt-is-pending-no-longer-causes-the-cli-to|Pressing Ctrl+C while a permission prompt is pending no longer causes the CLI to hang]] · Change
- 2026-05-07 · <span class="tl-product tl-p3">**ChatGPT**</span> · [[Changes/ChatGPT/2026-05-07-over-the-coming-weeks-we-ll-be-rolling-out-trusted-contact-an-optional-safety-fe|Trusted contact in ChatGPT]] · Change
- 2026-05-07 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-05-07-added-sandbox-bwrappath-and-sandbox-socatpath-managed-settings-linux-wsl-to-spec|Added sandbox.bwrapPath and sandbox.socatPath managed settings (Linux/WSL)…]] · Change
- 2026-05-07 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2026-05-07-11-safety-and-privacy-changes-in-rust-v0-129-0|11 Safety and Privacy changes in rust-v0.129.0]] · Digest
- 2026-05-07 · <span class="tl-product tl-p28">**OpenCode**</span> · [[Changes/OpenCode/2026-05-07-desktop-allow-trusted-app-windows-to-write-to-the-clipboard-without-permission-f|Desktop Allow trusted app windows to write to the clipboard without permission failures]] · Change
- 2026-05-06 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-05-06-fixed-permission-mode-flag-being-ignored-when-resuming-a-plan-mode-session-with|Fixed --permission-mode flag being ignored when resuming a plan-mode session…]] · Fix
- 2026-05-06 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-05-06-fixed-session-title-chip-from-rename-disappearing-while-a-permission-or-other-di|Fixed session title chip from /rename disappearing while a permission or other…]] · Fix
- 2026-05-06 · <span class="tl-product tl-p15">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-05-06-protect-against-rce-from-malicious-bare-repositories-nested-inside-a-project-for|Protect against RCE from malicious bare repositories nested inside a project…]] · Change
- 2026-05-05 · <span class="tl-product tl-p14">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-05-05-feat-cli-secure-env-loading-and-enforce-workspace-trust-in-headless-mode-by-ehed|feat(cli): secure .env loading and enforce workspace trust in headless mode]] · Change
- 2026-05-05 · <span class="tl-product tl-p15">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-05-05-memory-tool-confirmation-prompt-now-shows-the-scope-repository-or-user-when-requ|Memory tool confirmation prompt now shows the scope (repository or user)…]] · Change
- 2026-05-04 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-05-04-sdk-hosts-now-receive-a-persistent-localsettings-suggestion-for-bash-permission|SDK hosts now receive a persistent localSettings suggestion for Bash permission…]] · Change
- 2026-05-02 · <span class="tl-product tl-p28">**OpenCode**</span> · [[Changes/OpenCode/2026-05-02-core-agents-can-use-the-global-temp-directory-without-extra-permission-prompts|Core Agents can use the global temp directory without extra permission prompts]] · Change
- 2026-05-01 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-05-01-3-safety-and-privacy-changes-in-v2-1-126|3 Safety and Privacy changes in v2.1.126]] · Digest
- 2026-05-01 · <span class="tl-product tl-p8">**Cursor**</span> · [[Changes/Cursor/2026-05-01-default-off-users-can-discover-and-opt-in|Default Off: users can discover and opt in]] · Change
- 2026-05-01 · <span class="tl-product tl-p29">**OpenHands**</span> · [[Changes/OpenHands/2026-05-01-added-sandbox-kvm-enabled-environment-variable-to-enable-passing-dev-kvm-to-sand|Added SANDBOX_KVM_ENABLED environment variable to enable passing /dev/kvm to sandbox…]] · Change

**2026-04**

- 2026-04-30 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2026-04-30-21-safety-and-privacy-changes-in-rust-v0-128-0|21 Safety and Privacy changes in rust-v0.128.0]] · Digest
- 2026-04-30 · <span class="tl-product tl-p8">**Cursor**</span> · [[Changes/Cursor/2026-04-30-cursor-security-review-is-now-in-beta-on-teams-and-enterprise-plans-you-can-run|Cursor Security Review is now in beta on Teams and Enterprise plans]] · Change
- 2026-04-29 · <span class="tl-product tl-p11">**Dify**</span> · [[Changes/Dify/2026-04-29-7-safety-and-privacy-changes-in-1-14-0|7 Safety and Privacy changes in 1.14.0]] · Digest
- 2026-04-28 · <span class="tl-product tl-p14">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-04-28-feat-sandbox-resolve-custom-seatbelt-profiles-from-home-gemini-first-by-mvanhorn|feat(sandbox): resolve custom seatbelt profiles from $HOME/.gemini first]] · Change
- 2026-04-28 · <span class="tl-product tl-p15">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-04-28-allow-acp-clients-to-toggle-allow-all-permission-mode-via-session-configuration|Allow ACP clients to toggle allow-all permission mode via session configuration]] · Change
- 2026-04-25 · <span class="tl-product tl-p28">**OpenCode**</span> · [[Changes/OpenCode/2026-04-25-core-lsp-permission-prompts-now-include-request-details-like-the-operation-file|Core LSP permission prompts now include request details like the operation, file…]] · Change
- 2026-04-24 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2026-04-24-9-safety-and-privacy-changes-in-rust-v0-125-0|9 Safety and Privacy changes in rust-v0.125.0]] · Digest
- 2026-04-23 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-04-23-fixed-mcp-step-up-authorization-silently-refreshing-instead-of-prompting-for-re|Fixed MCP step-up authorization silently refreshing instead of prompting…]] · Fix
- 2026-04-23 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-04-23-4-safety-and-privacy-changes-in-v2-1-119|4 Safety and Privacy changes in v2.1.119]] · Digest
- 2026-04-23 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2026-04-23-17-safety-and-privacy-changes-in-rust-v0-124-0|17 Safety and Privacy changes in rust-v0.124.0]] · Digest
- 2026-04-23 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2026-04-23-6-safety-and-privacy-changes-in-rust-v0-123-0|6 Safety and Privacy changes in rust-v0.123.0]] · Digest
- 2026-04-23 · <span class="tl-product tl-p14">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-04-23-6-safety-and-privacy-changes-in-v0-39-0|6 Safety and Privacy changes in v0.39.0]] · Digest
- 2026-04-23 · <span class="tl-product tl-p15">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-04-23-permission-prompts-appear-correctly-in-remote-sessions-for-the-cli-tui|Permission prompts appear correctly in remote sessions for the CLI TUI]] · Change
- 2026-04-22 · <span class="tl-product tl-p25">**Ollama**</span> · [[Changes/Ollama/2026-04-22-better-mlx-thread-safety-for-array-management|Better MLX thread safety for array management]] · Change
- 2026-04-21 · <span class="tl-product tl-p26">**Open WebUI**</span> · [[Changes/Open WebUI/2026-04-21-11-safety-and-privacy-changes-in-v0-9-0|11 Safety and Privacy changes in v0.9.0]] · Digest
- 2026-04-21 · <span class="tl-product tl-p28">**OpenCode**</span> · [[Changes/OpenCode/2026-04-21-terminal-fixed-permission-replies-using-remote-workspaces-so-they-are-sent-to-th|Terminal Fixed permission replies using remote workspaces so they are sent…]] · Change
- 2026-04-20 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-04-20-security-sandbox-auto-allow-no-longer-bypasses-the-dangerous-path-safety-check-f|Security: sandbox auto-allow no longer bypasses the dangerous-path safety check…]] · Change
- 2026-04-20 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2026-04-20-9-safety-and-privacy-changes-in-rust-v0-122-0|9 Safety and Privacy changes in rust-v0.122.0]] · Digest
- 2026-04-18 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-04-18-fixed-a-crash-in-the-permission-dialog-when-an-agent-teams-teammate-requested-to|Fixed a crash in the permission dialog when an agent teams teammate requested tool…]] · Fix
- 2026-04-17 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-04-17-6-safety-and-privacy-changes-in-v2-1-113|6 Safety and Privacy changes in v2.1.113]] · Digest
- 2026-04-16 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-04-16-2-safety-and-privacy-changes-in-v2-1-111|2 Safety and Privacy changes in v2.1.111]] · Digest
- 2026-04-16 · <span class="tl-product tl-p15">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-04-16-2-safety-and-privacy-changes-in-v1-0-28|2 Safety and Privacy changes in v1.0.28]] · Digest
- 2026-04-15 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2026-04-15-10-safety-and-privacy-changes-in-rust-v0-121-0|10 Safety and Privacy changes in rust-v0.121.0]] · Digest
- 2026-04-14 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-04-14-2-safety-and-privacy-changes-in-v2-1-108|2 Safety and Privacy changes in v2.1.108]] · Digest
- 2026-04-14 · <span class="tl-product tl-p14">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-04-14-3-safety-and-privacy-changes-in-v0-38-0|3 Safety and Privacy changes in v0.38.0]] · Digest
- 2026-04-14 · <span class="tl-product tl-p15">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-04-14-permission-prompt-notification-hook-only-fires-when-a-prompt-is-actually-shown-t|Permission prompt notification hook only fires when a prompt is actually shown to the user]] · Change
- 2026-04-13 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-04-13-fixed-bash-tool-suggesting-acceptedits-permission-mode-when-exiting-plan-mode-wo|Fixed Bash tool suggesting acceptEdits permission mode when exiting plan mode…]] · Fix
- 2026-04-11 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2026-04-11-4-safety-and-privacy-changes-in-rust-v0-120-0|4 Safety and Privacy changes in rust-v0.120.0]] · Digest
- 2026-04-10 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-04-10-fixed-a-command-injection-vulnerability-in-the-posix-which-fallback-used-by-lsp|Fixed a command injection vulnerability in the POSIX which fallback used by LSP…]] · Fix
- 2026-04-10 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2026-04-10-8-safety-and-privacy-changes-in-rust-v0-119-0|8 Safety and Privacy changes in rust-v0.119.0]] · Digest
- 2026-04-09 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-04-09-7-safety-and-privacy-changes-in-v2-1-98|7 Safety and Privacy changes in v2.1.98]] · Digest
- 2026-04-09 · <span class="tl-product tl-p15">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-04-09-permission-checks-and-other-hooks-now-work-correctly-when-using-anthropic-models|Permission checks and other hooks now work correctly when using Anthropic models…]] · Change
- 2026-04-09 · <span class="tl-product tl-p28">**OpenCode**</span> · [[Changes/OpenCode/2026-04-09-core-add-permission-prompts-for-gitlab-duo-workflow-tool-calls-instead-of-auto-r|Core Add permission prompts for GitLab Duo Workflow tool calls instead…]] · Change
- 2026-04-08 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-04-08-3-safety-and-privacy-changes-in-v2-1-97|3 Safety and Privacy changes in v2.1.97]] · Digest
- 2026-04-08 · <span class="tl-product tl-p14">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-04-08-16-safety-and-privacy-changes-in-v0-37-0|16 Safety and Privacy changes in v0.37.0]] · Digest
- 2026-04-08 · <span class="tl-product tl-p28">**OpenCode**</span> · [[Changes/OpenCode/2026-04-08-terminal-added-opencode-run-dangerously-skip-permissions-to-auto-approve-non-den|Terminal Added opencode run --dangerously-skip-permissions to auto-approve…]] · Change
- 2026-04-07 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-04-07-vscode-added-a-warning-banner-when-settings-json-files-fail-to-parse-so-users-kn|VSCode Added a warning banner when settings.json files fail to parse, so users…]] · Change
- 2026-04-04 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-04-04-linux-sandbox-now-ships-the-apply-seccomp-helper-in-both-npm-and-native-builds-r|Linux sandbox now ships the apply-seccomp helper in both npm and native builds…]] · Change
- 2026-04-04 · <span class="tl-product tl-p15">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-04-04-add-notification-hook-event-that-fires-asynchronously-on-shell-completion-permis|Add notification hook event that fires asynchronously on shell completion…]] · Change
- 2026-04-03 · <span class="tl-product tl-p10">**Devin**</span> · [[Changes/Devin/2026-04-03-gitlab-pat-rotation-fix-responsive-mobile-layouts-startup-command-display-improv|GitLab PAT rotation fix, responsive mobile layouts, startup command display…]] · Change
- 2026-04-02 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-04-02-fixed-plan-mode-in-remote-sessions-losing-track-of-the-plan-file-after-a-contain|Fixed plan mode in remote sessions losing track of the plan file after a container…]] · Fix
- 2026-04-02 · <span class="tl-product tl-p15">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-04-02-add-permissionrequest-hook-to-allow-scripts-to-programmatically-approve-or-deny|Add PermissionRequest hook to allow scripts to programmatically approve or deny tool…]] · Change
- 2026-04-01 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-04-01-2-safety-and-privacy-changes-in-v2-1-89|2 Safety and Privacy changes in v2.1.89]] · Digest
- 2026-04-01 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-04-01-4-safety-and-privacy-changes-in-v2-1-90|4 Safety and Privacy changes in v2.1.90]] · Digest
- 2026-04-01 · <span class="tl-product tl-p14">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-04-01-7-safety-and-privacy-changes-in-v0-36-0|7 Safety and Privacy changes in v0.36.0]] · Digest

**2026-03**

- 2026-03-31 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2026-03-31-7-safety-and-privacy-changes-in-rust-v0-118-0|7 Safety and Privacy changes in rust-v0.118.0]] · Digest
- 2026-03-31 · <span class="tl-product tl-p15">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-03-31-2-safety-and-privacy-changes-in-v1-0-14|2 Safety and Privacy changes in v1.0.14]] · Digest
- 2026-03-30 · <span class="tl-product tl-p15">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-03-30-mcp-servers-using-microsoft-entra-id-authentication-no-longer-show-the-consent-s|MCP servers using Microsoft Entra ID authentication no longer show the consent…]] · Change
- 2026-03-27 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-03-27-fixed-official-marketplace-plugin-scripts-failing-with-permission-denied-on-maco|Fixed official marketplace plugin scripts failing…]] · Fix
- 2026-03-27 · <span class="tl-product tl-p11">**Dify**</span> · [[Changes/Dify/2026-03-27-6-safety-and-privacy-changes-in-1-13-3|6 Safety and Privacy changes in 1.13.3]] · Digest
- 2026-03-27 · <span class="tl-product tl-p26">**Open WebUI**</span> · [[Changes/Open WebUI/2026-03-27-terminal-server-connection-security-terminal-server-verification-and-policy-savi|🔒 Terminal server connection security. Terminal server verification and policy…]] · Change
- 2026-03-26 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-03-26-fixed-the-allow-claude-to-edit-its-own-settings-for-this-session-permission-opti|Fixed the "allow Claude to edit its own settings for this session" permission option…]] · Fix
- 2026-03-26 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-03-26-2-safety-and-privacy-changes-in-v2-1-85|2 Safety and Privacy changes in v2.1.85]] · Digest
- 2026-03-26 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2026-03-26-5-safety-and-privacy-changes-in-rust-v0-117-0|5 Safety and Privacy changes in rust-v0.117.0]] · Digest
- 2026-03-26 · <span class="tl-product tl-p28">**OpenCode**</span> · [[Changes/OpenCode/2026-03-26-core-respect-agent-permission-configuration-for-todowrite-tool|Core Respect agent permission configuration for todowrite tool]] · Change
- 2026-03-25 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-03-25-2-safety-and-privacy-changes-in-v2-1-83|2 Safety and Privacy changes in v2.1.83]] · Digest
- 2026-03-25 · <span class="tl-product tl-p26">**Open WebUI**</span> · [[Changes/Open WebUI/2026-03-25-4-safety-and-privacy-changes-in-v0-8-11|4 Safety and Privacy changes in v0.8.11]] · Digest
- 2026-03-24 · <span class="tl-product tl-p14">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-03-24-5-safety-and-privacy-changes-in-v0-35-0|5 Safety and Privacy changes in v0.35.0]] · Digest
- 2026-03-20 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-03-20-2-safety-and-privacy-changes-in-v2-1-81|2 Safety and Privacy changes in v2.1.81]] · Digest
- 2026-03-19 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2026-03-19-8-safety-and-privacy-changes-in-rust-v0-116-0|8 Safety and Privacy changes in rust-v0.116.0]] · Digest
- 2026-03-18 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-03-18-fixed-custom-status-line-showing-nothing-when-workspace-trust-is-blocking-it|Fixed custom status line showing nothing when workspace trust is blocking it]] · Fix
- 2026-03-17 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-03-17-2-safety-and-privacy-changes-in-v2-1-78|2 Safety and Privacy changes in v2.1.78]] · Digest
- 2026-03-17 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-03-17-3-safety-and-privacy-changes-in-v2-1-77|3 Safety and Privacy changes in v2.1.77]] · Digest
- 2026-03-17 · <span class="tl-product tl-p11">**Dify**</span> · [[Changes/Dify/2026-03-17-3-safety-and-privacy-changes-in-1-13-1|3 Safety and Privacy changes in 1.13.1]] · Digest
- 2026-03-17 · <span class="tl-product tl-p14">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-03-17-3-safety-and-privacy-changes-in-v0-34-0|3 Safety and Privacy changes in v0.34.0]] · Digest
- 2026-03-17 · <span class="tl-product tl-p25">**Ollama**</span> · [[Changes/Ollama/2026-03-17-ci-cd-generate-code-reviews-security-checks-and-other-tasks-within-your-ci|CI/CD: Generate code reviews, security checks, and other tasks within your CI]] · Change
- 2026-03-16 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2026-03-16-9-safety-and-privacy-changes-in-rust-v0-115-0|9 Safety and Privacy changes in rust-v0.115.0]] · Digest
- 2026-03-16 · <span class="tl-product tl-p15">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-03-16-extension-tools-now-work-with-the-permissions-system-use-skippermission-per-tool|Extension tools now work with the permissions system, use skipPermission per-tool…]] · Change
- 2026-03-16 · <span class="tl-product tl-p28">**OpenCode**</span> · [[Changes/OpenCode/2026-03-16-core-delete-legacy-permission-module|Core Delete legacy permission module]] · Change
- 2026-03-14 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-03-14-3-safety-and-privacy-changes-in-v2-1-76|3 Safety and Privacy changes in v2.1.76]] · Digest
- 2026-03-12 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-03-12-fixed-voice-mode-silently-failing-on-the-macos-native-binary-for-users-whose-ter|Fixed voice mode silently failing on the macOS native binary for users whose…]] · Fix
- 2026-03-12 · <span class="tl-product tl-p6">**Cline**</span> · [[Changes/Cline/2026-03-12-markdown-image-loading-now-requires-user-consent|Markdown image loading now requires user consent]] · Change
- 2026-03-12 · <span class="tl-product tl-p24">**Notion**</span> · [[Changes/Notion/2026-03-12-workspace-owners-can-now-set-a-workspace-wide-policy-for-ai-meeting-notes-audio|New consent controls for AI Meeting Notes]] · Change
- 2026-03-12 · <span class="tl-product tl-p28">**OpenCode**</span> · [[Changes/OpenCode/2026-03-12-2-safety-and-privacy-changes-in-v1-2-25|2 Safety and Privacy changes in v1.2.25]] · Digest
- 2026-03-12 · <span class="tl-product tl-p39">**v0**</span> · [[Changes/v0/2026-03-12-improved-snowflake-deployment-error-messages-for-permission-issues|Improved Snowflake deployment error messages for permission issues]] · Change
- 2026-03-11 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-03-11-fixed-freezes-and-100-cpu-loops-triggered-by-permission-prompts-for-complex-bash|Fixed freezes and 100% CPU loops triggered by permission prompts for complex bash commands]] · Fix
- 2026-03-11 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2026-03-11-2-safety-and-privacy-changes-in-rust-v0-114-0|2 Safety and Privacy changes in rust-v0.114.0]] · Digest
- 2026-03-11 · <span class="tl-product tl-p14">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-03-11-refactor-cli-fully-remove-react-anti-patterns-improve-type-safety-and-fix-ux-ove|refactor(cli): fully remove React anti patterns, improve type safety and fix UX…]] · Change
- 2026-03-11 · <span class="tl-product tl-p15">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-03-11-2-safety-and-privacy-changes-in-v1-0-4|2 Safety and Privacy changes in v1.0.4]] · Digest
- 2026-03-10 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-03-10-6-safety-and-privacy-changes-in-v2-1-72|6 Safety and Privacy changes in v2.1.72]] · Digest
- 2026-03-10 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2026-03-10-10-safety-and-privacy-changes-in-rust-v0-113-0|10 Safety and Privacy changes in rust-v0.113.0]] · Digest
- 2026-03-09 · <span class="tl-product tl-p15">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-03-09-reset-allowed-tools-now-fully-undoes-allow-all-and-re-triggers-the-autopilot-per|/reset-allowed-tools now fully undoes /allow-all and re-triggers the autopilot…]] · Change
- 2026-03-08 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2026-03-08-6-safety-and-privacy-changes-in-rust-v0-112-0|6 Safety and Privacy changes in rust-v0.112.0]] · Digest
- 2026-03-08 · <span class="tl-product tl-p26">**Open WebUI**</span> · [[Changes/Open WebUI/2026-03-08-open-terminal-permission-fix-open-terminal-is-now-visible-without-requiring-allo|🖥️ Open Terminal permission fix. Open Terminal is now visible without requiring…]] · Change
- 2026-03-07 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-03-07-fixed-false-positive-permission-prompts-for-compound-bash-commands-containing-he|Fixed false-positive permission prompts for compound bash commands containing…]] · Fix
- 2026-03-07 · <span class="tl-product tl-p28">**OpenCode**</span> · [[Changes/OpenCode/2026-03-07-core-enable-auto-accept-keybind-regardless-of-permission-config|Core Enable auto-accept keybind regardless of permission config]] · Change
- 2026-03-05 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-03-05-5-safety-and-privacy-changes-in-v2-1-69|5 Safety and Privacy changes in v2.1.69]] · Digest
- 2026-03-05 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2026-03-05-4-safety-and-privacy-changes-in-rust-v0-110-0|4 Safety and Privacy changes in rust-v0.110.0]] · Digest
- 2026-03-05 · <span class="tl-product tl-p8">**Cursor**</span> · [[Changes/Cursor/2026-03-05-when-invoked-the-agent-spins-up-a-cloud-sandbox-and-follows-your-instructions-us|When invoked, the agent spins up a cloud sandbox and follows your instructions using…]] · Change
- 2026-03-05 · <span class="tl-product tl-p24">**Notion**</span> · [[Changes/Notion/2026-03-05-the-new-can-create-pages-database-permission-lets-users-create-new-pages-in-a-da|The new “can create pages” database permission lets users create new pages…]] · Change
- 2026-03-03 · <span class="tl-product tl-p8">**Cursor**</span> · [[Changes/Cursor/2026-03-03-fixed-team-permission-and-access-control-inconsistencies-across-organization-set|Fixed team permission and access control inconsistencies across organization setups]] · Fix
- 2026-03-03 · <span class="tl-product tl-p15">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-03-03-autopilot-permission-dialog-appears-on-first-prompt-submission-instead-of-on-mod|Autopilot permission dialog appears on first prompt submission instead of on mode switch]] · Change
- 2026-03-03 · <span class="tl-product tl-p28">**OpenCode**</span> · [[Changes/OpenCode/2026-03-03-2-safety-and-privacy-changes-in-v1-2-16|2 Safety and Privacy changes in v1.2.16]] · Digest
- 2026-03-03 · <span class="tl-product tl-p39">**v0**</span> · [[Changes/v0/2026-03-03-fixed-integration-permission-checks-for-team-roles|Fixed integration permission checks for team roles]] · Fix
- 2026-03-02 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2026-03-02-8-safety-and-privacy-changes-in-rust-v0-107-0|8 Safety and Privacy changes in rust-v0.107.0]] · Digest
- 2026-03-02 · <span class="tl-product tl-p26">**Open WebUI**</span> · [[Changes/Open WebUI/2026-03-02-connection-access-control-privacy-tool-server-and-terminal-connections-without-e|🔒 Connection access control privacy. Tool server and terminal connections…]] · Change
- 2026-03-01 · <span class="tl-product tl-p26">**Open WebUI**</span> · [[Changes/Open WebUI/2026-03-01-4-safety-and-privacy-changes-in-v0-8-6|4 Safety and Privacy changes in v0.8.6]] · Digest

**2026-02**

- 2026-02-28 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-02-28-fixed-listener-leak-in-interactive-permission-handler-during-auto-approvals|Fixed listener leak in interactive permission handler during auto-approvals]] · Fix
- 2026-02-27 · <span class="tl-product tl-p14">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-02-27-6-safety-and-privacy-changes-in-v0-31-0|6 Safety and Privacy changes in v0.31.0]] · Digest
- 2026-02-26 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2026-02-26-12800-fix-enforce-sandbox-envelope-for-zsh-fork-execution-bolinfest|♯12800 fix: enforce sandbox envelope for zsh fork execution @bolinfest]] · Change
- 2026-02-25 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2026-02-25-9-safety-and-privacy-changes-in-rust-v0-105-0|9 Safety and Privacy changes in rust-v0.105.0]] · Digest
- 2026-02-25 · <span class="tl-product tl-p14">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-02-25-refactor-core-adopt-coretoolcallstatus-enum-for-type-safety-by-jerop-in-https-gi|refactor(core): adopt CoreToolCallStatus enum for type safety]] · Change
- 2026-02-24 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-02-24-3-safety-and-privacy-changes-in-v2-1-51|3 Safety and Privacy changes in v2.1.51]] · Digest
- 2026-02-24 · <span class="tl-product tl-p28">**OpenCode**</span> · [[Changes/OpenCode/2026-02-24-core-normalize-paths-at-permission-boundaries-on-windows|Core Normalize paths at permission boundaries on Windows]] · Change
- 2026-02-23 · <span class="tl-product tl-p26">**Open WebUI**</span> · [[Changes/Open WebUI/2026-02-23-backend-config-null-safety-language-detection-during-app-initialization-no-longe|🛡️ Backend config null safety. Language detection during app initialization no…]] · Change
- 2026-02-23 · <span class="tl-product tl-p26">**Open WebUI**</span> · [[Changes/Open WebUI/2026-02-23-3-safety-and-privacy-changes-in-v0-8-4|3 Safety and Privacy changes in v0.8.4]] · Digest
- 2026-02-21 · <span class="tl-product tl-p15">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-02-21-show-permission-elevation-dialog-when-accepting-a-plan-with-autopilot-to-prevent|Show permission elevation dialog when accepting a plan with autopilot to prevent…]] · Change
- 2026-02-19 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-02-19-3-safety-and-privacy-changes-in-v2-1-49|3 Safety and Privacy changes in v2.1.49]] · Digest
- 2026-02-19 · <span class="tl-product tl-p28">**OpenCode**</span> · [[Changes/OpenCode/2026-02-19-4-safety-and-privacy-changes-in-v1-2-7|4 Safety and Privacy changes in v1.2.7]] · Digest
- 2026-02-18 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-02-18-2-safety-and-privacy-changes-in-v2-1-47|2 Safety and Privacy changes in v2.1.47]] · Digest
- 2026-02-18 · <span class="tl-product tl-p8">**Cursor**</span> · [[Changes/Cursor/2026-02-18-7-safety-and-privacy-changes-in-cli-improvements-and-mermaid-ascii|7 Safety and Privacy changes in CLI Improvements and Mermaid ASCII…]] · Digest
- 2026-02-18 · <span class="tl-product tl-p14">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-02-18-5-safety-and-privacy-changes-in-v0-29-0|5 Safety and Privacy changes in v0.29.0]] · Digest
- 2026-02-17 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-02-17-vscode-improved-permission-destination-choice-project-user-session-to-persist-ac|VSCode Improved permission destination choice (project/user/session) to persist…]] · Change
- 2026-02-17 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2026-02-17-9-safety-and-privacy-changes-in-rust-v0-102-0|9 Safety and Privacy changes in rust-v0.102.0]] · Digest
- 2026-02-17 · <span class="tl-product tl-p8">**Cursor**</span> · [[Changes/Cursor/2026-02-17-3-safety-and-privacy-changes-in-2-5|3 Safety and Privacy changes in 2.5]] · Digest
- 2026-02-14 · <span class="tl-product tl-p26">**Open WebUI**</span> · [[Changes/Open WebUI/2026-02-14-public-sharing-security-fix-fixed-a-security-issue-where-users-with-write-access|🛡️ Public sharing security fix. Fixed a security issue where users with write…]] · Change
- 2026-02-13 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-02-13-2-safety-and-privacy-changes-in-v2-1-41|2 Safety and Privacy changes in v2.1.41]] · Digest
- 2026-02-12 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2026-02-12-5-safety-and-privacy-changes-in-rust-v0-100-0|5 Safety and Privacy changes in rust-v0.100.0]] · Digest
- 2026-02-12 · <span class="tl-product tl-p15">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-02-12-permission-prompts-with-long-diffs-are-scrollable-in-alt-screen-mode|Permission prompts with long diffs are scrollable in alt-screen mode]] · Change
- 2026-02-12 · <span class="tl-product tl-p26">**Open WebUI**</span> · [[Changes/Open WebUI/2026-02-12-5-safety-and-privacy-changes-in-v0-8-0|5 Safety and Privacy changes in v0.8.0]] · Digest
- 2026-02-11 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2026-02-11-8-safety-and-privacy-changes-in-rust-v0-99-0|8 Safety and Privacy changes in rust-v0.99.0]] · Digest
- 2026-02-11 · <span class="tl-product tl-p11">**Dify**</span> · [[Changes/Dify/2026-02-11-2-safety-and-privacy-changes-in-1-13-0|2 Safety and Privacy changes in 1.13.0]] · Digest
- 2026-02-10 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-02-10-2-safety-and-privacy-changes-in-v2-1-38|2 Safety and Privacy changes in v2.1.38]] · Digest
- 2026-02-10 · <span class="tl-product tl-p14">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-02-10-3-safety-and-privacy-changes-in-v0-28-0|3 Safety and Privacy changes in v0.28.0]] · Digest
- 2026-02-06 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-02-06-fixed-a-bug-where-commands-excluded-from-sandboxing-via-sandbox-excludedcommands|Fixed a bug where commands excluded from sandboxing…]] · Fix
- 2026-02-05 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2026-02-05-2-safety-and-privacy-changes-in-rust-v0-97-0|2 Safety and Privacy changes in rust-v0.97.0]] · Digest
- 2026-02-05 · <span class="tl-product tl-p15">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-02-05-2-safety-and-privacy-changes-in-v0-0-403|2 Safety and Privacy changes in v0.0.403]] · Digest
- 2026-02-04 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2026-02-04-6-safety-and-privacy-changes-in-rust-v0-95-0|6 Safety and Privacy changes in rust-v0.95.0]] · Digest
- 2026-02-04 · <span class="tl-product tl-p14">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-02-04-security-hooks-wrap-hook-injected-context-in-distinct-xml-tags-by-yunaseoul-in-h|security(hooks): Wrap hook-injected context in distinct XML tags]] · Change
- 2026-02-04 · <span class="tl-product tl-p28">**OpenCode**</span> · [[Changes/OpenCode/2026-02-04-core-improve-skills-system-with-better-prompting-fix-permission-requests-after-s|Core Improve skills system with better prompting, fix permission requests after…]] · Change
- 2026-02-03 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-02-03-fixed-permission-dialogs-stealing-focus-while-actively-typing|Fixed permission dialogs stealing focus while actively typing]] · Fix
- 2026-02-03 · <span class="tl-product tl-p11">**Dify**</span> · [[Changes/Dify/2026-02-03-9-safety-and-privacy-changes-in-1-12-0|9 Safety and Privacy changes in 1.12.0]] · Digest
- 2026-02-02 · <span class="tl-product tl-p29">**OpenHands**</span> · [[Changes/OpenHands/2026-02-02-2-safety-and-privacy-changes-in-1-3-0|2 Safety and Privacy changes in 1.3.0]] · Digest

**2026-01**

- 2026-01-31 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2026-01-31-4-safety-and-privacy-changes-in-rust-v0-93-0|4 Safety and Privacy changes in rust-v0.93.0]] · Digest
- 2026-01-30 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-01-30-permissions-now-respect-content-level-ask-over-tool-level-allow-previously-allow|Permissions now respect content-level ask over tool-level allow]] · Change
- 2026-01-30 · <span class="tl-product tl-p15">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-01-30-acp-server-support-permission-flags-yolo-allow-all-etc-and-permissions-config|ACP server support permission flags: --yolo, --allow-all, etc. and permissions config]] · Change
- 2026-01-29 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-01-29-fixed-per-user-temp-directory-isolation-to-prevent-permission-conflicts-on-share|Fixed per-user temp directory isolation to prevent permission conflicts on shared systems]] · Fix
- 2026-01-29 · <span class="tl-product tl-p28">**OpenCode**</span> · [[Changes/OpenCode/2026-01-29-core-allow-media-src-data-url-for-small-audio-files-in-content-security-policy|Core Allow media-src data: URL for small audio files in Content Security Policy]] · Change
- 2026-01-28 · <span class="tl-product tl-p14">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-01-28-3-safety-and-privacy-changes-in-v0-26-0|3 Safety and Privacy changes in v0.26.0]] · Digest
- 2026-01-28 · <span class="tl-product tl-p20">**LM Studio**</span> · [[Changes/LM Studio/2026-01-28-allow-creating-permission-tokens-without-allowed-mcp-permissions|Allow creating permission tokens without allowed MCP permissions]] · Change
- 2026-01-27 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-01-27-2-safety-and-privacy-changes-in-v2-1-20|2 Safety and Privacy changes in v2.1.20]] · Digest
- 2026-01-27 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2026-01-27-2-safety-and-privacy-changes-in-rust-v0-92-0|2 Safety and Privacy changes in rust-v0.92.0]] · Digest
- 2026-01-25 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2026-01-25-4-safety-and-privacy-changes-in-rust-v0-90-0|4 Safety and Privacy changes in rust-v0.90.0]] · Digest
- 2026-01-25 · <span class="tl-product tl-p28">**OpenCode**</span> · [[Changes/OpenCode/2026-01-25-2-safety-and-privacy-changes-in-v1-1-35|2 Safety and Privacy changes in v1.1.35]] · Digest
- 2026-01-23 · <span class="tl-product tl-p16">**Google Antigravity**</span> · [[Changes/Google Antigravity/2026-01-23-terminal-commands-can-now-be-executed-within-a-sandbox-for-macos-users|Terminal commands can now be executed within a sandbox for MacOS users]] · Change
- 2026-01-23 · <span class="tl-product tl-p28">**OpenCode**</span> · [[Changes/OpenCode/2026-01-23-core-show-file-path-in-apply-patch-request-permission-screen|Core Show file path in apply_patch request permission screen]] · Change
- 2026-01-22 · <span class="tl-product tl-p2">**AnythingLLM**</span> · [[Changes/AnythingLLM/2026-01-22-refactor-managed-services-in-data-handling-privacy-onboarding-step-to-use-their|Refactor Managed Services in "Data Handling & Privacy" Onboarding Step to Use…]] · Change
- 2026-01-22 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2026-01-22-2-safety-and-privacy-changes-in-rust-v0-89-0|2 Safety and Privacy changes in rust-v0.89.0]] · Digest
- 2026-01-22 · <span class="tl-product tl-p8">**Cursor**</span> · [[Changes/Cursor/2026-01-22-unified-cli-permissions-with-the-editor-including-run-everything-auto-run-in-san|Unified CLI permissions with the editor, including Run Everything, Auto-Run…]] · Change
- 2026-01-22 · <span class="tl-product tl-p28">**OpenCode**</span> · [[Changes/OpenCode/2026-01-22-core-ensure-cat-command-triggers-external-directory-permission-check-in-bash-too|Core Ensure cat command triggers external directory permission check in Bash tool]] · Change
- 2026-01-21 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2026-01-21-3-safety-and-privacy-changes-in-rust-v0-88-0|3 Safety and Privacy changes in rust-v0.88.0]] · Digest
- 2026-01-21 · <span class="tl-product tl-p28">**OpenCode**</span> · [[Changes/OpenCode/2026-01-21-core-implement-home-directory-expansion-for-permission-patterns-using-and-home-p|Core Implement home directory expansion for permission patterns using ~ and $HOME prefixes]] · Change
- 2026-01-19 · <span class="tl-product tl-p28">**OpenCode**</span> · [[Changes/OpenCode/2026-01-19-terminal-add-mouse-support-for-permission-buttons-in-tui|Terminal Add mouse support for permission buttons in TUI]] · Change
- 2026-01-15 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2026-01-15-revert-linux-sandboxing-now-falls-back-to-landlock-only-restrictions-when-user-n|revert Linux sandboxing now falls back to Landlock-only restrictions when user…]] · Change
- 2026-01-14 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-01-14-2-safety-and-privacy-changes-in-v2-1-7|2 Safety and Privacy changes in v2.1.7]] · Digest
- 2026-01-14 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2026-01-14-5-safety-and-privacy-changes-in-rust-v0-81-0|5 Safety and Privacy changes in rust-v0.81.0]] · Digest
- 2026-01-14 · <span class="tl-product tl-p14">**Gemini CLI**</span> · [[Changes/Gemini CLI/2026-01-14-7-safety-and-privacy-changes-in-v0-24-0|7 Safety and Privacy changes in v0.24.0]] · Digest
- 2026-01-14 · <span class="tl-product tl-p18">**HeyGen**</span> · [[Changes/HeyGen/2026-01-14-what-s-new-a-new-guided-flow-lets-you-create-your-avatar-with-a-single-15-second|What's new: A new guided flow lets you create your avatar with a single 15-second…]] · Change
- 2026-01-14 · <span class="tl-product tl-p28">**OpenCode**</span> · [[Changes/OpenCode/2026-01-14-terminal-tweak-external-directory-permission-rendering-in-tui|Terminal Tweak external directory permission rendering in TUI]] · Change
- 2026-01-13 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-01-13-fixed-permission-bypass-via-shell-line-continuation-that-could-allow-blocked-com|Fixed permission bypass via shell line continuation that could allow blocked…]] · Fix
- 2026-01-13 · <span class="tl-product tl-p11">**Dify**</span> · [[Changes/Dify/2026-01-13-5-safety-and-privacy-changes-in-1-11-3|5 Safety and Privacy changes in 1.11.3]] · Digest
- 2026-01-13 · <span class="tl-product tl-p15">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2026-01-13-provide-inline-feedback-when-rejecting-tool-permission-requests-so-agents-don-t|Provide inline feedback when rejecting tool permission requests so agents don't have…]] · Change
- 2026-01-13 · <span class="tl-product tl-p28">**OpenCode**</span> · [[Changes/OpenCode/2026-01-13-terminal-add-fullscreen-view-to-permission-prompt|Terminal Add fullscreen view to permission prompt]] · Change
- 2026-01-13 · <span class="tl-product tl-p28">**OpenCode**</span> · [[Changes/OpenCode/2026-01-13-2-safety-and-privacy-changes-in-v1-1-16|2 Safety and Privacy changes in v1.1.16]] · Digest
- 2026-01-12 · <span class="tl-product tl-p28">**OpenCode**</span> · [[Changes/OpenCode/2026-01-12-core-add-password-authentication-and-improve-server-security|Core Add password authentication and improve server security]] · Change
- 2026-01-12 · <span class="tl-product tl-p28">**OpenCode**</span> · [[Changes/OpenCode/2026-01-12-core-check-worktree-for-external-directory-permission-in-subdirectories|Core Check worktree for external_directory permission in subdirectories]] · Change
- 2026-01-09 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-01-09-2-safety-and-privacy-changes-in-v2-1-2|2 Safety and Privacy changes in v2.1.2]] · Digest
- 2026-01-09 · <span class="tl-product tl-p5">**Claude Code**</span> · [[Changes/Claude Code/2026-01-09-2-safety-and-privacy-changes-in-v2-1-3|2 Safety and Privacy changes in v2.1.3]] · Digest
- 2026-01-09 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2026-01-09-2-safety-and-privacy-changes-in-rust-v0-80-0|2 Safety and Privacy changes in rust-v0.80.0]] · Digest
- 2026-01-09 · <span class="tl-product tl-p26">**Open WebUI**</span> · [[Changes/Open WebUI/2026-01-09-6-safety-and-privacy-changes-in-v0-7-0|6 Safety and Privacy changes in v0.7.0]] · Digest
- 2026-01-08 · <span class="tl-product tl-p28">**OpenCode**</span> · [[Changes/OpenCode/2026-01-08-2-safety-and-privacy-changes-in-v1-1-7|2 Safety and Privacy changes in v1.1.7]] · Digest
- 2026-01-07 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2026-01-07-allow-global-exec-flags-model-json-sandbox-toggles-etc-to-be-passed-after-codex|Allow global exec flags (model/json/sandbox toggles, etc.) to be passed after…]] · Change
- 2026-01-07 · <span class="tl-product tl-p28">**OpenCode**</span> · [[Changes/OpenCode/2026-01-07-desktop-permission-auto-accept-should-hide-when-not-needed|Desktop Permission auto-accept should hide when not needed]] · Change
- 2026-01-06 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2026-01-06-3-safety-and-privacy-changes-in-rust-v0-78-0|3 Safety and Privacy changes in rust-v0.78.0]] · Digest
- 2026-01-05 · <span class="tl-product tl-p28">**OpenCode**</span> · [[Changes/OpenCode/2026-01-05-core-fix-permission-evaluation-to-use-rule-based-matching-instead-of-wildcard-pa|Core Fix permission evaluation to use rule-based matching instead of wildcard patterns]] · Change
- 2026-01-05 · <span class="tl-product tl-p28">**OpenCode**</span> · [[Changes/OpenCode/2026-01-05-core-preserve-permission-config-key-order-to-maintain-user-defined-permission-pr|Core Preserve permission config key order to maintain user-defined permission precedence]] · Change
- 2026-01-04 · <span class="tl-product tl-p28">**OpenCode**</span> · [[Changes/OpenCode/2026-01-04-13-safety-and-privacy-changes-in-v1-1-1|13 Safety and Privacy changes in v1.1.1]] · Digest

</details>

</details>

<details class="disclosure">
<summary>2025 · 189 entries (Aider 1 · AnythingLLM 1 · ChatGPT 3 · Claude 1 · Cline 1 · Codex CLI 29 · Cursor 5 · Descript 1 · Devin 3 · Dify 27 · ElevenLabs 5 · Gemini 1 · Gemini CLI 24 · GitHub Copilot CLI 6 · Google Antigravity 2 · Granola 1 · LM Studio 1 · Lovable 9 · Manus 2 · Ollama 2 · Open WebUI 31 · OpenHands 8 · Raycast 4 · Replit 19 · v0 2)</summary>

**2025-12**

- 2025-12-26 · <span class="tl-product tl-p32">**Replit**</span> · [[Changes/Replit/2025-12-26-security-center-for-enterprise|Security Center for Enterprise]] · Expansion
- 2025-12-23 · <span class="tl-product tl-p21">**Lovable**</span> · [[Changes/Lovable/2025-12-23-public-preview-link-controls|Public preview link controls]] · Launch
- 2025-12-08 · <span class="tl-product tl-p16">**Google Antigravity**</span> · [[Changes/Google Antigravity/2025-12-08-secure-mode-and-security-fixes|Secure Mode and Security Fixes]] · Launch

**2025-11**

- 2025-11-26 · <span class="tl-product tl-p21">**Lovable**</span> · [[Changes/Lovable/2025-11-26-private-projects-for-everyone|Private projects for everyone]] · Launch
- 2025-11-24 · <span class="tl-product tl-p26">**Open WebUI**</span> · [[Changes/Open WebUI/2025-11-24-granular-sharing-permissions-are-now-available-with-two-tiered-control-separatin|🔐 Granular sharing permissions are now available with two-tiered control separating…]] · Launch
- 2025-11-24 · <span class="tl-product tl-p26">**Open WebUI**</span> · [[Changes/Open WebUI/2025-11-24-granular-import-and-export-permissions-are-now-available-for-workspace-items-int|🔐 Granular import and export permissions are now available for workspace items…]] · Launch
- 2025-11-21 · <span class="tl-product tl-p32">**Replit**</span> · [[Changes/Replit/2025-11-21-hounddog-privacy-scanning-integration|HoundDog privacy scanning integration]] · Launch
- 2025-11-20 · <span class="tl-product tl-p14">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-11-20-docs-remove-references-to-deprecated-flags-checkpointing-sandbox-image-by-nayong|docs: remove references to deprecated flags (--checkpointing, --sandbox-image)]] · Policy
- 2025-11-07 · <span class="tl-product tl-p10">**Devin**</span> · [[Changes/Devin/2025-11-07-slack-notification-safety|Slack Notification Safety]] · Launch
- 2025-11-05 · <span class="tl-product tl-p12">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-11-05-security|Security]] · Launch

**2025-10**

- 2025-10-29 · <span class="tl-product tl-p8">**Cursor**</span> · [[Changes/Cursor/2025-10-29-sandboxed-terminals-ga|Sandboxed Terminals (GA)]] · Launch
- 2025-10-20 · <span class="tl-product tl-p12">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-10-20-elevencreative-studio|ElevenCreative Studio]] · Launch
- 2025-10-10 · <span class="tl-product tl-p32">**Replit**</span> · [[Changes/Replit/2025-10-10-dependency-vulnerability-scanning|Dependency vulnerability scanning]] · Launch

**2025-09**

- 2025-09-29 · <span class="tl-product tl-p3">**ChatGPT**</span> · [[Changes/ChatGPT/2025-09-29-we-re-rolling-out-parental-controls-globally-in-chatgpt-to-help-families-guide-h-289d0a|ChatGPT rolls out parental controls globally to help families guide how ChatGPT…]] · Policy
- 2025-09-29 · <span class="tl-product tl-p8">**Cursor**</span> · [[Changes/Cursor/2025-09-29-sandboxed-terminals|Sandboxed terminals]] · Launch
- 2025-09-26 · <span class="tl-product tl-p32">**Replit**</span> · [[Changes/Replit/2025-09-26-security-scan-enforcement-for-enterprises|Security scan enforcement for enterprises]] · Launch
- 2025-09-26 · <span class="tl-product tl-p32">**Replit**</span> · [[Changes/Replit/2025-09-26-security-scan-in-deployment|Security scan in deployment]] · Launch
- 2025-09-19 · <span class="tl-product tl-p32">**Replit**</span> · [[Changes/Replit/2025-09-19-supply-chain-attack-blocking|Supply chain attack blocking]] · Launch
- 2025-09-19 · <span class="tl-product tl-p32">**Replit**</span> · [[Changes/Replit/2025-09-19-malicious-file-detection|Malicious file detection]] · Launch
- 2025-09-01 · <span class="tl-product tl-p21">**Lovable**</span> · [[Changes/Lovable/2025-09-01-security-upgrades|Security upgrades]] · Launch

**2025-08**

- 2025-08-29 · <span class="tl-product tl-p32">**Replit**</span> · [[Changes/Replit/2025-08-29-security-rating-improvement|Security rating improvement]] · Launch
- 2025-08-22 · <span class="tl-product tl-p32">**Replit**</span> · [[Changes/Replit/2025-08-22-soc-2-type-ii-certification|SOC 2 Type II certification]] · Launch
- 2025-08-12 · <span class="tl-product tl-p10">**Devin**</span> · [[Changes/Devin/2025-08-12-vpc-repo-indexing|VPC Repo Indexing]] · Launch
- 2025-08-06 · <span class="tl-product tl-p4">**Claude**</span> · [[Changes/Claude/2025-08-06-claude-code-security-reviews|Claude Code Security Reviews]] · Launch

**2025-07**

- 2025-07-11 · <span class="tl-product tl-p32">**Replit**</span> · [[Changes/Replit/2025-07-11-deployment-privacy-indicators|Deployment privacy indicators]] · Launch

**2025-06**

- 2025-06-30 · <span class="tl-product tl-p12">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-06-30-workspaces|Workspaces]] · Launch
- 2025-06-27 · <span class="tl-product tl-p32">**Replit**</span> · [[Changes/Replit/2025-06-27-security-scanner-updates|Security scanner updates]] · Launch
- 2025-06-23 · <span class="tl-product tl-p12">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-06-23-sip-trunking|SIP Trunking]] · Launch
- 2025-06-20 · <span class="tl-product tl-p22">**Manus**</span> · [[Changes/Manus/2025-06-20-open-the-browser-in-a-session-log-in-manually-once-we-encrypt-save-your-login-st|Introducing Manus Cloud Browser]] · Launch
- 2025-06-20 · <span class="tl-product tl-p32">**Replit**</span> · [[Changes/Replit/2025-06-20-deployment-prevention|Deployment prevention]] · Launch
- 2025-06-20 · <span class="tl-product tl-p32">**Replit**</span> · [[Changes/Replit/2025-06-20-view-live-app-button|View live app button]] · Launch
- 2025-06-20 · <span class="tl-product tl-p32">**Replit**</span> · [[Changes/Replit/2025-06-20-security-scanner-improvements|Security scanner improvements]] · Launch
- 2025-06-04 · <span class="tl-product tl-p21">**Lovable**</span> · [[Changes/Lovable/2025-06-04-security|Security]] · Launch

**2025-05**

- 2025-05-23 · <span class="tl-product tl-p32">**Replit**</span> · [[Changes/Replit/2025-05-23-private-development-urls|Private Development URLs]] · Launch
- 2025-05-16 · <span class="tl-product tl-p32">**Replit**</span> · [[Changes/Replit/2025-05-16-security-scans|Security scans]] · Launch
- 2025-05-09 · <span class="tl-product tl-p32">**Replit**</span> · [[Changes/Replit/2025-05-09-enhanced-enterprise-deployment-privacy-settings|Enhanced enterprise deployment privacy settings]] · Launch

**2025-04**

- 2025-04-25 · <span class="tl-product tl-p32">**Replit**</span> · [[Changes/Replit/2025-04-25-advanced-privacy-settings-for-teams|Advanced privacy settings for teams]] · Launch
- 2025-04-14 · <span class="tl-product tl-p12">**ElevenLabs**</span> · [[Changes/ElevenLabs/2025-04-14-pronunciation-dictionaries|Pronunciation Dictionaries]] · Launch

**2025-03**

- 2025-03-13 · <span class="tl-product tl-p13">**Gemini**</span> · [[Changes/Gemini/2025-03-13-gemini-gets-personal-with-tailored-help-based-on-your-search-history|Gemini gets personal, with tailored help based on your Search history]] · Launch

<details class="disclosure">
<summary>Fixes, digests and other changes · 150 (Aider 1 · AnythingLLM 1 · ChatGPT 2 · Cline 1 · Codex CLI 29 · Cursor 3 · Descript 1 · Devin 1 · Dify 27 · Gemini CLI 23 · GitHub Copilot CLI 6 · Google Antigravity 1 · Granola 1 · LM Studio 1 · Lovable 5 · Manus 1 · Ollama 2 · Open WebUI 29 · OpenHands 8 · Raycast 4 · Replit 1 · v0 2)</summary>

**2025-12**

- 2025-12-25 · <span class="tl-product tl-p11">**Dify**</span> · [[Changes/Dify/2025-12-25-3-safety-and-privacy-changes-in-1-11-2|3 Safety and Privacy changes in 1.11.2]] · Digest
- 2025-12-22 · <span class="tl-product tl-p8">**Cursor**</span> · [[Changes/Cursor/2025-12-22-improved-stability-around-how-the-agent-respects-auto-run-preferences-to-prevent|Improved stability around how the agent respects auto-run preferences to prevent…]] · Change
- 2025-12-21 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2025-12-21-2-safety-and-privacy-changes-in-rust-v0-77-0|2 Safety and Privacy changes in rust-v0.77.0]] · Digest
- 2025-12-21 · <span class="tl-product tl-p26">**Open WebUI**</span> · [[Changes/Open WebUI/2025-12-21-6-safety-and-privacy-changes-in-v0-6-42|6 Safety and Privacy changes in v0.6.42]] · Digest
- 2025-12-19 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2025-12-19-2-safety-and-privacy-changes-in-rust-v0-76-0|2 Safety and Privacy changes in rust-v0.76.0]] · Digest
- 2025-12-19 · <span class="tl-product tl-p15">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2025-12-19-add-url-permission-controls-which-affect-common-shell-commands-which-access-the|Add URL permission controls which affect common shell commands which access the web]] · Change
- 2025-12-18 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2025-12-18-3-safety-and-privacy-changes-in-rust-v0-74-0|3 Safety and Privacy changes in rust-v0.74.0]] · Digest
- 2025-12-16 · <span class="tl-product tl-p14">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-12-16-2-safety-and-privacy-changes-in-v0-21-0|2 Safety and Privacy changes in v0.21.0]] · Digest
- 2025-12-15 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2025-12-15-3-safety-and-privacy-changes-in-rust-v0-73-0|3 Safety and Privacy changes in rust-v0.73.0]] · Digest
- 2025-12-13 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2025-12-13-3-safety-and-privacy-changes-in-rust-v0-72-0|3 Safety and Privacy changes in rust-v0.72.0]] · Digest
- 2025-12-12 · <span class="tl-product tl-p11">**Dify**</span> · [[Changes/Dify/2025-12-12-3-safety-and-privacy-changes-in-1-11-1|3 Safety and Privacy changes in 1.11.1]] · Digest
- 2025-12-12 · <span class="tl-product tl-p39">**v0**</span> · [[Changes/v0/2025-12-12-cve-2025-55184-denial-of-service-dos-vulnerability|CVE-2025-55184 : Denial of Service (DoS) vulnerability]] · Change
- 2025-12-12 · <span class="tl-product tl-p39">**v0**</span> · [[Changes/v0/2025-12-12-cve-2025-55183-source-code-disclosure-vulnerability|CVE-2025-55183 : Source code disclosure vulnerability]] · Change
- 2025-12-11 · <span class="tl-product tl-p11">**Dify**</span> · [[Changes/Dify/2025-12-11-2-safety-and-privacy-changes-in-1-11-0|2 Safety and Privacy changes in 1.11.0]] · Digest
- 2025-12-10 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2025-12-10-5-safety-and-privacy-changes-in-rust-v0-69-0|5 Safety and Privacy changes in rust-v0.69.0]] · Digest
- 2025-12-09 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2025-12-09-3-safety-and-privacy-changes-in-rust-v0-66-0|3 Safety and Privacy changes in rust-v0.66.0]] · Digest
- 2025-12-09 · <span class="tl-product tl-p14">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-12-09-add-consent-flag-to-link-command-by-kevinjwang1-in-https-github-com-google-gemin|Add consent flag to Link command]] · Change
- 2025-12-08 · <span class="tl-product tl-p16">**Google Antigravity**</span> · [[Changes/Google Antigravity/2025-12-08-various-security-fixes|Various security fixes]] · Change
- 2025-12-02 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2025-12-02-9-safety-and-privacy-changes-in-rust-v0-64-0|9 Safety and Privacy changes in rust-v0.64.0]] · Digest
- 2025-12-02 · <span class="tl-product tl-p14">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-12-02-improve-code-coverage-for-cli-src-ui-privacy-package-by-megha1188-in-https-githu|Improve code coverage for cli/src/ui/privacy package]] · Change
- 2025-12-02 · <span class="tl-product tl-p26">**Open WebUI**</span> · [[Changes/Open WebUI/2025-12-02-2-safety-and-privacy-changes-in-v0-6-41|2 Safety and Privacy changes in v0.6.41]] · Digest

**2025-11**

- 2025-11-27 · <span class="tl-product tl-p6">**Cline**</span> · [[Changes/Cline/2025-11-27-maint-npm-audit-fix-for-glob-package-vulnerability-by-canvrno-in-https-github-co|maint: npm audit fix for glob package vulnerability]] · Change
- 2025-11-26 · <span class="tl-product tl-p11">**Dify**</span> · [[Changes/Dify/2025-11-26-2-safety-and-privacy-changes-in-1-10-1|2 Safety and Privacy changes in 1.10.1]] · Digest
- 2025-11-26 · <span class="tl-product tl-p21">**Lovable**</span> · [[Changes/Lovable/2025-11-26-improved-share-invite-experience|Improved share & invite experience]] · Change
- 2025-11-24 · <span class="tl-product tl-p26">**Open WebUI**</span> · [[Changes/Open WebUI/2025-11-24-api-key-creation-is-now-controlled-by-granular-user-and-group-permissions-with-t|🔐 API key creation is now controlled by granular user and group permissions…]] · Change
- 2025-11-20 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2025-11-20-shell-reliability-and-sandbox-warnings-fallback-shell-selection-is-hardened-and|Shell reliability and sandbox warnings]] · Change
- 2025-11-19 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2025-11-19-7-safety-and-privacy-changes-in-rust-v0-59-0|7 Safety and Privacy changes in rust-v0.59.0]] · Digest
- 2025-11-18 · <span class="tl-product tl-p15">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2025-11-18-fix-file-operations-timing-out-while-waiting-for-user-permission|Fix file operations timing out while waiting for user permission]] · Change
- 2025-11-17 · <span class="tl-product tl-p15">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2025-11-17-2-safety-and-privacy-changes-in-v0-0-359|2 Safety and Privacy changes in v0.0.359]] · Digest
- 2025-11-13 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2025-11-13-6480-use-codex-linux-sandbox-in-unified-exec-6c36318bd|♯6480 — Use codex-linux-sandbox in unified exec (6c36318bd)]] · Change
- 2025-11-13 · <span class="tl-product tl-p11">**Dify**</span> · [[Changes/Dify/2025-11-13-2-safety-and-privacy-changes-in-1-10-0|2 Safety and Privacy changes in 1.10.0]] · Digest
- 2025-11-12 · <span class="tl-product tl-p22">**Manus**</span> · [[Changes/Manus/2025-11-12-the-moment-you-enable-payments-manus-spins-up-a-temporary-stripe-sandbox-so-you|Start testing payments instantly with Stripe]] · Change
- 2025-11-07 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2025-11-07-2-safety-and-privacy-changes-in-rust-v0-56-0|2 Safety and Privacy changes in rust-v0.56.0]] · Digest
- 2025-11-07 · <span class="tl-product tl-p14">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-11-07-migrate-console-error-to-coreevents-debugger-for-sandbox-logger-chatrecordingser|migrate console.error to coreEvents/debugger for sandbox, logger, chatRecordingService]] · Change
- 2025-11-06 · <span class="tl-product tl-p26">**Open WebUI**</span> · [[Changes/Open WebUI/2025-11-06-4-safety-and-privacy-changes-in-v0-6-35|4 Safety and Privacy changes in v0.6.35]] · Digest
- 2025-11-04 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2025-11-04-3-safety-and-privacy-changes-in-rust-v0-54-0|3 Safety and Privacy changes in rust-v0.54.0]] · Digest
- 2025-11-04 · <span class="tl-product tl-p14">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-11-04-fix-infra-simplify-cancel-in-progress-and-add-permission-to-set-status-step-by-s|fix(infra) - Simplify cancel in progress and add permission to set status step]] · Change

**2025-10**

- 2025-10-31 · <span class="tl-product tl-p31">**Raycast**</span> · [[Changes/Raycast/2025-10-31-keyboard-privacy-statement-accessible-from-settings-in-the-app|Keyboard: Privacy statement, accessible from settings in the app]] · Change
- 2025-10-30 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2025-10-30-3-safety-and-privacy-changes-in-rust-v0-52-0|3 Safety and Privacy changes in rust-v0.52.0]] · Digest
- 2025-10-29 · <span class="tl-product tl-p29">**OpenHands**</span> · [[Changes/OpenHands/2025-10-29-3-safety-and-privacy-changes-in-0-60-0|3 Safety and Privacy changes in 0.60.0]] · Digest
- 2025-10-28 · <span class="tl-product tl-p9">**Descript**</span> · [[Changes/Descript/2025-10-28-permission-changes-now-take-effect-immediately-without-needing-to-refresh|Permission changes now take effect immediately without needing to refresh]] · Change
- 2025-10-25 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2025-10-25-5536-added-model-summary-and-risk-assessment-for-commands-that-violate-sandbox-p|♯5536 — Added model summary and risk assessment for commands that violate sandbox policy]] · Change
- 2025-10-23 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2025-10-23-2-safety-and-privacy-changes-in-rust-v0-48-0|2 Safety and Privacy changes in rust-v0.48.0]] · Digest
- 2025-10-22 · <span class="tl-product tl-p11">**Dify**</span> · [[Changes/Dify/2025-10-22-fix-web-app-permission-check-by-douxc-in-https-github-com-langgenius-dify-pull-2|Fix/web app permission check]] · Change
- 2025-10-22 · <span class="tl-product tl-p14">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-10-22-2-safety-and-privacy-changes-in-v0-10-0|2 Safety and Privacy changes in v0.10.0]] · Digest
- 2025-10-22 · <span class="tl-product tl-p15">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2025-10-22-ensure-that-environment-variables-are-expanded-before-running-path-permission-ch|Ensure that environment variables are expanded before running path permission checks]] · Change
- 2025-10-17 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2025-10-17-2-safety-and-privacy-changes-in-rust-v0-47-0|2 Safety and Privacy changes in rust-v0.47.0]] · Digest
- 2025-10-16 · <span class="tl-product tl-p26">**Open WebUI**</span> · [[Changes/Open WebUI/2025-10-16-jwt-token-expiration-default-is-now-set-to-4-weeks-instead-of-never-expiring-wit|🔒 JWT token expiration default is now set to 4 weeks instead of never expiring…]] · Change
- 2025-10-07 · <span class="tl-product tl-p14">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-10-07-3-safety-and-privacy-changes-in-v0-8-0|3 Safety and Privacy changes in v0.8.0]] · Digest
- 2025-10-06 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2025-10-06-codex-login-api-key-was-replaced-with-codex-login-with-api-key-that-reads-the-ke|codex login --api-key was replaced with codex login --with-api-key that reads…]] · Change
- 2025-10-06 · <span class="tl-product tl-p21">**Lovable**</span> · [[Changes/Lovable/2025-10-06-better-workspace-management|Better workspace management]] · Change
- 2025-10-03 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2025-10-03-3-safety-and-privacy-changes-in-rust-v0-44-0|3 Safety and Privacy changes in rust-v0.44.0]] · Digest
- 2025-10-03 · <span class="tl-product tl-p10">**Devin**</span> · [[Changes/Devin/2025-10-03-enterprise-api-v2-git-permissions-endpoint-now-returns-permission-names-dict-map|Enterprise API v2 git permissions endpoint now returns permission\names dict…]] · Change
- 2025-10-01 · <span class="tl-product tl-p14">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-10-01-4-safety-and-privacy-changes-in-v0-7-0|4 Safety and Privacy changes in v0.7.0]] · Digest
- 2025-10-01 · <span class="tl-product tl-p15">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2025-10-01-improved-how-we-extract-paths-from-shell-commands-for-permission-handling-might|Improved how we extract paths from shell commands for permission handling…]] · Change
- 2025-10-01 · <span class="tl-product tl-p29">**OpenHands**</span> · [[Changes/OpenHands/2025-10-01-significantly-improved-the-security-of-the-openhands-enterprise-docker-image-by|Significantly improved the security of the OpenHands enterprise Docker image…]] · Change

**2025-09**

- 2025-09-29 · <span class="tl-product tl-p11">**Dify**</span> · [[Changes/Dify/2025-09-29-3-safety-and-privacy-changes-in-1-9-1|3 Safety and Privacy changes in 1.9.1]] · Digest
- 2025-09-29 · <span class="tl-product tl-p26">**Open WebUI**</span> · [[Changes/Open WebUI/2025-09-29-2-safety-and-privacy-changes-in-v0-6-32|2 Safety and Privacy changes in v0.6.32]] · Digest
- 2025-09-26 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2025-09-26-2-safety-and-privacy-changes-in-rust-v0-42-0|2 Safety and Privacy changes in rust-v0.42.0]] · Digest
- 2025-09-26 · <span class="tl-product tl-p15">**GitHub Copilot CLI**</span> · [[Changes/GitHub Copilot CLI/2025-09-26-improved-the-error-message-received-when-using-a-pat-that-is-missing-the-copilot|Improved the error message received when using a PAT that is missing…]] · Change
- 2025-09-25 · <span class="tl-product tl-p26">**Open WebUI**</span> · [[Changes/Open WebUI/2025-09-25-3-safety-and-privacy-changes-in-v0-6-31|3 Safety and Privacy changes in v0.6.31]] · Digest
- 2025-09-24 · <span class="tl-product tl-p14">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-09-24-4-safety-and-privacy-changes-in-v0-6-0|4 Safety and Privacy changes in v0.6.0]] · Digest
- 2025-09-23 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2025-09-23-3880-add-non-sandbox-test-helper-3880|♯3880 Add non_sandbox_test helper (♯3880)]] · Change
- 2025-09-22 · <span class="tl-product tl-p11">**Dify**</span> · [[Changes/Dify/2025-09-22-5-safety-and-privacy-changes-in-1-9-0|5 Safety and Privacy changes in 1.9.0]] · Digest
- 2025-09-17 · <span class="tl-product tl-p14">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-09-17-2-safety-and-privacy-changes-in-v0-5-3|2 Safety and Privacy changes in v0.5.3]] · Digest
- 2025-09-17 · <span class="tl-product tl-p26">**Open WebUI**</span> · [[Changes/Open WebUI/2025-09-17-microsoft-entra-id-authentication-type-support-was-added-for-azure-openai-connec|🔑 Microsoft Entra ID authentication type support was added for Azure OpenAI…]] · Change
- 2025-09-17 · <span class="tl-product tl-p26">**Open WebUI**</span> · [[Changes/Open WebUI/2025-09-17-knowledge-base-permission-logic-was-corrected-to-ensure-private-collection-owner|📚 Knowledge base permission logic was corrected to ensure private collection owners…]] · Change
- 2025-09-15 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2025-09-15-3-safety-and-privacy-changes-in-rust-v0-36-0|3 Safety and Privacy changes in rust-v0.36.0]] · Digest
- 2025-09-10 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2025-09-10-ci-build-faster-tests-with-nextest-add-shear-minor-macos-permission-adjustment|CI/Build: faster tests with nextest, add shear; minor macOS permission adjustment]] · Change
- 2025-09-09 · <span class="tl-product tl-p14">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-09-09-2-safety-and-privacy-changes-in-v0-4-0|2 Safety and Privacy changes in v0.4.0]] · Digest
- 2025-09-09 · <span class="tl-product tl-p26">**Open WebUI**</span> · [[Changes/Open WebUI/2025-09-09-4-safety-and-privacy-changes-in-v0-6-27|4 Safety and Privacy changes in v0.6.27]] · Digest
- 2025-09-05 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2025-09-05-3128-mcp-sandbox-call|♯3128 MCP sandbox call]] · Change
- 2025-09-04 · <span class="tl-product tl-p14">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-09-04-2-safety-and-privacy-changes-in-v0-3-0|2 Safety and Privacy changes in v0.3.0]] · Digest
- 2025-09-03 · <span class="tl-product tl-p11">**Dify**</span> · [[Changes/Dify/2025-09-03-3-safety-and-privacy-changes-in-1-8-1|3 Safety and Privacy changes in 1.8.1]] · Digest

**2025-08**

- 2025-08-28 · <span class="tl-product tl-p26">**Open WebUI**</span> · [[Changes/Open WebUI/2025-08-28-2-safety-and-privacy-changes-in-v0-6-26|2 Safety and Privacy changes in v0.6.26]] · Digest
- 2025-08-27 · <span class="tl-product tl-p11">**Dify**</span> · [[Changes/Dify/2025-08-27-7-safety-and-privacy-changes-in-1-8-0|7 Safety and Privacy changes in 1.8.0]] · Digest
- 2025-08-26 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2025-08-26-2587-do-not-show-timeouts-as-sandbox-error-s|♯2587 do not show timeouts as "sandbox error"s]] · Change
- 2025-08-21 · <span class="tl-product tl-p26">**Open WebUI**</span> · [[Changes/Open WebUI/2025-08-21-6-safety-and-privacy-changes-in-v0-6-23|6 Safety and Privacy changes in v0.6.23]] · Digest
- 2025-08-20 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2025-08-20-2464-https-github-com-openai-codex-pull-2464-docs-document-writable-roots-for-sa|♯2464((source link) docs: document writable_roots…]] · Change
- 2025-08-15 · <span class="tl-product tl-p2">**AnythingLLM**</span> · [[Changes/AnythingLLM/2025-08-15-update-security-ui-to-match-all-other-settings-by-ashikaanand12-in-https-github|Update Security UI to match all other Settings]] · Change
- 2025-08-14 · <span class="tl-product tl-p14">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-08-14-7-safety-and-privacy-changes-in-v0-1-21|7 Safety and Privacy changes in v0.1.21]] · Digest
- 2025-08-13 · <span class="tl-product tl-p14">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-08-13-ensure-sandbox-build-script-is-cross-platform-by-wldoooon-in-https-github-com-go|ensure sandbox build script is cross-platform]] · Change
- 2025-08-12 · <span class="tl-product tl-p14">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-08-12-2-safety-and-privacy-changes-in-v0-1-19|2 Safety and Privacy changes in v0.1.19]] · Digest
- 2025-08-11 · <span class="tl-product tl-p11">**Dify**</span> · [[Changes/Dify/2025-08-11-3-safety-and-privacy-changes-in-1-7-2|3 Safety and Privacy changes in 1.7.2]] · Digest
- 2025-08-10 · <span class="tl-product tl-p26">**Open WebUI**</span> · [[Changes/Open WebUI/2025-08-10-opentelemetry-configuration-consistency-fixed-an-issue-where-opentelemetry-metri|🛠️ OpenTelemetry Configuration Consistency]] · Change
- 2025-08-09 · <span class="tl-product tl-p26">**Open WebUI**</span> · [[Changes/Open WebUI/2025-08-09-10-safety-and-privacy-changes-in-v0-6-19|10 Safety and Privacy changes in v0.6.19]] · Digest
- 2025-08-07 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2025-08-07-new-onboarding-flow-that-uses-sandbox-workspace-write-and-ask-for-approval-on-re|new onboarding flow that uses…]] · Change
- 2025-08-06 · <span class="tl-product tl-p14">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-08-06-4-safety-and-privacy-changes-in-v0-1-18|4 Safety and Privacy changes in v0.1.18]] · Digest
- 2025-08-05 · <span class="tl-product tl-p14">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-08-05-4-safety-and-privacy-changes-in-v0-1-17|4 Safety and Privacy changes in v0.1.17]] · Digest
- 2025-08-02 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2025-08-02-https-github-com-openai-codex-pull-1705-security-fix-to-ensure-apply-patch-is-ru|(source link) security fix to ensure apply_patch…]] · Change
- 2025-08-02 · <span class="tl-product tl-p14">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-08-02-4-safety-and-privacy-changes-in-v0-1-16|4 Safety and Privacy changes in v0.1.16]] · Digest

**2025-07**

- 2025-07-30 · <span class="tl-product tl-p14">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-07-30-migrate-privacy-to-new-architecture-by-abhipatel12-in-https-github-com-google-ge|Migrate /privacy to new architecture]] · Change
- 2025-07-29 · <span class="tl-product tl-p8">**Cursor**</span> · [[Changes/Cursor/2025-07-29-2-safety-and-privacy-changes-in-1-3|2 Safety and Privacy changes in 1.3]] · Digest
- 2025-07-25 · <span class="tl-product tl-p14">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-07-25-migrate-privacy-to-new-architecture-by-abhipatel12-in-https-github-com-google-ge|Migrate /privacy to new architecture]] · Change
- 2025-07-23 · <span class="tl-product tl-p11">**Dify**</span> · [[Changes/Dify/2025-07-23-2-safety-and-privacy-changes-in-1-7-0|2 Safety and Privacy changes in 1.7.0]] · Digest
- 2025-07-19 · <span class="tl-product tl-p14">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-07-19-migrate-privacy-to-new-architecture-by-abhipatel12-in-https-github-com-google-ge|Migrate /privacy to new architecture]] · Change
- 2025-07-19 · <span class="tl-product tl-p26">**Open WebUI**</span> · [[Changes/Open WebUI/2025-07-19-2-safety-and-privacy-changes-in-v0-6-17|2 Safety and Privacy changes in v0.6.17]] · Digest
- 2025-07-14 · <span class="tl-product tl-p26">**Open WebUI**</span> · [[Changes/Open WebUI/2025-07-14-3-safety-and-privacy-changes-in-v0-6-16|3 Safety and Privacy changes in v0.6.16]] · Digest
- 2025-07-11 · <span class="tl-product tl-p14">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-07-11-update-terms-of-service-and-privacy-notice-for-clarity-by-jkcinouye-in-https-git|Update Terms of Service and Privacy Notice for clarity]] · Change
- 2025-07-08 · <span class="tl-product tl-p7">**Codex CLI**</span> · [[Changes/Codex CLI/2025-07-08-adds-support-for-a-sandbox-flag-and-makes-some-breaking-changes-to-config-toml-a|Adds support for a --sandbox flag and makes some breaking changes to config.toml…]] · Change
- 2025-07-07 · <span class="tl-product tl-p17">**Granola**</span> · [[Changes/Granola/2025-07-07-we-ve-shown-independent-auditors-that-our-security-practices-meet-soc2-type-2-st|Granola is SOC2 compliant]] · Change
- 2025-07-02 · <span class="tl-product tl-p11">**Dify**</span> · [[Changes/Dify/2025-07-02-chore-upgrade-package-versions-for-security-reason-by-iamjoel-in-https-github-co|chore: upgrade package versions for security reason]] · Change
- 2025-07-01 · <span class="tl-product tl-p14">**Gemini CLI**</span> · [[Changes/Gemini CLI/2025-07-01-esc-to-exit-privacy-screen-in-error-state-by-scidomino-in-https-github-com-googl|Esc to exit privacy screen in error state]] · Change

**2025-06**

- 2025-06-26 · <span class="tl-product tl-p31">**Raycast**</span> · [[Changes/Raycast/2025-06-26-favicon-provider-we-added-a-new-setting-to-let-you-pick-your-favicon-provider-or|Favicon Provider: We added a new setting to let you pick your favicon provider…]] · Change
- 2025-06-25 · <span class="tl-product tl-p11">**Dify**</span> · [[Changes/Dify/2025-06-25-2-safety-and-privacy-changes-in-1-5-0|2 Safety and Privacy changes in 1.5.0]] · Digest
- 2025-06-25 · <span class="tl-product tl-p20">**LM Studio**</span> · [[Changes/LM Studio/2025-06-25-fixed-a-bug-where-tool-permission-dialog-wouldn-t-auto-scroll-to-the-bottom-of-t|Fixed a bug where tool permission dialog wouldn't auto-scroll to the bottom of the chat]] · Fix
- 2025-06-20 · <span class="tl-product tl-p29">**OpenHands**</span> · [[Changes/OpenHands/2025-06-20-daytona-runtime-sandbox-handling-by-idagelic-in-https-github-com-all-hands-ai-op|Daytona Runtime sandbox handling]] · Change
- 2025-06-20 · <span class="tl-product tl-p29">**OpenHands**</span> · [[Changes/OpenHands/2025-06-20-support-for-dev-container-networking-without-host-mode-by-llamantino-in-https-gi|Support for dev container networking without host mode by @llamantino…]] · Change
- 2025-06-20 · <span class="tl-product tl-p29">**OpenHands**</span> · [[Changes/OpenHands/2025-06-20-enhanced-security-by-ensuring-redirect-uri-is-https-unless-it-is-for-localhost-b|Enhanced security by ensuring redirect URI is HTTPS unless it is for localhost]] · Change
- 2025-06-16 · <span class="tl-product tl-p26">**Open WebUI**</span> · [[Changes/Open WebUI/2025-06-16-2-safety-and-privacy-changes-in-v0-6-15|2 Safety and Privacy changes in v0.6.15]] · Digest
- 2025-06-11 · <span class="tl-product tl-p11">**Dify**</span> · [[Changes/Dify/2025-06-11-2-safety-and-privacy-changes-in-1-4-2|2 Safety and Privacy changes in 1.4.2]] · Digest
- 2025-06-11 · <span class="tl-product tl-p31">**Raycast**</span> · [[Changes/Raycast/2025-06-11-this-release-aims-to-fix-a-number-of-instability-issues-that-you-have-experience|This release aims to fix a number of instability issues that you have experienced…]] · Change
- 2025-06-10 · <span class="tl-product tl-p26">**Open WebUI**</span> · [[Changes/Open WebUI/2025-06-10-4-safety-and-privacy-changes-in-v0-6-14|4 Safety and Privacy changes in v0.6.14]] · Digest
- 2025-06-04 · <span class="tl-product tl-p8">**Cursor**</span> · [[Changes/Cursor/2025-06-04-team-admins-can-now-disable-privacy-mode|Team admins can now disable Privacy Mode]] · Change

**2025-05**

- 2025-05-27 · <span class="tl-product tl-p11">**Dify**</span> · [[Changes/Dify/2025-05-27-3-safety-and-privacy-changes-in-1-4-1|3 Safety and Privacy changes in 1.4.1]] · Digest
- 2025-05-26 · <span class="tl-product tl-p26">**Open WebUI**</span> · [[Changes/Open WebUI/2025-05-26-general-backend-stability-security-enhancements-various-backend-refinements-ensu|⚡ General Backend Stability & Security Enhancements]] · Change
- 2025-05-19 · <span class="tl-product tl-p26">**Open WebUI**</span> · [[Changes/Open WebUI/2025-05-19-3-safety-and-privacy-changes-in-v0-6-10|3 Safety and Privacy changes in v0.6.10]] · Digest
- 2025-05-16 · <span class="tl-product tl-p32">**Replit**</span> · [[Changes/Replit/2025-05-16-this-week-s-release-is-all-about-safety-and-security-replit-has-added-a-new-secu|This week's release is all about safety and security]] · Change
- 2025-05-15 · <span class="tl-product tl-p11">**Dify**</span> · [[Changes/Dify/2025-05-15-chore-upgrade-package-version-to-fix-security-issue-by-iamjoel-in-https-github-c|chore: upgrade package version to fix security issue]] · Change
- 2025-05-12 · <span class="tl-product tl-p29">**OpenHands**</span> · [[Changes/OpenHands/2025-05-12-simplified-workspace-mounting-with-sandbox-volumes-by-xingyaoww-in-https-github|Simplified workspace mounting with SANDBOX_VOLUMES]] · Change
- 2025-05-06 · <span class="tl-product tl-p26">**Open WebUI**</span> · [[Changes/Open WebUI/2025-05-06-tool-server-settings-ui-privacy-restored-prevented-restricted-users-from-accessi|🔎 Tool Server Settings UI Privacy Restored]] · Change
- 2025-05-05 · <span class="tl-product tl-p26">**Open WebUI**</span> · [[Changes/Open WebUI/2025-05-05-7-safety-and-privacy-changes-in-v0-6-6|7 Safety and Privacy changes in v0.6.6]] · Digest

**2025-04**

- 2025-04-23 · <span class="tl-product tl-p11">**Dify**</span> · [[Changes/Dify/2025-04-23-5-safety-and-privacy-changes-in-1-3-0|5 Safety and Privacy changes in 1.3.0]] · Digest
- 2025-04-23 · <span class="tl-product tl-p29">**OpenHands**</span> · [[Changes/OpenHands/2025-04-23-enabled-custom-sandbox-for-resolver-by-tetsu-is-in-https-github-com-all-hands-ai|Enabled custom sandbox for resolver]] · Change
- 2025-04-13 · <span class="tl-product tl-p26">**Open WebUI**</span> · [[Changes/Open WebUI/2025-04-13-5-safety-and-privacy-changes-in-v0-6-3|5 Safety and Privacy changes in v0.6.3]] · Digest
- 2025-04-09 · <span class="tl-product tl-p11">**Dify**</span> · [[Changes/Dify/2025-04-09-4-safety-and-privacy-changes-in-1-2-0|4 Safety and Privacy changes in 1.2.0]] · Digest
- 2025-04-09 · <span class="tl-product tl-p31">**Raycast**</span> · [[Changes/Raycast/2025-04-09-favicon-provider-we-added-a-new-setting-to-let-you-pick-your-favicon-provider-or|Favicon Provider: We added a new setting to let you pick your favicon provider…]] · Change
- 2025-04-05 · <span class="tl-product tl-p26">**Open WebUI**</span> · [[Changes/Open WebUI/2025-04-05-3-safety-and-privacy-changes-in-v0-6-1|3 Safety and Privacy changes in v0.6.1]] · Digest
- 2025-04-01 · <span class="tl-product tl-p26">**Open WebUI**</span> · [[Changes/Open WebUI/2025-04-01-2-safety-and-privacy-changes-in-v0-6-0|2 Safety and Privacy changes in v0.6.0]] · Digest

**2025-03**

- 2025-03-24 · <span class="tl-product tl-p11">**Dify**</span> · [[Changes/Dify/2025-03-24-3-safety-and-privacy-changes-in-0-15-5|3 Safety and Privacy changes in 0.15.5]] · Digest
- 2025-03-24 · <span class="tl-product tl-p11">**Dify**</span> · [[Changes/Dify/2025-03-24-2-safety-and-privacy-changes-in-1-1-3|2 Safety and Privacy changes in 1.1.3]] · Digest
- 2025-03-21 · <span class="tl-product tl-p11">**Dify**</span> · [[Changes/Dify/2025-03-21-3-safety-and-privacy-changes-in-1-1-2|3 Safety and Privacy changes in 1.1.2]] · Digest
- 2025-03-21 · <span class="tl-product tl-p11">**Dify**</span> · [[Changes/Dify/2025-03-21-3-safety-and-privacy-changes-in-0-15-4|3 Safety and Privacy changes in 0.15.4]] · Digest
- 2025-03-21 · <span class="tl-product tl-p21">**Lovable**</span> · [[Changes/Lovable/2025-03-21-shipped-continuous-project-lock-extensions-and-sandbox-pings-to-support-long-run|Shipped continuous project lock extensions and sandbox pings to support long-running…]] · Change
- 2025-03-20 · <span class="tl-product tl-p11">**Dify**</span> · [[Changes/Dify/2025-03-20-fix-removing-member-without-permission-by-batman0911-in-https-github-com-langgen|fix removing member without permission]] · Change
- 2025-03-19 · <span class="tl-product tl-p29">**OpenHands**</span> · [[Changes/OpenHands/2025-03-19-feat-microagents-add-security-microagent-by-h55nick-in-https-github-com-all-hand|feat(microagents): Add security microagent]] · Change
- 2025-03-18 · <span class="tl-product tl-p3">**ChatGPT**</span> · [[Changes/ChatGPT/2025-03-18-more-clear-and-private-incognito-keyboard-for-temporary-chats|More clear and private Incognito keyboard for Temporary Chats]] · Change
- 2025-03-18 · <span class="tl-product tl-p3">**ChatGPT**</span> · [[Changes/ChatGPT/2025-03-18-new-ui-for-temporary-chats-we-ve-made-accessing-and-viewing-these-private-conver|New UI for Temporary Chats]] · Change
- 2025-03-18 · <span class="tl-product tl-p11">**Dify**</span> · [[Changes/Dify/2025-03-18-this-release-aims-to-strengthen-our-platform-s-reliability-security-and-usabilit|This release aims to strengthen our platform's reliability, security, and usability…]] · Change
- 2025-03-13 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2025-03-13-added-ignore-permission-denied-option-to-file-watcher-to-prevent-errors-when-acc|Added ignore_permission_denied option to file watcher to prevent errors…]] · Change
- 2025-03-11 · <span class="tl-product tl-p11">**Dify**</span> · [[Changes/Dify/2025-03-11-2-safety-and-privacy-changes-in-1-0-1|2 Safety and Privacy changes in 1.0.1]] · Digest

**2025-02**

- 2025-02-27 · <span class="tl-product tl-p25">**Ollama**</span> · [[Changes/Ollama/2025-02-27-fixed-a-series-of-permission-denied-issues-when-installing-ollama-on-linux|Fixed a series of permission denied issues when installing Ollama on Linux]] · Fix
- 2025-02-21 · <span class="tl-product tl-p21">**Lovable**</span> · [[Changes/Lovable/2025-02-21-no-more-stuck-on-saving-changes-for-messages-that-produces-code-and-don-t-result|No more stuck on saving changes... for messages that produces code and don't…]] · Change
- 2025-02-20 · <span class="tl-product tl-p25">**Ollama**</span> · [[Changes/Ollama/2025-02-20-fixed-permission-denied-issues-after-installing-ollama-on-linux|Fixed permission denied issues after installing Ollama on Linux]] · Fix
- 2025-02-18 · <span class="tl-product tl-p26">**Open WebUI**</span> · [[Changes/Open WebUI/2025-02-18-message-delete-confirmation-dialog-prevent-accidental-deletions-with-a-new-confi|🗑️ Message Delete Confirmation Dialog]] · Change
- 2025-02-05 · <span class="tl-product tl-p26">**Open WebUI**</span> · [[Changes/Open WebUI/2025-02-05-3-safety-and-privacy-changes-in-v0-5-8|3 Safety and Privacy changes in v0.5.8]] · Digest

**2025-01**

- 2025-01-23 · <span class="tl-product tl-p26">**Open WebUI**</span> · [[Changes/Open WebUI/2025-01-23-rbac-permissions-for-tools-and-models-corrected-incorrect-role-based-access-cont|🔒 RBAC Permissions for Tools and Models]] · Change
- 2025-01-18 · <span class="tl-product tl-p21">**Lovable**</span> · [[Changes/Lovable/2025-01-18-sandbox-issues-are-resolved-and-the-service-is-fully-operational-again|Sandbox issues are resolved, and the service is fully operational again]] · Change
- 2025-01-07 · <span class="tl-product tl-p11">**Dify**</span> · [[Changes/Dify/2025-01-07-2-safety-and-privacy-changes-in-0-15-0|2 Safety and Privacy changes in 0.15.0]] · Digest
- 2025-01-05 · <span class="tl-product tl-p26">**Open WebUI**</span> · [[Changes/Open WebUI/2025-01-05-api-endpoint-restrictions-resolution-fixed-a-critical-bug-where-the-api-key-allo|🔑 API Endpoint Restrictions Resolution]] · Change

</details>

</details>

<details class="disclosure">
<summary>2024 · 62 entries (Aider 1 · AnythingLLM 1 · Cline 1 · Cursor 2 · Descript 1 · Dify 22 · Gemini 4 · Ollama 1 · Open WebUI 15 · OpenHands 10 · Raycast 2 · Runway 1 · Superwhisper 1)</summary>

**2024-11**

- 2024-11-18 · <span class="tl-product tl-p13">**Gemini**</span> · [[Changes/Gemini/2024-11-18-expanding-the-gemini-app-as-a-core-service-with-enterprise-grade-data-protection|Expanding the Gemini app as a core service with enterprise-grade data protection…]] · Expansion
- 2024-11-12 · <span class="tl-product tl-p13">**Gemini**</span> · [[Changes/Gemini/2024-11-12-launching-gemini-to-google-workspace-for-education-teen-students|Launching Gemini to Google Workspace for Education teen students]] · Policy

**2024-08**

- 2024-08-29 · <span class="tl-product tl-p13">**Gemini**</span> · [[Changes/Gemini/2024-08-29-added-data-protection-for-google-workspace-for-education-users|Added data protection for Google Workspace for Education users]] · Launch

**2024-05**

- 2024-05-07 · <span class="tl-product tl-p9">**Descript**</span> · [[Changes/Descript/2024-05-07-descript-for-web-now-with-recording-beta|Descript for Web now with Recording (Beta)]] · Launch

**2024-04**

- 2024-04-30 · <span class="tl-product tl-p13">**Gemini**</span> · [[Changes/Gemini/2024-04-30-extensions-are-now-available-in-more-languages|Extensions are now available in more languages]] · Launch

<details class="disclosure">
<summary>Fixes, digests and other changes · 57 (Aider 1 · AnythingLLM 1 · Cline 1 · Cursor 2 · Dify 22 · Ollama 1 · Open WebUI 15 · OpenHands 10 · Raycast 2 · Runway 1 · Superwhisper 1)</summary>

**2024-12**

- 2024-12-25 · <span class="tl-product tl-p26">**Open WebUI**</span> · [[Changes/Open WebUI/2024-12-25-api-key-authentication-restriction-narrowed-api-key-auth-permissions-to-api-mode|💡 API Key Authentication Restriction]] · Change
- 2024-12-18 · <span class="tl-product tl-p6">**Cline**</span> · [[Changes/Cline/2024-12-18-cline-s-most-requested-feature-is-here-you-can-now-let-cline-work-more-autonomou|Cline's most requested feature is here 🎉 You can now let Cline work more…]] · Change
- 2024-12-04 · <span class="tl-product tl-p29">**OpenHands**</span> · [[Changes/OpenHands/2024-12-04-support-custom-sandbox-for-resolver-by-malhotra5-in-https-github-com-all-hands-a|Support custom sandbox for resolver]] · Change
- 2024-12-04 · <span class="tl-product tl-p31">**Raycast**</span> · [[Changes/Raycast/2024-12-04-deeplinks-removed-security-alert-showing-when-opening-a-deeplink-from-quicklink|Deeplinks: Removed security alert showing when opening a deeplink from quicklink]] · Change

**2024-11**

- 2024-11-26 · <span class="tl-product tl-p25">**Ollama**</span> · [[Changes/Ollama/2024-11-26-strong-typing-throughout-the-library-for-improved-reliability-and-type-safety|Strong typing throughout the library for improved reliability and type safety]] · Change
- 2024-11-19 · <span class="tl-product tl-p26">**Open WebUI**</span> · [[Changes/Open WebUI/2024-11-19-2-safety-and-privacy-changes-in-v0-4-0|2 Safety and Privacy changes in v0.4.0]] · Digest
- 2024-11-11 · <span class="tl-product tl-p11">**Dify**</span> · [[Changes/Dify/2024-11-11-2-safety-and-privacy-changes-in-0-11-1|2 Safety and Privacy changes in 0.11.1]] · Digest
- 2024-11-05 · <span class="tl-product tl-p11">**Dify**</span> · [[Changes/Dify/2024-11-05-chore-mount-config-file-of-sandbox-by-hjlarry-in-https-github-com-langgenius-dif|chore: mount config file of sandbox]] · Change

**2024-10**

- 2024-10-26 · <span class="tl-product tl-p26">**Open WebUI**</span> · [[Changes/Open WebUI/2024-10-26-strict-transport-security-crash-resolved-a-crash-when-setting-the-strict-transpo|🔒 Strict-Transport-Security Crash]] · Change
- 2024-10-23 · <span class="tl-product tl-p11">**Dify**</span> · [[Changes/Dify/2024-10-23-nltk-security-issue-and-upgrade-unstructured-by-johnjyong-in-https-github-com-la|nltk security issue and upgrade unstructured]] · Change
- 2024-10-21 · <span class="tl-product tl-p11">**Dify**</span> · [[Changes/Dify/2024-10-21-update-dify-sandbox-version-to-0-2-10-by-hexian2001-in-https-github-com-langgeni|Update dify-sandbox version to 0.2.10]] · Change
- 2024-10-17 · <span class="tl-product tl-p29">**OpenHands**</span> · [[Changes/OpenHands/2024-10-17-add-modal-sandbox-support-as-a-new-runtime-by-pawalt-in-https-github-com-all-han|Add Modal sandbox support as a new runtime]] · Change
- 2024-10-14 · <span class="tl-product tl-p11">**Dify**</span> · [[Changes/Dify/2024-10-14-2-safety-and-privacy-changes-in-0-9-2|2 Safety and Privacy changes in 0.9.2]] · Digest
- 2024-10-09 · <span class="tl-product tl-p8">**Cursor**</span> · [[Changes/Cursor/2024-10-09-update-0-42-1-0-42-5-fixes-the-following-upstream-security-issue-cve-2024-43601|UPDATE (0.42.1 - 0.42.5): Fixes the following upstream security issue: CVE-2024-43601]] · Change

**2024-09**

- 2024-09-24 · <span class="tl-product tl-p26">**Open WebUI**</span> · [[Changes/Open WebUI/2024-09-24-2-safety-and-privacy-changes-in-v0-3-24|2 Safety and Privacy changes in v0.3.24]] · Digest
- 2024-09-20 · <span class="tl-product tl-p11">**Dify**</span> · [[Changes/Dify/2024-09-20-validate-user-permission-before-enter-app-detail-page-by-douxc-in-https-github-c|validate user permission before enter app detail page]] · Change
- 2024-09-19 · <span class="tl-product tl-p26">**Open WebUI**</span> · [[Changes/Open WebUI/2024-09-19-secure-response-headers-implemented-security-response-headers-bolstering-web-app|🔗 Secure Response Headers]] · Change
- 2024-09-17 · <span class="tl-product tl-p8">**Cursor**</span> · [[Changes/Cursor/2024-09-17-this-update-fixes-the-following-security-issue-cve-2024-45599|This update fixes the following security issue: CVE-2024-45599]] · Change
- 2024-09-12 · <span class="tl-product tl-p11">**Dify**</span> · [[Changes/Dify/2024-09-12-editors-can-now-create-api-keys-directly-streamlining-the-development-workflow-a|Editors can now create API keys directly, streamlining the development workflow…]] · Change
- 2024-09-10 · <span class="tl-product tl-p11">**Dify**</span> · [[Changes/Dify/2024-09-10-add-dify-sandbox-health-check-in-docker-compose-yaml-8121-by-hwzhuhao-in-https-g|add dify-sandbox health check in docker-compose.yaml (♯8121)]] · Change
- 2024-09-04 · <span class="tl-product tl-p26">**Open WebUI**</span> · [[Changes/Open WebUI/2024-09-04-dependency-updates-updated-several-backend-dependencies-like-aiohttp-authlib-duc|🚧 Dependency Updates]] · Change
- 2024-09-03 · <span class="tl-product tl-p11">**Dify**</span> · [[Changes/Dify/2024-09-03-4-safety-and-privacy-changes-in-0-7-3|4 Safety and Privacy changes in 0.7.3]] · Digest

**2024-08**

- 2024-08-27 · <span class="tl-product tl-p26">**Open WebUI**</span> · [[Changes/Open WebUI/2024-08-27-2-safety-and-privacy-changes-in-v0-3-16|2 Safety and Privacy changes in v0.3.16]] · Digest
- 2024-08-26 · <span class="tl-product tl-p11">**Dify**</span> · [[Changes/Dify/2024-08-26-feat-7134-use-dataset-api-create-a-dataset-with-permission-by-crazywoola-in-http|Feat/7134 use dataset api create a dataset with permission]] · Change
- 2024-08-23 · <span class="tl-product tl-p29">**OpenHands**</span> · [[Changes/OpenHands/2024-08-23-3-safety-and-privacy-changes-in-0-9-0|3 Safety and Privacy changes in 0.9.0]] · Digest
- 2024-08-21 · <span class="tl-product tl-p26">**Open WebUI**</span> · [[Changes/Open WebUI/2024-08-21-security-enhancements-various-security-improvements-implemented-across-the-platf|🛡️ Security Enhancements]] · Change
- 2024-08-19 · <span class="tl-product tl-p11">**Dify**</span> · [[Changes/Dify/2024-08-19-2-safety-and-privacy-changes-in-0-7-1|2 Safety and Privacy changes in 0.7.1]] · Digest
- 2024-08-07 · <span class="tl-product tl-p26">**Open WebUI**</span> · [[Changes/Open WebUI/2024-08-07-2-safety-and-privacy-changes-in-v0-3-12|2 Safety and Privacy changes in v0.3.12]] · Digest
- 2024-08-06 · <span class="tl-product tl-p11">**Dify**</span> · [[Changes/Dify/2024-08-06-3-safety-and-privacy-changes-in-0-6-16|3 Safety and Privacy changes in 0.6.16]] · Digest
- 2024-08-01 · <span class="tl-product tl-p29">**OpenHands**</span> · [[Changes/OpenHands/2024-08-01-2-safety-and-privacy-changes-in-0-8-3|2 Safety and Privacy changes in 0.8.3]] · Digest

**2024-07**

- 2024-07-31 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2024-07-31-resolved-permission-issues-when-using-docker-run-user-xxx|Resolved permission issues when using docker run --user xxx]] · Change
- 2024-07-27 · <span class="tl-product tl-p29">**OpenHands**</span> · [[Changes/OpenHands/2024-07-27-fix-update-swebenchsshbox-after-global-config-was-removed-from-sandbox-by-rajwor|FIX Update SWEBenchSSHBox after global config was removed…]] · Change
- 2024-07-26 · <span class="tl-product tl-p2">**AnythingLLM**</span> · [[Changes/AnythingLLM/2024-07-26-3-safety-and-privacy-changes-in-v1-0-0|3 Safety and Privacy changes in v1.0.0]] · Digest
- 2024-07-19 · <span class="tl-product tl-p29">**OpenHands**</span> · [[Changes/OpenHands/2024-07-19-2-safety-and-privacy-changes-in-0-8-1|2 Safety and Privacy changes in 0.8.1]] · Digest
- 2024-07-13 · <span class="tl-product tl-p29">**OpenHands**</span> · [[Changes/OpenHands/2024-07-13-6-safety-and-privacy-changes-in-0-8-0|6 Safety and Privacy changes in 0.8.0]] · Digest
- 2024-07-08 · <span class="tl-product tl-p11">**Dify**</span> · [[Changes/Dify/2024-07-08-2-safety-and-privacy-changes-in-0-6-13|2 Safety and Privacy changes in 0.6.13]] · Digest
- 2024-07-05 · <span class="tl-product tl-p29">**OpenHands**</span> · [[Changes/OpenHands/2024-07-05-2-safety-and-privacy-changes-in-0-7-1|2 Safety and Privacy changes in 0.7.1]] · Digest

**2024-06**

- 2024-06-30 · <span class="tl-product tl-p26">**Open WebUI**</span> · [[Changes/Open WebUI/2024-06-30-dependency-update-upgraded-authlib-from-version-1-3-0-to-1-3-1-to-ensure-better|📦 Dependency Update]] · Change
- 2024-06-29 · <span class="tl-product tl-p29">**OpenHands**</span> · [[Changes/OpenHands/2024-06-29-12-safety-and-privacy-changes-in-0-7-0|12 Safety and Privacy changes in 0.7.0]] · Digest
- 2024-06-28 · <span class="tl-product tl-p11">**Dify**</span> · [[Changes/Dify/2024-06-28-feat-permission-and-security-fixes-by-chazzhou-in-https-github-com-langgenius-di|feat: permission and security fixes]] · Change
- 2024-06-27 · <span class="tl-product tl-p26">**Open WebUI**</span> · [[Changes/Open WebUI/2024-06-27-2-safety-and-privacy-changes-in-v0-3-6|2 Safety and Privacy changes in v0.3.6]] · Digest
- 2024-06-14 · <span class="tl-product tl-p11">**Dify**</span> · [[Changes/Dify/2024-06-14-2-safety-and-privacy-changes-in-0-6-11|2 Safety and Privacy changes in 0.6.11]] · Digest
- 2024-06-14 · <span class="tl-product tl-p33">**Runway**</span> · [[Changes/Runway/2024-06-14-creating-a-custom-voice-will-now-require-explicit-user-consent|Voice Verification]] · Change
- 2024-06-12 · <span class="tl-product tl-p26">**Open WebUI**</span> · [[Changes/Open WebUI/2024-06-12-mixed-content-with-https-issue-resolved-a-problem-where-mixed-content-http-and-h|🔒 Mixed Content with HTTPS Issue]] · Change
- 2024-06-04 · <span class="tl-product tl-p11">**Dify**</span> · [[Changes/Dify/2024-06-04-chore-upgrade-sandbox-by-yeuoly-in-https-github-com-langgenius-dify-pull-4839|chore: upgrade sandbox]] · Change
- 2024-06-04 · <span class="tl-product tl-p29">**OpenHands**</span> · [[Changes/OpenHands/2024-06-04-2-safety-and-privacy-changes-in-0-6-1|2 Safety and Privacy changes in 0.6.1]] · Digest

**2024-05**

- 2024-05-13 · <span class="tl-product tl-p11">**Dify**</span> · [[Changes/Dify/2024-05-13-and-we-also-removed-the-need-for-sys-admin-permission-for-the-sandbox-service|And we also removed the need for SYS_ADMIN permission for the sandbox service]] · Change
- 2024-05-09 · <span class="tl-product tl-p11">**Dify**</span> · [[Changes/Dify/2024-05-09-2-safety-and-privacy-changes-in-0-6-7|2 Safety and Privacy changes in 0.6.7]] · Digest
- 2024-05-02 · <span class="tl-product tl-p11">**Dify**</span> · [[Changes/Dify/2024-05-02-2-safety-and-privacy-changes-in-0-6-6|2 Safety and Privacy changes in 0.6.6]] · Digest

**2024-04**

- 2024-04-24 · <span class="tl-product tl-p26">**Open WebUI**</span> · [[Changes/Open WebUI/2024-04-24-2-safety-and-privacy-changes-in-v0-1-121|2 Safety and Privacy changes in v0.1.121]] · Digest
- 2024-04-16 · <span class="tl-product tl-p11">**Dify**</span> · [[Changes/Dify/2024-04-16-2-safety-and-privacy-changes-in-0-6-3|2 Safety and Privacy changes in 0.6.3]] · Digest
- 2024-04-11 · <span class="tl-product tl-p11">**Dify**</span> · [[Changes/Dify/2024-04-11-chore-address-security-alerts-on-braces-escape-and-katex-by-nite-knite-in-https|chore: address security alerts on braces escape and KaTeX]] · Change
- 2024-04-10 · <span class="tl-product tl-p26">**Open WebUI**</span> · [[Changes/Open WebUI/2024-04-10-share-chat-permission-resolved-issue-with-chat-sharing-permissions|🔒 Share Chat Permission: Resolved issue with chat sharing permissions]] · Change
- 2024-04-04 · <span class="tl-product tl-p26">**Open WebUI**</span> · [[Changes/Open WebUI/2024-04-04-security-patches-applied-necessary-security-patches|🔒 Security Patches: Applied necessary security patches]] · Change

**2024-03**

- 2024-03-13 · <span class="tl-product tl-p34">**Superwhisper**</span> · [[Changes/Superwhisper/2024-03-13-if-user-has-completed-onboarding-do-not-continue-prompting-for-accessiblity-perm|If user has completed onboarding, do not continue prompting for accessiblity permission]] · Change

**2024-02**

- 2024-02-28 · <span class="tl-product tl-p11">**Dify**</span> · [[Changes/Dify/2024-02-28-2-safety-and-privacy-changes-in-0-5-7|2 Safety and Privacy changes in 0.5.7]] · Digest

**2024-01**

- 2024-01-10 · <span class="tl-product tl-p31">**Raycast**</span> · [[Changes/Raycast/2024-01-10-grabbing-your-text-selection-is-now-faster-when-accessibility-permission-is-enab|Grabbing your text selection is now faster when accessibility permission is enabled]] · Change

</details>

</details>

<details class="disclosure">
<summary>2023 · 13 entries (Aider 1 · ChatGPT 1 · Cursor 3 · Descript 2 · Dify 1 · Gemini 1 · Notion 2 · Ollama 1 · Raycast 1)</summary>

**2023-12**

- 2023-12-18 · <span class="tl-product tl-p13">**Gemini**</span> · [[Changes/Gemini/2023-12-18-expanding-bard-extensions-to-new-languages|Expanding Bard Extensions to new languages]] · Expansion

**2023-08**

- 2023-08-28 · <span class="tl-product tl-p3">**ChatGPT**</span> · [[Changes/ChatGPT/2023-08-28-today-we-re-launching-chatgpt-enterprise-which-offers-enterprise-grade-security-4958cf|Introducing ChatGPT Enterprise]] · Launch

**2023-04**

- 2023-04-27 · <span class="tl-product tl-p24">**Notion**</span> · [[Changes/Notion/2023-04-27-2-step-verification-a-k-a-2fa-mfa|2-step verification (a.k.a]] · Launch
- 2023-04-27 · <span class="tl-product tl-p24">**Notion**</span> · [[Changes/Notion/2023-04-27-mention-groups|mention groups]] · Launch

<details class="disclosure">
<summary>Fixes, digests and other changes · 9 (Aider 1 · Cursor 3 · Descript 2 · Dify 1 · Ollama 1 · Raycast 1)</summary>

**2023-12**

- 2023-12-05 · <span class="tl-product tl-p9">**Descript**</span> · [[Changes/Descript/2023-12-05-ai-speaker-authorization-has-been-simplified-so-you-can-upload-a-consent-stateme|AI Speaker authorization has been simplified, so you can Upload a consent statement…]] · Change

**2023-11**

- 2023-11-17 · <span class="tl-product tl-p25">**Ollama**</span> · [[Changes/Ollama/2023-11-17-fix-permission-denied-issues-when-running-ollama-create-on-linux|Fix permission denied issues when running ollama create on Linux]] · Change

**2023-10**

- 2023-10-16 · <span class="tl-product tl-p9">**Descript**</span> · [[Changes/Descript/2023-10-16-set-default-privacy-for-published-pages-https-help-descript-com-hc-en-us-article|Set Default Privacy for Published…]] · Change

**2023-08**

- 2023-08-30 · <span class="tl-product tl-p8">**Cursor**</span> · [[Changes/Cursor/2023-08-30-api-key-input-box-is-now-a-password-type|API Key input box is now a password type]] · Change
- 2023-08-15 · <span class="tl-product tl-p11">**Dify**</span> · [[Changes/Dify/2023-08-15-fix-frontend-permission-check-by-matriq-in-https-github-com-langgenius-dify-pull|fix: frontend permission check]] · Fix

**2023-07**

- 2023-07-24 · <span class="tl-product tl-p1">**Aider**</span> · [[Changes/Aider/2023-07-24-encourage-gpt-to-use-language-like-add-files-to-the-chat-to-ask-users-for-permis|Encourage GPT to use language like "add files to the chat" to ask users…]] · Change

**2023-06**

- 2023-06-27 · <span class="tl-product tl-p8">**Cursor**</span> · [[Changes/Cursor/2023-06-27-cursor-is-now-based-on-version-1-79-2-of-vscodium-which-comes-with-security-upda|Cursor is now based on version 1.79.2 of VSCodium, which comes with security updates…]] · Change

**2023-04**

- 2023-04-16 · <span class="tl-product tl-p8">**Cursor**</span> · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]] · Change

**2023-02**

- 2023-02-01 · <span class="tl-product tl-p31">**Raycast**</span> · [[Changes/Raycast/2023-02-01-file-search-the-authorisation-prompt-should-no-longer-appear-after-denying-permi|File Search: The authorisation prompt should no longer appear after denying permissions]] · Change

</details>

</details>

<details class="disclosure" open>
<summary>2022 · 3 entries (Notion 2 · Raycast 1)</summary>

**2022-06**

- 2022-06-29 · <span class="tl-product tl-p24">**Notion**</span> · [[Changes/Notion/2022-06-29-request-access-to-pages|Request access to pages]] · Launch

**2022-02**

- 2022-02-08 · <span class="tl-product tl-p24">**Notion**</span> · [[Changes/Notion/2022-02-08-can-edit-content-permission-level|Can Edit Content permission level]] · Launch

<details class="disclosure">
<summary>Fixes, digests and other changes · 1 (Raycast 1)</summary>

**2022-04**

- 2022-04-06 · <span class="tl-product tl-p31">**Raycast**</span> · [[Changes/Raycast/2022-04-06-app-updater-added-flow-to-help-fix-permission-problems-for-non-root-users-added|App Updater: added flow to help fix permission problems for non-root users, added…]] · Change

</details>

</details>

<details class="disclosure" open>
<summary>2021 · 3 entries (Descript 1 · Notion 1 · Raycast 1)</summary>

**2021-08**

- 2021-08-10 · <span class="tl-product tl-p9">**Descript**</span> · [[Changes/Descript/2021-08-10-soc-2-type-ii-compliance|SOC 2 Type II Compliance]] · Launch

<details class="disclosure">
<summary>Fixes, digests and other changes · 2 (Notion 1 · Raycast 1)</summary>

**2021-08**

- 2021-08-25 · <span class="tl-product tl-p31">**Raycast**</span> · [[Changes/Raycast/2021-08-25-file-search-now-prompts-for-removable-volume-access-permission-if-required-this|File search: Now prompts for "Removable Volume" access permission if required]] · Change

**2021-01**

- 2021-01-27 · <span class="tl-product tl-p24">**Notion**</span> · [[Changes/Notion/2021-01-27-when-troubleshooting-with-notion-s-support-team-you-can-now-grant-and-revoke-con|When troubleshooting with Notion's support team, you can now grant and revoke…]] · Change

</details>

</details>

<details class="disclosure" open>
<summary>2020 · 5 entries (Descript 1 · Notion 1 · Raycast 3)</summary>

**2020-12**

- 2020-12-02 · <span class="tl-product tl-p31">**Raycast**</span> · [[Changes/Raycast/2020-12-02-script-commands-improvements|Script Commands Improvements]] · Launch

**2020-11**

- 2020-11-11 · <span class="tl-product tl-p24">**Notion**</span> · [[Changes/Notion/2020-11-11-flexible-sub-page-permissions|Flexible sub-page permissions 📑]] · Launch

<details class="disclosure">
<summary>Fixes, digests and other changes · 3 (Descript 1 · Raycast 2)</summary>

**2020-12**

- 2020-12-02 · <span class="tl-product tl-p31">**Raycast**</span> · [[Changes/Raycast/2020-12-02-fixed-a-bug-where-permission-windows-appeared-behind-raycast|Fixed a bug where permission windows appeared behind Raycast]] · Fix

**2020-10**

- 2020-10-16 · <span class="tl-product tl-p31">**Raycast**</span> · [[Changes/Raycast/2020-10-16-important-we-changed-permission-scopes-required-to-use-github-so-you-will-be-ask|⚠️ Important: We changed permission scopes required to use GitHub so you will…]] · Change

**2020-07**

- 2020-07-28 · <span class="tl-product tl-p9">**Descript**</span> · [[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke Application Access]] · Change

</details>

</details>

</div>
<!-- chronolog:end -->