import { getDate } from "../quartz/components/Date"
import { write } from "../quartz/plugins/emitters/helpers"
import { QuartzEmitterPlugin } from "../quartz/plugins/types"
import { escapeHTML } from "../quartz/util/escape"
import { FullSlug, joinSegments, simplifySlug } from "../quartz/util/path"

const FEED_TITLE = "ChronoLog"
const FEED_DESCRIPTION =
  "Tracked changes in ChatGPT, Claude Code and Cursor, from official release notes"
const FEED_LIMIT = 30
const FEED_SECTIONS = ["Changes/", "Releases/"]

type FeedItem = { slug: string; title: string; description: string; date: Date }

// RSS limited to Change Cards and Release pages (ContentIndex has enableRSS: false):
// home, product, theme and About pages are not news items.
export const ChronologFeed: QuartzEmitterPlugin = () => ({
  name: "ChronologFeed",
  async *emit(ctx, content) {
    const cfg = ctx.cfg.configuration
    const base = cfg.baseUrl ?? ""
    const items: FeedItem[] = []
    for (const [_tree, file] of content) {
      const slug = file.data.slug!
      if (!FEED_SECTIONS.some((section) => slug.startsWith(section))) continue
      items.push({
        slug: simplifySlug(slug),
        title: String(file.data.frontmatter?.title ?? slug),
        description: file.data.description ?? "",
        date: getDate(cfg, file.data) ?? new Date(),
      })
    }
    // Newest first; ties by slug so the feed is reproducible.
    items.sort((a, b) => b.date.getTime() - a.date.getTime() || a.slug.localeCompare(b.slug))
    const entries = items.slice(0, FEED_LIMIT).map((item) => {
      const url = `https://${joinSegments(base, encodeURI(item.slug))}`
      return `<item>
      <title>${escapeHTML(item.title)}</title>
      <link>${url}</link>
      <guid>${url}</guid>
      <description>${escapeHTML(item.description)}</description>
      <pubDate>${item.date.toUTCString()}</pubDate>
    </item>`
    })
    const feed = `<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0">
  <channel>
    <title>${escapeHTML(FEED_TITLE)}</title>
    <link>https://${base}</link>
    <description>${escapeHTML(FEED_DESCRIPTION)}</description>
    <language>en</language>
    ${entries.join("\n    ")}
  </channel>
</rss>`
    yield write({ ctx, content: feed, slug: "index" as FullSlug, ext: ".xml" })
  },
  externalResources: (ctx) => ({
    additionalHead: [
      <link
        rel="alternate"
        type="application/rss+xml"
        title={FEED_TITLE}
        href={`https://${ctx.cfg.configuration.baseUrl}/index.xml`}
      />,
    ],
  }),
})
