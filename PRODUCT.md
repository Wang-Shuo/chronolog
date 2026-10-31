# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

**Primary: industry analysts and investors.** They come to ChronoLog to spot inflection points in AI products: when a capability first appeared in an official changelog, which tracked products followed and how long it took, and where a product's strategic emphasis shifted. They read across products and across months, compare themes, and need every statement to trace back to a dated official source they can cite.

Secondary audiences named in the PRD (product managers doing competitive research, developers and tech leads tracking their toolchain, content creators looking for structured material) are served by the same archive but do not decide trade-offs when they conflict with the primary reader.

As of 2026-10-31 there are no measured readers: analytics were only just wired (GoatCounter, opt-in at build time), the repository has no issues, and no reader testing has been done. Reader needs above are the confirmed target, not observed behavior.

## Product Purpose

ChronoLog turns official product release histories into a theme-organized archive: Release pages, normalized Change Cards (one announced change each, dated, with one theme, a kind and the quoted source line), product timelines with cadence and Eras, and cross-product Theme pages with curated research summaries.

Success means a reader can find a trend or turning point within a few minutes (the PRD Phase 3 test: "find a trend in 3 minutes") and leave with a dated, sourced claim they trust.

## Positioning

The primary axis is **theme, not time**. Instead of "what did Cursor ship in March?", ChronoLog answers "how did the agent-mode theme evolve across the tracked products, and in what order?". Its claims are deliberately bounded to what official changelogs announce, with source links, coverage gaps and scope stated, so the archive is citable rather than speculative.

## Operating Context

- Data comes only from official changelogs: ChatGPT release notes (Help Center, sometimes via an imported browser snapshot when the site returns a 403), Claude Code GitHub Releases (from v2.0.73, 2025-12-19), and the Cursor changelog.
- A deterministic Python pipeline (no external LLM API at run time) collects, extracts cards, classifies themes against a fixed vocabulary (`_scripts/themes.yaml`), validates a staged vault and publishes through a recoverable transaction. A scheduled GitHub workflow generates daily; every content batch is reviewed in a pull request before deployment to GitHub Pages.
- Curators write theme summaries, product positioning, Eras and key moments in `_scripts/editorial.yaml`, following `docs/style-guide.md`. Human regions in the Markdown are never overwritten by the pipeline.
- The vault opens directly in Obsidian; Obsidian is the editor's back office and Quartz is the public site.

## Capabilities and Constraints

- Page types: Home, About the data, Product, Theme (25 themes), Release, Change Card (including digest and "Other changes" cards), monthly Archive, RSS feed.
- Card kinds: launch, expansion, pricing, policy, fix, digest, change. Dates are announcement dates, not availability dates. Cadence is measured to the newest archived release, and products can be marked quiet or silent.
- Every card ends with a link that opens a prefilled GitHub issue for reporting problems.
- Static site only: no backend, user accounts, personalization, comments or paywall.
- The public site is currently written in English, in the third person. This is the current state, not a binding commitment.
- Known quality gaps (2026-10-31 review): theme classification is about 64–74% accurate in sampling (target ≥ 90%), about 25% of titles are truncated, and Claude Code's verbose release notes dominate counts. Design must not present the data as more precise or more complete than it is.
- **Open decision: product scope.** The current portfolio is ChatGPT, Claude Code and Cursor. Options under consideration are refocusing on AI coding agents (adding Codex CLI, Gemini CLI, GitHub Copilot) or running separate assistant and coding lanes. Aider, Continue, OpenHands and Tabby have product pages but their sources are disabled. Do not design around a fixed set of three products.
- Planned but not yet built (PRD): a weekly signal layer, a capability matrix, revision ("silent edit") detection, and CSV/JSON exports.

## Brand Commitments

- Name: **ChronoLog**. Product names are written exactly as **ChatGPT**, **Claude Code**, **Cursor**; feature and model names are kept as the source writes them.
- **Epistemic restraint (binding):** every factual statement cites an official source. Announcement is never presented as availability. No claims that one product followed, influenced or outperformed another; no cross-product causation, adoption or quality comparisons. Uncertainty is stated once, in a scope sentence, not scattered as hedging.
- **Short quotes plus a link (binding):** quote the source briefly and link to it rather than republishing whole changelogs.
- **Static, no accounts (binding):** a Markdown/Obsidian vault is the single source of truth, published as a static Quartz site.
- Editorial voice (`docs/style-guide.md`): research notes with citations, not marketing copy. Dates are always `YYYY-MM-DD`.

## Evidence on Hand

- Live site: https://wang-shuo.github.io/chronolog/
- Archive as of 2026-10-31: 3 active products, 818 archived releases, 2,742 tracked changes, 25 themes, 62 pending theme reviews (`About.md`, `index.md`).
- Curated research summaries exist for 7 themes; Eras exist for the products in `_scripts/editorial.yaml`.
- Brand icon and share image: `_scripts/brand/`.
- Product and design history: `docs/chronolog-prd.md`, `docs/design-review-2026-10-15.md`, `docs/review-2026-10-31.md`.
- Absent and not to be fabricated: reader testimonials, usage numbers, press, partnerships, accuracy figures beyond the sampled review, or any claim of complete lifetime coverage.

## Product Principles

1. **Theme before time.** The way into the archive is a question about how something evolved, not a feed of everything that shipped.
2. **Every claim is citable.** A reader can reach the dated official source from any fact in one step, and the site never says more than the source does.
3. **Signal over volume.** Launches, pricing, policy, new models and deprecations come first; routine fix lines must not drown them, and verbose changelogs must not outweigh terse ones just because they write more.
4. **Honest coverage.** Gaps, sampling rules, classification limits and scope are visible to the reader, but stated once and plainly rather than as defensive hedging.
5. **Reader-facing, not pipeline-facing.** Operational detail (fetch timestamps, hashes, review queues, maintenance notes) stays out of the reader's path and lives on About or in the repository.
