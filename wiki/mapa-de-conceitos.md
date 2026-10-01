# Mapa de conceitos da legislação

**Resumo**: Quarta lente de análise da malha: em vez de ligar normas entre si, liga cada conceito às normas em que ele nasce, é redefinido, é usado sem definição ou entra em conflito. Cobre 19 normas das três esferas e 48 conceitos de arborização, com a contagem de ocorrências por norma.

**Fontes**:
- raw/legislacao/Decreto Estadual 30.443-1989.pdf; raw/legislacao/Decreto Municipail 53.889-2013.pdf; raw/legislacao/Lei 16402-2016.pdf; raw/legislacao/Portaria SVMA 105-2024_anexos completos.pdf; raw/legislacao/Quadro 1 – Conceitos e definições.pdf
- Texto vigente baixado dos portais oficiais em 2026-10-01: Leis municipais 10.365/1987, 13.293/2002, 15.442/2011, 16.050/2014 e 17.794/2022; Decretos municipais 59.671/2020 e 61.859/2022; Portarias SVMA 130/2013, 39/2024 e 51/2024 (legislacao.prefeitura.sp.gov.br); Decreto Estadual 39.743/1994 (al.sp.gov.br); Lei Federal 12.651/2012, Lei Federal 9.605/1998 e LC 140/2011 (planalto.gov.br)
- Contagens: `assets/dados/conceitos-por-norma.csv`; lista de normas: `assets/dados/normas-do-corpus.csv`

**Última atualização**: 2026-10-01

---

## Como ler

Para cada conceito, a lente registra quatro papéis que uma norma pode ter:

- **Define** — dá o significado do termo ("considera-se", "para os efeitos desta lei").
- **Redefine** — muda o significado, o limiar ou o alcance de um termo já definido.
- **Usa** — emprega o termo sem definir, apoiando-se na definição de outra norma.
- **Conflita** — usa o termo com sentido ou limiar incompatível com a definição vigente.

O método vem da [[legisprudencia]]: coerência *sincrônica* (o mesmo termo com o mesmo sentido ao mesmo tempo) e *diacrônica* (o sentido se mantém quando uma norma sucede a outra).

## Conceitos com conflito ou redefinição

### Vegetação de porte arbóreo (o que conta como árvore)

| Norma | Papel | Texto |
|---|---|---|
| Lei 10.365/1987, art. 2º | define (revogado em 2022) | "espécimes vegetais **lenhosos**, com DAP **superior** a 0,05 m" |
| Lei 17.794/2022, art. 1º, § único | redefine | "espécime ou espécimes vegetais com DAP **superior** a 0,05 m" — sai "lenhosos" |
| Portaria SVMA 51/2024, art. 2º, I | usa | repete a lei |
| Portaria SVMA 105/2024, art. 3º, III | **conflita** | "DAP **igual ou superior** a 0,05 m [...] conforme Lei Municipal 17.794/2022" |
| Proposta de Quadro 1 da LPUOS | redefine | "indivíduo arbóreo existente" só a partir de DAP 20 cm, em três classes |

Conflito: uma árvore com exatamente 5 cm de DAP é árvore para a Portaria 105 e não é para a lei que ela diz seguir. Afeta toda contagem de exemplares em TCA.

### Bem de interesse comum → bem especialmente protegido

Lei 10.365/1987, art. 1º: "bem de interesse comum a todos os munícipes" (revogado). Lei 17.794/2022, art. 1º: "bem especialmente protegido, de interesse de todos os munícipes". A Portaria 51/2024, art. 2º, IV repete a lei. Mudança de 2022 sem conflito atual.

### Vegetação significativa

| Norma | Papel | Texto |
|---|---|---|
| Decreto Estadual 30.443/1989, art. 1º | origem do termo | título do documento-anexo "Vegetação Significativa do Município de São Paulo"; os exemplares nele descritos são "patrimônio ambiental" |
| Lei 16.050/2014 (PDE) | usa, sem definir | "áreas de vegetação significativa de interesse ecológico e paisagístico"; atributo das ZEPAM |
| Lei 16.402/2016, arts. 19 e 71, §7º | usa e **conflita** | atributo das ZEPAM; e "vegetação arbórea significativa **a critério de SVMA**" |
| Lei 17.794/2022, arts. 4º e 5º | define | em APP; ou protege sítio de valor paisagístico, científico ou histórico; ou indicada em plano municipal; ou declarada por ato do Executivo |
| Decreto 61.859/2022, art. 3º, I | usa | competência da SVMA para autorizar o manejo |
| Portaria SVMA 51/2024, art. 5º | **redefine** | acrescenta a hipótese V ("bosque ou maciço heterogêneo" > 10.000 m², em parque ou praça, em região carente de áreas verdes, em encosta > 40%); restringe a hipótese do valor paisagístico às "devidamente registradas em resoluções"; estende o conceito à "área" |
| Portaria SVMA 105/2024, Anexo VIII | usa | Fator Multiplicador 10 (em APP) e 2 (art. 5º) |

Conflitos: (1) a portaria amplia e, num ponto, estreita o conceito fixado em lei; a hipótese V é o texto do art. 4º, §2º, "a" da Lei 10.365/1987, que tratava de outro conceito (vegetação de preservação permanente). (2) A LPUOS deixa "a critério de SVMA" o que a Lei 17.794 define por critérios. A Portaria 51, art. 5º, §1º indica a camada **"Vegetação Significativa 2023"** do GeoSampa como mapeamento oficial — fonte de dados para análise quantitativa. O §2º promete um procedimento de declaração por ato normativo da SVMA. `[verificar]` se foi editado. Ver [[vegetacao-significativa]].

### Imune de corte e patrimônio ambiental

| Norma | Papel | Texto |
|---|---|---|
| Lei Federal 12.651/2012, art. 70, II | base federal vigente | o poder público pode "declarar qualquer árvore imune de corte, por motivo de sua localização, raridade, beleza ou condição de porta-sementes" |
| Decreto Estadual 30.443/1989, arts. 1º a 16 | define por lista | "patrimônio ambiental" (art. 1º) e árvores "imunes de corte" (arts. 2º a 16) |
| Decreto Estadual 39.743/1994 | redefine a competência | corte excepcional decidido pelo Município, salvo reservas e maciços ≥ 1.000 m² |
| Lei 10.365/1987, art. 16 | define a versão municipal (revogado em 2022, não restaurado) | árvore "declarada imune ao corte, mediante ato do Executivo Municipal" |
| Lei 16.050/2014 (PDE), arts. 5º e 7º | **outro sentido** | "patrimônio ambiental" como o conjunto do ambiente natural e urbano |
| Lei 17.794/2022 | não usa | a função passa ao art. 5º, III (vegetação significativa por ato do Executivo) |
| Decreto 53.889/2013 e Portaria 105/2024 | usam | parcela P e Fator Multiplicador 2 |

Conflitos: (1) "patrimônio ambiental" é lista fechada de árvores no decreto estadual e conceito amplo no PDE. (2) A Portaria 105 mantém a categoria "imune de corte", que a lei municipal vigente não tem. (3) A sanção do decreto estadual aponta para o Código Florestal de 1965, mas o poder de declarar árvore imune de corte continua na lei federal de 2012 (art. 70, II). Ver [[decreto-estadual-30443-1989]].

### Vegetação de preservação permanente (municipal) × Área de Preservação Permanente (federal)

| Norma | Papel | Texto |
|---|---|---|
| Lei Federal 12.651/2012, art. 3º, II | define APP | "área protegida, coberta ou não por vegetação nativa", com função ambiental; faixas no art. 4º |
| Lei 10.365/1987, art. 4º | define a categoria municipal (revogado em 2022, **restaurado** pela ADIN) | vegetação de porte arbóreo que, "por sua localização, extensão ou composição florística", protege solo, água e paisagem; inclui bosque > 10.000 m², faixa de **20 m** de cursos d'água e de nascentes |
| Lei 17.794/2022, art. 4º | usa APP | vegetação em APP é significativa |
| Decreto 53.889/2013; Portarias 130/2013 e 105/2024 | usam as duas | parcelas A e B; Fatores Multiplicadores 10, 3 e 2 |

Conflito: dois conceitos de nome quase igual e conteúdo diferente convivem no mesmo cálculo. A categoria municipal é mais larga em tipo (inclui bosques fora de margem) e tem faixa própria de 20 m; a federal tem faixa mínima de 30 m. O art. 4º, §1º da lei municipal ainda cita o Código Florestal de 1965 — e o portal grafa "Lei Federal nº 7.771", quando o número é 4.771. Ver [[lei-10365-1987]].

### Maciço, bosque, fragmento florestal

| Norma | Termo | Critério |
|---|---|---|
| Lei 10.365/1987, art. 4º, §3º (restaurado) | bosque ou floresta heterogênea | 3 ou mais **gêneros**; copas cobrindo mais de 40% do solo |
| Decreto Estadual 39.743/1994 | maciço contínuo de vegetação | área ≥ **1.000 m²**; sem definição do termo |
| Lei 16.050/2014, art. 27, XXIV | maciços arbóreos significativos | sem definição |
| Decreto 53.889/2013, art. 5º, §1º | maciço, bosque, floresta | critério de cálculo, sem definição |
| Portaria SVMA 51/2024, art. 2º, XII | bosque ou maciço heterogêneo | 3 ou mais **espécies**; copas > 40% |
| Portaria SVMA 105/2024, Anexo VIII | fragmento florestal em regeneração | copa a suprimir maior ou menor que **1.000 m²**; remete à Resolução CONAMA 01/1994 |
| Proposta de Quadro 1 da LPUOS | maciço arbóreo | pelo menos **15 árvores** e **500 m²** de copa contínua |

Conflito: quatro limiares (40% de cobertura, 500 m², 1.000 m², 10.000 m²), três termos e a troca de "gêneros" por "espécies" entre a lei e a portaria. O propósito desta wiki inclui os "maciços arbóreos", e não há definição legal única para eles.

### Manejo

| Norma | Papel | Texto |
|---|---|---|
| Lei 17.794/2022, art. 7º | define | "aquele que ocorre desde o plantio e durante todo o seu ciclo vital, visando à conservação e à sanidade" |
| Portaria SVMA 51/2024, art. 2º, V | usa | repete a lei |
| Portaria SVMA 105/2024, art. 3º, V | **conflita** | "aquele que ocorre por corte, transplante ou remoção" |
| Lei Federal 12.651/2012 | outro sentido | "manejo sustentável", "manejo florestal" |

Conflito: duas portarias da mesma Secretaria, do mesmo ano, definem "manejo" de modo oposto — cuidar da árvore (51) e retirar a árvore (105). "Remoção" aparece na 105 ao lado de corte e transplante sem ser definida. Ver [[manejo-arboreo]].

### TCA

Lei 16.050/2014, art. 154: "Termo de **Compromisso** Ambiental" (define). Decreto 53.889/2013 e Portaria 105/2024, art. 49: mesmo nome. Lei 16.402/2016: "Compromisso" no art. 77 e "Termo de **Compensação** Ambiental" no art. 29-A, §3º (conflita). Ver [[termo-de-compromisso-ambiental-tca]].

### Recebimento parcial, provisório e definitivo

Decreto 53.889/2013, art. 8º, §§6º a 8º (define, 4 hipóteses de parcial). Portaria 105/2024, arts. 59 e 60 (redefine: 3 hipóteses; "Termo" e "Certificado" para o mesmo documento). Ver [[ciclo-de-vida-do-tca]].

### Muda (padrão)

Portaria 51/2024, art. 2º, II e III: padrão 3 (DAP 3 cm, altura 2,50 m, pote de 12 L) e padrão 5 (DAP 5 cm, 25 L). Portaria 105/2024, art. 3º, XV: padrão DAP 7 cm (40 L); art. 3º, XIII: muda de reflorestamento com 1,30 m de altura. Proposta de Quadro 1: "indivíduo arbóreo a ser plantado" com DAP 3 cm. O decreto de preços públicos mede a muda pela altura ("até 2,50 m"). Definições espalhadas por três atos, sem conflito direto.

## Conceitos sem definição no corpus

| Conceito | Situação |
|---|---|
| **Cerrado** | aparece só na Lei Federal 12.651/2012, e apenas para a Reserva Legal na Amazônia Legal. **Nenhuma** norma estadual ou municipal do corpus menciona o bioma. A Lei Estadual 13.550/2009 (Cerrado paulista) não é citada por nenhuma norma analisada. `[verificar]` se há remanescentes de cerrado protegidos por outro instrumento no Município |
| **Mata Atlântica** | usada em 8 normas (PDE, LPUOS, Lei 17.794, Portarias 130/2013, 51/2024 e 105/2024, Leis federais 12.651 e 9.605), nunca definida no corpus. A definição está na Lei Federal 11.428/2006, citada só pelo PDE (art. 287, sobre o PMMA). A Portaria 105 exige o mapa do PMMA (art. 8º, IV, "f") e usa os estágios da Resolução CONAMA 01/1994 |
| **Estágio de regeneração** | decide a competência (Estado ou Município) e o Fator Multiplicador, mas a definição está na Resolução CONAMA 01/1994, fora do corpus |
| **Área verde** | três definições parciais e nenhuma geral: "área verde urbana" (Lei 12.651/2012, art. 3º, XX); Sistema de Áreas Protegidas, Áreas Verdes e Espaços Livres (PDE, art. 265); "região carente de áreas verdes" — menos de 15% num raio de 2 km (Lei 10.365/1987, art. 4º, §4º, restaurado). O termo aparece 124 vezes no PDE |
| **Fragmento florestal** | usado no Decreto 53.889 e nas Portarias 130 e 105 para graduar o Fator Multiplicador; sem definição |
| **Utilidade pública e interesse social** | definidos na Lei 12.651/2012, art. 3º, VIII e IX; a Portaria 105, art. 38, usa os termos para o regime 1:1 sem remeter a essa definição |
| **Remoção** | a Portaria 105 distingue "corte, transplante ou remoção"; nenhuma norma define remoção |
| **Poda drástica** | a Lei 17.794/2022, art. 29, remete a regulamento; a definição está só na Portaria 51/2024, art. 2º, X |

## Matriz de ocorrências

Número de vezes que o termo aparece em cada norma (texto vigente ou consolidado). "·" = não aparece. A última coluna conta em quantas normas o conceito está presente.

| Conceito | L12651 | L9605 | LC140 | DE30443 | DE39743 | L10365 | L13293 | L15442 | PDE | LPUOS | L17794 | D53889 | D59671 | D61859 | P130 | P39 | P51 | P105 | Q1 | normas |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| vegetação de porte arbóreo | · | · | · | · | · | 21 | · | · | · | 3 | 44 | · | · | 6 | 2 | · | 34 | 3 | · | 7 |
| exemplar / espécime arbóreo | · | · | · | 9 | 5 | 1 | · | · | · | 3 | 5 | 10 | · | 3 | 29 | 1 | 6 | 44 | 6 | 12 |
| vegetação significativa | · | · | · | 1 | · | · | · | · | 6 | 3 | 2 | · | · | 1 | · | · | 10 | 6 | · | 7 |
| imune de corte | 1 | · | · | 18 | 1 | 2 | · | · | · | · | · | 4 | · | · | 5 | · | · | 2 | · | 7 |
| patrimônio ambiental | · | · | · | 3 | 1 | · | · | · | 7 | 1 | · | 4 | · | · | 5 | · | · | 5 | · | 7 |
| vegetação de preservação permanente | · | · | · | · | · | 3 | · | · | · | · | · | 4 | · | · | 3 | · | · | 5 | · | 4 |
| área de preservação permanente (APP) | 78 | · | · | · | · | · | · | · | 29 | 5 | 1 | 8 | · | · | 35 | · | 2 | 60 | · | 8 |
| área verde | 6 | · | · | · | · | 12 | · | · | 124 | 32 | 1 | · | 1 | · | 22 | · | 3 | 10 | · | 9 |
| maciço arbóreo | · | · | · | · | 1 | · | · | · | 3 | · | · | 1 | · | · | 3 | · | 2 | 3 | 1 | 7 |
| bosque | · | · | · | · | · | 2 | · | · | · | · | · | 1 | · | · | · | · | 3 | · | · | 3 |
| fragmento florestal | · | · | · | · | · | · | · | · | 1 | 1 | · | 2 | · | · | 5 | · | · | 5 | · | 5 |
| Mata Atlântica | 1 | 1 | · | · | · | · | · | · | 13 | 3 | 1 | · | · | · | 1 | · | 1 | 4 | · | 8 |
| Cerrado | 2 | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | 1 |
| vegetação nativa | 62 | · | · | · | · | · | · | · | 5 | 1 | · | · | · | · | 2 | · | · | 3 | · | 5 |
| manejo | 38 | · | 7 | · | 1 | · | · | · | 40 | 9 | 20 | 19 | · | 9 | 55 | 2 | 36 | 91 | · | 12 |
| supressão | 34 | · | 8 | · | · | 15 | · | 2 | 2 | 2 | 25 | · | 2 | 4 | 3 | 3 | 36 | 4 | · | 13 |
| poda drástica | · | · | · | · | · | · | · | · | · | · | 2 | · | · | · | 1 | · | 3 | · | · | 3 |
| compensação ambiental | 3 | · | · | · | · | · | · | · | 4 | 1 | 1 | 17 | · | · | 69 | 1 | 1 | 63 | · | 9 |
| TCA | · | · | · | · | · | · | · | · | 10 | 4 | · | 32 | · | · | 55 | 21 | 10 | 136 | · | 7 |
| TAC | · | · | · | · | · | · | · | · | 16 | 4 | · | · | · | · | · | 1 | 7 | 6 | · | 5 |
| densidade arbórea | · | · | · | · | · | 1 | · | · | · | · | 1 | 1 | · | · | 7 | · | 2 | 18 | · | 6 |
| área permeável | · | · | · | · | · | · | 3 | · | 16 | 22 | · | 1 | 1 | · | 6 | 1 | · | 13 | 2 | 9 |
| Quota Ambiental | · | · | · | · | · | · | · | · | · | 20 | · | · | · | · | · | · | · | 5 | 3 | 3 |
| utilidade pública | 5 | · | · | · | · | · | · | · | 15 | 2 | · | 3 | · | · | 2 | · | · | 4 | · | 6 |
| interesse social | 9 | · | · | · | · | · | · | · | 108 | 25 | · | 7 | · | · | 4 | · | · | 8 | · | 6 |

Siglas: **L12651** Lei Federal 12.651/2012; **L9605** Lei Federal 9.605/1998; **LC140** LC 140/2011; **DE30443** Decreto Est. 30.443/1989; **DE39743** Decreto Est. 39.743/1994; **L10365** Lei 10.365/1987; **L13293** Lei 13.293/2002; **L15442** Lei 15.442/2011; **PDE** Lei 16.050/2014 (PDE); **LPUOS** Lei 16.402/2016 (LPUOS); **L17794** Lei 17.794/2022; **D53889** Decreto 53.889/2013; **D59671** Decreto 59.671/2020; **D61859** Decreto 61.859/2022; **P130** Portaria SVMA 130/2013 (revogada); **P39** Portaria SVMA 39/2024; **P51** Portaria SVMA 51/2024; **P105** Portaria SVMA 105/2024; **Q1** Proposta de Quadro 1 (LPUOS).

A matriz completa, com os 48 conceitos, está em `assets/dados/conceitos-por-norma.csv`. A contagem é por expressão regular sobre o texto extraído; não distingue uso de definição. Os papéis (define, redefine, usa, conflita) das tabelas acima foram atribuídos por leitura.

## O que esta lente mostra

- **O vocabulário não é estável.** Dos conceitos centrais, sete têm definição conflitante ou redefinida por ato inferior: árvore (limiar de DAP), vegetação significativa, imune de corte, preservação permanente, maciço, manejo e TCA.
- **Portaria redefinindo lei.** Em três casos (vegetação significativa, manejo, limiar de DAP) a redefinição vem de portaria, contra o texto da lei. É o mesmo padrão da hierarquia frágil apontado em [[questionar-criterios-tca]].
- **Conceitos-chave definidos fora.** Mata Atlântica e estágio de regeneração mandam no cálculo e na competência, e sua definição não está em nenhuma norma municipal.
- **Cerrado ausente.** O bioma não aparece em nenhuma norma municipal ou estadual do corpus.

## Uso em análise quantitativa

- A contagem por norma (CSV) permite medir concentração: quais normas carregam cada conceito e quais conceitos existem em uma norma só.
- Cada conflito de definição é uma variável de incerteza em bases de TCA: o limiar de DAP muda a contagem de árvores; a definição de maciço muda o enquadramento no Fator Multiplicador; "manejo" muda o que se soma.
- A camada "Vegetação Significativa 2023" do GeoSampa (Portaria 51/2024, art. 5º, §1º) e as listas do Decreto Estadual 30.443/1989 são bases para cruzar com a localização dos TCAs.

## Páginas relacionadas

- [[legisprudencia]]
- [[vegetacao-significativa]]
- [[decreto-estadual-30443-1989]]
- [[lei-10365-1987]]
- [[lei-17794-2022]]
- [[portaria-svma-51-2024]]
- [[portaria-svma-105-2024]]
- [[lei-16402-2016]]
- [[manejo-arboreo]]
- [[ciclo-de-vida-do-tca]]
- [[calculo-da-compensacao]]
- [[questionar-criterios-tca]]
