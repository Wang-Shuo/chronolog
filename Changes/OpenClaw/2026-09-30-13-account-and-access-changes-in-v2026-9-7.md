---
card_id: openclaw-2026-09-30-2c3a14
date: '2026-09-30'
description: 'OpenClaw · 2026-09-30 · Account and Access: 13 changes in v2026.9.7
  — OpenClaw 2026.9.7 is snappier under load and smoother in long conversations, with
  better…'
diffusion:
  first_in_tracked: "[[Changes/Notion/2020-07-28-sign-into-notion-with-your-apple-id-the-perfect-combination-of-speedy-and-secure|Sign
    into Notion with your Apple ID \U0001F5DD️ The perfect combination of speedy and
    secure]]"
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2255
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 60c0bed38769e8352db835b5ead31f01877544ad267af6f72b57398c56f1e4a6
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-09-30-2c3a14
  comparison: ''
  date: '2026-09-30'
  description: 'OpenClaw — v2026.9.7: 13 Account and Access changes'
  evidence:
  - quote: OpenClaw 2026.9.7 is snappier under load and smoother in long conversations,
      with better update backups and rollback protection, plus fixes for upgrading
      from 2026.9.5. It also adds OpenAI’s Agents API and Sign in with ChatGPT (Beta)
      , alongside better chat on Mac, iPhone and iPad, and help picking up work after
      a restart.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Setup reaches the first question sooner and gives clearer guidance when
      sign-in, pairing, or installation needs attention.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: First-run setup shows detected API keys and tokens again, with clearer
      sign-in choices. Connect & verify checks your credentials and can select the
      agent's model. Device-code sign-in no longer ends early because of OpenClaw's
      shorter timer, though the provider's code can still expire. Custom model addresses
      must use HTTP or HTTPS, and automated LM Studio setup now explains connection
      and model-check failures.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: You can restart your abandoned sign-in for the same provider and setup
      target using the same sign-in method. Use the newest sign-in link. Model verification
      also stops on connection failures without the repeated retries used in ordinary
      chat, so retry setup yourself after a temporary outage clears.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: On shared Gateways with at least two individual profiles, you can edit
      your personal instructions in Profile or through authenticated chat. Individual
      sign-in is required for separate personal files; a shared Owner login edits
      the shared profile. This works in local agent workspaces, with a 4,000-character
      limit and existing prompt limits. Single-user setups still use the main USER.md
      file. Save before closing the browser, and avoid editing the same file elsewhere
      at the same time.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Matrix login and logout fixes prevent account changes from incorrectly
      marking a restarted account as stopped. Authorized reviewers can also use reactions
      on Matrix approval prompts , including prompts restored after a restart.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: This reuses the app's existing permissions. iPhone and iPad, standalone
      browsers and saved non-Primary Tauri connections keep their separate sign-in.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Signing back into the same verified account preserves conversation choices.
      Missing older account selections may still need reconnection or an explicit
      choice. ChatGPT Beta sign-in supports automatic compaction in native Codex,
      but not manual compaction or remote execution; see the setup guide .
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Copilot keeps credentials for different organizations separate during repair,
      refresh, and logout. If an agent relied on another organization's credentials,
      sign in for the intended organization. Newly saved conversations also preserve
      valid encrypted reasoning, and each agent keeps its own Code Mode controls without
      gaining extra tool permissions.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Automatic web search now uses an available xAI sign-in before a Tavily
      key, falling back to Tavily if Grok fails. A provider you selected explicitly
      keeps its existing behavior. Browser connection fixes also preserve supplied
      login credentials and correctly detect Windows browsers installed in paths with
      spaces.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Foreground apps on supported Linux workers can also use host-held model
      API keys without copying the real key to the worker. This needs a supported
      API-key connection and a proxy-compatible app; OAuth and detached apps are unsupported.
      If cleanup fails, check the remote app before reusing the worker. Revoking its
      key access does not stop the app.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Resets that include sessions now remove SQLite conversation history and
      its archives. Check the dry-run first, because the selected scope also removes
      configuration and OAuth credentials. Legacy JSON/JSONL import files remain.
      An incomplete reset reports failure without restoring anything it already deleted.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  - quote: Configured Cloudflare OIDC sign-in now recognizes GitHub identities in
      authenticated custom claims. If optional GitHub details are missing or lookup
      fails, otherwise authorized email sign-in can continue. Existing account conflicts
      still require an administrator to link the email explicitly with users.linkEmail
      ; profiles are not merged automatically.
    source_release: https://docs.openclaw.ai/releases/2026.9.7
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 13-account-and-access-changes-in-v2026-9-7
  source_release: openclaw-2026-09-30-v2026-9-7-3d25d2bd
  source_type: openclaw_changelog
  theme: account-access
  title: 13 Account and Access changes in v2026.9.7
  type: change
related_changes:
- '[[Changes/Windsurf/2026-09-29-sign-in-with-chatgpt-cf599d|Sign in with ChatGPT]]'
- '[[Changes/Cline/2026-09-30-if-a-new-task-fails-cline-sign-in-signing-in-and-submitting-a-revised-prompt-now|If
  a new task fails Cline sign-in, signing in and submitting a revised prompt now…]]'
- '[[Changes/GitHub Copilot CLI/2026-09-30-mcp-oauth-sign-in-to-servers-such-as-datadog-reuses-a-still-valid-cached-token|MCP
  OAuth sign-in to servers such as Datadog reuses a still-valid cached token]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-09-30-v2026-9-7-3d25d2bd|openclaw-2026-09-30-v2026-9-7-3d25d2bd]]'
source_type: openclaw_changelog
theme: account-access
title: 13 Account and Access changes in v2026.9.7
type: change
---

<!-- chronolog:begin region="header" -->
# 13 Account and Access changes in v2026.9.7

**OpenClaw** · 2026-09-30 · [[Themes/account-access|Account and Access]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.9.7) · from [[Releases/OpenClaw/openclaw-2026-09-30-v2026-9-7-3d25d2bd|v2026.9.7]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> OpenClaw 2026.9.7 is snappier under load and smoother in long conversations, with better update backups and rollback protection, plus fixes for upgrading from 2026.9.5. It also adds OpenAI’s Agents API and Sign in with ChatGPT (Beta) , alongside better chat on Mac, iPhone and iPad, and help picking up work after a restart.

> Setup reaches the first question sooner and gives clearer guidance when sign-in, pairing, or installation needs attention.

> First-run setup shows detected API keys and tokens again, with clearer sign-in choices. Connect & verify checks your credentials and can select the agent's model. Device-code sign-in no longer ends early because of OpenClaw's shorter timer, though the provider's code can still expire. Custom model addresses must use HTTP or HTTPS, and automated LM Studio setup now explains connection and model-check failures.

> You can restart your abandoned sign-in for the same provider and setup target using the same sign-in method. Use the newest sign-in link. Model verification also stops on connection failures without the repeated retries used in ordinary chat, so retry setup yourself after a temporary outage clears.

> On shared Gateways with at least two individual profiles, you can edit your personal instructions in Profile or through authenticated chat. Individual sign-in is required for separate personal files; a shared Owner login edits the shared profile. This works in local agent workspaces, with a 4,000-character limit and existing prompt limits. Single-user setups still use the main USER.md file. Save before closing the browser, and avoid editing the same file elsewhere at the same time.

> Matrix login and logout fixes prevent account changes from incorrectly marking a restarted account as stopped. Authorized reviewers can also use reactions on Matrix approval prompts , including prompts restored after a restart.

> This reuses the app's existing permissions. iPhone and iPad, standalone browsers and saved non-Primary Tauri connections keep their separate sign-in.

> Signing back into the same verified account preserves conversation choices. Missing older account selections may still need reconnection or an explicit choice. ChatGPT Beta sign-in supports automatic compaction in native Codex, but not manual compaction or remote execution; see the setup guide .

> Copilot keeps credentials for different organizations separate during repair, refresh, and logout. If an agent relied on another organization's credentials, sign in for the intended organization. Newly saved conversations also preserve valid encrypted reasoning, and each agent keeps its own Code Mode controls without gaining extra tool permissions.

> Automatic web search now uses an available xAI sign-in before a Tavily key, falling back to Tavily if Grok fails. A provider you selected explicitly keeps its existing behavior. Browser connection fixes also preserve supplied login credentials and correctly detect Windows browsers installed in paths with spaces.

> Foreground apps on supported Linux workers can also use host-held model API keys without copying the real key to the worker. This needs a supported API-key connection and a proxy-compatible app; OAuth and detached apps are unsupported. If cleanup fails, check the remote app before reusing the worker. Revoking its key access does not stop the app.

> Resets that include sessions now remove SQLite conversation history and its archives. Check the dry-run first, because the selected scope also removes configuration and OAuth credentials. Legacy JSON/JSONL import files remain. An incomplete reset reports failure without restoring anything it already deleted.

> Configured Cloudflare OIDC sign-in now recognizes GitHub identities in authenticated custom claims. If optional GitHub details are missing or lookup fails, otherwise authorized email sign-in can continue. Existing account conflicts still require an administrator to link the email explicitly with users.linkEmail ; profiles are not merged automatically.

Source: https://docs.openclaw.ai/releases/2026.9.7
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-09-30-4-context-window-changes-in-v2026-9-7|4 Context Window changes in v2026.9.7]] · Context Window
- [[Changes/OpenClaw/2026-09-30-13-developer-workflow-changes-in-v2026-9-7|13 Developer Workflow changes in v2026.9.7]] · Developer Workflow
- [[Changes/OpenClaw/2026-09-30-3-files-and-data-changes-in-v2026-9-7|3 Files and Data changes in v2026.9.7]] · Files and Data
- [[Changes/OpenClaw/2026-09-30-2-enterprise-and-administration-changes-in-v2026-9-7|2 Enterprise and Administration changes in v2026.9.7]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-09-30-15-memory-and-personalization-changes-in-v2026-9-7|15 Memory and Personalization changes in v2026.9.7]] · Memory and Personalization
- [[Changes/OpenClaw/2026-09-30-33-agent-mode-changes-in-v2026-9-7|33 Agent Mode changes in v2026.9.7]] · Agent Mode
- [[Changes/OpenClaw/2026-09-30-17-interface-experience-changes-in-v2026-9-7|17 Interface Experience changes in v2026.9.7]] · Interface Experience
- [[Changes/OpenClaw/2026-09-30-36-apps-and-integrations-changes-in-v2026-9-7|36 Apps and Integrations changes in v2026.9.7]] · Apps and Integrations
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
## Nearby in Account and Access

- Earlier: 2026-09-30 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-09-30-mcp-oauth-sign-in-to-servers-such-as-datadog-reuses-a-still-valid-cached-token|MCP OAuth sign-in to servers such as Datadog reuses a still-valid cached token]]
- Later: 2026-10-01 · Claude Code · [[Changes/Claude Code/2026-10-01-added-url-prompts-from-mcp-servers-on-the-2025-11-25-protocol-for-example-to-sig|Added URL prompts from MCP servers on the 2025-11-25 protocol, for example to sign in]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Notion · [[Changes/Notion/2020-07-28-sign-into-notion-with-your-apple-id-the-perfect-combination-of-speedy-and-secure|Sign into Notion with your Apple ID 🗝️ The perfect combination of speedy and secure]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-09-30-2c3a14&body=Card%3A%20Changes%2FOpenClaw%2F2026-09-30-13-account-and-access-changes-in-v2026-9-7.md%0ACard%20ID%3A%20openclaw-2026-09-30-2c3a14%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.9.7%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->