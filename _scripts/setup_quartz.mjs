import fs from "node:fs/promises"
import path from "node:path"
import { pathToFileURL } from "node:url"

const root = process.cwd()

const quartzSource = path.join(root, "node_modules", "quartz", "quartz")
const quartzRuntime = path.join(root, "quartz")
await fs.rm(quartzRuntime, { recursive: true, force: true })
await fs.cp(quartzSource, quartzRuntime, { recursive: true })

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
