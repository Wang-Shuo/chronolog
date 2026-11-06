import { QuartzFilterPlugin } from "../quartz/plugins/types"
import { ACTIVE_PRODUCTS } from "./products"

// Disabled products and fixture records stay local. Adding an enabled source
// automatically enables its real records in HTML, search and the graph.
export const ActiveChronolog: QuartzFilterPlugin = () => {
  const names = new Set(ACTIVE_PRODUCTS.map((product) => product.display_name))
  const ids = new Set(ACTIVE_PRODUCTS.map((product) => product.name))
  return {
    name: "ActiveChronolog",
    shouldPublish(_ctx, [_tree, file]) {
      const meta = file.data.frontmatter ?? {}
      if (meta.superseded === true || meta.superseded === "true") return false
      if (meta.source_type === "fixture" || meta.publication === "fixture") return false
      if (meta.product_name && !names.has(String(meta.product_name))) return false
      if (meta.product && !ids.has(String(meta.product))) return false
      return true
    },
  }
}
