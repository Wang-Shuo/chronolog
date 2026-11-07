---
card_id: github-copilot-cli-2026-11-06-3a1c5b
date: '2026-11-06'
description: 'GitHub Copilot CLI · 2026-11-06 · Agent Mode: 34 changes in 1.0.106
  — Show each agent''s selection ID in /agent when multiple agents share a display
  name.'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents,
    new docs]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1219
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: agent-mode
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 46009161ed84b30e19b598807f323979cc9dc501a8e5f92e3acd19ad7d247dbb
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-11-06-3a1c5b
  comparison: ''
  date: '2026-11-06'
  description: 'GitHub Copilot CLI — 1.0.106: 34 Agent Mode changes'
  evidence:
  - quote: Show each agent's selection ID in /agent when multiple agents share a display
      name.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: '`--no-ask-user` and the `askUser` setting now say they remove the `ask_user`
      question form, and that the agent can still ask questions in its replies; they
      no longer say the agent stops asking questions.'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: A message sent while the agent is working that mentions a file or directory
      (`@path`) is no longer rejected with "Submission failed" when an earlier one
      is still waiting.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Warn on stderr when the agent selected with `-p --agent` has frontmatter
      keys Copilot ignores, and log every agent file's warnings
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Auto mode falls back to a valid default when a saved Efficiency preference
      is unavailable.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: ACP mode now honors --agent so the selected agent persona, prompt, and
      tools are applied at startup.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Clicking tool calls in /tasks sub-agent details now expands and collapses
      their output
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: In copilot -p streaming mode, sub-agent replies now print as complete blocks
      instead of interleaving mid-token.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Use explicit --model with custom agents unless the agent requires a specific
      model
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: '`includeCoAuthoredBy: false` is now honored in ACP mode (`copilot --acp`),
      so ACP clients no longer instruct the agent to add a Co-authored-by trailer
      to commits.'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Skill and background-agent timeline entries now show sanitized, readable
      errors and results
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Custom agents that share a built-in agent's name are no longer offered
      to the model as a second agent type, since delegating to that name always runs
      the built-in agent
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Instruction files whose frontmatter is not valid YAML now keep an applyTo
      or paths list and excludeAgent, instead of applying to every file, to none,
      or to an agent they exclude
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: A `!` shell command cancelled after it printed output now shows that output
      once, instead of repeating it above the cancellation message.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: The "Agent finished" desktop notification no longer shows a reply from
      an earlier turn or from another session when a prompt ends without a reply of
      its own, such as a prompt blocked by a hook.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: The "Agent finished" desktop notification now shows inline code such as
      `src/*.ts` as written, keeps spaced-out asterisks such as `2 * 3`, and no longer
      leaves part of a link's address behind when the address contains parentheses.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: In `-p` mode, a sub-agent's streamed reply now ends with a line break,
      so `--silent` no longer prints it and the main agent's answer as one line and
      the default output no longer glues it to the front of the task tool's row.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: In cloud sessions, /chronicle standup now checks local history before reporting
      no recent activity
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Keep the /settings and /agent search carets at the cursor when long queries
      wrap, so no query character is hidden.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Running agents in /workflows now show their current activity in run details.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: When the session folder is deleted mid-session, a `!` shell command now
      says the working directory no longer exists instead of reporting `GenericFailure,
      No such file or directory`.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: /resume <session-id> foregrounds an already running background session
      instead of showing it twice on exit
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Rewind keeps turns where agents edit files above the capture size limit
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Directories added with --add-dir or /add-dir now load skills from .agents/skills
      and .claude/skills, and custom agents from .claude/agents.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Auto mode no longer repeats the same model explanation when routing checks
      keep the model unchanged.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Recall misspelled slash commands with Up to correct them while the agent
      is working
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Subagents respect includeCoAuthoredBy when composing git commit messages.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Prevent generation-check lock timeouts from permanently breaking /tasks
      and subagent interactions in long sessions
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: '@-imports in AGENTS.md, CLAUDE.md and copilot-instructions.md now follow
      Markdown code fence rules, so an import shown inside a nested code example is
      no longer pulled into the instructions and a real import after such an example
      is no longer dropped'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Custom agents that declare `search` or `web` aliases now receive the corresponding
      search and web tools.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Show a warning when a custom agent name conflicts with a built-in delegated
      agent
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Custom agents stay available when runtime updates arrive before the startup
      agent list fetch.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Sub-agents now honor managed bypass-disable policies for /allow-all.
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  - quote: Keep agent selection at startup and resume quiet, with the selected agent
      still shown in the footer
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.106
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 34-agent-mode-changes-in-v1-0-106
  source_release: github-copilot-cli-2026-11-06-v1-0-106-github-435988160-ec5b15d4
  source_type: github_releases
  theme: agent-mode
  title: 34 Agent Mode changes in v1.0.106
  type: change
related_changes:
- '[[Changes/OpenClaw/2026-11-05-4-agent-mode-changes-in-v2026-11-1|4 Agent Mode changes
  in v2026.11.1]]'
- '[[Changes/OpenHands/2026-11-05-2-agent-mode-changes-in-v1-36-0|2 Agent Mode changes
  in v1.36.0]]'
- '[[Changes/Codex CLI/2026-11-06-6-agent-mode-changes-in-rust-v0-167-0|6 Agent Mode
  changes in rust-v0.167.0]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-11-06-v1-0-106-github-435988160-ec5b15d4|github-copilot-cli-2026-11-06-v1-0-106-github-435988160-ec5b15d4]]'
source_type: github_releases
theme: agent-mode
title: 34 Agent Mode changes in v1.0.106
type: change
---

<!-- chronolog:begin region="header" -->
# 34 Agent Mode changes in v1.0.106

**GitHub Copilot CLI** · 2026-11-06 · [[Themes/agent-mode|Agent Mode]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.106) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-11-06-v1-0-106-github-435988160-ec5b15d4|1.0.106]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Show each agent's selection ID in /agent when multiple agents share a display name.

> `--no-ask-user` and the `askUser` setting now say they remove the `ask_user` question form, and that the agent can still ask questions in its replies; they no longer say the agent stops asking questions.

> A message sent while the agent is working that mentions a file or directory (`@path`) is no longer rejected with "Submission failed" when an earlier one is still waiting.

> Warn on stderr when the agent selected with `-p --agent` has frontmatter keys Copilot ignores, and log every agent file's warnings

> Auto mode falls back to a valid default when a saved Efficiency preference is unavailable.

> ACP mode now honors --agent so the selected agent persona, prompt, and tools are applied at startup.

> Clicking tool calls in /tasks sub-agent details now expands and collapses their output

> In copilot -p streaming mode, sub-agent replies now print as complete blocks instead of interleaving mid-token.

> Use explicit --model with custom agents unless the agent requires a specific model

> `includeCoAuthoredBy: false` is now honored in ACP mode (`copilot --acp`), so ACP clients no longer instruct the agent to add a Co-authored-by trailer to commits.

> Skill and background-agent timeline entries now show sanitized, readable errors and results

> Custom agents that share a built-in agent's name are no longer offered to the model as a second agent type, since delegating to that name always runs the built-in agent

> Instruction files whose frontmatter is not valid YAML now keep an applyTo or paths list and excludeAgent, instead of applying to every file, to none, or to an agent they exclude

> A `!` shell command cancelled after it printed output now shows that output once, instead of repeating it above the cancellation message.

> The "Agent finished" desktop notification no longer shows a reply from an earlier turn or from another session when a prompt ends without a reply of its own, such as a prompt blocked by a hook.

> The "Agent finished" desktop notification now shows inline code such as `src/*.ts` as written, keeps spaced-out asterisks such as `2 * 3`, and no longer leaves part of a link's address behind when the address contains parentheses.

> In `-p` mode, a sub-agent's streamed reply now ends with a line break, so `--silent` no longer prints it and the main agent's answer as one line and the default output no longer glues it to the front of the task tool's row.

> In cloud sessions, /chronicle standup now checks local history before reporting no recent activity

> Keep the /settings and /agent search carets at the cursor when long queries wrap, so no query character is hidden.

> Running agents in /workflows now show their current activity in run details.

> When the session folder is deleted mid-session, a `!` shell command now says the working directory no longer exists instead of reporting `GenericFailure, No such file or directory`.

> /resume \<session-id> foregrounds an already running background session instead of showing it twice on exit

> Rewind keeps turns where agents edit files above the capture size limit

> Directories added with --add-dir or /add-dir now load skills from .agents/skills and .claude/skills, and custom agents from .claude/agents.

> Auto mode no longer repeats the same model explanation when routing checks keep the model unchanged.

> Recall misspelled slash commands with Up to correct them while the agent is working

> Subagents respect includeCoAuthoredBy when composing git commit messages.

> Prevent generation-check lock timeouts from permanently breaking /tasks and subagent interactions in long sessions

> @-imports in AGENTS.md, CLAUDE.md and copilot-instructions.md now follow Markdown code fence rules, so an import shown inside a nested code example is no longer pulled into the instructions and a real import after such an example is no longer dropped

> Custom agents that declare `search` or `web` aliases now receive the corresponding search and web tools.

> Show a warning when a custom agent name conflicts with a built-in delegated agent

> Custom agents stay available when runtime updates arrive before the startup agent list fetch.

> Sub-agents now honor managed bypass-disable policies for /allow-all.

> Keep agent selection at startup and resume quiet, with the selected agent still shown in the footer

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.106
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-11-06-4-voice-and-audio-changes-in-v1-0-106|4 Voice and Audio changes in v1.0.106]] · Voice and Audio
- [[Changes/GitHub Copilot CLI/2026-11-06-2-files-and-data-changes-in-v1-0-106|2 Files and Data changes in v1.0.106]] · Files and Data
- [[Changes/GitHub Copilot CLI/2026-11-06-3-reliability-and-performance-changes-in-v1-0-106|3 Reliability and Performance changes in v1.0.106]] · Reliability and Performance
- [[Changes/GitHub Copilot CLI/2026-11-06-10-memory-and-personalization-changes-in-v1-0-106|10 Memory and Personalization changes in v1.0.106]] · Memory and Personalization
- [[Changes/GitHub Copilot CLI/2026-11-06-64-developer-workflow-changes-in-v1-0-106|64 Developer Workflow changes in v1.0.106]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-11-06-34-safety-and-privacy-changes-in-v1-0-106|34 Safety and Privacy changes in v1.0.106]] · Safety and Privacy
- [[Changes/GitHub Copilot CLI/2026-11-06-9-collaboration-changes-in-v1-0-106|9 Collaboration changes in v1.0.106]] · Collaboration
- [[Changes/GitHub Copilot CLI/2026-11-06-8-mobile-and-desktop-changes-in-v1-0-106|8 Mobile and Desktop changes in v1.0.106]] · Mobile and Desktop
- [[Changes/GitHub Copilot CLI/2026-11-06-4-projects-and-workspaces-changes-in-v1-0-106|4 Projects and Workspaces changes in v1.0.106]] · Projects and Workspaces
- [[Changes/GitHub Copilot CLI/2026-11-06-8-accessibility-and-localization-changes-in-v1-0-106|8 Accessibility and Localization changes in v1.0.106]] · Accessibility and Localization
- [[Changes/GitHub Copilot CLI/2026-11-06-17-context-window-changes-in-v1-0-106|17 Context Window changes in v1.0.106]] · Context Window
- [[Changes/GitHub Copilot CLI/2026-11-06-57-editor-experience-changes-in-v1-0-106|57 Editor Experience changes in v1.0.106]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-11-06-33-model-support-changes-in-v1-0-106|33 Model Support changes in v1.0.106]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-11-06-89-apps-and-integrations-changes-in-v1-0-106|89 Apps and Integrations changes in v1.0.106]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-11-06-2-image-generation-changes-in-v1-0-106|2 Image Generation changes in v1.0.106]] · Image Generation
- [[Changes/GitHub Copilot CLI/2026-11-06-42-interface-experience-changes-in-v1-0-106|42 Interface Experience changes in v1.0.106]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-11-06-5-pricing-model-changes-in-v1-0-106|5 Pricing Model changes in v1.0.106]] · Pricing Model
- [[Changes/GitHub Copilot CLI/2026-11-06-in-the-every-schedule-manager-x-now-removes-the-highlighted-schedule-even-after|In the /every schedule manager, x now removes the highlighted schedule even after…]] · Automation and Scheduling
- [[Changes/GitHub Copilot CLI/2026-11-06-23-account-and-access-changes-in-v1-0-106|23 Account and Access changes in v1.0.106]] · Account and Access
- [[Changes/GitHub Copilot CLI/2026-11-06-172-other-changes-in-v1-0-106|172 other changes in v1.0.106]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Agent Mode

- Earlier: 2026-11-06 · Codex CLI · [[Changes/Codex CLI/2026-11-06-6-agent-mode-changes-in-rust-v0-167-0|6 Agent Mode changes in rust-v0.167.0]]
- Later: 2026-11-06 · OpenCode · [[Changes/OpenCode/2026-11-06-2-agent-mode-changes-in-v2-2-6|2 Agent Mode changes in v2.2.6]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-07-06 · Cursor · [[Changes/Cursor/2023-07-06-welcome-to-the-first-nightly-release-it-comes-with-agents-which-we-aren-t-releas|Agents, new docs]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-11-06-3a1c5b&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-11-06-34-agent-mode-changes-in-v1-0-106.md%0ACard%20ID%3A%20github-copilot-cli-2026-11-06-3a1c5b%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.106%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->