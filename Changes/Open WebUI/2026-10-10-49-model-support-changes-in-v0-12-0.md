---
card_id: open-webui-2026-10-10-5c62e0
date: '2026-10-10'
description: "Open WebUI · 2026-10-10 · Model Support: 49 changes in v0.12.0 — \U0001F579️
  **Model controls.** Anyone who can edit a model can now add named controls to it
  in the…"
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1370
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 1555540d404831e2b7cd26f0ee5477ad69c494783320a53a45a9bf878674f64b
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-10-10-5c62e0
  comparison: ''
  date: '2026-10-10'
  description: 'Open WebUI — v0.12.0: 49 Model Support changes'
  evidence:
  - quote: "\U0001F579️ **Model controls.** Anyone who can edit a model can now add
      named controls to it in the model editor, such as a Thinking control whose Low,
      Medium and High options each set the reasoning effort, where every option can
      carry its own custom parameters and one can be marked as the default, shown
      either as a menu or as a slider that runs from the first option to the last;
      people with the Allow Chat Controls and Allow Chat Params permissions then pick
      an option from a knobs button next to the model selector in the chat input,
      their choice is remembered for that model, and the names of controls and options
      can be translated for each language in the editor. Controls cannot be set on
      pipe, direct connection or arena models and are not applied to automation runs.
      [Commit](https://github.com/open-webui/open-webui/commit/106aae70e9ad1a3356762779d72673b7dc1293a7),
      [Commit](https://github.com/open-webui/open-webui/commit/e9cca320b40025a892436a9791902af85a426ad3),
      [Commit](https://github.com/open-webui/open-webui/commit/efd94fde63882818d451370a2b39edb93ba6a8f5),
      [Commit](https://github.com/open-webui/open-webui/commit/3e0e760ce30cf2b5f177b29478c0a8ec85f1d5a8),
      [Commit](https://github.com/open-webui/open-webui/commit/79d376a1f37436065d78e25be9bc342fe0724801),
      [#31972](https://github.com/open-webui/open-webui/issues/31972)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F5C4️ **Knowledge bases as a file browser.** A knowledge base now
      opens with its folders and files on the left and the selected file next to them,
      where you can switch between a preview of the original file and the text the
      model searches, edit that text in place or download the file, with search, filters
      and sorting above the list and a question before unsaved edits are dropped.
      [Commit](https://github.com/open-webui/open-webui/commit/33dd7dd224d4fc4031185a4dd589242681f24af7),
      [Commit](https://github.com/open-webui/open-webui/commit/9181381b0a67674aa37bc9f1f8dc45c8fe85fdd9),
      [Commit](https://github.com/open-webui/open-webui/commit/b130fec73c90a57e121b5e3759a03fee053c9f93),
      [Commit](https://github.com/open-webui/open-webui/commit/96ea26d09f14bb9d26864af3b0a6d382cae748a9),
      [Commit](https://github.com/open-webui/open-webui/commit/550311b21822d50ef9c6c63069408b35287b4607)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F947 **Default models per group.** Administrators can now set default
      models for a group in its settings, which its members get for new chats instead
      of the global default, with the most deeply nested group winning when several
      apply and a user's own default models still taking priority. [Commit](https://github.com/open-webui/open-webui/commit/398c37c73cee80e5b1f3e2ceb05403744aab71be)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F47B **Unavailable models in the admin Models list.** The Models
      list in Admin Settings now opens on a new Available view that leaves out base
      models no longer offered by any connection, and an Unavailable view lists those
      leftovers, while each model's menu now offers Delete for a leftover or workspace
      model and Reset for an available base model to bring its saved settings back
      to the defaults. [Commit](https://github.com/open-webui/open-webui/commit/461cc7aff9066a2e30f12fd8d67341d48a75befe),
      [Commit](https://github.com/open-webui/open-webui/commit/ffce74fd292489653f9d05d914dfb120e90abcbe),
      [#31389](https://github.com/open-webui/open-webui/issues/31389), [#32048](https://github.com/open-webui/open-webui/issues/32048),
      [#26812](https://github.com/open-webui/open-webui/issues/26812)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F9F2 **Reordering filtered model lists.** Models on the admin models
      page can now be dragged into place while a search, view or tag filter is active,
      with every model hidden by the filter keeping its position. [#30390](https://github.com/open-webui/open-webui/pull/30390),
      [#29634](https://github.com/open-webui/open-webui/issues/29634)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F4A1 **Model ID suggestions for connections.** After verifying a
      connection in the add or edit connection dialog, the model ID field suggests
      the models the server reports, leaving out ones already added. [Commit](https://github.com/open-webui/open-webui/commit/fd0749fba106db4809a2c72fc42538d249b8b519)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F392 **Skills built-in tool per model.** The Builtin Tools section
      of a model now has a Skills switch, on by default, so a model can be kept from
      finding and loading skills on its own while skills a user picks for a chat still
      apply. [Commit](https://github.com/open-webui/open-webui/commit/55e1c44c946828ab92c94934c12c4fc8aa7568fd)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F3C1 **Finish reason for outlet filters.** Outlet filters now get
      the reason the model stopped, such as reaching the token limit or stopping to
      call a tool, on the finished reply of OpenAI-compatible and Ollama models, so
      they no longer have to read every streamed chunk to find out, and Ollama replies
      cut off by the token limit now report length instead of stop. [#32079](https://github.com/open-webui/open-webui/pull/32079)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F4C2 **Folder default model set in the folder settings.** A folder's
      default model for new chats is now chosen in the folder's settings, and switching
      the model inside a chat in that folder no longer changes the folder's default.
      [Commit](https://github.com/open-webui/open-webui/commit/a3a2e42ee00a70d6c646735345e6b771bcd2a70d),
      [Commit](https://github.com/open-webui/open-webui/commit/8f4f29d8345196e3221c85ecff0411fbd7e371af)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: ⏲️ **Failed timers show their error.** A timer that fails before the model
      starts answering, for example because its model was removed, now shows the error
      in its reply, where the chat kept a blank reply that looked stuck. [#31483](https://github.com/open-webui/open-webui/pull/31483),
      [#31481](https://github.com/open-webui/open-webui/issues/31481)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: ✅ **Approving several tool calls at once.** With tool approval set to ask,
      every tool the model calls in one turn now gets its own approval card in turn,
      where only the first did and the others stayed on "Executing..." forever. [#31315](https://github.com/open-webui/open-webui/pull/31315),
      [#29293](https://github.com/open-webui/open-webui/issues/29293)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F501 **Approved tool results kept.** With tool approval set to ask,
      the result of an approved tool call now stays in the chat once the reply finishes,
      so the model still sees it in later turns and a second tool call no longer sends
      the first back to waiting for approval and runs it again. [#31502](https://github.com/open-webui/open-webui/pull/31502)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F9E0 **Ollama system prompt after tool calls.** With native function
      calling on an Ollama model, the model's system prompt now stays in place after
      a tool result, so the final answer follows the model's instructions again. [#30375](https://github.com/open-webui/open-webui/pull/30375),
      [#30161](https://github.com/open-webui/open-webui/issues/30161)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F9F0 **Chats recover from broken tool history.** A chat where a
      tool call was saved without its result, or a result without its call, no longer
      fails on every following message with Anthropic and Bedrock models, because
      such unmatched pieces are now left out of what is sent to the model. [#31431](https://github.com/open-webui/open-webui/pull/31431),
      [#28937](https://github.com/open-webui/open-webui/issues/28937)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F521 **Missing space after thinking.** Reasoning model answers no
      longer lose a space right after the thinking block, where \"The answer is 4.\"
      could be shown and saved as \"The answeris 4.\". [#31438](https://github.com/open-webui/open-webui/pull/31438),
      [#31435](https://github.com/open-webui/open-webui/issues/31435)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F3C1 **Stray end of solution marker.** Replies from models that
      wrap their answer in solution markers no longer show the closing marker, and
      text written after it appears as a normal part of the reply. [#31436](https://github.com/open-webui/open-webui/pull/31436),
      [#31434](https://github.com/open-webui/open-webui/issues/31434)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F52D **Thinking indicator after tool calls.** A group of collapsed
      steps in a reply now shows \"Exploring\" with a spinner while the model is still
      thinking inside it, such as after a tool call, where it already read \"Explored\"
      and the chat looked stuck. [Commit](https://github.com/open-webui/open-webui/commit/19957bc19b769388a61bc9ebd7322deb006ddd62),
      [#29531](https://github.com/open-webui/open-webui/issues/29531)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F4CF **Output limit for Ollama through the API.** A \"max_tokens\"
      value sent through the API to an Ollama model now limits the reply length and
      overrides the value saved in the model's advanced parameters, where Ollama ignored
      it and replies ran to full length. [#31437](https://github.com/open-webui/open-webui/pull/31437),
      [#31432](https://github.com/open-webui/open-webui/issues/31432)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F4F1 **Composer buttons at larger UI scale.** On phones with UI
      Scale at 1.2x or more, the + and Integrations buttons in the message input stay
      visible and tappable, with the model name shortened to make room. [#30374](https://github.com/open-webui/open-webui/pull/30374),
      [#29989](https://github.com/open-webui/open-webui/issues/29989)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F4AF **Relevance scores on knowledge tool citations.** Citations
      from knowledge and chat file searches made by the model through native function
      calling now show their relevance percentage, as the same sources already did
      with classic retrieval. [#31307](https://github.com/open-webui/open-webui/pull/31307),
      [#29776](https://github.com/open-webui/open-webui/issues/29776)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: ☁️ **Long non-Latin S3 file names.** Files stored on S3 with long names
      in scripts such as Cyrillic are now read correctly, so their content reaches
      the model instead of failing with "File name too long". [#30418](https://github.com/open-webui/open-webui/pull/30418),
      [#30409](https://github.com/open-webui/open-webui/issues/30409)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F4C8 **Leaderboard chart for slashed model IDs.** The leaderboard
      activity chart now shows data for models whose ID contains a slash, such as
      Hugging Face models served through Ollama. [#30456](https://github.com/open-webui/open-webui/pull/30456),
      [#30455](https://github.com/open-webui/open-webui/issues/30455)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F3DF️ **Arena models after editing.** Editing an arena model in
      the admin models page, for example to set its tools, no longer removes its access
      settings and model pool, where non-admin users lost the arena model and its
      chats ignored the configured models. [#31309](https://github.com/open-webui/open-webui/pull/31309),
      [#29564](https://github.com/open-webui/open-webui/issues/29564)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F503 **Model sync API on SQLite.** Syncing models through the API
      on a default SQLite setup now saves changes to existing models, where the request
      stalled and returned an empty list with \"database is locked\" in the log. [#31349](https://github.com/open-webui/open-webui/pull/31349),
      [#31346](https://github.com/open-webui/open-webui/issues/31346)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F4CA **Scrollable admin analytics.** The analytics tab in the admin
      settings now scrolls, so the full model and user ranking tables can be reached
      where their lower rows were cut off. [#30429](https://github.com/open-webui/open-webui/pull/30429),
      [#30428](https://github.com/open-webui/open-webui/issues/30428)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F9EE **jina-colbert-v2 reranker.** The jinaai/jina-colbert-v2 reranking
      model loads again on the current transformers release, and saving the Documents
      settings no longer quietly turns hybrid search off with it. [#31532](https://github.com/open-webui/open-webui/pull/31532),
      [#31522](https://github.com/open-webui/open-webui/issues/31522)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F5BC️ **Pasted images in notes.** Images pasted into a note now
      stay when the note is cut and pasted, edited from its Chat panel or edited by
      a model, where they disappeared. [#31513](https://github.com/open-webui/open-webui/pull/31513),
      [#31512](https://github.com/open-webui/open-webui/issues/31512)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: ⏏️ **Ejecting models over HTTPS.** Ejecting a model from the model selector
      on llama.cpp and Ollama connections served with a self-signed or internal certificate
      now follows "AIOHTTP_CLIENT_SESSION_SSL", where it failed with a certificate
      error. [#31391](https://github.com/open-webui/open-webui/pull/31391), [#31371](https://github.com/open-webui/open-webui/issues/31371)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001FAA8 **OpenAI models on Amazon Bedrock.** GPT-5.6 and GPT-6 models
      on an Amazon Bedrock OpenAI-compatible connection, with ids such as us.openai.gpt-6-sol,
      now receive their token limit as max_completion_tokens, where Bedrock rejected
      every request with a token limit, including title and emoji generation. [#30976](https://github.com/open-webui/open-webui/pull/30976),
      [#30510](https://github.com/open-webui/open-webui/issues/30510)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001FA84 **Artifact preview stays open.** The artifact preview no longer
      closes right after opening on its own, which happened now and then in any chat
      and every time a filter function wrote part of the reply before the model answered.
      [#31653](https://github.com/open-webui/open-webui/pull/31653), [#31652](https://github.com/open-webui/open-webui/pull/31652),
      [#31643](https://github.com/open-webui/open-webui/issues/31643)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F004 **Chinese punctuation in uploaded files.** Text extracted from
      uploaded files now keeps full-width punctuation such as ：（），！？ and curly quotes
      as written, where they were turned into their ASCII forms in the file preview
      and in what the model saw; files uploaded earlier keep the altered text until
      they are uploaded again. [#31655](https://github.com/open-webui/open-webui/pull/31655),
      [#17087](https://github.com/open-webui/open-webui/issues/17087)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F4B8 **Prompt caching across consecutive tool calls.** When a model
      calls one tool after another with no text in between, the earlier messages now
      stay identical from one request to the next, so the provider's prompt cache
      keeps matching instead of missing for the rest of the chat. [#31593](https://github.com/open-webui/open-webui/pull/31593),
      [#31588](https://github.com/open-webui/open-webui/issues/31588)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F198 **Custom model fallback in the web UI.** With \"ENABLE_CUSTOM_MODEL_FALLBACK\"
      on, chats sent from the web UI with a workspace model whose base model is gone
      are now answered by the first default model, where they failed with \"Model
      not found\". [#31353](https://github.com/open-webui/open-webui/pull/31353),
      [#31345](https://github.com/open-webui/open-webui/issues/31345)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F6A6 **Provider errors reach API clients.** API requests that fail
      at the model provider, such as on a rate limit, now return the provider's own
      status code, error message and Retry-After header, where they came back as a
      generic 400 or an empty 200 without the header, and a provider error sent as
      plain text is now shown as written. [Commit](https://github.com/open-webui/open-webui/commit/015dbc8619568ac077ec1d782661836a63691ba1),
      [#31326](https://github.com/open-webui/open-webui/issues/31326), [#28938](https://github.com/open-webui/open-webui/issues/28938)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: ⏹️ **Cancelled Ollama downloads keep existing models.** Cancelling an Ollama
      model download in Manage Ollama or the model selector no longer deletes the
      model, which removed an existing copy on the target server or the same model
      on another Ollama connection. [#31824](https://github.com/open-webui/open-webui/pull/31824),
      [#31823](https://github.com/open-webui/open-webui/issues/31823)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F9CA **Chats with tool calls reopen on some Responses API providers.**
      Reopening a chat where the model wrote text, called a tool and then answered
      no longer freezes the browser tab with providers that reuse output item ids
      in every response, such as OpenVINO Model Server, including chats saved before
      this fix. [#31838](https://github.com/open-webui/open-webui/pull/31838), [#31837](https://github.com/open-webui/open-webui/issues/31837)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F3C5 **Private arena models for admins.** Arena models left private
      with no access grants are now visible to administrators in the model selector,
      can be chatted with and show their profile image, even with the admin access
      bypass turned off, where they disappeared for everyone. [#31858](https://github.com/open-webui/open-webui/pull/31858),
      [#30013](https://github.com/open-webui/open-webui/issues/30013)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F999 **GGUF uploads to Ollama create the model.** Uploading a GGUF
      file in Manage Ollama now creates the model in both File Mode and URL Mode,
      named after the file, where the file reached Ollama but no model appeared; the
      Modelfile Content box was removed, as Ollama reads the template and stop sequences
      from the GGUF file. [#31862](https://github.com/open-webui/open-webui/pull/31862),
      [#31861](https://github.com/open-webui/open-webui/issues/31861)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F4F4 **Model list after unloading a model.** Unloading a model from
      Ollama or llama.cpp now refreshes the model list right away, so it no longer
      shows the model as loaded until the list is refreshed later. [#31921](https://github.com/open-webui/open-webui/issues/31921),
      [Commit](https://github.com/open-webui/open-webui/commit/cf5755f9498d642557c1039eb3acf19bdb09b399)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F9F7 **Tool calls with reused ids.** With providers that number
      tool calls from zero again each time the model calls tools within one reply,
      such as Kimi K3 on OpenRouter, each call now keeps its own arguments and result,
      where later calls overwrote earlier ones in the saved chat and the model got
      earlier results next to the wrong arguments. [#31887](https://github.com/open-webui/open-webui/pull/31887),
      [#28305](https://github.com/open-webui/open-webui/issues/28305)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F46F **Earlier tool calls sent twice after a paused reply.** After
      answering a question from the Ask User tool or pressing Continue, later tool
      rounds no longer send everything from before the pause to the model a second
      time, which made providers that reject repeated tool calls, like DeepSeek, stop
      the chat with a \"Duplicate 'call_id'\" error. [#32029](https://github.com/open-webui/open-webui/pull/32029),
      [#31991](https://github.com/open-webui/open-webui/issues/31991)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F305 **Model images saved as files.** JPEG and WebP images returned
      by a model are now saved as files with only a link kept in the chat, the same
      way PNG images already were, instead of being stored as raw data inside the
      chat and making it larger by the size of each image. [#31975](https://github.com/open-webui/open-webui/pull/31975),
      [#31916](https://github.com/open-webui/open-webui/issues/31916)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F464 **Workspace lists after quick searches.** The Models, Prompts,
      Knowledge and Skills workspace lists no longer show results from an earlier
      search or filter that answered late, which could put other people's items under
      Created by you. [Commit](https://github.com/open-webui/open-webui/commit/4b9d31b390886454ae22b2f8cb020ff2400d5124),
      [#31965](https://github.com/open-webui/open-webui/issues/31965)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F587️ **Files attached to shared notes.** People a note is shared
      with can now open its attached files and have them used in the note's chat,
      where they were refused and the model answered without them. [Commit](https://github.com/open-webui/open-webui/commit/b612c8847ad186dbfe8f745f81f0d97286ea7919),
      [#32011](https://github.com/open-webui/open-webui/issues/32011)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F6A6 **Filters before approved tool calls.** After you approve a
      tool call, request filters now check the request before the tool runs, where
      the tool ran first and a filter rejecting the request came only after its effects,
      and the follow-up request now uses the same prepared history as any other message
      instead of one rebuilt from the saved chat, which dropped the extracted content
      of attached files and left the model only their names. [Commit](https://github.com/open-webui/open-webui/commit/639139aa7a69a78a758f2075d42d4d5e1554cf57),
      [#31986](https://github.com/open-webui/open-webui/issues/31986)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F39E️ **Images streamed by a model saved once.** When a model streams
      its images in separate pieces, each image is now kept once, where every new
      piece saved all earlier images again, so four images could end up stored as
      fifteen with duplicates in the chat. [#32054](https://github.com/open-webui/open-webui/pull/32054),
      [#32053](https://github.com/open-webui/open-webui/issues/32053)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F6F0️ **User info headers for rerankers.** With \"ENABLE_FORWARD_USER_INFO_HEADERS\"
      on and hybrid search enabled, rerank requests now carry the signed-in user's
      headers when a chat searches attached knowledge, when a model uses the built-in
      knowledge search tool and when the collection query API runs, where only the
      embedding requests of the same search had them. [#32061](https://github.com/open-webui/open-webui/pull/32061),
      [#32060](https://github.com/open-webui/open-webui/issues/32060)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F9EF **Non-streamed replies with tool calls finish.** With Stream
      Chat Response turned off, a reply in which the model calls a tool is now saved
      and marked as finished, where the chat kept showing it as still generating until
      the page was reloaded. [#32083](https://github.com/open-webui/open-webui/pull/32083)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  - quote: "\U0001F4AD **Answers that mention a thinking tag.** When a model sends
      its reasoning separately, such as through Ollama, an answer that contains the
      text \"<think>\" is no longer cut off there with the rest hidden in a second
      thinking block. [Commit](https://github.com/open-webui/open-webui/commit/236965c7e9238bb98630d940fa83666fd323d6e9),
      [#31540](https://github.com/open-webui/open-webui/issues/31540)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 49-model-support-changes-in-v0-12-0
  source_release: open-webui-2026-10-10-v0-12-0-github-409209575-f076e92b
  source_type: github_releases
  theme: model-support
  title: 49 Model Support changes in v0.12.0
  type: change
related_changes:
- '[[Changes/Ollama/2026-10-08-4-model-support-changes-in-v0-40-2|4 Model Support
  changes in v0.40.2]]'
- '[[Changes/OpenHands/2026-10-08-test-e2e-launch-the-same-model-profile-test-from-the-beta-profile-by-enyst-in-ht|test(e2e):
  launch the same-model profile test from the BETA profile]]'
- '[[Changes/Claude Code/2026-10-09-claude-tag-changed-claude-in-slack-to-show-the-footer-with-the-session-link-mode|Claude
  Tag Changed Claude in Slack to show the footer with the session link, model…]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-10-10-v0-12-0-github-409209575-f076e92b|open-webui-2026-10-10-v0-12-0-github-409209575-f076e92b]]'
source_type: github_releases
theme: model-support
title: 49 Model Support changes in v0.12.0
type: change
---

<!-- chronolog:begin region="header" -->
# 49 Model Support changes in v0.12.0

**Open WebUI** · 2026-10-10 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.12.0) · from [[Releases/Open WebUI/open-webui-2026-10-10-v0-12-0-github-409209575-f076e92b|v0.12.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🕹️ **Model controls.** Anyone who can edit a model can now add named controls to it in the model editor, such as a Thinking control whose Low, Medium and High options each set the reasoning effort, where every option can carry its own custom parameters and one can be marked as the default, shown either as a menu or as a slider that runs from the first option to the last; people with the Allow Chat Controls and Allow Chat Params permissions then pick an option from a knobs button next to the model selector in the chat input, their choice is remembered for that model, and the names of controls and options can be translated for each language in the editor. Controls cannot be set on pipe, direct connection or arena models and are not applied to automation runs. [Commit](https://github.com/open-webui/open-webui/commit/106aae70e9ad1a3356762779d72673b7dc1293a7), [Commit](https://github.com/open-webui/open-webui/commit/e9cca320b40025a892436a9791902af85a426ad3), [Commit](https://github.com/open-webui/open-webui/commit/efd94fde63882818d451370a2b39edb93ba6a8f5), [Commit](https://github.com/open-webui/open-webui/commit/3e0e760ce30cf2b5f177b29478c0a8ec85f1d5a8), [Commit](https://github.com/open-webui/open-webui/commit/79d376a1f37436065d78e25be9bc342fe0724801), [#31972](https://github.com/open-webui/open-webui/issues/31972)

> 🗄️ **Knowledge bases as a file browser.** A knowledge base now opens with its folders and files on the left and the selected file next to them, where you can switch between a preview of the original file and the text the model searches, edit that text in place or download the file, with search, filters and sorting above the list and a question before unsaved edits are dropped. [Commit](https://github.com/open-webui/open-webui/commit/33dd7dd224d4fc4031185a4dd589242681f24af7), [Commit](https://github.com/open-webui/open-webui/commit/9181381b0a67674aa37bc9f1f8dc45c8fe85fdd9), [Commit](https://github.com/open-webui/open-webui/commit/b130fec73c90a57e121b5e3759a03fee053c9f93), [Commit](https://github.com/open-webui/open-webui/commit/96ea26d09f14bb9d26864af3b0a6d382cae748a9), [Commit](https://github.com/open-webui/open-webui/commit/550311b21822d50ef9c6c63069408b35287b4607)

> 🥇 **Default models per group.** Administrators can now set default models for a group in its settings, which its members get for new chats instead of the global default, with the most deeply nested group winning when several apply and a user's own default models still taking priority. [Commit](https://github.com/open-webui/open-webui/commit/398c37c73cee80e5b1f3e2ceb05403744aab71be)

> 👻 **Unavailable models in the admin Models list.** The Models list in Admin Settings now opens on a new Available view that leaves out base models no longer offered by any connection, and an Unavailable view lists those leftovers, while each model's menu now offers Delete for a leftover or workspace model and Reset for an available base model to bring its saved settings back to the defaults. [Commit](https://github.com/open-webui/open-webui/commit/461cc7aff9066a2e30f12fd8d67341d48a75befe), [Commit](https://github.com/open-webui/open-webui/commit/ffce74fd292489653f9d05d914dfb120e90abcbe), [#31389](https://github.com/open-webui/open-webui/issues/31389), [#32048](https://github.com/open-webui/open-webui/issues/32048), [#26812](https://github.com/open-webui/open-webui/issues/26812)

> 🧲 **Reordering filtered model lists.** Models on the admin models page can now be dragged into place while a search, view or tag filter is active, with every model hidden by the filter keeping its position. [#30390](https://github.com/open-webui/open-webui/pull/30390), [#29634](https://github.com/open-webui/open-webui/issues/29634)

> 💡 **Model ID suggestions for connections.** After verifying a connection in the add or edit connection dialog, the model ID field suggests the models the server reports, leaving out ones already added. [Commit](https://github.com/open-webui/open-webui/commit/fd0749fba106db4809a2c72fc42538d249b8b519)

> 🎒 **Skills built-in tool per model.** The Builtin Tools section of a model now has a Skills switch, on by default, so a model can be kept from finding and loading skills on its own while skills a user picks for a chat still apply. [Commit](https://github.com/open-webui/open-webui/commit/55e1c44c946828ab92c94934c12c4fc8aa7568fd)

> 🏁 **Finish reason for outlet filters.** Outlet filters now get the reason the model stopped, such as reaching the token limit or stopping to call a tool, on the finished reply of OpenAI-compatible and Ollama models, so they no longer have to read every streamed chunk to find out, and Ollama replies cut off by the token limit now report length instead of stop. [#32079](https://github.com/open-webui/open-webui/pull/32079)

> 📂 **Folder default model set in the folder settings.** A folder's default model for new chats is now chosen in the folder's settings, and switching the model inside a chat in that folder no longer changes the folder's default. [Commit](https://github.com/open-webui/open-webui/commit/a3a2e42ee00a70d6c646735345e6b771bcd2a70d), [Commit](https://github.com/open-webui/open-webui/commit/8f4f29d8345196e3221c85ecff0411fbd7e371af)

> ⏲️ **Failed timers show their error.** A timer that fails before the model starts answering, for example because its model was removed, now shows the error in its reply, where the chat kept a blank reply that looked stuck. [#31483](https://github.com/open-webui/open-webui/pull/31483), [#31481](https://github.com/open-webui/open-webui/issues/31481)

> ✅ **Approving several tool calls at once.** With tool approval set to ask, every tool the model calls in one turn now gets its own approval card in turn, where only the first did and the others stayed on "Executing..." forever. [#31315](https://github.com/open-webui/open-webui/pull/31315), [#29293](https://github.com/open-webui/open-webui/issues/29293)

> 🔁 **Approved tool results kept.** With tool approval set to ask, the result of an approved tool call now stays in the chat once the reply finishes, so the model still sees it in later turns and a second tool call no longer sends the first back to waiting for approval and runs it again. [#31502](https://github.com/open-webui/open-webui/pull/31502)

> 🧠 **Ollama system prompt after tool calls.** With native function calling on an Ollama model, the model's system prompt now stays in place after a tool result, so the final answer follows the model's instructions again. [#30375](https://github.com/open-webui/open-webui/pull/30375), [#30161](https://github.com/open-webui/open-webui/issues/30161)

> 🧰 **Chats recover from broken tool history.** A chat where a tool call was saved without its result, or a result without its call, no longer fails on every following message with Anthropic and Bedrock models, because such unmatched pieces are now left out of what is sent to the model. [#31431](https://github.com/open-webui/open-webui/pull/31431), [#28937](https://github.com/open-webui/open-webui/issues/28937)

> 🔡 **Missing space after thinking.** Reasoning model answers no longer lose a space right after the thinking block, where "The answer is 4." could be shown and saved as "The answeris 4.". [#31438](https://github.com/open-webui/open-webui/pull/31438), [#31435](https://github.com/open-webui/open-webui/issues/31435)

> 🏁 **Stray end of solution marker.** Replies from models that wrap their answer in solution markers no longer show the closing marker, and text written after it appears as a normal part of the reply. [#31436](https://github.com/open-webui/open-webui/pull/31436), [#31434](https://github.com/open-webui/open-webui/issues/31434)

> 🔭 **Thinking indicator after tool calls.** A group of collapsed steps in a reply now shows "Exploring" with a spinner while the model is still thinking inside it, such as after a tool call, where it already read "Explored" and the chat looked stuck. [Commit](https://github.com/open-webui/open-webui/commit/19957bc19b769388a61bc9ebd7322deb006ddd62), [#29531](https://github.com/open-webui/open-webui/issues/29531)

> 📏 **Output limit for Ollama through the API.** A "max_tokens" value sent through the API to an Ollama model now limits the reply length and overrides the value saved in the model's advanced parameters, where Ollama ignored it and replies ran to full length. [#31437](https://github.com/open-webui/open-webui/pull/31437), [#31432](https://github.com/open-webui/open-webui/issues/31432)

> 📱 **Composer buttons at larger UI scale.** On phones with UI Scale at 1.2x or more, the + and Integrations buttons in the message input stay visible and tappable, with the model name shortened to make room. [#30374](https://github.com/open-webui/open-webui/pull/30374), [#29989](https://github.com/open-webui/open-webui/issues/29989)

> 💯 **Relevance scores on knowledge tool citations.** Citations from knowledge and chat file searches made by the model through native function calling now show their relevance percentage, as the same sources already did with classic retrieval. [#31307](https://github.com/open-webui/open-webui/pull/31307), [#29776](https://github.com/open-webui/open-webui/issues/29776)

> ☁️ **Long non-Latin S3 file names.** Files stored on S3 with long names in scripts such as Cyrillic are now read correctly, so their content reaches the model instead of failing with "File name too long". [#30418](https://github.com/open-webui/open-webui/pull/30418), [#30409](https://github.com/open-webui/open-webui/issues/30409)

> 📈 **Leaderboard chart for slashed model IDs.** The leaderboard activity chart now shows data for models whose ID contains a slash, such as Hugging Face models served through Ollama. [#30456](https://github.com/open-webui/open-webui/pull/30456), [#30455](https://github.com/open-webui/open-webui/issues/30455)

> 🏟️ **Arena models after editing.** Editing an arena model in the admin models page, for example to set its tools, no longer removes its access settings and model pool, where non-admin users lost the arena model and its chats ignored the configured models. [#31309](https://github.com/open-webui/open-webui/pull/31309), [#29564](https://github.com/open-webui/open-webui/issues/29564)

> 🔃 **Model sync API on SQLite.** Syncing models through the API on a default SQLite setup now saves changes to existing models, where the request stalled and returned an empty list with "database is locked" in the log. [#31349](https://github.com/open-webui/open-webui/pull/31349), [#31346](https://github.com/open-webui/open-webui/issues/31346)

> 📊 **Scrollable admin analytics.** The analytics tab in the admin settings now scrolls, so the full model and user ranking tables can be reached where their lower rows were cut off. [#30429](https://github.com/open-webui/open-webui/pull/30429), [#30428](https://github.com/open-webui/open-webui/issues/30428)

> 🧮 **jina-colbert-v2 reranker.** The jinaai/jina-colbert-v2 reranking model loads again on the current transformers release, and saving the Documents settings no longer quietly turns hybrid search off with it. [#31532](https://github.com/open-webui/open-webui/pull/31532), [#31522](https://github.com/open-webui/open-webui/issues/31522)

> 🖼️ **Pasted images in notes.** Images pasted into a note now stay when the note is cut and pasted, edited from its Chat panel or edited by a model, where they disappeared. [#31513](https://github.com/open-webui/open-webui/pull/31513), [#31512](https://github.com/open-webui/open-webui/issues/31512)

> ⏏️ **Ejecting models over HTTPS.** Ejecting a model from the model selector on llama.cpp and Ollama connections served with a self-signed or internal certificate now follows "AIOHTTP_CLIENT_SESSION_SSL", where it failed with a certificate error. [#31391](https://github.com/open-webui/open-webui/pull/31391), [#31371](https://github.com/open-webui/open-webui/issues/31371)

> 🪨 **OpenAI models on Amazon Bedrock.** GPT-5.6 and GPT-6 models on an Amazon Bedrock OpenAI-compatible connection, with ids such as us.openai.gpt-6-sol, now receive their token limit as max_completion_tokens, where Bedrock rejected every request with a token limit, including title and emoji generation. [#30976](https://github.com/open-webui/open-webui/pull/30976), [#30510](https://github.com/open-webui/open-webui/issues/30510)

> 🪄 **Artifact preview stays open.** The artifact preview no longer closes right after opening on its own, which happened now and then in any chat and every time a filter function wrote part of the reply before the model answered. [#31653](https://github.com/open-webui/open-webui/pull/31653), [#31652](https://github.com/open-webui/open-webui/pull/31652), [#31643](https://github.com/open-webui/open-webui/issues/31643)

> 🀄 **Chinese punctuation in uploaded files.** Text extracted from uploaded files now keeps full-width punctuation such as ：（），！？ and curly quotes as written, where they were turned into their ASCII forms in the file preview and in what the model saw; files uploaded earlier keep the altered text until they are uploaded again. [#31655](https://github.com/open-webui/open-webui/pull/31655), [#17087](https://github.com/open-webui/open-webui/issues/17087)

> 💸 **Prompt caching across consecutive tool calls.** When a model calls one tool after another with no text in between, the earlier messages now stay identical from one request to the next, so the provider's prompt cache keeps matching instead of missing for the rest of the chat. [#31593](https://github.com/open-webui/open-webui/pull/31593), [#31588](https://github.com/open-webui/open-webui/issues/31588)

> 🆘 **Custom model fallback in the web UI.** With "ENABLE_CUSTOM_MODEL_FALLBACK" on, chats sent from the web UI with a workspace model whose base model is gone are now answered by the first default model, where they failed with "Model not found". [#31353](https://github.com/open-webui/open-webui/pull/31353), [#31345](https://github.com/open-webui/open-webui/issues/31345)

> 🚦 **Provider errors reach API clients.** API requests that fail at the model provider, such as on a rate limit, now return the provider's own status code, error message and Retry-After header, where they came back as a generic 400 or an empty 200 without the header, and a provider error sent as plain text is now shown as written. [Commit](https://github.com/open-webui/open-webui/commit/015dbc8619568ac077ec1d782661836a63691ba1), [#31326](https://github.com/open-webui/open-webui/issues/31326), [#28938](https://github.com/open-webui/open-webui/issues/28938)

> ⏹️ **Cancelled Ollama downloads keep existing models.** Cancelling an Ollama model download in Manage Ollama or the model selector no longer deletes the model, which removed an existing copy on the target server or the same model on another Ollama connection. [#31824](https://github.com/open-webui/open-webui/pull/31824), [#31823](https://github.com/open-webui/open-webui/issues/31823)

> 🧊 **Chats with tool calls reopen on some Responses API providers.** Reopening a chat where the model wrote text, called a tool and then answered no longer freezes the browser tab with providers that reuse output item ids in every response, such as OpenVINO Model Server, including chats saved before this fix. [#31838](https://github.com/open-webui/open-webui/pull/31838), [#31837](https://github.com/open-webui/open-webui/issues/31837)

> 🏅 **Private arena models for admins.** Arena models left private with no access grants are now visible to administrators in the model selector, can be chatted with and show their profile image, even with the admin access bypass turned off, where they disappeared for everyone. [#31858](https://github.com/open-webui/open-webui/pull/31858), [#30013](https://github.com/open-webui/open-webui/issues/30013)

> 🦙 **GGUF uploads to Ollama create the model.** Uploading a GGUF file in Manage Ollama now creates the model in both File Mode and URL Mode, named after the file, where the file reached Ollama but no model appeared; the Modelfile Content box was removed, as Ollama reads the template and stop sequences from the GGUF file. [#31862](https://github.com/open-webui/open-webui/pull/31862), [#31861](https://github.com/open-webui/open-webui/issues/31861)

> 📴 **Model list after unloading a model.** Unloading a model from Ollama or llama.cpp now refreshes the model list right away, so it no longer shows the model as loaded until the list is refreshed later. [#31921](https://github.com/open-webui/open-webui/issues/31921), [Commit](https://github.com/open-webui/open-webui/commit/cf5755f9498d642557c1039eb3acf19bdb09b399)

> 🧷 **Tool calls with reused ids.** With providers that number tool calls from zero again each time the model calls tools within one reply, such as Kimi K3 on OpenRouter, each call now keeps its own arguments and result, where later calls overwrote earlier ones in the saved chat and the model got earlier results next to the wrong arguments. [#31887](https://github.com/open-webui/open-webui/pull/31887), [#28305](https://github.com/open-webui/open-webui/issues/28305)

> 👯 **Earlier tool calls sent twice after a paused reply.** After answering a question from the Ask User tool or pressing Continue, later tool rounds no longer send everything from before the pause to the model a second time, which made providers that reject repeated tool calls, like DeepSeek, stop the chat with a "Duplicate 'call_id'" error. [#32029](https://github.com/open-webui/open-webui/pull/32029), [#31991](https://github.com/open-webui/open-webui/issues/31991)

> 🌅 **Model images saved as files.** JPEG and WebP images returned by a model are now saved as files with only a link kept in the chat, the same way PNG images already were, instead of being stored as raw data inside the chat and making it larger by the size of each image. [#31975](https://github.com/open-webui/open-webui/pull/31975), [#31916](https://github.com/open-webui/open-webui/issues/31916)

> 👤 **Workspace lists after quick searches.** The Models, Prompts, Knowledge and Skills workspace lists no longer show results from an earlier search or filter that answered late, which could put other people's items under Created by you. [Commit](https://github.com/open-webui/open-webui/commit/4b9d31b390886454ae22b2f8cb020ff2400d5124), [#31965](https://github.com/open-webui/open-webui/issues/31965)

> 🖇️ **Files attached to shared notes.** People a note is shared with can now open its attached files and have them used in the note's chat, where they were refused and the model answered without them. [Commit](https://github.com/open-webui/open-webui/commit/b612c8847ad186dbfe8f745f81f0d97286ea7919), [#32011](https://github.com/open-webui/open-webui/issues/32011)

> 🚦 **Filters before approved tool calls.** After you approve a tool call, request filters now check the request before the tool runs, where the tool ran first and a filter rejecting the request came only after its effects, and the follow-up request now uses the same prepared history as any other message instead of one rebuilt from the saved chat, which dropped the extracted content of attached files and left the model only their names. [Commit](https://github.com/open-webui/open-webui/commit/639139aa7a69a78a758f2075d42d4d5e1554cf57), [#31986](https://github.com/open-webui/open-webui/issues/31986)

> 🎞️ **Images streamed by a model saved once.** When a model streams its images in separate pieces, each image is now kept once, where every new piece saved all earlier images again, so four images could end up stored as fifteen with duplicates in the chat. [#32054](https://github.com/open-webui/open-webui/pull/32054), [#32053](https://github.com/open-webui/open-webui/issues/32053)

> 🛰️ **User info headers for rerankers.** With "ENABLE_FORWARD_USER_INFO_HEADERS" on and hybrid search enabled, rerank requests now carry the signed-in user's headers when a chat searches attached knowledge, when a model uses the built-in knowledge search tool and when the collection query API runs, where only the embedding requests of the same search had them. [#32061](https://github.com/open-webui/open-webui/pull/32061), [#32060](https://github.com/open-webui/open-webui/issues/32060)

> 🧯 **Non-streamed replies with tool calls finish.** With Stream Chat Response turned off, a reply in which the model calls a tool is now saved and marked as finished, where the chat kept showing it as still generating until the page was reloaded. [#32083](https://github.com/open-webui/open-webui/pull/32083)

> 💭 **Answers that mention a thinking tag.** When a model sends its reasoning separately, such as through Ollama, an answer that contains the text "\<think>" is no longer cut off there with the rest hidden in a second thinking block. [Commit](https://github.com/open-webui/open-webui/commit/236965c7e9238bb98630d940fa83666fd323d6e9), [#31540](https://github.com/open-webui/open-webui/issues/31540)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.12.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-10-10-5-reliability-and-performance-changes-in-v0-12-0|5 Reliability and Performance changes in v0.12.0]] · Reliability and Performance
- [[Changes/Open WebUI/2026-10-10-5-enterprise-and-administration-changes-in-v0-12-0|5 Enterprise and Administration changes in v0.12.0]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-10-10-7-apps-and-integrations-changes-in-v0-12-0|7 Apps and Integrations changes in v0.12.0]] · Apps and Integrations
- [[Changes/Open WebUI/2026-10-10-12-voice-and-audio-changes-in-v0-12-0|12 Voice and Audio changes in v0.12.0]] · Voice and Audio
- [[Changes/Open WebUI/2026-10-10-27-developer-workflow-changes-in-v0-12-0|27 Developer Workflow changes in v0.12.0]] · Developer Workflow
- [[Changes/Open WebUI/2026-10-10-5-image-generation-changes-in-v0-12-0|5 Image Generation changes in v0.12.0]] · Image Generation
- [[Changes/Open WebUI/2026-10-10-19-account-and-access-changes-in-v0-12-0|19 Account and Access changes in v0.12.0]] · Account and Access
- [[Changes/Open WebUI/2026-10-10-10-automation-and-scheduling-changes-in-v0-12-0|10 Automation and Scheduling changes in v0.12.0]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-10-10-3-mobile-and-desktop-changes-in-v0-12-0|3 Mobile and Desktop changes in v0.12.0]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-10-10-6-files-and-data-changes-in-v0-12-0|6 Files and Data changes in v0.12.0]] · Files and Data
- [[Changes/Open WebUI/2026-10-10-13-collaboration-changes-in-v0-12-0|13 Collaboration changes in v0.12.0]] · Collaboration
- [[Changes/Open WebUI/2026-10-10-2-memory-and-personalization-changes-in-v0-12-0|2 Memory and Personalization changes in v0.12.0]] · Memory and Personalization
- [[Changes/Open WebUI/2026-10-10-5-context-window-changes-in-v0-12-0|5 Context Window changes in v0.12.0]] · Context Window
- [[Changes/Open WebUI/2026-10-10-18-interface-experience-changes-in-v0-12-0|18 Interface Experience changes in v0.12.0]] · Interface Experience
- [[Changes/Open WebUI/2026-10-10-7-agent-mode-changes-in-v0-12-0|7 Agent Mode changes in v0.12.0]] · Agent Mode
- [[Changes/Open WebUI/2026-10-10-6-safety-and-privacy-changes-in-v0-12-0|6 Safety and Privacy changes in v0.12.0]] · Safety and Privacy
- [[Changes/Open WebUI/2026-10-10-21-editor-experience-changes-in-v0-12-0|21 Editor Experience changes in v0.12.0]] · Editor Experience
- [[Changes/Open WebUI/2026-10-10-4-search-and-browsing-changes-in-v0-12-0|4 Search and Browsing changes in v0.12.0]] · Search and Browsing
- [[Changes/Open WebUI/2026-10-10-68-other-changes-in-v0-12-0|68 other changes in v0.12.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-10-09 · Claude Code · [[Changes/Claude Code/2026-10-09-claude-tag-changed-claude-in-slack-to-show-the-footer-with-the-session-link-mode|Claude Tag Changed Claude in Slack to show the footer with the session link, model…]]
- Later: 2026-10-12 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-10-12-2-model-support-changes-in-v1-0-96|2 Model Support changes in v1.0.96]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-10-10-5c62e0&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-10-10-49-model-support-changes-in-v0-12-0.md%0ACard%20ID%3A%20open-webui-2026-10-10-5c62e0%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.12.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->