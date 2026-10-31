---
name: ChronoLog
description: A reading-room archive of official AI product changelogs, organized by theme.
colors:
  archive-ochre: "#8a5c12"
  archive-ochre-lamp: "#d49a36"
  patina-teal: "#3f6f6b"
  patina-teal-lamp: "#74aaa4"
  reading-room-paper: "#f8f7f2"
  paper-rule: "#dedbd2"
  graphite: "#6c6a63"
  carbon-ink: "#34332f"
  heading-ink: "#171714"
  night-graphite: "#9d9a90"
  ochre-wash: "rgba(155, 106, 25, 0.15)"
  ochre-wash-lamp: "rgba(212, 154, 54, 0.2)"
  marginal-note: "#fff0bd"
  marginal-note-lamp: "#5a4314"
  product-chatgpt: "#0f766e"
  product-claude-code: "#b45309"
  product-cursor: "#4b5563"
typography:
  display:
    fontFamily: "Inter, system-ui, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: "2rem"
    fontWeight: 700
    lineHeight: "normal"
  headline:
    fontFamily: "Inter, system-ui, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: "1.4rem"
    fontWeight: 700
    lineHeight: "normal"
  title:
    fontFamily: "Inter, system-ui, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: "1.12rem"
    fontWeight: 700
    lineHeight: "normal"
  body:
    fontFamily: "Inter, system-ui, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.6
  label:
    fontFamily: "Inter, system-ui, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: "0.85rem"
    fontWeight: 400
    lineHeight: 1.35
  wordmark:
    fontFamily: "Inter, system-ui, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: "1.75rem"
    fontWeight: 700
  mono:
    fontFamily: "'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, monospace"
    fontSize: "0.9em"
    fontWeight: 400
rounded:
  hairline: "3px"
  field: "4px"
  pill: "5px"
spacing:
  pill-x: "0.1rem"
  cell-y: "0.2rem"
  cell-x: "0.7rem"
  gutter: "1rem"
  column-pad: "2rem"
  top: "6rem"
  side-panel: "320px"
components:
  link-internal:
    backgroundColor: "{colors.ochre-wash}"
    textColor: "{colors.archive-ochre}"
    rounded: "{rounded.pill}"
    padding: "0 0.1rem"
  link-internal-hover:
    backgroundColor: "{colors.ochre-wash}"
    textColor: "{colors.patina-teal}"
  link-external:
    textColor: "{colors.archive-ochre}"
  link-external-hover:
    textColor: "{colors.patina-teal}"
  tag-pill:
    backgroundColor: "{colors.ochre-wash}"
    textColor: "{colors.archive-ochre}"
    rounded: "{rounded.pill}"
    padding: "0 0.1rem"
  search-field:
    backgroundColor: "{colors.reading-room-paper}"
    textColor: "{colors.carbon-ink}"
    rounded: "{rounded.field}"
    height: "2rem"
  evidence-quote:
    textColor: "{colors.carbon-ink}"
    padding: "0 0 0 1rem"
  table-header:
    textColor: "{colors.carbon-ink}"
    typography: "{typography.body}"
    padding: "0.4rem 0.7rem"
  table-cell:
    textColor: "{colors.carbon-ink}"
    padding: "0.2rem 0.7rem"
  wordmark:
    textColor: "{colors.archive-ochre}"
    typography: "{typography.wordmark}"
  tagline:
    textColor: "{colors.graphite}"
    typography: "{typography.label}"
---

# Design System: ChronoLog

## Overview

**Creative North Star: "The Reading-Room Archive"**

ChronoLog looks like a working archive in a quiet reading room: warm paper, near-black ink, and a single ochre tone that marks every citable thing. Nothing on the page competes with the record. The reader walks the stacks (Products, Themes, Archive in the left rail), pulls a file (a theme, a product, a card), and finds every claim stamped with a date and a path back to its official source. The calm is deliberate: the reader is weighing evidence, and the interface should feel like a catalogue, not a feed.

The system is Quartz's three-column reading layout, re-inked. Structure comes from typography and hairline rules, not from boxes or shadows. Density is that of a research document: plain lists of dated entries joined by middle dots, compact tables, and long cited paragraphs at a comfortable 1.6 line height. Color is scarce and functional. Ochre means "this goes somewhere", teal means "you are pointing at it", and everything else is ink on paper. Dark mode is the same room after hours: carbon paper, lamp-lit ochre, nothing new added.

Data visualization stays typographic. Cadence is drawn with block characters (█) in running text, timelines are tables of quarters × products, and an empty cell says why it is empty: a quiet middle dot, or `not archived`. This keeps the archive readable in Obsidian, in RSS and on the web alike.

**Key Characteristics:**
- Warm off-white paper and warm near-black ink; one ochre accent, one teal hover.
- Flat surfaces; hierarchy from type size, weight and hairline rules only.
- Every citable reference is ochre: internal links sit on a soft ochre wash, external links are bare ochre text with an outbound glyph.
- ISO dates (`YYYY-MM-DD`) and middle-dot (·) separators are a visual signature as much as a writing rule.
- Charts are made of type: block-character bars, quarter-by-product tables.

## Colors

A paper-and-ink palette with one warm metallic accent and one oxidized cool counterpart; every hue is pulled slightly toward yellow so the page never reads as clinical white.

### Primary
- **Archive Ochre** (light): links, the wordmark, tag pills, breadcrumbs, the evidence-quote rule. It is the color of "citable, follow this". Measures 5.4:1 on Reading-Room Paper.
- **Archive Ochre, Lamp-Lit** (dark): the same role in dark mode, brighter so it holds 7.2:1 on carbon paper.
- **Ochre Wash** / **Ochre Wash, Lamp-Lit**: the translucent background behind internal links and tag pills. It turns each internal link into a small catalogue tab.

### Secondary
- **Patina Teal** (light) / **Patina Teal, Lamp-Lit** (dark): hover state for every link, the keyboard focus ring and the selection tint. It appears only in response to the reader, never at rest.

### Neutral
- **Reading-Room Paper**: page background in light mode; text color of headings in dark mode.
- **Paper Rule**: table row rules, search-field border and the faint dividers between page regions; body text in dark mode.
- **Graphite**: secondary text (site tagline, table header rule, metadata). Measures 5.0:1 on paper.
- **Night Graphite**: the dark-mode counterpart of Graphite.
- **Carbon Ink**: body text in light mode; rules in dark mode.
- **Heading Ink**: headings in light mode; page background ("carbon paper") in dark mode.
- **Marginal Note** / **Marginal Note, Lamp-Lit**: `==highlighted==` text, like a pencil underline.

### Reserved (defined, not yet in use)
- **ChatGPT Teal**, **Claude Code Amber**, **Cursor Slate** (`--product-*` custom properties in `_scripts/site_title.tsx`, with brighter dark-mode values): reserved for distinguishing products in comparisons. No surface uses them yet; the first one to do so sets their usage rules here.

### Named Rules
**The Ochre-Means-Citable Rule.** Archive Ochre is spent only on things a reader can follow: links, tags, breadcrumbs, the source rule of an evidence quote, the wordmark. Never use it for decoration, emphasis or status.

**The Teal-Under-the-Pointer Rule.** Patina Teal appears only as a response to the reader (hover, keyboard focus, selection). A surface that shows teal at rest is wrong.

**The One-Room Rule.** Every color in use comes from this palette. Stock Quartz colors do not ship: the cyan `info` callout that once framed the theme timeline year groups was replaced with palette disclosures (2026-10-31), and any new Quartz component is re-inked before it appears.

## Typography

**Display Font:** Inter (with system-ui, Segoe UI, Roboto, Helvetica fallbacks)
**Body Font:** Inter
**Label/Mono Font:** JetBrains Mono, for code identifiers, flags and environment variables quoted from changelogs

**Character:** One neutral grotesque throughout, so the record carries the voice rather than the type. Weight does the work: 700 for headings, 600 for links, 400 for everything else. The mono face appears only where the source itself is code.

### Hierarchy
- **Display** (700, 2rem): the page's own H1, such as a theme name, a product name or a card title.
- **Headline** (700, 1.4rem): page sections such as "Latest changes", "Research summary", "Key moments", "Timeline".
- **Title** (700, 1.12rem): sub-groups within a section, such as a product name under "Latest changes".
- **Body** (400, 1rem, line height 1.6): cited paragraphs, dated lists, table cells. The center column caps measure at roughly 750–800px (about 80–90 characters).
- **Label** (400, 0.85rem, line height 1.35, Graphite): the site tagline and other quiet metadata.
- **Wordmark** (700, 1.75rem, Archive Ochre): "ChronoLog" at the top of the left rail; it is the home link.
- **Mono** (400, 0.9em): inline code from source text.

### Named Rules
**The Weight-Not-Color Rule.** Hierarchy is set by size and weight in ink colors. Headings never take the accent; the accent is reserved for links.

**The ISO-Date Rule.** Dates in content render as `YYYY-MM-DD` in the body face, set in running text at body size, never as badges.

## Layout

Quartz's three-column reading grid on a single paper surface.

- **Desktop (≥ 1200px):** left rail (320px: wordmark, tagline, search, theme toggle, Explorer), center reading column, right rail (320px: Graph on card pages only, Table of Contents, Backlinks). The whole grid is capped at 1500px and centered. The rails are sticky, full-height columns with 6rem top padding, 2rem side padding and 1.2rem between their components; the center column scrolls between them.
- **Tablet (800–1200px):** the left rail stays; the right rail drops below the content. The page gets 1rem side padding.
- **Mobile (< 800px):** a single column with 1rem side padding. Wordmark, search and theme toggle share one header row, Explorer and Table of Contents are hidden, and Backlinks follow the content. No page may scroll horizontally at 390px; long identifiers in content and sidebars break anywhere (`overflow-wrap: anywhere`).
- **Rhythm:** heading top margins step down by level (2.25rem, 1.9rem, 1.62rem, 1.5rem) with 1rem below each. Lists of dated entries are plain bullets at body line height.
- **Navigation order** in the Explorer is fixed: Products → Themes → Archive, months newest first. Changes, Releases, Alerts and tags are never listed in the rail.

## Elevation & Depth

Flat, by design. No surface carries a shadow. Depth comes from tone and line: Paper Rule hairlines between table rows, a 2px Graphite rule under table headers, the Ochre Wash behind internal links, and the 3px Archive Ochre rule on the left of an evidence quote. The only floating layers are Quartz's link-preview popovers and the search overlay, which inherit Quartz's defaults.

### Named Rules
**The Flat-Paper Rule.** Surfaces do not lift. If something needs separating, use a hairline rule or a change of tone, never a shadow or a card container.

## Shapes

Barely softened corners on small inline objects, square everything else. Internal-link pills, tag pills, code spans and callouts use a 5px radius, the search field 4px and small form controls 3px. Blocks of content such as sections, tables and lists have no container and no radius; they sit directly on the paper. The only recurring line shapes are the vertical ochre rule of the evidence quote and the horizontal rules of tables.

## Components

### Links
Quiet, catalogue-tab feel.
- **Internal (vault) link:** Archive Ochre text, weight 600, on an Ochre Wash background, 5px radius, with 0.1rem horizontal padding. Reads as a filed reference.
- **External (official source) link:** Archive Ochre text, weight 600, no background, followed by a small outbound-arrow glyph.
- **Hover:** text shifts to Patina Teal over 0.2s ease; the wash stays.
- **Broken link:** Archive Ochre at 50% opacity, rising to 80% on hover.

### Tag pills
- **Style:** the internal-link pill with a leading `#` (`#theme`, `#product`). They currently appear above every page title. They are taxonomy labels rather than reader navigation, which the 2026-10-31 review flagged.

### Evidence quote
The card's core: the official source text, quoted.
- **Style:** a blockquote with a 3px Archive Ochre left rule, 1rem left padding and no background, in Carbon Ink body text. It ends with a "Source:" line linking to the official URL.

### Tables (Key moments)
- **Style:** a borderless table on paper, aligned with the text column (no inset). The header row is in body weight 700 with a 2px Graphite rule beneath; body rows are separated by Paper Rule hairlines. Cells are top-aligned with 0.45rem × 0.7rem padding and a 1.5 line height, and the first column never wraps on wide screens.
- **Key moments** is the signature use. Each cell stacks a `<time>` date and an internal link per entry, and dates never break at their hyphens. The rows are:
  - a bold **First in archive** row leading the table, with each product's earliest tracked card in the theme;
  - one row per quarter (newest first);
  - a range row (`2023 Q4 → 2024 Q4`) for quarters skipped between two rows.
- **Coverage states:** an empty cell says why it is empty. A middle dot (·) means no key moment inside the product's archive. `not archived` (Graphite) means the quarter is wholly before the product's archive begins. `archive begins YYYY-MM-DD` marks the quarter or range where it does. A one-line legend under the table lists each product's archive start. An empty cell must never read as "this product was later".
- **Phones (< 800px):** the table takes its natural width and scrolls inside its container. Product columns are about 9rem wide, and the quarter column (4.5rem, allowed to wrap) stays pinned on paper with a hairline edge painted by the cell itself.

### Cadence bars
- **Style:** inline block-character bars (█) in Carbon Ink, each followed by its number, in a plain list labelled by `YYYY-MM` (product pages) or theme name and card count (theme rankings). Typographic and copy-pasteable. They render the same in Obsidian, RSS and the site.

### Disclosures
A ruled list of folds, not boxes. Used for theme timeline years, "How to read this timeline", and the product page's release archive and change list.
- **Markup:** native `<details class="disclosure">` emitted by `writer.py`, with Markdown inside, so the summary is keyboard-operable and folded links leave the tab order. Never use Quartz callouts for collapsible content.
- **Style:** no background or box. A Paper Rule hairline sits above each disclosure, and consecutive disclosures share their rules and close with one below the last. The summary line is Heading Ink at weight 600 with 0.65rem vertical padding, led by a small Archive Ochre chevron drawn in CSS (2px strokes). The chevron points right when closed and down when open, and turns Patina Teal on hover. It rotates over 0.2s only when the reader allows motion.
- **Default state:** a theme with ≤ 12 entries shows its years open; longer timelines and product archives start folded.

### Focus
- Every focusable element shows a 2px Patina Teal outline with a 2px offset when focused from the keyboard (`:focus-visible`): 5.3:1 on paper and 6.9:1 on carbon. The browser's default blue ring never ships.

### Navigation
- **Left rail:** the wordmark (Archive Ochre, 1.75rem, 700) over the tagline (Label, Graphite), then a search field (paper background, 1px Paper Rule border, 4px radius, magnifier icon and placeholder "Search"), the sun or moon theme toggle, and the Explorer tree (bold folder labels with a chevron).
- **Breadcrumbs:** Archive Ochre links separated by a dark chevron (❯), followed by the page date in body text.
- **Right rail:** "Table of Contents" (weight 700, collapsible) with entries in Graphite at reduced opacity, and "Backlinks" as an internal-link list.
- **Mobile:** the rails collapse, and search and the theme toggle move into the header row beside the wordmark.

### Site title (signature)
The wordmark plus the one-line tagline "Tracked changes in ChatGPT, Claude Code and Cursor" (Label, Graphite). It appears on every page and is also where the site-wide CSS lives (`_scripts/site_title.tsx`), because the Quartz runtime is re-copied on every install.

## Do's and Don'ts

### Do:
- **Do** keep Archive Ochre for followable things only (links, tags, breadcrumbs, source rules, wordmark); see The Ochre-Means-Citable Rule.
- **Do** separate content with Paper Rule hairlines and tone, keeping every surface flat.
- **Do** draw data with type: block-character bars, quarter × product tables, and middle-dot placeholders for quarters without a moment, kept distinct from `not archived`.
- **Do** set dates as `YYYY-MM-DD` and join metadata with middle dots (`2026-10-30 · Memory and Personalization: …`).
- **Do** verify that every new color pairing meets WCAG AA in both modes; the incumbent text colors measure 5.0–11.8:1 in light mode and 6.4–13:1 in dark mode.
- **Do** keep every page free of horizontal scroll at 390px, breaking long identifiers anywhere.
- **Do** put site-wide CSS in a component under `_scripts/` (currently `site_title.tsx`), never in `quartz/`, which is overwritten on install.

### Don't:
- **Don't** introduce colors from outside the palette, including stock Quartz component colors such as the cyan callout.
- **Don't** use shadows, raised cards or boxed containers for content blocks.
- **Don't** color headings with the accent or use color alone to rank importance.
- **Don't** show Patina Teal at rest; it belongs to hover and selection.
- **Don't** use the reserved product colors decoratively; their first real use defines their rules.
- **Don't** add a second typeface for display; Inter carries every role except quoted code.
