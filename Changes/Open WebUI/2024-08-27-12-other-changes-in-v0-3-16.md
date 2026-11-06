---
card_id: open-webui-2024-08-27-477396
date: '2024-08-27'
description: "Open WebUI · 2024-08-27 · Other changes: 12 changes in v0.3.16 — **\U0001F680
  Config DB Migration**: Migrated configuration handling from config.json to the database…"
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 8ceab345800aa30d2eddb4850cef5158e68cc550c698d73c400793b5c963945a
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2024-08-27-477396
  comparison: ''
  date: '2024-08-27'
  description: 'Open WebUI — v0.3.16: 12 other changes'
  evidence:
  - quote: "**\U0001F680 Config DB Migration**: Migrated configuration handling from
      config.json to the database, enabling high-availability setups and load balancing
      across multiple Open WebUI instances."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.3.16
  - quote: '**✨ TTS Content Control**: Added functionality to control how message
      content is segmented for Text-to-Speech (TTS) generation requests, allowing
      for more flexible speech output options.'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.3.16
  - quote: "**\U0001F446 Click-to-Copy for Codespan**: Enhanced interactive experience
      in the WebUI by allowing users to click to copy content from code spans directly."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.3.16
  - quote: "**\U0001F3AC Call Overlay Styling**: Adjusted call overlay styling on
      large screens to not cover the entire interface, but only the chat control area,
      for a more unobtrusive interaction experience."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.3.16
  - quote: "**\U0001F527 Pipe Functions with '**files**' Param**: Fixed issues with
      '**files**' parameter not functioning correctly in pipe functions."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.3.16
  - quote: "**\U0001F4DD Markdown Processing for RAG**: Fixed issues with processing
      Markdown in files."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.3.16
  - quote: "**\U0001F6AB Duplicate System Prompts**: Fixed bugs causing system prompts
      to duplicate."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.3.16
  - quote: "**\U0001F50D Content-Type for Ollama Chats**: Added 'application/x-ndjson'
      content-type to '/api/chat' endpoint responses to match raw Ollama responses."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.3.16
  - quote: "\U0001F44F Massive thanks to our incredible contributors for their hard
      work and dedication to making this release possible:"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.3.16
  - quote: '@Peter-De-Ath, @michaelpoluektov, @jannikstdl, @zhaofengli, @dependabot[bot],
      @kiosion, @KarlLee830, @aleixdorca, @0xThresh, @que-nguyen, @Yanyutin753'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.3.16
  - quote: "\U0001F680 We'd like to extend a heartfelt thank you to our amazing sponsors
      for their generous support (Note: We've excluded private sponsors from this
      list. If you'd like to get featured here, feel free to reach out to us!):"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.3.16
  - quote: '@digitalbrainowners, @Jkintree2, @lukepiette, @roosi-gmbh, @Trabing, @Razgaleh,
      @calabresefrj, @mushmax, @rndmcnlly, @GenieDev101, @Lance1101, @awaliuddin,
      @PortlandKyGuy'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.3.16
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 12-other-changes-in-v0-3-16
  source_release: open-webui-2024-08-27-v0-3-16-github-172195711-cee1ca67
  source_type: github_releases
  theme: uncategorized
  title: 12 other changes in v0.3.16
  type: change
source_release: '[[Releases/Open WebUI/open-webui-2024-08-27-v0-3-16-github-172195711-cee1ca67|open-webui-2024-08-27-v0-3-16-github-172195711-cee1ca67]]'
source_type: github_releases
theme: uncategorized
title: 12 other changes in v0.3.16
type: change
---

<!-- chronolog:begin region="header" -->
# 12 other changes in v0.3.16

**Open WebUI** · 2024-08-27 · Other changes · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.3.16) · from [[Releases/Open WebUI/open-webui-2024-08-27-v0-3-16-github-172195711-cee1ca67|v0.3.16]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> **🚀 Config DB Migration**: Migrated configuration handling from config.json to the database, enabling high-availability setups and load balancing across multiple Open WebUI instances.

> **✨ TTS Content Control**: Added functionality to control how message content is segmented for Text-to-Speech (TTS) generation requests, allowing for more flexible speech output options.

> **👆 Click-to-Copy for Codespan**: Enhanced interactive experience in the WebUI by allowing users to click to copy content from code spans directly.

> **🎬 Call Overlay Styling**: Adjusted call overlay styling on large screens to not cover the entire interface, but only the chat control area, for a more unobtrusive interaction experience.

> **🔧 Pipe Functions with '**files**' Param**: Fixed issues with '**files**' parameter not functioning correctly in pipe functions.

> **📝 Markdown Processing for RAG**: Fixed issues with processing Markdown in files.

> **🚫 Duplicate System Prompts**: Fixed bugs causing system prompts to duplicate.

> **🔍 Content-Type for Ollama Chats**: Added 'application/x-ndjson' content-type to '/api/chat' endpoint responses to match raw Ollama responses.

> 👏 Massive thanks to our incredible contributors for their hard work and dedication to making this release possible:

> @Peter-De-Ath, @michaelpoluektov, @jannikstdl, @zhaofengli, @dependabot[bot], @kiosion, @KarlLee830, @aleixdorca, @0xThresh, @que-nguyen, @Yanyutin753

> 🚀 We'd like to extend a heartfelt thank you to our amazing sponsors for their generous support (Note: We've excluded private sponsors from this list. If you'd like to get featured here, feel free to reach out to us!):

> @digitalbrainowners, @Jkintree2, @lukepiette, @roosi-gmbh, @Trabing, @Razgaleh, @calabresefrj, @mushmax, @rndmcnlly, @GenieDev101, @Lance1101, @awaliuddin, @PortlandKyGuy

Source: https://github.com/open-webui/open-webui/releases/tag/v0.3.16
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2024-08-27-show-knowledge-search-status-enhanced-model-usage-transparency-by-displaying-sta|😄 Show Knowledge Search Status]] · Model Support
- [[Changes/Open WebUI/2024-08-27-call-mode-activation-via-url-added-a-call-true-url-search-parameter-enabling-dir|🔗 Call Mode Activation via URL]] · Mobile and Desktop
- [[Changes/Open WebUI/2024-08-27-2-safety-and-privacy-changes-in-v0-3-16|2 Safety and Privacy changes in v0.3.16]] · Safety and Privacy
- [[Changes/Open WebUI/2024-08-27-latex-rendering-issue-addressed-an-issue-that-affected-the-correct-rendering-of|🔧 LaTeX Rendering Issue]] · Interface Experience
- [[Changes/Open WebUI/2024-08-27-disable-signups-conditionally-implemented-conditional-logic-to-disable-sign-ups|✋ Disable Signups Conditionally]] · Account and Access
- [[Changes/Open WebUI/2024-08-27-file-leak-prevention-resolved-the-issue-of-uploaded-files-mistakenly-being-acces|📁 File Leak Prevention]] · Files and Data
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2024-08-27-477396&body=Card%3A%20Changes%2FOpen%20WebUI%2F2024-08-27-12-other-changes-in-v0-3-16.md%0ACard%20ID%3A%20open-webui-2024-08-27-477396%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.3.16%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->