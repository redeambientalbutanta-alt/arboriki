// Copia wiki/ (fonte da verdade) para content/ (pasta gerada, ignorada pelo git).
// Roda antes de cada build, local ou no CI — content/ nunca é a fonte, sempre um espelho.
import { cpSync, mkdirSync, rmSync, writeFileSync } from "node:fs"
import { fileURLToPath } from "node:url"
import path from "node:path"

const siteDir = path.dirname(path.dirname(fileURLToPath(import.meta.url)))
const wikiDir = path.join(siteDir, "..", "wiki")
const contentDir = path.join(siteDir, "content")

rmSync(contentDir, { recursive: true, force: true })
mkdirSync(contentDir, { recursive: true })
cpSync(wikiDir, contentDir, { recursive: true })

// Site não é divulgado nem deve ser indexado por buscadores.
writeFileSync(path.join(contentDir, "robots.txt"), "User-agent: *\nDisallow: /\n")

console.log(`wiki/ copiado para site/content/`)
