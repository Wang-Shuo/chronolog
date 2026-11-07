---
card_id: openclaw-2026-09-08-2eec83
date: '2026-09-08'
description: 'OpenClaw · 2026-09-08 · Apps and Integrations: 23 changes in v2026.9.3
  — Docker setup preserves the ownership of your project files while repairing the…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We
    are announcing experimental support for AI plugins in ChatGPT]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1265
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: apps-integrations
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 0a0c017f71a34fb1fdced7e9f9af3893063c92c5759b89e8fb300ea9cae8e194
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-08-2eec83
  comparison: ''
  date: '2026-09-08'
  description: 'OpenClaw — v2026.9.3: 23 Apps and Integrations changes'
  evidence:
  - quote: Docker setup preserves the ownership of your project files while repairing
      the OpenClaw state that needs to be writable. Packaged plugin dependencies are
      reachable from their Docker installation, and browser-enabled images prepare
      the private cache parent for the non-root runtime user. Operator-mounted cache
      permissions still belong to the operator.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Supported updates rehearse core and plugin changes before activating them,
      then check the installation that actually started. Recovery also keeps a clearer
      distinction between a working restored installation and an update that failed,
      so the result tells you what happened and what still needs attention.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: OpenClaw validates supported core and plugin updates in isolated candidate
      state before switching the running installation. Enabled npm plugin targets
      are checked before downtime, and private plugin copies preserve supported linked
      and workspace dependency layouts so rehearsal can load them against the staged
      host. Incompatible agent stores are rejected before installation changes.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Eligible validation failures can enter a bounded repair using your configured
      model in disposable rehearsal state. The candidate must pass independent validation
      before activation, and changes that require editing your configuration are reported
      for you to resolve. Plugin metadata checks confirm the selected target but do
      not reserve its eventual download.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Final update verification checks service ownership, health, the running
      version and build, plugin activation, channel readiness and HTTP readiness without
      making a model call. A failed check follows the supported repair or rollback
      path, while a healthy restored service is reported as recovery rather than a
      successful update. Verified rollback also avoids starting unnecessary automatic
      triage.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Post-update maintenance runs through the activated CLI. Version-bound official
      plugins follow the selected release, missing untracked official plugins receive
      the matching stable version on their first repair, and explicit pins keep their
      intended selectors.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Eligible interrupted work, follow-ups and attachments can resume after
      an update, while accepted child results wait for their parent to recover. Update
      the Codex plugin with the Gateway for the corresponding work recovery; unknown
      submissions remain unconfirmed, and missing attachment bytes need to be sent
      again.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Source installations build browser assets from the checked-out source and
      can run maintenance from another working directory. Normal source-server updates
      build the runtime, plugins and UI without regenerating developer declarations
      unless requested. Windows MSYS Git paths are normalized at filesystem boundaries
      while revision arguments remain intact.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Paired-node browsers, Chrome MCP existing-session profiles and routes where
      streaming is unavailable continue to use screenshots. Frames remain subject
      to the requesting connection’s access and the browser’s navigation rules.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Browser repaints can reach the panel without waiting for another screenshot.
      Conceptual illustration, not a screenshot. Paired nodes, existing Chrome MCP
      sessions and unavailable streams keep screenshot fallback.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Team Reports brings selected GitHub and Discord activity into a history
      you can browse inside OpenClaw, while session-owned MCP connections can stay
      available between turns. Plugin authors also have several SDK migrations to
      account for, alongside fixes to installation, connected coding agents, and cloud
      worker preparation.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: When installed and enabled, the optional Team Reports plugin collects authenticated
      GitHub activity and explicitly configured Discord sources into daily, weekly,
      and monthly reports. It is disabled by default. Stored history, people timelines,
      calendars, and optional model summaries make it easier to return to what happened
      across a team.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Plugin authors should follow the SDK migration guide when updating execution-policy,
      approval, inbound-media, and session integrations. Execution-policy helpers
      now live under execPolicy in agent-harness-runtime , approval account helpers
      belong to approval-native-runtime , and approval filtering uses the full matchesApprovalRequestFilters
      contract. The retired generic forwarding evaluator has no drop-in replacement.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Use buildChannelInboundMediaPayload for inbound media. The abortAndDrainAgentHarnessRun
      callable and its returned data remain available, but its removed named result
      type must be inferred. MCP prompt adapters return typed prompt results, preserving
      descriptions, roles, and native images for vision-capable models while Code
      Mode retains the original JSON.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Plugin installation stages managed packages before publishing their files,
      preserves exact recovery information, and replaces package manifests atomically
      after builds. Failed deletion leaves a disabled installation available for a
      later retry, while refreshed metadata and SDK modules reach subsequent plugin
      preparation.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Expired plugin-install owners stop deleting copied source files, and recovery
      keeps exact ownership and filesystem checks. Retain reported recovery files
      until the current installation has been checked.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Session-owned MCP servers now remain alive between turns by default. An
      unset or zero idle timeout disables idle eviction; a positive timeout opts into
      it. Reset, deletion, Stop, and shutdown still clean up their servers, and run-owned
      servers still end with their run.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Connected coding agents preserve more of the context around their work,
      including ACP arguments and history, SDK terminal outcomes, replay order, and
      empty client tool results. Successful closes retire their managed delegates,
      while failed closes remain retryable and wait deadlines remain distinct from
      terminal outcomes.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: The system agent can read installed plugin versions, sources, and dependency
      diagnostics directly. Tool assembly continues past a safely reported broken
      factory, preserves the originating tool context across supported backends, and
      avoids repeating plugin eligibility work within a single operation. Read-only
      discovery does not change installation or approval authority.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Fetched files keep readable names through media staging, PDF extraction
      respects global plugin disablement and document allowlists, and HTTP cancellation
      reaches input downloads. Cancellation does not stop a codec that is already
      running.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Plugin setup validates the file it is about to load, and delegated model
      overrides are checked against the destination agent's resolved model. Filesystem
      transfer checks include exact archive entries and their implicit parent directories,
      cloud media access stays with the filesystem owner, and eligible Apple state
      files have unintended extra ACL grants removed within the supported ownership
      rules.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Unrelated Settings saves preserve plugin secret references, sensitive-field
      metadata survives plugin ownership changes, and private Talk route identifiers
      stay out of public configuration and catalog projections. Failed local secret
      lookups explain the problem without disclosing the secret itself.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  - quote: Configuration references are divided into focused pages with familiar anchors
      preserved, and corrected redirects keep older entry points useful. CLI documentation
      searches can limit displayed results, while revised examples explain existing
      command deadlines, approvals, secrets, hooks, diagnostics, and Code Mode output
      helpers.
    source_release: https://docs.openclaw.ai/releases/2026.9.3
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 23-apps-and-integrations-changes-in-v2026-9-3
  source_release: openclaw-2026-09-08-v2026-9-3-dfcfef48
  source_type: openclaw_changelog
  theme: apps-integrations
  title: 23 Apps and Integrations changes in v2026.9.3
  type: change
related_changes:
- '[[Changes/Lovable/2026-09-07-connect-your-app-to-gong|Connect your app to Gong]]'
- '[[Changes/Lovable/2026-09-07-connector-forms-are-split-into-collapsible-sections|Connector
  forms are split into collapsible sections]]'
- '[[Changes/Claude Code/2026-09-08-4-apps-and-integrations-changes-in-v2-1-265|4
  Apps and Integrations changes in v2.1.265]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-08-v2026-9-3-dfcfef48|openclaw-2026-09-08-v2026-9-3-dfcfef48]]'
source_type: openclaw_changelog
theme: apps-integrations
title: 23 Apps and Integrations changes in v2026.9.3
type: change
---

<!-- chronolog:begin region="header" -->
# 23 Apps and Integrations changes in v2026.9.3

**OpenClaw** · 2026-09-08 · [[Themes/apps-integrations|Apps and Integrations]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.3) · from [[Releases/OpenClaw/openclaw-2026-09-08-v2026-9-3-dfcfef48|v2026.9.3]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Docker setup preserves the ownership of your project files while repairing the OpenClaw state that needs to be writable. Packaged plugin dependencies are reachable from their Docker installation, and browser-enabled images prepare the private cache parent for the non-root runtime user. Operator-mounted cache permissions still belong to the operator.

> Supported updates rehearse core and plugin changes before activating them, then check the installation that actually started. Recovery also keeps a clearer distinction between a working restored installation and an update that failed, so the result tells you what happened and what still needs attention.

> OpenClaw validates supported core and plugin updates in isolated candidate state before switching the running installation. Enabled npm plugin targets are checked before downtime, and private plugin copies preserve supported linked and workspace dependency layouts so rehearsal can load them against the staged host. Incompatible agent stores are rejected before installation changes.

> Eligible validation failures can enter a bounded repair using your configured model in disposable rehearsal state. The candidate must pass independent validation before activation, and changes that require editing your configuration are reported for you to resolve. Plugin metadata checks confirm the selected target but do not reserve its eventual download.

> Final update verification checks service ownership, health, the running version and build, plugin activation, channel readiness and HTTP readiness without making a model call. A failed check follows the supported repair or rollback path, while a healthy restored service is reported as recovery rather than a successful update. Verified rollback also avoids starting unnecessary automatic triage.

> Post-update maintenance runs through the activated CLI. Version-bound official plugins follow the selected release, missing untracked official plugins receive the matching stable version on their first repair, and explicit pins keep their intended selectors.

> Eligible interrupted work, follow-ups and attachments can resume after an update, while accepted child results wait for their parent to recover. Update the Codex plugin with the Gateway for the corresponding work recovery; unknown submissions remain unconfirmed, and missing attachment bytes need to be sent again.

> Source installations build browser assets from the checked-out source and can run maintenance from another working directory. Normal source-server updates build the runtime, plugins and UI without regenerating developer declarations unless requested. Windows MSYS Git paths are normalized at filesystem boundaries while revision arguments remain intact.

> Paired-node browsers, Chrome MCP existing-session profiles and routes where streaming is unavailable continue to use screenshots. Frames remain subject to the requesting connection’s access and the browser’s navigation rules.

> Browser repaints can reach the panel without waiting for another screenshot. Conceptual illustration, not a screenshot. Paired nodes, existing Chrome MCP sessions and unavailable streams keep screenshot fallback.

> Team Reports brings selected GitHub and Discord activity into a history you can browse inside OpenClaw, while session-owned MCP connections can stay available between turns. Plugin authors also have several SDK migrations to account for, alongside fixes to installation, connected coding agents, and cloud worker preparation.

> When installed and enabled, the optional Team Reports plugin collects authenticated GitHub activity and explicitly configured Discord sources into daily, weekly, and monthly reports. It is disabled by default. Stored history, people timelines, calendars, and optional model summaries make it easier to return to what happened across a team.

> Plugin authors should follow the SDK migration guide when updating execution-policy, approval, inbound-media, and session integrations. Execution-policy helpers now live under execPolicy in agent-harness-runtime , approval account helpers belong to approval-native-runtime , and approval filtering uses the full matchesApprovalRequestFilters contract. The retired generic forwarding evaluator has no drop-in replacement.

> Use buildChannelInboundMediaPayload for inbound media. The abortAndDrainAgentHarnessRun callable and its returned data remain available, but its removed named result type must be inferred. MCP prompt adapters return typed prompt results, preserving descriptions, roles, and native images for vision-capable models while Code Mode retains the original JSON.

> Plugin installation stages managed packages before publishing their files, preserves exact recovery information, and replaces package manifests atomically after builds. Failed deletion leaves a disabled installation available for a later retry, while refreshed metadata and SDK modules reach subsequent plugin preparation.

> Expired plugin-install owners stop deleting copied source files, and recovery keeps exact ownership and filesystem checks. Retain reported recovery files until the current installation has been checked.

> Session-owned MCP servers now remain alive between turns by default. An unset or zero idle timeout disables idle eviction; a positive timeout opts into it. Reset, deletion, Stop, and shutdown still clean up their servers, and run-owned servers still end with their run.

> Connected coding agents preserve more of the context around their work, including ACP arguments and history, SDK terminal outcomes, replay order, and empty client tool results. Successful closes retire their managed delegates, while failed closes remain retryable and wait deadlines remain distinct from terminal outcomes.

> The system agent can read installed plugin versions, sources, and dependency diagnostics directly. Tool assembly continues past a safely reported broken factory, preserves the originating tool context across supported backends, and avoids repeating plugin eligibility work within a single operation. Read-only discovery does not change installation or approval authority.

> Fetched files keep readable names through media staging, PDF extraction respects global plugin disablement and document allowlists, and HTTP cancellation reaches input downloads. Cancellation does not stop a codec that is already running.

> Plugin setup validates the file it is about to load, and delegated model overrides are checked against the destination agent's resolved model. Filesystem transfer checks include exact archive entries and their implicit parent directories, cloud media access stays with the filesystem owner, and eligible Apple state files have unintended extra ACL grants removed within the supported ownership rules.

> Unrelated Settings saves preserve plugin secret references, sensitive-field metadata survives plugin ownership changes, and private Talk route identifiers stay out of public configuration and catalog projections. Failed local secret lookups explain the problem without disclosing the secret itself.

> Configuration references are divided into focused pages with familiar anchors preserved, and corrected redirects keep older entry points useful. CLI documentation searches can limit displayed results, while revised examples explain existing command deadlines, approvals, secrets, hooks, diagnostics, and Code Mode output helpers.

Source: https://docs.openclaw.ai/releases/2026.9.3
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-09-08-7-automation-and-scheduling-changes-in-v2026-9-3|7 Automation and Scheduling changes in v2026.9.3]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-09-08-10-memory-and-personalization-changes-in-v2026-9-3|10 Memory and Personalization changes in v2026.9.3]] · Memory and Personalization
- [[Changes/OpenClaw/2026-09-08-2-files-and-data-changes-in-v2026-9-3|2 Files and Data changes in v2026.9.3]] · Files and Data
- [[Changes/OpenClaw/2026-09-08-12-context-window-changes-in-v2026-9-3|12 Context Window changes in v2026.9.3]] · Context Window
- [[Changes/OpenClaw/2026-09-08-ordinary-model-changes-now-apply-to-the-current-chat-by-default-including-admini|Ordinary model changes now apply to the current chat by default, including…]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-09-08-10-mobile-and-desktop-changes-in-v2026-9-3|10 Mobile and Desktop changes in v2026.9.3]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-09-08-4-reliability-and-performance-changes-in-v2026-9-3|4 Reliability and Performance changes in v2026.9.3]] · Reliability and Performance
- [[Changes/OpenClaw/2026-09-08-provider-adapters-preserve-initial-anthropic-text-and-thinking-keep-images-with|Provider adapters preserve initial Anthropic text and thinking, keep images…]] · Multimodal Input
- [[Changes/OpenClaw/2026-09-08-8-editor-experience-changes-in-v2026-9-3|8 Editor Experience changes in v2026.9.3]] · Editor Experience
- [[Changes/OpenClaw/2026-09-08-8-voice-and-audio-changes-in-v2026-9-3|8 Voice and Audio changes in v2026.9.3]] · Voice and Audio
- [[Changes/OpenClaw/2026-09-08-15-model-support-changes-in-v2026-9-3|15 Model Support changes in v2026.9.3]] · Model Support
- [[Changes/OpenClaw/2026-09-08-3-search-and-browsing-changes-in-v2026-9-3|3 Search and Browsing changes in v2026.9.3]] · Search and Browsing
- [[Changes/OpenClaw/2026-09-08-16-agent-mode-changes-in-v2026-9-3|16 Agent Mode changes in v2026.9.3]] · Agent Mode
- [[Changes/OpenClaw/2026-09-08-11-interface-experience-changes-in-v2026-9-3|11 Interface Experience changes in v2026.9.3]] · Interface Experience
- [[Changes/OpenClaw/2026-09-08-slack-delivers-valid-structured-sections-intact-even-when-their-accessibility-te|Slack delivers valid structured sections intact even when their accessibility text…]] · Accessibility and Localization
- [[Changes/OpenClaw/2026-09-08-4-collaboration-changes-in-v2026-9-3|4 Collaboration changes in v2026.9.3]] · Collaboration
- [[Changes/OpenClaw/2026-09-08-14-safety-and-privacy-changes-in-v2026-9-3|14 Safety and Privacy changes in v2026.9.3]] · Safety and Privacy
- [[Changes/OpenClaw/2026-09-08-4-pricing-model-changes-in-v2026-9-3|4 Pricing Model changes in v2026.9.3]] · Pricing Model
- [[Changes/OpenClaw/2026-09-08-8-account-and-access-changes-in-v2026-9-3|8 Account and Access changes in v2026.9.3]] · Account and Access
- [[Changes/OpenClaw/2026-09-08-22-developer-workflow-changes-in-v2026-9-3|22 Developer Workflow changes in v2026.9.3]] · Developer Workflow
- [[Changes/OpenClaw/2026-09-08-77-other-changes-in-v2026-9-3|77 other changes in v2026.9.3]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Apps and Integrations

- Earlier: 2026-09-08 · Claude Code · [[Changes/Claude Code/2026-09-08-4-apps-and-integrations-changes-in-v2-1-265|4 Apps and Integrations changes in v2.1.265]]
- Later: 2026-09-09 · Claude Code · [[Changes/Claude Code/2026-09-09-claude-tag-added-a-use-a-custom-connector-link-to-the-preset-connection-forms-in|Claude Tag Added a "Use a custom connector" link to the preset connection forms…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-23 · ChatGPT · [[Changes/ChatGPT/2023-03-23-we-are-announcing-experimental-support-for-ai-plugins-in-chatgpt-tools-designed-6b2581|We are announcing experimental support for AI plugins in ChatGPT]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-08-2eec83&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-08-23-apps-and-integrations-changes-in-v2026-9-3.md%0ACard%20ID%3A%20openclaw-2026-09-08-2eec83%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.3%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->