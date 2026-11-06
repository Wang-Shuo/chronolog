---
card_id: codex-cli-2025-10-30-576b56
date: '2025-10-30'
description: 'Codex CLI · 2025-10-30 · Other changes: 59 changes in 0.52.0 — Execute
  commands directly with `!<cmd>`'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: c76af39165f6f66c69c75529168c437a5e65824845200035cdd29e0efb7a0837
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2025-10-30-576b56
  comparison: ''
  date: '2025-10-30'
  description: 'Codex CLI — 0.52.0: 59 other changes'
  evidence:
  - quote: Execute commands directly with `!<cmd>`
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.52.0
  - quote: 'Auth: new CLI auth storage abstraction with keyring support and configurable
      backend.'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.52.0
  - quote: 'App server: GetConversationSummary RPC; fetch/resume conversation summaries
      by id; refined account/protocol types.'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.52.0
  - quote: 'Execution/events: item streaming events; ghost commits; clearer deprecation
      warnings; better token refresh handling and logs.'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.52.0
  - quote: Log HTTP Version in https://github.com/openai/codex/pull/5475
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.52.0
  - quote: 'feat: local tokenizer in https://github.com/openai/codex/pull/5508'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.52.0
  - quote: 'chore: drop approve all in https://github.com/openai/codex/pull/5503'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.52.0
  - quote: 'chore: clean spec tests in https://github.com/openai/codex/pull/5517'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.52.0
  - quote: '[app-server] send account/rateLimits/updated notifications in https://github.com/openai/codex/pull/5477'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.52.0
  - quote: '[app-server] add new account method API stubs in https://github.com/openai/codex/pull/5527'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.52.0
  - quote: 'chore: clean handle_container_exec_with_params in https://github.com/openai/codex/pull/5516'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.52.0
  - quote: 'tui: show aggregated output in display in https://github.com/openai/codex/pull/5539'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.52.0
  - quote: Handle cancelling/aborting while processing a turn in https://github.com/openai/codex/pull/5543
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.52.0
  - quote: 'chore: testing on apply_path in https://github.com/openai/codex/pull/5557'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.52.0
  - quote: 'feat: use actual tokenizer for unified_exec truncation in https://github.com/openai/codex/pull/5514'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.52.0
  - quote: 'feat: end events on unified exec in https://github.com/openai/codex/pull/5551'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.52.0
  - quote: Use Option symbol for mac key hints in https://github.com/openai/codex/pull/5582
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.52.0
  - quote: Moving token_info to ConversationHistory in https://github.com/openai/codex/pull/5581
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.52.0
  - quote: adding messaging for stale rate limits + when no rate limits are cached
      in https://github.com/openai/codex/pull/5570
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.52.0
  - quote: Add CodexHttpClient wrapper with request logging in https://github.com/openai/codex/pull/5564
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.52.0
  - quote: Add instruction for upgrading codex with brew in https://github.com/openai/codex/pull/5640
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.52.0
  - quote: Log more types of request IDs in https://github.com/openai/codex/pull/5645
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.52.0
  - quote: '[codex][app-server] introduce codex/event/raw_item events in https://github.com/openai/codex/pull/5578'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.52.0
  - quote: Improve feedback in https://github.com/openai/codex/pull/5661
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.52.0
  - quote: Followup feedback in https://github.com/openai/codex/pull/5663
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.52.0
  - quote: Skip flaky test in https://github.com/openai/codex/pull/5680
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.52.0
  - quote: Reduced runtime of unit test that was taking multiple minutes in https://github.com/openai/codex/pull/5688
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.52.0
  - quote: Add feedback upload request handling in https://github.com/openai/codex/pull/5682
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.52.0
  - quote: 'feat: undo wiring in https://github.com/openai/codex/pull/5630'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.52.0
  - quote: 'feat: TUI undo op in https://github.com/openai/codex/pull/5629'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.52.0
  - quote: 'nit: doc on session task in https://github.com/openai/codex/pull/5809'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.52.0
  - quote: 'chore: undo nits in https://github.com/openai/codex/pull/5631'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.52.0
  - quote: 'feat: introduce GetConversationSummary RPC in https://github.com/openai/codex/pull/5803'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.52.0
  - quote: 'feat: return an error if unknown enabled/disabled feature in https://github.com/openai/codex/pull/5817'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.52.0
  - quote: Made token refresh code resilient to missing id_token in https://github.com/openai/codex/pull/5782
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.52.0
  - quote: '[Auth] Introduce New Auth Storage Abstraction for Codex CLI in https://github.com/openai/codex/pull/5569'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.52.0
  - quote: '[Auth] Add keyring support for Codex CLI in https://github.com/openai/codex/pull/5591'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.52.0
  - quote: Centralize truncation in conversation history in https://github.com/openai/codex/pull/5652
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.52.0
  - quote: '[Auth] Choose which auth storage to use based on config in https://github.com/openai/codex/pull/5792'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.52.0
  - quote: 'tui: show queued messages during response stream in https://github.com/openai/codex/pull/5540'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.52.0
  - quote: 'revert #5812 release file in https://github.com/openai/codex/pull/5887'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.52.0
  - quote: remove beta experimental header in https://github.com/openai/codex/pull/5892
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.52.0
  - quote: verify mime type of images in https://github.com/openai/codex/pull/5888
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.52.0
  - quote: '[app-server] Annotate more exported types with a title in https://github.com/openai/codex/pull/5879'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.52.0
  - quote: '[App Server] Allow fetching or resuming a conversation summary from the
      conversation id in https://github.com/openai/codex/pull/5890'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.52.0
  - quote: '[codex][app-server] resume conversation from history in https://github.com/openai/codex/pull/5893'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.52.0
  - quote: 'feat: deprecation warning in https://github.com/openai/codex/pull/5825'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.52.0
  - quote: Add missing "nullable" macro to protocol structs that contain optional
      fields in https://github.com/openai/codex/pull/5901
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.52.0
  - quote: Add a wrapper around raw response items in https://github.com/openai/codex/pull/5923
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.52.0
  - quote: Delegate review to codex instance in https://github.com/openai/codex/pull/5572
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.52.0
  - quote: Add item streaming events in https://github.com/openai/codex/pull/5546
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.52.0
  - quote: asdf in https://github.com/openai/codex/pull/5940
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.52.0
  - quote: Send delegate header in https://github.com/openai/codex/pull/5942
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.52.0
  - quote: 'chore: unify config crates in https://github.com/openai/codex/pull/5958'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.52.0
  - quote: Pass initial history as an optional to codex delegate in https://github.com/openai/codex/pull/5950
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.52.0
  - quote: 'nit: log rmcp_client in https://github.com/openai/codex/pull/5978'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.52.0
  - quote: 'chore: testing on freeform apply_patch in https://github.com/openai/codex/pull/5952'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.52.0
  - quote: '[codex] add developer instructions in https://github.com/openai/codex/pull/5897'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.52.0
  - quote: '[app-server] remove serde(skip_serializing_if = \"Option::is_none\") annotations
      in https://github.com/openai/codex/pull/5939'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.52.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 59-other-changes-in-rust-v0-52-0
  source_release: codex-cli-2025-10-30-rust-v0-52-0-github-258584762-83f2b559
  source_type: github_releases
  theme: uncategorized
  title: 59 other changes in rust-v0.52.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2025-10-30-rust-v0-52-0-github-258584762-83f2b559|codex-cli-2025-10-30-rust-v0-52-0-github-258584762-83f2b559]]'
source_type: github_releases
theme: uncategorized
title: 59 other changes in rust-v0.52.0
type: change
---

<!-- chronolog:begin region="header" -->
# 59 other changes in rust-v0.52.0

**Codex CLI** · 2025-10-30 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.52.0) · from [[Releases/Codex CLI/codex-cli-2025-10-30-rust-v0-52-0-github-258584762-83f2b559|0.52.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Execute commands directly with `!<cmd>`

> Auth: new CLI auth storage abstraction with keyring support and configurable backend.

> App server: GetConversationSummary RPC; fetch/resume conversation summaries by id; refined account/protocol types.

> Execution/events: item streaming events; ghost commits; clearer deprecation warnings; better token refresh handling and logs.

> Log HTTP Version in https://github.com/openai/codex/pull/5475

> feat: local tokenizer in https://github.com/openai/codex/pull/5508

> chore: drop approve all in https://github.com/openai/codex/pull/5503

> chore: clean spec tests in https://github.com/openai/codex/pull/5517

> [app-server] send account/rateLimits/updated notifications in https://github.com/openai/codex/pull/5477

> [app-server] add new account method API stubs in https://github.com/openai/codex/pull/5527

> chore: clean handle_container_exec_with_params in https://github.com/openai/codex/pull/5516

> tui: show aggregated output in display in https://github.com/openai/codex/pull/5539

> Handle cancelling/aborting while processing a turn in https://github.com/openai/codex/pull/5543

> chore: testing on apply_path in https://github.com/openai/codex/pull/5557

> feat: use actual tokenizer for unified_exec truncation in https://github.com/openai/codex/pull/5514

> feat: end events on unified exec in https://github.com/openai/codex/pull/5551

> Use Option symbol for mac key hints in https://github.com/openai/codex/pull/5582

> Moving token_info to ConversationHistory in https://github.com/openai/codex/pull/5581

> adding messaging for stale rate limits + when no rate limits are cached in https://github.com/openai/codex/pull/5570

> Add CodexHttpClient wrapper with request logging in https://github.com/openai/codex/pull/5564

> Add instruction for upgrading codex with brew in https://github.com/openai/codex/pull/5640

> Log more types of request IDs in https://github.com/openai/codex/pull/5645

> [codex][app-server] introduce codex/event/raw_item events in https://github.com/openai/codex/pull/5578

> Improve feedback in https://github.com/openai/codex/pull/5661

> Followup feedback in https://github.com/openai/codex/pull/5663

> Skip flaky test in https://github.com/openai/codex/pull/5680

> Reduced runtime of unit test that was taking multiple minutes in https://github.com/openai/codex/pull/5688

> Add feedback upload request handling in https://github.com/openai/codex/pull/5682

> feat: undo wiring in https://github.com/openai/codex/pull/5630

> feat: TUI undo op in https://github.com/openai/codex/pull/5629

> nit: doc on session task in https://github.com/openai/codex/pull/5809

> chore: undo nits in https://github.com/openai/codex/pull/5631

> feat: introduce GetConversationSummary RPC in https://github.com/openai/codex/pull/5803

> feat: return an error if unknown enabled/disabled feature in https://github.com/openai/codex/pull/5817

> Made token refresh code resilient to missing id_token in https://github.com/openai/codex/pull/5782

> [Auth] Introduce New Auth Storage Abstraction for Codex CLI in https://github.com/openai/codex/pull/5569

> [Auth] Add keyring support for Codex CLI in https://github.com/openai/codex/pull/5591

> Centralize truncation in conversation history in https://github.com/openai/codex/pull/5652

> [Auth] Choose which auth storage to use based on config in https://github.com/openai/codex/pull/5792

> tui: show queued messages during response stream in https://github.com/openai/codex/pull/5540

> revert #5812 release file in https://github.com/openai/codex/pull/5887

> remove beta experimental header in https://github.com/openai/codex/pull/5892

> verify mime type of images in https://github.com/openai/codex/pull/5888

> [app-server] Annotate more exported types with a title in https://github.com/openai/codex/pull/5879

> [App Server] Allow fetching or resuming a conversation summary from the conversation id in https://github.com/openai/codex/pull/5890

> [codex][app-server] resume conversation from history in https://github.com/openai/codex/pull/5893

> feat: deprecation warning in https://github.com/openai/codex/pull/5825

> Add missing "nullable" macro to protocol structs that contain optional fields in https://github.com/openai/codex/pull/5901

> Add a wrapper around raw response items in https://github.com/openai/codex/pull/5923

> Delegate review to codex instance in https://github.com/openai/codex/pull/5572

> Add item streaming events in https://github.com/openai/codex/pull/5546

> asdf in https://github.com/openai/codex/pull/5940

> Send delegate header in https://github.com/openai/codex/pull/5942

> chore: unify config crates in https://github.com/openai/codex/pull/5958

> Pass initial history as an optional to codex delegate in https://github.com/openai/codex/pull/5950

> nit: log rmcp_client in https://github.com/openai/codex/pull/5978

> chore: testing on freeform apply_patch in https://github.com/openai/codex/pull/5952

> [codex] add developer instructions in https://github.com/openai/codex/pull/5897

> [app-server] remove serde(skip_serializing_if = \"Option::is_none\") annotations in https://github.com/openai/codex/pull/5939

Source: https://github.com/openai/codex/releases/tag/rust-v0.52.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2025-10-30-chore-speed-up-pipeline-in-https-github-com-openai-codex-pull-5812|chore: speed-up pipeline in (source link)]] · Reliability and Performance
- [[Changes/Codex CLI/2025-10-30-ability-to-buy-credits-for-more-usage-more-information-https-help-openai-com-en|Ability to buy credits for more usage]] · Pricing Model
- [[Changes/Codex CLI/2025-10-30-5-model-support-changes-in-rust-v0-52-0|5 Model Support changes in rust-v0.52.0]] · Model Support
- [[Changes/Codex CLI/2025-10-30-11-apps-and-integrations-changes-in-rust-v0-52-0|11 Apps and Integrations changes in rust-v0.52.0]] · Apps and Integrations
- [[Changes/Codex CLI/2025-10-30-chore-decompose-submission-loop-in-https-github-com-openai-codex-pull-5854|chore: decompose submission loop in (source link)]] · Automation and Scheduling
- [[Changes/Codex CLI/2025-10-30-3-agent-mode-changes-in-rust-v0-52-0|3 Agent Mode changes in rust-v0.52.0]] · Agent Mode
- [[Changes/Codex CLI/2025-10-30-2-context-window-changes-in-rust-v0-52-0|2 Context Window changes in rust-v0.52.0]] · Context Window
- [[Changes/Codex CLI/2025-10-30-2-account-and-access-changes-in-rust-v0-52-0|2 Account and Access changes in rust-v0.52.0]] · Account and Access
- [[Changes/Codex CLI/2025-10-30-chore-config-editor-in-https-github-com-openai-codex-pull-5878|chore: config editor in (source link)]] · Editor Experience
- [[Changes/Codex CLI/2025-10-30-5-developer-workflow-changes-in-rust-v0-52-0|5 Developer Workflow changes in rust-v0.52.0]] · Developer Workflow
- [[Changes/Codex CLI/2025-10-30-3-safety-and-privacy-changes-in-rust-v0-52-0|3 Safety and Privacy changes in rust-v0.52.0]] · Safety and Privacy
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2025-10-30-576b56&body=Card%3A%20Changes%2FCodex%20CLI%2F2025-10-30-59-other-changes-in-rust-v0-52-0.md%0ACard%20ID%3A%20codex-cli-2025-10-30-576b56%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.52.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->