# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

# Wiki Arborização

Base de conhecimento coletiva sobre arborização urbana no Município de São Paulo, publicada em formato wiki. Segue o padrão LLM Wiki de Andrej Karpathy: páginas curtas interligadas por `[[wiki-links]]`, construídas a partir de fontes primárias em `raw/`.

## Propósito

Apoiar movimentos ambientalistas na contestação de cortes arbitrários de árvores em São Paulo. Subsidiar a revisão das leis ambientais sobre poda, corte, maciços arbóreos, áreas imunes ao corte, compensação, TCA e bosques.

## Dois eixos

Avalie todo documento processado nos dois eixos. Se a fonte tocar ambos, crie páginas nos dois e conecte-as por `[[wiki-links]]`.

- **Eixo 1 — Legislação atual.** Detalhe a norma de forma didática e esquemática. Aponte lacunas, termos vagos, ambiguidades e ausência de regulamentação. Defina protocolos de fiscalização. Cruze com bases abertas de emissão de TCA.
- **Eixo 2 — Aperfeiçoamento.** Escreva texto para emendas, decretos e normas que reforcem a proteção de áreas verdes.

Use a Legística (ciência da qualidade e da elaboração das leis) e a Avaliação de Impacto Legislativo (AIL) ex-ante e ex-post como método de análise.

# Estrutura de pastas

```
raw/          fontes primárias imutáveis (PDFs, recortes de Diário Oficial, relatórios de TCA)
src/arboriki/ pacote Python: CLI de extração (cli.py, extract.py), scraper de HTML estático
.arboriki/    estado da CLI: manifest.json (versionado) e extracted/ (texto puro, ignorado)
wiki/         páginas markdown mantidas pelo Claude
  index.md                  índice geral
  log.md                    registro append-only de operações
  linha-tempo.md            cronologia de eventos
  noticias-relacionadas.md  registro de notícias de imprensa
  legislacao/               análises de normas vigentes e projetos de lei
  projetos/                 propostas de leis e normas (Eixo 2)
  assets/grafos/            grafos interativos (HTML) embutidos nas páginas via iframe
lat.md/       grafo de conhecimento do projeto (spec, invariantes, "porquês")
```

Regras fixas:

- Nunca modifique nada em `raw/`.
- Nomeie páginas em minúsculas com hífens: `impactos-ambientais.md`.
- Escreva em português claro e direto (pt-BR).
- Se não conseguir ler um arquivo de `raw/`, mova-o para `raw/descarte/`.
- Quando não souber categorizar algo, pergunte ao usuário.

# Comandos

O ambiente Python é gerido por `uv` (`pyproject.toml` + `uv.lock`, Python >= 3.12). O venv fica em `.venv/`. O código-fonte é o pacote `src/arboriki/`.

```bash
uv sync                              # cria o venv e instala as dependências
uv add <pacote>                      # adiciona uma dependência
uv run arboriki scan                 # lista o que mudou em raw/ desde a última extração
uv run arboriki extract [--force]    # extrai texto puro de raw/ para .arboriki/extracted/
uv run python src/arboriki/scraper.py <url>   # scraper de HTML estático (crawl recursivo)
```

O OCR de PDF digitalizado exige o binário de sistema `tesseract` (idioma `por`), instalado à parte. A CLI rasteriza as páginas com `pymupdf`, então `poppler` não é necessário. Sem `tesseract` no PATH, defina `TESSERACT_CMD` (veja `.env.example`).

lat.md — rode sempre:

```bash
lat search "<intenção>"    # antes de começar: busca semântica no grafo
lat section "<id>"         # lê a seção completa
lat check                  # depois de mexer em lat.md/ ou no código: valida links e refs
```

`lat search` precisa de `LAT_LLM_KEY` (`sk-...` ou `vck_...`). Sem a chave, use `lat locate`.

Git: repositório iniciado, sem commits. Crie um branch antes de commitar.

# Fluxo da wiki

Dispare o fluxo quando o usuário adicionar um arquivo em `raw/` ou fornecer uma URL de portal legislativo oficial (Planalto, ALESP, CMSP).

Para executar a ingestão, use a skill `ingestao-wiki-legislativo`. A especificação recursiva completa — profundidade máxima, encoding, RegEx de citações, rastreabilidade — está em `lat.md/ingestion-flow.md`.

Passos, em ordem:

0. Rode `uv run arboriki extract` para extrair o texto puro das fontes novas ou alteradas de `raw/` para `.arboriki/extracted/`.
1. Leia a fonte inteira (o texto extraído ou o arquivo original). Aplique OCR se for PDF digitalizado.
2. Mapeie as citações a outras normas. Siga cada citação até `max_depth = 3`.
3. Crie a página de resumo. Norma vigente vai em `wiki/legislacao/`. Projeto de lei vai em `wiki/projetos/`.
4. Aplique a AIL e a bifurcação de eixos.
5. Crie ou atualize uma página de conceito para cada entidade importante (ex.: `[[termo-de-compromisso-ambiental-tca]]`).
6. Gere o diagrama Mermaid ao final da análise (skill `gerador-diagrama-drawio`). Se a malha for densa, gere também o grafo interativo (skill `gerador-mapa-interativo-d3blocks`).
7. Gere o bloco Cypher de relacionamentos (skill `formatador-cypher-neo4j`).
8. Atualize `wiki/index.md`, `wiki/log.md`, `wiki/linha-tempo.md` e `wiki/noticias-relacionadas.md`.

## Formato de página (padrão)

```markdown
# Título da Página

**Resumo**: Uma ou duas frases descrevendo esta página.

**Fontes**: Arquivos de raw/ dos quais esta página extrai informação.

**Última atualização**: Data.

---

Conteúdo. Títulos claros, parágrafos curtos. Vincule conceitos com [[wiki-links]].

## Páginas relacionadas

- [[conceito-relacionado-1]]
```

## Formato de análise legislativa

Para projetos de lei e normas, acrescente à página:

```markdown
## Identificação

- **Número**: XXX/AAAA
- **Autoria**: Nome do autor
- **Status**: em tramitação / aprovado / arquivado
- **Instância**: Câmara Municipal de SP / ALESP / outro

## O que propõe

Síntese objetiva do texto normativo em linguagem acessível.
Dispositivos ou princípios que servem de argumento para o movimento.

## Pontos de atenção ou lacunas

Disposições que enfraquecem a proteção, brechas ou contradições internas.

## Atores envolvidos

Autores, relatores, entidades que apoiam ou se opõem ao PL.
```

## Regras de citação

- Toda afirmação factual referencia sua fonte: `(fonte: nome-do-arquivo.pdf)`.
- Fonte de site legislativo: aponte o link direto para o Artigo, Parágrafo ou Inciso no HTML consultado.
- Se duas fontes divergirem, registre a contradição explicitamente na página.
- Afirmação sem amparo documental em `raw/`: marque `[verificar]`.

# Resposta a perguntas

1. Leia `wiki/index.md` para achar as páginas relevantes.
2. Leia essas páginas e sintetize a resposta.
3. Cite as páginas específicas do wiki que você usou.
4. Se a resposta não estiver no wiki, diga isso com clareza.
5. Se a resposta for valiosa, ofereça salvá-la como página nova.

# Auditoria (lint)

Quando o usuário pedir auditoria do wiki, reporte uma lista numerada com a correção sugerida para cada achado:

- Contradições entre páginas.
- Páginas órfãs (sem links de entrada de outras páginas).
- Conceitos citados em páginas que não têm página própria.
- Afirmações possivelmente desatualizadas por uma fonte mais recente.
- Páginas fora do formato padrão.

# Princípios de engenharia

## 1. Pense antes de codificar

Não presuma. Não esconda confusão. Explicite os tradeoffs. Declare suas premissas. Se houver múltiplas interpretações, apresente-as. Se houver uma abordagem mais simples, diga. Se algo não estiver claro, pare e pergunte.

## 2. Simplicidade em primeiro lugar

O mínimo de código que resolve o problema. Nada especulativo. Sem funcionalidades além do pedido, sem abstrações de uso único, sem "flexibilidade" não solicitada, sem tratamento de erro para cenários impossíveis. Se 200 linhas poderiam ser 50, reescreva.

## 3. Mudanças cirúrgicas

Mexa apenas no necessário. Não "melhore" código adjacente. Não refatore o que não está quebrado. Imite o estilo existente. Se notar código morto não relacionado, mencione — não delete. Remova imports e funções que as suas mudanças tornaram inúteis.

## 4. Execução orientada a objetivos

Transforme a tarefa em meta verificável. "Adicionar validação" vira "escreva testes para entradas inválidas, depois faça-os passar". "Corrigir o bug" vira "escreva um teste que o reproduz, depois faça-o passar". Para tarefas multi-etapa, declare um plano curto com a checagem de cada passo.

# Fontes regulatórias de partida

Malha inicial para a ingestão recursiva. Disponíveis em HTML estático nos portais do Planalto (federal) e da Prefeitura de SP (municipal).

## Eixo 1 — Calçadas, passeios públicos e acessibilidade

- **Lei Municipal 15.442/2011** — limpeza, fechamento de terrenos e passeios em SP.
- **Lei Municipal 13.293/2002** — diretrizes de "Calçadas Verdes".
- **Decreto Municipal 59.671/2020** — consolida os critérios vigentes de padronização de calçadas.
- Histórico (revogados, rastrear só como elos de evolução temporal): Decretos 27.505/1988, 45.904/2005 e 52.903/2012.

## Eixos 1 e 2 — Manejo, poda, arborização e fiscalização

- **Lei Municipal 17.794/2022** — Código de Arborização Urbana vigente. Revogou a Lei 10.365/1987 e a Lei 13.646/2003.
- **Decreto Municipal 61.859/2022** — regulamenta os laudos e relatórios de manejo arbóreo.
- **Portaria Conjunta SVMA/SMJ/SMSU/SMSUB 08/2024** — Plano Municipal de Arborização Urbana (PMAU) e fiscalização integrada.
- **Lei Federal 9.605/1998** e **Decreto 6.514/2008** — crimes ambientais federais.

## Eixo 2 — Compensação, TCA e parcerias

- **Portaria SVMA 130/2013** — critérios e procedimentos de compensação por corte de árvores.
- **Decreto Municipal 58.156/2018** — programa "Adote uma Praça" e cooperação de áreas verdes.

# Skills do projeto

- **`ingestao-wiki-legislativo`** — executa o fluxo da wiki de ponta a ponta para uma nova fonte.
- **`formatador-cypher-neo4j`** — converte os relacionamentos jurídicos em blocos Cypher `MERGE`.
- **`gerador-diagrama-drawio`** — gera o diagrama Mermaid da análise, pronto para o Draw.io.
- **`gerador-mapa-interativo-d3blocks`** — gera o grafo relacional interativo (HTML) da malha de leis, embutido na página via iframe.
- **`pesquisa-legislacao`** — pesquisa e rastreia normas nos portais da Prefeitura de SP, da ALESP e do Planalto (vigência, revogação, regulamentação).

# Integração com lat.md

`lat.md/` guarda o "o quê" e o "porquê" do projeto. O código aponta de volta com comentários `# @lat: [[secao]]`.

```
lat.md/ingestion-flow.md    spec do fluxo de ingestão de PDF e HTML estático
lat.md/cypher-model.md       ontologia Neo4j (labels e arestas)
lat.md/diagram-style.md      padrão visual do diagrama Mermaid e do grafo d3graph
src/arboriki/extract.py      # @lat: [[ingestion-flow#...#Ferramenta de extração — CLI arboriki]]
src/arboriki/scraper.py      # @lat: [[ingestion-flow]]
```

%% lat:begin %%
# Before starting work

- Run `lat search` to find sections relevant to your task. Read them to understand the design intent before writing code.
- Run `lat expand` on user prompts to expand any `[[refs]]` — this resolves section names to file locations and provides context.

# Post-task checklist (REQUIRED — do not skip)

After EVERY task, before responding to the user:

- [ ] Update `lat.md/` if you added or changed any functionality, architecture, tests, or behavior
- [ ] Run `lat check` — all wiki links and code refs must pass
- [ ] Do not skip these steps. Do not consider your task done until both are complete.

---

# What is lat.md?

This project uses [lat.md](https://www.npmjs.com/package/lat.md) to maintain a structured knowledge graph of its architecture, design decisions, and test specs in the `lat.md/` directory. It is a set of cross-linked markdown files that describe **what** this project does and **why** — the domain concepts, key design decisions, business logic, and test specifications. Use it to ground your work in the actual architecture rather than guessing.

# Commands

```bash
lat locate "Section Name"      # find a section by name (exact, fuzzy)
lat refs "file#Section"        # find what references a section
lat search "natural language"  # semantic search across all sections
lat expand "user prompt text"  # expand [[refs]] to resolved locations
lat check                      # validate all links and code refs
```

Run `lat --help` when in doubt about available commands or options.

If `lat search` fails because no API key is configured, explain to the user that semantic search requires a key provided via `LAT_LLM_KEY` (direct value), `LAT_LLM_KEY_FILE` (path to key file), or `LAT_LLM_KEY_HELPER` (command that prints the key). Supported key prefixes: `sk-...` (OpenAI) or `vck_...` (Vercel). If the user doesn't want to set it up, use `lat locate` for direct lookups instead.

# Syntax primer

- **Section ids**: `lat.md/path/to/file#Heading#SubHeading` — full form uses project-root-relative path (e.g. `lat.md/tests/search#RAG Replay Tests`). Short form uses bare file name when unique (e.g. `search#RAG Replay Tests`, `cli#search#Indexing`).
- **Wiki links**: `[[target]]` or `[[target|alias]]` — cross-references between sections. Can also reference source code: `[[src/foo.ts#myFunction]]`.
- **Source code links**: Wiki links in `lat.md/` files can reference functions, classes, constants, and methods in TypeScript/JavaScript/Python/Rust/Go/C files. Use the full path: `[[src/config.ts#getConfigDir]]`, `[[src/server.ts#App#listen]]` (class method), `[[lib/utils.py#parse_args]]`, `[[src/lib.rs#Greeter#greet]]` (Rust impl method), `[[src/app.go#Greeter#Greet]]` (Go method), `[[src/app.h#Greeter]]` (C struct). `lat check` validates these exist.
- **Code refs**: `// @lat: [[section-id]]` (JS/TS/Rust/Go/C) or `# @lat: [[section-id]]` (Python) — ties source code to concepts

# Test specs

Key tests can be described as sections in `lat.md/` files (e.g. `tests.md`). Add frontmatter to require that every leaf section is referenced by a `// @lat:` or `# @lat:` comment in test code:

```markdown
---
lat:
  require-code-mention: true
---
# Tests

Authentication and authorization test specifications.

## User login

Verify credential validation and error handling for the login endpoint.

### Rejects expired tokens
Tokens past their expiry timestamp are rejected with 401, even if otherwise valid.

### Handles missing password
Login request without a password field returns 400 with a descriptive error.
```

Every section MUST have a description — at least one sentence explaining what the test verifies and why. Empty sections with just a heading are not acceptable. (This is a specific case of the general leading paragraph rule below.)

Each test in code should reference its spec with exactly one comment placed next to the relevant test — not at the top of the file:

```python
# @lat: [[tests#User login#Rejects expired tokens]]
def test_rejects_expired_tokens():
    ...

# @lat: [[tests#User login#Handles missing password]]
def test_handles_missing_password():
    ...
```

Do not duplicate refs. One `@lat:` comment per spec section, placed at the test that covers it. `lat check` will flag any spec section not covered by a code reference, and any code reference pointing to a nonexistent section.

# Section structure

Every section in `lat.md/` **must** have a leading paragraph — at least one sentence immediately after the heading, before any child headings or other block content. The first paragraph must be ≤250 characters (excluding `[[wiki link]]` content). This paragraph serves as the section's overview and is used in search results, command output, and RAG context — keeping it concise guarantees the section's essence is always captured.

```markdown
# Good Section

Brief overview of what this section documents and why it matters.

More detail can go in subsequent paragraphs, code blocks, or lists.

## Child heading

Details about this child topic.
```

```markdown
# Bad Section

## Child heading

Details about this child topic.
```

The second example is invalid because `Bad Section` has no leading paragraph. `lat check` validates this rule and reports errors for missing or overly long leading paragraphs.
%% lat:end %%
