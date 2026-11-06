---
card_id: dify-2023-09-10-dfb4f1
date: '2023-09-10'
description: 'Dify · 2023-09-10 · Developer Workflow: 3 changes in Version 0.3.21
  — To ensure that the previous applications can still function properly after removing
  the…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 176
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: c7ef6a9b34080707bee2ba5cb4f1e13eaf567b62ded044d9217c08d3319508cf
product: dify
product_name: Dify
record:
  card_id: dify-2023-09-10-dfb4f1
  comparison: ''
  date: '2023-09-10'
  description: 'Dify — Version 0.3.21: 3 Developer Workflow changes'
  evidence:
  - quote: 'To ensure that the previous applications can still function properly after
      removing the fixed parameters in the query content of the text generation application,
      we need to execute a command to fix the data:'
    source_release: https://github.com/langgenius/dify/releases/tag/0.3.21
  - quote: '**Enter the Docker Container**: Before running the migration script, you
      need to enter the Docker container where your application is running. Use the
      following command:'
    source_release: https://github.com/langgenius/dify/releases/tag/0.3.21
  - quote: '**Run the Migration Script**: Once inside the container, execute the following
      migration command. The migration script can be executed multiple times without
      side effects:'
    source_release: https://github.com/langgenius/dify/releases/tag/0.3.21
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: dify
  product_name: Dify
  slug: 3-developer-workflow-changes-in-0-3-21
  source_release: dify-2023-09-10-0-3-21-github-120538894-5afc54de
  source_type: github_releases
  theme: developer-workflow
  title: 3 Developer Workflow changes in 0.3.21
  type: change
related_changes:
- '[[Changes/Cursor/2023-08-26-we-had-a-big-bug-for-people-on-language-packs-thank-you-to-all-who-helped-us-deb|Bug
  fix for people on language packs]]'
- '[[Changes/Cursor/2023-09-05-ships-with-cursor-python-a-language-server-fork-of-pyright-built-for-cursor|Cursor-Python
  LSP]]'
- '[[Changes/Dify/2023-09-09-feat-add-visual-studio-code-debug-config-by-garfielddai-in-https-github-com-lang|feat:
  add visual studio code debug config]]'
source_release: '[[Releases/Dify/dify-2023-09-10-0-3-21-github-120538894-5afc54de|dify-2023-09-10-0-3-21-github-120538894-5afc54de]]'
source_type: github_releases
theme: developer-workflow
title: 3 Developer Workflow changes in 0.3.21
type: change
---

<!-- chronolog:begin region="header" -->
# 3 Developer Workflow changes in 0.3.21

**Dify** · 2023-09-10 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/langgenius/dify/releases/tag/0.3.21) · from [[Releases/Dify/dify-2023-09-10-0-3-21-github-120538894-5afc54de|Version 0.3.21]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> To ensure that the previous applications can still function properly after removing the fixed parameters in the query content of the text generation application, we need to execute a command to fix the data:

> **Enter the Docker Container**: Before running the migration script, you need to enter the Docker container where your application is running. Use the following command:

> **Run the Migration Script**: Once inside the container, execute the following migration command. The migration script can be executed multiple times without side effects:

Source: https://github.com/langgenius/dify/releases/tag/0.3.21
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Dify/2023-09-10-the-query-parameter-in-the-post-v1-completion-messages-endpoint-of-the-app-opena|The query parameter in the POST /v1/completion-messages endpoint of the App…]] · Editor Experience
- [[Changes/Dify/2023-09-10-5-other-changes-in-0-3-21|5 other changes in 0.3.21]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2023-09-09 · Dify · [[Changes/Dify/2023-09-09-feat-add-visual-studio-code-debug-config-by-garfielddai-in-https-github-com-lang|feat: add visual studio code debug config]]
- Later: 2023-09-22 · Ollama · [[Changes/Ollama/2023-09-22-ollama-will-now-fit-words-in-the-available-width-of-the-terminal-for-better-read|Ollama will now fit words in the available width of the terminal for better readability]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-18 · Cursor · [[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20dify-2023-09-10-dfb4f1&body=Card%3A%20Changes%2FDify%2F2023-09-10-3-developer-workflow-changes-in-0-3-21.md%0ACard%20ID%3A%20dify-2023-09-10-dfb4f1%0ASource%3A%20https%3A%2F%2Fgithub.com%2Flanggenius%2Fdify%2Freleases%2Ftag%2F0.3.21%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->