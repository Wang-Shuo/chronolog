---
card_id: open-webui-2026-08-25-f1ebf1
date: '2026-08-25'
description: "Open WebUI · 2026-08-25 · Model Support: 56 changes in v0.11.1 — \U0001F64B♂️
  **Models that can ask you a question.** A new built-in tool lets a model pause and
  put up…"
diffusion:
  first_in_tracked: '[[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We
    made more improvements to the ChatGPT model!]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1324
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: model-support
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 29990534310ab9474ee2ed3187ad66d5b22fad5df516324be51d7004729b23a0
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-08-25-f1ebf1
  comparison: ''
  date: '2026-08-25'
  description: 'Open WebUI — v0.11.1: 56 Model Support changes'
  evidence:
  - quote: "\U0001F64B♂️ **Models that can ask you a question.** A new built-in tool
      lets a model pause and put up to three multiple-choice questions to you before
      continuing, with room to type your own answer instead, and the question survives
      a reload in a saved conversation, so you can come back and answer it later rather
      than losing the conversation. [Commit](https://github.com/open-webui/open-webui/commit/4465f52a3eb521854cf190f91b0ea7cf3fa21830),
      [Commit](https://github.com/open-webui/open-webui/commit/133549a87ee371577453d897c2db2d8071223f27),
      [Commit](https://github.com/open-webui/open-webui/commit/b018feb7419e68314378b3cdd8b7b1b389400a98),
      [Commit](https://github.com/open-webui/open-webui/commit/083e35144152d6a301bed01aa6d898db3871ddcf),
      [Commit](https://github.com/open-webui/open-webui/commit/256cce505be8ddd4930e8cb2536faea718d3f789),
      [Commit](https://github.com/open-webui/open-webui/commit/14e4d72d9a21a10196e8e6efb04180cd9104b8e6),
      [Commit](https://github.com/open-webui/open-webui/commit/57bd08304e45f707768a898de9f50894929008dd),
      [Commit](https://github.com/open-webui/open-webui/commit/d9014b3483d4c6e8d99e50395afcdc538bcf05cd)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F680 **Faster model list lookups.** Title generation, tag suggestions,
      autocomplete, and other background steps of a chat turn now fetch the model
      list in one go, which keeps other people's responses flowing on busy Redis-backed
      instances with many models. [#27821](https://github.com/open-webui/open-webui/pull/27821)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F9CA **Faster file access checks.** Checking whether you may reach
      a file no longer walks every workspace model you can see looking for it, so
      opening a folder of files, downloading one, or retrieving from one is much quicker
      on instances with many models. [#28802](https://github.com/open-webui/open-webui/pull/28802)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F68F **Faster workspace model lookups.** Working out which workspace
      models you may edit no longer loads every model on the instance and discards
      most of them, which also speeds up exporting models and the file access checks
      that relied on it. [#28795](https://github.com/open-webui/open-webui/pull/28795)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F941 **Long replies no longer slow as they grow.** A long reply
      is no longer re-examined from the beginning for reasoning and code blocks on
      every piece that arrives, so the work stops growing with the length of the reply,
      which on a long reply is around 190x less time spent on it. [#28861](https://github.com/open-webui/open-webui/pull/28861)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F9F0 **Managing models on more servers.** Administrators can now
      download, load, and unload models on llama.cpp and LM Studio connections from
      the manage models dialog, remove them on llama.cpp, and start a download straight
      from the model picker's search box, alongside the Ollama support that was already
      there. [Commit](https://github.com/open-webui/open-webui/commit/85c3d0ae2fad58ffc2b92b1733a6c8bc7ab471db),
      [Commit](https://github.com/open-webui/open-webui/commit/8260d527ee97372a207ce9bd9c6dab4909061281),
      [Commit](https://github.com/open-webui/open-webui/commit/25802c048e6123fa602182949ad2a9f349e1e863),
      [Commit](https://github.com/open-webui/open-webui/commit/31c1ffd55a018a74c7e53a35fb9f9bbe33774b6f),
      [#28766](https://github.com/open-webui/open-webui/pull/28766)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F3F7️ **Named writing blocks.** When a model wraps a draft such
      as an email in a writing block, the block is now titled with its subject and
      shows the recipient beside it, rather than every block reading simply as Writing.
      [#28280](https://github.com/open-webui/open-webui/pull/28280), [#28198](https://github.com/open-webui/open-webui/issues/28198)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F9FE **CSV shape in retrieval.** Turning on \"ENABLE_RAG_CSV_SUMMARY\"
      adds a short line naming the row count, data row count, column count, and column
      names of a CSV file to what the model sees, giving it the shape of the table
      alongside its contents. [Commit](https://github.com/open-webui/open-webui/commit/1b72899f246ba46ab8f7cd6aee2d56ef69217d82)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F4D9 **OpenDocument files in a temporary chat.** A text document,
      spreadsheet, or presentation from an office suite that uses the OpenDocument
      format now has its text read out in the browser when attached to a temporary
      chat, where the model was handed the raw archive and answered that it could
      not read the file. [Commit](https://github.com/open-webui/open-webui/commit/9e7c9360b744c878ae0c38aa1caf3886f27b07ab),
      [#28906](https://github.com/open-webui/open-webui/discussions/28906)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: ✂️ **Long replies cut off partway.** A single oversized piece of a streamed
      reply, such as a long reasoning trace or a turn carrying many tool calls, no
      longer ends the answer early with a misleading error about byte counts, which
      affected every default installation. [#28114](https://github.com/open-webui/open-webui/pull/28114),
      [#25664](https://github.com/open-webui/open-webui/issues/25664)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F9D1\U0001F4BB **Code execution reachable through a tag in a reply.**
      On installs using native function calling, the older path that runs code found
      inside a tag in the model's reply is no longer active alongside the built-in
      tool, so code execution happens only through an explicit tool call. [#29024](https://github.com/open-webui/open-webui/pull/29024)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F9EC **Workspace models shadowing a real one.** Someone without
      administrator rights can no longer create, import, or edit a workspace model
      so that it takes over the identity of a model served by a connected provider,
      where doing so would have changed what everyone else got when they picked that
      model. [Commit](https://github.com/open-webui/open-webui/commit/ea55d38793014a4e3cd5a4046816fe22e69e9739)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F50D **Listing a single connection's models.** Asking for the models
      or version of one particular connection is now restricted to administrators,
      and a request naming a specific backend is checked against the models that backend
      actually serves even where the access control bypass is turned on. [Commit](https://github.com/open-webui/open-webui/commit/16f118d77ad9d68c64116f94551ffb14bf8b2abd)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F9E9 **Chats during model list refreshes.** On direct connections,
      background work such as title and tag generation no longer fails or runs against
      a mix of old and new model entries while the model list is being refreshed.
      [#27821](https://github.com/open-webui/open-webui/pull/27821)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F6AB **Duplicate models in lists.** Adding a model that is already
      on a connection's allowed list is now rejected instead of quietly adding it
      a second time, the arena picker no longer offers models you have already chosen,
      and existing duplicates are cleaned up the next time the list is saved. [#28251](https://github.com/open-webui/open-webui/pull/28251),
      [#28249](https://github.com/open-webui/open-webui/issues/28249)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F3AF **Custom model parameters combining.** Setting a custom parameter
      on a model no longer silently discards every custom parameter defined in the
      global defaults, and a value sent directly in an API request is no longer overwritten
      by the model's saved settings. [Commit](https://github.com/open-webui/open-webui/commit/11739a2de8eddf7ef26378356aff8a1bcab4a349),
      [#28241](https://github.com/open-webui/open-webui/issues/28241)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F527 **Full tool parameter descriptions.** A tool whose parameter
      description runs over several lines now passes the whole description to the
      model instead of only its first line. [Commit](https://github.com/open-webui/open-webui/commit/b606e13da3753027ead0e92e35e1399b60c96c8e)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F39A️ **ColBERT reranker startup.** Loading a ColBERT reranker now
      names the model in the log rather than printing a logging error and a traceback
      in its place. [#27838](https://github.com/open-webui/open-webui/pull/27838)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: ↕️ **Expand button in the message box.** The button that enlarges the message
      box no longer sits on top of a tagged model's dismiss button or the first attached
      file, and stays reachable in long prompts. [#27676](https://github.com/open-webui/open-webui/pull/27676),
      [#26736](https://github.com/open-webui/open-webui/issues/26736)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001FA84 **Merged responses after a reload.** Merging the answers from
      several models now works on a conversation you have reopened, instead of the
      merging model reporting that the other responses were empty. [#27673](https://github.com/open-webui/open-webui/pull/27673),
      [#26962](https://github.com/open-webui/open-webui/issues/26962)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F501 **Rebuilding knowledge base vectors.** Rebuilding the vectors
      for a knowledge base now also rebuilds them for each file it contains, so attaching
      a single file afterwards finds its content instead of quietly returning nothing
      and letting the model answer from thin air. [#28106](https://github.com/open-webui/open-webui/issues/28106),
      [Commit](https://github.com/open-webui/open-webui/commit/2a6e671f548970c8223692024e630b9936e9fa7c),
      [Commit](https://github.com/open-webui/open-webui/commit/89922cc9d585e10b026693681b44afdc4b874588)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F4F0 **Attached pages reaching the model.** The text pulled from
      an attached web page or YouTube video now actually reaches the model, rather
      than arriving empty so the reply had nothing to work from, and opening the source
      to check no longer fails. [#28378](https://github.com/open-webui/open-webui/issues/28378),
      [Commit](https://github.com/open-webui/open-webui/commit/9c21d4ed3ba9ba8e53def7e1a1366b74834cb42d)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F4C5 **Editing a calendar event through chat.** Asking a model to
      change one thing about an event, such as its title, no longer fails or wipes
      the details you did not mention. [#27777](https://github.com/open-webui/open-webui/pull/27777),
      [#27776](https://github.com/open-webui/open-webui/issues/27776)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001FA7A **Repairing default model settings.** Instances whose stored
      default and pinned model settings had been written in the wrong shape are corrected
      on startup, so those defaults take effect again. [Commit](https://github.com/open-webui/open-webui/commit/5c05608e3ac0aefce8c1eed18c3e205c61f6b6fe)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F9FD **Cleaner conversation history for the model.** Internal bookkeeping
      attached to your messages, such as attachment records and token counts, is no
      longer sent to the model along with the conversation. [Commit](https://github.com/open-webui/open-webui/commit/a32a17965ca36f730ebf5ff53a2a8e17082b61a6)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F914 **Reasoning carried back to Ollama.** A model's earlier thinking
      is now passed back to Ollama in its own native field rather than pasted into
      the message as tagged text, so reasoning models keep their train of thought
      across turns. [Commit](https://github.com/open-webui/open-webui/commit/3258330729942b533dc5fe141e876cee7e5eb40d)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: ✏️ **Editing other people's channel messages.** Asking a model to work
      on a message in a channel now only applies to your own messages, where write
      access to the channel had been enough to reach anyone's. [#28631](https://github.com/open-webui/open-webui/pull/28631)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F4DA **Knowledge search and shared files in chat.** A model searching
      your knowledge bases or reading a file shared with you through a group now works,
      where it had failed since 0.11.0 and quietly answered as though the knowledge
      were empty, affecting instances that forward user details to their embedding
      service and, for shared files, every instance regardless of settings. [#27642](https://github.com/open-webui/open-webui/pull/27642),
      [#27641](https://github.com/open-webui/open-webui/issues/27641)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F524 **Model names on connections with a prefix.** A connection
      that adds a prefix to its model names now strips it before sending a request
      through the responses endpoint, where the prefixed name was passed on and rejected
      as unknown. [#28575](https://github.com/open-webui/open-webui/pull/28575), [#28574](https://github.com/open-webui/open-webui/issues/28574)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F58C️ **White boxes behind model icons.** Model icons with a transparent
      background no longer sit on a white square in the admin models list, matching
      how they already appeared everywhere else. [#27612](https://github.com/open-webui/open-webui/pull/27612),
      [#27611](https://github.com/open-webui/open-webui/issues/27611)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F504 **Syncing a model catalogue more than once.** Syncing models
      now updates the ones that already exist, where any repeat of a previous sync
      silently did nothing at all while still reporting success. [#28036](https://github.com/open-webui/open-webui/pull/28036),
      [#28033](https://github.com/open-webui/open-webui/issues/28033)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F50B **Session and usage records left uncleared.** The routines
      that clear out stale sessions and finished model usage can no longer be discarded
      while the application is running, so those records stop accumulating unnoticed,
      and both now stop cleanly on shutdown. [#28053](https://github.com/open-webui/open-webui/pull/28053),
      [#28052](https://github.com/open-webui/open-webui/issues/28052)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: ⚗️ **Reasoning carried between turns.** A model's earlier thinking is now
      recognised from providers that report it in their own nested field, and reasoning
      that cannot be sent back without a signature is left out rather than being passed
      on and rejected. [Commit](https://github.com/open-webui/open-webui/commit/b6dc70c93b0d36e2659438e7a55aa8b21fee27f8)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F6CE️ **Losing all your settings.** Your interface settings are
      no longer wiped by a session that failed to load them, which could happen with
      no action on your part and cleared everything from your theme to your model
      parameters; saving now changes only the settings you actually changed, and a
      session that cannot load them tells you instead of carrying on as though you
      had none. [#27766](https://github.com/open-webui/open-webui/issues/27766), [Commit](https://github.com/open-webui/open-webui/commit/ad8c79f68657bd3bcf5db6be650e498bb904b36b)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F9EF **Timers that fail without saying so.** A timer whose reply
      cannot be generated, such as one set against a model that has since been removed,
      is now recorded as failed with the reason, instead of being marked as completed
      while the reply never arrives. [#27785](https://github.com/open-webui/open-webui/pull/27785),
      [#27783](https://github.com/open-webui/open-webui/issues/27783)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F52D **Searching the calendar without an end date.** Asking a model
      to search your calendar without naming an end date now works on PostgreSQL,
      where the open-ended range was too large for the database to accept and the
      search failed outright. [Commit](https://github.com/open-webui/open-webui/commit/9550731cc17759f6862595b8cd849ae48695b5c1),
      [#27717](https://github.com/open-webui/open-webui/issues/27717)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: ⚓ **Starting up as a non-root user.** Deployments that run the container
      as a non-root user, such as Kubernetes setups using runAsNonRoot, start again,
      where a bundled speech model file that only root could read had stopped them
      since 0.11.0, and a bundled text corpus is now stored somewhere a non-root user
      can reach. [#27651](https://github.com/open-webui/open-webui/issues/27651),
      [Commit](https://github.com/open-webui/open-webui/commit/0480ca9653f0d566eaedadf0af0d785a9938480b),
      [#28866](https://github.com/open-webui/open-webui/pull/28866)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F5C4️ **Empty models section in the sidebar.** The models section
      no longer appears with nothing in it when every pinned model has since been
      removed, renamed, or hidden. [#27634](https://github.com/open-webui/open-webui/pull/27634),
      [#27633](https://github.com/open-webui/open-webui/issues/27633)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F4AB **Thinking indicator with the fade turned off.** Turning off
      the fade effect for streaming text no longer hides the thinking indicator and
      its spinner, which had made a reasoning model look as though it had already
      finished from the first moment it started. [#28559](https://github.com/open-webui/open-webui/issues/28559),
      [Commit](https://github.com/open-webui/open-webui/commit/b1dc945bd6cf97a7067e603fc1b797301e626fb6)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F4DC **System prompt repeated after a tool call.** On models served
      by a pipe or manifold, the system prompt is no longer added again each time
      a tool runs, where it built up one extra copy per round and was sent to the
      provider that way. [#28739](https://github.com/open-webui/open-webui/pull/28739),
      [#28736](https://github.com/open-webui/open-webui/issues/28736)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F5E8 **Attached conversations reaching the model.** A conversation
      attached to your message is now listed among its attachments, where it was left
      out entirely and the model was never told it was there. [#28788](https://github.com/open-webui/open-webui/pull/28788)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F4C9 **Usage figures drifting upward on clustered setups.** The
      routine that clears out finished model usage no longer stops for good across
      the whole cluster after a brief interruption, which had left the usage figures
      counting models nobody was using and grew the work every disconnection had to
      do. [#28834](https://github.com/open-webui/open-webui/pull/28834)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F53B **Message box controls in a narrow panel.** Narrowing the note
      chat panel, or squeezing the chat with a wide controls pane, no longer hides
      the attach and integrations buttons behind the model name or pushes the send
      button outside the box; the model name is shortened to make room instead. [#28912](https://github.com/open-webui/open-webui/pull/28912),
      [#28911](https://github.com/open-webui/open-webui/issues/28911)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: ⌛ **Replies that are all thinking and no answer.** A reply from a provider
      using the responses format that ends while the model is still in its reasoning,
      with no answer text after it, now finishes normally instead of failing the whole
      turn and leaving an unreadable error in place of the reply. [#28872](https://github.com/open-webui/open-webui/pull/28872),
      [#28871](https://github.com/open-webui/open-webui/issues/28871)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F39E **Workspace models in the admin models list.** Workspace models
      appear in the admin models list again, so they can be ordered, set as the default,
      and pinned for everyone; choosing one opens its own editor, where it opened
      the base model editor and could strip the model's base model, turning it into
      something else. [Commit](https://github.com/open-webui/open-webui/commit/ccbb3303f2ec5db0b16573bbb665a12f6764da66),
      [#27702](https://github.com/open-webui/open-webui/issues/27702)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F9FF **Shortening a conversation with the wrong model.** Choosing
      to shorten long conversations with the model you are chatting with now does
      that, where it used the configured task model instead on any instance that has
      one. [Commit](https://github.com/open-webui/open-webui/commit/5093a9938937153e287db27a671f5ba1fb5d7592),
      [#27603](https://github.com/open-webui/open-webui/issues/27603)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F399 **The wrong model selected when reopening a chat.** Reopening
      a conversation where a reply was regenerated with a different model now selects
      the model behind the reply you are looking at, where it picked the one used
      for the first attempt, which might be a model no longer available. [#27674](https://github.com/open-webui/open-webui/pull/27674),
      [#25052](https://github.com/open-webui/open-webui/issues/25052), [Commit](https://github.com/open-webui/open-webui/commit/8a170897bad569d93e069226a996942583ebde80)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F6DC **Coding tools that speak Anthropic's format.** A tool such
      as Cline pointed at Open WebUI using Anthropic's own message format can reach
      models again, where every request failed before it was even sent, and once that
      was corrected the request was rejected by Anthropic for being signed the wrong
      way. [#27675](https://github.com/open-webui/open-webui/pull/27675), [#27595](https://github.com/open-webui/open-webui/issues/27595),
      [#27695](https://github.com/open-webui/open-webui/issues/27695)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F4D7 **Opening knowledge attached to a model or folder.** Clicking
      a knowledge item attached to a model or a folder opens it again, so it can be
      read and its retrieval mode changed between focused retrieval and the whole
      document, where since 0.11.0 neither was possible outside a chat. [#27686](https://github.com/open-webui/open-webui/pull/27686),
      [#27684](https://github.com/open-webui/open-webui/issues/27684), [#27801](https://github.com/open-webui/open-webui/issues/27801),
      [#28825](https://github.com/open-webui/open-webui/issues/28825)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F3DE **Clearing a model's picture.** A model's picture can be reset
      to the default logo again, where since 0.11.0 a custom one could only ever be
      replaced. [#29007](https://github.com/open-webui/open-webui/pull/29007), [#27685](https://github.com/open-webui/open-webui/issues/27685),
      [Commit](https://github.com/open-webui/open-webui/commit/06e7aac219b3027a9d578624c473b041ad26a692)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F573️ **Blank messages left in a conversation.** Streamed events
      that never fill in an item no longer leave an empty assistant message saved
      in the conversation and sent back to the model on every later turn. [Commit](https://github.com/open-webui/open-webui/commit/2a0274a0a039dbe0a1ad4d24003b085aae7b896b)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001FA9C **Falling back when a base model is gone.** Chatting with a
      workspace model whose base model has been removed now falls back to the default
      model for everyone, where the fallback previously applied only for administrators
      and anyone else was refused whenever that base model had no workspace entry
      of its own, such as one supplied by a pipe. [Commit](https://github.com/open-webui/open-webui/commit/20fe43d9da621957c48fc92104bc8f1cc0d691b7)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F9E0 **Conversations breaking after a model switch.** Switching
      to a different model once a reasoning model has answered no longer leaves the
      conversation unusable, where the earlier model's stored reasoning was replayed
      to a provider that then rejected every later request. [Commit](https://github.com/open-webui/open-webui/commit/c4b3e6840f34a5d267bc12c0ec1a82156a324d45),
      [#28240](https://github.com/open-webui/open-webui/issues/28240)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F9EC **Workspace models pointing at themselves.** A workspace model
      whose base model was set to its own identifier is now saved without that reference,
      where the entry was thrown away while models were being combined so none of
      its settings ever took effect. [Commit](https://github.com/open-webui/open-webui/commit/eadce55e343df69520e6bc86dbbdfdcdfdcafb30),
      [#28952](https://github.com/open-webui/open-webui/issues/28952), [#28923](https://github.com/open-webui/open-webui/issues/28923)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F4ED **A short model list sticking on every worker.** When one worker
      briefly reports fewer models than it should, that shorter list is no longer
      left in place for the whole deployment, where chatting with one of the missing
      models failed on every server until something restarted. [Commit](https://github.com/open-webui/open-webui/commit/6330350a406d8c1fd603f725e59a88324c8e2256),
      [#28777](https://github.com/open-webui/open-webui/issues/28777)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  - quote: "\U0001F170 **Connection prefixes now show in model names.** A connection's
      prefix appears in the name shown in the model picker, not only in its identifier,
      where whether it did depended on the shape of the provider's reply and so worked
      on some connections and not others; models on prefixed connections will now
      read differently than before. [#28950](https://github.com/open-webui/open-webui/pull/28950),
      [#28929](https://github.com/open-webui/open-webui/issues/28929)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 56-model-support-changes-in-v0-11-1
  source_release: open-webui-2026-08-25-v0-11-1-github-376725636-ce7e3a4c
  source_type: github_releases
  theme: model-support
  title: 56 Model Support changes in v0.11.1
  type: change
related_changes:
- '[[Changes/Cline/2026-08-23-refresh-the-built-in-model-catalog-new-entries-include-claude-fable-5-grok-4-6-o|Refresh
  the built-in model catalog]]'
- '[[Changes/Lovable/2026-08-24-chat-latest-for-your-app-s-ai-features|Chat Latest
  for your app''s AI features]]'
- '[[Changes/Dify/2026-08-25-93-model-support-changes-in-1-17-0|93 Model Support changes
  in 1.17.0]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-08-25-v0-11-1-github-376725636-ce7e3a4c|open-webui-2026-08-25-v0-11-1-github-376725636-ce7e3a4c]]'
source_type: github_releases
theme: model-support
title: 56 Model Support changes in v0.11.1
type: change
---

<!-- chronolog:begin region="header" -->
# 56 Model Support changes in v0.11.1

**Open WebUI** · 2026-08-25 · [[Themes/model-support|Model Support]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.11.1) · from [[Releases/Open WebUI/open-webui-2026-08-25-v0-11-1-github-376725636-ce7e3a4c|v0.11.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🙋♂️ **Models that can ask you a question.** A new built-in tool lets a model pause and put up to three multiple-choice questions to you before continuing, with room to type your own answer instead, and the question survives a reload in a saved conversation, so you can come back and answer it later rather than losing the conversation. [Commit](https://github.com/open-webui/open-webui/commit/4465f52a3eb521854cf190f91b0ea7cf3fa21830), [Commit](https://github.com/open-webui/open-webui/commit/133549a87ee371577453d897c2db2d8071223f27), [Commit](https://github.com/open-webui/open-webui/commit/b018feb7419e68314378b3cdd8b7b1b389400a98), [Commit](https://github.com/open-webui/open-webui/commit/083e35144152d6a301bed01aa6d898db3871ddcf), [Commit](https://github.com/open-webui/open-webui/commit/256cce505be8ddd4930e8cb2536faea718d3f789), [Commit](https://github.com/open-webui/open-webui/commit/14e4d72d9a21a10196e8e6efb04180cd9104b8e6), [Commit](https://github.com/open-webui/open-webui/commit/57bd08304e45f707768a898de9f50894929008dd), [Commit](https://github.com/open-webui/open-webui/commit/d9014b3483d4c6e8d99e50395afcdc538bcf05cd)

> 🚀 **Faster model list lookups.** Title generation, tag suggestions, autocomplete, and other background steps of a chat turn now fetch the model list in one go, which keeps other people's responses flowing on busy Redis-backed instances with many models. [#27821](https://github.com/open-webui/open-webui/pull/27821)

> 🧊 **Faster file access checks.** Checking whether you may reach a file no longer walks every workspace model you can see looking for it, so opening a folder of files, downloading one, or retrieving from one is much quicker on instances with many models. [#28802](https://github.com/open-webui/open-webui/pull/28802)

> 🚏 **Faster workspace model lookups.** Working out which workspace models you may edit no longer loads every model on the instance and discards most of them, which also speeds up exporting models and the file access checks that relied on it. [#28795](https://github.com/open-webui/open-webui/pull/28795)

> 🥁 **Long replies no longer slow as they grow.** A long reply is no longer re-examined from the beginning for reasoning and code blocks on every piece that arrives, so the work stops growing with the length of the reply, which on a long reply is around 190x less time spent on it. [#28861](https://github.com/open-webui/open-webui/pull/28861)

> 🧰 **Managing models on more servers.** Administrators can now download, load, and unload models on llama.cpp and LM Studio connections from the manage models dialog, remove them on llama.cpp, and start a download straight from the model picker's search box, alongside the Ollama support that was already there. [Commit](https://github.com/open-webui/open-webui/commit/85c3d0ae2fad58ffc2b92b1733a6c8bc7ab471db), [Commit](https://github.com/open-webui/open-webui/commit/8260d527ee97372a207ce9bd9c6dab4909061281), [Commit](https://github.com/open-webui/open-webui/commit/25802c048e6123fa602182949ad2a9f349e1e863), [Commit](https://github.com/open-webui/open-webui/commit/31c1ffd55a018a74c7e53a35fb9f9bbe33774b6f), [#28766](https://github.com/open-webui/open-webui/pull/28766)

> 🏷️ **Named writing blocks.** When a model wraps a draft such as an email in a writing block, the block is now titled with its subject and shows the recipient beside it, rather than every block reading simply as Writing. [#28280](https://github.com/open-webui/open-webui/pull/28280), [#28198](https://github.com/open-webui/open-webui/issues/28198)

> 🧾 **CSV shape in retrieval.** Turning on "ENABLE_RAG_CSV_SUMMARY" adds a short line naming the row count, data row count, column count, and column names of a CSV file to what the model sees, giving it the shape of the table alongside its contents. [Commit](https://github.com/open-webui/open-webui/commit/1b72899f246ba46ab8f7cd6aee2d56ef69217d82)

> 📙 **OpenDocument files in a temporary chat.** A text document, spreadsheet, or presentation from an office suite that uses the OpenDocument format now has its text read out in the browser when attached to a temporary chat, where the model was handed the raw archive and answered that it could not read the file. [Commit](https://github.com/open-webui/open-webui/commit/9e7c9360b744c878ae0c38aa1caf3886f27b07ab), [#28906](https://github.com/open-webui/open-webui/discussions/28906)

> ✂️ **Long replies cut off partway.** A single oversized piece of a streamed reply, such as a long reasoning trace or a turn carrying many tool calls, no longer ends the answer early with a misleading error about byte counts, which affected every default installation. [#28114](https://github.com/open-webui/open-webui/pull/28114), [#25664](https://github.com/open-webui/open-webui/issues/25664)

> 🧑💻 **Code execution reachable through a tag in a reply.** On installs using native function calling, the older path that runs code found inside a tag in the model's reply is no longer active alongside the built-in tool, so code execution happens only through an explicit tool call. [#29024](https://github.com/open-webui/open-webui/pull/29024)

> 🧬 **Workspace models shadowing a real one.** Someone without administrator rights can no longer create, import, or edit a workspace model so that it takes over the identity of a model served by a connected provider, where doing so would have changed what everyone else got when they picked that model. [Commit](https://github.com/open-webui/open-webui/commit/ea55d38793014a4e3cd5a4046816fe22e69e9739)

> 🔍 **Listing a single connection's models.** Asking for the models or version of one particular connection is now restricted to administrators, and a request naming a specific backend is checked against the models that backend actually serves even where the access control bypass is turned on. [Commit](https://github.com/open-webui/open-webui/commit/16f118d77ad9d68c64116f94551ffb14bf8b2abd)

> 🧩 **Chats during model list refreshes.** On direct connections, background work such as title and tag generation no longer fails or runs against a mix of old and new model entries while the model list is being refreshed. [#27821](https://github.com/open-webui/open-webui/pull/27821)

> 🚫 **Duplicate models in lists.** Adding a model that is already on a connection's allowed list is now rejected instead of quietly adding it a second time, the arena picker no longer offers models you have already chosen, and existing duplicates are cleaned up the next time the list is saved. [#28251](https://github.com/open-webui/open-webui/pull/28251), [#28249](https://github.com/open-webui/open-webui/issues/28249)

> 🎯 **Custom model parameters combining.** Setting a custom parameter on a model no longer silently discards every custom parameter defined in the global defaults, and a value sent directly in an API request is no longer overwritten by the model's saved settings. [Commit](https://github.com/open-webui/open-webui/commit/11739a2de8eddf7ef26378356aff8a1bcab4a349), [#28241](https://github.com/open-webui/open-webui/issues/28241)

> 🔧 **Full tool parameter descriptions.** A tool whose parameter description runs over several lines now passes the whole description to the model instead of only its first line. [Commit](https://github.com/open-webui/open-webui/commit/b606e13da3753027ead0e92e35e1399b60c96c8e)

> 🎚️ **ColBERT reranker startup.** Loading a ColBERT reranker now names the model in the log rather than printing a logging error and a traceback in its place. [#27838](https://github.com/open-webui/open-webui/pull/27838)

> ↕️ **Expand button in the message box.** The button that enlarges the message box no longer sits on top of a tagged model's dismiss button or the first attached file, and stays reachable in long prompts. [#27676](https://github.com/open-webui/open-webui/pull/27676), [#26736](https://github.com/open-webui/open-webui/issues/26736)

> 🪄 **Merged responses after a reload.** Merging the answers from several models now works on a conversation you have reopened, instead of the merging model reporting that the other responses were empty. [#27673](https://github.com/open-webui/open-webui/pull/27673), [#26962](https://github.com/open-webui/open-webui/issues/26962)

> 🔁 **Rebuilding knowledge base vectors.** Rebuilding the vectors for a knowledge base now also rebuilds them for each file it contains, so attaching a single file afterwards finds its content instead of quietly returning nothing and letting the model answer from thin air. [#28106](https://github.com/open-webui/open-webui/issues/28106), [Commit](https://github.com/open-webui/open-webui/commit/2a6e671f548970c8223692024e630b9936e9fa7c), [Commit](https://github.com/open-webui/open-webui/commit/89922cc9d585e10b026693681b44afdc4b874588)

> 📰 **Attached pages reaching the model.** The text pulled from an attached web page or YouTube video now actually reaches the model, rather than arriving empty so the reply had nothing to work from, and opening the source to check no longer fails. [#28378](https://github.com/open-webui/open-webui/issues/28378), [Commit](https://github.com/open-webui/open-webui/commit/9c21d4ed3ba9ba8e53def7e1a1366b74834cb42d)

> 📅 **Editing a calendar event through chat.** Asking a model to change one thing about an event, such as its title, no longer fails or wipes the details you did not mention. [#27777](https://github.com/open-webui/open-webui/pull/27777), [#27776](https://github.com/open-webui/open-webui/issues/27776)

> 🩺 **Repairing default model settings.** Instances whose stored default and pinned model settings had been written in the wrong shape are corrected on startup, so those defaults take effect again. [Commit](https://github.com/open-webui/open-webui/commit/5c05608e3ac0aefce8c1eed18c3e205c61f6b6fe)

> 🧽 **Cleaner conversation history for the model.** Internal bookkeeping attached to your messages, such as attachment records and token counts, is no longer sent to the model along with the conversation. [Commit](https://github.com/open-webui/open-webui/commit/a32a17965ca36f730ebf5ff53a2a8e17082b61a6)

> 🤔 **Reasoning carried back to Ollama.** A model's earlier thinking is now passed back to Ollama in its own native field rather than pasted into the message as tagged text, so reasoning models keep their train of thought across turns. [Commit](https://github.com/open-webui/open-webui/commit/3258330729942b533dc5fe141e876cee7e5eb40d)

> ✏️ **Editing other people's channel messages.** Asking a model to work on a message in a channel now only applies to your own messages, where write access to the channel had been enough to reach anyone's. [#28631](https://github.com/open-webui/open-webui/pull/28631)

> 📚 **Knowledge search and shared files in chat.** A model searching your knowledge bases or reading a file shared with you through a group now works, where it had failed since 0.11.0 and quietly answered as though the knowledge were empty, affecting instances that forward user details to their embedding service and, for shared files, every instance regardless of settings. [#27642](https://github.com/open-webui/open-webui/pull/27642), [#27641](https://github.com/open-webui/open-webui/issues/27641)

> 🔤 **Model names on connections with a prefix.** A connection that adds a prefix to its model names now strips it before sending a request through the responses endpoint, where the prefixed name was passed on and rejected as unknown. [#28575](https://github.com/open-webui/open-webui/pull/28575), [#28574](https://github.com/open-webui/open-webui/issues/28574)

> 🖌️ **White boxes behind model icons.** Model icons with a transparent background no longer sit on a white square in the admin models list, matching how they already appeared everywhere else. [#27612](https://github.com/open-webui/open-webui/pull/27612), [#27611](https://github.com/open-webui/open-webui/issues/27611)

> 🔄 **Syncing a model catalogue more than once.** Syncing models now updates the ones that already exist, where any repeat of a previous sync silently did nothing at all while still reporting success. [#28036](https://github.com/open-webui/open-webui/pull/28036), [#28033](https://github.com/open-webui/open-webui/issues/28033)

> 🔋 **Session and usage records left uncleared.** The routines that clear out stale sessions and finished model usage can no longer be discarded while the application is running, so those records stop accumulating unnoticed, and both now stop cleanly on shutdown. [#28053](https://github.com/open-webui/open-webui/pull/28053), [#28052](https://github.com/open-webui/open-webui/issues/28052)

> ⚗️ **Reasoning carried between turns.** A model's earlier thinking is now recognised from providers that report it in their own nested field, and reasoning that cannot be sent back without a signature is left out rather than being passed on and rejected. [Commit](https://github.com/open-webui/open-webui/commit/b6dc70c93b0d36e2659438e7a55aa8b21fee27f8)

> 🛎️ **Losing all your settings.** Your interface settings are no longer wiped by a session that failed to load them, which could happen with no action on your part and cleared everything from your theme to your model parameters; saving now changes only the settings you actually changed, and a session that cannot load them tells you instead of carrying on as though you had none. [#27766](https://github.com/open-webui/open-webui/issues/27766), [Commit](https://github.com/open-webui/open-webui/commit/ad8c79f68657bd3bcf5db6be650e498bb904b36b)

> 🧯 **Timers that fail without saying so.** A timer whose reply cannot be generated, such as one set against a model that has since been removed, is now recorded as failed with the reason, instead of being marked as completed while the reply never arrives. [#27785](https://github.com/open-webui/open-webui/pull/27785), [#27783](https://github.com/open-webui/open-webui/issues/27783)

> 🔭 **Searching the calendar without an end date.** Asking a model to search your calendar without naming an end date now works on PostgreSQL, where the open-ended range was too large for the database to accept and the search failed outright. [Commit](https://github.com/open-webui/open-webui/commit/9550731cc17759f6862595b8cd849ae48695b5c1), [#27717](https://github.com/open-webui/open-webui/issues/27717)

> ⚓ **Starting up as a non-root user.** Deployments that run the container as a non-root user, such as Kubernetes setups using runAsNonRoot, start again, where a bundled speech model file that only root could read had stopped them since 0.11.0, and a bundled text corpus is now stored somewhere a non-root user can reach. [#27651](https://github.com/open-webui/open-webui/issues/27651), [Commit](https://github.com/open-webui/open-webui/commit/0480ca9653f0d566eaedadf0af0d785a9938480b), [#28866](https://github.com/open-webui/open-webui/pull/28866)

> 🗄️ **Empty models section in the sidebar.** The models section no longer appears with nothing in it when every pinned model has since been removed, renamed, or hidden. [#27634](https://github.com/open-webui/open-webui/pull/27634), [#27633](https://github.com/open-webui/open-webui/issues/27633)

> 💫 **Thinking indicator with the fade turned off.** Turning off the fade effect for streaming text no longer hides the thinking indicator and its spinner, which had made a reasoning model look as though it had already finished from the first moment it started. [#28559](https://github.com/open-webui/open-webui/issues/28559), [Commit](https://github.com/open-webui/open-webui/commit/b1dc945bd6cf97a7067e603fc1b797301e626fb6)

> 📜 **System prompt repeated after a tool call.** On models served by a pipe or manifold, the system prompt is no longer added again each time a tool runs, where it built up one extra copy per round and was sent to the provider that way. [#28739](https://github.com/open-webui/open-webui/pull/28739), [#28736](https://github.com/open-webui/open-webui/issues/28736)

> 🗨 **Attached conversations reaching the model.** A conversation attached to your message is now listed among its attachments, where it was left out entirely and the model was never told it was there. [#28788](https://github.com/open-webui/open-webui/pull/28788)

> 📉 **Usage figures drifting upward on clustered setups.** The routine that clears out finished model usage no longer stops for good across the whole cluster after a brief interruption, which had left the usage figures counting models nobody was using and grew the work every disconnection had to do. [#28834](https://github.com/open-webui/open-webui/pull/28834)

> 🔻 **Message box controls in a narrow panel.** Narrowing the note chat panel, or squeezing the chat with a wide controls pane, no longer hides the attach and integrations buttons behind the model name or pushes the send button outside the box; the model name is shortened to make room instead. [#28912](https://github.com/open-webui/open-webui/pull/28912), [#28911](https://github.com/open-webui/open-webui/issues/28911)

> ⌛ **Replies that are all thinking and no answer.** A reply from a provider using the responses format that ends while the model is still in its reasoning, with no answer text after it, now finishes normally instead of failing the whole turn and leaving an unreadable error in place of the reply. [#28872](https://github.com/open-webui/open-webui/pull/28872), [#28871](https://github.com/open-webui/open-webui/issues/28871)

> 🎞 **Workspace models in the admin models list.** Workspace models appear in the admin models list again, so they can be ordered, set as the default, and pinned for everyone; choosing one opens its own editor, where it opened the base model editor and could strip the model's base model, turning it into something else. [Commit](https://github.com/open-webui/open-webui/commit/ccbb3303f2ec5db0b16573bbb665a12f6764da66), [#27702](https://github.com/open-webui/open-webui/issues/27702)

> 🧿 **Shortening a conversation with the wrong model.** Choosing to shorten long conversations with the model you are chatting with now does that, where it used the configured task model instead on any instance that has one. [Commit](https://github.com/open-webui/open-webui/commit/5093a9938937153e287db27a671f5ba1fb5d7592), [#27603](https://github.com/open-webui/open-webui/issues/27603)

> 🎙 **The wrong model selected when reopening a chat.** Reopening a conversation where a reply was regenerated with a different model now selects the model behind the reply you are looking at, where it picked the one used for the first attempt, which might be a model no longer available. [#27674](https://github.com/open-webui/open-webui/pull/27674), [#25052](https://github.com/open-webui/open-webui/issues/25052), [Commit](https://github.com/open-webui/open-webui/commit/8a170897bad569d93e069226a996942583ebde80)

> 🛜 **Coding tools that speak Anthropic's format.** A tool such as Cline pointed at Open WebUI using Anthropic's own message format can reach models again, where every request failed before it was even sent, and once that was corrected the request was rejected by Anthropic for being signed the wrong way. [#27675](https://github.com/open-webui/open-webui/pull/27675), [#27595](https://github.com/open-webui/open-webui/issues/27595), [#27695](https://github.com/open-webui/open-webui/issues/27695)

> 📗 **Opening knowledge attached to a model or folder.** Clicking a knowledge item attached to a model or a folder opens it again, so it can be read and its retrieval mode changed between focused retrieval and the whole document, where since 0.11.0 neither was possible outside a chat. [#27686](https://github.com/open-webui/open-webui/pull/27686), [#27684](https://github.com/open-webui/open-webui/issues/27684), [#27801](https://github.com/open-webui/open-webui/issues/27801), [#28825](https://github.com/open-webui/open-webui/issues/28825)

> 🏞 **Clearing a model's picture.** A model's picture can be reset to the default logo again, where since 0.11.0 a custom one could only ever be replaced. [#29007](https://github.com/open-webui/open-webui/pull/29007), [#27685](https://github.com/open-webui/open-webui/issues/27685), [Commit](https://github.com/open-webui/open-webui/commit/06e7aac219b3027a9d578624c473b041ad26a692)

> 🕳️ **Blank messages left in a conversation.** Streamed events that never fill in an item no longer leave an empty assistant message saved in the conversation and sent back to the model on every later turn. [Commit](https://github.com/open-webui/open-webui/commit/2a0274a0a039dbe0a1ad4d24003b085aae7b896b)

> 🪜 **Falling back when a base model is gone.** Chatting with a workspace model whose base model has been removed now falls back to the default model for everyone, where the fallback previously applied only for administrators and anyone else was refused whenever that base model had no workspace entry of its own, such as one supplied by a pipe. [Commit](https://github.com/open-webui/open-webui/commit/20fe43d9da621957c48fc92104bc8f1cc0d691b7)

> 🧠 **Conversations breaking after a model switch.** Switching to a different model once a reasoning model has answered no longer leaves the conversation unusable, where the earlier model's stored reasoning was replayed to a provider that then rejected every later request. [Commit](https://github.com/open-webui/open-webui/commit/c4b3e6840f34a5d267bc12c0ec1a82156a324d45), [#28240](https://github.com/open-webui/open-webui/issues/28240)

> 🧬 **Workspace models pointing at themselves.** A workspace model whose base model was set to its own identifier is now saved without that reference, where the entry was thrown away while models were being combined so none of its settings ever took effect. [Commit](https://github.com/open-webui/open-webui/commit/eadce55e343df69520e6bc86dbbdfdcdfdcafb30), [#28952](https://github.com/open-webui/open-webui/issues/28952), [#28923](https://github.com/open-webui/open-webui/issues/28923)

> 📭 **A short model list sticking on every worker.** When one worker briefly reports fewer models than it should, that shorter list is no longer left in place for the whole deployment, where chatting with one of the missing models failed on every server until something restarted. [Commit](https://github.com/open-webui/open-webui/commit/6330350a406d8c1fd603f725e59a88324c8e2256), [#28777](https://github.com/open-webui/open-webui/issues/28777)

> 🅰 **Connection prefixes now show in model names.** A connection's prefix appears in the name shown in the model picker, not only in its identifier, where whether it did depended on the shape of the provider's reply and so worked on some connections and not others; models on prefixed connections will now read differently than before. [#28950](https://github.com/open-webui/open-webui/pull/28950), [#28929](https://github.com/open-webui/open-webui/issues/28929)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.11.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-08-25-9-files-and-data-changes-in-v0-11-1|9 Files and Data changes in v0.11.1]] · Files and Data
- [[Changes/Open WebUI/2026-08-25-image-generation-and-web-search-staying-switched-off-turning-either-off-now-take|🎨 Image generation and web search staying switched off. Turning either off now…]] · Image Generation
- [[Changes/Open WebUI/2026-08-25-7-safety-and-privacy-changes-in-v0-11-1|7 Safety and Privacy changes in v0.11.1]] · Safety and Privacy
- [[Changes/Open WebUI/2026-08-25-improved-ui-accessibility-a-closed-sidebar-is-no-longer-reachable-by-keyboard-or|♿ Improved UI accessibility. A closed sidebar is no longer reachable by keyboard…]] · Accessibility and Localization
- [[Changes/Open WebUI/2026-08-25-2-pricing-model-changes-in-v0-11-1|2 Pricing Model changes in v0.11.1]] · Pricing Model
- [[Changes/Open WebUI/2026-08-25-11-automation-and-scheduling-changes-in-v0-11-1|11 Automation and Scheduling changes in v0.11.1]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-08-25-10-reliability-and-performance-changes-in-v0-11-1|10 Reliability and Performance changes in v0.11.1]] · Reliability and Performance
- [[Changes/Open WebUI/2026-08-25-6-collaboration-changes-in-v0-11-1|6 Collaboration changes in v0.11.1]] · Collaboration
- [[Changes/Open WebUI/2026-08-25-4-context-window-changes-in-v0-11-1|4 Context Window changes in v0.11.1]] · Context Window
- [[Changes/Open WebUI/2026-08-25-13-account-and-access-changes-in-v0-11-1|13 Account and Access changes in v0.11.1]] · Account and Access
- [[Changes/Open WebUI/2026-08-25-starting-up-on-windows-the-windows-start-script-now-creates-the-secret-key-it-ne|🪟 Starting up on Windows. The Windows start script now creates the secret key…]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-08-25-2-multimodal-input-changes-in-v0-11-1|2 Multimodal Input changes in v0.11.1]] · Multimodal Input
- [[Changes/Open WebUI/2026-08-25-12-editor-experience-changes-in-v0-11-1|12 Editor Experience changes in v0.11.1]] · Editor Experience
- [[Changes/Open WebUI/2026-08-25-4-apps-and-integrations-changes-in-v0-11-1|4 Apps and Integrations changes in v0.11.1]] · Apps and Integrations
- [[Changes/Open WebUI/2026-08-25-73-developer-workflow-changes-in-v0-11-1|73 Developer Workflow changes in v0.11.1]] · Developer Workflow
- [[Changes/Open WebUI/2026-08-25-8-memory-and-personalization-changes-in-v0-11-1|8 Memory and Personalization changes in v0.11.1]] · Memory and Personalization
- [[Changes/Open WebUI/2026-08-25-files-for-delegated-tasks-a-task-handed-to-a-sub-agent-can-now-carry-the-attachm|🤝 Files for delegated tasks. A task handed to a sub-agent can now carry…]] · Agent Mode
- [[Changes/Open WebUI/2026-08-25-4-enterprise-and-administration-changes-in-v0-11-1|4 Enterprise and Administration changes in v0.11.1]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-08-25-24-interface-experience-changes-in-v0-11-1|24 Interface Experience changes in v0.11.1]] · Interface Experience
- [[Changes/Open WebUI/2026-08-25-5-search-and-browsing-changes-in-v0-11-1|5 Search and Browsing changes in v0.11.1]] · Search and Browsing
- [[Changes/Open WebUI/2026-08-25-4-voice-and-audio-changes-in-v0-11-1|4 Voice and Audio changes in v0.11.1]] · Voice and Audio
- [[Changes/Open WebUI/2026-08-25-39-other-changes-in-v0-11-1|39 other changes in v0.11.1]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Model Support

- Earlier: 2026-08-25 · Dify · [[Changes/Dify/2026-08-25-93-model-support-changes-in-1-17-0|93 Model Support changes in 1.17.0]]
- Later: 2026-08-26 · Claude Code · [[Changes/Claude Code/2026-08-26-added-claude-api-cost-optimize-to-profile-an-existing-project-s-claude-api-spend|Added /claude-api cost-optimize to profile an existing project's Claude API spend…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-01-09 · ChatGPT · [[Changes/ChatGPT/2023-01-09-we-made-more-improvements-to-the-chatgpt-model-it-should-be-generally-better-acr|We made more improvements to the ChatGPT model!]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-08-25-f1ebf1&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-08-25-56-model-support-changes-in-v0-11-1.md%0ACard%20ID%3A%20open-webui-2026-08-25-f1ebf1%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.11.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->