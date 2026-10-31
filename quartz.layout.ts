import { PageLayout, SharedLayout } from "./quartz/cfg"
import * as Component from "./quartz/components"
import SiteTitle from "./_scripts/site_title"

const base = process.env.CHRONOLOG_BASE_URL ?? "localhost:8080"
const scheme = /^(localhost|127\.0\.0\.1)([:/]|$)/.test(base) ? "http" : "https"
const siteUrl = `${scheme}://${base.replace(/\/+$/, "")}`

export const sharedPageComponents: SharedLayout = {
  head: Component.Head(),
  header: [],
  afterBody: [],
  footer: Component.Footer({
    links: {
      GitHub: "https://github.com/Wang-Shuo/chronolog",
      About: `${siteUrl}/About`,
      RSS: `${siteUrl}/index.xml`,
    },
  }),
}

// Cards, releases and alerts are reached from product, theme and release pages; listing
// thousands of leaves in the sidebar hides the entry points. filterFn and sortFn are
// serialized with toString() and run in the browser, so they must not reference anything
// outside themselves, nor define inner functions (the build wraps those in an undefined
// __name helper). Folders come in reading order (Products, Themes, Archive) and months
// newest first; month titles such as "April 2026" would otherwise sort by name.
const explorer = () =>
  Component.Explorer({
    folderDefaultState: "open",
    filterFn: (node) => !["tags", "Changes", "Releases", "Alerts"].includes(node.slugSegment),
    sortFn: (a, b) => {
      if (a.isFolder !== b.isFolder) return a.isFolder ? -1 : 1
      const folders = ["Products", "Themes", "Archive"]
      const rankA = folders.includes(a.slugSegment) ? folders.indexOf(a.slugSegment) : folders.length
      const rankB = folders.includes(b.slugSegment) ? folders.indexOf(b.slugSegment) : folders.length
      if (rankA !== rankB) return rankA - rankB
      const month = /^\d{4}-\d{2}$/
      if (month.test(a.slugSegment) && month.test(b.slugSegment)) {
        return b.slugSegment.localeCompare(a.slugSegment)
      }
      return a.displayName.localeCompare(b.displayName, undefined, { numeric: true, sensitivity: "base" })
    },
  })

// The local graph is useful around a card. Around a theme it draws every card of the
// theme (hundreds of nodes), and its canvas widened theme pages on phones.
const graph = Component.ConditionalRender({
  component: Component.Graph(),
  condition: (props) => (props.fileData.slug ?? "").startsWith("Changes/"),
})

export const defaultContentPageLayout: PageLayout = {
  beforeBody: [
    Component.Breadcrumbs(),
    // Vault pages already have their own H1; avoid repeating long card titles.
    Component.ContentMeta({ showReadingTime: false }),
    Component.TagList(),
  ],
  left: [
    SiteTitle(),
    Component.MobileOnly(Component.Spacer()),
    Component.Search(),
    Component.Darkmode(),
    Component.DesktopOnly(explorer()),
  ],
  right: [graph, Component.DesktopOnly(Component.TableOfContents()), Component.Backlinks()],
}

export const defaultListPageLayout: PageLayout = {
  beforeBody: [
    Component.Breadcrumbs(),
    Component.ArticleTitle(),
    Component.ContentMeta({ showReadingTime: false }),
  ],
  left: [
    SiteTitle(),
    Component.MobileOnly(Component.Spacer()),
    Component.Search(),
    Component.Darkmode(),
    Component.DesktopOnly(explorer()),
  ],
  right: [],
}
