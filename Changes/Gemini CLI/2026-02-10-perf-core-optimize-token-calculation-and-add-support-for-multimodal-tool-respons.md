---
card_id: gemini-cli-2026-02-10-5c3b70
date: '2026-02-10'
description: 'Gemini CLI · 2026-02-10 · Multimodal Input: perf(core): optimize token
  calculation and add support for multimodal tool responses by @abhipatel12 in…'
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-09-25-you-can-now-show-chatgpt-one-or-more-images-troubleshoot-why-your-grill-won-t-st-e42bd6|Image
    input will be generally available to Plus users on all platforms]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 869
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: multimodal
  tracked_products_count: 10
evolves_from: []
extractor_version: fallback-v5
impact: significant
kind: change
machine_hash: c94627458e0e7abc27b0244985a59f9c7bff6344a82f88e64441f02d4d7b9ad1
product: gemini-cli
product_name: Gemini CLI
record:
  ai_generated: true
  card_id: gemini-cli-2026-02-10-5c3b70
  comparison: ''
  confidence: low
  date: '2026-02-10'
  description: 'Gemini CLI — Release v0.28.0: perf(core): optimize token calculation
    and add support for multimodal tool responses by @abhipatel12 in https://github.com/google-gemini/gemini-cli/pull/17835'
  evidence:
  - quote: 'perf(core): optimize token calculation and add support for multimodal
      tool responses by @abhipatel12 in https://github.com/google-gemini/gemini-cli/pull/17835'
    source_release: https://github.com/google-gemini/gemini-cli/releases/tag/v0.28.0
  extractor_version: fallback-v5
  impact: significant
  kind: change
  product: gemini-cli
  product_name: Gemini CLI
  slug: perf-core-optimize-token-calculation-and-add-support-for-multimodal-tool-respons
  source_release: gemini-cli-2026-02-10-v0-28-0-github-285023966-1bd56186
  source_type: github_releases
  theme: multimodal
  title: 'perf(core): optimize token calculation and add support for multimodal tool
    responses'
  type: change
related_changes:
- '[[Changes/Gemini CLI/2025-08-06-feat-core-parse-multimodal-mcp-tool-responses-by-luccasparoni-in-https-github-co|feat(core):
  Parse Multimodal MCP Tool responses]]'
- '[[Changes/Gemini CLI/2025-08-14-feat-core-parse-multimodal-mcp-tool-responses-by-luccasparoni-in-https-github-co|feat(core):
  Parse Multimodal MCP Tool responses]]'
- '[[Changes/Claude Code/2025-12-19-added-clickable-image-n-links-that-open-attached-images-in-the-default-viewer|Added
  clickable Image ♯N links that open attached images in the default viewer]]'
source_release: '[[Releases/Gemini CLI/gemini-cli-2026-02-10-v0-28-0-github-285023966-1bd56186|gemini-cli-2026-02-10-v0-28-0-github-285023966-1bd56186]]'
source_type: github_releases
theme: multimodal
title: 'perf(core): optimize token calculation and add support for multimodal tool
  responses'
type: change
---

<!-- chronolog:begin region="header" -->
# perf(core): optimize token calculation and add support for multimodal tool responses

**Gemini CLI** · 2026-02-10 · [[Themes/multimodal|Multimodal Input]] · [Official source](https://github.com/google-gemini/gemini-cli/releases/tag/v0.28.0) · from [[Releases/Gemini CLI/gemini-cli-2026-02-10-v0-28-0-github-285023966-1bd56186|Release v0.28.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> perf(core): optimize token calculation and add support for multimodal tool responses by @abhipatel12 in https://github.com/google-gemini/gemini-cli/pull/17835
>
> Source: https://github.com/google-gemini/gemini-cli/releases/tag/v0.28.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Gemini CLI/2026-02-10-4-agent-mode-changes-in-v0-28-0|4 Agent Mode changes in v0.28.0]] · Agent Mode
- [[Changes/Gemini CLI/2026-02-10-test-core-mock-fetch-in-oauth-transport-fallback-tests-by-jw409-in-https-github|test(core): mock fetch in OAuth transport fallback tests]] · Account and Access
- [[Changes/Gemini CLI/2026-02-10-docs-document-gemini-cli-home-environment-variable-by-adamfweidman-in-https-gith|docs: document GEMINI_CLI_HOME environment variable]] · Model Support
- [[Changes/Gemini CLI/2026-02-10-7-apps-and-integrations-changes-in-v0-28-0|7 Apps and Integrations changes in v0.28.0]] · Apps and Integrations
- [[Changes/Gemini CLI/2026-02-10-2-interface-experience-changes-in-v0-28-0|2 Interface Experience changes in v0.28.0]] · Interface Experience
- [[Changes/Gemini CLI/2026-02-10-feat-acp-add-session-resume-support-by-bdmorgan-in-https-github-com-google-gemin|feat(acp): add session resume support]] · Projects and Workspaces
- [[Changes/Gemini CLI/2026-02-10-3-editor-experience-changes-in-v0-28-0|3 Editor Experience changes in v0.28.0]] · Editor Experience
- [[Changes/Gemini CLI/2026-02-10-6-developer-workflow-changes-in-v0-28-0|6 Developer Workflow changes in v0.28.0]] · Developer Workflow
- [[Changes/Gemini CLI/2026-02-10-3-safety-and-privacy-changes-in-v0-28-0|3 Safety and Privacy changes in v0.28.0]] · Safety and Privacy
- [[Changes/Gemini CLI/2026-02-10-feat-core-add-setting-to-disable-loop-detection-by-sandytao520-in-https-github-c|feat(core): add setting to disable loop detection]] · Automation and Scheduling
- [[Changes/Gemini CLI/2026-02-10-59-other-changes-in-v0-28-0|59 other changes in v0.28.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Multimodal Input

- Earlier: 2025-12-19 · Claude Code · [[Changes/Claude Code/2025-12-19-added-clickable-image-n-links-that-open-attached-images-in-the-default-viewer|Added clickable Image ♯N links that open attached images in the default viewer]]
- Later: 2026-02-11 · Codex CLI · [[Changes/Codex CLI/2026-02-11-11336-always-expose-view-image-and-return-unsupported-image-input-error-aibrahim|♯11336 Always expose view_image and return unsupported image-input error @aibrahim-oai]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-09-25 · ChatGPT · [[Changes/ChatGPT/2023-09-25-you-can-now-show-chatgpt-one-or-more-images-troubleshoot-why-your-grill-won-t-st-e42bd6|Image input will be generally available to Plus users on all platforms]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20gemini-cli-2026-02-10-5c3b70&body=Card%3A%20Changes%2FGemini%20CLI%2F2026-02-10-perf-core-optimize-token-calculation-and-add-support-for-multimodal-tool-respons.md%0ACard%20ID%3A%20gemini-cli-2026-02-10-5c3b70%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fgoogle-gemini%2Fgemini-cli%2Freleases%2Ftag%2Fv0.28.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->