---
card_id: github-copilot-cli-2026-07-30-0019cf
date: '2026-07-30'
description: 'GitHub Copilot CLI · 2026-07-30 · Safety and Privacy: 5 changes in 1.0.76
  — Sandbox denied paths are enforced for relative and symlinked entries on macOS
  and…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost
    mode for opting out of storing any kind of data on our servers]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1201
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 7694eed27e101d9eee0a4855ea3ddd00387fa074a5b0bbdc1121cd6d2ebc00a2
product: github-copilot-cli
product_name: GitHub Copilot CLI
record:
  card_id: github-copilot-cli-2026-07-30-0019cf
  comparison: ''
  date: '2026-07-30'
  description: 'GitHub Copilot CLI — 1.0.76: 5 Safety and Privacy changes'
  evidence:
  - quote: Sandbox denied paths are enforced for relative and symlinked entries on
      macOS and Linux (Windows cannot deny per path)
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.76
  - quote: URL permission prompts now keep their sandbox-bypass warning and the model's
      reason when a host integration rebuilds the prompt, so an elevated fetch is
      no longer shown as an ordinary one
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.76
  - quote: '`web_fetch` now follows HTTP redirects instead of failing, asking permission
      for the redirect target when it is on a different origin and showing where the
      redirect came from'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.76
  - quote: 'Enterprise administrators can enforce a restrictive sandbox floor: managed
      settings tighten (but never loosen) the user''s sandbox policy, and the `/sandbox`
      dialog surfaces the org-configured managed values with locked fields and managed
      filesystem paths so admins can confirm what is enforced.'
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.76
  - quote: web_fetch routes through the configured sandbox proxy when outbound is
      allowed, and denies egress when network.allowOutbound is false (a proxy no longer
      overrides the user's outbound policy); when a proxied fetch fails it warns that
      curl/wget share the same proxy, and suggests requestSandboxBypass only when
      the sandbox proxy itself is unreachable
    source_release: https://github.com/github/copilot-cli/releases/tag/v1.0.76
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: github-copilot-cli
  product_name: GitHub Copilot CLI
  slug: 5-safety-and-privacy-changes-in-v1-0-76
  source_release: github-copilot-cli-2026-07-30-v1-0-76-github-362129864-0932fe29
  source_type: github_releases
  theme: safety-privacy
  title: 5 Safety and Privacy changes in v1.0.76
  type: change
related_changes:
- '[[Changes/Codex CLI/2026-07-29-6-safety-and-privacy-changes-in-rust-v0-146-0|6
  Safety and Privacy changes in rust-v0.146.0]]'
- '[[Changes/Lovable/2026-07-29-fewer-false-alarms-in-dependency-scans|Fewer false
  alarms in dependency scans]]'
- '[[Changes/OpenHands/2026-07-29-fix-revive-local-telemetry-consent-banner-by-malhotra5-in-https-github-com-openh|fix:
  Revive local telemetry consent banner]]'
source_release: '[[Releases/GitHub Copilot CLI/github-copilot-cli-2026-07-30-v1-0-76-github-362129864-0932fe29|github-copilot-cli-2026-07-30-v1-0-76-github-362129864-0932fe29]]'
source_type: github_releases
theme: safety-privacy
title: 5 Safety and Privacy changes in v1.0.76
type: change
---

<!-- chronolog:begin region="header" -->
# 5 Safety and Privacy changes in v1.0.76

**GitHub Copilot CLI** · 2026-07-30 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://github.com/github/copilot-cli/releases/tag/v1.0.76) · from [[Releases/GitHub Copilot CLI/github-copilot-cli-2026-07-30-v1-0-76-github-362129864-0932fe29|1.0.76]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Sandbox denied paths are enforced for relative and symlinked entries on macOS and Linux (Windows cannot deny per path)

> URL permission prompts now keep their sandbox-bypass warning and the model's reason when a host integration rebuilds the prompt, so an elevated fetch is no longer shown as an ordinary one

> `web_fetch` now follows HTTP redirects instead of failing, asking permission for the redirect target when it is on a different origin and showing where the redirect came from

> Enterprise administrators can enforce a restrictive sandbox floor: managed settings tighten (but never loosen) the user's sandbox policy, and the `/sandbox` dialog surfaces the org-configured managed values with locked fields and managed filesystem paths so admins can confirm what is enforced.

> web_fetch routes through the configured sandbox proxy when outbound is allowed, and denies egress when network.allowOutbound is false (a proxy no longer overrides the user's outbound policy); when a proxied fetch fails it warns that curl/wget share the same proxy, and suggests requestSandboxBypass only when the sandbox proxy itself is unreachable

Source: https://github.com/github/copilot-cli/releases/tag/v1.0.76
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/GitHub Copilot CLI/2026-07-30-a-userpromptsubmitted-hook-returning-a-non-string-value-for-modifiedprompt-modif|A userPromptSubmitted hook returning a non-string value for modifiedPrompt…]] · Memory and Personalization
- [[Changes/GitHub Copilot CLI/2026-07-30-diff-scrolls-and-syntax-highlights-large-multi-file-diffs-faster|/diff scrolls and syntax-highlights large multi-file diffs faster]] · Reliability and Performance
- [[Changes/GitHub Copilot CLI/2026-07-30-2-developer-workflow-changes-in-v1-0-76|2 Developer Workflow changes in v1.0.76]] · Developer Workflow
- [[Changes/GitHub Copilot CLI/2026-07-30-2-apps-and-integrations-changes-in-v1-0-76|2 Apps and Integrations changes in v1.0.76]] · Apps and Integrations
- [[Changes/GitHub Copilot CLI/2026-07-30-2-model-support-changes-in-v1-0-76|2 Model Support changes in v1.0.76]] · Model Support
- [[Changes/GitHub Copilot CLI/2026-07-30-restore-the-early-warning-when-unreclaimable-system-and-tool-context-nears-the-l|Restore the early warning when unreclaimable system and tool context nears…]] · Context Window
- [[Changes/GitHub Copilot CLI/2026-07-30-voice-mode-pauses-playing-media-before-recording-and-resumes-it-afterward-where|Voice mode pauses playing media before recording and resumes it afterward, where…]] · Voice and Audio
- [[Changes/GitHub Copilot CLI/2026-07-30-2-agent-mode-changes-in-v1-0-76|2 Agent Mode changes in v1.0.76]] · Agent Mode
- [[Changes/GitHub Copilot CLI/2026-07-30-2-editor-experience-changes-in-v1-0-76|2 Editor Experience changes in v1.0.76]] · Editor Experience
- [[Changes/GitHub Copilot CLI/2026-07-30-4-interface-experience-changes-in-v1-0-76|4 Interface Experience changes in v1.0.76]] · Interface Experience
- [[Changes/GitHub Copilot CLI/2026-07-30-10-other-changes-in-v1-0-76|10 other changes in v1.0.76]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Safety and Privacy

- Earlier: 2026-07-29 · OpenHands · [[Changes/OpenHands/2026-07-29-fix-revive-local-telemetry-consent-banner-by-malhotra5-in-https-github-com-openh|fix: Revive local telemetry consent banner]]
- Later: 2026-07-30 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-07-30-2-safety-and-privacy-changes-in-v1-0-77|2 Safety and Privacy changes in v1.0.77]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-04-16 · Cursor · [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|Ghost mode for opting out of storing any kind of data on our servers]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20github-copilot-cli-2026-07-30-0019cf&body=Card%3A%20Changes%2FGitHub%20Copilot%20CLI%2F2026-07-30-5-safety-and-privacy-changes-in-v1-0-76.md%0ACard%20ID%3A%20github-copilot-cli-2026-07-30-0019cf%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgithub%2Fcopilot-cli%2Freleases%2Ftag%2Fv1.0.76%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->