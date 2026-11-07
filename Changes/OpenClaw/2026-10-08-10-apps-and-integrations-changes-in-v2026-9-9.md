---
card_id: openclaw-2026-10-08-38c829
date: '2026-10-08'
description: 'OpenClaw · 2026-10-08 · Apps and Integrations: 10 changes in v2026.9.9
  — Package-manager updates. pnpm updates avoid the “not a terminal” failure, and
  optional…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If
    you have a recording with each speaker with a different microphone, or saved…]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2855
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: cdd24cb6704b0bc731c5c27b44353d345889e199a442da7fc427ea1799bbe32d
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-10-08-38c829
  comparison: ''
  date: '2026-10-08'
  description: 'OpenClaw — v2026.9.9: 10 Apps and Integrations changes'
  evidence:
  - quote: 'Package-manager updates. pnpm updates avoid the “not a terminal” failure,
      and optional plugin syntax errors can produce warnings instead of blocking the
      update snapshot. Large npm installs can continue past a scan limit with a warning
      that full package contents are unverified. An older updater may need a manual
      first update or the plugin recovery steps . df11aae by @alkor2000 ; #161001
      , #162298 by @steipete , with reporting by @jamiezigelbaum .'
    source_release: https://docs.openclaw.ai/releases/2026.9.9
  - quote: 'Plugin installation records. An upgrade encountering damaged old plugin
      metadata preserves the original record and its valid installation entries. Already-lost
      data still needs a backup, and a separate unresolved registry-refresh problem
      can overwrite preserved entries; do not use refresh as an assured recovery step.
      #161485 by @steipete , reported by @aniruddhaadak80 .'
    source_release: https://docs.openclaw.ai/releases/2026.9.9
  - quote: 'Cancelling queued messages. If you cancel a message that is still waiting
      to be processed, the reply already in progress can finish instead of getting
      stuck. A separate unresolved issue can let pending plugin work continue while
      you reset or delete the conversation. #164230 by @vincentkoc .'
    source_release: https://docs.openclaw.ai/releases/2026.9.9
  - quote: 'Plugin skills during updates. In source-checkout installations, valid
      plugin skills stay loadable during an update instead of temporarily disappearing
      with hardlink warnings. #165882 by @RomneyDa .'
    source_release: https://docs.openclaw.ai/releases/2026.9.9
  - quote: 'Copilot tool calls. Plugin and MCP tools keep working after the first
      Copilot conversation turn instead of failing with “Async work scope is closed.”
      #164598 by @ericcurtin , with diagnosis by @takyyon .'
    source_release: https://docs.openclaw.ai/releases/2026.9.9
  - quote: 'Model changes and plugin recovery. Switching models can reuse large plugins
      already running instead of copying them again and freezing requests. Failed
      plugin reloads can recover healthy model access and replies without a restart,
      and a missing context-engine plugin can use the built-in fallback . Initial
      loading can still block; unsuccessful recovery still needs a reload or restart.
      #161267 by @obviyus , reported by @cmrstudio56 ; 8abe351 by @sahilsatralkar
      ; #161023 by @Patrick-Erichsen .'
    source_release: https://docs.openclaw.ai/releases/2026.9.9
  - quote: 'Plugins under Bun on macOS. Plugins such as iMessage can load when copying
      a larger dependency hits Bun''s bad-file-descriptor error on macOS. #159403
      by @sunlit-deng , reported by @hannesrudolph , with follow-up work by @steipete
      .'
    source_release: https://docs.openclaw.ai/releases/2026.9.9
  - quote: 'MCP connections. Remote MCP plugins no longer stop native sessions from
      starting because OpenClaw gives them an unnecessary local working directory.
      An HTTP error from an MCP server also avoids the affected Node 26 crash path.
      #162376 by @Patrick-Erichsen ; 66c7c35 by @RvsL .'
    source_release: https://docs.openclaw.ai/releases/2026.9.9
  - quote: 'Bundled MCP connections. MCP servers imported from Claude and Codex bundles
      use the connection type their configuration requests instead of incorrectly
      falling back to another transport. #166200 .'
    source_release: https://docs.openclaw.ai/releases/2026.9.9
  - quote: 'Request checks on paired computers. Plugin input policies can now reject
      a request before OpenClaw carries it out on a paired computer. A policy error
      also blocks the request. These checks cover OpenClaw jobs, not Codex or Copilot,
      and see only the prompt and history available at the Gateway. If a policy needs
      instructions or skill context added on the paired computer, run the job locally
      with a supported runner instead. Blocking a request does not erase text already
      saved in the conversation. #164270 by @steipete .'
    source_release: https://docs.openclaw.ai/releases/2026.9.9
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 10-apps-and-integrations-changes-in-v2026-9-9
  source_release: openclaw-2026-10-08-v2026-9-9-933614cc
  source_type: openclaw_changelog
  theme: apps-integrations
  title: 10 Apps and Integrations changes in v2026.9.9
  type: change
related_changes:
- '[[Changes/Lovable/2026-10-08-app-chat-connectors-zendesk-neon-motherduck-oracle-autonomous-ai-database-ibm-db|App
  + chat connectors]]'
- '[[Changes/Lovable/2026-10-08-chat-connectors-loom|Chat connectors: Loom]]'
- '[[Changes/Ollama/2026-10-08-readme-add-oxi-to-community-integrations-by-maziluiosif-in-https-github-com-olla|README:
  add oxi to community integrations]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-10-08-v2026-9-9-933614cc|openclaw-2026-10-08-v2026-9-9-933614cc]]'
source_type: openclaw_changelog
theme: apps-integrations
title: 10 Apps and Integrations changes in v2026.9.9
type: change
---

<!-- chronolog:begin region="header" -->
# 10 Apps and Integrations changes in v2026.9.9

**OpenClaw** · 2026-10-08 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.9) · from [[Releases/OpenClaw/openclaw-2026-10-08-v2026-9-9-933614cc|v2026.9.9]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Package-manager updates. pnpm updates avoid the “not a terminal” failure, and optional plugin syntax errors can produce warnings instead of blocking the update snapshot. Large npm installs can continue past a scan limit with a warning that full package contents are unverified. An older updater may need a manual first update or the plugin recovery steps . df11aae by @alkor2000 ; #161001 , #162298 by @steipete , with reporting by @jamiezigelbaum .

> Plugin installation records. An upgrade encountering damaged old plugin metadata preserves the original record and its valid installation entries. Already-lost data still needs a backup, and a separate unresolved registry-refresh problem can overwrite preserved entries; do not use refresh as an assured recovery step. #161485 by @steipete , reported by @aniruddhaadak80 .

> Cancelling queued messages. If you cancel a message that is still waiting to be processed, the reply already in progress can finish instead of getting stuck. A separate unresolved issue can let pending plugin work continue while you reset or delete the conversation. #164230 by @vincentkoc .

> Plugin skills during updates. In source-checkout installations, valid plugin skills stay loadable during an update instead of temporarily disappearing with hardlink warnings. #165882 by @RomneyDa .

> Copilot tool calls. Plugin and MCP tools keep working after the first Copilot conversation turn instead of failing with “Async work scope is closed.” #164598 by @ericcurtin , with diagnosis by @takyyon .

> Model changes and plugin recovery. Switching models can reuse large plugins already running instead of copying them again and freezing requests. Failed plugin reloads can recover healthy model access and replies without a restart, and a missing context-engine plugin can use the built-in fallback . Initial loading can still block; unsuccessful recovery still needs a reload or restart. #161267 by @obviyus , reported by @cmrstudio56 ; 8abe351 by @sahilsatralkar ; #161023 by @Patrick-Erichsen .

> Plugins under Bun on macOS. Plugins such as iMessage can load when copying a larger dependency hits Bun's bad-file-descriptor error on macOS. #159403 by @sunlit-deng , reported by @hannesrudolph , with follow-up work by @steipete .

> MCP connections. Remote MCP plugins no longer stop native sessions from starting because OpenClaw gives them an unnecessary local working directory. An HTTP error from an MCP server also avoids the affected Node 26 crash path. #162376 by @Patrick-Erichsen ; 66c7c35 by @RvsL .

> Bundled MCP connections. MCP servers imported from Claude and Codex bundles use the connection type their configuration requests instead of incorrectly falling back to another transport. #166200 .

> Request checks on paired computers. Plugin input policies can now reject a request before OpenClaw carries it out on a paired computer. A policy error also blocks the request. These checks cover OpenClaw jobs, not Codex or Copilot, and see only the prompt and history available at the Gateway. If a policy needs instructions or skill context added on the paired computer, run the job locally with a supported runner instead. Blocking a request does not erase text already saved in the conversation. #164270 by @steipete .

Source: https://docs.openclaw.ai/releases/2026.9.9
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-10-08-4-agent-mode-changes-in-v2026-9-9|4 Agent Mode changes in v2026.9.9]] · Agent Mode
- [[Changes/OpenClaw/2026-10-08-model-retries-and-context-one-shot-model-requests-through-the-gateway-retain-the|Model retries and context]] · Context Window
- [[Changes/OpenClaw/2026-10-08-2-voice-and-audio-changes-in-v2026-9-9|2 Voice and Audio changes in v2026.9.9]] · Voice and Audio
- [[Changes/OpenClaw/2026-10-08-3-developer-workflow-changes-in-v2026-9-9|3 Developer Workflow changes in v2026.9.9]] · Developer Workflow
- [[Changes/OpenClaw/2026-10-08-windows-mxc-sandbox-the-optional-mxc-sandbox-can-start-and-run-tools-on-compatib|Windows MXC sandbox]] · Safety and Privacy
- [[Changes/OpenClaw/2026-10-08-claude-haiku-5-5-you-can-select-haiku-5-5-through-the-anthropic-api-and-claude-c|Claude Haiku 5.5. You can select Haiku 5.5 through the Anthropic API and Claude CLI]] · Pricing Model
- [[Changes/OpenClaw/2026-10-08-4-interface-experience-changes-in-v2026-9-9|4 Interface Experience changes in v2026.9.9]] · Interface Experience
- [[Changes/OpenClaw/2026-10-08-2-account-and-access-changes-in-v2026-9-9|2 Account and Access changes in v2026.9.9]] · Account and Access
- [[Changes/OpenClaw/2026-10-08-2-enterprise-and-administration-changes-in-v2026-9-9|2 Enterprise and Administration changes in v2026.9.9]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-10-08-4-model-support-changes-in-v2026-9-9|4 Model Support changes in v2026.9.9]] · Model Support
- [[Changes/OpenClaw/2026-10-08-3-mobile-and-desktop-changes-in-v2026-9-9|3 Mobile and Desktop changes in v2026.9.9]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-10-08-feishu-attachments-files-sent-with-captions-or-together-in-feishu-lark-posts-rea|Feishu attachments]] · Multimodal Input
- [[Changes/OpenClaw/2026-10-08-2-memory-and-personalization-changes-in-v2026-9-9|2 Memory and Personalization changes in v2026.9.9]] · Memory and Personalization
- [[Changes/OpenClaw/2026-10-08-2-automation-and-scheduling-changes-in-v2026-9-9|2 Automation and Scheduling changes in v2026.9.9]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-10-08-september-database-compatibility-upgrading-from-september-stable-keeps-shared-da|September database compatibility]] · Collaboration
- [[Changes/OpenClaw/2026-10-08-24-other-changes-in-v2026-9-9|24 other changes in v2026.9.9]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-10-08 · Ollama · [[Changes/Ollama/2026-10-08-readme-add-oxi-to-community-integrations-by-maziluiosif-in-https-github-com-olla|README: add oxi to community integrations]]
- Later: 2026-10-08 · OpenHands · [[Changes/OpenHands/2026-10-08-feat-apps-add-authenticated-backend-view-helper-by-neubig-in-https-github-com-op|feat(apps): add authenticated backend view helper]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-12-14 · Descript · [[Changes/Descript/2018-12-14-if-you-have-a-recording-with-each-speaker-with-a-different-microphone-or-saved-a|If you have a recording with each speaker with a different microphone, or saved…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-10-08-38c829&body=Card%3A%20Changes%2FOpenClaw%2F2026-10-08-10-apps-and-integrations-changes-in-v2026-9-9.md%0ACard%20ID%3A%20openclaw-2026-10-08-38c829%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.9%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->