import { createHash } from "node:crypto"
import { promises as fs } from "node:fs"
import { dirname } from "node:path"
import { QuartzEmitterPluginInstance, QuartzTransformerPluginInstance } from "../quartz/plugins/types"
import { BuildCtx } from "../quartz/util/ctx"
import { FilePath, joinSegments } from "../quartz/util/path"

// OFM's callout/Mermaid resources are identical on every page. Emit their original
// bytes once instead of repeating them throughout a large release archive. Keep
// resources that depend on their inline URL context in their original form.
export function shareTransformerResources(plugin: QuartzTransformerPluginInstance) {
  function bundle(ctx: BuildCtx) {
    const original = plugin.externalResources?.(ctx) ?? {}
    const assets = new Map<string, string>()
    const prefix = new URL(`https://${ctx.cfg.configuration.baseUrl ?? "localhost"}`).pathname.replace(/\/+$/, "")
    const asset = (content: string, extension: string) => {
      const digest = createHash("sha256").update(content).digest("hex")
      const path = `static/shared-${digest}.${extension}`
      assets.set(path, content)
      return `${prefix}/${path}`
    }
    const resources = {
      ...original,
      css: original.css?.map((resource) =>
        resource.inline && !/(?:url\s*\(|@import\b)/i.test(resource.content)
          ? { ...resource, content: asset(resource.content, "css"), inline: false }
          : resource,
      ),
      js: original.js?.map((resource) => {
        if (resource.contentType !== "inline" || /(?:import\.meta|document\.currentScript|\b(?:from\s*|import\s*(?:\(\s*)?)["'](?:\.|\/))/.test(resource.script)) {
          return resource
        }
        const { script, ...attributes } = resource
        return { ...attributes, contentType: "external" as const, src: asset(script, "js") }
      }),
    }
    return { resources, assets }
  }

  const emit: QuartzEmitterPluginInstance["emit"] = async function* (ctx) {
    for (const [asset, content] of bundle(ctx).assets) {
      const destination = joinSegments(ctx.argv.output, asset) as FilePath
      await fs.mkdir(dirname(destination), { recursive: true })
      await fs.writeFile(destination, content)
      yield destination
    }
  }
  return {
    transformer: { ...plugin, externalResources: (ctx: BuildCtx) => bundle(ctx).resources },
    emitter: { name: "SharedTransformerResources", emit, partialEmit: emit },
  }
}
