import FolderContent from "../quartz/components/pages/FolderContent"
import {
  QuartzComponent,
  QuartzComponentConstructor,
  QuartzComponentProps,
} from "../quartz/components/types"
import { htmlToJsx } from "../quartz/util/jsx"

// Folder pages render their folder note and then list the folder's pages. The archive's
// folder note (Archive/index.md, tagged "archive") already lists every month with
// per-product counts, so its folder page shows only the note; other folders are unchanged.
export default (() => {
  const Listing = FolderContent()
  const ChronologFolderContent: QuartzComponent = (props: QuartzComponentProps) => {
    const tags = props.fileData.frontmatter?.tags ?? []
    if (!tags.includes("archive")) {
      return <Listing {...props} />
    }
    return (
      <div class="popover-hint">
        <article>{htmlToJsx(props.fileData.filePath!, props.tree)}</article>
      </div>
    )
  }

  ChronologFolderContent.css = Listing.css
  return ChronologFolderContent
}) satisfies QuartzComponentConstructor
