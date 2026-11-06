---
card_id: codex-cli-2026-01-09-a27186
date: '2026-01-09'
description: 'Codex CLI · 2026-01-09 · Other changes: 62 changes in 0.80.0 — Add conversation/thread
  fork endpoints in the protocol and app server so clients can branch a…'
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: eaeecb5f24789e3dc3a35dbfa7675ed8f3a1e3639ac8e8b653d2353b83d58bcc
product: codex-cli
product_name: Codex CLI
record:
  card_id: codex-cli-2026-01-09-a27186
  comparison: ''
  date: '2026-01-09'
  description: 'Codex CLI — 0.80.0: 62 other changes'
  evidence:
  - quote: Add conversation/thread fork endpoints in the protocol and app server so
      clients can branch a session into a new thread. (#8866)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.80.0
  - quote: 'Introduce metrics capabilities with additional counters for observability.
      (#8318, #8910)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.80.0
  - quote: Allow explicit skill invocations through v2 API user input. (#8864)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.80.0
  - quote: '`/review <instructions>` in TUI/TUI2 now launches the review flow instead
      of sending plain text. (#8823)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.80.0
  - quote: 'Windows paste handling now supports non-ASCII multiline input reliably.
      Special thanks to @occurrent laying the groundwork for this fix in #8021! (#8774)'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.80.0
  - quote: Skill-creator docs clarify YAML frontmatter formatting and quoting rules.
      (#8610)
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.80.0
  - quote: '#8734 fix: do not propose to add multiline commands to execpolicy @tibo-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.80.0
  - quote: '#8805 chore: stabilize core tool parallelism test @tibo-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.80.0
  - quote: '#8820 chore: silent just fmt @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.80.0
  - quote: '#8823 fix: handle /review arguments in TUI @tibo-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.80.0
  - quote: '#8822 chore: rename unified exec sessions @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.80.0
  - quote: '#8825 fix: handle early codex exec exit @tibo-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.80.0
  - quote: '#8830 chore: unify conversation with thread name @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.80.0
  - quote: '#8840 Move tests below auth manager @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.80.0
  - quote: '#8845 fix: upgrade lru crate to 0.16.3 @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.80.0
  - quote: '#8763 Merge Modelfamily into modelinfo @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.80.0
  - quote: '#8842 remove unnecessary todos @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.80.0
  - quote: '#8846 Stop using AuthManager as the source of codex_home @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.80.0
  - quote: '#8850 chore: drop useless feature flags @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.80.0
  - quote: '#8848 chore: drop some deprecated @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.80.0
  - quote: '#8853 [chore] update app server doc with skills @celia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.80.0
  - quote: '#8451 fix: implement ''Allow this session'' for apply_patch approvals
      @owenlin0'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.80.0
  - quote: '#8849 Simplify error managment in `run_turn` @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.80.0
  - quote: '#8767 Add feature for optional request compression @cconger'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.80.0
  - quote: '#8610 Clarify YAML frontmatter formatting in skill-creator @darlingm'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.80.0
  - quote: '#8801 Support symlink for skills discovery. @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.80.0
  - quote: '#8800 Feat: appServer.requirementList for requirement.toml @shijie-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.80.0
  - quote: '#8861 fix: update resource path resolution logic so it works with Bazel
      @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.80.0
  - quote: '#8868 fix: use tokio for I/O in an async function @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.80.0
  - quote: footer note to TUI @iceweasel-oai
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.80.0
  - quote: '#8879 feat: introduce find_resource! macro that works with Cargo or Bazel
      @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.80.0
  - quote: '#8864 Support UserInput::Skill in V2 API. @xl-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.80.0
  - quote: '#8876 add ability to disable input temporarily in the TUI. @iceweasel-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.80.0
  - quote: '#8884 fix: make the find_resource! macro responsible for the absolutize()
      call @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.80.0
  - quote: '#8774 fix: windows can now paste non-ascii multiline text @dylan-hurd-oai,
      @occurrent'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.80.0
  - quote: '#8855 chore: add list thread ids on manager @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.80.0
  - quote: '#8318 feat: metrics capabilities @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.80.0
  - quote: '#8826 fix: stabilize list_dir pagination order @tibo-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.80.0
  - quote: '#8892 chore: drop metrics exporter config @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.80.0
  - quote: '#8896 chore: align error limit comment @tibo-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.80.0
  - quote: '#8888 fix: leverage find_resource! macro in load_sse_fixture_with_id @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.80.0
  - quote: '#8887 fix: leverage codex_utils_cargo_bin() in codex-rs/core/tests/suite
      @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.80.0
  - quote: '#8907 chore: drop useless interaction_input @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.80.0
  - quote: '#8903 nit: drop unused function call error @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.80.0
  - quote: '#8910 feat: add a few metrics @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.80.0
  - quote: '#8911 gitignore bazel-* @zbarsky-openai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.80.0
  - quote: '#8843 config requirements: improve requirement error messages @gt-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.80.0
  - quote: '#8914 fix: reduce duplicate include_str!() calls @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.80.0
  - quote: '#8902 feat: add list loaded threads to app server @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.80.0
  - quote: '#8870 [fix] app server flaky thread/resume tests @celia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.80.0
  - quote: '#8916 clean: all history cloning @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.80.0
  - quote: '#8915 otel test: retry WouldBlock errors @gt-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.80.0
  - quote: '#8913 Add `read-only` when backfilling requirements from managed_config
      @gt-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.80.0
  - quote: '#8857 Immutable CodexAuth @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.80.0
  - quote: '#8927 nit: parse_arguments @jif-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.80.0
  - quote: '#8932 fix: increase timeout for tests that have been flaking with timeout
      issues @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.80.0
  - quote: '#8874 [fix] app server flaky send_messages test @celia-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.80.0
  - quote: '#8866 feat: fork conversation/thread @apanasenko-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.80.0
  - quote: '#8858 remove `get_responses_requests` and `get_responses_request_bodies`
      to use in-place matcher @aibrahim-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.80.0
  - quote: '#8880 Attempt to reload auth as a step in 401 recovery @pakrym-oai'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.80.0
  - quote: '#8946 fix: increase timeout for wait_for_event() for Bazel @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.80.0
  - quote: '#8951 fix: remove existing process hardening from Codex CLI @bolinfest'
    source_release: https://github.com/openai/codex/releases/tag/rust-v0.80.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: codex-cli
  product_name: Codex CLI
  slug: 62-other-changes-in-rust-v0-80-0
  source_release: codex-cli-2026-01-09-rust-v0-80-0-github-275597320-df7b3faf
  source_type: github_releases
  theme: uncategorized
  title: 62 other changes in rust-v0.80.0
  type: change
source_release: '[[Releases/Codex CLI/codex-cli-2026-01-09-rust-v0-80-0-github-275597320-df7b3faf|codex-cli-2026-01-09-rust-v0-80-0-github-275597320-df7b3faf]]'
source_type: github_releases
theme: uncategorized
title: 62 other changes in rust-v0.80.0
type: change
---

<!-- chronolog:begin region="header" -->
# 62 other changes in rust-v0.80.0

**Codex CLI** · 2026-01-09 · Other changes · Digest · [Official source](https://github.com/openai/codex/releases/tag/rust-v0.80.0) · from [[Releases/Codex CLI/codex-cli-2026-01-09-rust-v0-80-0-github-275597320-df7b3faf|0.80.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Add conversation/thread fork endpoints in the protocol and app server so clients can branch a session into a new thread. (#8866)

> Introduce metrics capabilities with additional counters for observability. (#8318, #8910)

> Allow explicit skill invocations through v2 API user input. (#8864)

> `/review <instructions>` in TUI/TUI2 now launches the review flow instead of sending plain text. (#8823)

> Windows paste handling now supports non-ASCII multiline input reliably. Special thanks to @occurrent laying the groundwork for this fix in #8021! (#8774)

> Skill-creator docs clarify YAML frontmatter formatting and quoting rules. (#8610)

> #8734 fix: do not propose to add multiline commands to execpolicy @tibo-openai

> #8805 chore: stabilize core tool parallelism test @tibo-openai

> #8820 chore: silent just fmt @jif-oai

> #8823 fix: handle /review arguments in TUI @tibo-openai

> #8822 chore: rename unified exec sessions @jif-oai

> #8825 fix: handle early codex exec exit @tibo-openai

> #8830 chore: unify conversation with thread name @jif-oai

> #8840 Move tests below auth manager @pakrym-oai

> #8845 fix: upgrade lru crate to 0.16.3 @bolinfest

> #8763 Merge Modelfamily into modelinfo @aibrahim-oai

> #8842 remove unnecessary todos @aibrahim-oai

> #8846 Stop using AuthManager as the source of codex_home @pakrym-oai

> #8850 chore: drop useless feature flags @jif-oai

> #8848 chore: drop some deprecated @jif-oai

> #8853 [chore] update app server doc with skills @celia-oai

> #8451 fix: implement 'Allow this session' for apply_patch approvals @owenlin0

> #8849 Simplify error managment in `run_turn` @aibrahim-oai

> #8767 Add feature for optional request compression @cconger

> #8610 Clarify YAML frontmatter formatting in skill-creator @darlingm

> #8801 Support symlink for skills discovery. @xl-openai

> #8800 Feat: appServer.requirementList for requirement.toml @shijie-oai

> #8861 fix: update resource path resolution logic so it works with Bazel @bolinfest

> #8868 fix: use tokio for I/O in an async function @bolinfest

> footer note to TUI @iceweasel-oai

> #8879 feat: introduce find_resource! macro that works with Cargo or Bazel @bolinfest

> #8864 Support UserInput::Skill in V2 API. @xl-openai

> #8876 add ability to disable input temporarily in the TUI. @iceweasel-oai

> #8884 fix: make the find_resource! macro responsible for the absolutize() call @bolinfest

> #8774 fix: windows can now paste non-ascii multiline text @dylan-hurd-oai, @occurrent

> #8855 chore: add list thread ids on manager @jif-oai

> #8318 feat: metrics capabilities @jif-oai

> #8826 fix: stabilize list_dir pagination order @tibo-openai

> #8892 chore: drop metrics exporter config @jif-oai

> #8896 chore: align error limit comment @tibo-openai

> #8888 fix: leverage find_resource! macro in load_sse_fixture_with_id @bolinfest

> #8887 fix: leverage codex_utils_cargo_bin() in codex-rs/core/tests/suite @bolinfest

> #8907 chore: drop useless interaction_input @jif-oai

> #8903 nit: drop unused function call error @jif-oai

> #8910 feat: add a few metrics @jif-oai

> #8911 gitignore bazel-* @zbarsky-openai

> #8843 config requirements: improve requirement error messages @gt-oai

> #8914 fix: reduce duplicate include_str!() calls @bolinfest

> #8902 feat: add list loaded threads to app server @jif-oai

> #8870 [fix] app server flaky thread/resume tests @celia-oai

> #8916 clean: all history cloning @jif-oai

> #8915 otel test: retry WouldBlock errors @gt-oai

> #8913 Add `read-only` when backfilling requirements from managed_config @gt-oai

> #8857 Immutable CodexAuth @pakrym-oai

> #8927 nit: parse_arguments @jif-oai

> #8932 fix: increase timeout for tests that have been flaking with timeout issues @bolinfest

> #8874 [fix] app server flaky send_messages test @celia-oai

> #8866 feat: fork conversation/thread @apanasenko-oai

> #8858 remove `get_responses_requests` and `get_responses_request_bodies` to use in-place matcher @aibrahim-oai

> #8880 Attempt to reload auth as a step in 401 recovery @pakrym-oai

> #8946 fix: increase timeout for wait_for_event() for Bazel @bolinfest

> #8951 fix: remove existing process hardening from Codex CLI @bolinfest

Source: https://github.com/openai/codex/releases/tag/rust-v0.80.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Codex CLI/2026-01-09-2-apps-and-integrations-changes-in-rust-v0-80-0|2 Apps and Integrations changes in rust-v0.80.0]] · Apps and Integrations
- [[Changes/Codex CLI/2026-01-09-2-agent-mode-changes-in-rust-v0-80-0|2 Agent Mode changes in rust-v0.80.0]] · Agent Mode
- [[Changes/Codex CLI/2026-01-09-codex-cli-subprocesses-again-inherit-env-vars-like-ld-library-path-dyld-library|Codex CLI subprocesses again inherit env vars like…]] · Reliability and Performance
- [[Changes/Codex CLI/2026-01-09-8939-chore-move-app-server-tests-from-chat-completion-to-responses-celia-oai|♯8939 chore move app server tests from chat completion to responses @celia-oai]] · Editor Experience
- [[Changes/Codex CLI/2026-01-09-app-server-readme-now-documents-skills-support-and-usage-8853|App-server README now documents skills support and usage]] · Files and Data
- [[Changes/Codex CLI/2026-01-09-4-developer-workflow-changes-in-rust-v0-80-0|4 Developer Workflow changes in rust-v0.80.0]] · Developer Workflow
- [[Changes/Codex CLI/2026-01-09-2-mobile-and-desktop-changes-in-rust-v0-80-0|2 Mobile and Desktop changes in rust-v0.80.0]] · Mobile and Desktop
- [[Changes/Codex CLI/2026-01-09-4-model-support-changes-in-rust-v0-80-0|4 Model Support changes in rust-v0.80.0]] · Model Support
- [[Changes/Codex CLI/2026-01-09-3-interface-experience-changes-in-rust-v0-80-0|3 Interface Experience changes in rust-v0.80.0]] · Interface Experience
- [[Changes/Codex CLI/2026-01-09-2-safety-and-privacy-changes-in-rust-v0-80-0|2 Safety and Privacy changes in rust-v0.80.0]] · Safety and Privacy
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20codex-cli-2026-01-09-a27186&body=Card%3A%20Changes%2FCodex%20CLI%2F2026-01-09-62-other-changes-in-rust-v0-80-0.md%0ACard%20ID%3A%20codex-cli-2026-01-09-a27186%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopenai%2Fcodex%2Freleases%2Ftag%2Frust-v0.80.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->