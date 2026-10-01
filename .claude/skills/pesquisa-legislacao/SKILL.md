---
name: pesquisa-legislacao
description: >-
  Pesquisa e extrai normas dos três portais legislativos oficiais que interessam ao projeto —
  Prefeitura de São Paulo (legislacao.prefeitura.sp.gov.br), ALESP (al.sp.gov.br) e federal
  (planalto.gov.br/ccivil_03). Sabe navegar TEXTO CONSOLIDADO/COMPILADO, Revogações, Correlações
  e Regulamentações para rastrear o que aconteceu com cada norma. Use quando o usuário fornecer
  uma URL de portal legislativo, citar uma lei/decreto/portaria a rastrear, ou pedir o texto
  vigente de uma norma.
---

# Pesquisa em portais de legislação

Objetivo: obter o **texto vigente** de uma norma e rastrear recursivamente o que a alterou, revogou
ou regulamentou. Respeite `max_depth = 3` e mantenha um registro de `visited_nodes` (ver
`lat section "ingestion-flow"`).

Ferramentas: `curl` via Bash para baixar o HTML; `pymupdf`/`BeautifulSoup` (no venv) para extrair
texto; `WebFetch` como alternativa quando o `curl` falhar. Textos de lei são de domínio público
(Lei 9.610/1998, art. 8º, I) — transcreva na íntegra quando necessário.

## 1. Prefeitura de São Paulo — `legislacao.prefeitura.sp.gov.br`

O portal mais estruturado. Codificação UTF-8. URLs por slug.

- **Página principal:** `/{slug}` (ex.: `/lei-17794-de-27-de-abril-de-2022`).
- **Texto vigente:** `/{slug}/consolidado` — sempre prefira este. A página principal traz o texto original.
- **Marcadores:** "Texto Consolidado" e "Texto Compilado" indicam que a norma sofreu alterações.
  No corpo, dispositivos alterados trazem `(Redação dada pela ...)`, `(Incluído pela ...)`,
  `(Revogado pela ...)`, `(eficácia suspensa pela ADIN nº ...)`.
- **Rastrear o destino da norma:**
  - `/{slug}/revogado-por` — o que a revogou (siga cada entrada).
  - `/{slug}/regulamentacoes` — decretos/portarias que a regulamentam, com o intervalo de artigos.
  - Âncoras `#historico` (Alterações) e `#correlacionadas` (Correlações) na própria página.
- **Anexos:** link "Anexos" na página principal (tabelas de cálculo, fatores, etc.).
- **Passo a passo:**
  1. Baixe `/{slug}/consolidado`. Extraia o texto do maior `<div>` de conteúdo.
  2. Registre ementa, autoria, data, e todas as marcações de alteração/suspensão.
  3. Baixe `/{slug}/revogado-por` e `/{slug}/regulamentacoes`. Enfileire cada norma citada.
  4. Varra o texto com o RegEx de menções (ver `ingestion-flow`) e enfileire as normas citadas.
  5. Repita para cada norma da fila até `max_depth = 3`.
- **Busca:** `https://legislacao.prefeitura.sp.gov.br/leis/{slug}` também resolve; a busca livre
  fica em `/` (campo de texto). Quando não souber o slug, use `WebSearch` com
  `allowed_domains: ["legislacao.prefeitura.sp.gov.br"]`.
- **Construa o slug diretamente quando souber o número e a data** — mais rápido que buscar:
  `{tipo}-{numero}-de-{dia}-de-{mes-por-extenso}-de-{ano}` (tipo no singular: `lei`, `decreto`,
  `portaria-secretaria-municipal-do-verde-e-do-meio-ambiente-svma`; número sem pontuação; mês
  por extenso em minúsculas). O dia nem sempre é zero-padded (`decreto-59671-de-7-de-agosto-de-2020`
  vs. `lei-15442-de-09-de-setembro-de-2011`) — teste sem zero primeiro; teste `/leis/{slug}` se
  `/{slug}` falhar.
- **O código HTTP não confirma nada.** O portal devolve **HTTP 200 com o corpo "404 - Página não
  encontrada"** para slug inexistente. Confirme sempre pelo corpo: a página certa contém o número da
  norma; a errada contém "Página não encontrada".
- **Resoluções do CADES** usam o tipo `resolucao-secretaria-municipal-do-verde-e-do-meio-ambiente-svma-cades`
  e a data de **publicação**, não a de assinatura (ex.: Resolução CADES 284, assinada em 11/12/2024:
  `/leis/resolucao-secretaria-municipal-do-verde-e-do-meio-ambiente-svma-cades-284-de-20-de-dezembro-de-2024`).
  Se o slug construído falhar, use `WebSearch` com `allowed_domains: ["legislacao.prefeitura.sp.gov.br"]`.
- **Leia o Anexo.** Decretos de preços, tabelas e parâmetros costumam ter o corpo curto ("ficam aprovados
  os preços constantes do Anexo") e todo o conteúdo no Anexo. Ler só o corpo leva a conclusões erradas
  (ex.: o Decreto 64.877/2025 parece não tratar de arborização; o Anexo tem o preço da muda).

## 2. ALESP (estadual) — `al.sp.gov.br`

Codificação ISO-8859-1 — **decodifique de ISO-8859-1 para UTF-8**. Página com muito JavaScript.

- **Pesquisa:** `https://www.al.sp.gov.br/norma/pesquisa` (formulário). A busca real é por
  parâmetros; a ficha de cada norma fica em `https://www.al.sp.gov.br/norma/{id}`.
- **Repositório histórico (texto da norma, HTML estático):**
  `https://www.al.sp.gov.br/repositorio/legislacao/{tipo}/{ano}/{tipo}-{numero}-{dd.mm.aaaa}.html`,
  com número sem ponto (ex.: `/repositorio/legislacao/decreto/1989/decreto-30443-20.09.1989.html`;
  `/repositorio/legislacao/decreto/1994/decreto-39743-23.12.1994.html`). A página traz o texto original
  com retificações, mas **não** mostra alterações posteriores — procure a norma alteradora pelo título
  ("Dá nova redação ao artigo X do Decreto n.º Y").
- Se a página não renderizar por `curl`, tente `WebFetch`; se ainda faltar conteúdo, registre
  `[verificar]` e peça a URL direta da norma ao usuário.
- `[verificar]` — a navegação de "revogações/correlações" da ALESP ainda não foi mapeada neste projeto.

## 3. Federal — `planalto.gov.br/ccivil_03`

HTML estático antigo (FrontPage), codificação **ISO-8859-1 — decodifique para UTF-8**.
`legislacao.presidencia.gov.br` tem proteção anti-robô; use o Planalto direto.

- **Leis:** `https://www.planalto.gov.br/ccivil_03/leis/l{numero}.htm` (ex.: `l9605.htm`);
  leis recentes: `/leis/_ato{ano}-{ano}/{ano}/lei/l{numero}.htm`.
- **Decretos:** `/decreto/d{numero}.htm` ou `/_ato.../decreto/d{numero}.htm`.
- **Revogação:** o Planalto risca o texto revogado (`<strike>`) e adiciona nota
  "(Revogado pela Lei nº ...)" / "(Vide ...)" ao lado do dispositivo e no cabeçalho.
- Sempre confira a linha "Texto compilado" / "Vide" no topo da página.

## Saída

Para cada norma rastreada, entregue ao fluxo de ingestão: ementa, número, tipo, esfera, ano,
status (vigente / revogada / eficácia suspensa), lista de normas que a alteram/revogam/regulamentam
com a URL de cada uma, e o texto vigente dos artigos relevantes ao tema. Marque `[verificar]`
tudo o que não conseguir confirmar no portal.
