---
card_id: chatgpt-2026-04-30-139382
date: '2026-04-30'
diffusion:
  first_in_tracked: '[[Changes/Cursor/2023-03-30-ai-now-requires-login|cursor-2023-03-30-3bf00d]]'
  lag_days: 1127
  role: follower
  scope: tracked-products-only
  theme: account-access
  tracked_products_count: 3
evolves_from:
- '[[Changes/ChatGPT/2026-04-22-we-re-launching-chatgpt-for-clinicians-a-free-version-of-chatgpt-for-verified-cl|chatgpt-2026-04-22-432031]]'
extractor_version: fallback-v2
impact: incremental
machine_hash: eae5660b0855f83a80fb1b941344d33d0db88d9157744419b6d05462b0a1fc94
product: chatgpt
product_name: ChatGPT
related_changes:
- '[[Changes/Claude Code/2026-04-09-added-interactive-google-vertex-ai-setup-wizard-accessible-from-the-login-screen|claude-code-2026-04-09-ac42a3]]'
- '[[Changes/ChatGPT/2026-04-22-we-re-launching-chatgpt-for-clinicians-a-free-version-of-chatgpt-for-verified-cl|chatgpt-2026-04-22-432031]]'
- '[[Changes/Claude Code/2026-04-28-clarified-the-mcp-message-shown-when-an-mcp-server-is-still-unauthorized-after-t|claude-code-2026-04-28-77f3f4]]'
source_release: '[[Releases/ChatGPT/chatgpt-2026-04-30-advanced-account-security-in-chatgpt-d81bf569|chatgpt-2026-04-30-advanced-account-security-in-chatgpt-d81bf569]]'
theme: account-access
type: change
---

# We’re rolling out Advanced Account Security, an optional setting for personal Ch

<!-- chronolog:begin region="description" -->
We’re rolling out Advanced Account Security, an optional setting for personal ChatGPT accounts that adds stronger sign-in requirements and stricter account safeguards to help reduce the risk of ATO (account take over), unauthorized access, and data exposure. With Advanced Account Security enabled, ChatGPT uses stronger sign-in methods like passkeys or compatible security keys and turns off weaker paths like password sign-in, email/SMS sign-in codes, and email-based account recovery. It also adds recovery keys, shorter active sessions, login notifications, and session management controls, giving users more protection and visibility across their account. Because these protections are stricter, recovery is also stricter. Users should save their recovery keys and keep access to their enrolled passkeys or security keys. If access to all sign-in methods and recovery keys is lost, access to the account may be lost.
<!-- chronolog:end -->

<!-- chronolog:begin region="evidence" -->
> We’re rolling out Advanced Account Security, an optional setting for personal ChatGPT accounts that adds stronger sign-in requirements and stricter account safeguards to help reduce the risk of ATO (account take over), unauthorized access, and data exposure. With Advanced Account Security enabled, ChatGPT uses stronger sign-in methods like passkeys or compatible security keys and turns off weaker paths like password sign-in, email/SMS sign-in codes, and email-based account recovery. It also adds recovery keys, shorter active sessions, login notifications, and session management controls, giving users more protection and visibility across their account. Because these protections are stricter, recovery is also stricter. Users should save their recovery keys and keep access to their enrolled passkeys or security keys. If access to all sign-in methods and recovery keys is lost, access to the account may be lost.
>
> Source: https://help.openai.com/en/articles/6825453-chatgpt-release-notes#advanced-account-security-in-chatgpt
<!-- chronolog:end -->

<!-- chronolog:begin region="evolution" -->
- [[Changes/ChatGPT/2026-04-22-we-re-launching-chatgpt-for-clinicians-a-free-version-of-chatgpt-for-verified-cl|chatgpt-2026-04-22-432031]]
<!-- chronolog:end -->

<!-- chronolog:begin region="diffusion" -->
- Theme: account-access
- Scope: tracked-products-only
- Role: follower
- First In Tracked: [[Changes/Cursor/2023-03-30-ai-now-requires-login|cursor-2023-03-30-3bf00d]]
- Lag Days: 1127
- Tracked Products Count: 3
<!-- chronolog:end -->

## Editor Notes