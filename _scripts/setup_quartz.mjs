import fs from "node:fs/promises"
import path from "node:path"
import { pathToFileURL } from "node:url"

const root = process.cwd()

async function removeIfWrongLink(target, expected) {
  try {
    const stat = await fs.lstat(target)
    if (!stat.isSymbolicLink()) {
      return
    }
    const current = await fs.readlink(target)
    if (current !== expected) {
      await fs.rm(target, { recursive: true, force: true })
    }
  } catch (error) {
    if (error.code !== "ENOENT") {
      throw error
    }
  }
}

async function ensureSymlink(target, relativeSource, type) {
  await removeIfWrongLink(target, relativeSource)
  try {
    await fs.lstat(target)
  } catch (error) {
    if (error.code !== "ENOENT") {
      throw error
    }
    await fs.symlink(relativeSource, target, type)
  }
}

await ensureSymlink(path.join(root, "quartz"), path.join("node_modules", "quartz", "quartz"), "dir")

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
