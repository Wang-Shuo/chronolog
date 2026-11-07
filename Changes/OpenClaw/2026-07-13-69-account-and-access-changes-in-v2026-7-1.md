---
card_id: openclaw-2026-07-13-93adbc
date: '2026-07-13'
description: 'OpenClaw · 2026-07-13 · Account and Access: 69 changes in v2026.7.1
  — The Gateway Dashboard login now fits and behaves better on phones and short windows,
  with…'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires
    login]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1201
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 29
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: b63e52d7054906eceac3ed5c3865274a221bee5609eedf7cac071849a20e5319
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-07-13-93adbc
  comparison: ''
  date: '2026-07-13'
  description: 'OpenClaw — v2026.7.1: 69 Account and Access changes'
  evidence:
  - quote: 'The Gateway Dashboard login now fits and behaves better on phones and
      short windows, with larger touch targets, easier URL entry, and reachable recovery
      help. #100208'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Temporary Gateway disconnects no longer replace an authenticated Control
      UI page with the login screen, preserving dashboard context while automatic
      reconnection continues. #100479'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: A failed Control UI login or Gateway connection now immediately shows the
      error, recovery steps, and relevant documentation link instead of hiding them
      in a collapsed panel. f9e194e
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Users with saved working dashboard credentials no longer see the login
      screen flash briefly while Control UI reconnects. #101849'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Owners and admins can now restore an expired Codex or OpenAI login from
      a browser through private Telegram, Web UI, Discord, or Slack commands without
      SSH access. #98006 Thanks @100yenadmin, @jalehman, @obviyus.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'macOS onboarding now verifies the chosen AI connection before first chat,
      presents clearer local and remote setup choices, and offers friendly recovery
      or a verified manual API-key path when authentication fails. #100288'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'First-time onboarding now preserves earlier choices after authentication
      or pairing trouble and gives users an actionable model-configuration next step
      instead of opening an unusable first chat. #100632'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: OpenClaw model selection expands across major hosted, managed, and local
      choices. Each supported provider route retains its own authentication, model
      limits, reasoning controls, tool behavior, image support, and usage reporting.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Tencent Hunyuan Hy3 now has a complete setup path through TokenHub or TokenPlan,
      including first-class authentication choices, CLI onboarding, model discovery,
      and configuration validation. Existing TokenHub configurations retain access
      to hy3-preview alongside the stable hy3 model.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Operators can configure Meta Model API with MODEL_API_KEY or the onboarding
      authentication choice, select meta-model-api/muse-spark-1.1 , and use supported
      streaming, tool calling, image input, and reasoning-effort controls.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Tencent Hunyuan Hy3 now has a complete supported OpenClaw setup path through
      TokenHub or TokenPlan, including first-class authentication, model discovery,
      configuration validation, CLI onboarding, and compatibility for existing hy3-preview
      setups. #99076 Thanks @moncac.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'openclaw channels login --channel feishu now prints a compact QR code
      that stays scannable in a normal terminal window. #97087 Thanks @nianjiuzst.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Telegram rich replies and progress messages containing OAuth email addresses
      now arrive instead of being rejected by Telegram validation. #95900 Thanks @obviyus.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Slack, Discord, Telegram, WhatsApp, and Microsoft Teams users now receive
      a clear retry and re-authentication message when a model provider returns a
      recognized HTTP 401 error instead of seeing only a reaction or no useful reply.
      #96599 Thanks @sjf-oa.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Slack startup and account checks now warn when a user OAuth credential
      is configured as the bot token, before identity confusion affects mentions or
      replies. #99931 Thanks @ooiuuii.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'openclaw channels login --channel whatsapp now replaces expired QR codes
      in place so interactive terminals show one current, scannable code. #100159'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: After /login codex succeeds in Telegram, retrying the request now uses
      the newly authenticated OpenAI profile instead of the previous account. fca0c81
      Thanks @100yenadmin.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Ollama Cloud setup now stops oversized or malicious authentication responses
      before they can consume excessive memory, while normal sign-in remains unchanged.
      #97581 Thanks @hugenshen.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'For Codex-backed OpenAI models, /status now identifies ChatGPT login authentication
      as oauth (codex-cli) instead of incorrectly labeling it as an environment API
      key. #91240 Related #91099 . Thanks @849261680, @ukstem.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'OpenAI OAuth usage checks now cap oversized WHAM rate-limit responses
      before they can destabilize the process. #97702 Thanks @cxbasdev.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'ChatGPT OAuth sign-in and refresh now reject unexpectedly large token
      responses cleanly instead of risking Gateway memory exhaustion. #99479 Thanks
      @pandah97.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'OpenAI-compatible providers routed through the GitHub Copilot BYOK harness
      now retain bearer authentication, reducing false 401 errors for valid credentials.
      #99955 Thanks @hxy91819.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: OpenAI/Codex and Anthropic OAuth result pages now show OpenClaw branding
      instead of the legacy Pi logo. 1834592
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Chutes login, user lookup, and token refresh now stop unexpectedly large
      OAuth responses with a bounded error instead of buffering them without limit.
      #96777 Thanks @wangmiao0668000666.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'xAI and Grok OAuth sign-in now works on SSH hosts, containers, VPS systems,
      and other headless environments without forwarding a localhost callback port.
      #97249 Thanks @fuller-stack-dev, @jaaneek.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'GitHub Copilot sign-in, refresh, and model-list checks now fail with labeled
      size limits when GitHub or a proxy returns an oversized response. #97499 Thanks
      @wangmiao0668000666.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Z.AI users can recover a profile that accidentally stored an onboarding
      command as the API key without wiping all authentication state. #97520 Thanks
      @zhangguiping-xydt.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'xAI sign-in, token refresh, and device approval now stop oversized OAuth
      responses before they can consume unbounded memory. #97615 Thanks @cxbasdev.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Google OAuth sign-in, token exchange, and project discovery now return
      a bounded error for oversized responses instead of risking a process crash.
      #97628 Thanks @vincentkoc, @wangmiao0668000666.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'OpenRouter model probes and agent requests now use discovered environment
      or profile API keys correctly instead of failing with a missing-authentication-header
      error. #98187 Related #97934 . Thanks @laurencebrown, @sunlit-deng.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'ChatGPT OAuth-backed Responses sessions now retain backend affinity across
      turns, improving prompt-cache reuse and reducing repeated processing of the
      same conversation context. #100233 Thanks @marvinthebored, @obviyus, @peetiegonzalez.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Anthropic sign-in now rejects unsupported callback-host overrides, keeps
      authorization on standard local loopback addresses, and avoids callback failures
      or exposure through a non-local listener. #96917 Thanks @xialonglee.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Expired Claude CLI authentication now shows the exact recovery command
      claude auth login && openclaw models auth login --provider anthropic --method
      cli instead of a generic failure. #97669 Thanks @alix-007.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Cloudflare 403 challenges on OpenAI or Codex OAuth requests now produce
      gateway-block guidance instead of incorrectly telling users their authentication
      failed. #94440 Related #94432 . Thanks @lzyyzznl, @pbm9z95m6z-hue.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'OpenAI authentication errors now point ChatGPT/Codex OAuth users to a
      model compatible with their existing sign-in instead of recommending an outdated
      default. #100579 Thanks @zhangguiping-xydt.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Codex app-server runs with an invalid ChatGPT OAuth session now surface
      the real sign-in error promptly instead of waiting for a misleading ten-second
      authentication timeout. #100713 Thanks @lin-hongkuan.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'After /model changes a session''s provider, /status and session_status
      now report that provider''s usage, authentication, runtime, and context details
      rather than stale defaults. #93384 Thanks @obviyus, @osolmaz, @rollingshmily,
      @samiralibabic, @zhangguiping-xydt.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Request-format and schema failures now show the relevant diagnostic without
      sending users through unnecessary provider login or reconfiguration steps. #95779
      Thanks @pick-cat.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Existing xAI and Grok OAuth sessions using the retired token endpoint
      can renew after expiry without forcing another browser or SSH-tunneled login.
      #96146 Thanks @fuller-stack-dev, @jaaneek.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'OpenRouter sign-in now fails safely on oversized replies, and Discord
      webhook sends remain successful when their optional response body is absent,
      malformed, or too large. #98098 Thanks @lwy-2.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Channel replies can now continue as soon as an embedded-agent turn finishes
      instead of waiting roughly 50 seconds for post-run authentication bookkeeping.
      #85829 Thanks @turbotheturtle.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Gateway startup no longer performs unsolicited provider-auth discovery
      across every configured agent, helping channels and local commands remain responsive
      while authentication loads on demand. #100667 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Gateway connection failures now identify the last completed handshake
      phase, helping operators distinguish upgrade, credential, authentication, session,
      and ready-state stalls. #93402 Thanks @849261680, @bzelones, @vincentkoc, @youngting520.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Gateway override authentication errors now tell CLI and TUI users whether
      to add a token or password, remove --url , or pair the relevant environment
      variables. #100418 Thanks @gmays.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'First-run macOS setup now recognizes a successfully saved Codex login
      and is less likely to finish with a stale Gateway or bundled-skills warning.
      #101218'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Slack rooms that require a mention no longer wake OpenClaw for ordinary
      messages when the bot identity is missing or untrusted, and setup warnings point
      operators to a Bot User OAuth Token when needed. #91584 Thanks @hiragram.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'openclaw doctor --fix now preserves separate OAuth accounts for the same
      provider, including each account reference and saved display name. #97541 Thanks
      @liuhao1024, @yetval.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Gateway authentication retries now send stored device tokens only to true
      loopback endpoints, not remote hostnames that merely resemble 127.* addresses.
      #99859 Thanks @ly85206559.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: /login codex now switches the active chat to the account just authenticated
      without overwriting a newer manual profile choice, and gives recovery guidance
      if the switch fails. 02c3de9 Thanks @vincentkoc.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Profile changes made through /login now use the standard session save path,
      preserving newer concurrent selections and existing recovery behavior. f07c478
      Thanks @vincentkoc.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Masked malformed credentials now stay on one safe line in setup and authentication
      diagnostics even when the original input contains newlines or other control
      bytes. #96445 Thanks @lin-hongkuan.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'When another OpenClaw process is refreshing OpenAI OAuth credentials,
      operators now see one useful contention error without duplicated wording or
      exposed local file paths. #101573 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Android connection recovery now identifies expired setup codes, stale
      credentials, and missing or invalid authentication with the appropriate next
      step. #98094 Thanks @qingminglong.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Android Gateway setup now replaces a generic authentication warning with
      specific recovery labels for expired setup codes, missing or invalid credentials,
      stale saved authentication, and required device identity. #98698 Related #98046
      . Thanks @ccaprani, @masatohoshino.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Android gateway setup now gives specific recovery actions for expired
      codes, stale credentials, pending node approval, and terminal authentication
      failures. #99414 Related #98045 , #98046 . Thanks @ccaprani.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'The iOS app can now connect through Cloudflare Access, Basic authentication,
      and similar proxies by storing per-Gateway credential headers for the next reconnect.
      #100768'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'The macOS Dashboard now follows a restarted remote SSH tunnel to its new
      local port automatically and keeps authentication tokens out of logged URLs.
      #100488'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Opening Control -> Terminal on iOS now goes directly to the terminal without
      briefly showing the general Web UI login screen during connection. #100727'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Starting QR login without a required official channel plugin now returns
      the exact installation command or openclaw doctor --fix instead of only saying
      the provider is unavailable. #90517 Related #83277 . Thanks @carol-iung, @tuaran.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'When Google Meet''s local OAuth callback port is occupied, openclaw meet
      auth login now offers the manual redirect-paste flow instead of stopping sign-in.
      #96492 Thanks @jinduwang1001-max, @yetval.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Valid openclaw.json files with a BOM, PowerShell formatting, or deep indentation
      can now save authentication, model, repair, and other configuration changes
      without manual reformatting. #100591 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'When cron command output is truncated, operators can still recover the
      earlier login or setup instruction they need without exposing its raw secret
      through notifications. #96393 Related #96346 . Thanks @nz365guy.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'A focused device-pairing Doctor lint check now provides structured warnings
      and repair guidance for pending requests, stale authentication, missing scopes,
      and unreadable stores. #97366 Thanks @giodl73-repo.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Fresh git installs now lead users through setup, or give the exact command
      to finish later, before missing configuration or Gateway authentication can
      break first use. #101901 Thanks @fuller-stack-dev.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Windows update and doctor repair now move an owned legacy Startup gateway
      to Task Scheduler without leaving a stale process, dropping authentication,
      or removing the fallback too early. #101213 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Strengthened Android gateway authentication coverage by making a timing-sensitive
      recovery check more reliable. #83826 Thanks @neatguycoding.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Centralized credential masking and secure secret comparison to keep authentication
      behavior consistent across supported workflows. #99746 Thanks @romneyda.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Consolidated internal hashing across authentication, sessions, approvals,
      identifiers, and plugins without changing compatibility. #99788 Thanks @romneyda.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Narrowed Google Meet integration internals without changing setup, authentication,
      or call behavior. #102010 Thanks @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 69-account-and-access-changes-in-v2026-7-1
  source_release: openclaw-2026-07-13-v2026-7-1-c2063718
  source_type: openclaw_changelog
  theme: account-access
  title: 69 Account and Access changes in v2026.7.1
  type: change
related_changes:
- '[[Changes/Claude Code/2026-07-10-gateway-login-now-supports-anthropic-operated-public-gateway-endpoints|Gateway:
  /login now supports Anthropic-operated public gateway endpoints]]'
- '[[Changes/GitHub Copilot CLI/2026-07-10-2-account-and-access-changes-in-v1-0-70|2
  Account and Access changes in v1.0.70]]'
- '[[Changes/Lovable/2026-07-10-sign-in-to-lovable-from-your-identity-provider-s-portal|Sign
  in to Lovable from your identity provider''s portal]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-07-13-v2026-7-1-c2063718|openclaw-2026-07-13-v2026-7-1-c2063718]]'
source_type: openclaw_changelog
theme: account-access
title: 69 Account and Access changes in v2026.7.1
type: change
---

<!-- chronolog:begin region="header" -->
# 69 Account and Access changes in v2026.7.1

**OpenClaw** · 2026-07-13 · [[Themes/account-access|Account and Access]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.7.1) · from [[Releases/OpenClaw/openclaw-2026-07-13-v2026-7-1-c2063718|v2026.7.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> The Gateway Dashboard login now fits and behaves better on phones and short windows, with larger touch targets, easier URL entry, and reachable recovery help. #100208

> Temporary Gateway disconnects no longer replace an authenticated Control UI page with the login screen, preserving dashboard context while automatic reconnection continues. #100479

> A failed Control UI login or Gateway connection now immediately shows the error, recovery steps, and relevant documentation link instead of hiding them in a collapsed panel. f9e194e

> Users with saved working dashboard credentials no longer see the login screen flash briefly while Control UI reconnects. #101849

> Owners and admins can now restore an expired Codex or OpenAI login from a browser through private Telegram, Web UI, Discord, or Slack commands without SSH access. #98006 Thanks @100yenadmin, @jalehman, @obviyus.

> macOS onboarding now verifies the chosen AI connection before first chat, presents clearer local and remote setup choices, and offers friendly recovery or a verified manual API-key path when authentication fails. #100288

> First-time onboarding now preserves earlier choices after authentication or pairing trouble and gives users an actionable model-configuration next step instead of opening an unusable first chat. #100632

> OpenClaw model selection expands across major hosted, managed, and local choices. Each supported provider route retains its own authentication, model limits, reasoning controls, tool behavior, image support, and usage reporting.

> Tencent Hunyuan Hy3 now has a complete setup path through TokenHub or TokenPlan, including first-class authentication choices, CLI onboarding, model discovery, and configuration validation. Existing TokenHub configurations retain access to hy3-preview alongside the stable hy3 model.

> Operators can configure Meta Model API with MODEL_API_KEY or the onboarding authentication choice, select meta-model-api/muse-spark-1.1 , and use supported streaming, tool calling, image input, and reasoning-effort controls.

> Tencent Hunyuan Hy3 now has a complete supported OpenClaw setup path through TokenHub or TokenPlan, including first-class authentication, model discovery, configuration validation, CLI onboarding, and compatibility for existing hy3-preview setups. #99076 Thanks @moncac.

> openclaw channels login --channel feishu now prints a compact QR code that stays scannable in a normal terminal window. #97087 Thanks @nianjiuzst.

> Telegram rich replies and progress messages containing OAuth email addresses now arrive instead of being rejected by Telegram validation. #95900 Thanks @obviyus.

> Slack, Discord, Telegram, WhatsApp, and Microsoft Teams users now receive a clear retry and re-authentication message when a model provider returns a recognized HTTP 401 error instead of seeing only a reaction or no useful reply. #96599 Thanks @sjf-oa.

> Slack startup and account checks now warn when a user OAuth credential is configured as the bot token, before identity confusion affects mentions or replies. #99931 Thanks @ooiuuii.

> openclaw channels login --channel whatsapp now replaces expired QR codes in place so interactive terminals show one current, scannable code. #100159

> After /login codex succeeds in Telegram, retrying the request now uses the newly authenticated OpenAI profile instead of the previous account. fca0c81 Thanks @100yenadmin.

> Ollama Cloud setup now stops oversized or malicious authentication responses before they can consume excessive memory, while normal sign-in remains unchanged. #97581 Thanks @hugenshen.

> For Codex-backed OpenAI models, /status now identifies ChatGPT login authentication as oauth (codex-cli) instead of incorrectly labeling it as an environment API key. #91240 Related #91099 . Thanks @849261680, @ukstem.

> OpenAI OAuth usage checks now cap oversized WHAM rate-limit responses before they can destabilize the process. #97702 Thanks @cxbasdev.

> ChatGPT OAuth sign-in and refresh now reject unexpectedly large token responses cleanly instead of risking Gateway memory exhaustion. #99479 Thanks @pandah97.

> OpenAI-compatible providers routed through the GitHub Copilot BYOK harness now retain bearer authentication, reducing false 401 errors for valid credentials. #99955 Thanks @hxy91819.

> OpenAI/Codex and Anthropic OAuth result pages now show OpenClaw branding instead of the legacy Pi logo. 1834592

> Chutes login, user lookup, and token refresh now stop unexpectedly large OAuth responses with a bounded error instead of buffering them without limit. #96777 Thanks @wangmiao0668000666.

> xAI and Grok OAuth sign-in now works on SSH hosts, containers, VPS systems, and other headless environments without forwarding a localhost callback port. #97249 Thanks @fuller-stack-dev, @jaaneek.

> GitHub Copilot sign-in, refresh, and model-list checks now fail with labeled size limits when GitHub or a proxy returns an oversized response. #97499 Thanks @wangmiao0668000666.

> Z.AI users can recover a profile that accidentally stored an onboarding command as the API key without wiping all authentication state. #97520 Thanks @zhangguiping-xydt.

> xAI sign-in, token refresh, and device approval now stop oversized OAuth responses before they can consume unbounded memory. #97615 Thanks @cxbasdev.

> Google OAuth sign-in, token exchange, and project discovery now return a bounded error for oversized responses instead of risking a process crash. #97628 Thanks @vincentkoc, @wangmiao0668000666.

> OpenRouter model probes and agent requests now use discovered environment or profile API keys correctly instead of failing with a missing-authentication-header error. #98187 Related #97934 . Thanks @laurencebrown, @sunlit-deng.

> ChatGPT OAuth-backed Responses sessions now retain backend affinity across turns, improving prompt-cache reuse and reducing repeated processing of the same conversation context. #100233 Thanks @marvinthebored, @obviyus, @peetiegonzalez.

> Anthropic sign-in now rejects unsupported callback-host overrides, keeps authorization on standard local loopback addresses, and avoids callback failures or exposure through a non-local listener. #96917 Thanks @xialonglee.

> Expired Claude CLI authentication now shows the exact recovery command claude auth login && openclaw models auth login --provider anthropic --method cli instead of a generic failure. #97669 Thanks @alix-007.

> Cloudflare 403 challenges on OpenAI or Codex OAuth requests now produce gateway-block guidance instead of incorrectly telling users their authentication failed. #94440 Related #94432 . Thanks @lzyyzznl, @pbm9z95m6z-hue.

> OpenAI authentication errors now point ChatGPT/Codex OAuth users to a model compatible with their existing sign-in instead of recommending an outdated default. #100579 Thanks @zhangguiping-xydt.

> Codex app-server runs with an invalid ChatGPT OAuth session now surface the real sign-in error promptly instead of waiting for a misleading ten-second authentication timeout. #100713 Thanks @lin-hongkuan.

> After /model changes a session's provider, /status and session_status now report that provider's usage, authentication, runtime, and context details rather than stale defaults. #93384 Thanks @obviyus, @osolmaz, @rollingshmily, @samiralibabic, @zhangguiping-xydt.

> Request-format and schema failures now show the relevant diagnostic without sending users through unnecessary provider login or reconfiguration steps. #95779 Thanks @pick-cat.

> Existing xAI and Grok OAuth sessions using the retired token endpoint can renew after expiry without forcing another browser or SSH-tunneled login. #96146 Thanks @fuller-stack-dev, @jaaneek.

> OpenRouter sign-in now fails safely on oversized replies, and Discord webhook sends remain successful when their optional response body is absent, malformed, or too large. #98098 Thanks @lwy-2.

> Channel replies can now continue as soon as an embedded-agent turn finishes instead of waiting roughly 50 seconds for post-run authentication bookkeeping. #85829 Thanks @turbotheturtle.

> Gateway startup no longer performs unsolicited provider-auth discovery across every configured agent, helping channels and local commands remain responsive while authentication loads on demand. #100667 Thanks @vincentkoc.

> Gateway connection failures now identify the last completed handshake phase, helping operators distinguish upgrade, credential, authentication, session, and ready-state stalls. #93402 Thanks @849261680, @bzelones, @vincentkoc, @youngting520.

> Gateway override authentication errors now tell CLI and TUI users whether to add a token or password, remove --url , or pair the relevant environment variables. #100418 Thanks @gmays.

> First-run macOS setup now recognizes a successfully saved Codex login and is less likely to finish with a stale Gateway or bundled-skills warning. #101218

> Slack rooms that require a mention no longer wake OpenClaw for ordinary messages when the bot identity is missing or untrusted, and setup warnings point operators to a Bot User OAuth Token when needed. #91584 Thanks @hiragram.

> openclaw doctor --fix now preserves separate OAuth accounts for the same provider, including each account reference and saved display name. #97541 Thanks @liuhao1024, @yetval.

> Gateway authentication retries now send stored device tokens only to true loopback endpoints, not remote hostnames that merely resemble 127.* addresses. #99859 Thanks @ly85206559.

> /login codex now switches the active chat to the account just authenticated without overwriting a newer manual profile choice, and gives recovery guidance if the switch fails. 02c3de9 Thanks @vincentkoc.

> Profile changes made through /login now use the standard session save path, preserving newer concurrent selections and existing recovery behavior. f07c478 Thanks @vincentkoc.

> Masked malformed credentials now stay on one safe line in setup and authentication diagnostics even when the original input contains newlines or other control bytes. #96445 Thanks @lin-hongkuan.

> When another OpenClaw process is refreshing OpenAI OAuth credentials, operators now see one useful contention error without duplicated wording or exposed local file paths. #101573 Thanks @vincentkoc.

> Android connection recovery now identifies expired setup codes, stale credentials, and missing or invalid authentication with the appropriate next step. #98094 Thanks @qingminglong.

> Android Gateway setup now replaces a generic authentication warning with specific recovery labels for expired setup codes, missing or invalid credentials, stale saved authentication, and required device identity. #98698 Related #98046 . Thanks @ccaprani, @masatohoshino.

> Android gateway setup now gives specific recovery actions for expired codes, stale credentials, pending node approval, and terminal authentication failures. #99414 Related #98045 , #98046 . Thanks @ccaprani.

> The iOS app can now connect through Cloudflare Access, Basic authentication, and similar proxies by storing per-Gateway credential headers for the next reconnect. #100768

> The macOS Dashboard now follows a restarted remote SSH tunnel to its new local port automatically and keeps authentication tokens out of logged URLs. #100488

> Opening Control -> Terminal on iOS now goes directly to the terminal without briefly showing the general Web UI login screen during connection. #100727

> Starting QR login without a required official channel plugin now returns the exact installation command or openclaw doctor --fix instead of only saying the provider is unavailable. #90517 Related #83277 . Thanks @carol-iung, @tuaran.

> When Google Meet's local OAuth callback port is occupied, openclaw meet auth login now offers the manual redirect-paste flow instead of stopping sign-in. #96492 Thanks @jinduwang1001-max, @yetval.

> Valid openclaw.json files with a BOM, PowerShell formatting, or deep indentation can now save authentication, model, repair, and other configuration changes without manual reformatting. #100591 Thanks @vincentkoc.

> When cron command output is truncated, operators can still recover the earlier login or setup instruction they need without exposing its raw secret through notifications. #96393 Related #96346 . Thanks @nz365guy.

> A focused device-pairing Doctor lint check now provides structured warnings and repair guidance for pending requests, stale authentication, missing scopes, and unreadable stores. #97366 Thanks @giodl73-repo.

> Fresh git installs now lead users through setup, or give the exact command to finish later, before missing configuration or Gateway authentication can break first use. #101901 Thanks @fuller-stack-dev.

> Windows update and doctor repair now move an owned legacy Startup gateway to Task Scheduler without leaving a stale process, dropping authentication, or removing the fallback too early. #101213 Thanks @vincentkoc.

> Strengthened Android gateway authentication coverage by making a timing-sensitive recovery check more reliable. #83826 Thanks @neatguycoding.

> Centralized credential masking and secure secret comparison to keep authentication behavior consistent across supported workflows. #99746 Thanks @romneyda.

> Consolidated internal hashing across authentication, sessions, approvals, identifiers, and plugins without changing compatibility. #99788 Thanks @romneyda.

> Narrowed Google Meet integration internals without changing setup, authentication, or call behavior. #102010 Thanks @vincentkoc.

Source: https://docs.openclaw.ai/releases/2026.7.1
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/OpenClaw/2026-07-13-5-projects-and-workspaces-changes-in-v2026-7-1|5 Projects and Workspaces changes in v2026.7.1]] · Projects and Workspaces
- [[Changes/OpenClaw/2026-07-13-99-developer-workflow-changes-in-v2026-7-1|99 Developer Workflow changes in v2026.7.1]] · Developer Workflow
- [[Changes/OpenClaw/2026-07-13-69-context-window-changes-in-v2026-7-1|69 Context Window changes in v2026.7.1]] · Context Window
- [[Changes/OpenClaw/2026-07-13-10-accessibility-and-localization-changes-in-v2026-7-1|10 Accessibility and Localization changes in v2026.7.1]] · Accessibility and Localization
- [[Changes/OpenClaw/2026-07-13-64-interface-experience-changes-in-v2026-7-1|64 Interface Experience changes in v2026.7.1]] · Interface Experience
- [[Changes/OpenClaw/2026-07-13-whatsapp-and-telegram-default-account-routing-warnings-are-now-available-through|WhatsApp and Telegram default-account routing warnings are now available through…]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-07-13-132-agent-mode-changes-in-v2026-7-1|132 Agent Mode changes in v2026.7.1]] · Agent Mode
- [[Changes/OpenClaw/2026-07-13-after-one-generated-video-clip-is-ready-a-different-next-clip-can-start-immediat|After one generated video clip is ready, a different next clip can start immediately…]] · Video Generation
- [[Changes/OpenClaw/2026-07-13-79-automation-and-scheduling-changes-in-v2026-7-1|79 Automation and Scheduling changes in v2026.7.1]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-07-13-130-model-support-changes-in-v2026-7-1|130 Model Support changes in v2026.7.1]] · Model Support
- [[Changes/OpenClaw/2026-07-13-59-safety-and-privacy-changes-in-v2026-7-1|59 Safety and Privacy changes in v2026.7.1]] · Safety and Privacy
- [[Changes/OpenClaw/2026-07-13-224-mobile-and-desktop-changes-in-v2026-7-1|224 Mobile and Desktop changes in v2026.7.1]] · Mobile and Desktop
- [[Changes/OpenClaw/2026-07-13-83-voice-and-audio-changes-in-v2026-7-1|83 Voice and Audio changes in v2026.7.1]] · Voice and Audio
- [[Changes/OpenClaw/2026-07-13-18-pricing-model-changes-in-v2026-7-1|18 Pricing Model changes in v2026.7.1]] · Pricing Model
- [[Changes/OpenClaw/2026-07-13-21-editor-experience-changes-in-v2026-7-1|21 Editor Experience changes in v2026.7.1]] · Editor Experience
- [[Changes/OpenClaw/2026-07-13-7-image-generation-changes-in-v2026-7-1|7 Image Generation changes in v2026.7.1]] · Image Generation
- [[Changes/OpenClaw/2026-07-13-channel-setup-warnings-are-now-available-as-structured-doctor-lint-findings-with|Channel setup warnings are now available as structured Doctor lint findings…]] · Automation and Scheduling
- [[Changes/OpenClaw/2026-07-13-4-enterprise-and-administration-changes-in-v2026-7-1|4 Enterprise and Administration changes in v2026.7.1]] · Enterprise and Administration
- [[Changes/OpenClaw/2026-07-13-2-presentation-creation-changes-in-v2026-7-1|2 Presentation Creation changes in v2026.7.1]] · Presentation Creation
- [[Changes/OpenClaw/2026-07-13-136-memory-and-personalization-changes-in-v2026-7-1|136 Memory and Personalization changes in v2026.7.1]] · Memory and Personalization
- [[Changes/OpenClaw/2026-07-13-213-apps-and-integrations-changes-in-v2026-7-1|213 Apps and Integrations changes in v2026.7.1]] · Apps and Integrations
- [[Changes/OpenClaw/2026-07-13-8-search-and-browsing-changes-in-v2026-7-1|8 Search and Browsing changes in v2026.7.1]] · Search and Browsing
- [[Changes/OpenClaw/2026-07-13-20-collaboration-changes-in-v2026-7-1|20 Collaboration changes in v2026.7.1]] · Collaboration
- [[Changes/OpenClaw/2026-07-13-13-files-and-data-changes-in-v2026-7-1|13 Files and Data changes in v2026.7.1]] · Files and Data
- [[Changes/OpenClaw/2026-07-13-19-multimodal-input-changes-in-v2026-7-1|19 Multimodal Input changes in v2026.7.1]] · Multimodal Input
- [[Changes/OpenClaw/2026-07-13-38-reliability-and-performance-changes-in-v2026-7-1|38 Reliability and Performance changes in v2026.7.1]] · Reliability and Performance
- [[Changes/OpenClaw/2026-07-13-686-other-changes-in-v2026-7-1|686 other changes in v2026.7.1]] · Other changes
- [[Changes/OpenClaw/2026-07-13-official-openclaw-container-images-are-now-available-from-docker-hub-as-well-as|Official OpenClaw container images are now available from Docker Hub as well…]] · Other changes
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Account and Access

- Earlier: 2026-07-10 · Lovable · [[Changes/Lovable/2026-07-10-sign-in-to-lovable-from-your-identity-provider-s-portal|Sign in to Lovable from your identity provider's portal]]
- Later: 2026-07-13 · OpenCode · [[Changes/OpenCode/2026-07-13-core-added-oauth-support-for-luna-responses-lite|Core Added OAuth support for Luna Responses Lite]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-30 · Cursor · [[Changes/Cursor/2023-03-30-ai-now-requires-login|AI now requires login]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-07-13-93adbc&body=Card%3A%20Changes%2FOpenClaw%2F2026-07-13-69-account-and-access-changes-in-v2026-7-1.md%0ACard%20ID%3A%20openclaw-2026-07-13-93adbc%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.7.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->