---
card_id: claude-code-2026-08-28-d13cf6
date: '2026-08-28'
description: 'Claude Code · 2026-08-28 · Mobile and Desktop: Improved Amazon Bedrock
  session start under `CLAUDE_CODE_PROVIDER_MANAGED_BY_HOST` (e.g. Claude Desktop):
  a…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-14-windows-and-linux-support|Windows
    and Linux support 🥳]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1263
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: mobile-desktop
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v5
impact: significant
kind: change
machine_hash: cf61f5fc8c4cb7221da15186d328918f7d330899c6578afefe2767aa98d28411
product: claude-code
product_name: Claude Code
record:
  ai_generated: true
  card_id: claude-code-2026-08-28-d13cf6
  comparison: ''
  confidence: low
  date: '2026-08-28'
  description: 'Claude Code — v2.1.251: Improved Amazon Bedrock session start under
    `CLAUDE_CODE_PROVIDER_MANAGED_BY_HOST` (e.g. Claude Desktop): a session given
    a Bedrock model ID or ARN no longer waits for inference-profile discovery'
  evidence:
  - quote: 'Improved Amazon Bedrock session start under `CLAUDE_CODE_PROVIDER_MANAGED_BY_HOST`
      (e.g. Claude Desktop): a session given a Bedrock model ID or ARN no longer waits
      for inference-profile discovery'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.251
  extractor_version: fallback-v5
  impact: significant
  kind: change
  product: claude-code
  product_name: Claude Code
  slug: improved-amazon-bedrock-session-start-under-claude-code-provider-managed-by-host
  source_release: claude-code-2026-08-28-v2-1-251-github-378586104-42ac2f96
  source_type: github_releases
  theme: mobile-desktop
  theme_matches:
  - matched_terms:
    - desktop
    score: 50
    theme: mobile-desktop
  - matched_terms:
    - model
    score: 50
    theme: model-support
  theme_resolution: manual-semantic-rule-v1
  title: Improved Amazon Bedrock session start under `CLAUDE_CODE_PROVIDER_MANAGED_BY_HOST`…
  type: change
related_changes:
- '[[Changes/Claude Code/2026-08-21-windows-cross-session-messaging-is-now-available-so-claude-code-sessions-across|Windows:
  cross-session messaging is now available, so Claude Code sessions across…]]'
- '[[Changes/ChatGPT/2026-08-25-plus-and-pro-users-can-ask-work-on-web-ios-and-android-to-respond-when-a-new-gma|Create
  webhook-triggered tasks]]'
- '[[Changes/Claude Code/2026-08-25-windows-macos-fixed-headless-sessions-not-cleaning-up-stale-entries-in-claude-se|Windows/macOS:
  Fixed headless sessions not cleaning up stale entries…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-08-28-v2-1-251-github-378586104-42ac2f96|claude-code-2026-08-28-v2-1-251-github-378586104-42ac2f96]]'
source_type: github_releases
theme: mobile-desktop
title: Improved Amazon Bedrock session start under CLAUDE_CODE_PROVIDER_MANAGED_BY_HOST…
type: change
---

<!-- chronolog:begin region="header" -->
# Improved Amazon Bedrock session start under `CLAUDE_CODE_PROVIDER_MANAGED_BY_HOST`…

**Claude Code** · 2026-08-28 · [[Themes/mobile-desktop|Mobile and Desktop]] · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.251) · from [[Releases/Claude Code/claude-code-2026-08-28-v2-1-251-github-378586104-42ac2f96|v2.1.251]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Improved Amazon Bedrock session start under `CLAUDE_CODE_PROVIDER_MANAGED_BY_HOST` (e.g. Claude Desktop): a session given a Bedrock model ID or ARN no longer waits for inference-profile discovery
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.251
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-08-28-changed-analytics-to-no-longer-turn-off-before-sign-in-solely-because-managed-se|Changed analytics to no longer turn off before sign-in solely because managed…]] · Account and Access
- [[Changes/Claude Code/2026-08-28-4-model-support-changes-in-v2-1-251|4 Model Support changes in v2.1.251]] · Model Support
- [[Changes/Claude Code/2026-08-28-added-a-per-session-prompt-cache-line-to-cost-hit-ratio-misses-tokens-re-cached|Added a per-session prompt-cache line to /cost…]] · Pricing Model
- [[Changes/Claude Code/2026-08-28-4-apps-and-integrations-changes-in-v2-1-251|4 Apps and Integrations changes in v2.1.251]] · Apps and Integrations
- [[Changes/Claude Code/2026-08-28-3-developer-workflow-changes-in-v2-1-251|3 Developer Workflow changes in v2.1.251]] · Developer Workflow
- [[Changes/Claude Code/2026-08-28-improved-retry-when-the-model-s-tool-call-is-malformed-the-broken-output-is-now|Improved retry when the model's tool call is malformed]] · Context Window
- [[Changes/Claude Code/2026-08-28-4-agent-mode-changes-in-v2-1-251|4 Agent Mode changes in v2.1.251]] · Agent Mode
- [[Changes/Claude Code/2026-08-28-6-safety-and-privacy-changes-in-v2-1-251|6 Safety and Privacy changes in v2.1.251]] · Safety and Privacy
- [[Changes/Claude Code/2026-08-28-8-other-changes-in-v2-1-251|8 other changes in v2.1.251]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Mobile and Desktop

- Earlier: 2026-08-25 · Claude Code · [[Changes/Claude Code/2026-08-25-windows-macos-fixed-headless-sessions-not-cleaning-up-stale-entries-in-claude-se|Windows/macOS: Fixed headless sessions not cleaning up stale entries…]]
- Later: 2026-08-31 · ChatGPT · [[Changes/ChatGPT/2026-08-31-chatgpt-work-and-codex-can-now-use-tools-that-supported-websites-provide-directl|ChatGPT Work and Codex can now use tools that supported websites provide directly…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-14 · Cursor · [[Changes/Cursor/2023-03-14-windows-and-linux-support|Windows and Linux support 🥳]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-08-28-d13cf6&body=Card%3A%20Changes%2FClaude%20Code%2F2026-08-28-improved-amazon-bedrock-session-start-under-claude-code-provider-managed-by-host.md%0ACard%20ID%3A%20claude-code-2026-08-28-d13cf6%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.251%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->