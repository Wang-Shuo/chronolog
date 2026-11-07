import { readFileSync } from "node:fs"
import { load } from "js-yaml"

type Product = { name: string; display_name: string; enabled?: boolean }

// Resolve from the code root, including builds whose vault is an isolated copy.
// Collection, publication and timeline filters share this catalog.
const sources = load(readFileSync("_scripts/sources.yaml", "utf8")) as { products: Product[] }
export const ACTIVE_PRODUCTS = sources.products.filter((product) => product.enabled !== false)

export const SITE_TAGLINE = "Tracked changes in AI products"
export const SITE_DESCRIPTION = `${SITE_TAGLINE}, from official release notes`
