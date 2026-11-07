---
card_id: open-webui-2026-06-29-ddb1f1
date: '2026-06-29'
description: "Open WebUI · 2026-06-29 · Developer Workflow: 42 changes in v0.10.0
  — \U0001F5A5️ **Open WebUI Computer agent support.** Open WebUI can now connect
  to Open WebUI…"
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1199
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: developer-workflow
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 5532846adca4f2e65b9519dd2f3301f319e5a6c0cacd7dbe0c414482750a628b
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2026-06-29-ddb1f1
  comparison: ''
  date: '2026-06-29'
  description: 'Open WebUI — v0.10.0: 42 Developer Workflow changes'
  evidence:
  - quote: "\U0001F5A5️ **Open WebUI Computer agent support.** Open WebUI can now
      connect to Open WebUI Computer through its OpenAI-compatible gateway, letting
      chats run full agent sessions on your own machine with file, terminal, git,
      and web access. [GitHub](https://github.com/open-webui/computer)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F5C2️ **External knowledge bases.** Knowledge bases can now be backed
      by an external retrieval source through configurable external knowledge connections,
      so you can search an existing external system from chat instead of only Open
      WebUI's built-in store. [Commit](https://github.com/open-webui/open-webui/commit/15c7e374384488effc3d6059d09b3a8aa79c618d)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F514 **New event system with webhooks.** Open WebUI now emits events
      for a wide range of system activity — sign-ins, configuration changes, startup,
      and actions across chats, knowledge, files, and more. Administrators can send
      these as outbound webhooks, route them to specific users or groups, and manage
      which events go where from a new event settings admin page. [Commit](https://github.com/open-webui/open-webui/commit/b5c43968db0ea1556b228d143ae5946dc4e944ba),
      [Commit](https://github.com/open-webui/open-webui/commit/745396867888718289a2dfcf0809b3e162e00629),
      [Commit](https://github.com/open-webui/open-webui/commit/5576e6ed8a80a4032b7c6cb3ee0cda0254019355),
      [Commit](https://github.com/open-webui/open-webui/commit/7b55a63fc7ee323e9114713ce1d2f3f688aa37e6),
      [Commit](https://github.com/open-webui/open-webui/commit/1a8e1a993928a28b9d814c77b2aef0361b630f27),
      [Commit](https://github.com/open-webui/open-webui/commit/ede39d82de05eeb7591329679c8cab97753e5ff0),
      [Commit](https://github.com/open-webui/open-webui/commit/8f890f0b43aed3d42b9e3d954e25e54e37d526d0),
      [Commit](https://github.com/open-webui/open-webui/commit/741b64edb6c2ff04c4b787528cfca1c5b66a1a27),
      [Commit](https://github.com/open-webui/open-webui/commit/303c426c3fffafc2369205021a82659ee8715a85),
      [#1240](https://github.com/open-webui/open-webui/issues/1240), [#16426](https://github.com/open-webui/open-webui/pull/16426)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F3F7️ **More custom header variables.** Custom request headers now
      support \"{{USER_MESSAGE_ID}}\", \"{{USER_MESSAGE_PARENT_ID}}\", and \"{{TASK}}\",
      letting connected services tell apart real user messages from automated background
      requests like title, tag, and follow-up generation. [Commit](https://github.com/open-webui/open-webui/commit/f85cb27ef835aa76aff7de6176bf2159ba392061)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: ⚡ **Faster model overview.** The admin model overview now loads its feedback
      history and tags through batched queries, so it opens noticeably faster on instances
      with many chats. [Commit](https://github.com/open-webui/open-webui/commit/40c09167cd6de1c853a5dd03c88b4fdcb279dfe1)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F3CE️ **Lighter channel profile previews.** Profile previews in
      channels now load a person's details only when you hover to open one, rather
      than fetching them for every message up front. [Commit](https://github.com/open-webui/open-webui/commit/4f69c33de0e9a8fde4f16d0b2f1ed8aac8741772)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F511 **Configurable secret key length.** The auto-generated secret
      key length can now be set with a new environment variable, instead of always
      using a fixed length. [Commit](https://github.com/open-webui/open-webui/commit/e473ab1231abedcb188c259b42ae7f2390739223),
      [#25906](https://github.com/open-webui/open-webui/pull/25906)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F510 **Argon2 password hashing option.** Password hashing can now
      use Argon2 through a configurable algorithm setting, removing the 72-byte password
      length limit that came with the previous default. [Commit](https://github.com/open-webui/open-webui/commit/33cd199e6dffddd4ee8974af41ebb894871d74c1),
      [Commit](https://github.com/open-webui/open-webui/commit/a70a6589afad0b429cdd77afa62163391f406a87),
      [#25656](https://github.com/open-webui/open-webui/pull/25656)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F510 **Optional encryption of valve values at rest.** Tool and function
      valve values can now be encrypted at rest through a new opt-in setting, with
      existing stored values migrated automatically, so sensitive settings like API
      keys aren't kept in plaintext. [Commit](https://github.com/open-webui/open-webui/commit/b4073f6378392b23a3954e33031bf5e1d98e090a),
      [#23721](https://github.com/open-webui/open-webui/pull/23721)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F9E9 **Filter Outlet Hook can now run on API requests and responses.**
      A filter function's outlet hook now runs for direct API callers, including streaming
      responses, so response post-processing isn't limited to the web interface; this
      is controlled by a new setting and on by default. [Commit](https://github.com/open-webui/open-webui/commit/390e200f76877b185002c88b4dda27b123d29e83),
      [#25650](https://github.com/open-webui/open-webui/pull/25650)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F4DD **Formatted valve descriptions.** Valve descriptions for tools
      and functions now render Markdown, so they can include formatting and links.
      [Commit](https://github.com/open-webui/open-webui/commit/7c0b0e42f5afb0e9c39bd2d42e4822d64d0c7b3e)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F53D **Dropdown inputs for valve options.** Valve and confirmation
      inputs can now present a set of options as a dropdown instead of free text,
      making fixed-choice settings easier to configure. [Commit](https://github.com/open-webui/open-webui/commit/422a4768ea7428b5dd6d401ccfba00e1e86eb98a),
      [#26278](https://github.com/open-webui/open-webui/pull/26278)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F4DC **Custom CA bundle for outbound connections.** A new environment
      variable lets you point Open WebUI at a custom CA certificate bundle, and the
      per-connection SSL settings now accept a bundle path, so deployments behind
      a corporate or internal CA can keep certificate verification on instead of disabling
      it. [Commit](https://github.com/open-webui/open-webui/commit/a54878b14f044d4aa1d8cf5be6f8ce9fc4285438),
      [Commit](https://github.com/open-webui/open-webui/commit/8b9e28b50354307a314111262f6737b6d8aa4685)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F5A5️ **More terminal server orchestrator controls.** Admins connecting
      an orchestrator terminal server can now configure session lifecycle policies
      and refresh or reset running terminal sessions, including targeting only idle
      ones, from the connection settings. [Commit](https://github.com/open-webui/open-webui/commit/7e8153e889a59afe4cf77261ea5e1ef5a66665f1)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: ⚡ **Leaner knowledge-file reading for agents.** The built-in tools that
      let a model read knowledge files now return output in bounded, paginated chunks
      with a default and a hard cap, instead of potentially returning an entire large
      file at once, sharply reducing token usage. [Commit](https://github.com/open-webui/open-webui/commit/a285a390c12e27e614d1ba9ffb92d1a0e49e7dfa),
      [#26139](https://github.com/open-webui/open-webui/issues/26139)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: ⚡ **Batched streaming updates.** Streaming responses now group small updates
      of the same type before sending them, reducing overhead during fast token streams
      and tool-call output. [Commit](https://github.com/open-webui/open-webui/commit/7240517807a8b0097065f7cbbb384d34084f90fd),
      [#26202](https://github.com/open-webui/open-webui/pull/26202)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F648 **Channel member lists no longer expose private data.** Viewing
      a channel's members now returns only basic profile details, instead of also
      exposing other members' settings, linked-account data, and personal information.
      [Commit](https://github.com/open-webui/open-webui/commit/fbcdcf146b99b5002705060a8243eee769108f9e)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F50C **Terminal connections can't be redirected to another user.**
      Terminal session identifiers are now safely encoded before being passed upstream,
      closing a way to tamper with the connection's user identity. [#26042](https://github.com/open-webui/open-webui/pull/26042)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F513 **Revoked sessions are rejected on real-time connections.**
      Real-time and terminal WebSocket connections now honor token revocation and
      expiry, so a signed-out or expired session can no longer keep a live connection
      open. [Commit](https://github.com/open-webui/open-webui/commit/33b91bd8ae8a100a5a306c91441a7d0b422c4cde),
      [#25764](https://github.com/open-webui/open-webui/pull/25764), [#25686](https://github.com/open-webui/open-webui/pull/25686)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F5C4️ **Unknown knowledge collections are denied by default.** Retrieval
      now rejects unknown or unscoped collection names by default, closing a legacy
      path that could be used to reach collections outside the normal access checks.
      [Commit](https://github.com/open-webui/open-webui/commit/d99ac7d3f83b25161ca775229150c8f7c74cceee)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F648 **Error responses no longer leak internals.** Server error
      responses now return sanitized messages instead of raw exception text, so internal
      details aren't exposed to signed-in users. [Commit](https://github.com/open-webui/open-webui/commit/ee5de69e374aabf5631da18a5bbc1c285ee6f7a1),
      [Commit](https://github.com/open-webui/open-webui/commit/0cc331d1c60341bb06b78ceeecfb2db86179c93e),
      [Commit](https://github.com/open-webui/open-webui/commit/396d9ac18193d43e40fb9d068075d4b780e971d7),
      [Commit](https://github.com/open-webui/open-webui/commit/0883638027a9b3cb7c9851f031c4f5fc1af1f25d),
      [#26375](https://github.com/open-webui/open-webui/pull/26375), [#26374](https://github.com/open-webui/open-webui/issues/26374)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F4CF **Upload size limit enforced on the server.** The maximum upload
      size is now enforced server-side, so it can't be bypassed by a client that ignores
      the limit. [Commit](https://github.com/open-webui/open-webui/commit/f8ec63203c4408c46bb06698ae624d17b01b9301),
      [Commit](https://github.com/open-webui/open-webui/commit/d3676b4f71bfdbaf4e4d76943c51117e18932ccf),
      [#25869](https://github.com/open-webui/open-webui/pull/25869)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F5C3️ **Prompt caching preserved over the Anthropic-compatible API.**
      Requests through the Anthropic-compatible API now keep their prompt-caching
      markers instead of having them stripped, so clients that rely on caching work
      as intended. [Commit](https://github.com/open-webui/open-webui/commit/caedcbae4988ef59ea7052b2a3198e2da4b5291a),
      [#25998](https://github.com/open-webui/open-webui/pull/25998), [#25964](https://github.com/open-webui/open-webui/discussions/25964)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F501 **Fewer redundant data loads.** Several views no longer fire
      duplicate background fetches at once, avoiding occasional glitches from overlapping
      requests. [#25943](https://github.com/open-webui/open-webui/pull/25943), [#25942](https://github.com/open-webui/open-webui/pull/25942),
      [#25934](https://github.com/open-webui/open-webui/pull/25934), [#25935](https://github.com/open-webui/open-webui/pull/25935),
      [#25838](https://github.com/open-webui/open-webui/pull/25838), [Commit](https://github.com/open-webui/open-webui/commit/e8d55c0a8beac9de0b2a0fe90f0bc0f9b64c1c1f)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F50E **Steadier search boxes across admin and workspace.** Search
      fields for users, knowledge, prompts, tools, and similar lists now run only
      as you type and reset to the first page correctly, instead of occasionally re-searching
      on their own. [Commit](https://github.com/open-webui/open-webui/commit/fc9c2ea1915accd1f6edca467e965283dff71cd7),
      [#25938](https://github.com/open-webui/open-webui/pull/25938)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F4CA **Admin feedback list loads again on PostgreSQL.** The admin
      feedback list no longer fails to load on PostgreSQL setups, where it previously
      returned a server error. [Commit](https://github.com/open-webui/open-webui/commit/7ee75a0c04a31528954903e88c9213d5fbb31aa7),
      [#25953](https://github.com/open-webui/open-webui/issues/25953)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F4BE **Saving a chat no longer drops messages.** Chat updates are
      now merged with the existing history on the server, with explicit tracking of
      deleted messages, instead of overwriting it, preventing message loss from concurrent
      or partial saves. [Commit](https://github.com/open-webui/open-webui/commit/22a44e67a8ba781feb8f2a267fed0c40213d8432),
      [Commit](https://github.com/open-webui/open-webui/commit/3319b6410e1b600b7a885a5fb78573e9a2061c22),
      [Commit](https://github.com/open-webui/open-webui/commit/24b8619f64731788ac38813768abbb64405effa4),
      [#25657](https://github.com/open-webui/open-webui/pull/25657)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F4FA **Channel message updates stay in their channel.** Streaming
      updates to a channel message are now skipped if the message no longer exists
      or belongs to a different channel, preventing stray updates. [Commit](https://github.com/open-webui/open-webui/commit/ac3449cac91e62b08a7c28e54fcd044d14dea791)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F4CC **Pinned channel messages update for everyone.** Pinning or
      unpinning a channel message now updates live for all members and works from
      thread views, instead of only changing for the person who pinned it. [Commit](https://github.com/open-webui/open-webui/commit/7ea7680f563da30b121258e5a7d7123185c4da2a)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F4CA **Vega-Lite charts render reliably.** Vega-Lite charts in chat
      are now detected by their code block language tag, so they render correctly.
      [#25843](https://github.com/open-webui/open-webui/pull/25843)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F50D **Chat search tool handles empty queries.** The built-in chat
      search tool no longer crashes when called with an empty query. [Commit](https://github.com/open-webui/open-webui/commit/b854eb09b13216f914ce5fd07ab717b8f752882b),
      [#26310](https://github.com/open-webui/open-webui/issues/26310)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F501 **Updating a knowledge file won't break the knowledge base.**
      When a file's content is updated, its new embeddings are now added before the
      old ones are removed, so a failed reindex leaves the knowledge base intact and
      usable instead of empty. [Commit](https://github.com/open-webui/open-webui/commit/248315de14d4537e0f2ec3f94dee8a7334cad248),
      [#23789](https://github.com/open-webui/open-webui/pull/23789), [#23787](https://github.com/open-webui/open-webui/issues/23787)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F3F7️ **Chat titles generate after long first responses.** A new
      chat now gets its title even when the first response takes a long time, such
      as one with extensive reasoning or many tool calls, instead of staying \"New
      Chat\". [Commit](https://github.com/open-webui/open-webui/commit/754787f43dffad3dce2c90e4fd0417b1f9dbb3c0),
      [#26240](https://github.com/open-webui/open-webui/issues/26240)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F511 **Whitespace in terminal server keys no longer breaks auth.**
      Terminal server API keys are now trimmed before use, so a key with stray leading
      or trailing whitespace still authenticates. [Commit](https://github.com/open-webui/open-webui/commit/fe3300bd6581aa469c2cdf757700ecc65a200df4),
      [Commit](https://github.com/open-webui/open-webui/commit/d6cda4a04b2e3a48855fc91abb2376cfd3a0378d)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F525 **One bad URL no longer fails Firecrawl scraping.** When fetching
      multiple pages through Firecrawl, a single failing URL is now skipped instead
      of aborting the whole batch, and rate limits are respected between requests.
      [Commit](https://github.com/open-webui/open-webui/commit/6f8221df58b17334233ac6bfe069b8f837f677d6),
      [#24183](https://github.com/open-webui/open-webui/pull/24183)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F464 **Owner avatars only show on shared folders.** Chat owner avatars
      in a folder's chat list now appear only when the folder is actually shared,
      instead of showing whenever owner information happened to be present. [Commit](https://github.com/open-webui/open-webui/commit/9802b0d13563b3535b86a350bab000d84686b1e9)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: ⏱️ **MinerU timeout saves.** The MinerU API timeout can now be saved from
      the admin settings, accepting a numeric value. [Commit](https://github.com/open-webui/open-webui/commit/3fd0384ffcd0eddd6f4c688475f8ad5d3b4de510),
      [#25604](https://github.com/open-webui/open-webui/pull/25604), [#25603](https://github.com/open-webui/open-webui/issues/25603)
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F4DC **Long dropdowns scroll.** Dropdown selects now scroll when
      their list is long, so all options stay reachable. [Commit](https://github.com/open-webui/open-webui/commit/4bc463072185d0d7c1c9218cd4487501090eccfe),
      [#25608](https://github.com/open-webui/open-webui/pull/25608)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F53D **Collapsible sections don't misfire on load.** Collapsible
      sections no longer trigger their change action when first rendered, avoiding
      unintended toggles on page load. [Commit](https://github.com/open-webui/open-webui/commit/c93d4f04aad1b0d4f8a8bda7ac403b2c8ee35f38),
      [#25229](https://github.com/open-webui/open-webui/pull/25229)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F514 **System events now fire automatically.** With the new event
      system, Open WebUI emits events for activity like startup, sign-ins, and configuration
      changes, so any webhook you already have configured may begin receiving calls
      for these newly emitted events after upgrading. Review your event and webhook
      settings after updating so you only receive the events you want. [Commit](https://github.com/open-webui/open-webui/commit/b5c43968db0ea1556b228d143ae5946dc4e944ba)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F527 **Local web fetch setting renamed.** The \"ENABLE_RAG_LOCAL_WEB_FETCH\"
      environment variable is now \"ENABLE_LOCAL_WEB_FETCH\", reflecting that it applies
      beyond retrieval; the old name still works as a deprecated alias. [Commit](https://github.com/open-webui/open-webui/commit/e3ba6984534898695b47ee4fc3d6b746e2865abc)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  - quote: "\U0001F9EA **Client-side Python now runs sandboxed.** Client-side Python
      (Pyodide) now runs in a sandboxed, opaque-origin iframe by default, isolating
      executed code from your session, cookies, local storage, and the app's own endpoints,
      while full Python, JavaScript, and external network access keep working. Code
      that relied on reaching same-origin Open WebUI endpoints from Pyodide will no
      longer be able to, and Pyodide is now marked legacy in the admin Code Execution
      settings. [Commit](https://github.com/open-webui/open-webui/commit/516051304e1b1f250c34438746ade673a79bd40c),
      [Commit](https://github.com/open-webui/open-webui/commit/c7be66626fd10c75ec35f662a709129ba1b020ec),
      [Commit](https://github.com/open-webui/open-webui/commit/62ae2069183109d878d72b9444a0e7c4f6c66caa),
      [Commit](https://github.com/open-webui/open-webui/commit/518702caae5a6484e71aa79e8ab908ec398290a7),
      [Commit](https://github.com/open-webui/open-webui/commit/03a8363583b7e0e04760d49f1e8d28dbbfefee4d)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 42-developer-workflow-changes-in-v0-10-0
  source_release: open-webui-2026-06-29-v0-10-0-github-346459817-fd55ed01
  source_type: github_releases
  theme: developer-workflow
  title: 42 Developer Workflow changes in v0.10.0
  type: change
related_changes:
- '[[Changes/Google Antigravity/2026-06-25-updated-the-permissions-request-dialog-to-display-a-clear-description-of-the-act|Updated
  the permissions request dialog to display a clear description of the action…]]'
- '[[Changes/Cline/2026-06-26-2-developer-workflow-changes-in-v4-0-0|2 Developer Workflow
  changes in v4.0.0]]'
- '[[Changes/Claude Code/2026-06-29-2-developer-workflow-changes-in-v2-1-196|2 Developer
  Workflow changes in v2.1.196]]'
source_release: '[[Releases/Open WebUI/open-webui-2026-06-29-v0-10-0-github-346459817-fd55ed01|open-webui-2026-06-29-v0-10-0-github-346459817-fd55ed01]]'
source_type: github_releases
theme: developer-workflow
title: 42 Developer Workflow changes in v0.10.0
type: change
---

<!-- chronolog:begin region="header" -->
# 42 Developer Workflow changes in v0.10.0

**Open WebUI** · 2026-06-29 · [[Themes/developer-workflow|Developer Workflow]] · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.10.0) · from [[Releases/Open WebUI/open-webui-2026-06-29-v0-10-0-github-346459817-fd55ed01|v0.10.0]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🖥️ **Open WebUI Computer agent support.** Open WebUI can now connect to Open WebUI Computer through its OpenAI-compatible gateway, letting chats run full agent sessions on your own machine with file, terminal, git, and web access. [GitHub](https://github.com/open-webui/computer)

> 🗂️ **External knowledge bases.** Knowledge bases can now be backed by an external retrieval source through configurable external knowledge connections, so you can search an existing external system from chat instead of only Open WebUI's built-in store. [Commit](https://github.com/open-webui/open-webui/commit/15c7e374384488effc3d6059d09b3a8aa79c618d)

> 🔔 **New event system with webhooks.** Open WebUI now emits events for a wide range of system activity — sign-ins, configuration changes, startup, and actions across chats, knowledge, files, and more. Administrators can send these as outbound webhooks, route them to specific users or groups, and manage which events go where from a new event settings admin page. [Commit](https://github.com/open-webui/open-webui/commit/b5c43968db0ea1556b228d143ae5946dc4e944ba), [Commit](https://github.com/open-webui/open-webui/commit/745396867888718289a2dfcf0809b3e162e00629), [Commit](https://github.com/open-webui/open-webui/commit/5576e6ed8a80a4032b7c6cb3ee0cda0254019355), [Commit](https://github.com/open-webui/open-webui/commit/7b55a63fc7ee323e9114713ce1d2f3f688aa37e6), [Commit](https://github.com/open-webui/open-webui/commit/1a8e1a993928a28b9d814c77b2aef0361b630f27), [Commit](https://github.com/open-webui/open-webui/commit/ede39d82de05eeb7591329679c8cab97753e5ff0), [Commit](https://github.com/open-webui/open-webui/commit/8f890f0b43aed3d42b9e3d954e25e54e37d526d0), [Commit](https://github.com/open-webui/open-webui/commit/741b64edb6c2ff04c4b787528cfca1c5b66a1a27), [Commit](https://github.com/open-webui/open-webui/commit/303c426c3fffafc2369205021a82659ee8715a85), [#1240](https://github.com/open-webui/open-webui/issues/1240), [#16426](https://github.com/open-webui/open-webui/pull/16426)

> 🏷️ **More custom header variables.** Custom request headers now support "{{USER_MESSAGE_ID}}", "{{USER_MESSAGE_PARENT_ID}}", and "{{TASK}}", letting connected services tell apart real user messages from automated background requests like title, tag, and follow-up generation. [Commit](https://github.com/open-webui/open-webui/commit/f85cb27ef835aa76aff7de6176bf2159ba392061)

> ⚡ **Faster model overview.** The admin model overview now loads its feedback history and tags through batched queries, so it opens noticeably faster on instances with many chats. [Commit](https://github.com/open-webui/open-webui/commit/40c09167cd6de1c853a5dd03c88b4fdcb279dfe1)

> 🏎️ **Lighter channel profile previews.** Profile previews in channels now load a person's details only when you hover to open one, rather than fetching them for every message up front. [Commit](https://github.com/open-webui/open-webui/commit/4f69c33de0e9a8fde4f16d0b2f1ed8aac8741772)

> 🔑 **Configurable secret key length.** The auto-generated secret key length can now be set with a new environment variable, instead of always using a fixed length. [Commit](https://github.com/open-webui/open-webui/commit/e473ab1231abedcb188c259b42ae7f2390739223), [#25906](https://github.com/open-webui/open-webui/pull/25906)

> 🔐 **Argon2 password hashing option.** Password hashing can now use Argon2 through a configurable algorithm setting, removing the 72-byte password length limit that came with the previous default. [Commit](https://github.com/open-webui/open-webui/commit/33cd199e6dffddd4ee8974af41ebb894871d74c1), [Commit](https://github.com/open-webui/open-webui/commit/a70a6589afad0b429cdd77afa62163391f406a87), [#25656](https://github.com/open-webui/open-webui/pull/25656)

> 🔐 **Optional encryption of valve values at rest.** Tool and function valve values can now be encrypted at rest through a new opt-in setting, with existing stored values migrated automatically, so sensitive settings like API keys aren't kept in plaintext. [Commit](https://github.com/open-webui/open-webui/commit/b4073f6378392b23a3954e33031bf5e1d98e090a), [#23721](https://github.com/open-webui/open-webui/pull/23721)

> 🧩 **Filter Outlet Hook can now run on API requests and responses.** A filter function's outlet hook now runs for direct API callers, including streaming responses, so response post-processing isn't limited to the web interface; this is controlled by a new setting and on by default. [Commit](https://github.com/open-webui/open-webui/commit/390e200f76877b185002c88b4dda27b123d29e83), [#25650](https://github.com/open-webui/open-webui/pull/25650)

> 📝 **Formatted valve descriptions.** Valve descriptions for tools and functions now render Markdown, so they can include formatting and links. [Commit](https://github.com/open-webui/open-webui/commit/7c0b0e42f5afb0e9c39bd2d42e4822d64d0c7b3e)

> 🔽 **Dropdown inputs for valve options.** Valve and confirmation inputs can now present a set of options as a dropdown instead of free text, making fixed-choice settings easier to configure. [Commit](https://github.com/open-webui/open-webui/commit/422a4768ea7428b5dd6d401ccfba00e1e86eb98a), [#26278](https://github.com/open-webui/open-webui/pull/26278)

> 📜 **Custom CA bundle for outbound connections.** A new environment variable lets you point Open WebUI at a custom CA certificate bundle, and the per-connection SSL settings now accept a bundle path, so deployments behind a corporate or internal CA can keep certificate verification on instead of disabling it. [Commit](https://github.com/open-webui/open-webui/commit/a54878b14f044d4aa1d8cf5be6f8ce9fc4285438), [Commit](https://github.com/open-webui/open-webui/commit/8b9e28b50354307a314111262f6737b6d8aa4685)

> 🖥️ **More terminal server orchestrator controls.** Admins connecting an orchestrator terminal server can now configure session lifecycle policies and refresh or reset running terminal sessions, including targeting only idle ones, from the connection settings. [Commit](https://github.com/open-webui/open-webui/commit/7e8153e889a59afe4cf77261ea5e1ef5a66665f1)

> ⚡ **Leaner knowledge-file reading for agents.** The built-in tools that let a model read knowledge files now return output in bounded, paginated chunks with a default and a hard cap, instead of potentially returning an entire large file at once, sharply reducing token usage. [Commit](https://github.com/open-webui/open-webui/commit/a285a390c12e27e614d1ba9ffb92d1a0e49e7dfa), [#26139](https://github.com/open-webui/open-webui/issues/26139)

> ⚡ **Batched streaming updates.** Streaming responses now group small updates of the same type before sending them, reducing overhead during fast token streams and tool-call output. [Commit](https://github.com/open-webui/open-webui/commit/7240517807a8b0097065f7cbbb384d34084f90fd), [#26202](https://github.com/open-webui/open-webui/pull/26202)

> 🙈 **Channel member lists no longer expose private data.** Viewing a channel's members now returns only basic profile details, instead of also exposing other members' settings, linked-account data, and personal information. [Commit](https://github.com/open-webui/open-webui/commit/fbcdcf146b99b5002705060a8243eee769108f9e)

> 🔌 **Terminal connections can't be redirected to another user.** Terminal session identifiers are now safely encoded before being passed upstream, closing a way to tamper with the connection's user identity. [#26042](https://github.com/open-webui/open-webui/pull/26042)

> 🔓 **Revoked sessions are rejected on real-time connections.** Real-time and terminal WebSocket connections now honor token revocation and expiry, so a signed-out or expired session can no longer keep a live connection open. [Commit](https://github.com/open-webui/open-webui/commit/33b91bd8ae8a100a5a306c91441a7d0b422c4cde), [#25764](https://github.com/open-webui/open-webui/pull/25764), [#25686](https://github.com/open-webui/open-webui/pull/25686)

> 🗄️ **Unknown knowledge collections are denied by default.** Retrieval now rejects unknown or unscoped collection names by default, closing a legacy path that could be used to reach collections outside the normal access checks. [Commit](https://github.com/open-webui/open-webui/commit/d99ac7d3f83b25161ca775229150c8f7c74cceee)

> 🙈 **Error responses no longer leak internals.** Server error responses now return sanitized messages instead of raw exception text, so internal details aren't exposed to signed-in users. [Commit](https://github.com/open-webui/open-webui/commit/ee5de69e374aabf5631da18a5bbc1c285ee6f7a1), [Commit](https://github.com/open-webui/open-webui/commit/0cc331d1c60341bb06b78ceeecfb2db86179c93e), [Commit](https://github.com/open-webui/open-webui/commit/396d9ac18193d43e40fb9d068075d4b780e971d7), [Commit](https://github.com/open-webui/open-webui/commit/0883638027a9b3cb7c9851f031c4f5fc1af1f25d), [#26375](https://github.com/open-webui/open-webui/pull/26375), [#26374](https://github.com/open-webui/open-webui/issues/26374)

> 📏 **Upload size limit enforced on the server.** The maximum upload size is now enforced server-side, so it can't be bypassed by a client that ignores the limit. [Commit](https://github.com/open-webui/open-webui/commit/f8ec63203c4408c46bb06698ae624d17b01b9301), [Commit](https://github.com/open-webui/open-webui/commit/d3676b4f71bfdbaf4e4d76943c51117e18932ccf), [#25869](https://github.com/open-webui/open-webui/pull/25869)

> 🗃️ **Prompt caching preserved over the Anthropic-compatible API.** Requests through the Anthropic-compatible API now keep their prompt-caching markers instead of having them stripped, so clients that rely on caching work as intended. [Commit](https://github.com/open-webui/open-webui/commit/caedcbae4988ef59ea7052b2a3198e2da4b5291a), [#25998](https://github.com/open-webui/open-webui/pull/25998), [#25964](https://github.com/open-webui/open-webui/discussions/25964)

> 🔁 **Fewer redundant data loads.** Several views no longer fire duplicate background fetches at once, avoiding occasional glitches from overlapping requests. [#25943](https://github.com/open-webui/open-webui/pull/25943), [#25942](https://github.com/open-webui/open-webui/pull/25942), [#25934](https://github.com/open-webui/open-webui/pull/25934), [#25935](https://github.com/open-webui/open-webui/pull/25935), [#25838](https://github.com/open-webui/open-webui/pull/25838), [Commit](https://github.com/open-webui/open-webui/commit/e8d55c0a8beac9de0b2a0fe90f0bc0f9b64c1c1f)

> 🔎 **Steadier search boxes across admin and workspace.** Search fields for users, knowledge, prompts, tools, and similar lists now run only as you type and reset to the first page correctly, instead of occasionally re-searching on their own. [Commit](https://github.com/open-webui/open-webui/commit/fc9c2ea1915accd1f6edca467e965283dff71cd7), [#25938](https://github.com/open-webui/open-webui/pull/25938)

> 📊 **Admin feedback list loads again on PostgreSQL.** The admin feedback list no longer fails to load on PostgreSQL setups, where it previously returned a server error. [Commit](https://github.com/open-webui/open-webui/commit/7ee75a0c04a31528954903e88c9213d5fbb31aa7), [#25953](https://github.com/open-webui/open-webui/issues/25953)

> 💾 **Saving a chat no longer drops messages.** Chat updates are now merged with the existing history on the server, with explicit tracking of deleted messages, instead of overwriting it, preventing message loss from concurrent or partial saves. [Commit](https://github.com/open-webui/open-webui/commit/22a44e67a8ba781feb8f2a267fed0c40213d8432), [Commit](https://github.com/open-webui/open-webui/commit/3319b6410e1b600b7a885a5fb78573e9a2061c22), [Commit](https://github.com/open-webui/open-webui/commit/24b8619f64731788ac38813768abbb64405effa4), [#25657](https://github.com/open-webui/open-webui/pull/25657)

> 📺 **Channel message updates stay in their channel.** Streaming updates to a channel message are now skipped if the message no longer exists or belongs to a different channel, preventing stray updates. [Commit](https://github.com/open-webui/open-webui/commit/ac3449cac91e62b08a7c28e54fcd044d14dea791)

> 📌 **Pinned channel messages update for everyone.** Pinning or unpinning a channel message now updates live for all members and works from thread views, instead of only changing for the person who pinned it. [Commit](https://github.com/open-webui/open-webui/commit/7ea7680f563da30b121258e5a7d7123185c4da2a)

> 📊 **Vega-Lite charts render reliably.** Vega-Lite charts in chat are now detected by their code block language tag, so they render correctly. [#25843](https://github.com/open-webui/open-webui/pull/25843)

> 🔍 **Chat search tool handles empty queries.** The built-in chat search tool no longer crashes when called with an empty query. [Commit](https://github.com/open-webui/open-webui/commit/b854eb09b13216f914ce5fd07ab717b8f752882b), [#26310](https://github.com/open-webui/open-webui/issues/26310)

> 🔁 **Updating a knowledge file won't break the knowledge base.** When a file's content is updated, its new embeddings are now added before the old ones are removed, so a failed reindex leaves the knowledge base intact and usable instead of empty. [Commit](https://github.com/open-webui/open-webui/commit/248315de14d4537e0f2ec3f94dee8a7334cad248), [#23789](https://github.com/open-webui/open-webui/pull/23789), [#23787](https://github.com/open-webui/open-webui/issues/23787)

> 🏷️ **Chat titles generate after long first responses.** A new chat now gets its title even when the first response takes a long time, such as one with extensive reasoning or many tool calls, instead of staying "New Chat". [Commit](https://github.com/open-webui/open-webui/commit/754787f43dffad3dce2c90e4fd0417b1f9dbb3c0), [#26240](https://github.com/open-webui/open-webui/issues/26240)

> 🔑 **Whitespace in terminal server keys no longer breaks auth.** Terminal server API keys are now trimmed before use, so a key with stray leading or trailing whitespace still authenticates. [Commit](https://github.com/open-webui/open-webui/commit/fe3300bd6581aa469c2cdf757700ecc65a200df4), [Commit](https://github.com/open-webui/open-webui/commit/d6cda4a04b2e3a48855fc91abb2376cfd3a0378d)

> 🔥 **One bad URL no longer fails Firecrawl scraping.** When fetching multiple pages through Firecrawl, a single failing URL is now skipped instead of aborting the whole batch, and rate limits are respected between requests. [Commit](https://github.com/open-webui/open-webui/commit/6f8221df58b17334233ac6bfe069b8f837f677d6), [#24183](https://github.com/open-webui/open-webui/pull/24183)

> 👤 **Owner avatars only show on shared folders.** Chat owner avatars in a folder's chat list now appear only when the folder is actually shared, instead of showing whenever owner information happened to be present. [Commit](https://github.com/open-webui/open-webui/commit/9802b0d13563b3535b86a350bab000d84686b1e9)

> ⏱️ **MinerU timeout saves.** The MinerU API timeout can now be saved from the admin settings, accepting a numeric value. [Commit](https://github.com/open-webui/open-webui/commit/3fd0384ffcd0eddd6f4c688475f8ad5d3b4de510), [#25604](https://github.com/open-webui/open-webui/pull/25604), [#25603](https://github.com/open-webui/open-webui/issues/25603)

> 📜 **Long dropdowns scroll.** Dropdown selects now scroll when their list is long, so all options stay reachable. [Commit](https://github.com/open-webui/open-webui/commit/4bc463072185d0d7c1c9218cd4487501090eccfe), [#25608](https://github.com/open-webui/open-webui/pull/25608)

> 🔽 **Collapsible sections don't misfire on load.** Collapsible sections no longer trigger their change action when first rendered, avoiding unintended toggles on page load. [Commit](https://github.com/open-webui/open-webui/commit/c93d4f04aad1b0d4f8a8bda7ac403b2c8ee35f38), [#25229](https://github.com/open-webui/open-webui/pull/25229)

> 🔔 **System events now fire automatically.** With the new event system, Open WebUI emits events for activity like startup, sign-ins, and configuration changes, so any webhook you already have configured may begin receiving calls for these newly emitted events after upgrading. Review your event and webhook settings after updating so you only receive the events you want. [Commit](https://github.com/open-webui/open-webui/commit/b5c43968db0ea1556b228d143ae5946dc4e944ba)

> 🔧 **Local web fetch setting renamed.** The "ENABLE_RAG_LOCAL_WEB_FETCH" environment variable is now "ENABLE_LOCAL_WEB_FETCH", reflecting that it applies beyond retrieval; the old name still works as a deprecated alias. [Commit](https://github.com/open-webui/open-webui/commit/e3ba6984534898695b47ee4fc3d6b746e2865abc)

> 🧪 **Client-side Python now runs sandboxed.** Client-side Python (Pyodide) now runs in a sandboxed, opaque-origin iframe by default, isolating executed code from your session, cookies, local storage, and the app's own endpoints, while full Python, JavaScript, and external network access keep working. Code that relied on reaching same-origin Open WebUI endpoints from Pyodide will no longer be able to, and Pyodide is now marked legacy in the admin Code Execution settings. [Commit](https://github.com/open-webui/open-webui/commit/516051304e1b1f250c34438746ade673a79bd40c), [Commit](https://github.com/open-webui/open-webui/commit/c7be66626fd10c75ec35f662a709129ba1b020ec), [Commit](https://github.com/open-webui/open-webui/commit/62ae2069183109d878d72b9444a0e7c4f6c66caa), [Commit](https://github.com/open-webui/open-webui/commit/518702caae5a6484e71aa79e8ab908ec398290a7), [Commit](https://github.com/open-webui/open-webui/commit/03a8363583b7e0e04760d49f1e8d28dbbfefee4d)

Source: https://github.com/open-webui/open-webui/releases/tag/v0.10.0
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2026-06-29-5-files-and-data-changes-in-v0-10-0|5 Files and Data changes in v0.10.0]] · Files and Data
- [[Changes/Open WebUI/2026-06-29-5-memory-and-personalization-changes-in-v0-10-0|5 Memory and Personalization changes in v0.10.0]] · Memory and Personalization
- [[Changes/Open WebUI/2026-06-29-3-voice-and-audio-changes-in-v0-10-0|3 Voice and Audio changes in v0.10.0]] · Voice and Audio
- [[Changes/Open WebUI/2026-06-29-14-interface-experience-changes-in-v0-10-0|14 Interface Experience changes in v0.10.0]] · Interface Experience
- [[Changes/Open WebUI/2026-06-29-4-collaboration-changes-in-v0-10-0|4 Collaboration changes in v0.10.0]] · Collaboration
- [[Changes/Open WebUI/2026-06-29-client-user-agent-forwarded-to-model-backends-the-browser-s-user-agent-is-now-pa|🪪 Client User-Agent forwarded to model backends. The browser's User-Agent is now…]] · Agent Mode
- [[Changes/Open WebUI/2026-06-29-scim-sync-can-t-demote-an-admin-a-scim-provisioning-sync-that-marks-a-user-inact|🛟 SCIM sync can't demote an admin. A SCIM provisioning sync that marks a user…]] · Enterprise and Administration
- [[Changes/Open WebUI/2026-06-29-8-search-and-browsing-changes-in-v0-10-0|8 Search and Browsing changes in v0.10.0]] · Search and Browsing
- [[Changes/Open WebUI/2026-06-29-25-model-support-changes-in-v0-10-0|25 Model Support changes in v0.10.0]] · Model Support
- [[Changes/Open WebUI/2026-06-29-6-reliability-and-performance-changes-in-v0-10-0|6 Reliability and Performance changes in v0.10.0]] · Reliability and Performance
- [[Changes/Open WebUI/2026-06-29-4-mobile-and-desktop-changes-in-v0-10-0|4 Mobile and Desktop changes in v0.10.0]] · Mobile and Desktop
- [[Changes/Open WebUI/2026-06-29-better-screen-reader-labels-on-toggles-integration-and-switch-toggles-now-expose|♿ Better screen-reader labels on toggles. Integration and switch toggles now…]] · Accessibility and Localization
- [[Changes/Open WebUI/2026-06-29-16-safety-and-privacy-changes-in-v0-10-0|16 Safety and Privacy changes in v0.10.0]] · Safety and Privacy
- [[Changes/Open WebUI/2026-06-29-2-pricing-model-changes-in-v0-10-0|2 Pricing Model changes in v0.10.0]] · Pricing Model
- [[Changes/Open WebUI/2026-06-29-7-apps-and-integrations-changes-in-v0-10-0|7 Apps and Integrations changes in v0.10.0]] · Apps and Integrations
- [[Changes/Open WebUI/2026-06-29-9-account-and-access-changes-in-v0-10-0|9 Account and Access changes in v0.10.0]] · Account and Access
- [[Changes/Open WebUI/2026-06-29-usable-chat-input-on-mobile-with-many-tools-when-skills-tools-terminal-web-searc|📱 Usable chat input on mobile with many tools. When skills, tools, terminal, web…]] · Image Generation
- [[Changes/Open WebUI/2026-06-29-6-automation-and-scheduling-changes-in-v0-10-0|6 Automation and Scheduling changes in v0.10.0]] · Automation and Scheduling
- [[Changes/Open WebUI/2026-06-29-3-context-window-changes-in-v0-10-0|3 Context Window changes in v0.10.0]] · Context Window
- [[Changes/Open WebUI/2026-06-29-10-editor-experience-changes-in-v0-10-0|10 Editor Experience changes in v0.10.0]] · Editor Experience
- [[Changes/Open WebUI/2026-06-29-29-other-changes-in-v0-10-0|29 other changes in v0.10.0]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Developer Workflow

- Earlier: 2026-06-29 · Claude Code · [[Changes/Claude Code/2026-06-29-2-developer-workflow-changes-in-v2-1-196|2 Developer Workflow changes in v2.1.196]]
- Later: 2026-06-30 · GitHub Copilot CLI · [[Changes/GitHub Copilot CLI/2026-06-30-21-developer-workflow-changes-in-v1-0-66|21 Developer Workflow changes in v1.0.66]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-18 · Cursor · [[Changes/Cursor/2023-03-18-built-in-terminal|Built-in terminal]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2026-06-29-ddb1f1&body=Card%3A%20Changes%2FOpen%20WebUI%2F2026-06-29-42-developer-workflow-changes-in-v0-10-0.md%0ACard%20ID%3A%20open-webui-2026-06-29-ddb1f1%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.10.0%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->