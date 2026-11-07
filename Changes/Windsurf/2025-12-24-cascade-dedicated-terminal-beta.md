---
card_id: windsurf-2025-12-24-2b62fd
date: '2025-12-24'
description: 'Windsurf · 2025-12-24 · Developer Workflow: Windsurf introduces a new
  approach for letting agents execute terminal commands. Instead of your default shell…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter
    Colors]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2661
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: significant
kind: launch
machine_hash: cc58e3c13db312113918d86604ffccce0292706256eb3c250f78e44ffa408ca6
product: windsurf
product_name: Windsurf
record:
  ai_generated: true
  card_id: windsurf-2025-12-24-2b62fd
  comparison: ''
  confidence: low
  date: '2025-12-24'
  description: 'Windsurf — v1.13.3: Windsurf introduces a new approach for letting
    agents execute terminal commands. Instead of your default shell, Cascade will
    now run commands in a dedicated zsh shell specifically configured for reliability.
    The Cascade Dedicated Terminal can use the environment variables you set in your
    .zshrc configuration and is interactive, which means you can answer any prompts
    from shell scripts without having to break your flow. This should improve the
    reliability and speed of shell commands, especially for users with complicated
    prompts (e.g., powerlevel10k).'
  evidence:
  - quote: Windsurf introduces a new approach for letting agents execute terminal
      commands. Instead of your default shell, Cascade will now run commands in a
      dedicated zsh shell specifically configured for reliability. The Cascade Dedicated
      Terminal can use the environment variables you set in your .zshrc configuration
      and is interactive, which means you can answer any prompts from shell scripts
      without having to break your flow. This should improve the reliability and speed
      of shell commands, especially for users with complicated prompts (e.g., powerlevel10k).
    source_release: https://docs.devin.ai/desktop/changelog#v1-13-3
  - quote: In this version, the Cascade Dedicated Terminal will be opt-in for Windsurf
      Stable on macOS. If you are experiencing issues with the older legacy terminal,
      we recommend switching to the new terminal early. We expect to make this feature
      the default in the future, while maintaining the legacy terminal extension for
      backwards compatibility purposes. You can opt-in in the Windsurf User Settings
      -> Disable Windsurf Legacy Terminal Profile.
    source_release: https://docs.devin.ai/desktop/changelog#v1-13-3
  extractor_version: fallback-v5
  impact: significant
  kind: launch
  product: windsurf
  product_name: Windsurf
  slug: cascade-dedicated-terminal-beta
  source_release: windsurf-2025-12-24-v1-13-3-cac9d5c1
  source_type: windsurf_changelog
  theme: developer-workflow
  title: Cascade Dedicated Terminal (Beta)
  type: change
related_changes:
- '[[Changes/Gemini CLI/2025-12-22-feat-a2a-introduce-init-command-for-a2a-server-by-cocosheng-g-in-https-github-co|feat(a2a):
  Introduce /init command for a2a server]]'
- '[[Changes/Open WebUI/2025-12-22-2-developer-workflow-changes-in-v0-6-43|2 Developer
  Workflow changes in v0.6.43]]'
- '[[Changes/Windsurf/2025-12-24-git-worktree-support|Git Worktree Support]]'
source_release: '[[Releases/Windsurf/windsurf-2025-12-24-v1-13-3-cac9d5c1|windsurf-2025-12-24-v1-13-3-cac9d5c1]]'
source_type: windsurf_changelog
theme: developer-workflow
title: Cascade Dedicated Terminal (Beta)
type: change
---

<!-- chronolog:begin region="header" -->
# Cascade Dedicated Terminal (Beta)

**Windsurf** · 2025-12-24 · [[Themes/developer-workflow|Developer Workflow]] · Launch · [Official source](https://docs.devin.ai/desktop/changelog#v1-13-3) · from [[Releases/Windsurf/windsurf-2025-12-24-v1-13-3-cac9d5c1|v1.13.3]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Windsurf introduces a new approach for letting agents execute terminal commands. Instead of your default shell, Cascade will now run commands in a dedicated zsh shell specifically configured for reliability. The Cascade Dedicated Terminal can use the environment variables you set in your .zshrc configuration and is interactive, which means you can answer any prompts from shell scripts without having to break your flow. This should improve the reliability and speed of shell commands, especially for users with complicated prompts (e.g., powerlevel10k).
>
> In this version, the Cascade Dedicated Terminal will be opt-in for Windsurf Stable on macOS. If you are experiencing issues with the older legacy terminal, we recommend switching to the new terminal early. We expect to make this feature the default in the future, while maintaining the legacy terminal extension for backwards compatibility purposes. You can opt-in in the Windsurf User Settings -> Disable Windsurf Legacy Terminal Profile.
>
> Source: https://docs.devin.ai/desktop/changelog#v1-13-3
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Windsurf/2025-12-24-context-window-indicator|Context Window Indicator]] · Context Window
- [[Changes/Windsurf/2025-12-24-git-worktree-support|Git Worktree Support]] · Developer Workflow
- [[Changes/Windsurf/2025-12-24-2-editor-experience-changes-in-v1-13-3|2 Editor Experience changes in v1.13.3]] · Editor Experience
- [[Changes/Windsurf/2025-12-24-2-developer-workflow-changes-in-v1-13-3|2 Developer Workflow changes in v1.13.3]] · Developer Workflow
- [[Changes/Windsurf/2025-12-24-multiple-fixes-to-the-model-context-protocol-implementation|Multiple fixes to the Model Context Protocol implementation]] · Context Window
- [[Changes/Windsurf/2025-12-24-swe-1-5-free|SWE-1.5 Free]] · Reliability and Performance
- [[Changes/Windsurf/2025-12-24-wave-13-merry-shipmas|Wave 13: Merry Shipmas]] · Developer Workflow
- [[Changes/Windsurf/2025-12-24-cascade-hooks|Cascade Hooks]] · Model Support
- [[Changes/Windsurf/2025-12-24-supports-lowering-permissions-for-cascade-s-web-fetch-tool|Supports lowering permissions for Cascade's Web Fetch tool]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2025-12-22 · Open WebUI · [[Changes/Open WebUI/2025-12-22-2-developer-workflow-changes-in-v0-6-43|2 Developer Workflow changes in v0.6.43]]
- Later: 2025-12-25 · Dify · [[Changes/Dify/2025-12-25-2-developer-workflow-changes-in-1-11-2|2 Developer Workflow changes in 1.11.2]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2018-09-11 · Descript · [[Changes/Descript/2018-09-11-highlight-text-in-many-colors-press-command-shift-h-to-quick-highlight-descript|Highlighter Colors]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20windsurf-2025-12-24-2b62fd&body=Card%3A%20Changes%2FWindsurf%2F2025-12-24-cascade-dedicated-terminal-beta.md%0ACard%20ID%3A%20windsurf-2025-12-24-2b62fd%0ASource%3A%20https%3A%2F%2Fdocs.devin.ai%2Fdesktop%2Fchangelog%23v1-13-3%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->