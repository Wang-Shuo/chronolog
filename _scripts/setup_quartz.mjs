import fs from "node:fs/promises"
import path from "node:path"
import { pathToFileURL } from "node:url"

const root = process.cwd()

const quartzSource = path.join(root, "node_modules", "quartz", "quartz")
const quartzRuntime = path.join(root, "quartz")
await fs.rm(quartzRuntime, { recursive: true, force: true })
await fs.cp(quartzSource, quartzRuntime, { recursive: true })

// The site icon and share image replace Quartz's own: Head links static/icon.png and
// static/og-image.png, and the Favicon emitter reads quartz/static/icon.png.
for (const name of ["icon.png", "og-image.png"]) {
  await fs.copyFile(path.join(root, "_scripts", "brand", name), path.join(quartzRuntime, "static", name))
}

const binPath = path.join(root, "node_modules", ".bin", "quartz")
const wrapperPath = path.join(root, "_scripts", "quartz_build_wrapper.mjs")
const wrapperUrl = pathToFileURL(wrapperPath).href
await fs.rm(binPath, { force: true })
await fs.writeFile(
  binPath,
  `#!/usr/bin/env node\nimport(${JSON.stringify(wrapperUrl)}).catch((error) => {\n  console.error(error)\n  process.exit(1)\n})\n`,
  "utf-8",
)
await fs.chmod(binPath, 0o755)
