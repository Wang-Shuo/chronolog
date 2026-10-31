import fs from "fs"
import { dirname } from "path"
import { globby } from "globby"
import { FilePath, QUARTZ, joinSegments } from "../quartz/util/path"
import { QuartzEmitterPlugin } from "../quartz/plugins/types"

// Quartz's Static emitter globs quartz/static with gitignore applied, and quartz/ is
// git-ignored here (it is copied from node_modules on install), so it emitted nothing
// and every page linked a missing static/icon.png and static/og-image.png.
export const ChronologStatic: QuartzEmitterPlugin = () => ({
  name: "ChronologStatic",
  async *emit({ argv }) {
    const staticPath = joinSegments(QUARTZ, "static")
    const outputStaticPath = joinSegments(argv.output, "static")
    for (const fp of await globby("**", { cwd: staticPath })) {
      const dest = joinSegments(outputStaticPath, fp) as FilePath
      await fs.promises.mkdir(dirname(dest), { recursive: true })
      await fs.promises.copyFile(joinSegments(staticPath, fp), dest)
      yield dest
    }
  },
  async *partialEmit() {},
})
