---
card_id: windsurf-2026-08-21-bbd69b
date: '2026-08-21'
description: 'Windsurf · 2026-08-21 · Mobile and Desktop: The Agent Command Center
  now follows whichever space is selected instead of being tied to one folder, converts
  an…'
diffusion:
  first_in_tracked: "[[Changes/Cursor/2023-03-14-windows-and-linux-support|Windows
    and Linux support \U0001F973]]"
  inference: No adoption, equivalence, or causation claim.
  lag_days: 1256
  relation: same-theme-chronology
  role: later-observed
  scope: tracked-products-only
  theme: mobile-desktop
  tracked_products_count: 20
evolves_from: []
extractor_version: fallback-v5
impact: paradigm-shift
kind: launch
machine_hash: 850f86421510945b00d6c525d2a38b376a04f92bdc759dd9dee823be10ec0c33
product: windsurf
product_name: Windsurf
record:
  ai_generated: true
  card_id: windsurf-2026-08-21-bbd69b
  comparison: ''
  confidence: low
  date: '2026-08-21'
  description: 'Windsurf — v3.8.20: The Agent Command Center now follows whichever
    space is selected instead of being tied to one folder, converts an editor window
    in place (no reload, no save prompt), and any number of agent windows can run
    side by side.'
  evidence:
  - quote: The Agent Command Center now follows whichever space is selected instead
      of being tied to one folder, converts an editor window in place (no reload,
      no save prompt), and any number of agent windows can run side by side.
    source_release: https://docs.devin.ai/desktop/changelog#v3-8-20
  - quote: A new **Agent Command Center location** setting (`devin.agentWindow.location`)
      can be used to split the agent command center into a separate window from the
      editor.
    source_release: https://docs.devin.ai/desktop/changelog#v3-8-20
  - quote: Significantly improved performance for switching between Agent and Editor
      mode (Ctrl/Cmd+G).
    source_release: https://docs.devin.ai/desktop/changelog#v3-8-20
  - quote: Improved update process on Windows to only install after explicitly clicking
      **Restart to Update**.
    source_release: https://docs.devin.ai/desktop/changelog#v3-8-20
  - quote: 'Windows: **Install Devin CLI** now writes a shim to the bundled CLI, so
      updating Devin Desktop updates the `devin` command too.'
    source_release: https://docs.devin.ai/desktop/changelog#v3-8-20
  - quote: 'Linux: uninstalling or upgrading the `.deb` no longer removes the shared
      Microsoft apt keyring, so other repositories signed by it keep working.'
    source_release: https://docs.devin.ai/desktop/changelog#v3-8-20
  - quote: The agent sidebar, composer, and welcome page now warn when a workspace
      is untrusted and offer a **trust workspace** prompt to activate local agents.
    source_release: https://docs.devin.ai/desktop/changelog#v3-8-20
  - quote: Improved recovery for corrupted `file://` working directories.
    source_release: https://docs.devin.ai/desktop/changelog#v3-8-20
  - quote: Added the ability to rename sessions from the tab dropdown.
    source_release: https://docs.devin.ai/desktop/changelog#v3-8-20
  - quote: 'Enterprise: Added a link to request more usage when hitting ACU limits.'
    source_release: https://docs.devin.ai/desktop/changelog#v3-8-20
  extractor_version: fallback-v5
  impact: paradigm-shift
  kind: launch
  product: windsurf
  product_name: Windsurf
  slug: devin-desktop
  source_release: windsurf-2026-08-21-v3-8-20-0d306190
  source_type: windsurf_changelog
  theme: mobile-desktop
  title: Devin Desktop
  type: change
related_changes:
- '[[Changes/Claude Code/2026-08-21-remote-sessions-images-uploaded-from-mobile-now-include-their-saved-file-path-so|Remote
  sessions: images uploaded from mobile now include their saved file path…]]'
- '[[Changes/Claude Code/2026-08-21-windows-cross-session-messaging-is-now-available-so-claude-code-sessions-across|Windows:
  cross-session messaging is now available, so Claude Code sessions across…]]'
- '[[Changes/Ollama/2026-08-21-developers-can-now-easily-configure-claude-desktop-to-seamlessly-work-with-ollam|Developers
  can now easily configure Claude Desktop to seamlessly work with Ollama…]]'
source_release: '[[Releases/Windsurf/windsurf-2026-08-21-v3-8-20-0d306190|windsurf-2026-08-21-v3-8-20-0d306190]]'
source_type: windsurf_changelog
theme: mobile-desktop
title: Devin Desktop
type: change
---

<!-- chronolog:begin region="header" -->
# Devin Desktop

**Windsurf** · 2026-08-21 · [[Themes/mobile-desktop|Mobile and Desktop]] · Launch · [Official source](https://docs.devin.ai/desktop/changelog#v3-8-20) · from [[Releases/Windsurf/windsurf-2026-08-21-v3-8-20-0d306190|v3.8.20]]
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> The Agent Command Center now follows whichever space is selected instead of being tied to one folder, converts an editor window in place (no reload, no save prompt), and any number of agent windows can run side by side.
>
> A new **Agent Command Center location** setting (`devin.agentWindow.location`) can be used to split the agent command center into a separate window from the editor.
>
> Significantly improved performance for switching between Agent and Editor mode (Ctrl/Cmd+G).
>
> Improved update process on Windows to only install after explicitly clicking **Restart to Update**.
>
> Windows: **Install Devin CLI** now writes a shim to the bundled CLI, so updating Devin Desktop updates the `devin` command too.
>
> Linux: uninstalling or upgrading the `.deb` no longer removes the shared Microsoft apt keyring, so other repositories signed by it keep working.
>
> The agent sidebar, composer, and welcome page now warn when a workspace is untrusted and offer a **trust workspace** prompt to activate local agents.
>
> Improved recovery for corrupted `file://` working directories.
>
> Added the ability to rename sessions from the tab dropdown.
>
> Enterprise: Added a link to request more usage when hitting ACU limits.
>
> Source: https://docs.devin.ai/desktop/changelog#v3-8-20
<!-- chronolog:end -->

<!-- chronolog:begin region="context" -->
## Also in this release

- [[Changes/Windsurf/2026-08-21-devin-cloud|Devin Cloud]] · Interface Experience
<!-- chronolog:end -->

<!-- chronolog:begin region="nearby" -->
## Nearby in Mobile and Desktop

- Earlier: 2026-08-21 · Ollama · [[Changes/Ollama/2026-08-21-developers-can-now-easily-configure-claude-desktop-to-seamlessly-work-with-ollam|Developers can now easily configure Claude Desktop to seamlessly work with Ollama…]]
- Later: 2026-08-25 · Claude Code · [[Changes/Claude Code/2026-08-25-windows-macos-fixed-headless-sessions-not-cleaning-up-stale-entries-in-claude-se|Windows/macOS: Fixed headless sessions not cleaning up stale entries…]]
<!-- chronolog:end -->

<!-- chronolog:begin region="relations" -->
## Related

- Earliest same-theme entry in the tracked set: 2023-03-14 · Cursor · [[Changes/Cursor/2023-03-14-windows-and-linux-support|Windows and Linux support 🥳]]
<!-- chronolog:end -->

<!-- chronolog:begin region="footer" -->
[Report an issue with this card](https://github.com/Wang-Shuo/chronolog/issues/new?title=Card%20feedback%3A%20windsurf-2026-08-21-bbd69b&body=Card%3A%20Changes%2FWindsurf%2F2026-08-21-devin-desktop.md%0ACard%20ID%3A%20windsurf-2026-08-21-bbd69b%0ASource%3A%20https%3A%2F%2Fdocs.devin.ai%2Fdesktop%2Fchangelog%23v3-8-20%0A%0AWhat%20should%20be%20corrected%3F%0A)
<!-- chronolog:end -->