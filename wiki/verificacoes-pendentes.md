# Verificações pendentes

**Resumo**: Lista do que falta confirmar na wiki — fontes ausentes, textos não ingeridos e dados a checar. Cada item tem um número estável; use esse número para indicar a fonte.

**Última atualização**: 2026-10-01

---

## Como atualizar uma pendência

Escolha um dos dois caminhos.

### Caminho A — você tem o documento (PDF, recorte de Diário Oficial, planilha)

1. Salve o arquivo em `raw/`, na subpasta do tema: `raw/legislacao/`, `raw/judicial/`, `raw/tecnico/` ou `raw/dados/`.
2. Dê ao arquivo um nome descritivo (ex.: `Decreto Municipal 59671-2020 - calcadas.pdf`).
3. Rode `uv run arboriki scan` para confirmar que a fonte foi detectada como `NOVO`.
4. Rode `uv run arboriki extract` para extrair o texto.
5. Peça ao Claude para rodar a skill `ingestao-wiki-legislativo`.

### Caminho B — você tem apenas o link da fonte

Indique a fonte na seção **Fontes indicadas**, logo abaixo, no formato:

```
<número da pendência>: <url ou nome do arquivo>
```

Um número pode ter mais de uma linha (ex.: duas portarias que resolvem o mesmo item). Depois de anotar, avise o Claude — ele roda a skill `pesquisa-legislacao` e ingere a fonte.

### Quando a pendência for resolvida

1. Remova a tag `[verificar]` da página afetada.
2. Acrescente a citação da fonte no formato `(fonte: nome-do-arquivo.ext)` ou o link direto ao artigo.
3. Mova o item, com uma linha de resumo, para a seção **Resolvidas**, no fim deste arquivo.
4. Registre a mudança em [[log]].
5. Rode `lat check`.

---

## Fontes indicadas (aguardando ingestão)

Formato: `<número>: <url ou arquivo>`. Vazio no momento — acrescente uma linha por fonte que você encontrar.

```

```

---

## Bloco 1 — TCA e compensação ambiental

| # | Item | O que falta e por quê | Páginas afetadas |
|---|---|---|---|
| 1 | **Base de dados aberta de TCAs emitidos** | O CLAUDE.md pede o cruzamento com dados de emissão de TCA; nenhum dataset público foi localizado. Buscar no Portal de Dados Abertos da PMSP e no GeoSampa | [[termo-de-compromisso-ambiental-tca]], [[questionar-criterios-tca]] |
| 2 | **Qual valor a SVMA usa como Vm (muda) e Vt (tutor)** | *Parcialmente resolvida.* O Anexo do Decreto 64.877/2025 fixa para 2026 muda com plantio R$ 337,00 e tutor com colocação R$ 229,00. Falta confirmar se a SVMA usa esses itens ou outro cálculo ("Vm calculado pela SVMA", Portaria 105/2024). Fonte ideal: memória de cálculo de um TCA real ou resposta da SVMA/CTCA | [[decreto-64877-2025]], [[compensacao-ambiental]], [[questionar-criterios-tca]] |
| 3 | **Lei 16.402/2016 — Quadros 3A e 3B vigentes (anexos)** | *Texto da lei ingerido.* Faltam os anexos em PDF com os valores de FV para árvore plantada/existente e a pontuação mínima de QA por perímetro. Obs.: o "art. 143" vem da Portaria 105/2024, art. 1º, IX, que cita por engano o art. 143 do PDE (CEPAC); a hipótese de TCA em ZEPAM é o art. 154, IV do PDE | [[lei-16402-2016]], [[portaria-svma-105-2024]] |
| 4 | **Lei 13.430/2002, art. 251 — texto integral** | Instituía o TCA no Plano Diretor de 2002; conteúdo hoje conhecido só indiretamente, via citação de outras normas | [[termo-de-compromisso-ambiental-tca]], [[portaria-svma-130-2013]] |
| 5 | **Portaria SVMA 130/2013 — data exata** | *Quase resolvida.* A Portaria 105/2024, art. 96, a identifica como "de 26 de agosto de 2013"; o endereço no portal usa 12/10/2013 (provável data de republicação). Falta confirmar no Diário Oficial | [[portaria-svma-130-2013]], [[linha-tempo]] |
| 6 | **TCA de emissões de GEE (Lei 16.050/2014, art. 154, III e §2º)** | *Refinada.* A Resolução CADES 284/2024 e a Portaria SVMA 129/2024 exigem inventário e mitigação no licenciamento, mas não citam o art. 154 nem o TCA. Falta saber se algum TCA de emissões já foi firmado | [[termo-de-compromisso-ambiental-tca]], [[questionar-criterios-tca]] |

## Bloco 2 — Norma vigente de manejo

| # | Item | O que falta e por quê | Páginas afetadas |
|---|---|---|---|
| 7 | **Lei Municipal 10.365/1987 — conferência do texto restaurado** | *Texto integral obtido no portal em 2026-10-01*, com as marcas de revogação e de restabelecimento pela ADIN. Falta só conferir se o portal marcou todos os trechos conforme o acórdão (item 15) | [[lei-10365-1987]], [[decreto-53889-2013]], [[questionar-criterios-tca]] |
| 8 | **Decretos 64.883/2025 e 64.986/2026** | Alteram o Decreto 61.859/2022 (arts. 2º-A e 2º-B); texto das alterações não ingerido | [[decreto-61859-2022]] |
| 9 | **Regulamento próprio de poda de cada Subprefeitura** | A Portaria SVMA 51/2024, art. 37, remete a "regulamento próprio" das 32 Subprefeituras para poda em área privada — risco de critério não uniforme | [[poda]], [[portaria-svma-51-2024]] |
| 10 | **Manual Técnico de Poda da PMSP — edição vigente** | Citado pela Lei 17.794/2022 e pelas Portarias SVMA 51/2024 e 105/2024 como referência técnica; edição atual não localizada como documento autônomo | [[poda]], [[manejo-arboreo]] |
| 11 | **Portarias SVMA 3/2023, 29/2023, 127/2024; Portaria SMSUB 155/2024** | Constam nas "Correlações" da Lei 17.794/2022; objeto de cada não confirmado | [[lei-17794-2022]], [[linha-tempo]] |
| 12 | **Portaria Conjunta SVMA/SMJ/SMSU/SMSUB 08/2024 — PMAU** | Regulamenta o Plano Municipal de Arborização Urbana e a fiscalização integrada (CLAUDE.md, "Fontes de partida") | [[arborizacao-urbana]], [[manejo-arboreo]] |
| 13 | **SISGAU — situação atual** | Relação com o "levantamento arbóreo decenal" da Lei 17.794/2022, art. 3º, não confirmada | [[arborizacao-urbana]] |
| 14 | **Normas da seção 6.6 do Manual** | Decreto Federal 6.514/2008; Decretos Municipais 26.535/1988, 28.088/1989, 29.586/1991; Lei Municipal 10.919/1990; MP 2.163-41/2001; Portaria 01/SVMA-DECONT/2014; Portaria 36/08-SVMA — status (vigentes ou revogadas) | [[lei-10365-1987]] |

## Bloco 3 — Decisão judicial

| # | Item | O que falta e por quê | Páginas afetadas |
|---|---|---|---|
| 15 | **ADIN nº 2085569-32.2023.8.26.0000 — acórdão integral** | Temos apenas o comunicado da Procuradoria da Câmara com o dispositivo da decisão; faltam relator, data do julgamento, fundamentação e **andamento de eventual recurso** (a decisão não é definitiva) | [[lei-17794-2022]], [[lei-10365-1987]], [[questionar-criterios-tca]] |

## Bloco 4 — Planos e programas municipais

| # | Item | O que falta e por quê | Páginas afetadas |
|---|---|---|---|
| 16 | **PLANPAVEL, PMSA, PMMA** | Planos que, pela Lei 17.794 art. 5º, II, tornam a vegetação "significativa"; conteúdo e status não ingeridos | [[vegetacao-significativa]] |
| 17 | **Decreto Municipal 58.156/2018 — "Adote uma Praça"** | Programa de cooperação de áreas verdes (CLAUDE.md, "Fontes de partida") | [[compensacao-ambiental]] |
| 18 | **Mapeamento Digital da Cobertura Vegetal (GeoSampa)** | A Portaria 105/2024 exige os mapas de 2017 e 2020; útil como base de dados para auditar a cobertura arbórea | [[questionar-criterios-tca]] |

## Bloco 5 — Legislação estadual e federal (contexto)

| # | Item | O que falta e por quê | Páginas afetadas |
|---|---|---|---|
| 19 | **Documento "Vegetação Significativa do Município de São Paulo" (anexo do Decreto Estadual 30.443/1989)** | *Os dois decretos foram ingeridos.* Falta o documento-anexo, depositado na Secretaria (estadual) do Meio Ambiente e não publicado com o decreto; e a ficha da norma na ALESP (`/norma/{id}`) para confirmar que não houve revogação | [[decreto-estadual-30443-1989]], [[vegetacao-significativa]] |
| 20 | **Consolidação das leis ambientais estaduais (ALESP)** | Estado atual do anteprojeto citado por Rosset (2009); e se há esforço equivalente na Câmara Municipal de SP | [[consolidacao-leis-ambientais-alesp]] |
| 21 | **PLC 488/2017 (Senado)** | Obrigaria o Executivo federal a avaliar o impacto de norma que crie política pública; situação de tramitação | [[avaliacao-de-impacto-legislativo]] |
| 22 | **Lei Federal 12.651/2012 (Código Florestal) — texto integral** | Base da "vegetação significativa" em APP; texto não ingerido | [[vegetacao-significativa]] |

## Bloco 6 — Datas e detalhes menores

| # | Item | O que falta | Páginas afetadas |
|---|---|---|---|
| 23 | Início da vigência da Lei 17.794/2022 | Data exata (vacatio de 90 dias a partir de 27/04/2022 — publicação no DOC) | [[lei-17794-2022]], [[linha-tempo]] |
| 24 | Autoria da Lei 10.365/1987 | Nome do vereador ou do Executivo autor | [[lei-10365-1987]] |
| 25 | Origem e status da "Proposta de alteração do Quadro 1" da LPUOS | Qual projeto de lei; se foi aprovada (e se é a que resultou na Lei 18.081/2024) | [[lei-16402-2016]] |
| 26 | Lei 18.081/2024 — data e número do PL | Revisão da LPUOS; data exata não confirmada | [[lei-16402-2016]], [[linha-tempo]] |
| 27 | Órgão estadual que hoje examina o corte em maciços ≥ 1.000 m² | Sucessor da "Secretaria do Meio Ambiente" do Decreto 39.743/1994 (SEMIL? CETESB?) | [[decreto-estadual-30443-1989]] |
| 28 | Efeito de cada certificado de recebimento do TCA | O que o recebimento parcial, provisório e definitivo liberam (por exemplo, o Certificado de Conclusão da obra); procurar no Código de Obras e nas normas de licenciamento de edificações | [[ciclo-de-vida-do-tca]] |
| 29 | Publicação dos recebimentos de TCA | Se os certificados de recebimento parcial, provisório e definitivo saem no Diário Oficial ou no GeoSampa | [[ciclo-de-vida-do-tca]] |
| 30 | Norma estadual usada na comparação do Anexo VI da Portaria 105/2024 | O Anexo manda comparar com "a legislação estadual" sem nomear a norma | [[calculo-da-compensacao]] |
| 31 | Procedimento de declaração de vegetação significativa | Ato normativo prometido pela Portaria SVMA 51/2024, art. 5º, §2º | [[vegetacao-significativa]] |
| 32 | Camada "Vegetação Significativa 2023" do GeoSampa | Baixar e cruzar com as listas do Decreto Estadual 30.443/1989 e com a localização dos TCAs | [[mapa-de-conceitos]] |
| 33 | Cerrado no Município | O bioma não aparece em nenhuma norma municipal ou estadual do corpus; verificar a Lei Estadual 13.550/2009 e a existência de remanescentes | [[mapa-de-conceitos]] |
| 34 | Normas definidoras fora do corpus | Lei Federal 11.428/2006 (Mata Atlântica) e Resolução CONAMA 01/1994 (estágios de regeneração): ingerir o texto | [[mapa-de-conceitos]] |

---

## Resolvidas

Itens fechados nesta sessão, para referência — não exigem mais ação.

| Item original | O que se descobriu | Fonte usada |
|---|---|---|
| Anexos da Portaria SVMA 105/2024 | Texto completo com Anexos I-IX (documentos, plantas PSA/PSP/PCA, fórmulas, tabelas) | `raw/legislacao/Portaria SVMA 105-2024_anexos completos.pdf` |
| Portaria SVMA 116/2024 | Altera a Portaria 105/2024; inclui o art. 96, que revoga expressamente a Portaria 130/2013, a Portaria 26/2004, a Portaria 36/2008 e a Publicação 5/2018 | `raw/legislacao/Portaria SVMA 116-2024.pdf` |
| Portaria SVMA 51/2024 | Muito além de "padrão de muda": define **poda drástica** e o critério de **urgência/risco de queda** (via NBR 16.246-3:2019) | `legislacao.prefeitura.sp.gov.br/portaria-...-svma-51-de-21-de-junho-de-2024` |
| Portaria SVMA 39/2024 | Procedimentos de solicitação, recebimento e fornecimento de mudas pela Divisão de Arborização Urbana (DAU) | `legislacao.prefeitura.sp.gov.br/portaria-...-svma-39-de-29-de-maio-de-2024` |
| Portarias SVMA 57/2024 e 122/2024 | Objeto confirmado — APRM e regularização em APP, respectivamente; tangenciais ao cálculo de compensação, não centrais | `legislacao.prefeitura.sp.gov.br` |
| Lei 16.050/2014, arts. 154-155 | Texto integral: 4 hipóteses de TCA (supressão, APP, GEE, potencial construtivo em ZEPAM); art. 155 sobre conversão em FEMA | `legislacao.prefeitura.sp.gov.br/lei-16050-de-31-de-julho-de-2014` |
| Decreto Municipal 53.889/2013 | Regulamento original do TCA: fórmula `CF=(A+B+C+D+E+P+M)×Fr`, tabela do Fator Multiplicador, regime 1:1 para obra pública/HIS/HMP — tudo desde 2013 | `raw/legislacao/Decreto Municipail 53.889-2013.pdf` |
| Critério de "risco de queda" | Existe — Portaria SVMA 51/2024, art. 42, remete à NBR ABNT 16.246-3:2019 (norma técnica paga, não decreto) | Portaria SVMA 51/2024 |
| Critério de "poda drástica" | Existe — Portaria SVMA 51/2024, art. 2º, X: corte de 1/3 ou mais da copa, entre outros parâmetros objetivos | Portaria SVMA 51/2024 |
| Decreto Municipal 59.671/2020 | Consolida os critérios de calçada; confirma a faixa livre de 1,20 m e acrescenta a regra dos 50% da largura | `legislacao.prefeitura.sp.gov.br/decreto-59671-de-7-de-agosto-de-2020` |
| Lei Municipal 13.293/2002 | "Calçadas Verdes"; obriga só órgãos públicos, incentiva (não obriga) o particular | `legislacao.prefeitura.sp.gov.br/lei-13293-de-14-de-janeiro-de-2002` |
| Lei Municipal 15.442/2011 | Lei-base de limpeza, fechamento de terrenos e passeios | `legislacao.prefeitura.sp.gov.br/lei-15442-de-09-de-setembro-de-2011` |
| ADIN nº 2085569-32.2023.8.26.0000 | Comunicado oficial da Procuradoria da Câmara: julgamento procedente por maioria, declara trechos da Lei 17.794/2022 inconstitucionais e **restaura parte dos arts. 4º-5º da Lei 10.365/1987**; decisão ainda não transitada em julgado | `saopaulo.sp.leg.br/assessoria_juridica/adin-no-2085569-32-2023-8-26-0000` |
| Decretos Estaduais 30.443/1989 e 39.743/1994 (item 19) | Lista de árvores imunes de corte; documento-anexo chamado "Vegetação Significativa do Município de São Paulo"; desde 1994 o Município decide o corte, salvo reservas e maciços ≥ 1.000 m²; sem registro de revogação | `raw/legislacao/Decreto Estadual 30.443-1989.pdf`; `al.sp.gov.br/repositorio/.../decreto-39743-23.12.1994.html` |
| Lei 16.402/2016 — texto (item 3) | Quota Ambiental; TCA com fator redutor 0,50 (art. 77); TAC não conta (art. 78); 1 árvore/50 m² permeáveis (art. 81, §4º); "Termo de Compensação Ambiental" no art. 29-A | `raw/legislacao/Lei 16402-2016.pdf` |
| Preço público da muda (item 2, parcial) | Anexo do Decreto 64.877/2025: muda com plantio R$ 337,00, tutor R$ 229,00 (2026). **Corrige** a afirmação anterior de que esse decreto não tratava de arborização | `raw/legislacao/doc. 151724539_Anexo_...pdf` |
| Regulamentação de GEE no licenciamento (item 6, parcial) | Resolução CADES 284/2024 e Portaria SVMA 129/2024 — inventário e mitigação, sem TCA | `legislacao.prefeitura.sp.gov.br/leis/...` |

---

## Páginas relacionadas

- [[index]]
- [[log]]
- [[linha-tempo]]
- [[questionar-criterios-tca]]
- [[aplicar-ail-legislacao-arborizacao]]
