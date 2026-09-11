---
name: gerador-mapa-interativo-d3blocks
description: >-
  Gera um grafo relacional interativo em HTML autônomo (malha de leis, fluxos de TCA) com a
  biblioteca d3blocks / d3graph, a partir das conexões identificadas na ingestão. Salva em
  wiki/assets/grafos/ e embute na página da lei via iframe. Use quando o usuário pedir um mapa
  navegável da malha regulatória, ou quando uma análise tiver conexões demais para o diagrama
  Mermaid estático.
---

# Gerador de mapa interativo (d3blocks)

Produza um grafo navegável da malha regulatória em HTML autônomo. Complementa o diagrama Mermaid estático da skill `gerador-diagrama-drawio` quando a malha fica densa. Leia o padrão primeiro: `lat section "diagram-style"`.

## 1. Dados de entrada

Monte um `pandas.DataFrame` com exatamente três colunas: `source`, `target` e `weight`.

- `source` e `target`: nomes curtos e estáveis das normas ou conceitos (ex.: `Lei 17.794/2022`).
- `weight = 2.0`: conexão direta ou explícita — citação no texto da norma ou hyperlink.
- `weight = 1.0`: conexão indireta ou semântica — descoberta por embeddings.

## 2. Configuração do d3graph

Instancie o `d3graph` a partir do `D3Blocks` e aplique:

- **Tamanho do nó:** proporcional ao *in-degree centrality* (número de normas que citam o nó).
- **Cor do nó:**
  - Verde: legislação municipal vigente de arborização (ex.: Lei 17.794/2022).
  - Vermelho: nó com lacuna textual ou alerta de fiscalização emitido pela análise.
  - Azul: projeto de lei e norma futura (Eixo 2).
- **Threshold:** habilite o slider de controle para o usuário isolar só as conexões fortes se a malha crescer demais.

## 3. Saída e integração na wiki

1. Exporte com `.d3graph()` para `wiki/assets/grafos/<nome-da-lei>.html`. Use o mesmo nome da página, em minúsculas com hífens.
2. Na página da lei em `wiki/legislacao/`, injete o iframe logo após o bloco Mermaid:

   ```html
   <iframe src="../assets/grafos/<nome-da-lei>.html" width="100%" height="600px" frameborder="0"></iframe>
   ```

## Dependências

`d3blocks` (com `pandas`), já no `pyproject.toml`. Instale o ambiente com `uv sync`.

## Ao terminar

- Rode `lat check`.
