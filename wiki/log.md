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
