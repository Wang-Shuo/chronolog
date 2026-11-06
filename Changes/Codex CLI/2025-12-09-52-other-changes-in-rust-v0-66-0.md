---
card_id: codex-cli-2025-12-09-25d6e0
date: '2025-12-09'
description: 'Codex CLI · 2025-12-09 · Other changes: 52 changes in 0.66.0 — fallback
  checks inspect each pipeline segment so unsafe tails (e.g., | rm -rf) are still
  caught…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: fbc863b352245b801be2c9b28c6fbf36f6f974577a40fed4b53330e50d960b7a
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2025-12-09-25d6e0
  comparison: ''
  date: '2025-12-09'
  description: 'Codex CLI — 0.66.0: 52 other changes'
  evidence:
  - quote: 'fallback checks inspect each pipeline segment so unsafe tails (e.g., |
      rm -rf) are still caught (#7033, #7543, #7609, #7653, #7544).'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.66.0
  - quote: 'dangling sessions after tool calls (#7563, #7620, #7655, #7594, #7592).'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.66.0
  - quote: 'Apply-patch: Windows CRLF line endings are preserved, new e2e scenarios
      cover more patch shapes, and Windows-specific test coverage reduces regressions
      in patch flows (#7515, #7567, #7554). Thanks to @cnaples79 who contributed the
      [core part](https://github.com/openai/codex/pull/4017) of this fix!'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.66.0
  - quote: 'Signing: Linux artifacts are signed via sigstore. (#7674).'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.66.0
  - quote: '(#7634, #7638, #7724, #7705).'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.66.0
  - quote: '#7310 Inline response recording and remove process_items indirection @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.66.0
  - quote: '#7543 execpolicy tui flow @zhao-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.66.0
  - quote: '#7544 Refactor execpolicy fallback evaluation @zhao-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.66.0
  - quote: '#7561 Do not emit start/end events for write stdin @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.66.0
  - quote: '#7563 Slightly better status display for unified exec @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.66.0
  - quote: '#7567 chore(apply-patch) scenarios for e2e testing @dylan-hurd-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.66.0
  - quote: '#7583 Fix handle_shortcut_overlay_key for cross-platform consistency @448523760'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.66.0
  - quote: '#7588 chore: default warning messages to true @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.66.0
  - quote: '#7591 chore: tool tip for /prompt @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.66.0
  - quote: '#7592 fix: release session ID when not used @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.66.0
  - quote: '#7593 chore: review in read-only @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.66.0
  - quote: '#7594 fix: sse for chat @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.66.0
  - quote: '#7595 Update execpolicy.md @zhao-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.66.0
  - quote: '#7602 add --branch to codex cloud exec @nornagon-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.66.0
  - quote: '#7605 fix(app-server): add duration_ms to McpToolCallItem @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.66.0
  - quote: '#7610 fix: taking plan type from usage endpoint instead of thru auth token
      @zhao-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.66.0
  - quote: '#7611 fix(app-server): add will_retry to ErrorNotification @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.66.0
  - quote: '#7615 chore: refactor to move Arc<RwLock> concern outside exec_policy_for
      @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.66.0
  - quote: '#7626 fix typo @zhao-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.66.0
  - quote: '#7629 fix(tui): add missing Ctrl+n/Ctrl+p support to ListSelectionView
      @pppp606'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.66.0
  - quote: '#7638 fix: ignore ghost snapshots in token consumption @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.66.0
  - quote: '#7645 Also load skills from repo root. @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.66.0
  - quote: '#7651 fix: OTEL HTTP exporter panic and mTLS support @asm89'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.66.0
  - quote: '#7652 Move justfile to repository root @joshka-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.66.0
  - quote: '#7654 fix: exec-server stream was erroring for large requests @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.66.0
  - quote: '#7655 fix wrap behavior for long commands @zhao-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.66.0
  - quote: '#7660 Restore status header after stream recovery @joshka-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.66.0
  - quote: '#7665 docs: fix documentation of rmcp client flag @JaySabva'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.66.0
  - quote: '#7669 fix(doc): TOML otel exporter example — multi-line inline table is
      invalid @448523760'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.66.0
  - quote: '#7672 docs: Remove experimental_use_rmcp_client from config @JaySabva'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.66.0
  - quote: '#7673 docs: point dev checks to just @voctory'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.66.0
  - quote: '#7674 feat: linux codesign with sigstore @shijie-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.66.0
  - quote: '#7675 feat: windows codesign with Azure trusted signing @shijie-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.66.0
  - quote: '#7678 fix: clear out space on ubuntu runners before running Rust tests
      @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.66.0
  - quote: '#7685 fix: refine the warning message and docs for deprecated tools config
      @gameofby'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.66.0
  - quote: '#7711 Add formatting client version to the x.x.x style. @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.66.0
  - quote: '#7713 chore(deps): bump ts-rs from 11.0.1 to 11.1.0 in /codex-rs @dependabot[bot]'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.66.0
  - quote: '#7714 chore(deps): bump derive_more from 2.0.1 to 2.1.0 in /codex-rs @dependabot[bot]'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.66.0
  - quote: '#7715 chore(deps): bump insta from 1.43.2 to 1.44.3 in /codex-rs @dependabot[bot]'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.66.0
  - quote: '#7716 chore(deps): bump wildmatch from 2.5.0 to 2.6.1 in /codex-rs @dependabot[bot]'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.66.0
  - quote: '#7724 Fixed regression for chat endpoint; missing tools name caused litellm
      proxy to crash @etraut-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.66.0
  - quote: '#7745 Make the device auth instructions more clear. @mzeng-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.66.0
  - quote: '#7747 updating app server types to support execpoilcy amendment @zhao-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.66.0
  - quote: '#7748 Remove legacy ModelInfo and merge it with ModelFamily @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.66.0
  - quote: '#7749 fix: pre-main hardening logic must tolerate non-UTF-8 env vars @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.66.0
  - quote: '#7753 Revert "feat: windows codesign with Azure trusted signing" @shijie-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.66.0
  - quote: '#7754 override instructions using ModelInfo @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.66.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 52-other-changes-in-rust-v0-66-0
  source_release: codex-cli-2025-12-09-rust-v0-66-0-github-268559734-698ec8f9
  source_type: github_releases
  theme: uncategorized
  title: 52 other changes in rust-v0.66.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2025-12-09-rust-v0-66-0-github-268559734-698ec8f9|codex-cli-2025-12-09-rust-v0-66-0-github-268559734-698ec8f9]]'
source_type: github_releases
theme: uncategorized
title: 52 other changes in rust-v0.66.0
type: change
---

<!-- chronolog:begin region="header" -->
# 52 other changes in rust-v0.66.0

**Codex CLI** · 2025-12-09 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.66.0) · from [[Releases/Codex CLI/codex-cli-2025-12-09-rust-v0-66-0-github-268559734-698ec8f9|0.66.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> fallback checks inspect each pipeline segment so unsafe tails (e.g., | rm -rf) are still caught (#7033, #7543, #7609, #7653, #7544).

> dangling sessions after tool calls (#7563, #7620, #7655, #7594, #7592).

> Apply-patch: Windows CRLF line endings are preserved, new e2e scenarios cover more patch shapes, and Windows-specific test coverage reduces regressions in patch flows (#7515, #7567, #7554). Thanks to @cnaples79 who contributed the [core part](https://github.com/openai/codex/pull/4017) of this fix!

> Signing: Linux artifacts are signed via sigstore. (#7674).

> (#7634, #7638, #7724, #7705).

> #7310 Inline response recording and remove process_items indirection @aibrahim-oai

> #7543 execpolicy tui flow @zhao-oai

> #7544 Refactor execpolicy fallback evaluation @zhao-oai

> #7561 Do not emit start/end events for write stdin @pakrym-oai

> #7563 Slightly better status display for unified exec @pakrym-oai

> #7567 chore(apply-patch) scenarios for e2e testing @dylan-hurd-oai

> #7583 Fix handle_shortcut_overlay_key for cross-platform consistency @448523760

> #7588 chore: default warning messages to true @jif-oai

> #7591 chore: tool tip for /prompt @jif-oai

> #7592 fix: release session ID when not used @jif-oai

> #7593 chore: review in read-only @jif-oai

> #7594 fix: sse for chat @jif-oai

> #7595 Update execpolicy.md @zhao-oai

> #7602 add --branch to codex cloud exec @nornagon-openai

> #7605 fix(app-server): add duration_ms to McpToolCallItem @owenlin0

> #7610 fix: taking plan type from usage endpoint instead of thru auth token @zhao-oai

> #7611 fix(app-server): add will_retry to ErrorNotification @owenlin0

> #7615 chore: refactor to move Arc\<RwLock> concern outside exec_policy_for @bolinfest

> #7626 fix typo @zhao-oai

> #7629 fix(tui): add missing Ctrl+n/Ctrl+p support to ListSelectionView @pppp606

> #7638 fix: ignore ghost snapshots in token consumption @jif-oai

> #7645 Also load skills from repo root. @xl-openai

> #7651 fix: OTEL HTTP exporter panic and mTLS support @asm89

> #7652 Move justfile to repository root @joshka-oai

> #7654 fix: exec-server stream was erroring for large requests @bolinfest

> #7655 fix wrap behavior for long commands @zhao-oai

> #7660 Restore status header after stream recovery @joshka-oai

> #7665 docs: fix documentation of rmcp client flag @JaySabva

> #7669 fix(doc): TOML otel exporter example — multi-line inline table is invalid @448523760

> #7672 docs: Remove experimental_use_rmcp_client from config @JaySabva

> #7673 docs: point dev checks to just @voctory

> #7674 feat: linux codesign with sigstore @shijie-oai

> #7675 feat: windows codesign with Azure trusted signing @shijie-oai

> #7678 fix: clear out space on ubuntu runners before running Rust tests @bolinfest

> #7685 fix: refine the warning message and docs for deprecated tools config @gameofby

> #7711 Add formatting client version to the x.x.x style. @aibrahim-oai

> #7713 chore(deps): bump ts-rs from 11.0.1 to 11.1.0 in /codex-rs @dependabot[bot]

> #7714 chore(deps): bump derive_more from 2.0.1 to 2.1.0 in /codex-rs @dependabot[bot]

> #7715 chore(deps): bump insta from 1.43.2 to 1.44.3 in /codex-rs @dependabot[bot]

> #7716 chore(deps): bump wildmatch from 2.5.0 to 2.6.1 in /codex-rs @dependabot[bot]

> #7724 Fixed regression for chat endpoint; missing tools name caused litellm proxy to crash @etraut-openai

> #7745 Make the device auth instructions more clear. @mzeng-openai

> #7747 updating app server types to support execpoilcy amendment @zhao-oai

> #7748 Remove legacy ModelInfo and merge it with ModelFamily @aibrahim-oai

> #7749 fix: pre-main hardening logic must tolerate non-UTF-8 env vars @bolinfest

> #7753 Revert "feat: windows codesign with Azure trusted signing" @shijie-oai

> #7754 override instructions using ModelInfo @aibrahim-oai

Source: https://github.com/openai/codex/releases/tag/rust-v0.66.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2025-12-09-3-apps-and-integrations-changes-in-rust-v0-66-0|3 Apps and Integrations changes in rust-v0.66.0]] · Apps and Integrations
- [[Changes/Codex CLI/2025-12-09-2-account-and-access-changes-in-rust-v0-66-0|2 Account and Access changes in rust-v0.66.0]] · Account and Access
- [[Changes/Codex CLI/2025-12-09-3-editor-experience-changes-in-rust-v0-66-0|3 Editor Experience changes in rust-v0.66.0]] · Editor Experience
- [[Changes/Codex CLI/2025-12-09-2-interface-experience-changes-in-rust-v0-66-0|2 Interface Experience changes in rust-v0.66.0]] · Interface Experience
- [[Changes/Codex CLI/2025-12-09-7729-feat-add-is-mutating-detection-for-shell-command-handler-jif-oai|♯7729 feat: add is-mutating detection for shell command handler @jif-oai]] · Agent Mode
- [[Changes/Codex CLI/2025-12-09-7547-use-shared-check-sandboxing-pakrym-oai|♯7547 Use shared check sandboxing @pakrym-oai]] · Collaboration
- [[Changes/Codex CLI/2025-12-09-3-safety-and-privacy-changes-in-rust-v0-66-0|3 Safety and Privacy changes in rust-v0.66.0]] · Safety and Privacy
- [[Changes/Codex CLI/2025-12-09-8-model-support-changes-in-rust-v0-66-0|8 Model Support changes in rust-v0.66.0]] · Model Support
- [[Changes/Codex CLI/2025-12-09-2-developer-workflow-changes-in-rust-v0-66-0|2 Developer Workflow changes in rust-v0.66.0]] · Developer Workflow
- [[Changes/Codex CLI/2025-12-09-general-fixes-parallel-tool-call-chat-now-returns-correctly-ghost-snapshot-token|General fixes: parallel tool-call chat now returns correctly, ghost snapshot tokens…]] · Context Window
- [[Changes/Codex CLI/2025-12-09-4-mobile-and-desktop-changes-in-rust-v0-66-0|4 Mobile and Desktop changes in rust-v0.66.0]] · Mobile and Desktop
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2025-12-09-25d6e0&body=Card%3A%20Changes%2FCodex%20CLI%2F2025-12-09-52-other-changes-in-rust-v0-66-0.md%0ACard%20ID%3A%20codex-cli-2025-12-09-25d6e0%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.66.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->