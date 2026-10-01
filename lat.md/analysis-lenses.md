# Lentes de análise
<!-- id: analysis-lenses -->

Formas de representar a malha de normas, cada uma para uma pergunta. Testadas a partir da Portaria SVMA 105/2024 em outubro de 2026. Ainda em avaliação: nenhuma substituiu o diagrama padrão de [[diagram-style]].

## As quatro lentes

Cada lente muda o que é o nó e o que é a ligação. Escolha a lente pela pergunta, não pelo desenho.

- **1 — Pirâmide por esfera.** Nó: norma. Posição: tipo (lei, decreto, infralegal) × esfera (federal, estadual, municipal). Seta: da norma superior para a que dela depende. A variante **1a** troca os eixos (esfera nas linhas, tipo nas colunas) e deixa a cadeia correr da esquerda para a direita.
- **2 — Quem cita quem.** Nó: norma. Parte da norma mais específica (a folha). Cada citação é classificada pela função no texto: fundamento, competência, parâmetro de cálculo, procedimento, proteção posterior, ciclo de vida.
- **3 — Rastreabilidade da coerência.** Nó: obrigação (dispositivo que cria dever, custo ou decisão). Trilha lida da Constituição até a obrigação, em três raias (federal, estadual, municipal). Cada trilha passa por seis testes: habilitação, degrau, vigência, termos, atualidade, publicidade.
- **4 — Mapa de conceitos.** Nó: conceito. Para cada norma, o papel: origem, define, redefine, usa, conflita. Página da wiki: `wiki/mapa-de-conceitos.md`.

## Regras aprendidas

Decisões que evitam erros já cometidos nesta análise.

- **Extraia as citações do texto integral, não do resumo.** A expressão regular de [[ingestion-flow#Ingestion Pipeline Specification#Mapeamento recursivo de citações]] não reconhece listas como "leis estaduais nº 13.579/2009, nº 15.790/2015": confira as enumerações à mão.
- **Uma contagem zero pede conferência.** O termo pode estar na norma com outra ordem de palavras ("considera-se de preservação permanente a vegetação").
- **Papel exige leitura.** A contagem diz onde o termo aparece; se a norma define, redefine ou conflita só se sabe lendo o dispositivo.
- **Seta da lei para o decreto.** Quando um decreto regulamenta uma lei, a seta sai da lei.

## Infográficos

Dois infográficos em SVG autônomo, gerados por script e embutidos nas páginas como imagem.

- `wiki/assets/infograficos/ciclo-de-vida-tca.svg` — etapas do TCA, vistorias obrigatórias e o intervalo sem vistoria. Página: `wiki/ciclo-de-vida-do-tca.md`.
- `wiki/assets/infograficos/calculo-compensacao.svg` — cálculo da compensação e exceções. Página: `wiki/calculo-da-compensacao.md`.

Cores fixas e fundo próprio, sem `<marker>` nem `<pattern>`: setas são polígonos, para o arquivo renderizar igual em navegador, Quartz e conversores.

## Dados para análise quantitativa

A wiki publica tabelas para uso por outro projeto, que cruza a legislação com bases de TCA.

- `wiki/assets/dados/conceitos-por-norma.csv` — ocorrências de 48 conceitos em 19 normas.
- `wiki/assets/dados/normas-do-corpus.csv` — sigla, esfera, tipo e ano de cada norma.
- `wiki/ciclo-de-vida-do-tca.md` — dicionário de eventos, regras de consistência e indicadores.
- `wiki/calculo-da-compensacao.md` — variáveis para recalcular a compensação e os pontos em que o texto não dá resultado único.

## Scripts

Os scripts de `scripts/analise/` regeneram os dados e as figuras. Rodam com `uv run python scripts/analise/<nome>.py`, nesta ordem.

1. `baixar_corpus.py` — baixa o texto vigente das normas que não estão em `raw/` para `.arboriki/extracted/portais/`. Confere o corpo da página (o portal devolve HTTP 200 para página inexistente).
2. `conceitos.py` — varre o corpus e grava `.arboriki/extracted/conceitos.json`.
3. `matriz_conceitos.py` — grava os CSV, atualiza a tabela de `wiki/mapa-de-conceitos.md` e gera o JSON compacto da página de comparação.
4. `infograficos.py` — gera os dois SVG.
5. `montar_lentes.py` — monta a página de comparação das lentes (`lentes.src.html` + dados + SVG) em `.arboriki/extracted/lentes.html`, publicada como artifact.
