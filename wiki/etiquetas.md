---
tags:
  - tipo/apoio
---

# Etiquetas

**Resumo**: Vocabulário das etiquetas (tags) usadas no topo de cada página da wiki, em cinco categorias: tipo, esfera federativa, situação, eixo e conceito. Serve para filtrar páginas no Obsidian e no site.

**Fontes**: `assets/dados/conceitos-por-norma.csv` e `assets/dados/normas-do-corpus.csv` (conceitos e esfera de cada norma); campo "Status" da seção Identificação de cada página de norma (situação).

**Última atualização**: 2026-10-01

---

## Como usar

- **No Obsidian**: abra o painel de tags ou busque `tag:#esfera/estadual`. Combine etiquetas na busca: `tag:#conceito/manejo tag:#tipo/portaria`. Na visão de grafo, crie grupos de cor por etiqueta (por exemplo, uma cor para cada `esfera/`).
- **No site**: clique numa etiqueta, no topo de qualquer página, para listar as páginas que a usam. A lista de todas as etiquetas fica em <https://redeambientalbutanta-alt.github.io/arboriki/tags/>.
- A etiqueta de cima reúne as de baixo: `esfera` lista todas as páginas com `esfera/municipal`, `esfera/estadual` ou `esfera/federal`.

## Categorias

### tipo — o que a página é

Toda página tem exatamente uma.

| Etiqueta | Uso |
|---|---|
| `tipo/lei` | página de lei ou lei complementar |
| `tipo/decreto` | página de decreto |
| `tipo/portaria` | página de portaria, resolução ou outro ato infralegal |
| `tipo/proposta` | projeto de lei, anteprojeto ou minuta |
| `tipo/conceito` | página de conceito de arborização |
| `tipo/analise` | página que cruza várias normas (lentes, ciclo de vida, cálculo, AIL) |
| `tipo/metodo` | Legística e demais métodos de análise |
| `tipo/apoio` | índice, log, linha do tempo, notícias, pendências |

### esfera — nível federativo

| Etiqueta | Uso |
|---|---|
| `esfera/municipal` | norma do Município de São Paulo |
| `esfera/estadual` | norma do Estado de São Paulo |
| `esfera/federal` | norma da União |

Em página de norma: a esfera da norma. Em página de conceito ou de análise: a esfera de cada norma que a página analisa. Páginas de método e de apoio não levam esfera.

Hoje não há página de norma federal na wiki. `esfera/federal` aparece só em [[mapa-de-conceitos]], que analisa três leis federais. As Leis federais 9.605/1998 e 12.651/2012 ainda não foram ingeridas como página.

### situacao — vigência da norma

Só em página de norma ou de proposta. Vem do campo "Status" da seção Identificação.

| Etiqueta | Uso |
|---|---|
| `situacao/vigente` | em vigor, mesmo que alterada |
| `situacao/parcialmente-revogada` | parte dos dispositivos revogada |
| `situacao/revogada` | revogada por inteiro |
| `situacao/sub-judice` | dispositivos afetados por decisão judicial não definitiva; soma-se às anteriores |
| `situacao/em-tramitacao` | proposta em tramitação |
| `situacao/arquivada` | proposta arquivada |

### eixo — eixo do projeto

| Etiqueta | Uso |
|---|---|
| `eixo/1-legislacao-atual` | a página descreve ou audita a norma em vigor |
| `eixo/2-aperfeicoamento` | a página traz proposta de texto ou de mudança |

Uma página pode ter os dois. Páginas de método e de apoio não levam eixo.

### conceito — conceitos de arborização

Uma etiqueta por conceito. A lista reúne os conceitos com página própria, os que têm definição conflitante ou ausente em [[mapa-de-conceitos]] e os que entram no cálculo da compensação. Os demais conceitos da matriz ficam só em `assets/dados/conceitos-por-norma.csv`.

| Etiqueta | Conceito | Página |
|---|---|---|
| `conceito/vegetacao-de-porte-arboreo` | o que conta como árvore (limiar de DAP) | [[arborizacao-urbana]] |
| `conceito/vegetacao-significativa` | vegetação significativa | [[vegetacao-significativa]] |
| `conceito/imune-de-corte` | árvore ou área imune de corte | [[decreto-estadual-30443-1989]] |
| `conceito/patrimonio-ambiental` | patrimônio ambiental | [[mapa-de-conceitos]] |
| `conceito/vegetacao-de-preservacao-permanente` | categoria municipal da Lei 10.365/1987, art. 4º | [[lei-10365-1987]] |
| `conceito/area-de-preservacao-permanente` | APP da lei federal | [[mapa-de-conceitos]] |
| `conceito/area-verde` | área verde | [[mapa-de-conceitos]] |
| `conceito/macico-arboreo` | maciço arbóreo, bosque e fragmento florestal | [[mapa-de-conceitos]] |
| `conceito/mata-atlantica` | Mata Atlântica | [[mapa-de-conceitos]] |
| `conceito/cerrado` | Cerrado | [[mapa-de-conceitos]] |
| `conceito/manejo` | manejo arbóreo | [[manejo-arboreo]] |
| `conceito/supressao` | supressão e corte | [[manejo-arboreo]] |
| `conceito/poda` | poda e poda drástica | [[poda]] |
| `conceito/compensacao-ambiental` | compensação ambiental | [[compensacao-ambiental]] |
| `conceito/tca` | Termo de Compromisso Ambiental | [[termo-de-compromisso-ambiental-tca]] |
| `conceito/densidade-arborea` | densidade arbórea | [[calculo-da-compensacao]] |
| `conceito/area-permeavel` | área permeável | [[lei-16402-2016]] |
| `conceito/quota-ambiental` | Quota Ambiental | [[lei-16402-2016]] |
| `conceito/calcada-verde` | calçada verde | [[calcada-verde]] |

## Regras de aplicação

1. Escreva as etiquetas no bloco `tags:` do topo da página, nesta ordem: tipo, esfera, situação, eixo, conceito.
2. Use só etiquetas desta página. Para criar uma etiqueta, acrescente-a primeiro aqui.
3. Escreva em minúsculas, sem acento, com hífens.
4. Etiquete a página com cada conceito que ela trata. Uma menção de passagem não conta.
5. Em página de norma, use o conceito só se ele também estiver no texto da norma. Confira em `assets/dados/conceitos-por-norma.csv` ou no texto extraído.
6. A etiqueta diz que a página trata do conceito. O papel da norma (define, redefine, usa, conflita) fica em [[mapa-de-conceitos]].
7. Ao mudar o "Status" de uma norma, mude também a etiqueta `situacao/`.

## Limites

- As etiquetas de conceito foram atribuídas por contagem de menções na página, conferida com a matriz de conceitos. Não substituem a leitura.
- Oito normas da matriz não têm página própria na wiki (Leis federais 12.651/2012 e 9.605/1998, LC 140/2011, PDE, Leis 13.293/2002 e 15.442/2011, Decreto 59.671/2020, Portaria SVMA 39/2024). Elas não aparecem nas listas por etiqueta. Por isso `conceito/cerrado` só leva a [[mapa-de-conceitos]].

## Categorias candidatas, ainda não adotadas

- **`orgao/`** — quem edita ou quem decide (SVMA, Subprefeitura, CADES, Câmara, Governo do Estado). Útil para saber a quem cobrar.
- **`achado/`** — tipo de falha apontada na norma: lacuna, termo vago, conflito de definição, remissão errada, falta de prazo, delegação sem critério. Exige reler a seção "Pontos de atenção" de cada página.
- **Papel no conceito** — um terceiro nível, como `conceito/manejo/conflita`. Traz para a etiqueta o que hoje está nas tabelas de [[mapa-de-conceitos]].
- **`tema/`** — compensação, poda, fiscalização, calçadas. Descartada por repetir a categoria `conceito/`.

## Páginas relacionadas

- [[mapa-de-conceitos]]
- [[index]]
- [[verificacoes-pendentes]]
