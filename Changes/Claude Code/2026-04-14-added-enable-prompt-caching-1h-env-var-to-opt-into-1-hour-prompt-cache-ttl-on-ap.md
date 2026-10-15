---
card_id: claude-code-2026-04-14-4bb7a3
date: '2026-04-14'
description: 'Claude Code · 2026-04-14 · Context Window: Added `ENABLE_PROMPT_CACHING_1H`
  env var to opt into 1-hour prompt cache TTL on API key, Bedrock, Vertex, and…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-05-04-extended-prompt-length-for-project-generation|Extended
    prompt length for project generation]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1076
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: context-window
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v4
impact: incremental
machine_hash: 207bf3eb8dd890437988a068b4d25dd3935c2d08578621a87045fe827bdc2573
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-04-14-4bb7a3
  comparison: ''
  date: '2026-04-14'
  description: 'Claude Code — v2.1.108: Added `ENABLE_PROMPT_CACHING_1H` env var to
    opt into 1-hour prompt cache TTL on API key, Bedrock, Vertex, and Foundry (`ENABLE_PROMPT_CACHING_1H_BEDROCK`
    is deprecated but still honored), and `FORCE_PROMPT_CACHING_5M` to force 5-minute
    TTL'
  evidence:
  - quote: Added `ENABLE_PROMPT_CACHING_1H` env var to opt into 1-hour prompt cache
      TTL on API key, Bedrock, Vertex, and Foundry (`ENABLE_PROMPT_CACHING_1H_BEDROCK`
      is deprecated but still honored), and `FORCE_PROMPT_CACHING_5M` to force 5-minute
      TTL
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.108
  extractor_version: fallback-v4
  impact: incremental
  product: claude-code
  product_name: Claude Code
  slug: added-enable-prompt-caching-1h-env-var-to-opt-into-1-hour-prompt-cache-ttl-on-ap
  source_release: claude-code-2026-04-14-v2-1-108-github-309009167-35123bd5
  source_type: github_releases
  theme: context-window
  theme_matches: []
  theme_resolution: manual-semantic-rule-v1
  title: Added `ENABLE_PROMPT_CACHING_1H` env var to opt into 1-hour prompt cache
    TTL on API…
  type: change
related_changes:
- '[[Changes/ChatGPT/2026-03-25-starting-today-for-chatgpt-plus-pro-and-business-users-long-pastes-are-handled-d|Starting
  today for ChatGPT Plus, Pro, and Business users, long pastes are handled…]]'
- '[[Changes/Claude Code/2026-03-27-reduced-token-overhead-when-mentioning-files-with-raw-string-content-no-longer-j|Reduced
  token overhead when mentioning files with @]]'
- '[[Changes/Claude Code/2026-04-09-added-exclude-dynamic-system-prompt-sections-flag-to-print-mode-for-improved-cro|Added
  --exclude-dynamic-system-prompt-sections flag to print mode for improved…]]'
source_release: '[[Releases/Claude Code/claude-code-2026-04-14-v2-1-108-github-309009167-35123bd5|claude-code-2026-04-14-v2-1-108-github-309009167-35123bd5]]'
source_type: github_releases
theme: context-window
title: Added ENABLE_PROMPT_CACHING_1H env var to opt into 1-hour prompt cache TTL
  on API…
type: change
---

<!-- chronolog:begin region="header" -->
# Added `ENABLE_PROMPT_CACHING_1H` env var to opt into 1-hour prompt cache TTL on API…

**Claude Code** · 2026-04-14 · [[Themes/context-window|Context Window]] · [Official source](https://github.com/anthropics/claude-code/releases/tag/v2.1.108) · from [[Releases/Claude Code/claude-code-2026-04-14-v2-1-108-github-309009167-35123bd5|v2.1.108]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `ENABLE_PROMPT_CACHING_1H` env var to opt into 1-hour prompt cache TTL on API key, Bedrock, Vertex, and Foundry (`ENABLE_PROMPT_CACHING_1H_BEDROCK` is deprecated but still honored), and `FORCE_PROMPT_CACHING_5M` to force 5-minute TTL
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.108
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Claude Code/2026-04-14-undo-is-now-an-alias-for-rewind|/undo is now an alias for /rewind]] · Interface Experience
- [[Changes/Claude Code/2026-04-14-added-recap-feature-to-provide-context-when-returning-to-a-session-configurable|Added recap feature to provide context when returning to a session, configurable…]] · Context Window
- [[Changes/Claude Code/2026-04-14-improved-model-to-warn-before-switching-models-mid-conversation-since-the-next-r|Improved /model to warn before switching models mid-conversation, since the next…]] · Model Support
- [[Changes/Claude Code/2026-04-14-the-model-can-now-discover-and-invoke-built-in-slash-commands-like-init-review-a|The model can now discover and invoke built-in slash commands like /init…]] · Safety and Privacy
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Context Window

- Earlier: 2026-04-09 · Claude Code · [[Changes/Claude Code/2026-04-09-added-exclude-dynamic-system-prompt-sections-flag-to-print-mode-for-improved-cro|Added --exclude-dynamic-system-prompt-sections flag to print mode for improved…]]
- Later: 2026-04-15 · Claude Code · [[Changes/Claude Code/2026-04-15-added-option-to-show-claude-s-last-response-as-commented-context-in-the-ctrl-g-e|Added option to show Claude's last response as commented context in the Ctrl+G…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-05-04 · Cursor · [[Changes/Cursor/2023-05-04-extended-prompt-length-for-project-generation|Extended prompt length for project generation]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20claude-code-2026-04-14-4bb7a3&body=Card%3A%20Changes%2FClaude%20Code%2F2026-04-14-added-enable-prompt-caching-1h-env-var-to-opt-into-1-hour-prompt-cache-ttl-on-ap.md%0ACard%20ID%3A%20claude-code-2026-04-14-4bb7a3%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fanthropics%2Fclaude-code%2Freleases%2Ftag%2Fv2.1.108%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->