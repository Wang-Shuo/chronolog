---
card_id: open-webui-2025-08-09-d82a69
date: '2025-08-09'
description: "Open WebUI · 2025-08-09 · Other changes: 29 changes in v0.6.19 — \U0001F6D1
  **Stop Button for Merge Responses**: Added a dedicated stop button to immediately
  halt the…"
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: 0b7cd8cd0d5241b68715444122179dd4ef403d5379253e990cb3c327c9a301a4
product: open-webui
product_name: Open WebUI
record:
  card_id: open-webui-2025-08-09-d82a69
  comparison: ''
  date: '2025-08-09'
  description: 'Open WebUI — v0.6.19: 29 other changes'
  evidence:
  - quote: "\U0001F6D1 **Stop Button for Merge Responses**: Added a dedicated stop
      button to immediately halt the generation of merged AI responses, providing
      users with more control over ongoing outputs."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.19
  - quote: '✍️ **Formatting Toolbar for Chat Input**: Introduced a dedicated formatting
      toolbar for the rich text chat input field, providing users with more accessible
      options for text styling and editing, configurable via interface settings.'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.19
  - quote: "\U0001F4E6 **Native Redis Cluster Mode Support**: Added full support for
      connecting to Redis in cluster mode, allowing for scalable and highly available
      Redis deployments beyond Sentinel-managed setups. New environment variables
      'REDIS_CLUSTER' and 'WEBSOCKET_REDIS_CLUSTER' enable the use of 'redis.cluster.RedisCluster'
      clients."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.19
  - quote: "\U0001F9D1\U0001F4BC **Export All Users to CSV**: Administrators can now
      export a complete list of all users to a CSV file directly from the Admin Panel's
      database settings. This provides a simple, one-click way to generate user data
      for auditing, reporting, or management purposes."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.19
  - quote: "\U0001F6C2 **Optional \"Confirm Password\" on Sign-Up**: To help prevent
      password typos during account creation, administrators can now enable a \"Confirm
      Password\" field on the sign-up page. This feature is disabled by default and
      can be activated via an environment variable for enhanced user experience."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.19
  - quote: "\U0001F4AC **View Full Chat from User Feedback**: Administrators can now
      easily navigate to the full conversation associated with a user feedback entry
      directly from the feedback modal, streamlining the review and troubleshooting
      process."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.19
  - quote: "\U0001F39A️ **Intuitive Hybrid Search BM25-Weight Slider**: The numerical
      input for the BM25-Weight parameter in Hybrid Search has been replaced with
      an interactive slider, offering a more intuitive way to adjust the balance between
      lexical and semantic search. A \"Default/Custom\" toggle and clearer labels
      enhance usability and understanding of this key parameter."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.19
  - quote: "\U0001F5BC️ **Option to Disable Image Compression in Channels**: Introduced
      a new setting under Interface options to allow users to force-disable image
      compression specifically for images posted in channels, ensuring higher resolution
      for critical visual content."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.19
  - quote: "\U0001F512 **Resolved FIPS Self-Test Failure**: Fixed a critical issue
      that prevented Open WebUI from running on FIPS-compliant systems, specifically
      resolving the \"FATAL FIPS SELFTEST FAILURE\" error related to OpenSSL and SentenceTransformers,
      restoring compatibility with secure environments."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.19
  - quote: "\U0001F510 **Hardened OIDC Signout Flow**: The OpenID Connect signout
      process now verifies that the 'OPENID_PROVIDER_URL' is configured before attempting
      to communicate with it, preventing potential errors and ensuring a more reliable
      logout experience."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.19
  - quote: "\U0001F353 **Raspberry Pi Compatibility Restored**: Pinned the pyarrow
      library to version 20.0.0, resolving an \"Illegal Instruction\" crash on ARM-based
      devices like the Raspberry Pi and ensuring stable operation on this hardware."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.19
  - quote: "\U0001F5BC️ **Table Pasting in Rich Text Input Displayed Correctly**:
      Fixed an issue where pasting table text into the rich text input would incorrectly
      display it as code. Tables are now properly rendered as expected, improving
      content formatting and user experience."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.19
  - quote: '✍️ **Rich Text Input TypeError Resolution**: Addressed a potential ''TypeError:
      ue.getWordAtDocPos is not a function'' in ''MessageInput.svelte'' by refactoring
      how the ''getWordAtDocPos'' function is accessed and referenced from ''RichTextInput.svelte'',
      ensuring stable rich text input behavior, especially after production restarts.'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.19
  - quote: "\U0001F3A8 **Consistent Dark Mode Background**: Fixed an issue where the
      application background could incorrectly flash or remain white during page loads
      and refreshes in dark mode, ensuring a seamless and consistent visual experience."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.19
  - quote: '✏️ **Underscores Allowed in Prompt Commands**: Fixed the validation for
      prompt commands to correctly allow the use of underscores (''_''), aligning
      with documentation examples and improving flexibility in naming custom prompts.'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.19
  - quote: "\U0001F4A1 **Title Generation Button Behavior Fixed**: Resolved an issue
      where clicking the \"Generate Title\" button while editing a chat or note title
      would incorrectly save the title before generation could start. The focus is
      now managed correctly, ensuring a smooth and predictable user experience."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.19
  - quote: '✏️ **Consistent Chat Input Height**: Fixed a minor visual bug where the
      chat input field''s height would change slightly when toggling the "Rich Text
      Input for Chat" setting, ensuring a more stable and consistent layout.'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.19
  - quote: "\U0001F517 **Robust Tool Server URL Handling**: Fixed an issue where providing
      a full URL for a tool server's OpenAPI specification resulted in an invalid
      path. The system now correctly handles both absolute URLs and relative paths,
      improving configuration flexibility."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.19
  - quote: '⚙️ **Corrected Direct Connection Save Logic**: Fixed a bug in the Admin
      Connections settings page by removing a redundant save action for ''Direct Connections'',
      leading to more reliable and predictable behavior when updating settings.'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.19
  - quote: "\U0001F6E0️ **Development Script CORS Fix**: Corrected the CORS origin
      URL in the local development script (dev.sh) by removing the trailing slash,
      ensuring a more reliable and consistent setup for developers."
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.19
  - quote: '> Get **enhanced capabilities**, including **custom theming and branding**,
      **Service Level Agreement (SLA) support**, **Long-Term Support (LTS) versions**,
      and **more!**'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.19
  - quote: "\U0001F44F Massive thanks to our incredible contributors for their hard
      work and dedication to making this release possible:"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.19
  - quote: '@silentoplayz, @andrewbbaek, @psy42a, @expruc, @Ithanil, @17jmumford,
      @dependabot[bot], @Classic298, @Rain6435, @Jakobu5, @Ithanil, @rndmcnlly, @hiwylee,
      @ahangarha, @gaby, @hadadrjt, @leebeomhun'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.19
  - quote: "\U0001F680 We'd like to extend a heartfelt thank you to our amazing sponsors
      for their generous support (Note: We've excluded private sponsors from this
      list. If you'd like to get featured here, feel free to reach out to us!)"
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.19
  - quote: '**Warp** <a href="https://warp.dev/open-webui" target="_blank">'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.19
  - quote: '<img src="https://docs.openwebui.com/sponsors/banners/warp-banner.png"
      alt="warp" style="width: 8rem; height: 8rem; border-radius: .75rem;" />'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.19
  - quote: '**Tailscale** <a href="https://tailscale.com/blog/self-host-a-local-ai-stack/?utm_source=OpenWebUI&utm_medium=paid-ad-placement&utm_campaign=OpenWebUI-Docs"
      target="_blank">'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.19
  - quote: '<img src="https://docs.openwebui.com/sponsors/banners/tailscale-banner.png"
      alt="tailscale" style="width: 8rem; height: 8rem; border-radius: .75rem;" />'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.19
  - quote: '@amd, @agency-agency, @roosi-gmbh, @feddersen-group, @SRKConsulting, @Poxel2,
      @mushmax, @rndmcnlly, @icanbwell, @Krambu-Travis, @loitragg, @GenieDev101, @CubicleGangster,
      @GitDatamind, @TOWaB, @TheZigGroup, @Classic298, @FominVO, @catalyst-net-nz,
      @JrdnHans, @hkosm, @VeroFess'
    source_release: https://github.com/open-webui/open-webui/releases/tag/v0.6.19
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: open-webui
  product_name: Open WebUI
  slug: 29-other-changes-in-v0-6-19
  source_release: open-webui-2025-08-09-v0-6-19-github-238805134-e05b9243
  source_type: github_releases
  theme: uncategorized
  title: 29 other changes in v0.6.19
  type: change
source_release: '[[Releases/Open WebUI/open-webui-2025-08-09-v0-6-19-github-238805134-e05b9243|open-webui-2025-08-09-v0-6-19-github-238805134-e05b9243]]'
source_type: github_releases
theme: uncategorized
title: 29 other changes in v0.6.19
type: change
---

<!-- chronolog:begin region="header" -->
# 29 other changes in v0.6.19

**Open WebUI** · 2025-08-09 · Other changes · Digest · [Official source](https://github.com/open-webui/open-webui/releases/tag/v0.6.19) · from [[Releases/Open WebUI/open-webui-2025-08-09-v0-6-19-github-238805134-e05b9243|v0.6.19]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> 🛑 **Stop Button for Merge Responses**: Added a dedicated stop button to immediately halt the generation of merged AI responses, providing users with more control over ongoing outputs.

> ✍️ **Formatting Toolbar for Chat Input**: Introduced a dedicated formatting toolbar for the rich text chat input field, providing users with more accessible options for text styling and editing, configurable via interface settings.

> 📦 **Native Redis Cluster Mode Support**: Added full support for connecting to Redis in cluster mode, allowing for scalable and highly available Redis deployments beyond Sentinel-managed setups. New environment variables 'REDIS_CLUSTER' and 'WEBSOCKET_REDIS_CLUSTER' enable the use of 'redis.cluster.RedisCluster' clients.

> 🧑💼 **Export All Users to CSV**: Administrators can now export a complete list of all users to a CSV file directly from the Admin Panel's database settings. This provides a simple, one-click way to generate user data for auditing, reporting, or management purposes.

> 🛂 **Optional "Confirm Password" on Sign-Up**: To help prevent password typos during account creation, administrators can now enable a "Confirm Password" field on the sign-up page. This feature is disabled by default and can be activated via an environment variable for enhanced user experience.

> 💬 **View Full Chat from User Feedback**: Administrators can now easily navigate to the full conversation associated with a user feedback entry directly from the feedback modal, streamlining the review and troubleshooting process.

> 🎚️ **Intuitive Hybrid Search BM25-Weight Slider**: The numerical input for the BM25-Weight parameter in Hybrid Search has been replaced with an interactive slider, offering a more intuitive way to adjust the balance between lexical and semantic search. A "Default/Custom" toggle and clearer labels enhance usability and understanding of this key parameter.

> 🖼️ **Option to Disable Image Compression in Channels**: Introduced a new setting under Interface options to allow users to force-disable image compression specifically for images posted in channels, ensuring higher resolution for critical visual content.

> 🔒 **Resolved FIPS Self-Test Failure**: Fixed a critical issue that prevented Open WebUI from running on FIPS-compliant systems, specifically resolving the "FATAL FIPS SELFTEST FAILURE" error related to OpenSSL and SentenceTransformers, restoring compatibility with secure environments.

> 🔐 **Hardened OIDC Signout Flow**: The OpenID Connect signout process now verifies that the 'OPENID_PROVIDER_URL' is configured before attempting to communicate with it, preventing potential errors and ensuring a more reliable logout experience.

> 🍓 **Raspberry Pi Compatibility Restored**: Pinned the pyarrow library to version 20.0.0, resolving an "Illegal Instruction" crash on ARM-based devices like the Raspberry Pi and ensuring stable operation on this hardware.

> 🖼️ **Table Pasting in Rich Text Input Displayed Correctly**: Fixed an issue where pasting table text into the rich text input would incorrectly display it as code. Tables are now properly rendered as expected, improving content formatting and user experience.

> ✍️ **Rich Text Input TypeError Resolution**: Addressed a potential 'TypeError: ue.getWordAtDocPos is not a function' in 'MessageInput.svelte' by refactoring how the 'getWordAtDocPos' function is accessed and referenced from 'RichTextInput.svelte', ensuring stable rich text input behavior, especially after production restarts.

> 🎨 **Consistent Dark Mode Background**: Fixed an issue where the application background could incorrectly flash or remain white during page loads and refreshes in dark mode, ensuring a seamless and consistent visual experience.

> ✏️ **Underscores Allowed in Prompt Commands**: Fixed the validation for prompt commands to correctly allow the use of underscores ('_'), aligning with documentation examples and improving flexibility in naming custom prompts.

> 💡 **Title Generation Button Behavior Fixed**: Resolved an issue where clicking the "Generate Title" button while editing a chat or note title would incorrectly save the title before generation could start. The focus is now managed correctly, ensuring a smooth and predictable user experience.

> ✏️ **Consistent Chat Input Height**: Fixed a minor visual bug where the chat input field's height would change slightly when toggling the "Rich Text Input for Chat" setting, ensuring a more stable and consistent layout.

> 🔗 **Robust Tool Server URL Handling**: Fixed an issue where providing a full URL for a tool server's OpenAPI specification resulted in an invalid path. The system now correctly handles both absolute URLs and relative paths, improving configuration flexibility.

> ⚙️ **Corrected Direct Connection Save Logic**: Fixed a bug in the Admin Connections settings page by removing a redundant save action for 'Direct Connections', leading to more reliable and predictable behavior when updating settings.

> 🛠️ **Development Script CORS Fix**: Corrected the CORS origin URL in the local development script (dev.sh) by removing the trailing slash, ensuring a more reliable and consistent setup for developers.

> > Get **enhanced capabilities**, including **custom theming and branding**, **Service Level Agreement (SLA) support**, **Long-Term Support (LTS) versions**, and **more!**

> 👏 Massive thanks to our incredible contributors for their hard work and dedication to making this release possible:

> @silentoplayz, @andrewbbaek, @psy42a, @expruc, @Ithanil, @17jmumford, @dependabot[bot], @Classic298, @Rain6435, @Jakobu5, @Ithanil, @rndmcnlly, @hiwylee, @ahangarha, @gaby, @hadadrjt, @leebeomhun

> 🚀 We'd like to extend a heartfelt thank you to our amazing sponsors for their generous support (Note: We've excluded private sponsors from this list. If you'd like to get featured here, feel free to reach out to us!)

> **Warp** \<a href="https://warp.dev/open-webui" target="_blank">

> \<img src="https://docs.openwebui.com/sponsors/banners/warp-banner.png" alt="warp" style="width: 8rem; height: 8rem; border-radius: .75rem;" />

> **Tailscale** \<a href="https://tailscale.com/blog/self-host-a-local-ai-stack/?utm_source=OpenWebUI&utm_medium=paid-ad-placement&utm_campaign=OpenWebUI-Docs" target="_blank">

> \<img src="https://docs.openwebui.com/sponsors/banners/tailscale-banner.png" alt="tailscale" style="width: 8rem; height: 8rem; border-radius: .75rem;" />

> @amd, @agency-agency, @roosi-gmbh, @feddersen-group, @SRKConsulting, @Poxel2, @mushmax, @rndmcnlly, @icanbwell, @Krambu-Travis, @loitragg, @GenieDev101, @CubicleGangster, @GitDatamind, @TOWaB, @TheZigGroup, @Classic298, @FominVO, @catalyst-net-nz, @JrdnHans, @hkosm, @VeroFess

Source: https://github.com/open-webui/open-webui/releases/tag/v0.6.19
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Open WebUI/2025-08-09-7-apps-and-integrations-changes-in-v0-6-19|7 Apps and Integrations changes in v0.6.19]] · Apps and Integrations
- [[Changes/Open WebUI/2025-08-09-2-editor-experience-changes-in-v0-6-19|2 Editor Experience changes in v0.6.19]] · Editor Experience
- [[Changes/Open WebUI/2025-08-09-3-enterprise-and-administration-changes-in-v0-6-19|3 Enterprise and Administration changes in v0.6.19]] · Enterprise and Administration
- [[Changes/Open WebUI/2025-08-09-2-mobile-and-desktop-changes-in-v0-6-19|2 Mobile and Desktop changes in v0.6.19]] · Mobile and Desktop
- [[Changes/Open WebUI/2025-08-09-2-search-and-browsing-changes-in-v0-6-19|2 Search and Browsing changes in v0.6.19]] · Search and Browsing
- [[Changes/Open WebUI/2025-08-09-customizable-floating-quick-actions-with-tool-support-take-full-control-of-your|✍️ Customizable Floating Quick Actions with Tool Support]] · Automation and Scheduling
- [[Changes/Open WebUI/2025-08-09-15-reliability-and-performance-changes-in-v0-6-19|15 Reliability and Performance changes in v0.6.19]] · Reliability and Performance
- [[Changes/Open WebUI/2025-08-09-2-files-and-data-changes-in-v0-6-19|2 Files and Data changes in v0.6.19]] · Files and Data
- [[Changes/Open WebUI/2025-08-09-folder-system-prompt-variables-restored-fixed-a-bug-where-prompt-variables-e-g-c|📁 Folder System Prompt Variables Restored]] · Context Window
- [[Changes/Open WebUI/2025-08-09-admin-first-whisper-language-priority-the-global-whisper-language-setting-now-ac|🗣️ Admin-First Whisper Language Priority]] · Voice and Audio
- [[Changes/Open WebUI/2025-08-09-2-developer-workflow-changes-in-v0-6-19|2 Developer Workflow changes in v0.6.19]] · Developer Workflow
- [[Changes/Open WebUI/2025-08-09-enhanced-memory-stability-and-security-refactored-memory-update-and-delete-opera|🧠 Enhanced Memory Stability and Security]] · Memory and Personalization
- [[Changes/Open WebUI/2025-08-09-11-model-support-changes-in-v0-6-19|11 Model Support changes in v0.6.19]] · Model Support
- [[Changes/Open WebUI/2025-08-09-4-account-and-access-changes-in-v0-6-19|4 Account and Access changes in v0.6.19]] · Account and Access
- [[Changes/Open WebUI/2025-08-09-10-safety-and-privacy-changes-in-v0-6-19|10 Safety and Privacy changes in v0.6.19]] · Safety and Privacy
- [[Changes/Open WebUI/2025-08-09-3-collaboration-changes-in-v0-6-19|3 Collaboration changes in v0.6.19]] · Collaboration
- [[Changes/Open WebUI/2025-08-09-3-accessibility-and-localization-changes-in-v0-6-19|3 Accessibility and Localization changes in v0.6.19]] · Accessibility and Localization
- [[Changes/Open WebUI/2025-08-09-13-interface-experience-changes-in-v0-6-19|13 Interface Experience changes in v0.6.19]] · Interface Experience
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->

<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20open-webui-2025-08-09-d82a69&body=Card%3A%20Changes%2FOpen%20WebUI%2F2025-08-09-29-other-changes-in-v0-6-19.md%0ACard%20ID%3A%20open-webui-2025-08-09-d82a69%0ASource%3A%20https%3A%2F%2Fgithub.com%2Fopen-webui%2Fopen-webui%2Freleases%2Ftag%2Fv0.6.19%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->