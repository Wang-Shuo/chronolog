---
card_id: open-webui-2026-09-21-e8cce4
date: '2026-09-21'
description: "Open WebUI · 2026-09-21 · Model Support: 41 changes in v0.11.4 — \U0001F4C9
  **Far smaller slim image.** A slim build now comes down at around 175 MB, near enough
  89%…"
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1351
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: d0fa294f5e1ab453fefc29b1bec3f657e3dd2699c752375f4c643f3c075be91b
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-09-21-e8cce4
  comparison: ''
  date: '2026-09-21'
  description: 'Open WebUI — v0.11.4: 41 Model Support changes'
  evidence:
  - quote: "\U0001F4C9 **Far smaller slim image.** A slim build now comes down at
      around 175 MB, near enough 89% smaller than the last release, the local models,
      the packages around them and the tools that installed them all gone from it;
      what that changes about the way an instance behaves is set out under Changed
      below and in the documentation. [Commit](https://github.com/open-webui/open-webui/commit/cb942bb94c8dc7941336088fb3392e2398ff56c1),
      [Commit](https://github.com/open-webui/open-webui/commit/d27aa72ab4a7b5632b4ad49e8467081ad3d7ebb4)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F4C7 **Automatic skill discovery.** Every skill you can reach is
      now listed to the model by name and description, and the full text of one is
      loaded only when it decides to use it; before, a skill you had not selected
      in the message box was invisible to it, and this applies to models with built-in
      tools on. [Commit](https://github.com/open-webui/open-webui/commit/e69236bccb1e12d14045b09b76ebac0490014851)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F310 **Suggested prompts in your language.** A fresh install now
      offers its suggested starter prompts in the language the interface is set to,
      rather than the same four in English for everyone, and the model defaults panel
      carries a way back to those defaults once its own suggestions have been edited.
      [Commit](https://github.com/open-webui/open-webui/commit/30881dbcc966206cc15fb0b2276b41d88f7c0f09),
      [Commit](https://github.com/open-webui/open-webui/commit/9fba2843b16a111b035949f5865e29ec6cf5ac9c)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F3F7️ **Custom file metadata.** Metadata attached to an uploaded
      file now travels with the pieces that file is split into and arrives with the
      retrieved sources, the oversized and internal fields left out, and an operator
      can name in \"RAG_SOURCE_METADATA_KEYS\" which of those fields the model itself
      gets to see alongside the text. [#29499](https://github.com/open-webui/open-webui/pull/29499),
      [#29486](https://github.com/open-webui/open-webui/issues/29486), [Commit](https://github.com/open-webui/open-webui/commit/894655f66b9563890e63c76090ddecc90a311eb2),
      [#29502](https://github.com/open-webui/open-webui/pull/29502), [#29696](https://github.com/open-webui/open-webui/pull/29696)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F39B️ **Admin model list filters.** The models page in the admin
      settings can now be narrowed to the base models a connection offers or to the
      ones built in the workspace, alongside the filters for enabled, disabled, visible
      and hidden. [Commit](https://github.com/open-webui/open-webui/commit/9e634c0c56e0a060717f1e24a11b082daf664036)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F198 **A model for every chat.** Opening a conversation whose model
      has since been retired no longer leaves it stranded with nothing selected; it
      falls back to your default model, then the configured default, then the first
      one available, and a chat that still has a live model keeps it. [#29757](https://github.com/open-webui/open-webui/pull/29757)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: ⚡ **Non-blocking search.** Searching the text of chats and knowledge, and
      the grep a model runs over a knowledge base, now run beside the rest of the
      server rather than in front of it, so a long search no longer keeps other requests
      waiting. [#29621](https://github.com/open-webui/open-webui/pull/29621), [Commit](https://github.com/open-webui/open-webui/commit/d9c8de9c39fca7c4756e0f9bd599b09ebe435208)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F522 **Sorted knowledge listings.** The \"ls\", \"tree\" and \"find\"
      commands a model runs over a knowledge base now sort by name and take \"-t\",
      \"-S\" and \"-r\" for newest first, largest first and reversed. [#29840](https://github.com/open-webui/open-webui/pull/29840)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001FAB5 **Model refusal logging.** A request turned away with \"Model
      not found\" now writes a warning naming the account, the model and why it was
      refused, while the message the caller sees stays as vague as before. [Commit](https://github.com/open-webui/open-webui/commit/f5fcf4c89fb27ed39825875d573446fa84aa2a5b)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F932 **Cheaper chat requests behind Redis.** Where several servers
      share their websocket traffic through Redis, a chat request no longer pulls
      the whole shared model list from Redis to ask about a couple of models; each
      worker keeps its own copy and refetches only when the list actually changed,
      so the cost stops growing with the number of models configured. [#28176](https://github.com/open-webui/open-webui/pull/28176),
      [#28167](https://github.com/open-webui/open-webui/issues/28167)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F512 **Connection model listing access.** The endpoints that list
      the models on a single Ollama or OpenAI connection could be reached by a signed-in
      account of any role, and now check the caller's role. [#29619](https://github.com/open-webui/open-webui/pull/29619)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F4F7 **Attachments sent without text.** Sending an image or a file
      with nothing typed to a model that has skills attached replaced the empty message
      with the list of skill names, so the model answered with its own catalogue instead
      of looking at what you sent. [#30045](https://github.com/open-webui/open-webui/pull/30045),
      [#30040](https://github.com/open-webui/open-webui/issues/30040)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F58D️ **SVG attachments read as text.** An SVG attached to a chat
      went up as a picture and came back rejected by every model that tried to decode
      it, and is now read as its source text instead, which needs a model that accepts
      file uploads. [#30102](https://github.com/open-webui/open-webui/pull/30102),
      [#30100](https://github.com/open-webui/open-webui/issues/30100)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001FA79 **Notes survive a small edit.** Asked to add a section or change
      a few lines, a model would send the whole note back and lose the rest of it
      with nothing to undo, because the editing tool never said when to edit a range
      instead; it now spells out the range rules the handler already enforced. [#30048](https://github.com/open-webui/open-webui/pull/30048)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F4D1 **Tika 4 document formatting.** Where document extraction runs
      against a Tika server on version 4, the text now comes back as Markdown rather
      than a flat run of characters, so headings, lists and tables survive into what
      the model reads. [Commit](https://github.com/open-webui/open-webui/commit/ba34bee2d17e1c00238c85a8aab1a11a60db164e)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F6BF **Tool results arrive when the tools are done.** The results
      of a model's tool calls now reach the reply as soon as the round that produced
      them finishes, instead of being held back with the rest of the streaming until
      the throttle let them through, and a channel reply or a continuation no longer
      carries the picture data a tool handed the model. [Commit](https://github.com/open-webui/open-webui/commit/478d1785fd27f400c614a5700f5b38ec9de412f9)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F64B **Typed answer submission.** In the card a model puts up to
      ask you a question, choosing one of its options on the last question sends your
      answers straight away, but typing your own into the Other box left Submit answers
      greyed out with no way to send it, and it now turns on as soon as that box has
      text. [#29494](https://github.com/open-webui/open-webui/pull/29494), [#29311](https://github.com/open-webui/open-webui/issues/29311)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F947 **A truthful Recommended badge.** The card a model puts up
      to ask you a question marks its first option Recommended, but nothing told the
      model that, so the badge fell on whichever option happened to be listed first;
      models are now asked to put the option they recommend there. [#30196](https://github.com/open-webui/open-webui/pull/30196),
      [#30195](https://github.com/open-webui/open-webui/issues/30195)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F4DC **Task list height.** The list of steps a model works through
      ran as long as it needed and pushed the rest of the reply down the page; it
      now stops at a quarter of the window's height and scrolls within itself. [Commit](https://github.com/open-webui/open-webui/commit/307b9b9133f0c7ad899f4b76226059da6f3177eb)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001FA99 **Model defaults save.** Saving the model defaults in the admin
      settings put the selected, pinned and ordered models back as they stood when
      the page was opened, undoing anything changed in between. [#30206](https://github.com/open-webui/open-webui/pull/30206)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F411 **Model clones keep their base.** Cloning a model from the
      admin Models settings now carries the model it was built on, where the clone
      came out detached from it, and an arena model no longer offers Clone at all.
      [#30080](https://github.com/open-webui/open-webui/pull/30080), [#30079](https://github.com/open-webui/open-webui/issues/30079)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F4AC **Model description round trips.** A workspace model whose
      description is switched from the default back to custom saves again, where the
      switch read the field as empty and the description was dropped on save. [#30249](https://github.com/open-webui/open-webui/pull/30249),
      [#30247](https://github.com/open-webui/open-webui/issues/30247)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F9FD **Knowledge folder deletion.** Deleting a folder without moving
      what was in it up a level dropped the files from the listing but left their
      text in the search index and the files themselves in storage, so a model went
      on retrieving and citing pages from a folder that was no longer there; the text
      is now removed with the folder, and a file no other knowledge base holds is
      deleted with it unless file retention is switched on. [Commit](https://github.com/open-webui/open-webui/commit/17dbc6f001aeea25ae1df528cb79bb272eca4a77)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F4E3 **Model mention chips.** A mention whose ID carried anything
      beyond letters, digits and a little punctuation, such as the brackets in some
      workspace model IDs, stayed on screen as the raw \"<@…>\" text both in the box
      you type in and in the message once sent; any ID without a space in it is now
      drawn as a chip. [#29864](https://github.com/open-webui/open-webui/pull/29864)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001FAA7 **False skill mentions.** Something written as \"<$fh>\" in
      a message, as Perl and other languages do, was taken for a mention of a skill
      and quietly removed before the model saw it, and drawn on screen as a chip;
      only mentions naming a skill that exists and is turned on are treated as mentions
      now. [Commit](https://github.com/open-webui/open-webui/commit/0edd731c7422870aa109fd0b758c6d68c06655da)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: ⛔ **Malformed tool calls.** Where a model asked for a tool with arguments
      that were not an object at all, a bare list or string, the reply stopped there;
      the model is now told what was wrong with the call and can try again. [Commit](https://github.com/open-webui/open-webui/commit/fed94c9f5af8a59660425d52df09e15fbedb25bc)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F9F7 **Chat unblocked after an error.** A reply that failed, on
      a content filter or an exhausted quota, left the chat turning away everything
      you typed after it and stopped the message queue. Only the failed reply now
      ends, so the chat carries on and the other replies in a multi-model answer keep
      writing. [Commit](https://github.com/open-webui/open-webui/commit/dbb17a5725f9d7f844a6eee63ffca0bd077c7d94)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001FAD9 **Empty failed replies in history.** An assistant turn that
      ended in an error with nothing written is no longer handed back to the model
      as part of the conversation when you send your next message. [Commit](https://github.com/open-webui/open-webui/commit/dbb17a5725f9d7f844a6eee63ffca0bd077c7d94)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F58C **Editing a stored image.** Asking a model to edit an image
      this instance already holds now works whatever host its address names, where
      a container name, a default port or a self-composed host made the edit fail
      with a generic loading error. [#29691](https://github.com/open-webui/open-webui/pull/29691),
      [#29220](https://github.com/open-webui/open-webui/issues/29220)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F4E4 **Tool export scope.** Exporting all tools at once returned
      every tool the account could see, the source of a tool shared for reading included;
      it now returns only the tools it may edit, matching the single-tool export and
      the way models already export. [#29310](https://github.com/open-webui/open-webui/pull/29310)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F5F3️ **Partial workspace exports.** Exporting the prompts or the
      models from the workspace wrote out only the page you happened to be looking
      at, so most of them were quietly left out of the file; both now export everything
      you are allowed to. [#30187](https://github.com/open-webui/open-webui/pull/30187)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F510 **Model pictures follow model access.** The picture belonging
      to a model is now shown only to people who can see that model, where anyone
      signed in could fetch it and tell an existing model from an unknown one by which
      picture came back. [#29700](https://github.com/open-webui/open-webui/pull/29700)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F34E **Answers survive on Apple Silicon.** Asking a question that
      searches a knowledge base with a locally run reranking model no longer takes
      the whole server down on a Mac, losing the answer and the connection with it.
      [#29735](https://github.com/open-webui/open-webui/pull/29735), [#29722](https://github.com/open-webui/open-webui/issues/29722)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F3DF️ **Arena models report their errors.** A message to an arena
      model whose provider answers with an error now shows that error in the chat,
      where it used to fail on something unrelated and leave the real reason unsaid,
      and titles and tags no longer break the same way. [#29662](https://github.com/open-webui/open-webui/pull/29662),
      [#29658](https://github.com/open-webui/open-webui/issues/29658)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F3F3️ **Nameless tool calls fail once.** A model endpoint that sends
      a tool call with no name at all now has that call fail on the spot, rather than
      the missing name being kept, stored with the message and sent back on the next
      turn for the endpoint to reject. [#29690](https://github.com/open-webui/open-webui/pull/29690),
      [#29686](https://github.com/open-webui/open-webui/issues/29686)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F4F0 **Docling conversion failures.** A file that Docling refuses
      or fails to convert now fails the upload with the reason Docling gave, rather
      than breaking with a raw error or quietly filing a placeholder that was then
      indexed and handed to the model in place of the file. [#30107](https://github.com/open-webui/open-webui/pull/30107),
      [#29808](https://github.com/open-webui/open-webui/issues/29808)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F4C4 **Uploaded text kept as written.** A file whose text contains
      escape sequences such as the one standing for a non-breaking space is now stored
      and read by the model exactly as it was written, rather than having some of
      them rewritten depending on where in the file they sat. [#29736](https://github.com/open-webui/open-webui/pull/29736),
      [#29732](https://github.com/open-webui/open-webui/issues/29732)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F6AE **Retired chat variables.** A model whose system prompt no
      longer declares a variable a previous prompt did stops asking for it, where
      every new chat kept opening the dialog and refusing to send until a value was
      entered. [#30173](https://github.com/open-webui/open-webui/pull/30173), [#30172](https://github.com/open-webui/open-webui/issues/30172)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001FAB6 **Slim starts with nothing configured.** The slim image leaves
      out the local models and the libraries around them, and still starts and holds
      a conversation on its defaults; the features that leaned on those models each
      need an external service of their own. [Commit](https://github.com/open-webui/open-webui/commit/cb942bb94c8dc7941336088fb3392e2398ff56c1)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F9E0 **Slim embedding requirements.** The slim image carries no
      embedding or reranking model, so knowledge needs OpenAI, Ollama or Azure OpenAI
      embeddings and an external reranker, falling back to plain cosine scoring where
      none is set. [Commit](https://github.com/open-webui/open-webui/commit/cb942bb94c8dc7941336088fb3392e2398ff56c1)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F9FE **Undeclared package imports.** Packages that sat in the image
      only by accident, among them nltk, pymongo, the Google Drive client and the
      Gemini SDK, are no longer installed, so a tool or function importing one must
      name it in its own requirements. [#29725](https://github.com/open-webui/open-webui/pull/29725),
      [#29726](https://github.com/open-webui/open-webui/pull/29726), [Commit](https://github.com/open-webui/open-webui/commit/a1c02098aa2687c72482a59117efe643b785df51)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 41-model-support-changes-in-v0-11-4
  source_release: open-webui-2026-09-21-v0-11-4-github-393232555-90de9130
  source_type: github_releases
  theme: model-support
  title: 41 Model Support changes in v0.11.4
  type: change
related_changes:
- '[[Changes/ElevenLabs/2026-09-21-python-sdk|Python SDK]]'
- '[[Changes/GitHub Copilot CLI/2026-09-21-enable-the-rubber-duck-agent-for-every-model-family-and-for-low-cost-tier-sessio|Enable
  the rubber-duck agent for every model family and for low-cost-tier session models]]'
- '[[Changes/Lovable/2026-09-21-jev-for-typed-decisions-in-your-app-s-ai-features|Jev
  for typed decisions in your app''s AI features]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-09-21-v0-11-4-github-393232555-90de9130|open-webui-2026-09-21-v0-11-4-github-393232555-90de9130]]'
source_type: github_releases
theme: model-support
title: 41 Model Support changes in v0.11.4
type: change
---

<!-- chronolog:begin region="header" -->
# 41 Model Support changes in v0.11.4

**Open WebUI** · 2026-09-21 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.11.4) · from [[Releases/Open WebUI/open-webui-2026-09-21-v0-11-4-github-393232555-90de9130|v0.11.4]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 📉 **Far smaller slim image.** A slim build now comes down at around 175 MB, near enough 89% smaller than the last release, the local models, the packages around them and the tools that installed them all gone from it; what that changes about the way an instance behaves is set out under Changed below and in the documentation. [Commit](https://github.com/open-webui/open-webui/commit/cb942bb94c8dc7941336088fb3392e2398ff56c1), [Commit](https://github.com/open-webui/open-webui/commit/d27aa72ab4a7b5632b4ad49e8467081ad3d7ebb4)

> 📇 **Automatic skill discovery.** Every skill you can reach is now listed to the model by name and description, and the full text of one is loaded only when it decides to use it; before, a skill you had not selected in the message box was invisible to it, and this applies to models with built-in tools on. [Commit](https://github.com/open-webui/open-webui/commit/e69236bccb1e12d14045b09b76ebac0490014851)

> 🌐 **Suggested prompts in your language.** A fresh install now offers its suggested starter prompts in the language the interface is set to, rather than the same four in English for everyone, and the model defaults panel carries a way back to those defaults once its own suggestions have been edited. [Commit](https://github.com/open-webui/open-webui/commit/30881dbcc966206cc15fb0b2276b41d88f7c0f09), [Commit](https://github.com/open-webui/open-webui/commit/9fba2843b16a111b035949f5865e29ec6cf5ac9c)

> 🏷️ **Custom file metadata.** Metadata attached to an uploaded file now travels with the pieces that file is split into and arrives with the retrieved sources, the oversized and internal fields left out, and an operator can name in "RAG_SOURCE_METADATA_KEYS" which of those fields the model itself gets to see alongside the text. [#29499](https://github.com/open-webui/open-webui/pull/29499), [#29486](https://github.com/open-webui/open-webui/issues/29486), [Commit](https://github.com/open-webui/open-webui/commit/894655f66b9563890e63c76090ddecc90a311eb2), [#29502](https://github.com/open-webui/open-webui/pull/29502), [#29696](https://github.com/open-webui/open-webui/pull/29696)

> 🎛️ **Admin model list filters.** The models page in the admin settings can now be narrowed to the base models a connection offers or to the ones built in the workspace, alongside the filters for enabled, disabled, visible and hidden. [Commit](https://github.com/open-webui/open-webui/commit/9e634c0c56e0a060717f1e24a11b082daf664036)

> 🆘 **A model for every chat.** Opening a conversation whose model has since been retired no longer leaves it stranded with nothing selected; it falls back to your default model, then the configured default, then the first one available, and a chat that still has a live model keeps it. [#29757](https://github.com/open-webui/open-webui/pull/29757)

> ⚡ **Non-blocking search.** Searching the text of chats and knowledge, and the grep a model runs over a knowledge base, now run beside the rest of the server rather than in front of it, so a long search no longer keeps other requests waiting. [#29621](https://github.com/open-webui/open-webui/pull/29621), [Commit](https://github.com/open-webui/open-webui/commit/d9c8de9c39fca7c4756e0f9bd599b09ebe435208)

> 🔢 **Sorted knowledge listings.** The "ls", "tree" and "find" commands a model runs over a knowledge base now sort by name and take "-t", "-S" and "-r" for newest first, largest first and reversed. [#29840](https://github.com/open-webui/open-webui/pull/29840)

> 🪵 **Model refusal logging.** A request turned away with "Model not found" now writes a warning naming the account, the model and why it was refused, while the message the caller sees stays as vague as before. [Commit](https://github.com/open-webui/open-webui/commit/f5fcf4c89fb27ed39825875d573446fa84aa2a5b)

> 🤲 **Cheaper chat requests behind Redis.** Where several servers share their websocket traffic through Redis, a chat request no longer pulls the whole shared model list from Redis to ask about a couple of models; each worker keeps its own copy and refetches only when the list actually changed, so the cost stops growing with the number of models configured. [#28176](https://github.com/open-webui/open-webui/pull/28176), [#28167](https://github.com/open-webui/open-webui/issues/28167)

> 🔒 **Connection model listing access.** The endpoints that list the models on a single Ollama or OpenAI connection could be reached by a signed-in account of any role, and now check the caller's role. [#29619](https://github.com/open-webui/open-webui/pull/29619)

> 📷 **Attachments sent without text.** Sending an image or a file with nothing typed to a model that has skills attached replaced the empty message with the list of skill names, so the model answered with its own catalogue instead of looking at what you sent. [#30045](https://github.com/open-webui/open-webui/pull/30045), [#30040](https://github.com/open-webui/open-webui/issues/30040)

> 🖍️ **SVG attachments read as text.** An SVG attached to a chat went up as a picture and came back rejected by every model that tried to decode it, and is now read as its source text instead, which needs a model that accepts file uploads. [#30102](https://github.com/open-webui/open-webui/pull/30102), [#30100](https://github.com/open-webui/open-webui/issues/30100)

> 🩹 **Notes survive a small edit.** Asked to add a section or change a few lines, a model would send the whole note back and lose the rest of it with nothing to undo, because the editing tool never said when to edit a range instead; it now spells out the range rules the handler already enforced. [#30048](https://github.com/open-webui/open-webui/pull/30048)

> 📑 **Tika 4 document formatting.** Where document extraction runs against a Tika server on version 4, the text now comes back as Markdown rather than a flat run of characters, so headings, lists and tables survive into what the model reads. [Commit](https://github.com/open-webui/open-webui/commit/ba34bee2d17e1c00238c85a8aab1a11a60db164e)

> 🚿 **Tool results arrive when the tools are done.** The results of a model's tool calls now reach the reply as soon as the round that produced them finishes, instead of being held back with the rest of the streaming until the throttle let them through, and a channel reply or a continuation no longer carries the picture data a tool handed the model. [Commit](https://github.com/open-webui/open-webui/commit/478d1785fd27f400c614a5700f5b38ec9de412f9)

> 🙋 **Typed answer submission.** In the card a model puts up to ask you a question, choosing one of its options on the last question sends your answers straight away, but typing your own into the Other box left Submit answers greyed out with no way to send it, and it now turns on as soon as that box has text. [#29494](https://github.com/open-webui/open-webui/pull/29494), [#29311](https://github.com/open-webui/open-webui/issues/29311)

> 🥇 **A truthful Recommended badge.** The card a model puts up to ask you a question marks its first option Recommended, but nothing told the model that, so the badge fell on whichever option happened to be listed first; models are now asked to put the option they recommend there. [#30196](https://github.com/open-webui/open-webui/pull/30196), [#30195](https://github.com/open-webui/open-webui/issues/30195)

> 📜 **Task list height.** The list of steps a model works through ran as long as it needed and pushed the rest of the reply down the page; it now stops at a quarter of the window's height and scrolls within itself. [Commit](https://github.com/open-webui/open-webui/commit/307b9b9133f0c7ad899f4b76226059da6f3177eb)

> 🪙 **Model defaults save.** Saving the model defaults in the admin settings put the selected, pinned and ordered models back as they stood when the page was opened, undoing anything changed in between. [#30206](https://github.com/open-webui/open-webui/pull/30206)

> 🐑 **Model clones keep their base.** Cloning a model from the admin Models settings now carries the model it was built on, where the clone came out detached from it, and an arena model no longer offers Clone at all. [#30080](https://github.com/open-webui/open-webui/pull/30080), [#30079](https://github.com/open-webui/open-webui/issues/30079)

> 💬 **Model description round trips.** A workspace model whose description is switched from the default back to custom saves again, where the switch read the field as empty and the description was dropped on save. [#30249](https://github.com/open-webui/open-webui/pull/30249), [#30247](https://github.com/open-webui/open-webui/issues/30247)

> 🧽 **Knowledge folder deletion.** Deleting a folder without moving what was in it up a level dropped the files from the listing but left their text in the search index and the files themselves in storage, so a model went on retrieving and citing pages from a folder that was no longer there; the text is now removed with the folder, and a file no other knowledge base holds is deleted with it unless file retention is switched on. [Commit](https://github.com/open-webui/open-webui/commit/17dbc6f001aeea25ae1df528cb79bb272eca4a77)

> 📣 **Model mention chips.** A mention whose ID carried anything beyond letters, digits and a little punctuation, such as the brackets in some workspace model IDs, stayed on screen as the raw "<@…>" text both in the box you type in and in the message once sent; any ID without a space in it is now drawn as a chip. [#29864](https://github.com/open-webui/open-webui/pull/29864)

> 🪧 **False skill mentions.** Something written as "<$fh>" in a message, as Perl and other languages do, was taken for a mention of a skill and quietly removed before the model saw it, and drawn on screen as a chip; only mentions naming a skill that exists and is turned on are treated as mentions now. [Commit](https://github.com/open-webui/open-webui/commit/0edd731c7422870aa109fd0b758c6d68c06655da)

> ⛔ **Malformed tool calls.** Where a model asked for a tool with arguments that were not an object at all, a bare list or string, the reply stopped there; the model is now told what was wrong with the call and can try again. [Commit](https://github.com/open-webui/open-webui/commit/fed94c9f5af8a59660425d52df09e15fbedb25bc)

> 🧷 **Chat unblocked after an error.** A reply that failed, on a content filter or an exhausted quota, left the chat turning away everything you typed after it and stopped the message queue. Only the failed reply now ends, so the chat carries on and the other replies in a multi-model answer keep writing. [Commit](https://github.com/open-webui/open-webui/commit/dbb17a5725f9d7f844a6eee63ffca0bd077c7d94)

> 🫙 **Empty failed replies in history.** An assistant turn that ended in an error with nothing written is no longer handed back to the model as part of the conversation when you send your next message. [Commit](https://github.com/open-webui/open-webui/commit/dbb17a5725f9d7f844a6eee63ffca0bd077c7d94)

> 🖌 **Editing a stored image.** Asking a model to edit an image this instance already holds now works whatever host its address names, where a container name, a default port or a self-composed host made the edit fail with a generic loading error. [#29691](https://github.com/open-webui/open-webui/pull/29691), [#29220](https://github.com/open-webui/open-webui/issues/29220)

> 📤 **Tool export scope.** Exporting all tools at once returned every tool the account could see, the source of a tool shared for reading included; it now returns only the tools it may edit, matching the single-tool export and the way models already export. [#29310](https://github.com/open-webui/open-webui/pull/29310)

> 🗳️ **Partial workspace exports.** Exporting the prompts or the models from the workspace wrote out only the page you happened to be looking at, so most of them were quietly left out of the file; both now export everything you are allowed to. [#30187](https://github.com/open-webui/open-webui/pull/30187)

> 🔐 **Model pictures follow model access.** The picture belonging to a model is now shown only to people who can see that model, where anyone signed in could fetch it and tell an existing model from an unknown one by which picture came back. [#29700](https://github.com/open-webui/open-webui/pull/29700)

> 🍎 **Answers survive on Apple Silicon.** Asking a question that searches a knowledge base with a locally run reranking model no longer takes the whole server down on a Mac, losing the answer and the connection with it. [#29735](https://github.com/open-webui/open-webui/pull/29735), [#29722](https://github.com/open-webui/open-webui/issues/29722)

> 🏟️ **Arena models report their errors.** A message to an arena model whose provider answers with an error now shows that error in the chat, where it used to fail on something unrelated and leave the real reason unsaid, and titles and tags no longer break the same way. [#29662](https://github.com/open-webui/open-webui/pull/29662), [#29658](https://github.com/open-webui/open-webui/issues/29658)

> 🏳️ **Nameless tool calls fail once.** A model endpoint that sends a tool call with no name at all now has that call fail on the spot, rather than the missing name being kept, stored with the message and sent back on the next turn for the endpoint to reject. [#29690](https://github.com/open-webui/open-webui/pull/29690), [#29686](https://github.com/open-webui/open-webui/issues/29686)

> 📰 **Docling conversion failures.** A file that Docling refuses or fails to convert now fails the upload with the reason Docling gave, rather than breaking with a raw error or quietly filing a placeholder that was then indexed and handed to the model in place of the file. [#30107](https://github.com/open-webui/open-webui/pull/30107), [#29808](https://github.com/open-webui/open-webui/issues/29808)

> 📄 **Uploaded text kept as written.** A file whose text contains escape sequences such as the one standing for a non-breaking space is now stored and read by the model exactly as it was written, rather than having some of them rewritten depending on where in the file they sat. [#29736](https://github.com/open-webui/open-webui/pull/29736), [#29732](https://github.com/open-webui/open-webui/issues/29732)

> 🚮 **Retired chat variables.** A model whose system prompt no longer declares a variable a previous prompt did stops asking for it, where every new chat kept opening the dialog and refusing to send until a value was entered. [#30173](https://github.com/open-webui/open-webui/pull/30173), [#30172](https://github.com/open-webui/open-webui/issues/30172)

> 🪶 **Slim starts with nothing configured.** The slim image leaves out the local models and the libraries around them, and still starts and holds a conversation on its defaults; the features that leaned on those models each need an external service of their own. [Commit](https://github.com/open-webui/open-webui/commit/cb942bb94c8dc7941336088fb3392e2398ff56c1)

> 🧠 **Slim embedding requirements.** The slim image carries no embedding or reranking model, so knowledge needs OpenAI, Ollama or Azure OpenAI embeddings and an external reranker, falling back to plain cosine scoring where none is set. [Commit](https://github.com/open-webui/open-webui/commit/cb942bb94c8dc7941336088fb3392e2398ff56c1)

> 🧾 **Undeclared package imports.** Packages that sat in the image only by accident, among them nltk, pymongo, the Google Drive client and the Gemini SDK, are no longer installed, so a tool or function importing one must name it in its own requirements. [#29725](https://github.com/open-webui/open-webui/pull/29725), [#29726](https://github.com/open-webui/open-webui/pull/29726), [Commit](https://github.com/open-webui/open-webui/commit/a1c02098aa2687c72482a59117efe643b785df51)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-09-21-4-safety-and-privacy-changes-in-v0-11-4|4 Safety and Privacy changes in v0.11.4]] · Safety and Privacy
- [[Changes/Open WebUI/2026-09-21-3-context-window-changes-in-v0-11-4|3 Context Window changes in v0.11.4]] · Context Window
- [[Changes/Open WebUI/2026-09-21-general-improvements-various-improvements-were-implemented-across-the-applicatio|🔄 General improvements. Various improvements were implemented across…]] · Reliability and Performance
- [[Changes/Open WebUI/2026-09-21-6-account-and-access-changes-in-v0-11-4|6 Account and Access changes in v0.11.4]] · Account and Access
- [[Changes/Open WebUI/2026-09-21-39-developer-workflow-changes-in-v0-11-4|39 Developer Workflow changes in v0.11.4]] · Developer Workflow
- [[Changes/Open WebUI/2026-09-21-2-image-generation-changes-in-v0-11-4|2 Image Generation changes in v0.11.4]] · Image Generation
- [[Changes/Open WebUI/2026-09-21-4-collaboration-changes-in-v0-11-4|4 Collaboration changes in v0.11.4]] · Collaboration
- [[Changes/Open WebUI/2026-09-21-5-voice-and-audio-changes-in-v0-11-4|5 Voice and Audio changes in v0.11.4]] · Voice and Audio
- [[Changes/Open WebUI/2026-09-21-10-files-and-data-changes-in-v0-11-4|10 Files and Data changes in v0.11.4]] · Files and Data
- [[Changes/Open WebUI/2026-09-21-21-editor-experience-changes-in-v0-11-4|21 Editor Experience changes in v0.11.4]] · Editor Experience
- [[Changes/Open WebUI/2026-09-21-6-memory-and-personalization-changes-in-v0-11-4|6 Memory and Personalization changes in v0.11.4]] · Memory and Personalization
- [[Changes/Open WebUI/2026-09-21-apple-device-replies-an-assistant-reply-no-longer-comes-up-blank-in-a-home-scree|📱 Apple device replies. An assistant reply no longer comes up blank in a home…]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-09-21-3-apps-and-integrations-changes-in-v0-11-4|3 Apps and Integrations changes in v0.11.4]] · Apps and Integrations
- [[Changes/Open WebUI/2026-09-21-6-search-and-browsing-changes-in-v0-11-4|6 Search and Browsing changes in v0.11.4]] · Search and Browsing
- [[Changes/Open WebUI/2026-09-21-13-interface-experience-changes-in-v0-11-4|13 Interface Experience changes in v0.11.4]] · Interface Experience
- [[Changes/Open WebUI/2026-09-21-4-automation-and-scheduling-changes-in-v0-11-4|4 Automation and Scheduling changes in v0.11.4]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-09-21-5-enterprise-and-administration-changes-in-v0-11-4|5 Enterprise and Administration changes in v0.11.4]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-09-21-61-other-changes-in-v0-11-4|61 other changes in v0.11.4]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-09-21 · Lovable · [[Changes/Lovable/2026-09-21-jev-for-typed-decisions-in-your-app-s-ai-features|Jev for typed decisions in your app's AI features]]
- Later: 2026-09-22 · Claude · [[Changes/Claude/2026-09-22-claude-opus-5-5-launch|Claude Opus 5.5 launch]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-09-21-e8cce4&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-09-21-41-model-support-changes-in-v0-11-4.md%0ACard%20ID%3A%20open-webui-2026-09-21-e8cce4%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.11.4%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->