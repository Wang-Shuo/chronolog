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
