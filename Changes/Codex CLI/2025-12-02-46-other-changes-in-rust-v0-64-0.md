---
card_id: codex-cli-2025-12-02-956476
date: '2025-12-02'
description: 'Codex CLI · 2025-12-02 · Other changes: 46 changes in 0.64.0 — Review
  flow is enhanced with a detached review mode, explicit enter and exit events, review…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 1c41e7f7872bdff6f7284834b980860877546a76b478f1d9f616a38c242a1a35
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2025-12-02-956476
  comparison: ''
  date: '2025-12-02'
  description: 'Codex CLI — 0.64.0: 46 other changes'
  evidence:
  - quote: Review flow is enhanced with a detached review mode, explicit enter and
      exit events, review thread IDs, and review history remains visible after rollout
      filtering changes.
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.64.0
  - quote: Tooling and ops gain follow-up v2 in the app-server test client, new config
      management utilities, and refreshed approvals documentation and quickstart placement.
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.64.0
  - quote: Delegate cancellation no longer hangs unified exec, early-exit sessions
      are cleaned up, and duplicate “waited” renderings are suppressed.
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.64.0
  - quote: recent_commits with limit zero now returns zero, and the NetBSD process-hardening
      build is unblocked.
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.64.0
  - quote: CLA allowlist now includes dependabot variants, and enterprises can skip
      upgrade checks and messages.
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.64.0
  - quote: Flaky tests are stabilized, session recycling is improved, and rollout
      session initialization surfaces errors for diagnosis.
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.64.0
  - quote: '[app-server] feat: expose gitInfo/cwd/etc. on Thread by @owenlin0 in #7060'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.64.0
  - quote: 'enable unified exec for experiments by @aibrahim-oai in #7118'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.64.0
  - quote: '[app-server] doc: approvals by @owenlin0 in #7105'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.64.0
  - quote: 'Windows: flag some invocations that launch browsers/URLs as dangerous
      by @iceweasel-oai in #7111'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.64.0
  - quote: 'move execpolicy quickstart by @zhao-oai in #7127'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.64.0
  - quote: 'chore: use proxy for encrypted summary by @jif-oai in #7252'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.64.0
  - quote: 'feat: unified exec basic pruning strategy by @jif-oai in #7239'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.64.0
  - quote: 'consolidate world-writable-directories scanning. by @iceweasel-oai in
      #7234'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.64.0
  - quote: '[feedback] Add source info into feedback metadata. by @mzeng-openai in
      #7140'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.64.0
  - quote: 'chore(deps): bump regex from 1.11.1 to 1.12.2 in /codex-rs by @dependabot[bot]
      in #7222'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.64.0
  - quote: 'chore(deps): bump actions/upload-artifact from 4 to 5 by @dependabot[bot]
      in #7229'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.64.0
  - quote: 'chore(deps): bump actions/checkout from 5 to 6 by @dependabot[bot] in
      #7230'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.64.0
  - quote: 'chore(deps): bump libc from 0.2.175 to 0.2.177 in /codex-rs by @dependabot[bot]
      in #7224'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.64.0
  - quote: 'chore(deps): bump webbrowser from 1.0.5 to 1.0.6 in /codex-rs by @dependabot[bot]
      in #7225'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.64.0
  - quote: 'Added alternate form of dependabot to CLA allow list by @etraut-openai
      in #7260'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.64.0
  - quote: 'Allow enterprises to skip upgrade checks and messages by @gpeal in #7213'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.64.0
  - quote: 'chore(ci): add cargo audit workflow and policy by @joshka-oai in #7108'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.64.0
  - quote: 'chore: add cargo-deny configuration by @joshka-oai in #7119'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.64.0
  - quote: '[app-server-test-client] add send-followup-v2 by @celia-oai in #7271'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.64.0
  - quote: 'feat[app-serve]: config management by @jif-oai in #7241'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.64.0
  - quote: 'feat: add custom env for unified exec process by @jif-oai in #7286'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.64.0
  - quote: '[app-server] feat: add thread_id and turn_id to item and error notifications
      by @owenlin0 in #7124'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.64.0
  - quote: 'chore: proper client extraction by @jif-oai in #6996'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.64.0
  - quote: 'tmp: drop flaky ubuntu by @jif-oai in #7300'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.64.0
  - quote: '[app-server] add thread/tokenUsage/updated v2 event by @celia-oai in #7268'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.64.0
  - quote: 'correctly recognize WorkspaceWrite policy on /approvals by @iceweasel-oai
      in #7301'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.64.0
  - quote: 'feat: update process ID for event handling by @jif-oai in #7261'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.64.0
  - quote: 'nit: drop file by @jif-oai in #7314'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.64.0
  - quote: 'chore: improve rollout session init errors by @jobchong in #7336'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.64.0
  - quote: 'feat: detached review by @jif-oai in #7292'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.64.0
  - quote: 'chore: better session recycling by @jif-oai in #7368'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.64.0
  - quote: 'chore(deps): bump arboard from 3.6.0 to 3.6.1 in /codex-rs by @dependabot[bot]
      in #7426'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.64.0
  - quote: 'chore(deps): bump serde_with from 3.14.0 to 3.16.1 in /codex-rs by @dependabot[bot]
      in #7422'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.64.0
  - quote: 'chore(deps): bump reqwest from 0.12.23 to 0.12.24 in /codex-rs by @dependabot[bot]
      in #7424'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.64.0
  - quote: 'chore(deps): bump tracing from 0.1.41 to 0.1.43 in /codex-rs by @dependabot[bot]
      in #7428'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.64.0
  - quote: 'chore(deps): bump image from 0.25.8 to 0.25.9 in /codex-rs by @dependabot[bot]
      in #7421'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.64.0
  - quote: '[app-server] add turn/plan/updated event by @celia-oai in #7329'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.64.0
  - quote: 'docs: clarify codex max defaults and xhigh availability by @kgruiz in
      #7449'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.64.0
  - quote: 'chore: update to rmcp@0.10.0 to pick up support for custom client notifications
      by @bolinfest in #7462'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.64.0
  - quote: '[app-server] Add ImageView item by @celia-oai in #7468'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.64.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 46-other-changes-in-rust-v0-64-0
  source_release: codex-cli-2025-12-02-rust-v0-64-0-github-266901625-82376886
  source_type: github_releases
  theme: uncategorized
  title: 46 other changes in rust-v0.64.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2025-12-02-rust-v0-64-0-github-266901625-82376886|codex-cli-2025-12-02-rust-v0-64-0-github-266901625-82376886]]'
source_type: github_releases
theme: uncategorized
title: 46 other changes in rust-v0.64.0
type: change
---

<!-- chronolog:begin region="header" -->
# 46 other changes in rust-v0.64.0

**Codex CLI** · 2025-12-02 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.64.0) · from [[Releases/Codex CLI/codex-cli-2025-12-02-rust-v0-64-0-github-266901625-82376886|0.64.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Review flow is enhanced with a detached review mode, explicit enter and exit events, review thread IDs, and review history remains visible after rollout filtering changes.

> Tooling and ops gain follow-up v2 in the app-server test client, new config management utilities, and refreshed approvals documentation and quickstart placement.

> Delegate cancellation no longer hangs unified exec, early-exit sessions are cleaned up, and duplicate “waited” renderings are suppressed.

> recent_commits with limit zero now returns zero, and the NetBSD process-hardening build is unblocked.

> CLA allowlist now includes dependabot variants, and enterprises can skip upgrade checks and messages.

> Flaky tests are stabilized, session recycling is improved, and rollout session initialization surfaces errors for diagnosis.

> [app-server] feat: expose gitInfo/cwd/etc. on Thread by @owenlin0 in #7060

> enable unified exec for experiments by @aibrahim-oai in #7118

> [app-server] doc: approvals by @owenlin0 in #7105

> Windows: flag some invocations that launch browsers/URLs as dangerous by @iceweasel-oai in #7111

> move execpolicy quickstart by @zhao-oai in #7127

> chore: use proxy for encrypted summary by @jif-oai in #7252

> feat: unified exec basic pruning strategy by @jif-oai in #7239

> consolidate world-writable-directories scanning. by @iceweasel-oai in #7234

> [feedback] Add source info into feedback metadata. by @mzeng-openai in #7140

> chore(deps): bump regex from 1.11.1 to 1.12.2 in /codex-rs by @dependabot[bot] in #7222

> chore(deps): bump actions/upload-artifact from 4 to 5 by @dependabot[bot] in #7229

> chore(deps): bump actions/checkout from 5 to 6 by @dependabot[bot] in #7230

> chore(deps): bump libc from 0.2.175 to 0.2.177 in /codex-rs by @dependabot[bot] in #7224

> chore(deps): bump webbrowser from 1.0.5 to 1.0.6 in /codex-rs by @dependabot[bot] in #7225

> Added alternate form of dependabot to CLA allow list by @etraut-openai in #7260

> Allow enterprises to skip upgrade checks and messages by @gpeal in #7213

> chore(ci): add cargo audit workflow and policy by @joshka-oai in #7108

> chore: add cargo-deny configuration by @joshka-oai in #7119

> [app-server-test-client] add send-followup-v2 by @celia-oai in #7271

> feat[app-serve]: config management by @jif-oai in #7241

> feat: add custom env for unified exec process by @jif-oai in #7286

> [app-server] feat: add thread_id and turn_id to item and error notifications by @owenlin0 in #7124

> chore: proper client extraction by @jif-oai in #6996

> tmp: drop flaky ubuntu by @jif-oai in #7300

> [app-server] add thread/tokenUsage/updated v2 event by @celia-oai in #7268

> correctly recognize WorkspaceWrite policy on /approvals by @iceweasel-oai in #7301

> feat: update process ID for event handling by @jif-oai in #7261

> nit: drop file by @jif-oai in #7314

> chore: improve rollout session init errors by @jobchong in #7336

> feat: detached review by @jif-oai in #7292

> chore: better session recycling by @jif-oai in #7368

> chore(deps): bump arboard from 3.6.0 to 3.6.1 in /codex-rs by @dependabot[bot] in #7426

> chore(deps): bump serde_with from 3.14.0 to 3.16.1 in /codex-rs by @dependabot[bot] in #7422

> chore(deps): bump reqwest from 0.12.23 to 0.12.24 in /codex-rs by @dependabot[bot] in #7424

> chore(deps): bump tracing from 0.1.41 to 0.1.43 in /codex-rs by @dependabot[bot] in #7428

> chore(deps): bump image from 0.25.8 to 0.25.9 in /codex-rs by @dependabot[bot] in #7421

> [app-server] add turn/plan/updated event by @celia-oai in #7329

> docs: clarify codex max defaults and xhigh availability by @kgruiz in #7449

> chore: update to rmcp@0.10.0 to pick up support for custom client notifications by @bolinfest in #7462

> [app-server] Add ImageView item by @celia-oai in #7468

Source: https://github.com/openai/codex/releases/tag/rust-v0.64.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2025-12-02-2-model-support-changes-in-rust-v0-64-0|2 Model Support changes in rust-v0.64.0]] · Model Support
- [[Changes/Codex CLI/2025-12-02-5-context-window-changes-in-rust-v0-64-0|5 Context Window changes in rust-v0.64.0]] · Context Window
- [[Changes/Codex CLI/2025-12-02-feat-support-login-as-an-option-on-shell-tool-mcp-by-bolinfest-in-7120|feat: support login as an option on shell-tool-mcp by @bolinfest in ♯7120]] · Account and Access
- [[Changes/Codex CLI/2025-12-02-3-apps-and-integrations-changes-in-rust-v0-64-0|3 Apps and Integrations changes in rust-v0.64.0]] · Apps and Integrations
- [[Changes/Codex CLI/2025-12-02-9-safety-and-privacy-changes-in-rust-v0-64-0|9 Safety and Privacy changes in rust-v0.64.0]] · Safety and Privacy
- [[Changes/Codex CLI/2025-12-02-powershell-apply-patch-parsing-is-corrected-and-apply-patch-tests-now-cover-shel|PowerShell apply_patch parsing is corrected, and apply_patch tests now cover…]] · Agent Mode
- [[Changes/Codex CLI/2025-12-02-4-developer-workflow-changes-in-rust-v0-64-0|4 Developer Workflow changes in rust-v0.64.0]] · Developer Workflow
- [[Changes/Codex CLI/2025-12-02-execution-gains-an-experimental-exp-model-unified-exec-pruning-to-limit-session|Execution gains an experimental “exp” model, unified exec pruning to limit session…]] · Mobile and Desktop
- [[Changes/Codex CLI/2025-12-02-3-editor-experience-changes-in-rust-v0-64-0|3 Editor Experience changes in rust-v0.64.0]] · Editor Experience
- [[Changes/Codex CLI/2025-12-02-chore-dedup-unified-exec-waited-rendering-by-jif-oai-in-7256|chore: dedup unified exec "waited" rendering by @jif-oai in ♯7256]] · Interface Experience
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2025-12-02-956476&body=Card%3A%20Changes%2FCodex%20CLI%2F2025-12-02-46-other-changes-in-rust-v0-64-0.md%0ACard%20ID%3A%20codex-cli-2025-12-02-956476%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.64.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->