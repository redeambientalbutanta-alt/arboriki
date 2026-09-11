---
name: formatador-cypher-neo4j
description: >-
  Converte os relacionamentos jurídicos identificados numa análise legística (explícitos e
  semânticos) em instruções Cypher MERGE prontas para o Neo4j, seguindo a ontologia do projeto.
  Use ao final de uma análise de norma, ou quando o usuário pedir o bloco Cypher de uma página da wiki.
---

# Formatador Cypher para Neo4j

Traduza os nós e as arestas da análise para Cypher estável. Leia a ontologia primeiro: `lat section "cypher-model"`.

## Regras

- Sempre `MERGE`, nunca `CREATE`.
- Um `MERGE` por nó; depois um `MERGE` por aresta.
- `id` de norma no formato `ESFERA_TIPO_NUMERO_ANO`, ex.: `MUN_LEI_17794_2022`.
- Propriedade de esfera: `esfera`, com valor `"Municipal"`, `"Estadual"` ou `"Federal"`.
- Termo vago ou ambíguo no texto da norma: aresta `[:VAGO_EM]` para o `(:Conceito)`.
- Norma que revoga outra: aresta `[:REVOGA]`.

## Saída

Um único bloco ` ```cypher ` ao final da página da wiki. Veja o exemplo em `lat.md/cypher-model.md#Formato de saída`.
