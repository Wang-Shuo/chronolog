---
card_id: codex-cli-2025-10-09-c606d1
date: '2025-10-09'
description: 'Codex CLI · 2025-10-09 · Other changes: 20 changes in 0.46.0 — Print
  codex resume note when quitting after codex resume by @nornagon-openai in…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 436a4b61168fa84f1de51603b55efd291b03eac49a487856a9c63a06fbb96cdf
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2025-10-09-c606d1
  comparison: ''
  date: '2025-10-09'
  description: 'Codex CLI — 0.46.0: 20 other changes'
  evidence:
  - quote: Print codex resume note when quitting after codex resume by @nornagon-openai
      in https://github.com/openai/codex/pull/4695
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.46.0
  - quote: Use Number instead of BigInt for TokenCountEvent by @ccy-oai in https://github.com/openai/codex/pull/4856
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.46.0
  - quote: Simplify request body assertions by @pakrym-oai in https://github.com/openai/codex/pull/4845
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.46.0
  - quote: '[Cloud Tasks] Use workspace deps by @tamird in https://github.com/openai/codex/pull/4693'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.46.0
  - quote: Simplify parallel by @pakrym-oai in https://github.com/openai/codex/pull/4829
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.46.0
  - quote: '[TUI] Remove bottom padding by @gpeal in https://github.com/openai/codex/pull/4854'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.46.0
  - quote: '[TUI] Dynamic width for line numbers in diffs by @nornagon-openai in https://github.com/openai/codex/pull/4664'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.46.0
  - quote: '[TUI] Wrapping bugfix by @nornagon-openai in https://github.com/openai/codex/pull/4674'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.46.0
  - quote: '`list_dir` tool by @jif-oai in https://github.com/openai/codex/pull/4817'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.46.0
  - quote: '[TUI] Remove instruction hack for /review by @dedrisian-oai in https://github.com/openai/codex/pull/4896'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.46.0
  - quote: '[TUI] Bring the transcript closer to display mode by @nornagon-openai
      in https://github.com/openai/codex/pull/4848'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.46.0
  - quote: remove experimental prefix by @rakesh-oai in https://github.com/openai/codex/pull/4907
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.46.0
  - quote: featgrep_files as a tool by @jif-oai in https://github.com/openai/codex/pull/4820
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.46.0
  - quote: CLI UP/ENTER by @jif-oai in https://github.com/openai/codex/pull/4944
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.46.0
  - quote: change log_sse_event() so it no longer takes a closure by @bolinfest in
      https://github.com/openai/codex/pull/4953
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.46.0
  - quote: truncate on compact by @jif-oai in https://github.com/openai/codex/pull/4942
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.46.0
  - quote: '[TUI] hardcode xterm palette, shimmer blends between fg and bg by @nornagon-openai
      in https://github.com/openai/codex/pull/4957'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.46.0
  - quote: Create alias by @rakesh-oai in https://github.com/openai/codex/pull/4971
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.46.0
  - quote: Set chat name by @dedrisian-oai in https://github.com/openai/codex/pull/4974
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.46.0
  - quote: revert /name for now by @dedrisian-oai in https://github.com/openai/codex/pull/4978
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.46.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 20-other-changes-in-rust-v0-46-0
  source_release: codex-cli-2025-10-09-rust-v0-46-0-github-253202599-fb352044
  source_type: github_releases
  theme: uncategorized
  title: 20 other changes in rust-v0.46.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2025-10-09-rust-v0-46-0-github-253202599-fb352044|codex-cli-2025-10-09-rust-v0-46-0-github-253202599-fb352044]]'
source_type: github_releases
theme: uncategorized
title: 20 other changes in rust-v0.46.0
type: change
---

<!-- chronolog:begin region="header" -->
# 20 other changes in rust-v0.46.0

**Codex CLI** · 2025-10-09 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.46.0) · from [[Releases/Codex CLI/codex-cli-2025-10-09-rust-v0-46-0-github-253202599-fb352044|0.46.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Print codex resume note when quitting after codex resume by @nornagon-openai in https://github.com/openai/codex/pull/4695

> Use Number instead of BigInt for TokenCountEvent by @ccy-oai in https://github.com/openai/codex/pull/4856

> Simplify request body assertions by @pakrym-oai in https://github.com/openai/codex/pull/4845

> [Cloud Tasks] Use workspace deps by @tamird in https://github.com/openai/codex/pull/4693

> Simplify parallel by @pakrym-oai in https://github.com/openai/codex/pull/4829

> [TUI] Remove bottom padding by @gpeal in https://github.com/openai/codex/pull/4854

> [TUI] Dynamic width for line numbers in diffs by @nornagon-openai in https://github.com/openai/codex/pull/4664

> [TUI] Wrapping bugfix by @nornagon-openai in https://github.com/openai/codex/pull/4674

> `list_dir` tool by @jif-oai in https://github.com/openai/codex/pull/4817

> [TUI] Remove instruction hack for /review by @dedrisian-oai in https://github.com/openai/codex/pull/4896

> [TUI] Bring the transcript closer to display mode by @nornagon-openai in https://github.com/openai/codex/pull/4848

> remove experimental prefix by @rakesh-oai in https://github.com/openai/codex/pull/4907

> featgrep_files as a tool by @jif-oai in https://github.com/openai/codex/pull/4820

> CLI UP/ENTER by @jif-oai in https://github.com/openai/codex/pull/4944

> change log_sse_event() so it no longer takes a closure by @bolinfest in https://github.com/openai/codex/pull/4953

> truncate on compact by @jif-oai in https://github.com/openai/codex/pull/4942

> [TUI] hardcode xterm palette, shimmer blends between fg and bg by @nornagon-openai in https://github.com/openai/codex/pull/4957

> Create alias by @rakesh-oai in https://github.com/openai/codex/pull/4971

> Set chat name by @dedrisian-oai in https://github.com/openai/codex/pull/4974

> revert /name for now by @dedrisian-oai in https://github.com/openai/codex/pull/4978

Source: https://github.com/openai/codex/releases/tag/rust-v0.46.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2025-10-09-6-apps-and-integrations-changes-in-rust-v0-46-0|6 Apps and Integrations changes in rust-v0.46.0]] · Apps and Integrations
- [[Changes/Codex CLI/2025-10-09-tui-switch-to-tree-sitter-highlight-bash-highlighting-by-nornagon-openai-in-http|TUI Switch to tree-sitter-highlight bash highlighting]] · Developer Workflow
- [[Changes/Codex CLI/2025-10-09-tui-breathing-spinner-on-true-color-terms-by-nornagon-openai-in-https-github-com|TUI Breathing spinner on true-color terms]] · Interface Experience
- [[Changes/Codex CLI/2025-10-09-make-context-line-permanent-by-dedrisian-oai-in-https-github-com-openai-codex-pu|Make context line permanent]] · Context Window
- [[Changes/Codex CLI/2025-10-09-we-are-in-the-middle-of-significantly-improving-support-for-connecting-to-mcp-se|We are in the middle of significantly improving support for connecting to MCP…]] · Account and Access
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2025-10-09-c606d1&body=Card%3A%20Changes%2FCodex%20CLI%2F2025-10-09-20-other-changes-in-rust-v0-46-0.md%0ACard%20ID%3A%20codex-cli-2025-10-09-c606d1%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.46.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->