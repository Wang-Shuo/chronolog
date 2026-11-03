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
