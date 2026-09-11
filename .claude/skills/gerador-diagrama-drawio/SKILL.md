---
name: gerador-diagrama-drawio
description: >-
  Gera o diagrama Mermaid flowchart TD que fecha cada análise legislativa do Eixo 1, com o
  código de cores do projeto (verde = norma vigente, azul tracejado = proposta de aperfeiçoamento,
  vermelho = lacuna ou alerta de fiscalização). Renderiza na wiki e cola no Draw.io. Use ao final
  de uma análise de norma.
---

# Gerador de diagrama Draw.io / Mermaid

Produza o bloco Mermaid da análise. Leia o padrão primeiro: `lat section "diagram-style"`.

## Regras

- `flowchart TD`, hierárquico, de cima para baixo.
- A norma-semente ocupa o topo.
- Classes: `municipal` (verde), `proposta` (azul tracejado), `lacuna` (vermelho); lei federal com `stroke-width:3px`.
- Rótulos de aresta curtos: `altera`, `regula`, `lacuna textual`, `impacta`.

## Saída

Um único bloco ` ```mermaid ` ao final do conteúdo principal da página da wiki. Veja o modelo em `lat.md/diagram-style.md#Exemplo`.
