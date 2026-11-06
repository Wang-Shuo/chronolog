---
card_id: gemini-cli-2026-02-04-808e06
date: '2026-02-04'
description: 'Gemini CLI · 2026-02-04 · Other changes: 72 changes in Release v0.27.0
  — remove fireAgent and beforeAgent hook by @ishaanxgupta in…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: a4da15aad497a16c4c3ca9795e1e27f4a1869c55bcd8153de676039eef467749
product: gemini-cli
product_name: Gemini CLI
record:
  card_id: gemini-cli-2026-02-04-808e06
  comparison: ''
  date: '2026-02-04'
  description: 'Gemini CLI — Release v0.27.0: 72 other changes'
  evidence:
  - quote: remove fireAgent and beforeAgent hook by @ishaanxgupta in https://github.com/google-gemini/gemini-cli/pull/16919
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: Remove unused modelHooks and toolHooks by @ved015 in https://github.com/google-gemini/gemini-cli/pull/17115
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: 'feat(cli): sanitize ANSI escape sequences in non-interactive output by
      @sehoon38 in https://github.com/google-gemini/gemini-cli/pull/17172'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: Update Attempt text to Retry when showing the retry happening to the …
      by @sehoon38 in https://github.com/google-gemini/gemini-cli/pull/17178
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: 'chore(skills): update pr-creator skill workflow by @sehoon38 in https://github.com/google-gemini/gemini-cli/pull/17180'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: 'chore(release): bump version to 0.27.0-nightly.20260121.97aac696f by @gemini-cli-robot
      in https://github.com/google-gemini/gemini-cli/pull/17181'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: Remove other rewind reference in docs by @chrstnb in https://github.com/google-gemini/gemini-cli/pull/17149
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: 'feat(skills): add code-reviewer skill by @sehoon38 in https://github.com/google-gemini/gemini-cli/pull/17187'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: 'feat(plan): refactor TestRig and eval helper to support configurable approval
      modes by @jerop in https://github.com/google-gemini/gemini-cli/pull/17171'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: 'feat(workflows): support recursive workstream labeling and new IDs by
      @bdmorgan in https://github.com/google-gemini/gemini-cli/pull/17207'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: 'Docs: Update changelogs for v.0.25.0 and v0.26.0-preview.0 releases. by
      @g-samroberts in https://github.com/google-gemini/gemini-cli/pull/17215'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: 'feat(cli): improve skill enablement/disablement verbiage by @NTaylorMullen
      in https://github.com/google-gemini/gemini-cli/pull/17192'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: 'feat(core): support dynamic variable substitution in system prompt override
      by @NTaylorMullen in https://github.com/google-gemini/gemini-cli/pull/17042'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: 'Docs: Marking for experimental features by @jkcinouye in https://github.com/google-gemini/gemini-cli/pull/16760'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: 'feat(plan): add approval mode instructions to system prompt by @jerop
      in https://github.com/google-gemini/gemini-cli/pull/17151'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: 'feat(core): enable disableLLMCorrection by default by @SandyTao520 in
      https://github.com/google-gemini/gemini-cli/pull/17223'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: drain stdin on exit by @scidomino in https://github.com/google-gemini/gemini-cli/pull/17241
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: 'refactor(cli): decouple UI from live tool execution via ToolActionsContext
      by @abhipatel12 in https://github.com/google-gemini/gemini-cli/pull/17183'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: 'feat(config): default enableEventDrivenScheduler to true by @abhipatel12
      in https://github.com/google-gemini/gemini-cli/pull/17211'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: 'feat: replace large text pastes with [Pasted Text: X lines] placeholder
      by @jackwotherspoon in https://github.com/google-gemini/gemini-cli/pull/16422'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: Enable the ability to queue specific nightly eval tests by @gundermanc
      in https://github.com/google-gemini/gemini-cli/pull/17262
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: 'refactor: improve large text paste placeholder by @jacob314 in https://github.com/google-gemini/gemini-cli/pull/17269'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: Added image pasting capabilities for Wayland and X11 on Linux by @devr0306
      in https://github.com/google-gemini/gemini-cli/pull/17144
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: 'feat: add AskUser tool schema by @jackwotherspoon in https://github.com/google-gemini/gemini-cli/pull/16988'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: Remove redundant calls setting linuxClipboardTool. getUserLinuxClipboardTool()
      now handles the caching internally by @jacob314 in https://github.com/google-gemini/gemini-cli/pull/17320
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: 'ci: allow failure in evals-nightly run step by @gundermanc in https://github.com/google-gemini/gemini-cli/pull/17319'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: Emit correct newline type return by @scidomino in https://github.com/google-gemini/gemini-cli/pull/17331
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: 'New skill: docs-writer by @g-samroberts in https://github.com/google-gemini/gemini-cli/pull/17268'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: Disable tips after 10 runs by @Adib234 in https://github.com/google-gemini/gemini-cli/pull/17101
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: 'feat(core): Remove legacy settings. by @joshualitt in https://github.com/google-gemini/gemini-cli/pull/17244'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: 'feat(plan): add ''communicate'' tool kind by @jerop in https://github.com/google-gemini/gemini-cli/pull/17341'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: 'feat(plan): update UI Theme for Plan Mode by @Adib234 in https://github.com/google-gemini/gemini-cli/pull/17243'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: 'Refactor: Migrate CLI `appEvents` to Core `coreEvents` by @Adib234 in
      https://github.com/google-gemini/gemini-cli/pull/15737'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: Update Code Wiki README badge by @PatoBeltran in https://github.com/google-gemini/gemini-cli/pull/15229
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: 'chore(refactor): extract BaseSettingsDialog component by @SandyTao520
      in https://github.com/google-gemini/gemini-cli/pull/17369'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: 'feat: add AskUserDialog for UI component of AskUser tool by @jackwotherspoon
      in https://github.com/google-gemini/gemini-cli/pull/17344'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: 'feat(plan): implement persistent `approvalMode` setting by @Adib234 in
      https://github.com/google-gemini/gemini-cli/pull/17350'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: 'feat(ui): Move keyboard handling into BaseSettingsDialog by @SandyTao520
      in https://github.com/google-gemini/gemini-cli/pull/17404'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: 'feat(cli): Moves tool confirmations to a queue UX by @abhipatel12 in https://github.com/google-gemini/gemini-cli/pull/17276'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: 'feat: Enforce unified folder trust for /directory add by @galz10 in https://github.com/google-gemini/gemini-cli/pull/17359'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: migrate fireToolNotificationHook to hookSystem by @ved015 in https://github.com/google-gemini/gemini-cli/pull/17398
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: Clean up dead code by @scidomino in https://github.com/google-gemini/gemini-cli/pull/17443
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: 'feat(workflow): expand stale-exempt labels to include help wanted and
      Public Roadmap by @bdmorgan in https://github.com/google-gemini/gemini-cli/pull/17459'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: 'chore(workflow): remove redundant label-enforcer workflow by @bdmorgan
      in https://github.com/google-gemini/gemini-cli/pull/17460'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: Resolves the confusing error message `ripgrep exited with code null that
      occurs when a search operation is cancelled or aborted by @maximmasiutin in
      https://github.com/google-gemini/gemini-cli/pull/14267
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: 'docs: Add instructions for MacPorts and uninstall instructions for Homebrew
      by @breun in https://github.com/google-gemini/gemini-cli/pull/17412'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: Follow up to "enableInteractiveShell for external tooling relying on a2a
      server" by @DavidAPierce in https://github.com/google-gemini/gemini-cli/pull/17130
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: 'feat(cli): add quick clear input shortcuts in vim mode by @harshanadim
      in https://github.com/google-gemini/gemini-cli/pull/17470'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: 'Docs: Refactor left nav on the website by @jkcinouye in https://github.com/google-gemini/gemini-cli/pull/17558'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: 'feat(plan): add persistent plan file storage by @jerop in https://github.com/google-gemini/gemini-cli/pull/17563'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: 'feat(ui): add solid background color option for input prompt by @jacob314
      in https://github.com/google-gemini/gemini-cli/pull/16563'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: 'feat(cli): add global setting to disable UI spinners by @galz10 in https://github.com/google-gemini/gemini-cli/pull/17234'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: 'test(core): fix tests in windows by @scidomino in https://github.com/google-gemini/gemini-cli/pull/17592'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: Always map mac keys, even on other platforms by @scidomino in https://github.com/google-gemini/gemini-cli/pull/17618
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: Ctrl-O by @jacob314 in https://github.com/google-gemini/gemini-cli/pull/17617
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: 'feat(plan): update cycling order of approval modes by @Adib234 in https://github.com/google-gemini/gemini-cli/pull/17622'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: 'feat: add double-click to expand/collapse large paste placeholders by
      @jackwotherspoon in https://github.com/google-gemini/gemini-cli/pull/17471'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: 'chore(core): delete legacy nonInteractiveToolExecutor by @abhipatel12
      in https://github.com/google-gemini/gemini-cli/pull/17573'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: paste transform followup by @jacob314 in https://github.com/google-gemini/gemini-cli/pull/17624
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: 'refactor: rename formatMemoryUsage to formatBytes by @Nubebuster in https://github.com/google-gemini/gemini-cli/pull/14997'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: Change formatting to prevent UI redressing attacks by @scidomino in https://github.com/google-gemini/gemini-cli/pull/17611
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: revert bad changes to tests by @scidomino in https://github.com/google-gemini/gemini-cli/pull/17673
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: 'feat(cli): show candidate issue state reason and duplicate status in triage
      by @sehoon38 in https://github.com/google-gemini/gemini-cli/pull/17676'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: 'feat: wire up `AskUserTool` with dialog by @jackwotherspoon in https://github.com/google-gemini/gemini-cli/pull/17411'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: Update docs-writer skill for editing and add style guide for reference.
      by @g-samroberts in https://github.com/google-gemini/gemini-cli/pull/17669
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: 'feat(plan): enable `AskUser` tool in `Plan` mode for clarifying questions
      by @jerop in https://github.com/google-gemini/gemini-cli/pull/17694'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: 'refactor(core): centralize path validation and allow temp dir access for
      tools by @NTaylorMullen in https://github.com/google-gemini/gemini-cli/pull/17185'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: 'refactor(cli): keyboard handling and AskUserDialog by @jacob314 in https://github.com/google-gemini/gemini-cli/pull/17414'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: feat(ux) Expandable (ctrl-O) and scrollable approvals in alternate buffer
      mode. by @jacob314 in https://github.com/google-gemini/gemini-cli/pull/17640
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: 'feat(skills): promote skills settings to stable by @abhipatel12 in https://github.com/google-gemini/gemini-cli/pull/17713'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: 'docs(skills): remove experimental labels and update tutorials by @abhipatel12
      in https://github.com/google-gemini/gemini-cli/pull/17714'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  - quote: Add support for an additional exclusion file besides .gitignore and .geminiignore
      by @alisa-alisa in https://github.com/google-gemini/gemini-cli/pull/16487
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: gemini-cli
  product_name: Gemini CLI
  slug: 72-other-changes-in-v0-27-0
  source_release: gemini-cli-2026-02-04-v0-27-0-github-282779403-9d866835
  source_type: github_releases
  theme: uncategorized
  title: 72 other changes in v0.27.0
  type: change
source_release: '[[Releases/Gemini CLI/gemini-cli-2026-02-04-v0-27-0-github-282779403-9d866835|gemini-cli-2026-02-04-v0-27-0-github-282779403-9d866835]]'
source_type: github_releases
theme: uncategorized
title: 72 other changes in v0.27.0
type: change
---

<!-- chronolog:begin region="header" -->
# 72 other changes in v0.27.0

**Gemini CLI** · 2026-02-04 · Other changes · Digest · [Official source](https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0) · from [[Releases/Gemini CLI/gemini-cli-2026-02-04-v0-27-0-github-282779403-9d866835|Release v0.27.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> remove fireAgent and beforeAgent hook by @ishaanxgupta in https://github.com/google-gemini/gemini-cli/pull/16919

> Remove unused modelHooks and toolHooks by @ved015 in https://github.com/google-gemini/gemini-cli/pull/17115

> feat(cli): sanitize ANSI escape sequences in non-interactive output by @sehoon38 in https://github.com/google-gemini/gemini-cli/pull/17172

> Update Attempt text to Retry when showing the retry happening to the … by @sehoon38 in https://github.com/google-gemini/gemini-cli/pull/17178

> chore(skills): update pr-creator skill workflow by @sehoon38 in https://github.com/google-gemini/gemini-cli/pull/17180

> chore(release): bump version to 0.27.0-nightly.20260121.97aac696f by @gemini-cli-robot in https://github.com/google-gemini/gemini-cli/pull/17181

> Remove other rewind reference in docs by @chrstnb in https://github.com/google-gemini/gemini-cli/pull/17149

> feat(skills): add code-reviewer skill by @sehoon38 in https://github.com/google-gemini/gemini-cli/pull/17187

> feat(plan): refactor TestRig and eval helper to support configurable approval modes by @jerop in https://github.com/google-gemini/gemini-cli/pull/17171

> feat(workflows): support recursive workstream labeling and new IDs by @bdmorgan in https://github.com/google-gemini/gemini-cli/pull/17207

> Docs: Update changelogs for v.0.25.0 and v0.26.0-preview.0 releases. by @g-samroberts in https://github.com/google-gemini/gemini-cli/pull/17215

> feat(cli): improve skill enablement/disablement verbiage by @NTaylorMullen in https://github.com/google-gemini/gemini-cli/pull/17192

> feat(core): support dynamic variable substitution in system prompt override by @NTaylorMullen in https://github.com/google-gemini/gemini-cli/pull/17042

> Docs: Marking for experimental features by @jkcinouye in https://github.com/google-gemini/gemini-cli/pull/16760

> feat(plan): add approval mode instructions to system prompt by @jerop in https://github.com/google-gemini/gemini-cli/pull/17151

> feat(core): enable disableLLMCorrection by default by @SandyTao520 in https://github.com/google-gemini/gemini-cli/pull/17223

> drain stdin on exit by @scidomino in https://github.com/google-gemini/gemini-cli/pull/17241

> refactor(cli): decouple UI from live tool execution via ToolActionsContext by @abhipatel12 in https://github.com/google-gemini/gemini-cli/pull/17183

> feat(config): default enableEventDrivenScheduler to true by @abhipatel12 in https://github.com/google-gemini/gemini-cli/pull/17211

> feat: replace large text pastes with [Pasted Text: X lines] placeholder by @jackwotherspoon in https://github.com/google-gemini/gemini-cli/pull/16422

> Enable the ability to queue specific nightly eval tests by @gundermanc in https://github.com/google-gemini/gemini-cli/pull/17262

> refactor: improve large text paste placeholder by @jacob314 in https://github.com/google-gemini/gemini-cli/pull/17269

> Added image pasting capabilities for Wayland and X11 on Linux by @devr0306 in https://github.com/google-gemini/gemini-cli/pull/17144

> feat: add AskUser tool schema by @jackwotherspoon in https://github.com/google-gemini/gemini-cli/pull/16988

> Remove redundant calls setting linuxClipboardTool. getUserLinuxClipboardTool() now handles the caching internally by @jacob314 in https://github.com/google-gemini/gemini-cli/pull/17320

> ci: allow failure in evals-nightly run step by @gundermanc in https://github.com/google-gemini/gemini-cli/pull/17319

> Emit correct newline type return by @scidomino in https://github.com/google-gemini/gemini-cli/pull/17331

> New skill: docs-writer by @g-samroberts in https://github.com/google-gemini/gemini-cli/pull/17268

> Disable tips after 10 runs by @Adib234 in https://github.com/google-gemini/gemini-cli/pull/17101

> feat(core): Remove legacy settings. by @joshualitt in https://github.com/google-gemini/gemini-cli/pull/17244

> feat(plan): add 'communicate' tool kind by @jerop in https://github.com/google-gemini/gemini-cli/pull/17341

> feat(plan): update UI Theme for Plan Mode by @Adib234 in https://github.com/google-gemini/gemini-cli/pull/17243

> Refactor: Migrate CLI `appEvents` to Core `coreEvents` by @Adib234 in https://github.com/google-gemini/gemini-cli/pull/15737

> Update Code Wiki README badge by @PatoBeltran in https://github.com/google-gemini/gemini-cli/pull/15229

> chore(refactor): extract BaseSettingsDialog component by @SandyTao520 in https://github.com/google-gemini/gemini-cli/pull/17369

> feat: add AskUserDialog for UI component of AskUser tool by @jackwotherspoon in https://github.com/google-gemini/gemini-cli/pull/17344

> feat(plan): implement persistent `approvalMode` setting by @Adib234 in https://github.com/google-gemini/gemini-cli/pull/17350

> feat(ui): Move keyboard handling into BaseSettingsDialog by @SandyTao520 in https://github.com/google-gemini/gemini-cli/pull/17404

> feat(cli): Moves tool confirmations to a queue UX by @abhipatel12 in https://github.com/google-gemini/gemini-cli/pull/17276

> feat: Enforce unified folder trust for /directory add by @galz10 in https://github.com/google-gemini/gemini-cli/pull/17359

> migrate fireToolNotificationHook to hookSystem by @ved015 in https://github.com/google-gemini/gemini-cli/pull/17398

> Clean up dead code by @scidomino in https://github.com/google-gemini/gemini-cli/pull/17443

> feat(workflow): expand stale-exempt labels to include help wanted and Public Roadmap by @bdmorgan in https://github.com/google-gemini/gemini-cli/pull/17459

> chore(workflow): remove redundant label-enforcer workflow by @bdmorgan in https://github.com/google-gemini/gemini-cli/pull/17460

> Resolves the confusing error message `ripgrep exited with code null that occurs when a search operation is cancelled or aborted by @maximmasiutin in https://github.com/google-gemini/gemini-cli/pull/14267

> docs: Add instructions for MacPorts and uninstall instructions for Homebrew by @breun in https://github.com/google-gemini/gemini-cli/pull/17412

> Follow up to "enableInteractiveShell for external tooling relying on a2a server" by @DavidAPierce in https://github.com/google-gemini/gemini-cli/pull/17130

> feat(cli): add quick clear input shortcuts in vim mode by @harshanadim in https://github.com/google-gemini/gemini-cli/pull/17470

> Docs: Refactor left nav on the website by @jkcinouye in https://github.com/google-gemini/gemini-cli/pull/17558

> feat(plan): add persistent plan file storage by @jerop in https://github.com/google-gemini/gemini-cli/pull/17563

> feat(ui): add solid background color option for input prompt by @jacob314 in https://github.com/google-gemini/gemini-cli/pull/16563

> feat(cli): add global setting to disable UI spinners by @galz10 in https://github.com/google-gemini/gemini-cli/pull/17234

> test(core): fix tests in windows by @scidomino in https://github.com/google-gemini/gemini-cli/pull/17592

> Always map mac keys, even on other platforms by @scidomino in https://github.com/google-gemini/gemini-cli/pull/17618

> Ctrl-O by @jacob314 in https://github.com/google-gemini/gemini-cli/pull/17617

> feat(plan): update cycling order of approval modes by @Adib234 in https://github.com/google-gemini/gemini-cli/pull/17622

> feat: add double-click to expand/collapse large paste placeholders by @jackwotherspoon in https://github.com/google-gemini/gemini-cli/pull/17471

> chore(core): delete legacy nonInteractiveToolExecutor by @abhipatel12 in https://github.com/google-gemini/gemini-cli/pull/17573

> paste transform followup by @jacob314 in https://github.com/google-gemini/gemini-cli/pull/17624

> refactor: rename formatMemoryUsage to formatBytes by @Nubebuster in https://github.com/google-gemini/gemini-cli/pull/14997

> Change formatting to prevent UI redressing attacks by @scidomino in https://github.com/google-gemini/gemini-cli/pull/17611

> revert bad changes to tests by @scidomino in https://github.com/google-gemini/gemini-cli/pull/17673

> feat(cli): show candidate issue state reason and duplicate status in triage by @sehoon38 in https://github.com/google-gemini/gemini-cli/pull/17676

> feat: wire up `AskUserTool` with dialog by @jackwotherspoon in https://github.com/google-gemini/gemini-cli/pull/17411

> Update docs-writer skill for editing and add style guide for reference. by @g-samroberts in https://github.com/google-gemini/gemini-cli/pull/17669

> feat(plan): enable `AskUser` tool in `Plan` mode for clarifying questions by @jerop in https://github.com/google-gemini/gemini-cli/pull/17694

> refactor(core): centralize path validation and allow temp dir access for tools by @NTaylorMullen in https://github.com/google-gemini/gemini-cli/pull/17185

> refactor(cli): keyboard handling and AskUserDialog by @jacob314 in https://github.com/google-gemini/gemini-cli/pull/17414

> feat(ux) Expandable (ctrl-O) and scrollable approvals in alternate buffer mode. by @jacob314 in https://github.com/google-gemini/gemini-cli/pull/17640

> feat(skills): promote skills settings to stable by @abhipatel12 in https://github.com/google-gemini/gemini-cli/pull/17713

> docs(skills): remove experimental labels and update tutorials by @abhipatel12 in https://github.com/google-gemini/gemini-cli/pull/17714

> Add support for an additional exclusion file besides .gitignore and .geminiignore by @alisa-alisa in https://github.com/google-gemini/gemini-cli/pull/16487

Source: https://github.com/google-gemini/gemini-cli/releases/tag/v0.27.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Gemini CLI/2026-02-04-11-developer-workflow-changes-in-v0-27-0|11 Developer Workflow changes in v0.27.0]] · Developer Workflow
- [[Changes/Gemini CLI/2026-02-04-14-apps-and-integrations-changes-in-v0-27-0|14 Apps and Integrations changes in v0.27.0]] · Apps and Integrations
- [[Changes/Gemini CLI/2026-02-04-4-interface-experience-changes-in-v0-27-0|4 Interface Experience changes in v0.27.0]] · Interface Experience
- [[Changes/Gemini CLI/2026-02-04-security-hooks-wrap-hook-injected-context-in-distinct-xml-tags-by-yunaseoul-in-h|security(hooks): Wrap hook-injected context in distinct XML tags]] · Safety and Privacy
- [[Changes/Gemini CLI/2026-02-04-4-editor-experience-changes-in-v0-27-0|4 Editor Experience changes in v0.27.0]] · Editor Experience
- [[Changes/Gemini CLI/2026-02-04-3-automation-and-scheduling-changes-in-v0-27-0|3 Automation and Scheduling changes in v0.27.0]] · Automation and Scheduling
- [[Changes/Gemini CLI/2026-02-04-6-model-support-changes-in-v0-27-0|6 Model Support changes in v0.27.0]] · Model Support
- [[Changes/Gemini CLI/2026-02-04-15-agent-mode-changes-in-v0-27-0|15 Agent Mode changes in v0.27.0]] · Agent Mode
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20gemini-cli-2026-02-04-808e06&body=Card%3A%20Changes%2FGemini%20CLI%2F2026-02-04-72-other-changes-in-v0-27-0.md%0ACard%20ID%3A%20gemini-cli-2026-02-04-808e06%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgoogle-gemini%2Fgemini-cli%2Freleases%2Ftag%2Fv0.27.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->