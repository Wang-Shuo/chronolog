---
card_id: opencode-2026-02-19-f7c113
date: '2026-02-19'
description: 'OpenCode · 2026-02-19 · Other changes: 39 changes in v1.2.7 — Core Normalize
  file status paths relative to instance directory'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 5cfdff62045413e9b07deea5d0c4209fe52a6ea8217fbc7b382186ad1b081001
product: opencode
product_name: OpenCode
record:
  card_id: opencode-2026-02-19-f7c113
  comparison: ''
  date: '2026-02-19'
  description: 'OpenCode — v1.2.7: 39 other changes'
  evidence:
  - quote: Core Normalize file status paths relative to instance directory
    source_release: https://opencode.ai/changelog/v1.2.7
  - quote: Core Migrate from Bun.Glob to npm glob package
    source_release: https://opencode.ai/changelog/v1.2.7
  - quote: Core Remove use of Bun.file
    source_release: https://opencode.ai/changelog/v1.2.7
  - quote: Core Text files misclassified as binary
    source_release: https://opencode.ai/changelog/v1.2.7
  - quote: Core Token substitution in OPENCODE_CONFIG_CONTENT now works correctly
    source_release: https://opencode.ai/changelog/v1.2.7
  - quote: Core Revert migration from Bun.file() to Filesystem module
    source_release: https://opencode.ai/changelog/v1.2.7
  - quote: Core Migrate project.ts from Bun.file() to Filesystem/stat modules
    source_release: https://opencode.ai/changelog/v1.2.7
  - quote: Core Migrate read tool from Bun.file() to Filesystem module
    source_release: https://opencode.ai/changelog/v1.2.7
  - quote: Core Migrate write tool from Bun.file() to Filesystem module
    source_release: https://opencode.ai/changelog/v1.2.7
  - quote: Core Migrate remaining tool files from Bun.file() to Filesystem/stat modules
    source_release: https://opencode.ai/changelog/v1.2.7
  - quote: Core Migrate storage.ts from Bun.file()/Bun.write() to Filesystem module
    source_release: https://opencode.ai/changelog/v1.2.7
  - quote: Core Migrate src/storage/json-migration.ts from Bun.file() to Filesystem
      module
    source_release: https://opencode.ai/changelog/v1.2.7
  - quote: Core Migrate storage database from Bun.file() to statSync for file existence
      checks
    source_release: https://opencode.ai/changelog/v1.2.7
  - quote: Core Migrate session prompt module from Bun.file() to Filesystem/stat modules
    source_release: https://opencode.ai/changelog/v1.2.7
  - quote: Core Fix crash in opencode run and show errored tool calls in output
    source_release: https://opencode.ai/changelog/v1.2.7
  - quote: Core Migrate skill discovery to use Filesystem module instead of Bun file
      APIs
    source_release: https://opencode.ai/changelog/v1.2.7
  - quote: Core Migrate session instruction handling from Bun.file() to Filesystem
      module
    source_release: https://opencode.ai/changelog/v1.2.7
  - quote: Core Migrate provider.ts from Bun.file() to Filesystem module
    source_release: https://opencode.ai/changelog/v1.2.7
  - quote: Core Migrate log utility from Bun.file() to Node.js fs module for better
      compatibility
    source_release: https://opencode.ai/changelog/v1.2.7
  - quote: Core Use HashiCorp releases API for installing terraform-ls
    source_release: https://opencode.ai/changelog/v1.2.7
  - quote: Core Migrate auth module from Bun.file()/Bun.write() to Filesystem module
    source_release: https://opencode.ai/changelog/v1.2.7
  - quote: Core Update SST version
    source_release: https://opencode.ai/changelog/v1.2.7
  - quote: Core Migrate src/global/index.ts from Bun.file() to Filesystem module
    source_release: https://opencode.ai/changelog/v1.2.7
  - quote: Core Migrate src/bun/index.ts from Bun.file()/Bun.write() to Filesystem
      module
    source_release: https://opencode.ai/changelog/v1.2.7
  - quote: Core Migrate config/markdown.ts from Bun.file() to Filesystem module
    source_release: https://opencode.ai/changelog/v1.2.7
  - quote: Core Migrate file/index.ts from Bun.file() to Filesystem module
    source_release: https://opencode.ai/changelog/v1.2.7
  - quote: Core Migrate format/formatter.ts from Bun.file() to Filesystem module
    source_release: https://opencode.ai/changelog/v1.2.7
  - quote: Core Allow readJson to be called without explicit type parameter
    source_release: https://opencode.ai/changelog/v1.2.7
  - quote: Core Migrate file/ripgrep.ts from Bun APIs to Filesystem module
    source_release: https://opencode.ai/changelog/v1.2.7
  - quote: Core Migrate index.ts from Bun.file() to Filesystem module
    source_release: https://opencode.ai/changelog/v1.2.7
  - quote: Core Add centralized filesystem module for Bun.file migration
    source_release: https://opencode.ai/changelog/v1.2.7
  - quote: Core Fix Clojure syntax highlighting
    source_release: https://opencode.ai/changelog/v1.2.7
  - quote: Core Don't autoload kilo
    source_release: https://opencode.ai/changelog/v1.2.7
  - quote: Core Add Kilo as a native provider
    source_release: https://opencode.ai/changelog/v1.2.7
  - quote: Core Simplify redundant ternary in updateMessage
    source_release: https://opencode.ai/changelog/v1.2.7
  - quote: Core Ensure Read tool uses fs/promises for all file system operations
    source_release: https://opencode.ai/changelog/v1.2.7
  - quote: Core Recover state after SSE reconnect and harden SSE streams
    source_release: https://opencode.ai/changelog/v1.2.7
  - quote: Core Keep message part order stable when files resolve asynchronously
    source_release: https://opencode.ai/changelog/v1.2.7
  - quote: Core Drop IDs from attachments in tools and assign them in prompt.ts instead
    source_release: https://opencode.ai/changelog/v1.2.7
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: opencode
  product_name: OpenCode
  slug: 39-other-changes-in-v1-2-7
  source_release: opencode-2026-02-19-v1-2-7-da02ddd2
  source_type: opencode_changelog
  theme: uncategorized
  title: 39 other changes in v1.2.7
  type: change
source_release: '[[Releases/OpenCode/opencode-2026-02-19-v1-2-7-da02ddd2|opencode-2026-02-19-v1-2-7-da02ddd2]]'
source_type: opencode_changelog
theme: uncategorized
title: 39 other changes in v1.2.7
type: change
---

<!-- chronolog:begin region="header" -->
# 39 other changes in v1.2.7

**OpenCode** · 2026-02-19 · Other changes · Digest · [Official source](https://opencode.ai/changelog/v1.2.7) · from [[Releases/OpenCode/opencode-2026-02-19-v1-2-7-da02ddd2|v1.2.7]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Core Normalize file status paths relative to instance directory

> Core Migrate from Bun.Glob to npm glob package

> Core Remove use of Bun.file

> Core Text files misclassified as binary

> Core Token substitution in OPENCODE_CONFIG_CONTENT now works correctly

> Core Revert migration from Bun.file() to Filesystem module

> Core Migrate project.ts from Bun.file() to Filesystem/stat modules

> Core Migrate read tool from Bun.file() to Filesystem module

> Core Migrate write tool from Bun.file() to Filesystem module

> Core Migrate remaining tool files from Bun.file() to Filesystem/stat modules

> Core Migrate storage.ts from Bun.file()/Bun.write() to Filesystem module

> Core Migrate src/storage/json-migration.ts from Bun.file() to Filesystem module

> Core Migrate storage database from Bun.file() to statSync for file existence checks

> Core Migrate session prompt module from Bun.file() to Filesystem/stat modules

> Core Fix crash in opencode run and show errored tool calls in output

> Core Migrate skill discovery to use Filesystem module instead of Bun file APIs

> Core Migrate session instruction handling from Bun.file() to Filesystem module

> Core Migrate provider.ts from Bun.file() to Filesystem module

> Core Migrate log utility from Bun.file() to Node.js fs module for better compatibility

> Core Use HashiCorp releases API for installing terraform-ls

> Core Migrate auth module from Bun.file()/Bun.write() to Filesystem module

> Core Update SST version

> Core Migrate src/global/index.ts from Bun.file() to Filesystem module

> Core Migrate src/bun/index.ts from Bun.file()/Bun.write() to Filesystem module

> Core Migrate config/markdown.ts from Bun.file() to Filesystem module

> Core Migrate file/index.ts from Bun.file() to Filesystem module

> Core Migrate format/formatter.ts from Bun.file() to Filesystem module

> Core Allow readJson to be called without explicit type parameter

> Core Migrate file/ripgrep.ts from Bun APIs to Filesystem module

> Core Migrate index.ts from Bun.file() to Filesystem module

> Core Add centralized filesystem module for Bun.file migration

> Core Fix Clojure syntax highlighting

> Core Don't autoload kilo

> Core Add Kilo as a native provider

> Core Simplify redundant ternary in updateMessage

> Core Ensure Read tool uses fs/promises for all file system operations

> Core Recover state after SSE reconnect and harden SSE streams

> Core Keep message part order stable when files resolve asynchronously

> Core Drop IDs from attachments in tools and assign them in prompt.ts instead

Source: https://opencode.ai/changelog/v1.2.7
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenCode/2026-02-19-46-mobile-and-desktop-changes-in-v1-2-7|46 Mobile and Desktop changes in v1.2.7]] · Mobile and Desktop
- [[Changes/OpenCode/2026-02-19-2-editor-experience-changes-in-v1-2-7|2 Editor Experience changes in v1.2.7]] · Editor Experience
- [[Changes/OpenCode/2026-02-19-core-migrate-agent-ts-from-bun-file-to-filesystem-module|Core Migrate agent.ts from Bun.file() to Filesystem module]] · Agent Mode
- [[Changes/OpenCode/2026-02-19-3-account-and-access-changes-in-v1-2-7|3 Account and Access changes in v1.2.7]] · Account and Access
- [[Changes/OpenCode/2026-02-19-core-make-read-tool-more-memory-efficient|Core Make read tool more memory efficient]] · Memory and Personalization
- [[Changes/OpenCode/2026-02-19-5-apps-and-integrations-changes-in-v1-2-7|5 Apps and Integrations changes in v1.2.7]] · Apps and Integrations
- [[Changes/OpenCode/2026-02-19-core-don-t-fetch-models-dev-on-completion|Core Don't fetch models.dev on completion]] · Interface Experience
- [[Changes/OpenCode/2026-02-19-4-safety-and-privacy-changes-in-v1-2-7|4 Safety and Privacy changes in v1.2.7]] · Safety and Privacy
- [[Changes/OpenCode/2026-02-19-3-model-support-changes-in-v1-2-7|3 Model Support changes in v1.2.7]] · Model Support
- [[Changes/OpenCode/2026-02-19-core-emit-prompt-too-large-error-when-github-context-overflows|Core Emit PROMPT_TOO_LARGE error when GitHub context overflows]] · Context Window
- [[Changes/OpenCode/2026-02-19-20-developer-workflow-changes-in-v1-2-7|20 Developer Workflow changes in v1.2.7]] · Developer Workflow
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20opencode-2026-02-19-f7c113&body=Card%3A%20Changes%2FOpenCode%2F2026-02-19-39-other-changes-in-v1-2-7.md%0ACard%20ID%3A%20opencode-2026-02-19-f7c113%0ASource%3A%20https%3A%2F%2Fopencode.ai%2Fchangelog%2Fv1.2.7%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->