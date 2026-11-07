---
card_id: open-webui-2026-07-27-ebf99c
date: '2026-07-27'
description: "Open WebUI · 2026-07-27 · Model Support: 39 changes in v0.11.0 — \U0001F516
  **Chat variables.** A model's system prompt can now declare fields such as text
  boxes and…"
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1295
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 45
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 5a1fb6839ac3bfb8c2c5bf6f4a12891f9859bc01f78d9f63fc076cc76d346229
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-07-27-ebf99c
  comparison: ''
  date: '2026-07-27'
  description: 'Open WebUI — v0.11.0: 39 Model Support changes'
  evidence:
  - quote: "\U0001F516 **Chat variables.** A model's system prompt can now declare
      fields such as text boxes and dropdown lists that you fill in for a conversation,
      with the values saved alongside the chat and carried over when it is forked
      or cloned. [Commit](https://github.com/open-webui/open-webui/commit/bef8ae4b2f05ca49ed88a02ab7a3cdc11b62c4f1),
      [Commit](https://github.com/open-webui/open-webui/commit/4e869011cd5040b5d6a197fc83d5f50d2425dbc2),
      [Commit](https://github.com/open-webui/open-webui/commit/1e88367cc837b39c0e9958fefbe053803336dce2),
      [Commit](https://github.com/open-webui/open-webui/commit/8cbb7f765cfc9c9b3237a6c5593cd93f849033f0),
      [Commit](https://github.com/open-webui/open-webui/commit/b35e2d265a4e4a2f2a075b31917d48be1dd9ef19),
      [Commit](https://github.com/open-webui/open-webui/commit/239cb740077a14e452ad002a1e671a09ab558e40),
      [#26915](https://github.com/open-webui/open-webui/discussions/26915)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F4C7 **User variables.** You can now store your own values in account
      settings, such as your role or how you like answers written, and a model's system
      prompt can insert them wherever they are needed. [Commit](https://github.com/open-webui/open-webui/commit/bd5d7b2e879511882429075d804d9222956f4a1a),
      [Commit](https://github.com/open-webui/open-webui/commit/212eec408ca320edfa2271e604d10e14b6a9bc1a),
      [Commit](https://github.com/open-webui/open-webui/commit/793a43d9c48225925929eb312fe2b70d5914d1da)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F4DD **Chat with a note.** Chatting with a note now gives you the
      full chat experience, including model choice, tools and file attachments, alongside
      suggested prompts, a button to insert a response straight into the note, edits
      that appear in the note as the assistant makes them, and as many separate conversations
      per note as you want to keep. [Commit](https://github.com/open-webui/open-webui/commit/423cafd4e75e34b487f3b5d10ec1c506f073b3da),
      [Commit](https://github.com/open-webui/open-webui/commit/185bca8552ee3f87ea95fdcad32a433924881b9a)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: ↕️ **Sort your lists.** The notes, prompts, models, knowledge, skills,
      tools and functions lists can now be sorted by title or by when they were last
      updated, in either direction, by clicking the column headings. [Commit](https://github.com/open-webui/open-webui/commit/30c91e46e5d237bee3c8805bd54749408cc2727a),
      [Commit](https://github.com/open-webui/open-webui/commit/56f2cb530259df5393ea1ae844bad5cc6b2c810c),
      [#27457](https://github.com/open-webui/open-webui/pull/27457), [#27456](https://github.com/open-webui/open-webui/discussions/27456)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F5C2️ **The assistant can search your attachments.** A new Files
      capability lets the model list the files attached to the chat and search them
      by meaning or by exact text, and read the parts it needs, rather than having
      their whole contents pushed into the conversation up front, and knowledge collections
      or notes attached to a chat are now announced to the model so it can query those
      the same way. [Commit](https://github.com/open-webui/open-webui/commit/57e60423b9963c4a69fdfda7ae5799efc5583010),
      [Commit](https://github.com/open-webui/open-webui/commit/55e0801dab8fe5f8bceff7d7c49772676724b8b1),
      [#26711](https://github.com/open-webui/open-webui/pull/26711), [#27232](https://github.com/open-webui/open-webui/issues/27232),
      [#26708](https://github.com/open-webui/open-webui/issues/26708)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F947 **Model order as a setting.** Administrators can now set the
      order models appear in through a new \"MODEL_ORDER_LIST\" variable, so the arrangement
      survives a restart on instances that do not persist configuration. [#27420](https://github.com/open-webui/open-webui/pull/27420),
      [#27206](https://github.com/open-webui/open-webui/issues/27206)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F4AD **Reasoning in Anthropic responses.** Responses from the Anthropic-compatible
      API now carry the model's reasoning as thinking blocks, in both streamed and
      complete responses. [Commit](https://github.com/open-webui/open-webui/commit/bb12b1a18b77d80829cedb2d5bf965808222415b)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F9E9 **Structured output through the Anthropic-compatible API.**
      Requests can now ask for a JSON schema or JSON object response and set a reasoning
      effort, which are carried through to the upstream model. [Commit](https://github.com/open-webui/open-webui/commit/bb12b1a18b77d80829cedb2d5bf965808222415b)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F9EE **Counts in the tabs.** The workspace tabs now show how many
      models, knowledge bases, prompts, skills, and tools you have, and the admin
      tabs do the same for users, groups, leaderboard entries, and feedback, so you
      can see the size of each section without opening it. [Commit](https://github.com/open-webui/open-webui/commit/05e3f713175c1eea43a99f29521eb01700c21d3c),
      [Commit](https://github.com/open-webui/open-webui/commit/727041da78bcfcb44c0e4c83c4e6a641b7061b90),
      [Commit](https://github.com/open-webui/open-webui/commit/f8ea15b84a274712dca33daa970f63ed7368043e)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F9F0 **Built-in tool descriptions built once.** The descriptions
      handed to the model for the built-in tools are now worked out once at startup
      rather than rebuilt on every message. [Commit](https://github.com/open-webui/open-webui/commit/d727ee4d1febb2b72d5f6c26668c562eadca54f1),
      [Commit](https://github.com/open-webui/open-webui/commit/12974c9e4ed97b2d68c4ad129c057ff0e774254e),
      [#27374](https://github.com/open-webui/open-webui/pull/27374), [#27396](https://github.com/open-webui/open-webui/pull/27396)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001FABA **Records read without a double pass.** Loading a model, tool,
      prompt, skill, note, knowledge base, channel or calendar no longer converts
      the record twice on the way out. [Commit](https://github.com/open-webui/open-webui/commit/f1409266feb224e74fe023d7459f1e2b5aad0b29),
      [#27377](https://github.com/open-webui/open-webui/pull/27377)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001FAAA **Fewer checks before a reply starts.** Working out whether
      you may use a model now looks up the model and your group memberships once instead
      of repeating both, including for every model a workspace model is built on.
      [#27378](https://github.com/open-webui/open-webui/pull/27378)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001FA84 **Lighter conversion for Ollama requests.** Preparing a request
      for an Ollama model no longer copies the entire conversation before sending
      it, which cost more with every message and repeated on each tool-call round.
      [#27371](https://github.com/open-webui/open-webui/pull/27371)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F6A6 **No filter bookkeeping without filters.** Streamed API responses
      only build up the full reply for outlet filters when the model actually has
      one configured, instead of doing it for every request. [Commit](https://github.com/open-webui/open-webui/commit/315a6b5995663eabe1c96776d66b6593860d47d6),
      [#27391](https://github.com/open-webui/open-webui/pull/27391)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: ✂️ **Cheaper tag detection while streaming.** Watching a reply for reasoning
      and code blocks now examines only the newly arrived text rather than rescanning
      the whole answer on every chunk, so a long answer no longer costs progressively
      more as it grows. [#27360](https://github.com/open-webui/open-webui/pull/27360)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F517 **Fewer Redis round trips per chat.** Deployments backed by
      Redis now look up the model and connected sessions once per request instead
      of twice, and fetch the model list in a single call. [#27225](https://github.com/open-webui/open-webui/pull/27225)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001FAB6 **Model lists without knowledge text.** Model lists no longer
      include the extracted text of files attached to a model as knowledge, so they
      stay small regardless of how large those knowledge bases are. [Commit](https://github.com/open-webui/open-webui/commit/48625e657ff11161c3588af2747598f102c1a4d1),
      [#27287](https://github.com/open-webui/open-webui/issues/27287)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F4EE **Name lookups off the thread pool.** Looking up a hostname
      no longer occupies one of the limited threads shared by every other piece of
      blocking work, so model calls, searches, page fetches and tool calls stop queueing
      behind each other once a few lookups are slow. [#27440](https://github.com/open-webui/open-webui/pull/27440)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F3AF **Model settings in the list endpoint.** Listing models no
      longer includes each one's parameters and system prompt for people with read
      access only, matching what opening a single model already returned. [#27004](https://github.com/open-webui/open-webui/pull/27004)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001FA9C **Reaching a restricted model through a shared one.** A shared
      workspace model can no longer be used to reach an underlying model the person
      could not otherwise use, which previously slipped through when that model had
      no entry of its own. [#26905](https://github.com/open-webui/open-webui/pull/26905),
      [#26900](https://github.com/open-webui/open-webui/issues/26900)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F3AC **Chat action availability.** Chat actions can no longer be
      triggered when they are disabled, not assigned to the model in use, or on a
      model the caller cannot access, matching the actions the interface actually
      offers. [#27243](https://github.com/open-webui/open-webui/pull/27243)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: ➡️ **Prompts opened from a link.** A prompt passed in through a link that
      sends automatically now waits for tool servers to finish loading, so external
      tools are available on that first message instead of the model reporting it
      has none. [Commit](https://github.com/open-webui/open-webui/commit/d7513e4ce81ada1936c0c34115f947e115d6f2cf),
      [#24176](https://github.com/open-webui/open-webui/issues/24176)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001FA86 **Summaries on a direct connection.** Summarizing a long conversation
      on a direct connection can now use the configured summary model rather than
      being limited to the connection's own model. [#26806](https://github.com/open-webui/open-webui/pull/26806)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F3B2 **Stable skill ordering.** Skills available to a model are
      now listed in the same order on every request, instead of shuffling between
      requests and quietly defeating prompt caching. [Commit](https://github.com/open-webui/open-webui/commit/b9d72741bb2f649cb67942ce7c635ea173f32b70),
      [#26986](https://github.com/open-webui/open-webui/issues/26986)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: ⭐ **Rating scale in multi-model replies.** The rating scale in the feedback
      panel is no longer cut off when several models answer side by side, so every
      score can be picked. [#26846](https://github.com/open-webui/open-webui/issues/26846)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F9D1\U0001F91D\U0001F9D1 **Duplicate models side by side.** Adding
      the same model twice in a side-by-side chat now keeps each column's own answer
      after a reload, instead of every column collapsing onto the first one. [#26980](https://github.com/open-webui/open-webui/pull/26980)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F4F1 **Model selector on small screens.** The model list now stays
      fully on screen and sizes itself to the space available, instead of running
      past the edge or hiding behind the on-screen keyboard on phones. [Commit](https://github.com/open-webui/open-webui/commit/79d3e34eea6dc2828d1945cc2b9fca5d662d825b),
      [Commit](https://github.com/open-webui/open-webui/commit/e39ff71532651438c32b2aa7ffe2b6068c94e6b2),
      [Commit](https://github.com/open-webui/open-webui/commit/ea31a3bd61fdf1a72206f9ed5f7252486d554c9b)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F9F2 **Search quality with prefix-based embedding models.** Memories,
      knowledge base descriptions and searches against an external vector database
      now carry the query and content markers your embedding model expects, so results
      are no longer quietly worse than they should be on models that rely on them.
      [Commit](https://github.com/open-webui/open-webui/commit/c4f5ac65ee3cd20dd1d507eda04fca21a866910a),
      [#26958](https://github.com/open-webui/open-webui/pull/26958), [#26353](https://github.com/open-webui/open-webui/issues/26353)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F9EC **Shared pipe model tool calls.** Non-admin users of a shared
      model built on a pipe or manifold model no longer see the response silently
      stop right after a tool call. [#26906](https://github.com/open-webui/open-webui/pull/26906),
      [#26900](https://github.com/open-webui/open-webui/issues/26900)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F3F7️ **Model names containing a connection prefix.** A prefix set
      on a connection is now removed only from the front of the model name, so a model
      whose own name contains that text is no longer mangled before the request is
      sent. [Commit](https://github.com/open-webui/open-webui/commit/ed663f16ecaaf99de194922d1634ecc5d906c703)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F999 **Newly pulled Ollama models.** Sending a message to a model
      that was pulled after the list was last built now refreshes the list and proceeds,
      instead of reporting the model as not found. [Commit](https://github.com/open-webui/open-webui/commit/ed663f16ecaaf99de194922d1634ecc5d906c703),
      [#27353](https://github.com/open-webui/open-webui/pull/27353)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F5D1️ **Deleting a model from the selector.** Removing a workspace
      model from the model selector menu now deletes just that model and leaves the
      underlying one in place, instead of failing with a not found error. [#26819](https://github.com/open-webui/open-webui/pull/26819)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F465 **Previewing what someone can use.** The preview of a person's
      access now includes the models, knowledge bases and tools they own, not just
      the ones shared with them. [Commit](https://github.com/open-webui/open-webui/commit/a9a3e5b95c8e641881fedc1ce7431eedab9a371b),
      [#27423](https://github.com/open-webui/open-webui/pull/27423), [#27407](https://github.com/open-webui/open-webui/discussions/27407)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: ♻️ **Connection changes take effect immediately.** Saving connection settings
      now refreshes the model list straight away, instead of leaving the previous
      models in place until the server was restarted.
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F6AB **Disabled OpenAI connections are enforced.** Turning off the
      OpenAI API now blocks chat requests to it and clears its models, rather than
      only hiding it from the interface."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F3DE️ **Images returned by a tool.** Images a tool produces are
      now passed to the model in a form the OpenAI-compatible providers accept, so
      it can actually look at them instead of receiving a result it cannot read. [Commit](https://github.com/open-webui/open-webui/commit/dd86b984bd508cf2841f08dae90411dfb5fe407f)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F523 **Names containing a vertical bar.** What you insert with the
      at sign or a slash is now recorded by the key you typed rather than guessed
      from its name, so a prompt or model whose name contains a vertical bar is no
      longer mistaken for a skill. [Commit](https://github.com/open-webui/open-webui/commit/e28b391e514384ec329ca871d02189aa81fb1a00)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: ✳️ **Asterisks in the message input.** Wrapping a word in asterisks no
      longer silently turns it italic and swallows the asterisks, so your prompt reaches
      the model exactly as you typed it. [Commit](https://github.com/open-webui/open-webui/commit/001775d8e868ce44f125e0d683dd50363f0e8318)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  - quote: "\U0001F4CB **Provider rejection logging.** When a model provider rejects
      a request, the reason it gave is now recorded in the server logs, so administrators
      can diagnose failures without querying the provider directly. [#27238](https://github.com/open-webui/open-webui/pull/27238),
      [#27237](https://github.com/open-webui/open-webui/issues/27237), [#26253](https://github.com/open-webui/open-webui/issues/26253)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 39-model-support-changes-in-v0-11-0
  source_release: open-webui-2026-07-27-v0-11-0-github-360322252-5f18424f
  source_type: github_releases
  theme: model-support
  title: 39 Model Support changes in v0.11.0
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-07-24-add-support-for-claude-opus-5|Add support
  for Claude Opus 5]]'
- '[[Changes/OpenCode/2026-07-24-core-preserve-mistral-reasoning-history-across-turns|Core
  Preserve Mistral reasoning history across turns]]'
- '[[Changes/Ollama/2026-07-25-quantize-draft-model-output-heads-at-the-requested-type-when-creating-speculativ|Quantize
  draft-model output heads at the requested type when creating…]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-07-27-v0-11-0-github-360322252-5f18424f|open-webui-2026-07-27-v0-11-0-github-360322252-5f18424f]]'
source_type: github_releases
theme: model-support
title: 39 Model Support changes in v0.11.0
type: change
---

<!-- chronolog:begin region="header" -->
# 39 Model Support changes in v0.11.0

**Open WebUI** · 2026-07-27 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.11.0) · from [[Releases/Open WebUI/open-webui-2026-07-27-v0-11-0-github-360322252-5f18424f|v0.11.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🔖 **Chat variables.** A model's system prompt can now declare fields such as text boxes and dropdown lists that you fill in for a conversation, with the values saved alongside the chat and carried over when it is forked or cloned. [Commit](https://github.com/open-webui/open-webui/commit/bef8ae4b2f05ca49ed88a02ab7a3cdc11b62c4f1), [Commit](https://github.com/open-webui/open-webui/commit/4e869011cd5040b5d6a197fc83d5f50d2425dbc2), [Commit](https://github.com/open-webui/open-webui/commit/1e88367cc837b39c0e9958fefbe053803336dce2), [Commit](https://github.com/open-webui/open-webui/commit/8cbb7f765cfc9c9b3237a6c5593cd93f849033f0), [Commit](https://github.com/open-webui/open-webui/commit/b35e2d265a4e4a2f2a075b31917d48be1dd9ef19), [Commit](https://github.com/open-webui/open-webui/commit/239cb740077a14e452ad002a1e671a09ab558e40), [#26915](https://github.com/open-webui/open-webui/discussions/26915)

> 📇 **User variables.** You can now store your own values in account settings, such as your role or how you like answers written, and a model's system prompt can insert them wherever they are needed. [Commit](https://github.com/open-webui/open-webui/commit/bd5d7b2e879511882429075d804d9222956f4a1a), [Commit](https://github.com/open-webui/open-webui/commit/212eec408ca320edfa2271e604d10e14b6a9bc1a), [Commit](https://github.com/open-webui/open-webui/commit/793a43d9c48225925929eb312fe2b70d5914d1da)

> 📝 **Chat with a note.** Chatting with a note now gives you the full chat experience, including model choice, tools and file attachments, alongside suggested prompts, a button to insert a response straight into the note, edits that appear in the note as the assistant makes them, and as many separate conversations per note as you want to keep. [Commit](https://github.com/open-webui/open-webui/commit/423cafd4e75e34b487f3b5d10ec1c506f073b3da), [Commit](https://github.com/open-webui/open-webui/commit/185bca8552ee3f87ea95fdcad32a433924881b9a)

> ↕️ **Sort your lists.** The notes, prompts, models, knowledge, skills, tools and functions lists can now be sorted by title or by when they were last updated, in either direction, by clicking the column headings. [Commit](https://github.com/open-webui/open-webui/commit/30c91e46e5d237bee3c8805bd54749408cc2727a), [Commit](https://github.com/open-webui/open-webui/commit/56f2cb530259df5393ea1ae844bad5cc6b2c810c), [#27457](https://github.com/open-webui/open-webui/pull/27457), [#27456](https://github.com/open-webui/open-webui/discussions/27456)

> 🗂️ **The assistant can search your attachments.** A new Files capability lets the model list the files attached to the chat and search them by meaning or by exact text, and read the parts it needs, rather than having their whole contents pushed into the conversation up front, and knowledge collections or notes attached to a chat are now announced to the model so it can query those the same way. [Commit](https://github.com/open-webui/open-webui/commit/57e60423b9963c4a69fdfda7ae5799efc5583010), [Commit](https://github.com/open-webui/open-webui/commit/55e0801dab8fe5f8bceff7d7c49772676724b8b1), [#26711](https://github.com/open-webui/open-webui/pull/26711), [#27232](https://github.com/open-webui/open-webui/issues/27232), [#26708](https://github.com/open-webui/open-webui/issues/26708)

> 🥇 **Model order as a setting.** Administrators can now set the order models appear in through a new "MODEL_ORDER_LIST" variable, so the arrangement survives a restart on instances that do not persist configuration. [#27420](https://github.com/open-webui/open-webui/pull/27420), [#27206](https://github.com/open-webui/open-webui/issues/27206)

> 💭 **Reasoning in Anthropic responses.** Responses from the Anthropic-compatible API now carry the model's reasoning as thinking blocks, in both streamed and complete responses. [Commit](https://github.com/open-webui/open-webui/commit/bb12b1a18b77d80829cedb2d5bf965808222415b)

> 🧩 **Structured output through the Anthropic-compatible API.** Requests can now ask for a JSON schema or JSON object response and set a reasoning effort, which are carried through to the upstream model. [Commit](https://github.com/open-webui/open-webui/commit/bb12b1a18b77d80829cedb2d5bf965808222415b)

> 🧮 **Counts in the tabs.** The workspace tabs now show how many models, knowledge bases, prompts, skills, and tools you have, and the admin tabs do the same for users, groups, leaderboard entries, and feedback, so you can see the size of each section without opening it. [Commit](https://github.com/open-webui/open-webui/commit/05e3f713175c1eea43a99f29521eb01700c21d3c), [Commit](https://github.com/open-webui/open-webui/commit/727041da78bcfcb44c0e4c83c4e6a641b7061b90), [Commit](https://github.com/open-webui/open-webui/commit/f8ea15b84a274712dca33daa970f63ed7368043e)

> 🧰 **Built-in tool descriptions built once.** The descriptions handed to the model for the built-in tools are now worked out once at startup rather than rebuilt on every message. [Commit](https://github.com/open-webui/open-webui/commit/d727ee4d1febb2b72d5f6c26668c562eadca54f1), [Commit](https://github.com/open-webui/open-webui/commit/12974c9e4ed97b2d68c4ad129c057ff0e774254e), [#27374](https://github.com/open-webui/open-webui/pull/27374), [#27396](https://github.com/open-webui/open-webui/pull/27396)

> 🪺 **Records read without a double pass.** Loading a model, tool, prompt, skill, note, knowledge base, channel or calendar no longer converts the record twice on the way out. [Commit](https://github.com/open-webui/open-webui/commit/f1409266feb224e74fe023d7459f1e2b5aad0b29), [#27377](https://github.com/open-webui/open-webui/pull/27377)

> 🪪 **Fewer checks before a reply starts.** Working out whether you may use a model now looks up the model and your group memberships once instead of repeating both, including for every model a workspace model is built on. [#27378](https://github.com/open-webui/open-webui/pull/27378)

> 🪄 **Lighter conversion for Ollama requests.** Preparing a request for an Ollama model no longer copies the entire conversation before sending it, which cost more with every message and repeated on each tool-call round. [#27371](https://github.com/open-webui/open-webui/pull/27371)

> 🚦 **No filter bookkeeping without filters.** Streamed API responses only build up the full reply for outlet filters when the model actually has one configured, instead of doing it for every request. [Commit](https://github.com/open-webui/open-webui/commit/315a6b5995663eabe1c96776d66b6593860d47d6), [#27391](https://github.com/open-webui/open-webui/pull/27391)

> ✂️ **Cheaper tag detection while streaming.** Watching a reply for reasoning and code blocks now examines only the newly arrived text rather than rescanning the whole answer on every chunk, so a long answer no longer costs progressively more as it grows. [#27360](https://github.com/open-webui/open-webui/pull/27360)

> 🔗 **Fewer Redis round trips per chat.** Deployments backed by Redis now look up the model and connected sessions once per request instead of twice, and fetch the model list in a single call. [#27225](https://github.com/open-webui/open-webui/pull/27225)

> 🪶 **Model lists without knowledge text.** Model lists no longer include the extracted text of files attached to a model as knowledge, so they stay small regardless of how large those knowledge bases are. [Commit](https://github.com/open-webui/open-webui/commit/48625e657ff11161c3588af2747598f102c1a4d1), [#27287](https://github.com/open-webui/open-webui/issues/27287)

> 📮 **Name lookups off the thread pool.** Looking up a hostname no longer occupies one of the limited threads shared by every other piece of blocking work, so model calls, searches, page fetches and tool calls stop queueing behind each other once a few lookups are slow. [#27440](https://github.com/open-webui/open-webui/pull/27440)

> 🎯 **Model settings in the list endpoint.** Listing models no longer includes each one's parameters and system prompt for people with read access only, matching what opening a single model already returned. [#27004](https://github.com/open-webui/open-webui/pull/27004)

> 🪜 **Reaching a restricted model through a shared one.** A shared workspace model can no longer be used to reach an underlying model the person could not otherwise use, which previously slipped through when that model had no entry of its own. [#26905](https://github.com/open-webui/open-webui/pull/26905), [#26900](https://github.com/open-webui/open-webui/issues/26900)

> 🎬 **Chat action availability.** Chat actions can no longer be triggered when they are disabled, not assigned to the model in use, or on a model the caller cannot access, matching the actions the interface actually offers. [#27243](https://github.com/open-webui/open-webui/pull/27243)

> ➡️ **Prompts opened from a link.** A prompt passed in through a link that sends automatically now waits for tool servers to finish loading, so external tools are available on that first message instead of the model reporting it has none. [Commit](https://github.com/open-webui/open-webui/commit/d7513e4ce81ada1936c0c34115f947e115d6f2cf), [#24176](https://github.com/open-webui/open-webui/issues/24176)

> 🪆 **Summaries on a direct connection.** Summarizing a long conversation on a direct connection can now use the configured summary model rather than being limited to the connection's own model. [#26806](https://github.com/open-webui/open-webui/pull/26806)

> 🎲 **Stable skill ordering.** Skills available to a model are now listed in the same order on every request, instead of shuffling between requests and quietly defeating prompt caching. [Commit](https://github.com/open-webui/open-webui/commit/b9d72741bb2f649cb67942ce7c635ea173f32b70), [#26986](https://github.com/open-webui/open-webui/issues/26986)

> ⭐ **Rating scale in multi-model replies.** The rating scale in the feedback panel is no longer cut off when several models answer side by side, so every score can be picked. [#26846](https://github.com/open-webui/open-webui/issues/26846)

> 🧑🤝🧑 **Duplicate models side by side.** Adding the same model twice in a side-by-side chat now keeps each column's own answer after a reload, instead of every column collapsing onto the first one. [#26980](https://github.com/open-webui/open-webui/pull/26980)

> 📱 **Model selector on small screens.** The model list now stays fully on screen and sizes itself to the space available, instead of running past the edge or hiding behind the on-screen keyboard on phones. [Commit](https://github.com/open-webui/open-webui/commit/79d3e34eea6dc2828d1945cc2b9fca5d662d825b), [Commit](https://github.com/open-webui/open-webui/commit/e39ff71532651438c32b2aa7ffe2b6068c94e6b2), [Commit](https://github.com/open-webui/open-webui/commit/ea31a3bd61fdf1a72206f9ed5f7252486d554c9b)

> 🧲 **Search quality with prefix-based embedding models.** Memories, knowledge base descriptions and searches against an external vector database now carry the query and content markers your embedding model expects, so results are no longer quietly worse than they should be on models that rely on them. [Commit](https://github.com/open-webui/open-webui/commit/c4f5ac65ee3cd20dd1d507eda04fca21a866910a), [#26958](https://github.com/open-webui/open-webui/pull/26958), [#26353](https://github.com/open-webui/open-webui/issues/26353)

> 🧬 **Shared pipe model tool calls.** Non-admin users of a shared model built on a pipe or manifold model no longer see the response silently stop right after a tool call. [#26906](https://github.com/open-webui/open-webui/pull/26906), [#26900](https://github.com/open-webui/open-webui/issues/26900)

> 🏷️ **Model names containing a connection prefix.** A prefix set on a connection is now removed only from the front of the model name, so a model whose own name contains that text is no longer mangled before the request is sent. [Commit](https://github.com/open-webui/open-webui/commit/ed663f16ecaaf99de194922d1634ecc5d906c703)

> 🦙 **Newly pulled Ollama models.** Sending a message to a model that was pulled after the list was last built now refreshes the list and proceeds, instead of reporting the model as not found. [Commit](https://github.com/open-webui/open-webui/commit/ed663f16ecaaf99de194922d1634ecc5d906c703), [#27353](https://github.com/open-webui/open-webui/pull/27353)

> 🗑️ **Deleting a model from the selector.** Removing a workspace model from the model selector menu now deletes just that model and leaves the underlying one in place, instead of failing with a not found error. [#26819](https://github.com/open-webui/open-webui/pull/26819)

> 👥 **Previewing what someone can use.** The preview of a person's access now includes the models, knowledge bases and tools they own, not just the ones shared with them. [Commit](https://github.com/open-webui/open-webui/commit/a9a3e5b95c8e641881fedc1ce7431eedab9a371b), [#27423](https://github.com/open-webui/open-webui/pull/27423), [#27407](https://github.com/open-webui/open-webui/discussions/27407)

> ♻️ **Connection changes take effect immediately.** Saving connection settings now refreshes the model list straight away, instead of leaving the previous models in place until the server was restarted.

> 🚫 **Disabled OpenAI connections are enforced.** Turning off the OpenAI API now blocks chat requests to it and clears its models, rather than only hiding it from the interface.

> 🏞️ **Images returned by a tool.** Images a tool produces are now passed to the model in a form the OpenAI-compatible providers accept, so it can actually look at them instead of receiving a result it cannot read. [Commit](https://github.com/open-webui/open-webui/commit/dd86b984bd508cf2841f08dae90411dfb5fe407f)

> 🔣 **Names containing a vertical bar.** What you insert with the at sign or a slash is now recorded by the key you typed rather than guessed from its name, so a prompt or model whose name contains a vertical bar is no longer mistaken for a skill. [Commit](https://github.com/open-webui/open-webui/commit/e28b391e514384ec329ca871d02189aa81fb1a00)

> ✳️ **Asterisks in the message input.** Wrapping a word in asterisks no longer silently turns it italic and swallows the asterisks, so your prompt reaches the model exactly as you typed it. [Commit](https://github.com/open-webui/open-webui/commit/001775d8e868ce44f125e0d683dd50363f0e8318)

> 📋 **Provider rejection logging.** When a model provider rejects a request, the reason it gave is now recorded in the server logs, so administrators can diagnose failures without querying the provider directly. [#27238](https://github.com/open-webui/open-webui/pull/27238), [#27237](https://github.com/open-webui/open-webui/issues/27237), [#26253](https://github.com/open-webui/open-webui/issues/26253)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.11.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-07-27-9-automation-and-scheduling-changes-in-v0-11-0|9 Automation and Scheduling changes in v0.11.0]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-07-27-13-safety-and-privacy-changes-in-v0-11-0|13 Safety and Privacy changes in v0.11.0]] · Safety and Privacy
- [[Changes/Open WebUI/2026-07-27-4-voice-and-audio-changes-in-v0-11-0|4 Voice and Audio changes in v0.11.0]] · Voice and Audio
- [[Changes/Open WebUI/2026-07-27-62-developer-workflow-changes-in-v0-11-0|62 Developer Workflow changes in v0.11.0]] · Developer Workflow
- [[Changes/Open WebUI/2026-07-27-19-interface-experience-changes-in-v0-11-0|19 Interface Experience changes in v0.11.0]] · Interface Experience
- [[Changes/Open WebUI/2026-07-27-7-memory-and-personalization-changes-in-v0-11-0|7 Memory and Personalization changes in v0.11.0]] · Memory and Personalization
- [[Changes/Open WebUI/2026-07-27-sub-agents-administrators-can-now-enable-sub-agents-which-let-a-model-hand-parts|🤖 Sub-agents. Administrators can now enable sub-agents, which let a model hand…]] · Agent Mode
- [[Changes/Open WebUI/2026-07-27-media-types-an-extraction-engine-may-handle-administrators-can-now-list-which-im|🖼️ Media types an extraction engine may handle. Administrators can now list…]] · Multimodal Input
- [[Changes/Open WebUI/2026-07-27-15-account-and-access-changes-in-v0-11-0|15 Account and Access changes in v0.11.0]] · Account and Access
- [[Changes/Open WebUI/2026-07-27-shared-image-checkpoint-changes-only-administrators-can-now-change-the-instance|🖌️ Shared image checkpoint changes. Only administrators can now change…]] · Image Generation
- [[Changes/Open WebUI/2026-07-27-7-search-and-browsing-changes-in-v0-11-0|7 Search and Browsing changes in v0.11.0]] · Search and Browsing
- [[Changes/Open WebUI/2026-07-27-2-collaboration-changes-in-v0-11-0|2 Collaboration changes in v0.11.0]] · Collaboration
- [[Changes/Open WebUI/2026-07-27-6-apps-and-integrations-changes-in-v0-11-0|6 Apps and Integrations changes in v0.11.0]] · Apps and Integrations
- [[Changes/Open WebUI/2026-07-27-3-enterprise-and-administration-changes-in-v0-11-0|3 Enterprise and Administration changes in v0.11.0]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-07-27-9-context-window-changes-in-v0-11-0|9 Context Window changes in v0.11.0]] · Context Window
- [[Changes/Open WebUI/2026-07-27-12-reliability-and-performance-changes-in-v0-11-0|12 Reliability and Performance changes in v0.11.0]] · Reliability and Performance
- [[Changes/Open WebUI/2026-07-27-2-pricing-model-changes-in-v0-11-0|2 Pricing Model changes in v0.11.0]] · Pricing Model
- [[Changes/Open WebUI/2026-07-27-9-files-and-data-changes-in-v0-11-0|9 Files and Data changes in v0.11.0]] · Files and Data
- [[Changes/Open WebUI/2026-07-27-7-editor-experience-changes-in-v0-11-0|7 Editor Experience changes in v0.11.0]] · Editor Experience
- [[Changes/Open WebUI/2026-07-27-2-mobile-and-desktop-changes-in-v0-11-0|2 Mobile and Desktop changes in v0.11.0]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-07-27-42-other-changes-in-v0-11-0|42 other changes in v0.11.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-07-25 · Ollama · [[Changes/Ollama/2026-07-25-quantize-draft-model-output-heads-at-the-requested-type-when-creating-speculativ|Quantize draft-model output heads at the requested type when creating…]]
- Later: 2026-07-28 · Cline · [[Changes/Cline/2026-07-28-add-support-for-free-cline-models-shown-as-free-in-the-model-picker-with-a-dedic|Add support for free Cline models, shown as "(free)" in the model picker…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-07-27-ebf99c&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-07-27-39-model-support-changes-in-v0-11-0.md%0ACard%20ID%3A%20open-webui-2026-07-27-ebf99c%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.11.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->