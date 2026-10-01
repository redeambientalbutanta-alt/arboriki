---
name: ingestao-wiki-legislativo
description: >-
  Processa uma nova fonte (arquivo em raw/ ou URL de portal legislativo: Planalto, ALESP, CMSP)
  e atualiza a wiki de arborização de ponta a ponta: leitura integral, mapeamento recursivo de
  citações, Avaliação de Impacto Legislativo ex-ante/ex-post, páginas de resumo e de conceito,
  diagrama e índices. Use quando o usuário adicionar um documento em raw/ ou
  pedir para ingerir uma norma ou projeto de lei.
---

# Ingestão e mapeamento recursivo da wiki legislativa

Atue como especialista em legística, ciência de dados jurídica e direito ambiental municipal de São Paulo. Processe a fonte de forma estritamente referenciada e atualize a estrutura de `wiki/`.

## Antes de começar

1. Rode `lat section "ingestion-flow"`. Respeite os invariantes: `max_depth = 3`, encoding ISO-8859-1 para UTF-8, rastreabilidade de todo fato.
2. Leia `wiki/index.md` para saber o que já existe.

## Passos

### 1. Leitura da fonte

- Leia o documento inteiro.
- PDF digitalizado: aplique OCR (`pytesseract` sobre imagens de `pdf2image`).
- HTML estático antigo: decodifique de ISO-8859-1 para UTF-8. Remova `<script>`, `<style>`, `<nav>` e `<footer>`.
- Arquivo ilegível: mova para `raw/descarte/` e avise o usuário.

### 2. Mapeamento de citações

- Rastreie links `<a>` e menções textuais via RegEx: `(?:Lei|Decreto|Portaria|Resolução|PL|Projeto de Lei)\s+(?:n[º°.]\s*)?([0-9.]+)(?:/(?:[0-9]{2,4})|\s+de\s+[0-9]{4})`.
- Mantenha um `visited_nodes` global. Pare em `max_depth = 3`.
- Cruze o tema material (compensação, poda, fiscalização) com normas que não se citam diretamente. Justifique o nexo.

### 3. Página de resumo

- Crie a página em `wiki/` com o nome da fonte, em minúsculas com hífens.
- Norma vigente: `wiki/legislacao/`. Projeto de lei ou proposta: `wiki/projetos/`.
- Use o "Formato de página (padrão)" e o "Formato de análise legislativa" do `CLAUDE.md`.
- Preencha o campo **Texto oficial** da Identificação com o link da norma no portal oficial da esfera: Prefeitura de SP (municipal), ALESP (estadual), Planalto (federal). Faça isso mesmo quando a fonte for um PDF de `raw/`.
- Ache o link com a skill `pesquisa-legislacao`. Abra o link e confira o corpo: o portal da Prefeitura devolve HTTP 200 para página inexistente.
- Sem link confirmado: escreva `[verificar]` no campo.

### 4. Avaliação de Impacto e bifurcação de eixos

- **Eixo 1:** mapeie o texto de forma didática. Marque em vermelho/laranja as lacunas, os termos vagos e as ambiguidades. Aponte protocolos de fiscalização e cruzamento com dados de TCA.
- **Eixo 2:** escreva alternativas textuais para emendas e decretos.
- Se a fonte tocar os dois eixos, crie uma página em cada um e conecte-as por `[[wiki-links]]`.

### 5. Páginas de conceito

- Crie ou atualize uma página por entidade importante: `[[termo-de-compromisso-ambiental-tca]]`, `[[zoneamento-urbano]]`, etc.

### 6. Etiquetas

- Leia `wiki/etiquetas.md`. Use só as etiquetas dessa página.
- Abra cada página criada com o bloco `tags:`, nesta ordem: `tipo/`, `esfera/`, `situacao/`, `eixo/`, `conceito/`.
- `tipo/`: exatamente uma por página.
- `esfera/`: a esfera da norma (`municipal`, `estadual`, `federal`). Em página de conceito ou de análise, a esfera de cada norma analisada.
- `situacao/`: só em norma ou proposta. Copie do campo "Status".
- `eixo/`: `1-legislacao-atual`, `2-aperfeicoamento` ou os dois.
- `conceito/`: uma por conceito que a página trata. Em página de norma, confirme que o termo está no texto da norma.
- Conceito novo: acrescente a etiqueta em `wiki/etiquetas.md` antes de usar.
- Revise as etiquetas de cada página alterada: mudança de "Status" muda `situacao/`.

### 7. Diagrama

- Gere o bloco Mermaid com a skill `gerador-diagrama-drawio`.
- Se a malha tiver conexões demais para o diagrama estático, gere também o grafo interativo com a skill `gerador-mapa-interativo-d3blocks` — ele é o que fica navegável na página publicada. Não gere bloco de código Cypher na página: é texto inerte, não renderiza nada.

### 8. Índices e logs (append-only)

- `wiki/index.md`: uma linha por página criada, com descrição de uma frase.
- `wiki/log.md`: data, nome da fonte e resumo das mudanças estruturais.
- `wiki/linha-tempo.md`: se houver datas de votação, sanção, revogação ou prazo de cumprimento.
- `wiki/noticias-relacionadas.md`: se a fonte for notícia de imprensa — data, título, link original e classificação temática.

## Rigor de citação

- Toda afirmação factual: `(fonte: nome-do-arquivo.ext)`.
- Fonte de site legislativo: link direto para o Artigo, Parágrafo ou Inciso.
- Divergência entre fontes: registre a contradição explicitamente na página.
- Afirmação sem amparo documental em `raw/`: marque `[verificar]`.

## Valores em reais

- Escreva `R\$ 500`, com barra invertida antes do cifrão.
- Sem a barra, o Obsidian e o site leem o trecho entre dois cifrões como fórmula e desfiguram o texto.
- Dentro de bloco de código (Mermaid incluso) ou de crases, escreva `R$` sem barra.
- Ao terminar, procure cifrão sem barra nas páginas que você criou ou alterou.

## Ao terminar

- Rode `lat check`.
