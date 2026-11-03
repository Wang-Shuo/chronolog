import { pathToRoot } from "../quartz/util/path"
import { classNames } from "../quartz/util/lang"
import {
  QuartzComponent,
  QuartzComponentConstructor,
  QuartzComponentProps,
} from "../quartz/components/types"

export const TAGLINE = "Tracked changes in ChatGPT, Claude Code and Cursor"

// quartz/ is re-copied from node_modules on install, so site-wide rules live here: this
// component is on every page. Product colours are defined for later use by content.
const style = `
:root {
  --product-chatgpt: #0f766e;
  --product-claude-code: #b45309;
  --product-cursor: #4b5563;
}
:root[saved-theme="dark"] {
  --product-chatgpt: #2dd4bf;
  --product-claude-code: #f59e0b;
  --product-cursor: #9ca3af;
}
.global-graph-icon {
  display: none;
}
.site-title {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
  min-width: 0;
}
.page-title {
  font-size: 1.75rem;
  margin: 0;
  font-family: var(--titleFont);
}
.site-tagline {
  margin: 0;
  font-size: 0.85rem;
  line-height: 1.35;
  color: var(--gray);
}
/* Card titles quote env var names and flags (CLAUDE_CODE_ENABLE_AUTO_MODE); unbroken,
   they widened theme pages to 458px on a 390px phone via the Backlinks list. Quartz sets
   break-word on these elements directly, which does not shrink their minimum width. */
article :is(p, ul, ol, li, a, td, th),
.sidebar :is(p, ul, ol, li, a) {
  overflow-wrap: anywhere;
}
/* Keyboard focus in the palette: Patina Teal answers the reader, like hover does
   (DESIGN.md, Teal-Under-the-Pointer). 5.3:1 on paper, 6.9:1 on carbon. */
:focus-visible {
  outline: 2px solid var(--tertiary);
  outline-offset: 2px;
  border-radius: 2px;
}
/* Disclosures: timeline years, the product release archive and change list. writer.py
   emits native <details>, so they open from the keyboard and folded links leave the tab
   order. Consecutive disclosures read as one ruled list: Paper Rule hairlines, a Heading
   Ink summary line and an Archive Ochre chevron (DESIGN.md, One-Room Rule). */
article details.disclosure {
  margin: 1rem 0;
  border-top: 1px solid var(--lightgray);
}
article details.disclosure + details.disclosure {
  margin-top: -1rem;
}
article details.disclosure:not(:has(+ details.disclosure)) {
  border-bottom: 1px solid var(--lightgray);
}
article details.disclosure > summary {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.65rem 0;
  list-style: none;
  cursor: pointer;
  font-weight: 600;
  color: var(--dark);
}
article details.disclosure > summary::-webkit-details-marker {
  display: none;
}
article details.disclosure > summary::before {
  content: "";
  flex: none;
  width: 0.45rem;
  height: 0.45rem;
  margin-left: 0.15rem;
  border-right: 2px solid var(--secondary);
  border-bottom: 2px solid var(--secondary);
  transform: rotate(-45deg);
}
article details.disclosure[open] > summary::before {
  transform: translateY(-0.15rem) rotate(45deg);
}
article details.disclosure > summary:hover::before {
  border-color: var(--tertiary);
}
article details.disclosure > :last-child {
  margin-bottom: 1rem;
}
@media (prefers-reduced-motion: no-preference) {
  article details.disclosure > summary::before {
    transition: transform 0.2s ease, border-color 0.2s ease;
  }
}
/* Key moments and other tables: aligned with the text column rather than inset by
   Quartz's 1rem margin, entries top-aligned so a quarter reads across products, and a
   1.5 line height instead of 2rem so stacked entries stay compact. */
article .table-container > table {
  margin: 1rem 0;
}
article .table-container > table > * {
  line-height: 1.5;
}
article .table-container td {
  padding-top: 0.45rem;
  padding-bottom: 0.45rem;
  vertical-align: top;
}
article .table-container td:first-child {
  white-space: nowrap;
}
/* ISO dates never break at their hyphens ("2026-09-" / "29"). */
article time {
  white-space: nowrap;
}
/* A quarter before a product's archive begins: present, but quieter than evidence. */
article .not-archived {
  color: var(--gray);
}
/* Phones: a product column needs ~9rem to read; the table scrolls sideways inside its
   container while the quarter column stays pinned on paper, so a cell never loses its
   row. No shadow (Flat-Paper Rule): a hairline marks the pinned edge. */
@media all and (max-width: 800px) {
  /* Browsers ignore min-width on table cells: let the table take its natural width and
     give each column a preferred one instead. */
  article .table-container > table {
    width: max-content;
  }
  article .table-container :is(td, th) {
    width: 9rem;
  }
  article .table-container :is(td, th):first-child {
    position: sticky;
    left: 0;
    width: 4.5rem;
    max-width: 4.5rem;
    padding-left: 0;
    white-space: normal;
    /* A collapsed table's borders stay put while the cell sticks, so the hairline is
       painted by the cell itself. */
    background: linear-gradient(to left, var(--lightgray) 1px, var(--light) 1px);
  }
}
`

// Same title markup and classes as Quartz's PageTitle, plus a one-line tagline.
export default (() => {
  const SiteTitle: QuartzComponent = ({ fileData, cfg, displayClass }: QuartzComponentProps) => {
    const title = cfg?.pageTitle ?? "ChronoLog"
    const baseDir = pathToRoot(fileData.slug!)
    return (
      <div class={classNames(displayClass, "site-title")}>
        <h2 class="page-title">
          <a href={baseDir}>{title}</a>
        </h2>
        <p class="site-tagline">{TAGLINE}</p>
      </div>
    )
  }

  SiteTitle.css = style
  return SiteTitle
}) satisfies QuartzComponentConstructor
