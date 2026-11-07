---
card_id: openclaw-2026-09-03-44cbab
date: '2026-09-03'
description: 'OpenClaw · 2026-09-03 · Account and Access: 12 changes in v2026.9.1
  — Accessibility and authority state are clearer in several places, including a stable…'
diffusion:
  first_in_tracked: "[[Changes/Notion/2020-07-28-sign-into-notion-with-your-apple-id-the-perfect-combination-of-speedy-and-secure|Sign
    into Notion with your Apple ID \U0001F5DD️ The perfect combination of speedy and
    secure]]"
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2228
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 5149dbb7893c38d08e085e5c96d3db7739d3084e1f6485eb37e521a6f180479c
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-03-44cbab
  comparison: ''
  date: '2026-09-03'
  description: 'OpenClaw — v2026.9.1: 12 Account and Access changes'
  evidence:
  - quote: Accessibility and authority state are clearer in several places, including
      a stable localized name for the composer, reduced-motion loading indicators,
      properly displayed wildcard tool policies, named approval requesters, optionless
      credential prompts, and specific recovery guidance for trusted-proxy sign-in
      failures. One regression remains in the sidebar. Shorter pin and unpin tooltips
      also became the icon buttons' accessible names, so assistive-technology users
      can lose the session-specific context that used to be repeated there.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: iOS now explains whether a model choice changes the current session, the
      agent default, or the global default, and it blocks unavailable choices or permanent
      authentication failures before a live send while still allowing offline queueing
      and temporary cooldowns. Localization coverage catches more dynamic macOS text
      and newer Apple controls, while a revoked or replaced Watch connection can no
      longer receive another command or submit a late result through the retired connection.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Remote and supervised work recovers in a few narrower places as well. Paired-node
      Claude runs can fall back to the node’s native Claude login when forwarded credentials
      are blank, SSH worker desktops avoid Unix-socket failures caused by long temporary
      paths, and completed Windows worker turns close their owned state before removing
      the runtime directory so the slot can be reclaimed normally.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: The recovery path is less mysterious too. OpenAI relogin can repair stale
      profile order, Doctor preserves custom-provider environment references instead
      of turning them into broken stored keys, forced login clears the credential
      owner it is meant to replace, and a changed provider priority reaches a running
      Gateway. Google and Vertex configuration can also restore their bundled provider
      plugin through restrictive allowlists, while read-only catalog work and GitHub
      Copilot authentication avoid loading discovery or agent-runtime work they cannot
      use.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Provider status now has one genuinely useful addition for xAI users, with
      OAuth-authenticated SuperGrok accounts able to show usage, reset time, plan,
      and prepaid balance in the usual status surfaces when xAI supplies them. API-key
      billing remains a separate bucket. DeepInfra and Anthropic Vertex estimates
      also follow their current advertised and regional rates more closely, but these
      are OpenClaw estimates rather than a change to what either provider bills.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Claude CLI setup now works through supported mise and asdf shims, local
      Claude failures keep bounded credential-redacted diagnostics, and Claude CLI-backed
      utility models can produce digests, progress, and tool titles through the runtime
      that owns their authentication. Codex and CLI agents only offer remote shell
      execution when a connected node can actually run commands, existing broken harnesses
      explain which plugin needs attention, and the official plugin now aligns managed
      installs and checks on Codex 0.152.1. Claude Code session catalogs also avoid
      rescanning an unchanged projects tree on every poll, with the improvement depending
      on the size of the catalog, disk load, and watcher availability.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Multi-agent operators can select the intended agent for channel add, channel-specific
      capabilities, login, logout, remove, and resolve, with that workspace retained
      while OpenClaw discovers, installs, or reloads the channel plugin. The existing
      System Agent, sole-agent, and legacy-owner rules still apply when no selector
      is supplied, while ambiguous or invalid ownership stops before authentication
      or setup begins.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: OpenClaw can connect to OAuth-enabled Streamable HTTP and SSE MCP servers
      that reject POST requests without a known size, including through openclaw mcp
      probe . The initial authenticated request and one token-refresh retry now reuse
      the same sized payload while changing only the bearer authorization. This does
      not fix the separate in-Gateway path that can send an unexpanded bearer-token
      placeholder.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Configured MCP tools remain available in Codex turns when native tools
      are disabled, with approvals, grants, naming, and cleanup still enforced. Requester-scoped
      connections stay alive for the tools that depend on them, alongside the existing
      sized OAuth request and token-refresh behavior.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: GitHub-backed Cloudflare Access and Tailscale sign-in can use the Gateway's
      existing GitHub credential for public profile verification, reducing failures
      caused by the anonymous API quota. Named operator roles are still admitted only
      after identity is verified, and an unavailable verification service now produces
      an accurate retryable error instead of opening a session with no usable scope.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Network-facing integrations now put firmer bounds around work before it
      can crowd out valid traffic. A2A JSON-RPC batches and responses have explicit
      limits, incomplete SMS webhook uploads cannot consume unbounded pre-authentication
      reads, and managed webhook traffic behind a trusted proxy is rate-limited by
      validated client rather than one proxy-wide identity.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  - quote: Several places where the product already had a working route but the documentation
      did not make it obvious are now clearer. Supported /login aliases, SecretRef
      defaults, TaskFlow audit warnings, uv-managed Python execution, and dead-letter
      recovery commands are documented where people look for them, retired pages lead
      to current migration guidance, and the Lite Mode Showcase link reaches the actual
      skill. Translation handling is less likely to strand localized pages on protected
      placeholders, while the expanded v2026.8.2 page is easier to navigate by topic
      and remains historical documentation.
    source_release: https://docs.openclaw.ai/releases/2026.9.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 12-account-and-access-changes-in-v2026-9-1
  source_release: openclaw-2026-09-03-v2026-9-1-281124fc
  source_type: openclaw_changelog
  theme: account-access
  title: 12 Account and Access changes in v2026.9.1
  type: change
related_changes:
- '[[Changes/OpenCode/2026-09-01-azure-cli-sign-in-now-asks-for-the-resource-name-directly-instead-of-querying-az|Azure
  CLI sign-in now asks for the resource name directly instead of querying Azure…]]'
- '[[Changes/Cline/2026-09-02-2-account-and-access-changes-in-v4-1-17|2 Account and
  Access changes in v4.1.17]]'
- '[[Changes/Codex CLI/2026-09-03-42128-https-github-com-openai-codex-pull-42128-prepare-mcp-connections-for-coord|♯42128((source
  link) Prepare MCP connections…]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-03-v2026-9-1-281124fc|openclaw-2026-09-03-v2026-9-1-281124fc]]'
source_type: openclaw_changelog
theme: account-access
title: 12 Account and Access changes in v2026.9.1
type: change
---

<!-- chronolog:begin region="header" -->
# 12 Account and Access changes in v2026.9.1

**OpenClaw** · 2026-09-03 · [[Themes/account-access|Account and Access]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.1) · from [[Releases/OpenClaw/openclaw-2026-09-03-v2026-9-1-281124fc|v2026.9.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Accessibility and authority state are clearer in several places, including a stable localized name for the composer, reduced-motion loading indicators, properly displayed wildcard tool policies, named approval requesters, optionless credential prompts, and specific recovery guidance for trusted-proxy sign-in failures. One regression remains in the sidebar. Shorter pin and unpin tooltips also became the icon buttons' accessible names, so assistive-technology users can lose the session-specific context that used to be repeated there.

> iOS now explains whether a model choice changes the current session, the agent default, or the global default, and it blocks unavailable choices or permanent authentication failures before a live send while still allowing offline queueing and temporary cooldowns. Localization coverage catches more dynamic macOS text and newer Apple controls, while a revoked or replaced Watch connection can no longer receive another command or submit a late result through the retired connection.

> Remote and supervised work recovers in a few narrower places as well. Paired-node Claude runs can fall back to the node’s native Claude login when forwarded credentials are blank, SSH worker desktops avoid Unix-socket failures caused by long temporary paths, and completed Windows worker turns close their owned state before removing the runtime directory so the slot can be reclaimed normally.

> The recovery path is less mysterious too. OpenAI relogin can repair stale profile order, Doctor preserves custom-provider environment references instead of turning them into broken stored keys, forced login clears the credential owner it is meant to replace, and a changed provider priority reaches a running Gateway. Google and Vertex configuration can also restore their bundled provider plugin through restrictive allowlists, while read-only catalog work and GitHub Copilot authentication avoid loading discovery or agent-runtime work they cannot use.

> Provider status now has one genuinely useful addition for xAI users, with OAuth-authenticated SuperGrok accounts able to show usage, reset time, plan, and prepaid balance in the usual status surfaces when xAI supplies them. API-key billing remains a separate bucket. DeepInfra and Anthropic Vertex estimates also follow their current advertised and regional rates more closely, but these are OpenClaw estimates rather than a change to what either provider bills.

> Claude CLI setup now works through supported mise and asdf shims, local Claude failures keep bounded credential-redacted diagnostics, and Claude CLI-backed utility models can produce digests, progress, and tool titles through the runtime that owns their authentication. Codex and CLI agents only offer remote shell execution when a connected node can actually run commands, existing broken harnesses explain which plugin needs attention, and the official plugin now aligns managed installs and checks on Codex 0.152.1. Claude Code session catalogs also avoid rescanning an unchanged projects tree on every poll, with the improvement depending on the size of the catalog, disk load, and watcher availability.

> Multi-agent operators can select the intended agent for channel add, channel-specific capabilities, login, logout, remove, and resolve, with that workspace retained while OpenClaw discovers, installs, or reloads the channel plugin. The existing System Agent, sole-agent, and legacy-owner rules still apply when no selector is supplied, while ambiguous or invalid ownership stops before authentication or setup begins.

> OpenClaw can connect to OAuth-enabled Streamable HTTP and SSE MCP servers that reject POST requests without a known size, including through openclaw mcp probe . The initial authenticated request and one token-refresh retry now reuse the same sized payload while changing only the bearer authorization. This does not fix the separate in-Gateway path that can send an unexpanded bearer-token placeholder.

> Configured MCP tools remain available in Codex turns when native tools are disabled, with approvals, grants, naming, and cleanup still enforced. Requester-scoped connections stay alive for the tools that depend on them, alongside the existing sized OAuth request and token-refresh behavior.

> GitHub-backed Cloudflare Access and Tailscale sign-in can use the Gateway's existing GitHub credential for public profile verification, reducing failures caused by the anonymous API quota. Named operator roles are still admitted only after identity is verified, and an unavailable verification service now produces an accurate retryable error instead of opening a session with no usable scope.

> Network-facing integrations now put firmer bounds around work before it can crowd out valid traffic. A2A JSON-RPC batches and responses have explicit limits, incomplete SMS webhook uploads cannot consume unbounded pre-authentication reads, and managed webhook traffic behind a trusted proxy is rate-limited by validated client rather than one proxy-wide identity.

> Several places where the product already had a working route but the documentation did not make it obvious are now clearer. Supported /login aliases, SecretRef defaults, TaskFlow audit warnings, uv-managed Python execution, and dead-letter recovery commands are documented where people look for them, retired pages lead to current migration guidance, and the Lite Mode Showcase link reaches the actual skill. Translation handling is less likely to strand localized pages on protected placeholders, while the expanded v2026.8.2 page is easier to navigate by topic and remains historical documentation.

Source: https://docs.openclaw.ai/releases/2026.9.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-09-03-14-agent-mode-changes-in-v2026-9-1|14 Agent Mode changes in v2026.9.1]] · Agent Mode
- [[Changes/OpenClaw/2026-09-03-12-voice-and-audio-changes-in-v2026-9-1|12 Voice and Audio changes in v2026.9.1]] · Voice and Audio
- [[Changes/OpenClaw/2026-09-03-2-files-and-data-changes-in-v2026-9-1|2 Files and Data changes in v2026.9.1]] · Files and Data
- [[Changes/OpenClaw/2026-09-03-7-collaboration-changes-in-v2026-9-1|7 Collaboration changes in v2026.9.1]] · Collaboration
- [[Changes/OpenClaw/2026-09-03-10-mobile-and-desktop-changes-in-v2026-9-1|10 Mobile and Desktop changes in v2026.9.1]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-09-03-19-memory-and-personalization-changes-in-v2026-9-1|19 Memory and Personalization changes in v2026.9.1]] · Memory and Personalization
- [[Changes/OpenClaw/2026-09-03-3-editor-experience-changes-in-v2026-9-1|3 Editor Experience changes in v2026.9.1]] · Editor Experience
- [[Changes/OpenClaw/2026-09-03-2-search-and-browsing-changes-in-v2026-9-1|2 Search and Browsing changes in v2026.9.1]] · Search and Browsing
- [[Changes/OpenClaw/2026-09-03-several-less-visible-repairs-keep-the-apps-from-failing-around-dependencies-and|Several less visible repairs keep the apps from failing around dependencies…]] · Multimodal Input
- [[Changes/OpenClaw/2026-09-03-13-automation-and-scheduling-changes-in-v2026-9-1|13 Automation and Scheduling changes in v2026.9.1]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-09-03-an-update-or-doctor-repair-now-does-more-to-preserve-the-setup-you-already-autho|An update or Doctor repair now does more to preserve the setup you already authored…]] · Projects and Workspaces
- [[Changes/OpenClaw/2026-09-03-11-developer-workflow-changes-in-v2026-9-1|11 Developer Workflow changes in v2026.9.1]] · Developer Workflow
- [[Changes/OpenClaw/2026-09-03-3-accessibility-and-localization-changes-in-v2026-9-1|3 Accessibility and Localization changes in v2026.9.1]] · Accessibility and Localization
- [[Changes/OpenClaw/2026-09-03-26-apps-and-integrations-changes-in-v2026-9-1|26 Apps and Integrations changes in v2026.9.1]] · Apps and Integrations
- [[Changes/OpenClaw/2026-09-03-10-safety-and-privacy-changes-in-v2026-9-1|10 Safety and Privacy changes in v2026.9.1]] · Safety and Privacy
- [[Changes/OpenClaw/2026-09-03-11-context-window-changes-in-v2026-9-1|11 Context Window changes in v2026.9.1]] · Context Window
- [[Changes/OpenClaw/2026-09-03-12-model-support-changes-in-v2026-9-1|12 Model Support changes in v2026.9.1]] · Model Support
- [[Changes/OpenClaw/2026-09-03-14-interface-experience-changes-in-v2026-9-1|14 Interface Experience changes in v2026.9.1]] · Interface Experience
- [[Changes/OpenClaw/2026-09-03-on-linux-managed-local-model-and-embedding-services-are-preferred-as-the-out-of|On Linux, managed local model and embedding services are preferred…]] · Reliability and Performance
- [[Changes/OpenClaw/2026-09-03-32-other-changes-in-v2026-9-1|32 other changes in v2026.9.1]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2026-09-03 · Codex CLI · [[Changes/Codex CLI/2026-09-03-42128-https-github-com-openai-codex-pull-42128-prepare-mcp-connections-for-coord|♯42128((source link) Prepare MCP connections…]]
- Later: 2026-09-04 · Claude Code · [[Changes/Claude Code/2026-09-04-2-account-and-access-changes-in-v2-1-261|2 Account and Access changes in v2.1.261]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Notion · [[Changes/Notion/2020-07-28-sign-into-notion-with-your-apple-id-the-perfect-combination-of-speedy-and-secure|Sign into Notion with your Apple ID 🗝️ The perfect combination of speedy and secure]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-03-44cbab&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-03-12-account-and-access-changes-in-v2026-9-1.md%0ACard%20ID%3A%20openclaw-2026-09-03-44cbab%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->