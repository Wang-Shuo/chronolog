---
card_id: openclaw-2026-07-13-9f5a75
date: '2026-07-13'
description: 'OpenClaw · 2026-07-13 · Safety and Privacy: 59 changes in v2026.7.1
  — Chat controls are clearer while work is in progress. The composer keeps attachments…'
diffusion:
  first_in_tracked: '[[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke
    Application Access]]'
  inference: No adoption, equivalence, or causation claim.
  lag_days: 2176
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: safety-privacy
  tracked_products_count: 37
evolves_from: []
extractor_version: fallback-v5
impact: incremental
kind: digest
machine_hash: a23332017d567a3861b66f77dbd331384344e0e7ff6fd014a0a4b81742877434
product: openclaw
product_name: OpenClaw
record:
  card_id: openclaw-2026-07-13-9f5a75
  comparison: ''
  date: '2026-07-13'
  description: 'OpenClaw — v2026.7.1: 59 Safety and Privacy changes'
  evidence:
  - quote: Chat controls are clearer while work is in progress. The composer keeps
      attachments, model choice, voice, reasoning, send and stop state, and message
      actions usable across screen sizes; Talk users can choose or refresh a microphone
      from settings and get readable permission guidance on narrow screens; quoted
      replies preserve the point being answered; and compact tool rows keep inputs,
      results, images, progress, errors, approvals, and steering available without
      overwhelming the conversation.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Control UI Talk users can choose and refresh a microphone on narrow screens
      and read clear permission guidance when browser access is blocked. #101377 Thanks
      @fuller-stack-dev.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'External tools can now receive session-scoped Gateway access without process-wide
      credentials or permission to impersonate another session, forming the secure
      base for openclaw attach . #96351 Thanks @anagnorisis2peripeteia, @obviyus.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'OpenRouter scans now interpret model names such as 8b-70b by their larger
      parameter size, improving minimum-size filters and small-model security warnings.
      #96288 Thanks @ly-wang19.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'CLI-backed agents now keep conversation continuity across prompt-only
      changes, avoiding needless cold starts while still resetting when security or
      runtime conditions require it. #99822 Related #99729 . Thanks @obviyus.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Operators can now set OPENCLAW_SANDBOX_IMAGE to build revision-specific
      sandbox image tags for controlled rollout and rollback. #99915'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Docker-backed sandbox file and shell commands now fail promptly with the
      original input-stream error instead of crashing, hanging, or remaining pending.
      #101032 Thanks @cxbasdev.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Busy or slower hosts now give Codex native permission checks and pre-tool
      hooks more time to finish, reducing dropped policy decisions. 123ec16 Thanks
      @vincentkoc.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Agent runs, Doctor, and Gateway tool views now describe access using the
      same policy that actually governs the run, reducing confusing permission mismatches.
      #99817'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'SSH-backed sandbox commands and uploads now stop cleanly, clean up child
      processes, and preserve the useful error when an input or output stream fails.
      #101031 Thanks @cxbasdev.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'ACP runtime controls can now truly clear saved model, thinking, working-directory,
      permission, timeout, mode, and backend-extra settings so later turns do not
      reuse stale values. #101044 Thanks @mushuiyu886.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'ACP tool titles, permission prompts, warnings, and errors now keep long
      emoji or CJK argument previews readable when shortened. #101535 Thanks @lsr911.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Credential resolution and redaction now cover more model and plugin paths,
      while sandboxing and approvals enforce clearer device, permission, and workspace
      boundaries. The secrets workflow also avoids exposing resolved model credentials
      in ordinary request and error paths.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Browser control now requires the same administrator permission through
      direct node invocation as through the standard browser request path, preventing
      write-only credentials or third-party plugins from gaining elevated access.
      #85916 Thanks @eleqtrizit, @laphilosophie.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'In shared channels, only the person who started a Claude Code command
      can approve or deny its tool permission requests. #98256 Thanks @eleqtrizit.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Approving a node that can handle sensitive browser traffic now requires
      administrator permission, matching the security level already required to use
      that capability. #104491 Thanks @yetval.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Under strict SSRF policy, remote-browser discovery can no longer redirect
      OpenClaw from the configured CDP endpoint to a different host, port, or security
      mode. cbc833a Thanks @vincentkoc.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Running /prose now shows operators the transitive remote imports and asks
      for consent before OpenProse fetches those code dependencies. 259877d Thanks
      @joshavant.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: OpenShell workspace file operations now stay inside the validated local
      sandbox mirror, with unsafe symlink, hard-link, cross-root, and changing-directory
      cases failing cleanly. c6f5725 Thanks @joshavant.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Security audits no longer mistake bundled placeholder keys for LM Studio,
      Ollama, and other keyless local providers as exposed plaintext credentials.
      #97622 Thanks @xydigit-sj.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Android SMS commands now clearly distinguish phone permission from the
      Gateway''s separate opt-in, allowing read-only sms.search without also enabling
      sms.send . #100993 Thanks @narcissus0702.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Config recovery now warns when the file was repaired but its final permissions
      could not be hardened, preserving the recovery while exposing the security issue.
      #95348 Thanks @hugenshen.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'openclaw security audit now reports Browser exposure only when plugin
      policy actually allows the Browser plugin to run. #97732 Thanks @amtellezfernandez.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Third-party Android builds can allow Gateway-requested location checks
      while the app is in the background by selecting Location > Always and granting
      Android''s persistent location permission. #100967 Thanks @ioridev.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Android one-shot camera captures now turn the camera and privacy indicator
      off promptly after success, failure, or cancellation. #98040 Thanks @nianjiuzst.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Android''s selected-photos permission now counts as usable access, allowing
      photos.latest while clearly showing how to manage the limited selection. #98059
      Thanks @nianjiuzst.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Android onboarding now finishes after permission-triggered node approval
      instead of trapping users in a loop between the Permissions and approval screens.
      #100959'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Android Gateway discovery, QR and manual setup, connection checks, approvals,
      and permission guidance now use the selected language across the translations
      in this release. Sources: 28062c8 , 3d43858 , ad74b32 , 1b07620 , 4fa4c9e ,
      1dd5230 , 9db7ec5 , e6f8788 , e5cf67e , b52d988 , cd3b4ee , c3bcb9f , 8af3aa0
      , c34e79e , c9c8f6c , 255e251 , 0e98ba4 , 0cc9927 , 97955d9 , ba449f2 , 0e22e54
      , ae65251 , d957f5a .'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Broader native app setup, chat, Talk, permission, connection, session,
      provider, and status text now uses the selected language across the language
      packs updated in this release. Sources: a39b07b , f8e1e0c , db27d2e , 28a8414
      , e8e96bf , 6ea407d , 0011a18 , 8c5adbf , 019603d , d3d7282 , 267898c , 55ed57a
      , c54dc67 , fd0355d , 49726a5 , 2ffeedf , #98043 , beca2b1 , 4078dc7 , e7e98f6
      , 3020f78 , 0c82908 , 8a3935f , 3f289fd , 203a896 , 6afef15 . Thanks @yeager.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Native photo-permission controls now explain limited, selected, and recent-photo
      access in the selected language across the translations in this release. Sources:
      c360f92 , 4dd027e , 9cde1ca , 328fb70 , 71e5fcc , b11d710 , 55a2a9b , c4b40d0
      , 3a1b983 , dea40a5 , 4b1fab8 , 44ca739 , d36452c , a50a59e , 49b68e1 , 122e4ba
      , 4086d35 , 547a563 , 538f28a , c5afa92 , 32a986d .'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'iOS location settings now explain Off, While Using, Always, Precise Location,
      restrictions, and permission mismatches in the selected language across the
      translations in this release. Sources: 3542585 , 261d79a , ef1474d , cc1d61b
      , 2a1e118 , 748bfee , e0b2dda , f371a2f , ee00cc7 , 27f9ae0 , 51a07ae , ba9d167
      , 576169e , 10500a6 , a344252 , d7d280f , cb2547f , 2191c2e , c63e9f9 , 4b1e0de
      , 525c4c7 .'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Native skill availability, Gateway setup, diagnostics, privacy, and access
      guidance now use the selected language across the translations in this release.
      Sources: fdcd5c0 , 26f6735 , 5220eff , bb7dbda , 952245b , edb1e74 , f7bad57
      , 0602930 , e779b8f , 0400be7 , 851d0ad , 1e0dd95 , 703e1ad , 1c93e50 , 37c45f2
      , 8fe917b , da21e4b , f4f63b1 , 3e4febb , a82cd35 , 52323b6 .'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'The iOS app now applies OpenClaw''s palette consistently across Talk,
      settings, Gateway, privacy, usage, and workboard views while retaining accessible
      contrast. #98930 Thanks @joelnishanth.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'iOS location settings now show the permission that is actually in effect,
      including Precise Location and mismatches between OpenClaw''s selected mode
      and the iOS grant. #99247 Thanks @pollybot13.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'iOS Calendar, Reminders, and Contacts commands now return an immediate
      permission-required result instead of opening a prompt that leaves the agent
      request waiting. #99477 Thanks @nianjiuzst.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: The iOS app now recovers when a location permission prompt returns without
      a clear decision instead of waiting indefinitely. 75c8753 Thanks @vincentkoc.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: The iOS camera permission prompt now clearly connects access to Gateway
      setup and assistant-requested photo, video, document, screen, or workspace capture.
      e77994e Thanks @joshavant.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'The macOS menu-bar app now uses fewer idle CPU wakeups and less repeated
      configuration and permission work, reducing background battery use without changing
      active status behavior. #100463'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'LaunchAgent-managed Gateways on permission-constrained macOS volumes now
      start the generated environment wrapper through /bin/sh , preventing immediate
      background-service exits. #89967 Related #87199 . Thanks @joshdaynard, @zhangguiping-xydt.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'doctor --lint --all can now explain the path or permission that would
      block a configuration repair before operators run doctor --fix . #100093 Thanks
      @giodl73-repo.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: Logbook users now have end-to-end guidance for setup, model routing, privacy
      choices, and troubleshooting missing capture or timeline results. b6a7898
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: ACP troubleshooting now names PermissionPromptUnavailableError , helping
      operators recognize a non-interactive permission failure and find the right
      configuration fix. b3a74cc
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'A broad reliability pass now replaces stalled child-process work with
      clear errors, improves sandbox diagnostics, bounds mobile calendar and voice
      state, normalizes cron fallbacks, and rejects unsafe provider responses. #100483
      Thanks @aniruddhaadak80, @cxbasdev, @jincheng-xydt, @morluto, @nianjiuzst, @pandah97,
      @versatagent, @xialonglee, @zenglingbiao, @zengwen-dt.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'SSH- and OpenShell-backed sandbox commands now clean up remote resources
      after failed launches, preserve the correct plugin session and channel context,
      and return a normal tool error for malformed input instead of an internal WeakMap
      failure. #96926 Thanks @jesse-merhi.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Docker sandbox commands now return an explicit failure when output cannot
      be read instead of crashing OpenClaw or reporting an incomplete result as successful.
      #100523 Thanks @cxbasdev.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: OpenShell sandbox sessions now start with the intended workspace files
      in the managed remote directory, avoiding missing-file and wrong-directory failures.
      d9034da Thanks @vincentkoc.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: The optional common sandbox image now includes Node 24 and pnpm so documented
      Node-based development tasks can run inside it. eabc12b Thanks @vincentkoc.
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'OpenShell sandbox uploads now place workspace directories at the requested
      remote path so sandbox commands can reliably find their files. #96303 Thanks
      @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Added clearer policy coverage reporting so maintainers can spot gaps as
      security-sensitive configuration evolves. #87081 Thanks @giodl73-repo.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Expanded browser safety coverage on Windows systems that support directory
      links, improving test portability. #90365 Thanks @aniruddhaadak80.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Expanded automated security review for code that launches local processes,
      helping catch high-severity risks before merge. #92667 Thanks @hxy91819.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Made QQBot and Zalo security tests depend on actual symlink support instead
      of the operating system name. #95531 Thanks @aniruddhaadak80, @vincentkoc.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Documented how contributors should route issues, support requests, security
      reports, and pull requests. #96714 Thanks @100yenadmin.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Restored green lint validation while preserving earlier Tailscale and
      Feishu safety fixes. #98598 Related #98462 , #98464 . Thanks @zhanglei99586.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Prevented test-only proxy assertions from causing false network-safety
      validation failures. #99233 Thanks @joshavant.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Removed an unused Slack download path, reducing security-sensitive maintenance
      while preserving private-file and image downloads. #99944 Thanks @miorbnli.'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Sped up package-candidate safety validation without changing the protections
      it provides. #100008'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Improved the safety and consistency of maintainer validation for heavy
      workloads and untrusted contributions. #100220'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  - quote: 'Improved the reliability and security of documentation translation checks.
      #103244'
    source_release: https://docs.openclaw.ai/releases/2026.7.1
  extractor_version: fallback-v5
  impact: incremental
  kind: digest
  product: openclaw
  product_name: OpenClaw
  slug: 59-safety-and-privacy-changes-in-v2026-7-1
  source_release: openclaw-2026-07-13-v2026-7-1-c2063718
  source_type: openclaw_changelog
  theme: safety-privacy
  title: 59 Safety and Privacy changes in v2026.7.1
  type: change
related_changes:
- '[[Changes/Claude Code/2026-07-11-2-safety-and-privacy-changes-in-v2-1-207|2 Safety
  and Privacy changes in v2.1.207]]'
- '[[Changes/Google Antigravity/2026-07-13-refined-command-permission-prompting-with-strict-literal-matching-relaxed-redire|Refined
  command permission prompting with strict literal matching, relaxed…]]'
- '[[Changes/Lovable/2026-07-13-redesigned-settings|Redesigned settings]]'
source_release: '[[Releases/OpenClaw/openclaw-2026-07-13-v2026-7-1-c2063718|openclaw-2026-07-13-v2026-7-1-c2063718]]'
source_type: openclaw_changelog
theme: safety-privacy
title: 59 Safety and Privacy changes in v2026.7.1
type: change
---

<!-- chronolog:begin region="header" -->
# 59 Safety and Privacy changes in v2026.7.1

**OpenClaw** · 2026-07-13 · [[Themes/safety-privacy|Safety and Privacy]] · Digest · [Official source](https://docs.openclaw.ai/releases/2026.7.1) · from [[Releases/OpenClaw/openclaw-2026-07-13-v2026-7-1-c2063718|v2026.7.1]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
## Changes in this digest

> Chat controls are clearer while work is in progress. The composer keeps attachments, model choice, voice, reasoning, send and stop state, and message actions usable across screen sizes; Talk users can choose or refresh a microphone from settings and get readable permission guidance on narrow screens; quoted replies preserve the point being answered; and compact tool rows keep inputs, results, images, progress, errors, approvals, and steering available without overwhelming the conversation.

> Control UI Talk users can choose and refresh a microphone on narrow screens and read clear permission guidance when browser access is blocked. #101377 Thanks @fuller-stack-dev.

> External tools can now receive session-scoped Gateway access without process-wide credentials or permission to impersonate another session, forming the secure base for openclaw attach . #96351 Thanks @anagnorisis2peripeteia, @obviyus.

> OpenRouter scans now interpret model names such as 8b-70b by their larger parameter size, improving minimum-size filters and small-model security warnings. #96288 Thanks @ly-wang19.

> CLI-backed agents now keep conversation continuity across prompt-only changes, avoiding needless cold starts while still resetting when security or runtime conditions require it. #99822 Related #99729 . Thanks @obviyus.

> Operators can now set OPENCLAW_SANDBOX_IMAGE to build revision-specific sandbox image tags for controlled rollout and rollback. #99915

> Docker-backed sandbox file and shell commands now fail promptly with the original input-stream error instead of crashing, hanging, or remaining pending. #101032 Thanks @cxbasdev.

> Busy or slower hosts now give Codex native permission checks and pre-tool hooks more time to finish, reducing dropped policy decisions. 123ec16 Thanks @vincentkoc.

> Agent runs, Doctor, and Gateway tool views now describe access using the same policy that actually governs the run, reducing confusing permission mismatches. #99817

> SSH-backed sandbox commands and uploads now stop cleanly, clean up child processes, and preserve the useful error when an input or output stream fails. #101031 Thanks @cxbasdev.

> ACP runtime controls can now truly clear saved model, thinking, working-directory, permission, timeout, mode, and backend-extra settings so later turns do not reuse stale values. #101044 Thanks @mushuiyu886.

> ACP tool titles, permission prompts, warnings, and errors now keep long emoji or CJK argument previews readable when shortened. #101535 Thanks @lsr911.

> Credential resolution and redaction now cover more model and plugin paths, while sandboxing and approvals enforce clearer device, permission, and workspace boundaries. The secrets workflow also avoids exposing resolved model credentials in ordinary request and error paths.

> Browser control now requires the same administrator permission through direct node invocation as through the standard browser request path, preventing write-only credentials or third-party plugins from gaining elevated access. #85916 Thanks @eleqtrizit, @laphilosophie.

> In shared channels, only the person who started a Claude Code command can approve or deny its tool permission requests. #98256 Thanks @eleqtrizit.

> Approving a node that can handle sensitive browser traffic now requires administrator permission, matching the security level already required to use that capability. #104491 Thanks @yetval.

> Under strict SSRF policy, remote-browser discovery can no longer redirect OpenClaw from the configured CDP endpoint to a different host, port, or security mode. cbc833a Thanks @vincentkoc.

> Running /prose now shows operators the transitive remote imports and asks for consent before OpenProse fetches those code dependencies. 259877d Thanks @joshavant.

> OpenShell workspace file operations now stay inside the validated local sandbox mirror, with unsafe symlink, hard-link, cross-root, and changing-directory cases failing cleanly. c6f5725 Thanks @joshavant.

> Security audits no longer mistake bundled placeholder keys for LM Studio, Ollama, and other keyless local providers as exposed plaintext credentials. #97622 Thanks @xydigit-sj.

> Android SMS commands now clearly distinguish phone permission from the Gateway's separate opt-in, allowing read-only sms.search without also enabling sms.send . #100993 Thanks @narcissus0702.

> Config recovery now warns when the file was repaired but its final permissions could not be hardened, preserving the recovery while exposing the security issue. #95348 Thanks @hugenshen.

> openclaw security audit now reports Browser exposure only when plugin policy actually allows the Browser plugin to run. #97732 Thanks @amtellezfernandez.

> Third-party Android builds can allow Gateway-requested location checks while the app is in the background by selecting Location > Always and granting Android's persistent location permission. #100967 Thanks @ioridev.

> Android one-shot camera captures now turn the camera and privacy indicator off promptly after success, failure, or cancellation. #98040 Thanks @nianjiuzst.

> Android's selected-photos permission now counts as usable access, allowing photos.latest while clearly showing how to manage the limited selection. #98059 Thanks @nianjiuzst.

> Android onboarding now finishes after permission-triggered node approval instead of trapping users in a loop between the Permissions and approval screens. #100959

> Android Gateway discovery, QR and manual setup, connection checks, approvals, and permission guidance now use the selected language across the translations in this release. Sources: 28062c8 , 3d43858 , ad74b32 , 1b07620 , 4fa4c9e , 1dd5230 , 9db7ec5 , e6f8788 , e5cf67e , b52d988 , cd3b4ee , c3bcb9f , 8af3aa0 , c34e79e , c9c8f6c , 255e251 , 0e98ba4 , 0cc9927 , 97955d9 , ba449f2 , 0e22e54 , ae65251 , d957f5a .

> Broader native app setup, chat, Talk, permission, connection, session, provider, and status text now uses the selected language across the language packs updated in this release. Sources: a39b07b , f8e1e0c , db27d2e , 28a8414 , e8e96bf , 6ea407d , 0011a18 , 8c5adbf , 019603d , d3d7282 , 267898c , 55ed57a , c54dc67 , fd0355d , 49726a5 , 2ffeedf , #98043 , beca2b1 , 4078dc7 , e7e98f6 , 3020f78 , 0c82908 , 8a3935f , 3f289fd , 203a896 , 6afef15 . Thanks @yeager.

> Native photo-permission controls now explain limited, selected, and recent-photo access in the selected language across the translations in this release. Sources: c360f92 , 4dd027e , 9cde1ca , 328fb70 , 71e5fcc , b11d710 , 55a2a9b , c4b40d0 , 3a1b983 , dea40a5 , 4b1fab8 , 44ca739 , d36452c , a50a59e , 49b68e1 , 122e4ba , 4086d35 , 547a563 , 538f28a , c5afa92 , 32a986d .

> iOS location settings now explain Off, While Using, Always, Precise Location, restrictions, and permission mismatches in the selected language across the translations in this release. Sources: 3542585 , 261d79a , ef1474d , cc1d61b , 2a1e118 , 748bfee , e0b2dda , f371a2f , ee00cc7 , 27f9ae0 , 51a07ae , ba9d167 , 576169e , 10500a6 , a344252 , d7d280f , cb2547f , 2191c2e , c63e9f9 , 4b1e0de , 525c4c7 .

> Native skill availability, Gateway setup, diagnostics, privacy, and access guidance now use the selected language across the translations in this release. Sources: fdcd5c0 , 26f6735 , 5220eff , bb7dbda , 952245b , edb1e74 , f7bad57 , 0602930 , e779b8f , 0400be7 , 851d0ad , 1e0dd95 , 703e1ad , 1c93e50 , 37c45f2 , 8fe917b , da21e4b , f4f63b1 , 3e4febb , a82cd35 , 52323b6 .

> The iOS app now applies OpenClaw's palette consistently across Talk, settings, Gateway, privacy, usage, and workboard views while retaining accessible contrast. #98930 Thanks @joelnishanth.

> iOS location settings now show the permission that is actually in effect, including Precise Location and mismatches between OpenClaw's selected mode and the iOS grant. #99247 Thanks @pollybot13.

> iOS Calendar, Reminders, and Contacts commands now return an immediate permission-required result instead of opening a prompt that leaves the agent request waiting. #99477 Thanks @nianjiuzst.

> The iOS app now recovers when a location permission prompt returns without a clear decision instead of waiting indefinitely. 75c8753 Thanks @vincentkoc.

> The iOS camera permission prompt now clearly connects access to Gateway setup and assistant-requested photo, video, document, screen, or workspace capture. e77994e Thanks @joshavant.

> The macOS menu-bar app now uses fewer idle CPU wakeups and less repeated configuration and permission work, reducing background battery use without changing active status behavior. #100463

> LaunchAgent-managed Gateways on permission-constrained macOS volumes now start the generated environment wrapper through /bin/sh , preventing immediate background-service exits. #89967 Related #87199 . Thanks @joshdaynard, @zhangguiping-xydt.

> doctor --lint --all can now explain the path or permission that would block a configuration repair before operators run doctor --fix . #100093 Thanks @giodl73-repo.

> Logbook users now have end-to-end guidance for setup, model routing, privacy choices, and troubleshooting missing capture or timeline results. b6a7898

> ACP troubleshooting now names PermissionPromptUnavailableError , helping operators recognize a non-interactive permission failure and find the right configuration fix. b3a74cc

> A broad reliability pass now replaces stalled child-process work with clear errors, improves sandbox diagnostics, bounds mobile calendar and voice state, normalizes cron fallbacks, and rejects unsafe provider responses. #100483 Thanks @aniruddhaadak80, @cxbasdev, @jincheng-xydt, @morluto, @nianjiuzst, @pandah97, @versatagent, @xialonglee, @zenglingbiao, @zengwen-dt.

> SSH- and OpenShell-backed sandbox commands now clean up remote resources after failed launches, preserve the correct plugin session and channel context, and return a normal tool error for malformed input instead of an internal WeakMap failure. #96926 Thanks @jesse-merhi.

> Docker sandbox commands now return an explicit failure when output cannot be read instead of crashing OpenClaw or reporting an incomplete result as successful. #100523 Thanks @cxbasdev.

> OpenShell sandbox sessions now start with the intended workspace files in the managed remote directory, avoiding missing-file and wrong-directory failures. d9034da Thanks @vincentkoc.

> The optional common sandbox image now includes Node 24 and pnpm so documented Node-based development tasks can run inside it. eabc12b Thanks @vincentkoc.

> OpenShell sandbox uploads now place workspace directories at the requested remote path so sandbox commands can reliably find their files. #96303 Thanks @vincentkoc.

> Added clearer policy coverage reporting so maintainers can spot gaps as security-sensitive configuration evolves. #87081 Thanks @giodl73-repo.

> Expanded browser safety coverage on Windows systems that support directory links, improving test portability. #90365 Thanks @aniruddhaadak80.

> Expanded automated security review for code that launches local processes, helping catch high-severity risks before merge. #92667 Thanks @hxy91819.

> Made QQBot and Zalo security tests depend on actual symlink support instead of the operating system name. #95531 Thanks @aniruddhaadak80, @vincentkoc.

> Documented how contributors should route issues, support requests, security reports, and pull requests. #96714 Thanks @100yenadmin.

> Restored green lint validation while preserving earlier Tailscale and Feishu safety fixes. #98598 Related #98462 , #98464 . Thanks @zhanglei99586.

> Prevented test-only proxy assertions from causing false network-safety validation failures. #99233 Thanks @joshavant.

> Removed an unused Slack download path, reducing security-sensitive maintenance while preserving private-file and image downloads. #99944 Thanks @miorbnli.

> Sped up package-candidate safety validation without changing the protections it provides. #100008

> Improved the safety and consistency of maintainer validation for heavy workloads and untrusted contributions. #100220

> Improved the reliability and security of documentation translation checks. #103244

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
- [[Changes/OpenClaw/2026-07-13-69-account-and-access-changes-in-v2026-7-1|69 Account and Access changes in v2026.7.1]] · Account and Access
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
## Nearby in Safety and Privacy

- Earlier: 2026-07-13 · Lovable · [[Changes/Lovable/2026-07-13-redesigned-settings|Redesigned settings]]
- Later: 2026-07-14 · Claude Code · [[Changes/Claude Code/2026-07-14-3-safety-and-privacy-changes-in-v2-1-210|3 Safety and Privacy changes in v2.1.210]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2020-07-28 · Descript · [[Changes/Descript/2020-07-28-in-the-case-of-your-account-security-being-compromised-revoke-access-to-your-acc|Revoke Application Access]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20openclaw-2026-07-13-9f5a75&body=Card%3A%20Changes%2FOpenClaw%2F2026-07-13-59-safety-and-privacy-changes-in-v2026-7-1.md%0ACard%20ID%3A%20openclaw-2026-07-13-9f5a75%0ASource%3A%20https%3A%2F%2Fdocs.openclaw.ai%2Freleases%2F2026.7.1%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->