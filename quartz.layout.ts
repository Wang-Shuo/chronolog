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
// thousands of leaves in the sidebar hides the entry points. filterFn is serialized with
// toString() and run in the browser, so it must not reference anything outside itself.
const explorer = () =>
  Component.Explorer({
    folderDefaultState: "open",
    filterFn: (node) => !["tags", "Changes", "Releases", "Alerts"].includes(node.slugSegment),
  })

// The local graph is useful around a card or a theme; on aggregate pages it is noise.
const graph = Component.ConditionalRender({
  component: Component.Graph(),
  condition: (props) => {
    const s = props.fileData.slug ?? ""
    return s.startsWith("Changes/") || s.startsWith("Themes/")
  },
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
