import { QuartzFilterPlugin } from "../quartz/plugins/types"

// Explicit three-source MVP publication scope. Local historical records remain
// available in the Vault but are not emitted into HTML, search, or the graph.
export const ActiveChronolog: QuartzFilterPlugin = () => ({
  name: "ActiveChronolog",
  shouldPublish(_ctx, [_tree, file]) {
    const meta = file.data.frontmatter ?? {}
    if (meta.superseded === true || meta.superseded === "true") return false
    if (meta.source_type === "fixture" || meta.publication === "fixture") return false
    if (meta.product_name && !["ChatGPT", "Claude Code", "Cursor"].includes(String(meta.product_name))) return false
    if (meta.product && !["chatgpt", "claude-code", "cursor"].includes(String(meta.product))) return false
    return true
  },
})
