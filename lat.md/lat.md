This directory defines the high-level concepts, business logic, and architecture of this project using markdown. It is managed by [lat.md](https://www.npmjs.com/package/lat.md) — a tool that anchors source code to these definitions. Install the `lat` command with `npm i -g lat.md` and run `lat --help`.

## Índice

Seções que descrevem o "o quê" e o "porquê" do projeto Wiki Arborização.

- [[ingestion-flow]] — spec do fluxo de ingestão recursiva de PDF e HTML estático nas duas saídas (grafo e wiki).
- [[cypher-model]] — ontologia Neo4j: labels, arestas e formato de saída `MERGE`.
- [[diagram-style]] — padrão visual dos diagramas Mermaid da wiki, colável no Draw.io.
- [[publishing]] — publicação da wiki como site estático (Quartz 5) em GitHub Pages, deploy automático via GitHub Actions.
