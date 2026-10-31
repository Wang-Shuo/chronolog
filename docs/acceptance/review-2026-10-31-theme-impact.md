# 分类规则修订影响清单（评审 2026-10-31 本周清单 ④）

- 规则改动：`_scripts/themes.yaml` 新增 `context_aliases`（套餐名、平台名只在没有其他主题匹配时计分）与 `memory.resource_sense_products`；`_scripts/extract.py` 中价格匹配不看代码片段、开发工具里的 memory 默认指内存。
- 输入：`docs/acceptance/m3-evidence/support-widget-20261031/collection.json.gz`（2026-10-31 采集）。用 `main` / `552f6ea` 与本分支分别抽取同一输入，逐条比较引文所属卡片的主题。
- 结果：5,196 行引文中 111 行改变主题（ChatGPT 36 / Claude Code 44 / Cursor 31）；没有一行进入待审或 “Other changes”，4 行从待审或 “Other changes” 回到正式主题（含 ChatGPT 2025-01-14 Scheduled tasks）。
- 卡片身份：85 个 card_id 退役、75 个新增（摘要卡组成变化导致；Claude Code 65 个），另有 51 张卡保留 ID 但换主题。退役卡的旧地址没有重定向，会 404（见评审 4.2）。
- 下次生成运行会按新规则重抽并全量对账，这些变化随生成 PR 进入审核。

## 复核结论（2026-10-31，Claude 初判，待人工确认）

- **改对**：内存类引文离开 Memory（Claude Code 12、Cursor 7）；`awk '{print $1}'` 离开 Pricing；ChatGPT study mode 回到 Learning Tools、custom instructions 回到 Memory、MoMo 付款归 Pricing、Scheduled tasks 从待审回到 Automation；以平台名误归 Mobile and Desktop 的界面、性能、语音、模型类条目回到各自主题；Cursor 的 team admins 归 Enterprise。
- **仍不理想但不比原来差**：一部分 Claude Code 条目因 “Code tab” 从 Mobile and Desktop 落到 Editor Experience（“tab” 别名的老问题）；Cursor “Agents also have access to a memory tool…” 识别为产品记忆、不再被当作内存，但所在卡片仍在 Safety and Privacy（未变）。
- **改错（已知）**：ChatGPT 2026-07-09 “If you already use the Codex app, update it…” 从 Mobile and Desktop 变为 Safety and Privacy（“security patches”）；ChatGPT 2026-05-14 “Codex is now available in preview in the ChatGPT mobile app” 从 Mobile and Desktop 变为 Projects and Workspaces。尝试把 “desktop app / mobile app” 设为强别名会造成 6 处新的误判，故未采用；这两条留待 `human_overrides` 实现后人工覆盖（评审本月清单 ⑧）。
- 未处理（不在本周规则范围）：“Account switching on iOS and Android” 仍在 Memory，“Texting your dot” 仍在 Safety，Claude Code auto mode for Max 仍在 Model Support，Cursor Composer 2.5 仍在 Agent Mode。

## 逐条清单

### memory → reliability-performance（19）

| 产品 | 日期 | 引文 |
| --- | --- | --- |
| Cursor | 2026-06-04 | Run correlation: Every send() now carries a platform-generated requestId, exposed on Run and RunResult and persisted across the in-memory, SQLite, and JSONL… |
| Cursor | 2026-04-02 | Large-file diff rendering is now much faster, smoother, and less memory-heavy. |
| Cursor | 2025-10-29 | Increased default memory for TypeScript language server. |
| Cursor | 2025-07-03 | Tab completions are now ~100ms faster, and TTFT has been reduced by 30%. We made this possible by restructuring our memory management system and optimizing d… |
| Cursor | 2025-02-19 | Crashes: Enhanced stability through memory and performance improvements, with additional crash prevention systems in place. |
| Cursor | 2023-09-08 | Better state management - prevents crashes from editor using too much memory |
| Cursor | 2023-09-07 | This should reduce any significant memory issues that users have been experiencing. |
| Claude Code | 2026-10-30 | Improved memory use in long headless and SDK turns that run many subagents: the parent session no longer keeps each subagent's tool results until the turn ends |
| Claude Code | 2026-10-30 | Improved `--resume` speed and memory use on damaged transcripts |
| Claude Code | 2026-10-23 | Improved memory use of non-interactive sessions (`-p`, Agent SDK) during compaction when the transcript file is very large |
| Claude Code | 2026-10-19 | Improved memory use when sending requests in long or resumed conversations |
| Claude Code | 2026-10-14 | Improved memory and disk use when PDFs are @-mentioned: their bytes are no longer kept in the session transcript |
| Claude Code | 2026-10-05 | Changed background sessions waiting on a scheduled wakeup (`/loop`): they are now left running through updates and low memory, where being restarted or shut… |
| Claude Code | 2026-10-01 | Improved handling of large MCP tool results: less memory, smaller session files, and no extra upload to count tokens for results far over the limit |
| Claude Code | 2026-09-28 | Improved startup time and memory use by building only the parts of the settings schema that your settings files actually use |
| Claude Code | 2026-08-18 | Improved the embedded `grep` in native macOS/Linux builds: pathological patterns now fail fast instead of exhausting memory, and `-m N` with `-A/-C` prints c… |
| Claude Code | 2026-08-14 | Added opt-in memory cgroup support for Bash tool commands on Linux (`CLAUDE_CODE_TOOL_MEMORY_LIMIT`) so a runaway build can't stall the session |
| Claude Code | 2026-06-24 | Reduced long-session memory growth from terminal output cache |
| Claude Code | 2026-03-12 | Added actionable suggestions to `/context` command — identifies context-heavy tools, memory bloat, and capacity warnings with specific optimization tips |

### mobile-desktop → interface-experience（8）

| 产品 | 日期 | 引文 |
| --- | --- | --- |
| ChatGPT | 2026-09-08 | Edit and comment. On mobile, open a generated image full-screen to edit it or add comments to tell ChatGPT what you’d like to change.. |
| ChatGPT | 2026-06-08 | Cleaned up logged-out mobile web experience: Logged-out users now see a composer in the middle of the screen to avoid being blocked by popups. The sidebar ha… |
| ChatGPT | 2026-03-26 | To give you more space to view your most critical chats and projects, the sidebar menu is now simplified on iOS and Android. ChatGPT experiences available to… |
| ChatGPT | 2026-02-27 | Sidebar actions on mobile web no longer stick while scrolling |
| ChatGPT | 2026-01-07 | Health appears as a new space in the ChatGPT sidebar. If you ask a health-related question in a regular chat, ChatGPT may also suggest continuing in Health.… |
| ChatGPT | 2025-12-18 | You can now pin chats to the top of your list for quick access to important conversations. Pinned chats are available on iOS, Android, Web, and Atlas. On web… |
| ChatGPT | 2025-05-06 | We've removed the row of individual tool icons from the mobile composer and replaced it with the new sliders‑style icon to open the Skills menu; tapping that… |
| ChatGPT | 2025-05-06 | No tools are deprecated—access is simply consolidated to clear space and reduce on‑screen clutter. |

### mobile-desktop → agent-mode（7）

| 产品 | 日期 | 引文 |
| --- | --- | --- |
| Cursor | 2026-10-06 | You can now see and reply to the local agents running on your computer from the Cursor iOS app. |
| Cursor | 2026-09-02 | Self-hosted workers now support computer use on Linux and Mac. With the right desktop packages, an agent can click, type, take screenshots, and drive the bro… |
| Cursor | 2026-07-29 | On iPhone and iPad, the review screen now covers the full PR: comments, checks, and approvals. Add or change reviewers, read comments, and prompt the agent t… |
| Cursor | 2026-06-29 | Cursor for iOS is now available in public beta on all paid plans. Launch and manage always-on agents from anywhere. |
| Cursor | 2026-06-17 | This release introduces updates to cloud agents in the Agents Window of the Cursor desktop app. |
| Cursor | 2025-09-29 | On Windows, Agent now correctly uses PowerShell. On macOS and Linux, PowerShell will be used if it's set as your default shell. Agent also properly detects t… |
| Claude Code | 2026-10-08 | Changed `claude agents` stopped with its background service (macOS, or Linux without the service installed): running sessions now stop in about a minute unle… |

### mobile-desktop → developer-workflow（6）

| 产品 | 日期 | 引文 |
| --- | --- | --- |
| Claude Code | 2026-10-15 | Improved mods: in VS Code and the desktop and mobile apps, a tree drawn above the question dialog can now hold Markdown and up to 48 rows; the terminal keeps… |
| Claude Code | 2026-09-08 | Added `user.email` and `user.groups` to the telemetry Claude Desktop and Cowork send through a Claude apps gateway, matching terminal sessions |
| Claude Code | 2026-09-04 | [VSCode] Added a hollow ring in the session list for sessions open in a terminal, another VS Code window, or Claude Desktop, so they no longer look closed |
| Claude Code | 2026-01-09 | Improved Option-as-Meta hint on macOS to show terminal-specific instructions for native CSIu terminals like iTerm2, Kitty, and WezTerm |
| Claude Code | 2025-12-19 | Added guidance for macOS users when Alt shortcuts fail due to terminal configuration |
| ChatGPT | 2026-08-25 | Plus and Pro users can ask Work on web, iOS, and Android to respond when a new Gmail message arrives, a Slack channel receives a message, or a GitHub pull re… |

### mobile-desktop → editor-experience（6）

| 产品 | 日期 | 引文 |
| --- | --- | --- |
| Cursor | 2023-12-30 | Cursor is now based on VS Code 1.85.1, which, among other things, includes floating editor windows. Just drag and drop an editor onto your desktop to try it… |
| Claude Code | 2026-10-30 | Added idle compaction to VS Code and Claude Desktop's Code tab: a 200K+ token conversation left idle is summarized, and the summary is used on your next mess… |
| Claude Code | 2026-10-14 | Added support for turning off the attribution block in Claude Desktop's Code tab: set `CLAUDE_CODE_ATTRIBUTION_HEADER=0` in the `env` of a Claude apps gatewa… |
| Claude Code | 2026-10-14 | Changed Claude Desktop's Code tab to apply managed settings when `forceLoginGatewayUrl` names an Anthropic-operated gateway that serves the session's hostnam… |
| Claude Code | 2026-10-09 | Added a `code` key to the Claude apps gateway's `managed.policies[]`: the same settings as `cli`, also applied in Claude Desktop's Code tab; beside `desktop`… |
| Claude Code | 2026-10-09 | Improved Claude Desktop's Code tab behind a Claude apps gateway: when a session can't start, including on a machine not set up for the gateway's `code` setti… |

### mobile-desktop → model-support（6）

| 产品 | 日期 | 引文 |
| --- | --- | --- |
| Claude Code | 2026-09-24 | Improved the Claude Desktop unknown-model error to suggest switching to a different model |
| Claude Code | 2026-09-14 | Added a spinner tip pointing Bedrock, Vertex AI, Foundry and LLM gateway users to the Claude desktop app; the claude.ai desktop app tip now suggests `/deskto… |
| Claude Code | 2026-08-28 | Improved Amazon Bedrock session start under `CLAUDE_CODE_PROVIDER_MANAGED_BY_HOST` (e.g. Claude Desktop): a session given a Bedrock model ID or ARN no longer… |
| ChatGPT | 2026-08-31 | Site tools use WebMCP and require a supported account, model, and webpage. They are available in the built-in desktop browser, not through the Chrome extensi… |
| ChatGPT | 2026-06-18 | Long-press send to choose a model: Android users on paid plans can now long-press the send button to choose a model for a one-off message without changing th… |
| ChatGPT | 2025-06-12 | Upload files and access model selector on mobile |

### mobile-desktop → reliability-performance（6）

| 产品 | 日期 | 引文 |
| --- | --- | --- |
| Claude Code | 2026-04-22 | Native builds on macOS and Linux: the `Glob` and `Grep` tools are replaced by embedded `bfs` and `ugrep` available through the Bash tool — faster searches wi… |
| Claude Code | 2026-03-17 | Faster startup on macOS (~60ms) by reading keychain credentials in parallel with module loading |
| Claude Code | 2026-03-11 | Improved clipboard image pasting performance on macOS |
| ChatGPT | 2025-03-18 | We have been working on a variety of usability and performance improvements and bug fixes across Web, Android, and iOS. Below are a small number of specific… |
| ChatGPT | 2025-02-14 | Improved Android conversation parsing performance. |
| ChatGPT | 2025-02-14 | iOS performance fixes. |

### apps-integrations → developer-workflow（4）

| 产品 | 日期 | 引文 |
| --- | --- | --- |
| Claude Code | 2026-09-28 | Changed `/recap` to decline with a short notice when it arrives relayed from a chat thread (your own included) or from a routine or webhook; typed in the ter… |
| Claude Code | 2026-08-17 | Remote Control: effort picks made on a phone or on claude.ai/code now apply to terminal- and Desktop/VS Code-hosted sessions, and the session publishes its e… |
| Claude Code | 2026-07-17 | Changed Enterprise `forceLoginMethod` to be enforced for VS Code extension, SDK, `setup-token`, and `install-github-app` logins, not just the terminal |
| Claude Code | 2026-05-13 | Added `terminalSequence` field to hook JSON output so hooks can emit desktop notifications, window titles, and bells without a controlling terminal |

### collaboration → agent-mode（4）

| 产品 | 日期 | 引文 |
| --- | --- | --- |
| Cursor | 2026-06-04 | With canvases, agents can create interactive artifacts like dashboards, reports, and internal tools that you can share with your team. |
| Cursor | 2026-05-11 | Mention @Cursor in any Teams channel to delegate a task to a cloud agent or pull information from Cursor into Teams. |
| Cursor | 2026-05-11 | Cursor automatically picks the right repository and model based on your prompt and recent agent activity. It reads the entire thread for context before imple… |
| Claude Code | 2026-08-11 | Removed the outdated note about auto mode sessions costing slightly more from the first-use notice for Pro, Max, and Team plans |

### collaboration → enterprise-admin（4）

| 产品 | 日期 | 引文 |
| --- | --- | --- |
| Cursor | 2026-06-03 | An organization is the top-level container for your company's identity, administration, and membership. It gives admins one place to view and manage their en… |
| Cursor | 2025-07-29 | Allow team admins to configure an extension allowlist |
| Cursor | 2025-03-23 | Enhanced visibility of auto-run controls configured by team admins, clarifying when they are active |
| Cursor | 2024-03-20 | Admin improvements: Team admins can now mark themselves as unpaid users and can see the last time team members used the product. |

### mobile-desktop → learning-tools（4）

| 产品 | 日期 | 引文 |
| --- | --- | --- |
| ChatGPT | 2025-07-29 | Study mode is currently available to users in Free, Plus, Pro, and Teams plans globally and will expand to Edu plans in the coming weeks. Study mode works wi… |
| ChatGPT | 2025-07-29 | Check your understanding with open-ended prompts and feedback. |
| ChatGPT | 2025-07-29 | Work with your materials by referencing images or PDFs you upload. |
| ChatGPT | 2025-07-29 | You can enable study mode at any time by selecting Tools in the prompt window and choosing Study and learn from the drop‑down menu or go to chatgpt.com/study… |

### mobile-desktop → voice（3）

| 产品 | 日期 | 引文 |
| --- | --- | --- |
| ChatGPT | 2026-09-29 | Audio is deleted once your notes are ready and can’t be accessed or replayed. Available in beta in the ChatGPT desktop app on macOS to Pro and Business users… |
| ChatGPT | 2025-08-07 | You can now set an accent color that applies to elements in ChatGPT, including your conversation bubbles, the Voice button, and highlighted text.On web: Clic… |
| ChatGPT | 2023-09-25 | You can now use voice to engage in a back-and-forth conversation with your assistant. Speak with it on the go, request a bedtime story, or settle a dinner ta… |

### collaboration → apps-integrations（2）

| 产品 | 日期 | 引文 |
| --- | --- | --- |
| Cursor | 2026-06-22 | Cursor now shows you a leaderboard of the most popular plugins, skills, and MCPs across your team. |
| Cursor | 2026-06-22 | Add any to your setup with one click from the new Customize page and extend Cursor for your workflow. |

### enterprise-admin → agent-mode（2）

| 产品 | 日期 | 引文 |
| --- | --- | --- |
| Cursor | 2025-10-29 | Launched in beta in 1.7, browser for Agent is now GA. We've added additional support for Enterprise teams to use Browser in 2.0. |
| Cursor | 2025-10-29 | Browser can now be embedded in-editor, including powerful new tools to select elements and forward DOM information to the agent. Learn more about using the b… |

### mobile-desktop → apps-integrations（2）

| 产品 | 日期 | 引文 |
| --- | --- | --- |
| Claude Code | 2026-10-20 | Changed plugins that Claude Desktop mounts by path to no longer keep their `allowed-tools` when your organization's managed settings set `allowManagedPermiss… |
| ChatGPT | 2026-08-21 | Find more useful plugins. Rankings now prioritize plugins people keep using after installation, helping relevant options surface across ChatGPT on web and mo… |

### mobile-desktop → context-window（2）

| 产品 | 日期 | 引文 |
| --- | --- | --- |
| ChatGPT | 2026-08-31 | Bring your browser into Work and Codex. Mention open tabs to use them as context, or ask ChatGPT to complete a browser task from the desktop app. |
| ChatGPT | 2026-08-31 | Side chat is available in Edge, Brave, and Vivaldi. Opera supports tab mentions and browser control, but not side chat. Update the desktop app before setup;… |

### mobile-desktop → safety-privacy（2）

| 产品 | 日期 | 引文 |
| --- | --- | --- |
| ChatGPT | 2026-07-09 | On desktop, Work can use local files and desktop apps with your permission. The built-in browser lets ChatGPT gather information from websites and work with… |
| ChatGPT | 2026-07-09 | If you already use the Codex app, update it as usual to move to the new ChatGPT desktop app. If you use the previous ChatGPT desktop app, follow the prompt i… |

### voice → agent-mode（2）

| 产品 | 日期 | 引文 |
| --- | --- | --- |
| Cursor | 2026-06-29 | Open the Cursor mobile app, choose a repo, and launch an agent the same way you would on the desktop app. Pick any frontier model, describe ideas out loud wi… |
| Cursor | 2026-06-29 | Cloud agents run in isolated virtual machines with full development environments to test, verify, and demo work. Move sessions from local to cloud to keep th… |

### __candidate__ → automation-scheduling（1）

| 产品 | 日期 | 引文 |
| --- | --- | --- |
| ChatGPT | 2025-01-14 | Today we’re rolling out a beta version of tasks—a new way to ask ChatGPT to do things for you at a future time. Whether it's one-time reminders or recurring… |

### apps-integrations → agent-mode（1）

| 产品 | 日期 | 引文 |
| --- | --- | --- |
| Claude Code | 2026-09-23 | Improved the time to resume very long sessions that have been compacted, most noticeably through the Agent SDK and Claude Desktop |

### collaboration → interface-experience（1）

| 产品 | 日期 | 引文 |
| --- | --- | --- |
| Cursor | 2026-07-10 | Combined all remote options—your machines, team pools, and existing remote workspaces—into one searchable Remote Machines menu. |

### collaboration → mobile-desktop（1）

| 产品 | 日期 | 引文 |
| --- | --- | --- |
| ChatGPT | 2026-08-31 | Share your stickers in messaging apps. Download your pack or add it to iMessage or WhatsApp on supported devices. |

### collaboration → safety-privacy（1）

| 产品 | 日期 | 引文 |
| --- | --- | --- |
| Cursor | 2026-10-13 | Starting today, the marketplace is also open to public submissions, so any team building developer tools can publish an app for Origin. |

### enterprise-admin → apps-integrations（1）

| 产品 | 日期 | 引文 |
| --- | --- | --- |
| Cursor | 2026-03-03 | On Teams and Enterprise plans, Admins can now create team marketplaces to share private plugins internally. Go to the settings page to manage and distribute… |

### enterprise-admin → developer-workflow（1）

| 产品 | 日期 | 引文 |
| --- | --- | --- |
| Claude Code | 2026-04-23 | `--from-pr` now accepts GitLab merge-request, Bitbucket pull-request, and GitHub Enterprise PR URLs |

### enterprise-admin → editor-experience（1）

| 产品 | 日期 | 引文 |
| --- | --- | --- |
| Claude Code | 2026-09-18 | [Claude Code on the web] Changed organization environments to open as a read-only summary from the Code tab on Team and Enterprise plans, with editing under… |

### enterprise-admin → memory（1）

| 产品 | 日期 | 引文 |
| --- | --- | --- |
| ChatGPT | 2026-07-15 | We’re increasing the character limit for custom instructions in ChatGPT. Plus, Pro, Enterprise, Business, and Education users can now save up to 5,000 charac… |

### enterprise-admin → pricing-model（1）

| 产品 | 日期 | 引文 |
| --- | --- | --- |
| Claude Code | 2026-09-29 | [Claude Tag] Added direct messages with Claude for members on an Enterprise plan Standard or Usage-Based Chat seat who also have Cowork; a seat that includes… |

### interface-experience → model-support（1）

| 产品 | 日期 | 引文 |
| --- | --- | --- |
| Claude Code | 2026-06-03 | Removed the "Claude in Chrome enabled" and "marketplace installed" startup messages; model auto-updates and the team-onboarding tip now show as quiet notices… |

### mobile-desktop → account-access（1）

| 产品 | 日期 | 引文 |
| --- | --- | --- |
| ChatGPT | 2026-10-20 | Locked chats let you keep selected conversations in your account while hiding them from regular chat history, pinned chats, and search. Open them with your 4… |

### mobile-desktop → memory（1）

| 产品 | 日期 | 引文 |
| --- | --- | --- |
| ChatGPT | 2026-08-20 | Use Computer History in more regions. Computer History is now available in the EEA, Switzerland, and the United Kingdom for Pro users in the ChatGPT desktop… |

### mobile-desktop → pricing-model（1）

| 产品 | 日期 | 引文 |
| --- | --- | --- |
| ChatGPT | 2026-10-21 | You can now use MoMo to pay for ChatGPT Go, Plus, and Pro subscriptions purchased on chatgpt.com in Vietnam.Subscriptions purchased through the iOS or Androi… |

### mobile-desktop → projects-workspaces（1）

| 产品 | 日期 | 引文 |
| --- | --- | --- |
| ChatGPT | 2026-05-14 | Codex is now available in preview in the ChatGPT mobile app, so you can stay connected to active work from your phone while Codex continues running on the co… |

### mobile-desktop → search-browsing（1）

| 产品 | 日期 | 引文 |
| --- | --- | --- |
| ChatGPT | 2026-03-23 | Now, it’s easier to find, reuse, and build on your files over time. When you upload or create a file—whether it’s a PDF, spreadsheet, image, or more—it’s aut… |

### model-support → apps-integrations（1）

| 产品 | 日期 | 引文 |
| --- | --- | --- |
| ChatGPT | 2026-09-29 | This is a limited preview with participating integrations. Using purchased credits requires a separate opt-in. A partner may still charge for its own product… |

### pricing-model → safety-privacy（1）

| 产品 | 日期 | 引文 |
| --- | --- | --- |
| Claude Code | 2026-04-09 | Fixed false Bash permission prompts for `cut -d /`, `paste -d /`, `column -s /`, `awk '{print $1}' file`, and filenames containing `%` |

### uncategorized → context-window（1）

| 产品 | 日期 | 引文 |
| --- | --- | --- |
| Claude Code | 2026-09-03 | Improved the Claude apps gateway on Amazon Bedrock: input tokens for an aborted request are now counted with AWS's free CountTokens API (grant `bedrock:Count… |

### uncategorized → enterprise-admin（1）

| 产品 | 日期 | 引文 |
| --- | --- | --- |
| Cursor | 2026-06-03 | Admins can move users between teams through the dashboard, API, or CSV |

### uncategorized → interface-experience（1）

| 产品 | 日期 | 引文 |
| --- | --- | --- |
| Claude Code | 2026-08-28 | Added a Spend limit bar to `/usage` and a `rate_limits.spend_limit` status line field for developers behind a Claude apps gateway with spend limits |

### uncategorized → model-support（1）

| 产品 | 日期 | 引文 |
| --- | --- | --- |
| Claude Code | 2026-10-08 | Added an optional `models` list to every Claude apps gateway upstream: only the listed models are sent there, on failover too, and one `*` in an entry is a w… |
