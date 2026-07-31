---
card_id: claude-code-2026-03-27-833a57
date: '2026-03-27'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-14-instant-fix-all-lint-errors-with-ai|cursor-2023-03-14-24e9bf]]'
  lag_days: 1109
  role: follower
  scope: tracked-products-only
  theme: editor-experience
  tracked_products_count: 3
evolves_from:
- '[[Changes/Claude Code/2026-02-25-vs-code-fixed-another-cause-of-command-claude-vscode-editor-openlast-not-found-c|claude-code-2026-02-25-d004fd]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: 2b94fa86bdc79d281f0ccc5c8e9be08e77a6c902304ba1d5f07568a3aa7a9349
product: claude-code
product_name: Claude Code
related_changes:
- '[[Changes/Claude Code/2026-02-25-vs-code-fixed-another-cause-of-command-claude-vscode-editor-openlast-not-found-c|claude-code-2026-02-25-d004fd]]'
- '[[Changes/ChatGPT/2026-02-27-edit-messages-with-images-you-can-now-edit-messages-that-include-image-attachmen|chatgpt-2026-02-27-f608a6]]'
- '[[Changes/Cursor/2026-03-04-install-the-cursor-acp-directly-in-your-jetbrains-ide-from-the-acp-registry-and|cursor-2026-03-04-cc7d5c]]'
source_release: '[[Releases/Claude Code/claude-code-2026-03-27-v2-1-86-github-302569462-d6b30859|claude-code-2026-03-27-v2-1-86-github-302569462-d6b30859]]'
theme: editor-experience
type: change
---

# Added `.jj` and `.sl` to VCS directory exclusion lists so Grep and file autocomp

<!-- chronolog:begin region="description" -->
Added `.jj` and `.sl` to VCS directory exclusion lists so Grep and file autocomplete don't descend into Jujutsu or Sapling metadata
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `.jj` and `.sl` to VCS directory exclusion lists so Grep and file autocomplete don't descend into Jujutsu or Sapling metadata
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.86
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/Claude Code/2026-02-25-vs-code-fixed-another-cause-of-command-claude-vscode-editor-openlast-not-found-c|claude-code-2026-02-25-d004fd]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: editor-experience
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-03-14-instant-fix-all-lint-errors-with-ai|cursor-2023-03-14-24e9bf]]
- Lag Days: 1109
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes