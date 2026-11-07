---
card_id: openclaw-2026-09-30-7db7a9
date: '2026-09-30'
description: 'OpenClaw · 2026-09-30 · Apps and Integrations: 36 changes in v2026.9.7
  — Third-party raw clients must adopt the updated streaming contract , even though
  the…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1287
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 555ffdd9df6cd6b34d6eca0e6ffa39dec19ebc5e8b8bb45512eccaf05a7ca00d
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-30-7db7a9
  comparison: ''
  date: '2026-09-30'
  description: 'OpenClaw — v2026.9.7: 36 Apps and Integrations changes'
  evidence:
  - quote: Third-party raw clients must adopt the updated streaming contract , even
      though the protocol still reports version 4. Custom SDK transports also need
      the documented event-ordering changes. Older clients can lose reply text, and
      reconnect recovery cannot always restore a complete answer.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Installed plugins open directly from command-palette results, and installation
      status stays visible during catalog refreshes. If Plugins Advanced settings
      fail to load after connecting, Reload can try again. Opening a disabled plugin’s
      page does not enable it.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Installed plugin pages now show account and credential setup , with Connect,
      Configure, and Edit actions for supported shared MCP sign-ins and web-search
      or web-fetch credentials. Sign-in requires administrator access, and Connect
      is disabled when browser sign-in is unavailable. Connected and Configured describe
      saved setup, not a live service or working-key check.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: The interface downloads less page-specific content at startup, and automatic
      chat titles wait until the first reply is underway. Diagrams return to Mermaid
      11.17.2, so Mermaid 12-only diagram types and built-in ELK layout are unavailable,
      and some connectors may look different.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: After replacing OpenClaw manually, run openclaw doctor --fix before starting
      it. Existing Task and Flow records are preserved, but some Codex assignments
      need manual migration . Review plugin permissions after Webhooks repair. If
      repair disables plugins or reports conflicting IDs, choose the allowed plugins
      before re-enabling them.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Installations older than June 2026 must upgrade through 2026.9.5 before
      installing the latest version. Make and verify a backup, stop OpenClaw, and
      follow that guide using the same account, profile, and installation paths. Run
      openclaw doctor --fix in 2026.9.5 and resolve import problems before continuing.
      Required plugins and channels must be enabled for their imports. If a newer
      version has already changed your databases, follow the compatible-backup recovery
      steps before downgrading.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Supported POSIX npm updates print a recovery command before replacing OpenClaw.
      If the updater disappears, that command can repair the package and launcher.
      Stop other package managers first, then start OpenClaw and check it after recovery.
      The helper does not restore your data or plugins and does not support Windows,
      pnpm, or Bun update paths.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Headless nodes using the default plugins can now activate a prepared update
      when idle. Nodes running published 2026.9.6 need one manual openclaw update
      followed by openclaw node restart to receive this repair. For foreground nodes,
      stop and restart openclaw node run instead. Follow the node update recovery
      guidance ; running work, plugins that cannot report whether they are idle, and
      database compatibility checks can still defer automatic activation.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Doctor keeps existing plugin files until their replacements are recorded
      and can finish deferred migrations after installing missing plugins. It can
      also repair archive-installed plugin links without the original archive. If
      an older updater hits the affected import.meta error, follow the disable, update,
      and re-enable steps . After an update, run openclaw completion --write-state
      if you want plugin commands included in shell completion.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: After a completed plugin migration, openclaw doctor --fix can clear repeated
      warnings about retained source files by archiving leftover history pointers.
      The imported conversations stay in place, and the archived files remain recoverable.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: On macOS, updates can refresh a recognized old service PATH. This may remove
      ~/bin , ~/.nix-profile/bin , ~/.volta/bin , ~/.asdf/shims , and fnm alias directories
      unless they contain the active runtime. If a CLI tool, MCP server, or skill
      stops finding a command, give it the command's absolute path. Custom PATH settings
      remain protected.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Restarts handle active settings changes and plugin reloads more carefully,
      fixing several shutdown stalls. Clients waiting for results or approvals can
      disconnect and reconnect without cancelling the underlying work. These fixes
      take effect once the new Gateway is running; they cannot change a shutdown already
      handled by an older version.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: The setup guides for Telegram , Feishu , Teams , and Nextcloud Talk cover
      each channel's requirements. Avoid conflicting callback paths and use distinct
      secrets for accounts sharing a route. A Teams path conflict can stop its old
      listener too. On 2026.9.6, separately installed Telegram and Feishu plugins
      need distinct endpoints per account. If Feishu uses old host/port settings,
      update core before explicitly updating a pinned Feishu plugin; updating core
      keeps the pin.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Top-level Slack chats in progress mode now show a temporary reaction followed
      by one final answer. You can keep progress previews through Slack messaging
      settings . Finished cards show that work is complete and link directly to visible
      sessions created for the work, with separate links when there are several.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Administrators can choose Slack reviewers for individual plugins and tools
      . Update the Gateway before adding these settings. Scoped requests go through
      native Slack DMs, so reconnect the bot if that route is unavailable. Choosing
      reviewers does not make a tool ask for approval.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Channel diagnostics show whether a plugin is installed but disabled, and
      expose errors that were missing from channel logs. Rejected status requests
      now report failure to scripts. Chat errors also distinguish recognized local
      timeouts from model-provider failures.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Foreground Claude CLI subagents can work beyond fifteen minutes while they
      continue making progress; silent work still has a timeout. Manual compaction
      keeps the conversation connected, and permitted shell tools keep working after
      a plugin refresh.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Claude CLI turns managed by the local plugin now allow quiet time while
      Claude shortens a long conversation. The overall run deadline still applies,
      and sessions running on a node keep their previous timeout behavior.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Connect Telnyx by installing its official provider with openclaw plugins
      install telnyx , then adding your API key. The Telnyx guide covers setup and
      model selection. The plugin is installed separately, and available models depend
      on your account.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Codex Computer Use works with the replacement plugin and newer Desktop
      app layouts on Mac. Restart the Gateway after updating OpenClaw to load the
      fix. macOS permissions and your existing tool restrictions still apply; custom
      legacy policies may need updating.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: If you disabled the old Computer Use plugin, automatic replacement now
      respects that choice. An owner or authorized administrator can run /codex computer-use
      install explicitly. To restore automatic setup, re-enable the old plugin setting
      as well.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Bun installations no longer need a separate Node installation for the packaged
      Chrome connector or managed-desktop control helper. Custom browser commands
      keep their existing behavior, and Windows extension connections still need node.exe
      .
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Desktops prepared for a cancelled or rejected action are now released when
      the run ends, with cleanup failures reported. Browser activity also avoids pauses
      caused by saving tab records to a busy database. Node shutdown waits for cleanup
      to finish, so a stuck plugin can still block shutdown or an automatic node update
      indefinitely.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Plugin pages now explain what an integration does and how to set it up,
      alongside fixes for plugin updates, cloud sessions, and connected coding agents.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Plugin pages show capabilities, setup guides, and the inputs their tools
      expect, so you can understand an integration before using it. Enabled image,
      video, and music providers also appear under Media. Customize UI is now in Advanced
      settings, with /settings/plugins?tab=advanced available to restore the built-in
      interface. A capability listing does not mean your account is connected or access
      is granted.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: You can install a package without changing whether it is enabled by using
      openclaw plugins install <package> --no-enable . Bun-only installations can
      manage npm plugins without separately installing Node or npm. When an install
      fails, the interface shows whether to retry or check its status first.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Plugin updates can apply supported settings repairs before activation,
      but check migrated listener settings afterward. Data migrations still need openclaw
      doctor --fix , and disabled plugins keep their pending changes. If an older
      updater rejects legacy settings, update OpenClaw itself first. An unconfirmed
      rollback leaves the matching package in place and reports the failure.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Plugin reloads can wait for work already in progress. Use openclaw plugins
      reload <ids...> --wait outside a conversation currently using that plugin to
      wait beyond the usual 60 seconds. Cancelling after the replacement takes effect
      does not undo it. Reload does not rebuild code, and some compiled changes still
      require a restart; browser-only changes can use Reload plugin UI .
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: After a forced stop during startup or plugin reload, OpenClaw can avoid
      an abandoned operation’s five-minute wait once it confirms the old process has
      exited on the same machine. Older operations without that process information
      and package installs still wait for their existing expiry.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Removal stops if settings reference the plugin again. Remove those references
      before retrying. Interrupted removal can leave the plugin disabled with cleanup
      still pending, and files already deleted are not restored.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: OpenClaw keeps loaded native plugin files until it exits, then can reclaim
      retired copies at a later startup. Cleanup of older temporary files can still
      disrupt an older running process if OpenClaw cannot identify it. Plugin authors
      must replace shared temporary roots such as /tmp with a private, user-owned
      directory that others cannot write to, using the existing secure-root helper.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: MCP servers get more time to list their tools, helping slower servers make
      them available in new chats and scheduled runs. Repeated startup failures show
      when to retry instead of making every run wait again. After signing in, tools
      may still take up to ten minutes to reappear unless you explicitly reload MCP
      in the process using it.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Plugin authors can reuse workspace-context helpers and utilities for handling
      models and replies. Plugins using the new exports must declare a compatible
      OpenClaw version through openclaw.compat.pluginApi . Visitor-management tools
      also return usable lists and invitation links in Code Mode. Revoke existing
      visitor grants before changing their configured account, application, or policy.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Hermes migration, LLM Task, and TypeSafe now wait until first use to load
      their execution code, reducing work when those features are available but unused.
      Large plugin tool sets also avoid repeated setup work. When prepared plugins
      cover a turn’s needs, OpenClaw reuses them instead of copying and registering
      them again.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Plugin authors must handle credentials becoming unavailable during reload
      and avoid caching them across reloads. If the managed-secret forwarding worker
      fails, restart the Gateway to restore forwarding.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Doctor preserves compatible POSIX file permissions when moving retired
      TOOLS.md notes into AGENTS.md . If it cannot do so safely, it warns and keeps
      both originals. Fix the permissions or merge the notes manually, because agents
      no longer read TOOLS.md at startup. Cleanup of legacy temporary plugin files
      on macOS and Linux also skips files belonging to another account.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 36-apps-and-integrations-changes-in-v2026-9-7
  source_release: openclaw-2026-09-30-v2026-9-7-3d25d2bd
  source_type: openclaw_changelog
  theme: apps-integrations
  title: 36 Apps and Integrations changes in v2026.9.7
  type: change
related_changes:
- '[[Changes/Lovable/2026-09-29-lovable-mcp-now-works-with-muse-by-meta|Lovable MCP
  now works with Muse by Meta]]'
- '[[Changes/Claude Code/2026-09-30-11-apps-and-integrations-changes-in-v2-1-286|11
  Apps and Integrations changes in v2.1.286]]'
- '[[Changes/GitHub Copilot CLI/2026-09-30-3-apps-and-integrations-changes-in-v1-0-90|3
  Apps and Integrations changes in v1.0.90]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-30-v2026-9-7-3d25d2bd|openclaw-2026-09-30-v2026-9-7-3d25d2bd]]'
source_type: openclaw_changelog
theme: apps-integrations
title: 36 Apps and Integrations changes in v2026.9.7
type: change
---

<!-- chronolog:begin region="header" -->
# 36 Apps and Integrations changes in v2026.9.7

**OpenClaw** · 2026-09-30 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.7) · from [[Releases/OpenClaw/openclaw-2026-09-30-v2026-9-7-3d25d2bd|v2026.9.7]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Third-party raw clients must adopt the updated streaming contract , even though the protocol still reports version 4. Custom SDK transports also need the documented event-ordering changes. Older clients can lose reply text, and reconnect recovery cannot always restore a complete answer.

> Installed plugins open directly from command-palette results, and installation status stays visible during catalog refreshes. If Plugins Advanced settings fail to load after connecting, Reload can try again. Opening a disabled plugin’s page does not enable it.

> Installed plugin pages now show account and credential setup , with Connect, Configure, and Edit actions for supported shared MCP sign-ins and web-search or web-fetch credentials. Sign-in requires administrator access, and Connect is disabled when browser sign-in is unavailable. Connected and Configured describe saved setup, not a live service or working-key check.

> The interface downloads less page-specific content at startup, and automatic chat titles wait until the first reply is underway. Diagrams return to Mermaid 11.17.2, so Mermaid 12-only diagram types and built-in ELK layout are unavailable, and some connectors may look different.

> After replacing OpenClaw manually, run openclaw doctor --fix before starting it. Existing Task and Flow records are preserved, but some Codex assignments need manual migration . Review plugin permissions after Webhooks repair. If repair disables plugins or reports conflicting IDs, choose the allowed plugins before re-enabling them.

> Installations older than June 2026 must upgrade through 2026.9.5 before installing the latest version. Make and verify a backup, stop OpenClaw, and follow that guide using the same account, profile, and installation paths. Run openclaw doctor --fix in 2026.9.5 and resolve import problems before continuing. Required plugins and channels must be enabled for their imports. If a newer version has already changed your databases, follow the compatible-backup recovery steps before downgrading.

> Supported POSIX npm updates print a recovery command before replacing OpenClaw. If the updater disappears, that command can repair the package and launcher. Stop other package managers first, then start OpenClaw and check it after recovery. The helper does not restore your data or plugins and does not support Windows, pnpm, or Bun update paths.

> Headless nodes using the default plugins can now activate a prepared update when idle. Nodes running published 2026.9.6 need one manual openclaw update followed by openclaw node restart to receive this repair. For foreground nodes, stop and restart openclaw node run instead. Follow the node update recovery guidance ; running work, plugins that cannot report whether they are idle, and database compatibility checks can still defer automatic activation.

> Doctor keeps existing plugin files until their replacements are recorded and can finish deferred migrations after installing missing plugins. It can also repair archive-installed plugin links without the original archive. If an older updater hits the affected import.meta error, follow the disable, update, and re-enable steps . After an update, run openclaw completion --write-state if you want plugin commands included in shell completion.

> After a completed plugin migration, openclaw doctor --fix can clear repeated warnings about retained source files by archiving leftover history pointers. The imported conversations stay in place, and the archived files remain recoverable.

> On macOS, updates can refresh a recognized old service PATH. This may remove ~/bin , ~/.nix-profile/bin , ~/.volta/bin , ~/.asdf/shims , and fnm alias directories unless they contain the active runtime. If a CLI tool, MCP server, or skill stops finding a command, give it the command's absolute path. Custom PATH settings remain protected.

> Restarts handle active settings changes and plugin reloads more carefully, fixing several shutdown stalls. Clients waiting for results or approvals can disconnect and reconnect without cancelling the underlying work. These fixes take effect once the new Gateway is running; they cannot change a shutdown already handled by an older version.

> The setup guides for Telegram , Feishu , Teams , and Nextcloud Talk cover each channel's requirements. Avoid conflicting callback paths and use distinct secrets for accounts sharing a route. A Teams path conflict can stop its old listener too. On 2026.9.6, separately installed Telegram and Feishu plugins need distinct endpoints per account. If Feishu uses old host/port settings, update core before explicitly updating a pinned Feishu plugin; updating core keeps the pin.

> Top-level Slack chats in progress mode now show a temporary reaction followed by one final answer. You can keep progress previews through Slack messaging settings . Finished cards show that work is complete and link directly to visible sessions created for the work, with separate links when there are several.

> Administrators can choose Slack reviewers for individual plugins and tools . Update the Gateway before adding these settings. Scoped requests go through native Slack DMs, so reconnect the bot if that route is unavailable. Choosing reviewers does not make a tool ask for approval.

> Channel diagnostics show whether a plugin is installed but disabled, and expose errors that were missing from channel logs. Rejected status requests now report failure to scripts. Chat errors also distinguish recognized local timeouts from model-provider failures.

> Foreground Claude CLI subagents can work beyond fifteen minutes while they continue making progress; silent work still has a timeout. Manual compaction keeps the conversation connected, and permitted shell tools keep working after a plugin refresh.

> Claude CLI turns managed by the local plugin now allow quiet time while Claude shortens a long conversation. The overall run deadline still applies, and sessions running on a node keep their previous timeout behavior.

> Connect Telnyx by installing its official provider with openclaw plugins install telnyx , then adding your API key. The Telnyx guide covers setup and model selection. The plugin is installed separately, and available models depend on your account.

> Codex Computer Use works with the replacement plugin and newer Desktop app layouts on Mac. Restart the Gateway after updating OpenClaw to load the fix. macOS permissions and your existing tool restrictions still apply; custom legacy policies may need updating.

> If you disabled the old Computer Use plugin, automatic replacement now respects that choice. An owner or authorized administrator can run /codex computer-use install explicitly. To restore automatic setup, re-enable the old plugin setting as well.

> Bun installations no longer need a separate Node installation for the packaged Chrome connector or managed-desktop control helper. Custom browser commands keep their existing behavior, and Windows extension connections still need node.exe .

> Desktops prepared for a cancelled or rejected action are now released when the run ends, with cleanup failures reported. Browser activity also avoids pauses caused by saving tab records to a busy database. Node shutdown waits for cleanup to finish, so a stuck plugin can still block shutdown or an automatic node update indefinitely.

> Plugin pages now explain what an integration does and how to set it up, alongside fixes for plugin updates, cloud sessions, and connected coding agents.

> Plugin pages show capabilities, setup guides, and the inputs their tools expect, so you can understand an integration before using it. Enabled image, video, and music providers also appear under Media. Customize UI is now in Advanced settings, with /settings/plugins?tab=advanced available to restore the built-in interface. A capability listing does not mean your account is connected or access is granted.

> You can install a package without changing whether it is enabled by using openclaw plugins install \<package> --no-enable . Bun-only installations can manage npm plugins without separately installing Node or npm. When an install fails, the interface shows whether to retry or check its status first.

> Plugin updates can apply supported settings repairs before activation, but check migrated listener settings afterward. Data migrations still need openclaw doctor --fix , and disabled plugins keep their pending changes. If an older updater rejects legacy settings, update OpenClaw itself first. An unconfirmed rollback leaves the matching package in place and reports the failure.

> Plugin reloads can wait for work already in progress. Use openclaw plugins reload \<ids...> --wait outside a conversation currently using that plugin to wait beyond the usual 60 seconds. Cancelling after the replacement takes effect does not undo it. Reload does not rebuild code, and some compiled changes still require a restart; browser-only changes can use Reload plugin UI .

> After a forced stop during startup or plugin reload, OpenClaw can avoid an abandoned operation’s five-minute wait once it confirms the old process has exited on the same machine. Older operations without that process information and package installs still wait for their existing expiry.

> Removal stops if settings reference the plugin again. Remove those references before retrying. Interrupted removal can leave the plugin disabled with cleanup still pending, and files already deleted are not restored.

> OpenClaw keeps loaded native plugin files until it exits, then can reclaim retired copies at a later startup. Cleanup of older temporary files can still disrupt an older running process if OpenClaw cannot identify it. Plugin authors must replace shared temporary roots such as /tmp with a private, user-owned directory that others cannot write to, using the existing secure-root helper.

> MCP servers get more time to list their tools, helping slower servers make them available in new chats and scheduled runs. Repeated startup failures show when to retry instead of making every run wait again. After signing in, tools may still take up to ten minutes to reappear unless you explicitly reload MCP in the process using it.

> Plugin authors can reuse workspace-context helpers and utilities for handling models and replies. Plugins using the new exports must declare a compatible OpenClaw version through openclaw.compat.pluginApi . Visitor-management tools also return usable lists and invitation links in Code Mode. Revoke existing visitor grants before changing their configured account, application, or policy.

> Hermes migration, LLM Task, and TypeSafe now wait until first use to load their execution code, reducing work when those features are available but unused. Large plugin tool sets also avoid repeated setup work. When prepared plugins cover a turn’s needs, OpenClaw reuses them instead of copying and registering them again.

> Plugin authors must handle credentials becoming unavailable during reload and avoid caching them across reloads. If the managed-secret forwarding worker fails, restart the Gateway to restore forwarding.

> Doctor preserves compatible POSIX file permissions when moving retired TOOLS.md notes into AGENTS.md . If it cannot do so safely, it warns and keeps both originals. Fix the permissions or merge the notes manually, because agents no longer read TOOLS.md at startup. Cleanup of legacy temporary plugin files on macOS and Linux also skips files belonging to another account.

Source: https://docs.openclaw.ai/releases/2026.9.7
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-09-30-4-context-window-changes-in-v2026-9-7|4 Context Window changes in v2026.9.7]] · Context Window
- [[Changes/OpenClaw/2026-09-30-13-developer-workflow-changes-in-v2026-9-7|13 Developer Workflow changes in v2026.9.7]] · Developer Workflow
- [[Changes/OpenClaw/2026-09-30-3-files-and-data-changes-in-v2026-9-7|3 Files and Data changes in v2026.9.7]] · Files and Data
- [[Changes/OpenClaw/2026-09-30-13-account-and-access-changes-in-v2026-9-7|13 Account and Access changes in v2026.9.7]] · Account and Access
- [[Changes/OpenClaw/2026-09-30-2-enterprise-and-administration-changes-in-v2026-9-7|2 Enterprise and Administration changes in v2026.9.7]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-09-30-15-memory-and-personalization-changes-in-v2026-9-7|15 Memory and Personalization changes in v2026.9.7]] · Memory and Personalization
- [[Changes/OpenClaw/2026-09-30-33-agent-mode-changes-in-v2026-9-7|33 Agent Mode changes in v2026.9.7]] · Agent Mode
- [[Changes/OpenClaw/2026-09-30-17-interface-experience-changes-in-v2026-9-7|17 Interface Experience changes in v2026.9.7]] · Interface Experience
- [[Changes/OpenClaw/2026-09-30-2-video-generation-changes-in-v2026-9-7|2 Video Generation changes in v2026.9.7]] · Video Generation
- [[Changes/OpenClaw/2026-09-30-12-voice-and-audio-changes-in-v2026-9-7|12 Voice and Audio changes in v2026.9.7]] · Voice and Audio
- [[Changes/OpenClaw/2026-09-30-21-safety-and-privacy-changes-in-v2026-9-7|21 Safety and Privacy changes in v2026.9.7]] · Safety and Privacy
- [[Changes/OpenClaw/2026-09-30-administrators-can-opt-into-heap-snapshots-to-investigate-memory-growth-a-snapsh|Administrators can opt into heap snapshots to investigate memory growth]] · Reliability and Performance
- [[Changes/OpenClaw/2026-09-30-14-mobile-and-desktop-changes-in-v2026-9-7|14 Mobile and Desktop changes in v2026.9.7]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-09-30-9-editor-experience-changes-in-v2026-9-7|9 Editor Experience changes in v2026.9.7]] · Editor Experience
- [[Changes/OpenClaw/2026-09-30-22-model-support-changes-in-v2026-9-7|22 Model Support changes in v2026.9.7]] · Model Support
- [[Changes/OpenClaw/2026-09-30-11-automation-and-scheduling-changes-in-v2026-9-7|11 Automation and Scheduling changes in v2026.9.7]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-09-30-4-search-and-browsing-changes-in-v2026-9-7|4 Search and Browsing changes in v2026.9.7]] · Search and Browsing
- [[Changes/OpenClaw/2026-09-30-3-pricing-model-changes-in-v2026-9-7|3 Pricing Model changes in v2026.9.7]] · Pricing Model
- [[Changes/OpenClaw/2026-09-30-10-collaboration-changes-in-v2026-9-7|10 Collaboration changes in v2026.9.7]] · Collaboration
- [[Changes/OpenClaw/2026-09-30-4-multimodal-input-changes-in-v2026-9-7|4 Multimodal Input changes in v2026.9.7]] · Multimodal Input
- [[Changes/OpenClaw/2026-09-30-72-other-changes-in-v2026-9-7|72 other changes in v2026.9.7]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-09-30 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-09-30-3-apps-and-integrations-changes-in-v1-0-90|3 Apps and Integrations changes in v1.0.90]]
- Later: 2026-10-01 · Claude Code · [[Changes/Claude Code/2026-10-01-11-apps-and-integrations-changes-in-v2-1-287|11 Apps and Integrations changes in v2.1.287]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-30-7db7a9&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-30-36-apps-and-integrations-changes-in-v2026-9-7.md%0ACard%20ID%3A%20openclaw-2026-09-30-7db7a9%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.7%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->