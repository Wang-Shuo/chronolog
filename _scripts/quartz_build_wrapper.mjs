import { spawn } from "node:child_process"
import path from "node:path"

const root = process.cwd()
const args = process.argv.slice(2)

if (
  args[0] === "build" &&
  !args.includes("--directory") &&
  !args.includes("-d")
) {
  args.splice(1, 0, "--directory", ".")
}

const quartzCli = path.join(root, "quartz", "bootstrap-cli.mjs")
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
