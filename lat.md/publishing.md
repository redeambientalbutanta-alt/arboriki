# Publicação do site
<!-- id: publishing -->

A wiki é publicada como site estático em `redeambientalbutanta-alt.github.io/arboriki`, gerado pelo Quartz 5 a partir de `wiki/`. O link não é divulgado nem indexado — uso interno, só leitura.

## Arquitetura

`wiki/` continua sendo a única fonte da verdade. `site/` é uma instalação isolada do [Quartz 5](https://quartz.jzhao.xyz) (projeto Node/TypeScript, sem relação com o `uv`/Python do resto do repositório).

- **`site/content/`** — gerada, nunca commitada (`.gitignore` de `site/` e `.git/info/exclude` da raiz). Espelho de `wiki/`, recriado a cada build pelo script `site/scripts/sync-content.mjs`.
- **`site/public/`** — saída do build (HTML/CSS/JS), gerada, nunca commitada.
- **`site/quartz.config.yaml`** — configuração: template `obsidian` (cobre `[[wiki-links]]` e Mermaid nativamente), `locale: pt-BR`, `baseUrl: redeambientalbutanta-alt.github.io/arboriki`.

> [!warning]
> Nunca rode `git add -A` ou `git add site/content` — essa pasta é um espelho gerado, não conteúdo versionado.

## Por que content/ não pode estar no `.gitignore` de `site/`

O Quartz descobre arquivos com `globby({ gitignore: true })`: ele mesmo respeita qualquer `.gitignore` que encontrar, inclusive o de `site/`.

Se `site/content/` entrasse nesse `.gitignore`, o próprio Quartz se excluiria da varredura e o build encontraria 0 arquivos — foi o que aconteceu na primeira tentativa.

A solução foi registrar `site/content/` em `.git/info/exclude` (arquivo local, nunca commitado, e que o `globby` do Quartz não lê) — git ignora a pasta, o Quartz continua enxergando ela.

## Plugins desativados e por quê

Quatro plugins do template `obsidian` foram desligados em `quartz.config.yaml` por conflitarem com o conteúdo ou o ambiente deste projeto.

- **`@quartz-community/latex`** — a wiki usa `R$` para valores em reais; o parser de LaTeX confundia o cifrão com abertura de modo matemático. Sem necessidade real de fórmulas matemáticas no projeto.
- **`@quartz-community/cname`** — gera um arquivo `CNAME` para domínio próprio. Não se aplica: o site fica no subcaminho padrão `redeambientalbutanta-alt.github.io/arboriki`, sem domínio customizado.
- **`@quartz-themes/core`** — tentava baixar um pacote de tema adicional em tempo de build (`npm install` dinâmico), que falha em ambientes com `--allow-scripts` restrito. A paleta de cores já é definida diretamente em `configuration.theme.colors`.
- **`@quartz-community/obsidian-plugin-excalidraw`** — a wiki não usa desenhos Excalidraw; o plugin emitia um aviso de carregamento sem função.

## Armadilha: bit de execução do CLI do Quartz

`site/quartz/bootstrap-cli.mjs` (o alvo do bin `quartz` do `package.json`) precisa do bit `+x` para `npx quartz ...` funcionar no runner Linux do CI.

Commits feitos no Windows perdem esse bit silenciosamente (`core.filemode=false` faz o git ignorar mudanças de permissão). O segundo deploy desta wiki falhou assim: passou no primeiro push por acaso, e travou com `quartz: Permission denied` no segundo. Corrigido de duas formas — `git update-index --chmod=+x` no arquivo, e um `chmod +x` redundante no workflow, caso o bit se perca de novo em um commit futuro feito no Windows.

## Discrição (link não divulgado, sem indexação)

Duas camadas, nenhuma delas é controle de acesso real (decidido assim porque o público é interno e pequeno):

- `content-index` com `enableSiteMap: false` e `enableRSS: false` — não gera `sitemap.xml` nem feed RSS, os dois arquivos que buscadores e leitores de feed normalmente descobrem sozinhos.
- `scripts/sync-content.mjs` grava um `robots.txt` com `Disallow: /` a cada build.

## Deploy automático

`.github/workflows/deploy.yml` builda e publica no GitHub Pages a cada `git push` na branch `main`.

Fica na raiz do repositório porque GitHub só lê workflows em `.github/workflows/` na raiz, nunca dentro de `site/`. Passos: `npm ci` → `quartz plugin install` → `npm run sync` (copia `wiki/` para `content/`) → `quartz build` → upload do artefato → `actions/deploy-pages`.

O GitHub configura "Settings → Pages → Source: GitHub Actions" sozinho no primeiro deploy bem-sucedido do `actions/deploy-pages` — não precisou de passo manual. URL ativa: `https://redeambientalbutanta-alt.github.io/arboriki/`.

O token do `gh auth login` precisa do escopo `workflow` além do `repo` padrão — sem ele, o push a `.github/workflows/` é recusado. Adicione com `gh auth refresh -h github.com -s workflow` se faltar.

## Comandos locais

Para conferir uma mudança antes de publicar, rode o preview localmente.

```bash
cd site
npm run sync              # copia ../wiki para content/
npx quartz build --serve  # preview em http://localhost:8080
```
