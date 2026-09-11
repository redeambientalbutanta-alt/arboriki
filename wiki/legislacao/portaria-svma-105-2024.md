# Portaria SVMA 105/2024 — Compensação ambiental e TCA

**Resumo**: Portaria da SVMA que fixa os critérios e procedimentos para autorizar o manejo arbóreo e a intervenção em APP e para calcular a compensação ambiental correspondente, formalizada no Termo de Compromisso Ambiental (TCA). É a norma que hoje determina "quanto" se compensa por árvore cortada em São Paulo.

**Fontes**:
- https://legislacao.prefeitura.sp.gov.br/portaria-secretaria-municipal-do-verde-e-do-meio-ambiente-svma-105-de-14-de-novembro-de-2024/consolidado
- raw/legislacao/Portaria SVMA 105-2024_anexos completos.pdf
- raw/legislacao/Portaria SVMA 116-2024.pdf

**Última atualização**: 2026-09-10

---

## Identificação

- **Número**: Portaria SVMA 105, de 14 de novembro de 2024
- **Autoria**: Rodrigo Pimentel Pinto Ravena, Secretário Municipal do Verde e do Meio Ambiente
- **Status**: em vigor; **alterada pela Portaria SVMA 116/2024**, de 10 de dezembro de 2024 (nova redação do art. 2º, §1º, I; art. 8º, IV, e; art. 54, §3º; art. 95; e inclusão do art. 96)
- **Instância**: SVMA (ato do Secretário)
- **Revoga**: o art. 96, incluído pela Portaria SVMA 116/2024, revoga expressamente a **Portaria SVMA 130/2013**, a **Portaria SVMA 26/2004**, a **Portaria SVMA 36/2008** e a **Publicação SVMA 5/2018**. Ver [[portaria-svma-130-2013]].

## Base normativa invocada

- **Lei 16.050/2014 (Plano Diretor Estratégico), arts. 154 e 155** — instituem o **Termo de Compromisso Ambiental (TCA)** (considerando da portaria). Ver [[termo-de-compromisso-ambiental-tca]].
- **Lei 17.794/2022, art. 8º, II e art. 42, parágrafo único** — exigem manifestação técnica e medidas compensatórias "disciplinadas em regulamento". Ver [[lei-17794-2022]].
- **Lei 16.402/2016 (LPUOS)** — Quota Ambiental (Quadro 3A); o plantio compensatório pode contar para a Quota.
- **Decreto 53.889/2013** — competência da SVMA, Câmara de Compensação Ambiental, conversão da compensação, base de cálculo da muda; é a fonte original da fórmula `CF=(A+B+C+D+E+P+M)×Fr` e da tabela do Fator Multiplicador (art. 5º), que esta portaria apenas atualiza e operacionaliza. Ver [[decreto-53889-2013]].
- **Lei Complementar Federal 140/2011**, **Deliberação Normativa CONSEMA 01/2024**, **Resolução CONAMA 01/1994** — repartição de competência com CETESB.
- **Portaria SVMA 51/2024** — padrão de muda (DAP 3 cm / 5 cm); **Portaria SVMA 39/2024** — entrega de mudas ao viveiro.

`[verificar]`: não confirmamos qual norma fixa hoje o valor monetário atualizado da muda e do tutor (Decreto 53.889/2013, art. 4º, previa reajuste pelo Índice de Edificações em Geral). **O Decreto 64.877/2025 não é essa norma** — trata de preços de serviços genéricos da Prefeitura e não cita SVMA, muda, tutor ou arborização.

## O que propõe — o cálculo da compensação

### Quando incide (art. 1º)

Edificação (inclusive impermeabilização de laje); intervenção em APP; PRAD; remediação de área contaminada; obra de infraestrutura; obra de utilidade/interesse público ou social; licenciamento ambiental; parcelamento do solo; transferência de potencial construtivo sem doação de área.

### Fórmula (Anexo VI)

- **Regime brando** — obra de infraestrutura, utilidade/interesse público ou social, HIS, HMP, PRAD, remediação:
  `CF = F × Fm` (F = nº de espécimes manejados, proporção 1:1).
- **Regime geral** — demais obras:
  `CF = (A + B + C + D + E + P + M) × Fr`, com uma parcela por tipo de vegetação:
  - **A** — vegetação significativa em APP; **B** — vegetação de preservação permanente/significativa fora de APP; **D** — demais espécimes do imóvel; **P** — patrimônio ambiental / imune ao corte:
    `[(It_exótica × T_exótica + Ic_exótica × C_exótica) × 50% + (It_nativa × T_nativa + Ic_nativa × C_nativa)] × Fm`
  - **C** — espécies ameaçadas de extinção: `(It_ex × T_ex + Ic_ex × C_ex) × Fm`
  - **E** — eucalipto, pínus e invasoras: proporção 1:1 (× Fm se em APP / patrimônio / imune)
  - **M** — vegetação morta: proporção 1:1

Onde:

| Símbolo | Significado |
|---|---|
| `Ic` | fator de corte: **média aritmética dos 10% maiores DAP dos exemplares a cortar** → Tabela VI |
| `It` | fator de transplante: média dos 10% maiores DAP dos exemplares a transplantar → Tabela V |
| `Fm` | Fator Multiplicador (valor ecológico) → Anexo VIII |
| `Fr` | fator redutor por mudas maiores que DAP 3 cm → Tabela IX |
| base | 1 muda = espécie nativa, DAP 3,0 cm, com tutor (Decreto 53.889/2013) |

**Tabela VI — corte** (classe `Ic`): DAP 5–10 cm → 3:1; 11–30 → 6:1; 31–60 → 9:1; 61–90 → 15:1; 91–120 → 21:1; 121–150 → 30:1; acima de 150 → **45:1**.

**Tabela V — transplante** (classe `It`): DAP 5–10 → 2:1; 11–30 → 3:1; 31–60 → 6:1; 61–90 → 10:1; 91–120 → 14:1; 121–150 → 18:1; acima de 150 → 20:1.

**Anexo VIII — Fator Multiplicador**: APP + vegetação significativa (art. 4º da Lei 17.794) → **10**; espécie ameaçada de extinção → 5; fragmento florestal em regeneração com copa a suprimir > 1.000 m² → 4; fragmento ≤ 1.000 m² → 3; VPP significativa com DAP predominante 31–60 cm → 3; VPP significativa com DAP 10–30 cm → 2; patrimônio ambiental (Decreto Estadual 30.443/1989) → 2; **demais situações → 1**.

**Tabela IX — fator redutor `Fr`**: muda DAP 3 cm → sem redução; DAP 5 cm → 30% + tutor; DAP 7 cm → 50% + tutor.

**Regras de arredondamento e comparação:** qualquer fração é arredondada para o inteiro superior (art. 39, parágrafo único). Compara-se o cálculo municipal com o estadual (CETESB) e aplica-se o mais restritivo por caso (Tabela VIII).

### Densidade arbórea (arts. 34-38)

A Planta do Projeto de Compensação Ambiental (PCA) deve manter a **densidade arbórea final ≥ densidade inicial** (nº de exemplares no lote + passeio lindeiro + plantios anteriores). Supressões não autorizadas contam na densidade inicial. Exceções ao critério de densidade dependem de parecer da DCRA e consulta à CTCA (art. 35: utilidade pública, ou preservação da "porção mais significativa da vegetação" + área permeável arborizada > 50% do mínimo da Quota Ambiental).

### Cumprimento da compensação (arts. 39-47)

1. Plantio no próprio imóvel (prioritário) ou no entorno lindeiro (art. 16).
2. Excedente à densidade final e ao entorno → decisão da **Câmara Técnica de Compensação Ambiental (CTCA)** (art. 33), preferindo plantio externo na área de influência indireta.
3. Na impossibilidade: **fornecimento de mudas ao viveiro municipal** (excedente × **fator 5,35**, art. 41; mínimo 10% no padrão DAP 5 cm), **depósito no FEMA-SP** (`VCF = CF × V`, art. 42 e Anexo VII), ou **conversão em obras e serviços** (Tabela Oficial de Referência de Preços Públicos, art. 46).

### Órgãos

- **GTMAPP** — Grupo Técnico de Manejo Arbóreo e Intervenção em APP: análise e parecer conclusivo, vistorias, recebimento.
- **CTCA** — Câmara Técnica de Compensação Ambiental: colegiado interno da SVMA (5 cargos: Chefe de Gabinete, Coordenadores de CLA, CGPABI, CFA e CAF), delibera a compensação excedente.
- **DCRA** — Divisão de Compensação e Reparação Ambiental.

## Pontos de atenção ou lacunas

Ver a análise legística completa em [[questionar-criterios-tca]]. Em resumo:

- **Hierarquia normativa frágil** — critérios de conteúdo econômico relevante fixados por portaria, alterável pelo Secretário sem processo legislativo.
- **Remissão ao "art. 4º da Lei 10.365/87" (Anexo VIII, itens E, F) — provavelmente ainda válida, mas por acidente processual, não por atualização.** A revogação desse trecho da Lei 10.365/1987 pela Lei 17.794/2022 foi declarada **inconstitucional** pela ADIN nº 2085569-32.2023.8.26.0000 (decisão ainda não definitiva) — então a citação pode estar tecnicamente correta hoje. Só não está claro se a SVMA manteve a remissão por saber disso ou porque simplesmente **herdou sem revisar** o texto do Decreto 53.889/2013 (2013). O item **G**, que no decreto de 2013 citava o revogado "art. 16" da Lei 10.365/87 ("imune ao corte"), foi **corrigido** nesta portaria para citar o Decreto Estadual 30.443/1989 e o art. 5º da Lei 17.794/2022 — mostrando que a SVMA revisou parte da tabela, mas não documentou por que manteve a citação à Lei 10.365/1987 nos itens E e F. Ver [[decreto-53889-2013]], [[lei-10365-1987]] e [[questionar-criterios-tca]].
- **Multiplicadores sem memória de cálculo pública** — por que 45:1 e não 30:1? O fator 5,35 vem intacto da Portaria 130/2013.
- **Cálculo sobre "10% dos maiores DAP"** — pode subestimar o impacto em lotes heterogêneos.
- **Regime `CF = F × Fm` (1:1)** para obra pública e HIS/HMP — subsídio ambiental implícito, não avaliado.
- **CTCA sem participação externa** e com decisões por "conveniência e oportunidade" (art. 33, §2º).
- **Instabilidade** — Portaria 130/2013 revogada, restaurada e revogada de novo; Portaria 105/2024 já alterada pela 116/2024.

## Atores envolvidos

SVMA (CLA, DCRA, GTMAPP, CTCA); CETESB e CONSEMA (competência estadual); interessados (empreendedores, órgãos públicos); Viveiro Manequinho Lopes; FEMA-SP.

## Normas citadas ou correlatas

Lei 16.050/2014 (arts. 154-155); Lei 16.402/2016; Lei 17.794/2022; Lei Federal 12.651/2012; LC Federal 140/2011; Decretos municipais 53.889/2013, 54.423/2013, 57.565/2016, 60.621/2021; Decreto Estadual 30.443/1989; Portarias SVMA 39/2024, 51/2024, 116/2024; Deliberação Normativa CONSEMA 01/2024; Resolução CONAMA 01/1994 e 237/1997.

Correlatas de objeto distinto (não centrais ao cálculo da compensação): **Portaria SVMA 57/2024** — alvará ambiental para intervenção em Área de Proteção e Recuperação dos Mananciais (APRM); **Portaria SVMA 122/2024** — regularização de empreendimentos em APP descaracterizada.

## Páginas relacionadas

- [[decreto-53889-2013]]
- [[termo-de-compromisso-ambiental-tca]]
- [[questionar-criterios-tca]]
- [[lei-17794-2022]]
- [[portaria-svma-130-2013]]
- [[compensacao-ambiental]]
- [[vegetacao-significativa]]
