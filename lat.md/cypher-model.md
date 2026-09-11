# Modelo de Grafo Neo4j
<!-- id: cypher-model -->

Ontologia que traduz os relacionamentos jurídicos da wiki — explícitos e semânticos — em nós e arestas do Neo4j. A skill `formatador-cypher-neo4j` emite blocos `MERGE` a partir deste modelo; `src/` (futuro `sync`) os aplica no banco.

## Labels

Entidades da wiki mapeadas para rótulos estáveis.

- `(:Norma {id, tipo, numero, ano, esfera, ementa})` — lei, decreto, portaria ou resolução. `id` no formato `ESFERA_TIPO_NUMERO_ANO`, ex.: `MUN_LEI_17794_2022`. `esfera` é `"Municipal"`, `"Estadual"` ou `"Federal"`.
- `(:AtoRegulatorio {id, tipo, numero, ano})` — TCA e demais atos administrativos individuais.
- `(:Orgao {nome})` — SVMA, subprefeituras, CMSP.
- `(:Conceito {termo})` — "Zoneamento Urbano", "Compensação Ambiental", "Maciço Arbóreo".

## Arestas

Conexões com semântica jurídica explícita.

- `(:Norma)-[:ALTERA]->(:Norma)`
- `(:Norma)-[:REVOGA]->(:Norma)`
- `(:Norma)-[:REGULAMENTA]->(:Norma)`
- `(:AtoRegulatorio)-[:VINCULADO_A]->(:Norma)`
- `(:Norma)-[:VAGO_EM]->(:Conceito)` — termo vago ou ambíguo no texto da norma
- `(:Norma)-[:IMPACTA_INDIRETAMENTE]->(:Conceito)`
- `(:Orgao)-[:FISCALIZA]->(:Conceito)`

## Formato de saída

Sempre `MERGE`, nunca `CREATE`, para não duplicar nós. Um `MERGE` por nó, depois um `MERGE` por aresta.

```cypher
MERGE (n1:Norma {id: "MUN_LEI_17794_2022", tipo: "Lei", numero: "17794", ano: "2022", esfera: "Municipal"})
MERGE (n2:Norma {id: "MUN_DECRETO_61859_2022", tipo: "Decreto", numero: "61859", ano: "2022", esfera: "Municipal"})
MERGE (n2)-[:REGULAMENTA]->(n1);
```
