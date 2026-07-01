import { spawn } from "node:child_process"
import fs from "node:fs/promises"
import path from "node:path"

const root = process.cwd()
const args = process.argv.slice(2)

async function exists(target) {
  try {
    await fs.access(target)
    return true
  } catch {
    return false
  }
}

async function mirrorVaultContent() {
  const contentRoot = path.join(root, "content")
  await fs.rm(contentRoot, { recursive: true, force: true })
  await fs.mkdir(contentRoot, { recursive: true })

  for (const directory of ["Products", "Changes", "Releases", "Themes", "Alerts"]) {
    const source = path.join(root, directory)
    if (await exists(source)) {
      await fs.cp(source, path.join(contentRoot, directory), { recursive: true })
    }
  }

  const index = path.join(root, "index.md")
  if (await exists(index)) {
    await fs.copyFile(index, path.join(contentRoot, "index.md"))
  }
}

if (args[0] === "build") {
  await mirrorVaultContent()
}

const quartzCli = path.join(root, "node_modules", "quartz", "quartz", "bootstrap-cli.mjs")
const child = spawn(process.execPath, [quartzCli, ...args], {
  cwd: root,
  stdio: "inherit",
})

child.on("exit", (code, signal) => {
  if (signal) {
    process.kill(process.pid, signal)
  } else {
    process.exit(code ?? 0)
  }
})
