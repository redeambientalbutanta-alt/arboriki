# Log de operações

**Resumo**: Registro append-only de toda operação estrutural na wiki. Nunca reescreva entradas anteriores; só acrescente ao final.

**Última atualização**: 2026-09-10

---

## 2026-09-10 — bootstrap

- Estrutura `wiki/` criada: `index.md`, `log.md`, `linha-tempo.md`, `noticias-relacionadas.md`, `legislacao/`, `projetos/`.
- Nenhuma fonte de `raw/` ingerida.

## 2026-09-10 — ingestão em lote de `raw/` (7 PDFs)

- Fontes: `raw/legistica/` (6 PDFs de teoria da legística e AIL) + `raw/arborização/Arborização Manual Técnico de SVMA.pdf`.
- Extração prévia via `arboriki extract` (`.arboriki/extracted/`).
- Nenhuma das fontes é legislação; geraram páginas de conceito e de método.
- Páginas de conceito criadas: `legistica`, `legistica-formal`, `legistica-material`, `avaliacao-de-impacto-legislativo`, `principios-da-legistica`, `checklist-legislativo`, `arborizacao-urbana`, `manejo-arboreo`, `poda`, `calcada-verde`, `compensacao-ambiental`.
- `wiki/legislacao/`: `lei-10365-1987` (análise indireta a partir do Manual; revogação pela Lei 17.794/2022 marcada `[verificar]`).
- `wiki/projetos/` (Eixo 2): `aplicar-ail-legislacao-arborizacao` (página-ponte entre eixos, com diagrama Mermaid e Cypher), `consolidacao-leis-ambientais-alesp`.
- `wiki/index.md` reorganizado em seções (legislação, projetos, conceitos de legística, conceitos de arborização).
- `wiki/linha-tempo.md` atualizado com marcos das normas citadas.
- Diagramas Mermaid em `arborizacao-urbana` e `aplicar-ail-legislacao-arborizacao`; blocos Cypher nas mesmas páginas.
- Divergência registrada: o Manual da SVMA (3ª ed.) apoia-se em normas revogadas/substituídas (Lei 10.365/1987; Decretos de calçada 45.904/2005 e 52.903/2012).

## 2026-09-10 — ingestão da lei-semente 17.794/2022 e rastreio de vigência

- Fontes: portais `legislacao.prefeitura.sp.gov.br` (Lei 17.794/2022, Decreto 61.859/2022, Portaria SVMA 130/2013, Portaria SVMA 105/2024) e página oficial do TCA da SVMA. Extração via `curl` + BeautifulSoup.
- Rastreio recursivo (`/consolidado`, `/revogado-por`, `/regulamentacoes`, Correlações): Lei 17.794/2022 revoga arts. 1-16 e 20-25 da Lei 10.365/1987 + 5 outras leis; regulamentada pelo Decreto 61.859/2022 (só arts. 23-27); dispositivos com eficácia suspensa pela ADIN nº 2085569-32.2023.8.26.0000. Portaria 130/2013 revogada em cadeia (69/2016 → 24/2018 → 31/2018 restaura → 105/2024 + 116/2024). TCA hoje: Portaria SVMA 105/2024 (base: arts. 154-155 da Lei 16.050/2014, PDE).
- Páginas de legislação criadas: `lei-17794-2022` (formato de análise completo), `decreto-61859-2022`, `portaria-svma-105-2024`, `portaria-svma-130-2013`.
- Conceitos criados: `termo-de-compromisso-ambiental-tca`, `vegetacao-significativa`.
- Eixo 2: `questionar-criterios-tca` — AIL ex-post com 9 achados e 8 propostas; diagrama Mermaid + Cypher.
- Skill criada: `pesquisa-legislacao` (navegação dos 3 portais oficiais); `lat.md/ingestion-flow.md` ganhou a seção "Rastreio de vigência nos portais".
- `README.md` criado (visão geral + uso da CLI).
- Páginas atualizadas para a norma vigente: `arborizacao-urbana` (tabela do que mudou), `manejo-arboreo`, `poda`, `calcada-verde`, `compensacao-ambiental`, `lei-10365-1987`, `aplicar-ail-legislacao-arborizacao`, `index`, `linha-tempo`.
- Divergência-chave registrada: o Anexo VIII da Portaria SVMA 105/2024 (2024) cita o art. 4º da Lei 10.365/1987, revogado em 2022.

## 2026-09-10 — página de verificações pendentes

- Criada [[verificacoes-pendentes]]: consolida os 35 itens `[verificar]` da wiki em 7 blocos, com "o que falta", "onde buscar" e as páginas afetadas.
- Inclui o procedimento de atualização: Caminho A (documento em `raw/<tema>/` → `arboriki extract` → skill) e Caminho B (link → skill `pesquisa-legislacao`).
- Ligada em `wiki/index.md` (Páginas de apoio).
- Extraídos (pendentes de análise) os 2 PDFs de legística adicionados a `raw/legistica/` (diretrizes de AIL da Câmara dos Deputados; TD-70 do Senado).

## 2026-09-10 — ingestão dos documentos do usuário + descoberta da ADIN + redesenho de verificações pendentes

- **`raw/legislacao/` criada pelo usuário** com 4 PDFs (imagens, exigiram OCR): Decreto Municipal 53.889/2013, Portaria SVMA 105/2024 (anexos completos) e Portaria SVMA 116/2024 (original + consolidado). Extraídos com `TESSERACT_CMD` apontado para a instalação existente (não estava no PATH do shell); `.env` criado com essa variável.
- **Aprendido o padrão de URL** do portal da Prefeitura a partir das edições do usuário em `verificacoes-pendentes.md`: `{tipo}-{numero}-de-{dia}-de-{mês}-de-{ano}`. Usado para construir e confirmar por `curl` 9 URLs (Portarias SVMA 51, 39, 57, 122/2024; Decreto 59.671/2020; Leis 13.293/2002, 15.442/2011, 16.050/2014, Decreto 64.877/2025). Documentado na skill `pesquisa-legislacao` e em `lat.md/ingestion-flow.md`.
- **Página nova**: `decreto-53889-2013` — regulamento original do TCA; origem da fórmula `CF=(A+B+C+D+E+P+M)×Fr` e da tabela do Fator Multiplicador, ainda em vigor.
- **Página nova**: `portaria-svma-51-2024` — corrige achado anterior: "risco de queda" e "poda drástica" **têm** critério objetivo (não são lacuna), mas definidos por portaria onde a Lei 17.794/2022 parecia pedir decreto.
- **Achado maior — ADIN nº 2085569-32.2023.8.26.0000**: julgamento procedente por maioria (TJSP, Órgão Especial, decisão não transitada em julgado) declara inconstitucionais trechos da Lei 17.794/2022 **e a revogação de partes dos arts. 4º-5º da Lei 10.365/1987** — restaurando-os. Isso reverte a leitura anterior de que a citação ao "art. 4º da Lei 10.365/87" no Decreto 53.889/2013 e na Portaria 105/2024 seria um erro: pode estar correta. Só a citação ao art. 16 (não alcançado pela ADIN) segue sendo remissão a norma morta. `questionar-criterios-tca`, `lei-17794-2022`, `lei-10365-1987`, `decreto-53889-2013` e `portaria-svma-105-2024` corrigidos.
- **Correção**: Decreto 64.877/2025 checado e **descartado** como fonte de preços da compensação (é decreto genérico de preços públicos, sem menção a SVMA/arborização) — pendência de "valor atual da muda" recolocada em aberto com essa ressalva.
- Bloco 3 (calçadas) resolvido: Decreto 59.671/2020, Lei 13.293/2002 e Lei 15.442/2011 ingeridos; `calcada-verde` reescrita.
- **`wiki/verificacoes-pendentes.md` redesenhada** a pedido do usuário: tabelas sem URL embutida; nova seção "Fontes indicadas" no formato `número: fonte`; itens resolvidos movidos para uma seção "Resolvidas"; pendências renumeradas de 1 a 24 (de 35, refletindo o progresso).
- `wiki/linha-tempo.md` reescrita com as datas exatas confirmadas nesta sessão.

## 2026-09-23 — ingestão de 5 fontes novas em `raw/`

- Fontes extraídas com `arboriki extract` (OCR onde necessário): `raw/legislacao/Decreto Estadual 30.443-1989.pdf`, `Lei 16402-2016.pdf`, `Quadro 1 – Conceitos e definições.pdf`, `doc. 151724539_Anexo_Decreto_de_Precos_Publicos_2026_com_linhas_ajustadas.pdf` e `raw/legistica/ESTUDOS_EM_LEGISTICA.pdf`.
- Rastreio complementar nos portais: Decreto Estadual 39.743/1994 (ALESP), Decreto 64.877/2025, Resolução CADES 284/2024 e Portaria SVMA 129/2024 (Prefeitura).
- **Páginas novas**: `decreto-estadual-30443-1989` (lista de árvores imunes de corte; origem do termo "vegetação significativa"), `lei-16402-2016` (LPUOS: Quota Ambiental, TCA com redutor 0,50, proposta de Quadro 1 com "maciço arbóreo"), `decreto-64877-2025` (preços públicos 2026), `legisprudencia` (conceito, a partir de *Estudos em Legística*, 2019).
- **Correção**: o registro de 2026-09-10 que descartou o Decreto 64.877/2025 estava errado — a leitura cobriu só o corpo do decreto; o **Anexo** traz muda com plantio R$ 337,00 e tutor R$ 229,00. Corrigidos `compensacao-ambiental`, `portaria-svma-105-2024`, `questionar-criterios-tca`, `linha-tempo`, `verificacoes-pendentes`.
- **Correção**: `arborizacao-urbana` dizia que a Lei 17.794/2022 "substituiu" a categoria de árvore imune ao corte; lei municipal não revoga decreto estadual — o Decreto 30.443/1989 segue vigente e suas árvores se enquadram no art. 5º, III da lei municipal.
- **Correção**: a pendência #3 associava o "art. 143" da Lei 16.402/2016 à ZEPAM; o art. 143 trata de interdição.
- `questionar-criterios-tca`: novos achados 4-A (valor da muda sem fonte pública) e 4-B (TCA vale metade na Quota Ambiental); 6-A atualizado (Resolução CADES 284/2024 exige mitigação, mas sem TCA); propostas 10 (publicar Vm e Vt) e 11 (uniformizar o nome do TCA); diagrama e grafo interativo regerados.
- Atualizados: `vegetacao-significativa`, `termo-de-compromisso-ambiental-tca`, `index`, `linha-tempo`, `verificacoes-pendentes` (itens 2, 3, 6, 19 revistos; 25-27 novos).
- `lat.md/diagram-style.md`: nova classe `estadual` (laranja) para normas estaduais.
- Skill `pesquisa-legislacao`: o portal da Prefeitura devolve HTTP 200 com corpo "404 - Página não encontrada" — checar o corpo, não só o código; padrão de URL do repositório da ALESP; ler sempre o Anexo.

## 2026-10-01 — lentes de análise, mapa de conceitos e ciclo de vida do TCA

- **Corpus ampliado**: texto vigente de 14 normas baixado dos portais oficiais para `.arboriki/extracted/portais/` (Leis 10.365/1987, 13.293/2002, 15.442/2011, 16.050/2014, 17.794/2022; Decretos 59.671/2020, 61.859/2022; Portarias SVMA 130/2013, 39/2024, 51/2024; Decreto Estadual 39.743/1994; Leis federais 12.651/2012, 9.605/1998; LC 140/2011).
- **Páginas novas**: `mapa-de-conceitos` (48 conceitos em 19 normas; onde cada um é definido, redefinido ou conflita), `ciclo-de-vida-do-tca` (etapas, intervalo sem vistoria, ambiguidade do "recebimento parcial", dicionário de eventos e indicadores), `calculo-da-compensacao` (cálculo em seis passos, exceções, pontos sem resultado único).
- **Infográficos**: `assets/infograficos/ciclo-de-vida-tca.svg` e `assets/infograficos/calculo-compensacao.svg`. **Dados**: `assets/dados/conceitos-por-norma.csv` e `assets/dados/normas-do-corpus.csv`.
- **Achados**: (1) entre a publicação do TCA e o informe de plantio não há vistoria obrigatória da SVMA (Portaria 105/2024, arts. 21 e 57); (2) "recebimento parcial" tem quatro hipóteses no Decreto 53.889/2013 e três na Portaria 105; (3) a Portaria 105 define "manejo" ao contrário da Lei 17.794/2022 e muda o limiar de DAP de "superior" para "igual ou superior" a 5 cm; (4) a Portaria 51/2024 acrescenta uma hipótese à "vegetação significativa" da lei; (5) Cerrado não aparece em nenhuma norma estadual ou municipal do corpus.
- **Erros de citação da Portaria 105/2024 registrados**: art. 143 do PDE (deveria ser arts. 122-133 e 154, IV); Resolução CONAMA 237 datada de 1987 (é de 1997); "CONAMA 01/1991"; Anexo VI remete ao Anexo VII em vez do VIII.
- **Correção**: a lista de normas citadas pela Portaria 105 estava incompleta (faltavam 5 leis estaduais de mananciais, Lei Orgânica, IN IBAMA, Resolução SMA 36/2018, Decisão CETESB 167/2015, Portaria SVMA 57/2024); a nota sobre o "art. 143" em `lei-16402-2016` foi refeita.
- **Pendências**: item 7 (texto da Lei 10.365/1987) quase resolvido; itens 28 a 34 novos.
- Logo da Rede Ambiental Butantã na página inicial (`assets/imagens/LogoRAB2026.svg`, cópia de `raw/imagens/`).
- Scripts de análise versionados em `scripts/analise/`; lentes documentadas em `lat.md/analysis-lenses.md`.
