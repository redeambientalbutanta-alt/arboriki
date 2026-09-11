# Arboriki — Wiki de Arborização Urbana de São Paulo

Base de conhecimento coletiva sobre a legislação de arborização urbana do Município de São Paulo, publicada em formato wiki. Segue o padrão *LLM Wiki* de Andrej Karpathy: páginas curtas em Markdown, interligadas por `[[wiki-links]]` e construídas a partir de fontes primárias.

## Propósito

Apoiar movimentos ambientalistas na contestação de cortes arbitrários de árvores e subsidiar a revisão das leis ambientais sobre poda, corte, maciços arbóreos, áreas imunes, compensação e Termo de Compromisso Ambiental (TCA).

O trabalho tem dois eixos:

- **Eixo 1 — Legislação atual.** Mapear a norma vigente de forma didática. Apontar lacunas, termos vagos e ausência de regulamentação. Definir protocolos de fiscalização.
- **Eixo 2 — Aperfeiçoamento.** Escrever texto para emendas, decretos e normas que reforcem a proteção de áreas verdes.

O método de análise é a Legística e a Avaliação de Impacto Legislativo (AIL) *ex ante* e *ex post*.

## Estrutura

```
raw/          fontes primárias imutáveis (PDFs, recortes de Diário Oficial)
src/arboriki/ pacote Python: CLI de extração e scraper de HTML estático
.arboriki/    estado da CLI: manifest.json (versionado) e extracted/ (ignorado)
wiki/         páginas Markdown mantidas pelo Claude
  index.md                  índice geral
  log.md                    registro append-only de operações
  linha-tempo.md            cronologia de eventos
  noticias-relacionadas.md  registro de notícias de imprensa
  legislacao/               análises de normas vigentes e projetos de lei
  projetos/                 propostas de aperfeiçoamento (Eixo 2)
  assets/grafos/            grafos interativos (HTML) embutidos via iframe
lat.md/       grafo de conhecimento do projeto (spec, invariantes, "porquês")
```

Regra fixa: **nunca modifique nada em `raw/`**.

## Requisitos

1. Instale o [`uv`](https://docs.astral.sh/uv/).
2. Instale o [`lat`](https://www.npmjs.com/package/lat.md): `npm i -g lat.md`.
3. Para OCR de PDF digitalizado, instale o binário `tesseract` com o idioma `por`:
   `winget install --interactive UB-Mannheim.TesseractOCR` (marque *Portuguese* no instalador).

## Ambiente Python

```bash
uv sync                 # cria o venv (.venv/) e instala as dependências
```

## Ferramenta CLI — `arboriki`

A CLI faz a parte mecânica da ingestão: detecta o que mudou em `raw/` e extrai o texto puro. A análise legística e a escrita das páginas continuam sendo trabalho do Claude, pela skill `ingestao-wiki-legislativo`.

### `arboriki scan`

Lista as fontes de `raw/` e marca o que mudou desde a última extração.

```bash
uv run arboriki scan
```

- Compara o hash SHA-256 de cada arquivo com `.arboriki/manifest.json`.
- Marca cada fonte como `NOVO`, `ALTERADO` ou `OK`; `REMOVIDO` para arquivo que saiu de `raw/`.
- Ignora a pasta `raw/descarte/`.

### `arboriki extract`

Extrai o texto puro das fontes novas ou alteradas.

```bash
uv run arboriki extract              # só o que mudou
uv run arboriki extract --force      # reprocessa todas as fontes
```

- **PDF:** lê a camada de texto nativa com `pymupdf`. Se uma página tiver menos de 20 caracteres, rasteriza a 300 dpi e aplica OCR (`tesseract`, idioma `por`).
- **HTML:** decodifica ISO-8859-1 quando não for UTF-8 e remove `<script>`, `<style>`, `<nav>`, `<footer>`.
- Grava cada resultado em `.arboriki/extracted/`, preservando a subpasta de origem.
- Atualiza `.arboriki/manifest.json` com o hash, o caminho do texto e a contagem de caracteres.
- Uma falha em uma fonte não interrompe as outras; o comando encerra com código diferente de zero se houver falha.

### Variáveis de ambiente (OCR)

Copie `.env.example` para `.env` e ajuste. Carregue com `uv run --env-file .env arboriki extract`.

| Variável | Uso |
|---|---|
| `TESSERACT_CMD` | caminho do executável do Tesseract, se não estiver no PATH |
| `ARBORIKI_OCR_LANG` | idioma(s) do OCR (padrão `por`; combine com `+`, ex.: `por+eng`) |
| `TESSDATA_PREFIX` | pasta com `tessdata/`, se os `.traineddata` ficarem fora do padrão |

## Grafo de conhecimento — `lat`

```bash
lat search "<intenção>"    # antes de começar: busca semântica no grafo
lat section "<id>"         # lê a seção completa
lat check                  # depois de mexer em lat.md/ ou no código: valida links e refs
```

## Fluxo de trabalho

1. Coloque a fonte em `raw/` ou forneça a URL de um portal legislativo (Planalto, ALESP, Prefeitura de SP).
2. Rode `uv run arboriki extract`.
3. Rode a skill `ingestao-wiki-legislativo`. Ela lê o texto, mapeia as citações, rastreia a vigência de cada norma (skill `pesquisa-legislacao`), aplica a AIL, escreve as páginas em `wiki/` e atualiza os índices.
4. Rode `lat check`.

## Publicação

A wiki é publicada como site estático em `redeambientalbutanta-alt.github.io/arboriki` (Quartz 5), gerado a partir de `wiki/`. Link não divulgado, sem indexação — uso interno.

```bash
cd site
npm run sync              # copia ../wiki para site/content/ (gerado, nunca commitado)
npx quartz build --serve  # preview em http://localhost:8080
```

Cada `git push` na branch `main` publica automaticamente via GitHub Actions (`.github/workflows/deploy.yml`). Detalhes da arquitetura em `lat.md/publishing.md`.

## Skills do projeto

| Skill | Função |
|---|---|
| `ingestao-wiki-legislativo` | executa o fluxo de ingestão de ponta a ponta |
| `pesquisa-legislacao` | pesquisa e rastreia normas nos portais oficiais |
| `formatador-cypher-neo4j` | converte os relacionamentos jurídicos em blocos Cypher `MERGE` |
| `gerador-diagrama-drawio` | gera o diagrama Mermaid da análise |
| `gerador-mapa-interativo-d3blocks` | gera o grafo relacional interativo (HTML) |
