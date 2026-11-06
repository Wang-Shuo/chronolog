---
card_id: open-webui-2026-09-21-2e2089
date: '2026-09-21'
description: "Open WebUI · 2026-09-21 · Developer Workflow: 39 changes in v0.11.4
  — \U0001F4E6 **Smaller standard image.** The image no longer carries a second copy
  of Python, two…"
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1283
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: dccffca104ef3e5ee94f8afdc3cd3e1c0cbf0f603cabb525ab47a62c79e501c0
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-09-21-2e2089
  comparison: ''
  date: '2026-09-21'
  description: 'Open WebUI — v0.11.4: 39 Developer Workflow changes'
  evidence:
  - quote: "\U0001F4E6 **Smaller standard image.** The image no longer carries a second
      copy of Python, two sets of fonts nothing ever loaded, packages nothing imports,
      or the tool that installed them, taking about 170 MB off a standard build. [#29731](https://github.com/open-webui/open-webui/pull/29731),
      [#29723](https://github.com/open-webui/open-webui/pull/29723), [#29725](https://github.com/open-webui/open-webui/pull/29725),
      [#29726](https://github.com/open-webui/open-webui/pull/29726), [#29728](https://github.com/open-webui/open-webui/pull/29728),
      [Commit](https://github.com/open-webui/open-webui/commit/91f8775b28b52c9ae7f2ab990cf2490bda8055d6),
      [Commit](https://github.com/open-webui/open-webui/commit/98fcb844e1b19f7dd6289af26273cdec5447dc52),
      [Commit](https://github.com/open-webui/open-webui/commit/508de20779168003e538bb936b49a31d4a8fb8bb),
      [Commit](https://github.com/open-webui/open-webui/commit/a1c02098aa2687c72482a59117efe643b785df51)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F9D1\U0001F4BB **Skills from a terminal.** Skills a connected terminal
      server offers now sit beside workspace skills everywhere skills are picked —
      the \"$\" and \"/\" menus, the integrations menu and the skills panel, each
      marked Terminal — and are used the same way: picking one puts its instructions,
      its folder and the files it ships with in front of the model, and a model that
      was only told a skill exists can open it itself. They follow whichever terminal
      is selected and clear when that changes. [Commit](https://github.com/open-webui/open-webui/commit/e69236bccb1e12d14045b09b76ebac0490014851)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F4D4 **Terminal instructions file.** A model working with a terminal
      is now handed the AGENTS.md sitting in that terminal's home directory, read
      afresh at the start of every turn, so the instructions you keep beside your
      work reach the model without being pasted in. [Commit](https://github.com/open-webui/open-webui/commit/946be432375057dc18dbcc7c3513feb322a83a4b),
      [Commit](https://github.com/open-webui/open-webui/commit/f6922a4c4293449805938c80fbe54174994a1fc6)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F4D3 **Skill creation from a chat.** Typing \"/skills:create\" in
      a chat that already has content, with a terminal selected, turns the workflow
      you just went through into a reusable skill written to \".agents/skills\" under
      that terminal's root working directory rather than whatever folder the shell
      happens to sit in, and authored to Open WebUI's skill standards. [Commit](https://github.com/open-webui/open-webui/commit/113c56fc8c1986359556107a20e206159ca32f59),
      [Commit](https://github.com/open-webui/open-webui/commit/924a4a10fbd0be508a69faf66bf08ac9761bc24d),
      [Commit](https://github.com/open-webui/open-webui/commit/58078ab3045cc7aee409d9215f68adf0e02c9165),
      [Commit](https://github.com/open-webui/open-webui/commit/d25f6c7135e0aee93dc2c840ce320d97617a6e47),
      [Commit](https://github.com/open-webui/open-webui/commit/a096961a31499be23890b98a040ecf2917405568)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F5A5️ **Terminal tabs per command.** The terminal pane now carries
      a tab for each command a model is running alongside your own shell, so you can
      watch them as they go, move between them and take the shell yourself, each tab
      opening with the command that produced it. Opening the pane puts you in a tab,
      starting your shell where nothing else is running, and closing the last tab
      folds the pane away again. [Commit](https://github.com/open-webui/open-webui/commit/54a7a7a7ce22725074c29c7e827446f5dce1421c),
      [Commit](https://github.com/open-webui/open-webui/commit/f3eade42aead0a3b96ada3a300d6c294c89f74a8),
      [Commit](https://github.com/open-webui/open-webui/commit/de1203f9b5d3d8b2a84bf5c89d1c61542469367a),
      [Commit](https://github.com/open-webui/open-webui/commit/675b9839f17df94f866c871cbdb9881323a18a8a)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F4C2 **Folder uploads to terminals.** The file browser beside a
      terminal takes a folder now, dropped onto it or picked from the Upload Folder
      entry in its menus, and rebuilds what is inside it as it goes, subfolders and
      all, where before a drop uploaded only the files sitting loose at the top. [Commit](https://github.com/open-webui/open-webui/commit/f80ef8bd001d7ef650fb278d6fbd05bea4afad0f),
      [Commit](https://github.com/open-webui/open-webui/commit/4cc0d48b4d83503199bcc5f2322881722971a499),
      [Commit](https://github.com/open-webui/open-webui/commit/674760bfc1122e0a19fe299e05a86d1cbb528e6f)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: ⚖️ **Side-by-side file comparison.** Picking two files in the file browser
      lights up a Compare button that lays them side by side or one above the other,
      numbering the lines, marking what was added and removed down to the part of
      the line that changed, counting both, and letting you swap which is which or
      leave whitespace out of it, a choice it remembers; a terminal too old to offer
      the comparison says so rather than failing quietly. [Commit](https://github.com/open-webui/open-webui/commit/8556033c6b64fa53e44152ebab1f889a578529af),
      [Commit](https://github.com/open-webui/open-webui/commit/3808eace6c2beb1904f0f04fdd443ec544f94acb)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F9F1 **In-place streaming appends.** Streamed replies can be assembled
      with CPython's in-place string append, turned on with \"ENABLE_CHAT_RESPONSE_STREAM_INPLACE_APPEND\"
      and left off by default while it is rolled out gradually. [Commit](https://github.com/open-webui/open-webui/commit/113c56fc8c1986359556107a20e206159ca32f59),
      [Commit](https://github.com/open-webui/open-webui/commit/924a4a10fbd0be508a69faf66bf08ac9761bc24d),
      [#30066](https://github.com/open-webui/open-webui/pull/30066)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F6AA **Signing out ends the session.** Signing out or having every
      token revoked left any live connection that account already had in place, and
      those are now cut at the same moment; a token already revoked can no longer
      be replayed to cut someone else's newer session. [Commit](https://github.com/open-webui/open-webui/commit/3a6d0fd203050401481bdb8621b827089d393817)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F333 **Knowledge directories stay inside their base.** A directory
      id supplied to the knowledge file routes is now refused where it belongs to
      a different knowledge base, where a caller-supplied id could reach into a directory
      tree outside the one being addressed. [Commit](https://github.com/open-webui/open-webui/commit/a9541c18ca2a056f4ccfe56b9c733cba74b86b49),
      [#29887](https://github.com/open-webui/open-webui/pull/29887)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F36A **Cookie forwarding scope.** A connection authenticating as
      the signed-in person is handed this instance's browser cookies only where its
      new Forward cookies switch is on, which an instance relying on it has to turn
      on after upgrading. [Commit](https://github.com/open-webui/open-webui/commit/b71744b17823f7a3a9a64cb363e79a7164ed5b23),
      [Commit](https://github.com/open-webui/open-webui/commit/3cda47cdb449aac970426f0929c9e5f8bb8bd807),
      [Commit](https://github.com/open-webui/open-webui/commit/f9f815c86220f809fad5ee1300c44f55dea74c79)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F5DD️ **Revocation list fallback.** Where the revocation list is
      kept in Redis and Redis cannot be reached, a token is now accepted rather than
      the request failing, so signing out may not take effect until Redis is back.
      [Commit](https://github.com/open-webui/open-webui/commit/c1615bec2f5f143084b5fcc04f42ebfa0dade9df),
      [Commit](https://github.com/open-webui/open-webui/commit/6a85abb3f5e002f3069007213e16e4ef60776890)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F4CB **Note paste placement.** A plain paste replaced more of the
      note than was selected, and a paste into a code block broke out of the block
      instead of going inside it; both now land exactly where they were dropped. [Commit](https://github.com/open-webui/open-webui/commit/d8f27e745bd31c89efa25cbe0f41bb0f70576fc5)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F9E9 **Tool steps in finished replies.** A reply that called tools
      showed each step as it ran, then lost them the moment the reply completed, because
      the provider's closing message replaced everything on screen rather than joining
      it; the closing message is now merged into what is already there, and a tool
      call is no longer mistaken for its own result. [Commit](https://github.com/open-webui/open-webui/commit/e1bfefdf9f8f2012cecfc7d81079bd6fff147932),
      [Commit](https://github.com/open-webui/open-webui/commit/31b272d3c93b87636c920f2aa68d6caaa07ae79a)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F9ED **Streamed replies follow along.** A reply arriving over the
      response events now keeps the view at the bottom as it is written, as replies
      on the older path already did, unless you have scrolled up yourself. [Commit](https://github.com/open-webui/open-webui/commit/dfde08aa7391d924359b27f5768411d7a533a6ec),
      [Commit](https://github.com/open-webui/open-webui/commit/88e78b7819b28ffe91f3dff24d8c5d992004197e)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: ⚠️ **Failed settings feedback.** Settings that could not be saved were
      shown as saved anyway until the page was reloaded, because the interface stored
      them locally without waiting on the server; a failure now raises an error and
      leaves the panel as it was. [Commit](https://github.com/open-webui/open-webui/commit/98a920168e2eea435ac15e1ad3d679946631e41d)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F532 **Shift-click file selection.** Shift-clicking a file in the
      terminal's file browser now adds that range to what is already selected, and
      clicking through a selected file removes its range. [Commit](https://github.com/open-webui/open-webui/commit/f80ef8bd001d7ef650fb278d6fbd05bea4afad0f),
      [Commit](https://github.com/open-webui/open-webui/commit/4cc0d48b4d83503199bcc5f2322881722971a499),
      [Commit](https://github.com/open-webui/open-webui/commit/674760bfc1122e0a19fe299e05a86d1cbb528e6f)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F6DF **Attachment name collisions.** Attaching a file to a message
      on an instance that puts attachments in a terminal's working directory replaced
      whatever file of that name was sitting there; the upload now takes the next
      free name, \"report (1).pdf\" beside \"report.pdf\", and the attachment shows
      the name it was saved under, though two uploads arriving at the same moment
      from different browsers can still land on the same name. [Commit](https://github.com/open-webui/open-webui/commit/d70053e44993f271d534fb87d2b40724b028fca2)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F4DB **Failed upload feedback.** A file that could not be written
      to the terminal now says so, rather than passing in silence while the browser
      refreshed as though it had arrived. [Commit](https://github.com/open-webui/open-webui/commit/f80ef8bd001d7ef650fb278d6fbd05bea4afad0f),
      [Commit](https://github.com/open-webui/open-webui/commit/4cc0d48b4d83503199bcc5f2322881722971a499),
      [Commit](https://github.com/open-webui/open-webui/commit/674760bfc1122e0a19fe299e05a86d1cbb528e6f)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F3AF **Prefilled question timing.** Opening a chat from a link holding
      a question sent it before the box had it, so a question naming a variable went
      off with the variable unfilled; the send now waits for the text to be in place
      and filled in. [Commit](https://github.com/open-webui/open-webui/commit/3808eace6c2beb1904f0f04fdd443ec544f94acb),
      [Commit](https://github.com/open-webui/open-webui/commit/a23b579233276e40159eb615917b9aeb7d5ed5c9)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F570️ **Temporary chat links.** A link carrying the temporary chat
      marker opened an ordinary chat, because the marker was written into the address
      but never read back when the page loaded, and such a link now opens the temporary
      chat it promises. [Commit](https://github.com/open-webui/open-webui/commit/67adde31936d1d2e656140f9edd898b1fbb18a1c)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F4E8 **Duplicated proxy headers.** A reply proxied from a terminal
      server or an OpenAI or Ollama connection no longer carries that server's own
      \"Server\" and \"Date\" headers, which had a reverse proxy in front logging
      a duplicate line for every one. [#29841](https://github.com/open-webui/open-webui/pull/29841),
      [#29824](https://github.com/open-webui/open-webui/issues/29824), [#29843](https://github.com/open-webui/open-webui/pull/29843)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F465 **Directory updates that were dropped.** A change your identity
      provider sent as an add or a remove, or without naming the attribute it was
      changing, was accepted and then quietly discarded, so a rename or a deactivation
      never reached the account; those now take effect. [Commit](https://github.com/open-webui/open-webui/commit/ad9da981680c0fd9151c803a366a01545ea907c1)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F5C3️ **Directory request validation.** A provisioning request carrying
      the wrong kind of value, or an attribute Open WebUI does not support, now comes
      back as an error instead of passing in silence, and a sync that changes nothing
      no longer marks the account as touched. [Commit](https://github.com/open-webui/open-webui/commit/ad9da981680c0fd9151c803a366a01545ea907c1)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F980 **Regex searches over chat and knowledge files.** A pattern
      search now runs in time proportional to the text whatever the pattern, where
      a nasty expression could stall the search for good, and the patterns it accepts
      follow RE2's rules, with no lookarounds or backreferences and character classes
      matching ASCII only. [Commit](https://github.com/open-webui/open-webui/commit/97e013a66169c4fcd7f26ab9e41a4ff260ffd4da)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F50C **Terminal tools need a terminal.** A model was offered the
      tools that read your terminal and type into it whether or not the chat had a
      terminal switched on and connected in your browser, so it could reach for one
      that was not there; those tools are now handed over only for the terminal the
      chat has open. [Commit](https://github.com/open-webui/open-webui/commit/ca1eefe2937081b010ffef3985997d17d3332fa3),
      [Commit](https://github.com/open-webui/open-webui/commit/1ddba7e2c6f625fbc2c131eb24d3b9775ad898ad)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F524 **Custom header encoding.** The custom headers a connection
      sends are encoded once the values are filled in, so a person's name or group
      carrying anything beyond plain ASCII, a line break included, no longer breaks
      the request or reaches the other end as something else. [Commit](https://github.com/open-webui/open-webui/commit/7a4a4b93dca34f8ce0c481b180d3eea23797e984)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F6A7 **Terminal proxy restrictions.** Requests passed through to
      a terminal server are now refused where they aim at that server's administrative
      endpoints, are not followed on to somewhere else, and are turned away where
      the path carries characters a parser would rewrite. [Commit](https://github.com/open-webui/open-webui/commit/51bb8cb142f72503e861eeee25ae4dc73c26c36b)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F4E1 **Broken stream reporting.** Where something failed part way
      through streaming an answer out of \"/api/chat/completions\", the stream simply
      stopped, leaving a client waiting on an answer that would never finish; it now
      closes with an error and a proper end of stream. [Commit](https://github.com/open-webui/open-webui/commit/c0fb36c9b833a85a3a7364e195cf54f3d6c7a787)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F4ED **Empty page uploads.** Adding a web address to a knowledge
      base that came back without any text failed with a bare \"Error uploading file\"
      and, where the upload itself was refused, left the row sitting in the list;
      the reason now reaches you as it was given, and the row is taken away. [Commit](https://github.com/open-webui/open-webui/commit/6786ae1797eadaad7464a147213790e2d272822b)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F3D7️ **Terminal server save button.** Saving a terminal server
      now waits for the save to finish before the dialog closes and cannot be set
      off twice by a second click. [Commit](https://github.com/open-webui/open-webui/commit/1cdd7aa459d6e96905324b452600ff56369d8a4e)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F5FA️ **Terminal file panel paths.** The file panel beside a terminal
      now opens the file a model just wrote even when it is named with a relative
      path, where the panel could not match the name, jumped to the root and dragged
      the session's working directory with it. [#30282](https://github.com/open-webui/open-webui/pull/30282),
      [#30051](https://github.com/open-webui/open-webui/issues/30051)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F6F0️ **Direct connections across workers.** A reply streamed over
      a direct connection no longer goes quiet part way through where several servers
      share their websocket traffic through Redis; the events it lives on now travel
      between workers the way the rest already did. [Commit](https://github.com/open-webui/open-webui/commit/0180efecf362d487e0c30f040f5948c325fbe337)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F516 **Visible title generation faults.** When a new chat's automatic
      title cannot be generated, the reason now reaches the log at the default level,
      rather than only under debug logging where a broken feature looked the same
      as a switched-off one. [#30106](https://github.com/open-webui/open-webui/pull/30106),
      [#29533](https://github.com/open-webui/open-webui/issues/29533)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F5C4️ **Slim database support.** The slim image runs on SQLite,
      its default, or on PostgreSQL; pointed at MySQL, MariaDB or another engine,
      or started with AWS RDS IAM logins switched on, it stops with an error instead
      of starting, and those deployments need the standard image. [Commit](https://github.com/open-webui/open-webui/commit/d27aa72ab4a7b5632b4ad49e8467081ad3d7ebb4)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F4C1 **Slim file storage.** The slim image keeps files on local
      storage, its default; configured for an S3, Google Cloud or Azure bucket, it
      stops with an error instead of starting, and those deployments need the standard
      image. [Commit](https://github.com/open-webui/open-webui/commit/d27aa72ab4a7b5632b4ad49e8467081ad3d7ebb4)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F9EE **Slim searches only through pgvector.** Knowledge search on
      the slim image needs PostgreSQL with pgvector, and configured for another vector
      store the instance still starts, and the failure arrives the first time something
      is searched rather than at startup. [Commit](https://github.com/open-webui/open-webui/commit/cb942bb94c8dc7941336088fb3392e2398ff56c1),
      [Commit](https://github.com/open-webui/open-webui/commit/d27aa72ab4a7b5632b4ad49e8467081ad3d7ebb4)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F578️ **Slim web page fetching.** The slim image carries no headless
      browser, so a web page is fetched over plain HTTP or through an external loader,
      and a page that draws itself with JavaScript comes back with less of its content
      than on the standard image. [Commit](https://github.com/open-webui/open-webui/commit/cb942bb94c8dc7941336088fb3392e2398ff56c1),
      [Commit](https://github.com/open-webui/open-webui/commit/d27aa72ab4a7b5632b4ad49e8467081ad3d7ebb4)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  - quote: "\U0001F9F0 **Slim git requirements.** The slim image no longer carries
      git, so a tool or function whose requirements point at a \"git+https://\" address
      fails to install and needs the standard image or a published package. [Commit](https://github.com/open-webui/open-webui/commit/30eed1251301f74e0dfeaad09c41e81320f790fc)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 39-developer-workflow-changes-in-v0-11-4
  source_release: open-webui-2026-09-21-v0-11-4-github-393232555-90de9130
  source_type: github_releases
  theme: developer-workflow
  title: 39 Developer Workflow changes in v0.11.4
  type: change
related_changes:
- '[[Changes/GitHub Copilot CLI/2026-09-17-the-status-row-now-says-it-is-waiting-for-background-shells-instead-of-working-w|The
  status row now says it is waiting for background shells, instead…]]'
- '[[Changes/Claude Code/2026-09-18-improved-ultrareview-when-there-s-nothing-to-review-messages-say-which-case-you|Improved
  /ultrareview when there''s nothing to review]]'
- '[[Changes/GitHub Copilot CLI/2026-09-21-5-developer-workflow-changes-in-v1-0-87|5
  Developer Workflow changes in v1.0.87]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-09-21-v0-11-4-github-393232555-90de9130|open-webui-2026-09-21-v0-11-4-github-393232555-90de9130]]'
source_type: github_releases
theme: developer-workflow
title: 39 Developer Workflow changes in v0.11.4
type: change
---

<!-- chronolog:begin region="header" -->
# 39 Developer Workflow changes in v0.11.4

**Open WebUI** · 2026-09-21 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.11.4) · from [[Releases/Open WebUI/open-webui-2026-09-21-v0-11-4-github-393232555-90de9130|v0.11.4]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 📦 **Smaller standard image.** The image no longer carries a second copy of Python, two sets of fonts nothing ever loaded, packages nothing imports, or the tool that installed them, taking about 170 MB off a standard build. [#29731](https://github.com/open-webui/open-webui/pull/29731), [#29723](https://github.com/open-webui/open-webui/pull/29723), [#29725](https://github.com/open-webui/open-webui/pull/29725), [#29726](https://github.com/open-webui/open-webui/pull/29726), [#29728](https://github.com/open-webui/open-webui/pull/29728), [Commit](https://github.com/open-webui/open-webui/commit/91f8775b28b52c9ae7f2ab990cf2490bda8055d6), [Commit](https://github.com/open-webui/open-webui/commit/98fcb844e1b19f7dd6289af26273cdec5447dc52), [Commit](https://github.com/open-webui/open-webui/commit/508de20779168003e538bb936b49a31d4a8fb8bb), [Commit](https://github.com/open-webui/open-webui/commit/a1c02098aa2687c72482a59117efe643b785df51)

> 🧑💻 **Skills from a terminal.** Skills a connected terminal server offers now sit beside workspace skills everywhere skills are picked — the "$" and "/" menus, the integrations menu and the skills panel, each marked Terminal — and are used the same way: picking one puts its instructions, its folder and the files it ships with in front of the model, and a model that was only told a skill exists can open it itself. They follow whichever terminal is selected and clear when that changes. [Commit](https://github.com/open-webui/open-webui/commit/e69236bccb1e12d14045b09b76ebac0490014851)

> 📔 **Terminal instructions file.** A model working with a terminal is now handed the AGENTS.md sitting in that terminal's home directory, read afresh at the start of every turn, so the instructions you keep beside your work reach the model without being pasted in. [Commit](https://github.com/open-webui/open-webui/commit/946be432375057dc18dbcc7c3513feb322a83a4b), [Commit](https://github.com/open-webui/open-webui/commit/f6922a4c4293449805938c80fbe54174994a1fc6)

> 📓 **Skill creation from a chat.** Typing "/skills:create" in a chat that already has content, with a terminal selected, turns the workflow you just went through into a reusable skill written to ".agents/skills" under that terminal's root working directory rather than whatever folder the shell happens to sit in, and authored to Open WebUI's skill standards. [Commit](https://github.com/open-webui/open-webui/commit/113c56fc8c1986359556107a20e206159ca32f59), [Commit](https://github.com/open-webui/open-webui/commit/924a4a10fbd0be508a69faf66bf08ac9761bc24d), [Commit](https://github.com/open-webui/open-webui/commit/58078ab3045cc7aee409d9215f68adf0e02c9165), [Commit](https://github.com/open-webui/open-webui/commit/d25f6c7135e0aee93dc2c840ce320d97617a6e47), [Commit](https://github.com/open-webui/open-webui/commit/a096961a31499be23890b98a040ecf2917405568)

> 🖥️ **Terminal tabs per command.** The terminal pane now carries a tab for each command a model is running alongside your own shell, so you can watch them as they go, move between them and take the shell yourself, each tab opening with the command that produced it. Opening the pane puts you in a tab, starting your shell where nothing else is running, and closing the last tab folds the pane away again. [Commit](https://github.com/open-webui/open-webui/commit/54a7a7a7ce22725074c29c7e827446f5dce1421c), [Commit](https://github.com/open-webui/open-webui/commit/f3eade42aead0a3b96ada3a300d6c294c89f74a8), [Commit](https://github.com/open-webui/open-webui/commit/de1203f9b5d3d8b2a84bf5c89d1c61542469367a), [Commit](https://github.com/open-webui/open-webui/commit/675b9839f17df94f866c871cbdb9881323a18a8a)

> 📂 **Folder uploads to terminals.** The file browser beside a terminal takes a folder now, dropped onto it or picked from the Upload Folder entry in its menus, and rebuilds what is inside it as it goes, subfolders and all, where before a drop uploaded only the files sitting loose at the top. [Commit](https://github.com/open-webui/open-webui/commit/f80ef8bd001d7ef650fb278d6fbd05bea4afad0f), [Commit](https://github.com/open-webui/open-webui/commit/4cc0d48b4d83503199bcc5f2322881722971a499), [Commit](https://github.com/open-webui/open-webui/commit/674760bfc1122e0a19fe299e05a86d1cbb528e6f)

> ⚖️ **Side-by-side file comparison.** Picking two files in the file browser lights up a Compare button that lays them side by side or one above the other, numbering the lines, marking what was added and removed down to the part of the line that changed, counting both, and letting you swap which is which or leave whitespace out of it, a choice it remembers; a terminal too old to offer the comparison says so rather than failing quietly. [Commit](https://github.com/open-webui/open-webui/commit/8556033c6b64fa53e44152ebab1f889a578529af), [Commit](https://github.com/open-webui/open-webui/commit/3808eace6c2beb1904f0f04fdd443ec544f94acb)

> 🧱 **In-place streaming appends.** Streamed replies can be assembled with CPython's in-place string append, turned on with "ENABLE_CHAT_RESPONSE_STREAM_INPLACE_APPEND" and left off by default while it is rolled out gradually. [Commit](https://github.com/open-webui/open-webui/commit/113c56fc8c1986359556107a20e206159ca32f59), [Commit](https://github.com/open-webui/open-webui/commit/924a4a10fbd0be508a69faf66bf08ac9761bc24d), [#30066](https://github.com/open-webui/open-webui/pull/30066)

> 🚪 **Signing out ends the session.** Signing out or having every token revoked left any live connection that account already had in place, and those are now cut at the same moment; a token already revoked can no longer be replayed to cut someone else's newer session. [Commit](https://github.com/open-webui/open-webui/commit/3a6d0fd203050401481bdb8621b827089d393817)

> 🌳 **Knowledge directories stay inside their base.** A directory id supplied to the knowledge file routes is now refused where it belongs to a different knowledge base, where a caller-supplied id could reach into a directory tree outside the one being addressed. [Commit](https://github.com/open-webui/open-webui/commit/a9541c18ca2a056f4ccfe56b9c733cba74b86b49), [#29887](https://github.com/open-webui/open-webui/pull/29887)

> 🍪 **Cookie forwarding scope.** A connection authenticating as the signed-in person is handed this instance's browser cookies only where its new Forward cookies switch is on, which an instance relying on it has to turn on after upgrading. [Commit](https://github.com/open-webui/open-webui/commit/b71744b17823f7a3a9a64cb363e79a7164ed5b23), [Commit](https://github.com/open-webui/open-webui/commit/3cda47cdb449aac970426f0929c9e5f8bb8bd807), [Commit](https://github.com/open-webui/open-webui/commit/f9f815c86220f809fad5ee1300c44f55dea74c79)

> 🗝️ **Revocation list fallback.** Where the revocation list is kept in Redis and Redis cannot be reached, a token is now accepted rather than the request failing, so signing out may not take effect until Redis is back. [Commit](https://github.com/open-webui/open-webui/commit/c1615bec2f5f143084b5fcc04f42ebfa0dade9df), [Commit](https://github.com/open-webui/open-webui/commit/6a85abb3f5e002f3069007213e16e4ef60776890)

> 📋 **Note paste placement.** A plain paste replaced more of the note than was selected, and a paste into a code block broke out of the block instead of going inside it; both now land exactly where they were dropped. [Commit](https://github.com/open-webui/open-webui/commit/d8f27e745bd31c89efa25cbe0f41bb0f70576fc5)

> 🧩 **Tool steps in finished replies.** A reply that called tools showed each step as it ran, then lost them the moment the reply completed, because the provider's closing message replaced everything on screen rather than joining it; the closing message is now merged into what is already there, and a tool call is no longer mistaken for its own result. [Commit](https://github.com/open-webui/open-webui/commit/e1bfefdf9f8f2012cecfc7d81079bd6fff147932), [Commit](https://github.com/open-webui/open-webui/commit/31b272d3c93b87636c920f2aa68d6caaa07ae79a)

> 🧭 **Streamed replies follow along.** A reply arriving over the response events now keeps the view at the bottom as it is written, as replies on the older path already did, unless you have scrolled up yourself. [Commit](https://github.com/open-webui/open-webui/commit/dfde08aa7391d924359b27f5768411d7a533a6ec), [Commit](https://github.com/open-webui/open-webui/commit/88e78b7819b28ffe91f3dff24d8c5d992004197e)

> ⚠️ **Failed settings feedback.** Settings that could not be saved were shown as saved anyway until the page was reloaded, because the interface stored them locally without waiting on the server; a failure now raises an error and leaves the panel as it was. [Commit](https://github.com/open-webui/open-webui/commit/98a920168e2eea435ac15e1ad3d679946631e41d)

> 🔲 **Shift-click file selection.** Shift-clicking a file in the terminal's file browser now adds that range to what is already selected, and clicking through a selected file removes its range. [Commit](https://github.com/open-webui/open-webui/commit/f80ef8bd001d7ef650fb278d6fbd05bea4afad0f), [Commit](https://github.com/open-webui/open-webui/commit/4cc0d48b4d83503199bcc5f2322881722971a499), [Commit](https://github.com/open-webui/open-webui/commit/674760bfc1122e0a19fe299e05a86d1cbb528e6f)

> 🛟 **Attachment name collisions.** Attaching a file to a message on an instance that puts attachments in a terminal's working directory replaced whatever file of that name was sitting there; the upload now takes the next free name, "report (1).pdf" beside "report.pdf", and the attachment shows the name it was saved under, though two uploads arriving at the same moment from different browsers can still land on the same name. [Commit](https://github.com/open-webui/open-webui/commit/d70053e44993f271d534fb87d2b40724b028fca2)

> 📛 **Failed upload feedback.** A file that could not be written to the terminal now says so, rather than passing in silence while the browser refreshed as though it had arrived. [Commit](https://github.com/open-webui/open-webui/commit/f80ef8bd001d7ef650fb278d6fbd05bea4afad0f), [Commit](https://github.com/open-webui/open-webui/commit/4cc0d48b4d83503199bcc5f2322881722971a499), [Commit](https://github.com/open-webui/open-webui/commit/674760bfc1122e0a19fe299e05a86d1cbb528e6f)

> 🎯 **Prefilled question timing.** Opening a chat from a link holding a question sent it before the box had it, so a question naming a variable went off with the variable unfilled; the send now waits for the text to be in place and filled in. [Commit](https://github.com/open-webui/open-webui/commit/3808eace6c2beb1904f0f04fdd443ec544f94acb), [Commit](https://github.com/open-webui/open-webui/commit/a23b579233276e40159eb615917b9aeb7d5ed5c9)

> 🕰️ **Temporary chat links.** A link carrying the temporary chat marker opened an ordinary chat, because the marker was written into the address but never read back when the page loaded, and such a link now opens the temporary chat it promises. [Commit](https://github.com/open-webui/open-webui/commit/67adde31936d1d2e656140f9edd898b1fbb18a1c)

> 📨 **Duplicated proxy headers.** A reply proxied from a terminal server or an OpenAI or Ollama connection no longer carries that server's own "Server" and "Date" headers, which had a reverse proxy in front logging a duplicate line for every one. [#29841](https://github.com/open-webui/open-webui/pull/29841), [#29824](https://github.com/open-webui/open-webui/issues/29824), [#29843](https://github.com/open-webui/open-webui/pull/29843)

> 👥 **Directory updates that were dropped.** A change your identity provider sent as an add or a remove, or without naming the attribute it was changing, was accepted and then quietly discarded, so a rename or a deactivation never reached the account; those now take effect. [Commit](https://github.com/open-webui/open-webui/commit/ad9da981680c0fd9151c803a366a01545ea907c1)

> 🗃️ **Directory request validation.** A provisioning request carrying the wrong kind of value, or an attribute Open WebUI does not support, now comes back as an error instead of passing in silence, and a sync that changes nothing no longer marks the account as touched. [Commit](https://github.com/open-webui/open-webui/commit/ad9da981680c0fd9151c803a366a01545ea907c1)

> 🦀 **Regex searches over chat and knowledge files.** A pattern search now runs in time proportional to the text whatever the pattern, where a nasty expression could stall the search for good, and the patterns it accepts follow RE2's rules, with no lookarounds or backreferences and character classes matching ASCII only. [Commit](https://github.com/open-webui/open-webui/commit/97e013a66169c4fcd7f26ab9e41a4ff260ffd4da)

> 🔌 **Terminal tools need a terminal.** A model was offered the tools that read your terminal and type into it whether or not the chat had a terminal switched on and connected in your browser, so it could reach for one that was not there; those tools are now handed over only for the terminal the chat has open. [Commit](https://github.com/open-webui/open-webui/commit/ca1eefe2937081b010ffef3985997d17d3332fa3), [Commit](https://github.com/open-webui/open-webui/commit/1ddba7e2c6f625fbc2c131eb24d3b9775ad898ad)

> 🔤 **Custom header encoding.** The custom headers a connection sends are encoded once the values are filled in, so a person's name or group carrying anything beyond plain ASCII, a line break included, no longer breaks the request or reaches the other end as something else. [Commit](https://github.com/open-webui/open-webui/commit/7a4a4b93dca34f8ce0c481b180d3eea23797e984)

> 🚧 **Terminal proxy restrictions.** Requests passed through to a terminal server are now refused where they aim at that server's administrative endpoints, are not followed on to somewhere else, and are turned away where the path carries characters a parser would rewrite. [Commit](https://github.com/open-webui/open-webui/commit/51bb8cb142f72503e861eeee25ae4dc73c26c36b)

> 📡 **Broken stream reporting.** Where something failed part way through streaming an answer out of "/api/chat/completions", the stream simply stopped, leaving a client waiting on an answer that would never finish; it now closes with an error and a proper end of stream. [Commit](https://github.com/open-webui/open-webui/commit/c0fb36c9b833a85a3a7364e195cf54f3d6c7a787)

> 📭 **Empty page uploads.** Adding a web address to a knowledge base that came back without any text failed with a bare "Error uploading file" and, where the upload itself was refused, left the row sitting in the list; the reason now reaches you as it was given, and the row is taken away. [Commit](https://github.com/open-webui/open-webui/commit/6786ae1797eadaad7464a147213790e2d272822b)

> 🏗️ **Terminal server save button.** Saving a terminal server now waits for the save to finish before the dialog closes and cannot be set off twice by a second click. [Commit](https://github.com/open-webui/open-webui/commit/1cdd7aa459d6e96905324b452600ff56369d8a4e)

> 🗺️ **Terminal file panel paths.** The file panel beside a terminal now opens the file a model just wrote even when it is named with a relative path, where the panel could not match the name, jumped to the root and dragged the session's working directory with it. [#30282](https://github.com/open-webui/open-webui/pull/30282), [#30051](https://github.com/open-webui/open-webui/issues/30051)

> 🛰️ **Direct connections across workers.** A reply streamed over a direct connection no longer goes quiet part way through where several servers share their websocket traffic through Redis; the events it lives on now travel between workers the way the rest already did. [Commit](https://github.com/open-webui/open-webui/commit/0180efecf362d487e0c30f040f5948c325fbe337)

> 🔖 **Visible title generation faults.** When a new chat's automatic title cannot be generated, the reason now reaches the log at the default level, rather than only under debug logging where a broken feature looked the same as a switched-off one. [#30106](https://github.com/open-webui/open-webui/pull/30106), [#29533](https://github.com/open-webui/open-webui/issues/29533)

> 🗄️ **Slim database support.** The slim image runs on SQLite, its default, or on PostgreSQL; pointed at MySQL, MariaDB or another engine, or started with AWS RDS IAM logins switched on, it stops with an error instead of starting, and those deployments need the standard image. [Commit](https://github.com/open-webui/open-webui/commit/d27aa72ab4a7b5632b4ad49e8467081ad3d7ebb4)

> 📁 **Slim file storage.** The slim image keeps files on local storage, its default; configured for an S3, Google Cloud or Azure bucket, it stops with an error instead of starting, and those deployments need the standard image. [Commit](https://github.com/open-webui/open-webui/commit/d27aa72ab4a7b5632b4ad49e8467081ad3d7ebb4)

> 🧮 **Slim searches only through pgvector.** Knowledge search on the slim image needs PostgreSQL with pgvector, and configured for another vector store the instance still starts, and the failure arrives the first time something is searched rather than at startup. [Commit](https://github.com/open-webui/open-webui/commit/cb942bb94c8dc7941336088fb3392e2398ff56c1), [Commit](https://github.com/open-webui/open-webui/commit/d27aa72ab4a7b5632b4ad49e8467081ad3d7ebb4)

> 🕸️ **Slim web page fetching.** The slim image carries no headless browser, so a web page is fetched over plain HTTP or through an external loader, and a page that draws itself with JavaScript comes back with less of its content than on the standard image. [Commit](https://github.com/open-webui/open-webui/commit/cb942bb94c8dc7941336088fb3392e2398ff56c1), [Commit](https://github.com/open-webui/open-webui/commit/d27aa72ab4a7b5632b4ad49e8467081ad3d7ebb4)

> 🧰 **Slim git requirements.** The slim image no longer carries git, so a tool or function whose requirements point at a "git+https://" address fails to install and needs the standard image or a published package. [Commit](https://github.com/open-webui/open-webui/commit/30eed1251301f74e0dfeaad09c41e81320f790fc)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.11.4
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-09-21-4-safety-and-privacy-changes-in-v0-11-4|4 Safety and Privacy changes in v0.11.4]] · Safety and Privacy
- [[Changes/Open WebUI/2026-09-21-3-context-window-changes-in-v0-11-4|3 Context Window changes in v0.11.4]] · Context Window
- [[Changes/Open WebUI/2026-09-21-general-improvements-various-improvements-were-implemented-across-the-applicatio|🔄 General improvements. Various improvements were implemented across…]] · Reliability and Performance
- [[Changes/Open WebUI/2026-09-21-6-account-and-access-changes-in-v0-11-4|6 Account and Access changes in v0.11.4]] · Account and Access
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
- [[Changes/Open WebUI/2026-09-21-41-model-support-changes-in-v0-11-4|41 Model Support changes in v0.11.4]] · Model Support
- [[Changes/Open WebUI/2026-09-21-5-enterprise-and-administration-changes-in-v0-11-4|5 Enterprise and Administration changes in v0.11.4]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-09-21-61-other-changes-in-v0-11-4|61 other changes in v0.11.4]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-09-21 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-09-21-5-developer-workflow-changes-in-v1-0-87|5 Developer Workflow changes in v1.0.87]]
- Later: 2026-09-22 · Claude Code · [[Changes/Claude Code/2026-09-22-3-developer-workflow-changes-in-v2-1-280|3 Developer Workflow changes in v2.1.280]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-18 · Cursor · [[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-09-21-2e2089&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-09-21-39-developer-workflow-changes-in-v0-11-4.md%0ACard%20ID%3A%20open-webui-2026-09-21-2e2089%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.11.4%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->