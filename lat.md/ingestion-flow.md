# Ingestion Pipeline Specification
<!-- id: ingestion-flow -->

Toda ingestão processa uma fonte bruta (`raw/` ou URL de portal oficial) em duas saídas: registros JSON para o grafo Neo4j e páginas markdown em `wiki/`. Esta seção fixa os invariantes; a skill `ingestao-wiki-legislativo` executa o fluxo.

## Escopo dos dois eixos

Toda fonte é avaliada nos dois eixos do projeto antes de virar página, sob a ótica da Legística e da Avaliação de Impacto Legislativo (AIL) ex-ante e ex-post.

- **Eixo 1 — Legislação atual.** Mapeamento didático do texto, protocolos de fiscalização, cruzamento com dados de TCA, alertas em vermelho/laranja para lacunas, termos vagos e ambiguidades.
- **Eixo 2 — Aperfeiçoamento.** Alternativas textuais para emendas, decretos e melhorias na proteção de áreas verdes.

Se a fonte tocar os dois eixos, a ingestão cria uma página em cada um e as conecta por `[[wiki-links]]`.

## Mapeamento recursivo de citações

A ingestão varre o texto capturado atrás de outras normas e as segue até um limite de profundidade, para construir a malha de relações sem entrar em laço infinito.

- **RegEx de menções:** `(?:Lei|Decreto|Portaria|Resolução|PL|Projeto de Lei)\s+(?:n[º°.]\s*)?([0-9.]+)(?:/(?:[0-9]{2,4})|\s+de\s+[0-9]{4})`.
- **Links `<a>`:** também são seguidos, além das menções textuais.
- **`visited_nodes`:** registro global de nós já visitados, para não reprocessar.
- **Conexões indiretas:** cruzar o tema material (compensação, manejo, poda, fiscalização) com normas que não se citam entre si, sempre justificando o nexo.

## Rastreio de vigência nos portais

Toda norma citada é seguida no portal oficial para saber se está vigente, foi alterada ou revogada. A skill `pesquisa-legislacao` executa a navegação; esta seção fixa o que rastrear.

- **Prefeitura de SP** (`legislacao.prefeitura.sp.gov.br`, UTF-8): usar sempre `/{slug}/consolidado`; seguir `/{slug}/revogado-por`, `/{slug}/regulamentacoes` e as âncoras `#historico` e `#correlacionadas`. Marcadores no corpo: `(Redação dada pela ...)`, `(Incluído pela ...)`, `(Revogado pela ...)`, `(eficácia suspensa pela ADIN ...)`. Conhecendo número e data, o slug é construível diretamente (`{tipo}-{numero}-de-{dia}-de-{mês}-de-{ano}`) — ver `pesquisa-legislacao`. O portal responde HTTP 200 mesmo para slug inexistente (corpo "404 - Página não encontrada"): valide pelo corpo. Leia sempre o Anexo quando o corpo remeter a ele.
- **ALESP** (`al.sp.gov.br`, ISO-8859-1): texto em `/repositorio/legislacao/{tipo}/{ano}/{tipo}-{numero}-{dd.mm.aaaa}.html` (sem alterações posteriores); ficha da norma em `/norma/{id}`; navegação de revogações ainda não mapeada — marcar `[verificar]`.
- **Federal** (`planalto.gov.br/ccivil_03`, ISO-8859-1): texto revogado aparece riscado (`<strike>`) com nota "(Revogado pela ...)"; conferir a linha "Texto compilado" / "Vide" no topo.
- Uma norma citada como vigente por uma fonte antiga (ex.: manual técnico) mas revogada no portal gera registro explícito de divergência na página da wiki.

## Constraints

Invariantes que toda ingestão respeita, qualquer que seja a fonte.

- **Max Depth:** a raspagem recursiva de HTML estático da CMSP/Planalto para em `max_depth = 3`.
- **Encoding:** links e páginas de HTML estático antigo são decodificados explicitamente de ISO-8859-1 para UTF-8.
- **Limpeza de HTML:** descartar `<script>`, `<style>`, `<nav>` e `<footer>` antes de extrair o texto.
- **Rastreabilidade:** todo fato escrito em `wiki/` carrega `(fonte: nome-do-arquivo.ext)` ou um link direto para o Artigo/Parágrafo/Inciso; sem amparo documental, recebe a tag `[verificar]`.
- **Divergência:** contradição entre duas fontes é registrada explicitamente na página.
- **Texto oficial:** toda página de norma traz, na Identificação, o link da norma no portal oficial da esfera (Prefeitura de SP, ALESP ou Planalto), mesmo quando a fonte ingerida foi um PDF de `raw/`. O link é validado pelo corpo da página; sem confirmação, o campo recebe `[verificar]`.
- **Cifrão:** valor em reais é escrito `R\$`, com barra invertida. O Obsidian e o Quartz leem o trecho entre dois cifrões como fórmula e desfiguram o texto. Dentro de bloco de código ou de crases o cifrão fica sem barra.

## Saídas

Cada fonte gera artefatos nas duas camadas, mantidas em sincronia.

- **Wiki:** página de resumo (em `wiki/legislacao/` ou `wiki/projetos/` quando for norma ou PL), páginas de conceito, diagrama Mermaid — e grafo interativo em `wiki/assets/grafos/` quando a malha for densa ([[diagram-style]]) — e bloco Cypher ([[cypher-model]]).
- **Índices append-only:** `wiki/index.md`, `wiki/log.md`, `wiki/linha-tempo.md` e `wiki/noticias-relacionadas.md`.
- **Etiquetas:** toda página criada ou alterada sai com o bloco `tags:` conforme [[ingestion-flow#Ingestion Pipeline Specification#Etiquetas]].

## Etiquetas

Toda página de `wiki/` abre com um bloco YAML `tags:` em cinco categorias. As etiquetas permitem filtrar por conceito e por esfera federativa no Obsidian e no site, sem depender dos links entre páginas.

- **`tipo/`** — o que a página é: `lei`, `decreto`, `portaria`, `proposta`, `conceito`, `analise`, `metodo`, `apoio`. Exatamente uma por página.
- **`esfera/`** — `municipal`, `estadual`, `federal`. Em página de norma, a esfera da norma; em página de conceito ou de análise, a esfera de cada norma analisada. Mesmo valor do atributo `esfera` de [[cypher-model#Modelo de Grafo Neo4j#Labels]].
- **`situacao/`** — `vigente`, `parcialmente-revogada`, `revogada`, `sub-judice`, `em-tramitacao`, `arquivada`. Só em norma ou proposta; espelha o campo "Status".
- **`eixo/`** — `1-legislacao-atual`, `2-aperfeicoamento`. Uma página pode ter os dois.
- **`conceito/`** — uma etiqueta por conceito de arborização que a página trata.

O vocabulário é fechado e mora em `wiki/etiquetas.md`: uma etiqueta nova entra primeiro lá. Etiquetas vão em minúsculas, sem acento, com hífens, na ordem tipo, esfera, situação, eixo, conceito.

Em página de norma, a etiqueta de conceito exige duas condições: a página trata do conceito e o termo está no texto da norma (conferir em `wiki/assets/dados/conceitos-por-norma.csv`). A etiqueta não diz o papel da norma — define, redefine, usa ou conflita fica na lente 4 de [[analysis-lenses#Lentes de análise#As quatro lentes]].

Categorias avaliadas e não adotadas: `orgao/` (quem edita ou decide), `achado/` (tipo de falha da norma), papel no conceito como terceiro nível, e `tema/` (descartada por repetir `conceito/`).

## Ferramenta de extração — CLI arboriki

O comando `arboriki` faz a parte mecânica da ingestão: detecta o que mudou em `raw/` e extrai texto puro. A análise continua sendo trabalho do Claude, via a skill `ingestao-wiki-legislativo`.

- `arboriki scan` — lista as fontes de `raw/` (menos `raw/descarte/`) e marca `NOVO`, `ALTERADO` ou `OK` contra o hash sha256 em `.arboriki/manifest.json`.
- `arboriki extract [--force]` — extrai o texto das fontes novas ou alteradas para `.arboriki/extracted/`, preservando a subpasta, e atualiza o manifesto.
- **PDF:** texto pela camada nativa (`pymupdf`); página com menos de 20 caracteres é rasterizada a 300 dpi e passada ao OCR (`tesseract`, idioma `por`).
- **HTML:** decodifica ISO-8859-1 quando não for UTF-8 e remove `<script>`, `<style>`, `<nav>`, `<footer>` (mesma regra de [[ingestion-flow#Ingestion Pipeline Specification#Constraints|Constraints]]).
- `tesseract` é binário de sistema, instalado à parte. `TESSERACT_CMD` e `ARBORIKI_OCR_LANG` sobrescrevem os padrões.
