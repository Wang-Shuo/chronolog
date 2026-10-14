---
card_id: claude-code-2026-08-04-02f51c
date: '2026-08-04'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1206
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 3
evolves_from: []
extractor_version: fallback-v3
impact: incremental
machine_hash: 4b38038d6939f829a2fd9edcc17663a4757e374426cc1200b4671a0864933688
product: claude-code
product_name: Claude Code
record:
  card_id: claude-code-2026-08-04-02f51c
  comparison: ''
  date: '2026-08-04'
  description: 'Claude Code — v2.1.221: Added `mode: "mask"` for sandbox credential
    files on Linux and WSL — sandboxed commands read a sentinel copy (the whole file,
    or just the spans captured by an `extract` regex) while the sandbox proxy substitutes
    the real value on egress; on macOS file masking falls back to `deny`'
  evidence:
  - quote: 'Added `mode: "mask"` for sandbox credential files on Linux and WSL — sandboxed
      commands read a sentinel copy (the whole file, or just the spans captured by
      an `extract` regex) while the sandbox proxy substitutes the real value on egress;
      on macOS file masking falls back to `deny`'
    source_release: https://github.com/anthropics/claude-code/releases/tag/v2.1.221
  extractor_version: fallback-v3
  impact: incremental
  product: claude-code
  product_name: Claude Code
  slug: added-mode-mask-for-sandbox-credential-files-on-linux-and-wsl-sandboxed-commands
  source_release: claude-code-2026-08-04-v2-1-221-github-364520051-d6a656ce
  source_type: github_releases
  theme: safety-privacy
  theme_matches:
  - matched_terms:
    - wsl
    score: 50
    theme: developer-workflow
  - matched_terms:
    - macos
    score: 50
    theme: mobile-desktop
  theme_resolution: manual-semantic-rule-v2
  title: 'Added `mode: "mask"` for sandbox credential files on Linux and WSL — sandboxed
    c'
  type: change
related_changes:
- '[[Changes/Claude Code/2026-07-22-fixed-agent-frontmatter-hooks-running-from-untrusted-folders-hooks-now-require-t|claude-code-2026-07-22-9528ae]]'
- '[[Changes/ChatGPT/2026-07-23-health-is-built-with-layered-privacy-and-security-safeguards-connected-medical-r|chatgpt-2026-07-23-4a5fd5]]'
- '[[Changes/Claude Code/2026-07-24-added-sandbox-network-strictallowlist-setting-to-deny-non-allowlisted-hosts-for|claude-code-2026-07-24-89a3e1]]'
source_release: '[[Releases/Claude Code/claude-code-2026-08-04-v2-1-221-github-364520051-d6a656ce|claude-code-2026-08-04-v2-1-221-github-364520051-d6a656ce]]'
source_type: github_releases
theme: safety-privacy
title: 'Added mode: "mask" for sandbox credential files on Linux and WSL — sandboxed
  c'
type: change
---

# Added `mode: "mask"` for sandbox credential files on Linux and WSL — sandboxed c

<!-- chronolog:begin region="description" -->
Claude Code — v2.1.221: Added `mode: "mask"` for sandbox credential files on Linux and WSL — sandboxed commands read a sentinel copy (the whole file, or just the spans captured by an `extract` regex) while the sandbox proxy substitutes the real value on egress; on macOS file masking falls back to `deny`
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> Added `mode: "mask"` for sandbox credential files on Linux and WSL — sandboxed commands read a sentinel copy (the whole file, or just the spans captured by an `extract` regex) while the sandbox proxy substitutes the real value on egress; on macOS file masking falls back to `deny`
>
> Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.221
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
No evidence-backed evolution relationship assigned.
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: safety-privacy
- Relation: same-theme-chronology
- Inference: No adoption, equivalence, or causation claim.
- Scope: tracked-products-only
- Role: later-observed
- First In Tracked: [[Changes/Cursor/2023-04-16-ghost-mode-for-opting-out-of-storing-any-kind-of-data-on-our-servers|cursor-2023-04-16-f0e22a]]
- Lag Days: 1206
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes