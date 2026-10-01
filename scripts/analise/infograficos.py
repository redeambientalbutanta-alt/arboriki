# @lat: [[analysis-lenses#Lentes de análise#Scripts]]
"""Gera os dois infográficos do TCA como SVG autônomo em wiki/assets/infograficos/."""
import pathlib, re, textwrap
from xml.sax.saxutils import escape as esc

OUT = pathlib.Path(__file__).resolve().parents[2] / "wiki" / "assets" / "infograficos"
OUT.mkdir(parents=True, exist_ok=True)

INK, MUTED, RULE, PAPER, PANEL = "#18211d", "#55635c", "#cfd8d2", "#f6f8f5", "#ffffff"
GREEN, GREEN_BG = "#2e8a4d", "#e3f2e8"
BLUE, BLUE_BG = "#2b62a8", "#e4edf8"
RED, RED_BG = "#c0392b", "#fbe6e3"
AMBER, AMBER_BG = "#a15c07", "#fdf0da"
FONT = "'IBM Plex Sans','Segoe UI',Arial,Helvetica,sans-serif"


class Svg:
    def __init__(self, w, h, title):
        self.w, self.h, self.p = w, h, []
        self.p.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" font-family="{FONT}" role="img" aria-label="{esc(title)}">')
        self.p.append('<defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#55635c"/></marker>'
                      '<marker id="ahr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#c0392b"/></marker>'
                      '<pattern id="hatch" width="10" height="10" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="10" height="10" fill="#fbe6e3"/><line x1="0" y1="0" x2="0" y2="10" stroke="#eab3ab" stroke-width="3"/></pattern></defs>')
        self.p.append(f'<rect width="{w}" height="{h}" fill="{PAPER}"/>')

    def rect(self, x, y, w, h, fill=PANEL, stroke=RULE, sw=1.2, rx=6, dash=None):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.p.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>')

    def text(self, x, y, s, size=12, fill=INK, weight=400, anchor="start", italic=False):
        st = ' font-style="italic"' if italic else ""
        self.p.append(f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" font-weight="{weight}" text-anchor="{anchor}"{st}>{esc(s)}</text>')

    def para(self, x, y, s, width_px, size=12, fill=INK, weight=400, lh=None):
        """Texto com quebra automática. Retorna o y da linha seguinte."""
        lh = lh or round(size * 1.38)
        chars = max(8, int(width_px / (size * 0.5)))
        for line in textwrap.wrap(s, chars) or [""]:
            self.text(x, y, line, size, fill, weight)
            y += lh
        return y

    def card(self, x, y, w, title, lines, fill=PANEL, stroke=RULE, tcolor=INK, ref=None, size=11.5, sw=1.4, h=None):
        """Caixa com título, corpo com quebra e referência legal. Retorna o y inferior."""
        chars = max(8, int((w - 20) / (size * 0.5)))
        n = 0
        for ln in lines:
            n += len(textwrap.wrap(ln, chars) or [""])
        tl = textwrap.wrap(title, max(8, int((w - 20) / (13 * 0.56))))
        hh = 14 + len(tl) * 17 + n * round(size * 1.38) + (18 if ref else 6) + 6
        hh = h or hh
        self.rect(x, y, w, hh, fill, stroke, sw)
        yy = y + 22
        for t in tl:
            self.text(x + 10, yy, t, 13, tcolor, 600)
            yy += 17
        yy += 2
        for ln in lines:
            yy = self.para(x + 10, yy, ln, w - 20, size, INK)
        if ref:
            self.text(x + 10, y + hh - 9, ref, 10.5, MUTED, 500)
        return y + hh

    def arrow(self, x1, y1, x2, y2, color="#55635c", sw=1.6, dash=None, red=False):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        c = RED if red else color
        self.p.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{c}" stroke-width="{sw}"{d}/>')
        self.head(x2, y2, x1, y1, c)

    def path(self, d, color="#55635c", sw=1.6, dash=None, red=False):
        ds = f' stroke-dasharray="{dash}"' if dash else ""
        c = RED if red else color
        self.p.append(f'<path d="{d}" fill="none" stroke="{c}" stroke-width="{sw}"{ds}/>')
        n = [float(v) for v in re.findall(r"-?\d+\.?\d*", d)]
        self.head(n[-2], n[-1], n[-4], n[-3], c)

    def head(self, x2, y2, x1, y1, color):
        import math
        a = math.atan2(y2 - y1, x2 - x1); L, Wd = 9, 4
        bx, by = x2 - L * math.cos(a), y2 - L * math.sin(a)
        pts = f"{x2:.1f},{y2:.1f} {bx - Wd * math.sin(a):.1f},{by + Wd * math.cos(a):.1f} {bx + Wd * math.sin(a):.1f},{by - Wd * math.cos(a):.1f}"
        self.p.append(f'<polygon points="{pts}" fill="{color}"/>')

    def save(self, name, h=None):
        if h:
            self.p[0] = self.p[0].replace(f'viewBox="0 0 {self.w} {self.h}"', f'viewBox="0 0 {self.w} {h}"').replace(f'height="{self.h}"', f'height="{h}"')
            self.p[2] = f'<rect width="{self.w}" height="{h}" fill="{PAPER}"/>'
        self.p.append("</svg>")
        (OUT / name).write_text("\n".join(self.p), encoding="utf-8")
        print("gravado", name)


# ======================================================================
# 1. CICLO DE VIDA DO TCA
# ======================================================================
def ciclo():
    W, H = 1500, 1060
    s = Svg(W, H, "Ciclo de vida do Termo de Compromisso Ambiental em São Paulo, com as três vistorias obrigatórias e o intervalo sem vistoria entre a publicação do TCA e o informe de plantio")
    s.text(30, 44, "Ciclo de vida do TCA", 26, INK, 700)
    s.text(30, 68, "Portaria SVMA 105/2024 (com a Portaria 116/2024) e Decreto 53.889/2013. Quem age em cada etapa, e quando a SVMA é obrigada a ir ao local.", 13, MUTED)

    # faixas
    LX, LW = 30, 1440
    y_int, y_svma, lane_h = 100, 330, 210
    s.rect(LX, y_int, LW, lane_h, "#eef3ef", RULE)
    s.rect(LX, y_svma, LW, lane_h, "#eef1f6", RULE)
    s.text(LX + 12, y_int + 20, "INTERESSADO  ·  declara e executa", 11.5, MUTED, 700)
    s.text(LX + 12, y_svma + 20, "SVMA  ·  analisa, autoriza e verifica", 11.5, MUTED, 700)

    # zona sem vistoria (da publicação do TCA até o informe de plantio), na faixa da SVMA
    zx1, zx2 = 668, 1110
    s.p.append(f'<rect x="{zx1}" y="{y_svma + 30}" width="{zx2 - zx1}" height="{lane_h - 42}" rx="6" fill="{RED_BG}" stroke="{RED}" stroke-width="1.6" stroke-dasharray="6 4"/>')
    s.rect(zx1 + 16, y_svma + 62, zx2 - zx1 - 32, 112, PANEL, RED, 1.4)
    s.text((zx1 + zx2) / 2, y_svma + 86, "INTERVALO SEM VISTORIA OBRIGATÓRIA", 13.5, RED, 700, "middle")
    yy = y_svma + 106
    for ln in ["Entre a publicação do TCA e o informe de plantio, nenhuma norma",
               "obriga a SVMA a ir ao local. O corte, o transplante e a obra inteira",
               "são acompanhados só por documentos que o interessado envia."]:
        s.text((zx1 + zx2) / 2, yy, ln, 11.5, INK, 400, "middle")
        yy += 16
    s.text((zx1 + zx2) / 2, yy + 4, "art. 21 lista só três vistorias; art. 57 fala em “acompanhamento” sem vistoria", 10.5, MUTED, 500, "middle")

    cw = 148
    # --- cartões da faixa do interessado
    I = [
        (40, "1. Pedido", ["Requerimento no Portal 156, plantas (situação atual, pretendida e de compensação) e preço público."], "arts. 4º e 8º"),
        (520, "5. Alvará apostilado", ["O TCA só produz efeito com o Alvará de Execução anotado com o nº do TCA. Protocolar na SVMA em 30 dias."], "art. 51"),
        (680, "6. Corte e transplante", ["Comunica o início (10 dias antes) e o fim (até 20 dias depois), com relatório fotográfico e ART."], "art. 57, §§1º e 3º"),
        (840, "7. Obra e plantio", ["Plantio “preferencialmente no período pós-obras”. O prazo é o que cada TCA fixar."], "art. 70, VI"),
        (1000, "8. Informe de plantio", ["Avisa que plantou. O prazo de manutenção começa a contar deste protocolo."], "arts. 21, II e 74, §1º"),
        (1160, "9. Manutenção", ["12 meses (mudas DAP 3, 5 ou 7 cm) ou 24 meses (reflorestamento)."], "art. 74"),
        (1320, "10. Informe final", ["Avisa o fim do prazo de manutenção e pede o recebimento definitivo."], "art. 21, III"),
    ]
    for x, t, ls, ref in I:
        s.card(x, y_int + 32, cw, t, ls, PANEL, GREEN, INK, ref, h=166)

    # --- cartões da faixa da SVMA
    S = [
        (200, "2. Vistoria 1", ["Obrigatória. Técnico vistoria o imóvel para analisar o pedido e emite relatório."], "arts. 21, I e 22", BLUE_BG, BLUE),
        (360, "3. Parecer e CTCA", ["Parecer conclusivo (vale 18 meses). A câmara interna decide o destino das mudas excedentes."], "arts. 13, 16, 19 e 33", PANEL, BLUE),
        (520, "4. TCA publicado", ["Despacho do Secretário, TCA lavrado, extrato no Diário Oficial e dados no GeoSampa."], "arts. 48 e 49", PANEL, BLUE),
        (1126, "Vistoria 2", ["Obrigatória, mas só depois do informe. Gera o recebimento provisório."], "arts. 21, II e 59, §1º", BLUE_BG, BLUE),
        (1290, "Vistoria 3", ["Obrigatória, só depois do informe final. Gera o recebimento definitivo."], "arts. 21, III e 59, §3º", BLUE_BG, BLUE),
    ]
    for x, t, ls, ref, fill, st in S:
        s.card(x, y_svma + 32, cw, t, ls, fill, st, INK, ref, h=166)

    # --- setas do fluxo
    yi, ys = y_int + 115, y_svma + 115
    s.path(f"M{40 + cw},{yi} C{210},{yi} {200 + cw / 2 - 40},{y_svma - 10} {200 + cw / 2},{y_svma + 32}")       # 1 -> 2
    s.arrow(200 + cw, ys, 360, ys)                                                                             # 2 -> 3
    s.arrow(360 + cw, ys, 520, ys)                                                                             # 3 -> 4
    s.arrow(520 + cw / 2, y_svma + 32, 520 + cw / 2, y_int + 32 + 166)                                          # 4 -> 5
    s.arrow(520 + cw, yi, 680, yi)                                                                             # 5 -> 6
    s.arrow(680 + cw, yi, 840, yi)                                                                             # 6 -> 7
    s.arrow(840 + cw, yi, 1000, yi)                                                                            # 7 -> 8
    s.arrow(1000 + cw, yi, 1160, yi)                                                                           # 8 -> 9
    s.arrow(1160 + cw, yi, 1320, yi)                                                                           # 9 -> 10
    s.path(f"M{1000 + cw / 2 + 20},{y_int + 32 + 166} C{1100},{y_svma - 6} {1170},{y_svma - 6} {1126 + cw / 2},{y_svma + 32}")   # 8 -> vistoria 2
    s.arrow(1320 + cw / 2 + 20, y_int + 32 + 166, 1290 + cw / 2 + 50, y_svma + 32)                              # 10 -> vistoria 3
    # documentos que sobem para a SVMA durante o intervalo (tracejado)
    for x in (680 + cw / 2, 840 + cw / 2):
        s.arrow(x, y_int + 32 + 166, x, y_svma + 30, RED, 1.3, "4 4", red=True)
    s.text(760, y_int + lane_h + 12, "só documentos", 10.5, RED, 600)

    # --- certificados
    cy = 560
    s.text(30, cy + 4, "O QUE SAI DE CADA VISTORIA", 11.5, MUTED, 700)
    s.card(30, cy + 14, 350, "Recebimento provisório", ["Todos os plantios feitos; falta só a manutenção.", "Depende da vistoria 2."], GREEN_BG, GREEN, INK, "Decreto 53.889, art. 8º, §7º · Portaria 105, art. 59, §1º", h=140)
    s.card(396, cy + 14, 350, "Recebimento definitivo", ["Cumprimento integral, incluída a manutenção.", "Depende da vistoria 3. Encerra o TCA."], GREEN_BG, GREEN, INK, "Decreto 53.889, art. 8º, §6º · Portaria 105, art. 59, §3º", h=140)
    s.card(762, cy + 14, 708, "Recebimento parcial: a mesma palavra, quatro sentidos", [
        "I. A compensação externa foi cumprida.",
        "II. O plantio interno de uma parte da obra foi feito (pelo menos 1 edifício inteiro).",
        "III. As obrigações NÃO foram cumpridas, por atraso da Administração.",
        "IV. Por deliberação da CTCA (só no decreto; a portaria omite). O documento é chamado ora de “Termo”, ora de “Certificado”.",
    ], AMBER_BG, AMBER, INK, "Decreto 53.889, art. 8º, §8º (4 hipóteses) · Portaria 105, arts. 59, §2º e 60 (3 hipóteses)", h=140)

    # --- relógios
    ry = 744
    s.text(30, ry + 4, "PRAZOS QUE A NORMA FIXA", 11.5, MUTED, 700)
    s.text(762, ry + 4, "PRAZOS QUE A NORMA NÃO FIXA", 11.5, RED, 700)
    s.rect(30, ry + 14, 716, 270, PANEL, RULE)
    s.rect(762, ry + 14, 708, 270, PANEL, RED, 1.4)
    tem = [
        ("18 meses", "validade do parecer conclusivo, renovável uma vez (art. 19)"),
        ("30 dias", "para protocolar na SVMA o Alvará de Execução apostilado (art. 51, §2º)"),
        ("2 anos", "sem cumprir o art. 51, ou sem iniciar a obra: o TCA é rescindido (art. 53, I e III)"),
        ("1 ano", "de obra paralisada: o TCA é rescindido (art. 53, IV)"),
        ("10 e 20 dias", "para comunicar o início e o fim de cada manejo (art. 57, §1º)"),
        ("12 ou 24 meses", "de manutenção, contados do protocolo do informe de plantio (art. 74)"),
        ("6 meses", "para repor as árvores se o TCA for rescindido depois do corte (art. 54, §2º)"),
        ("0,1% ao dia", "de multa por atraso, até 25% do valor da obrigação (art. 83)"),
    ]
    y = ry + 40
    for a, b in tem:
        s.text(46, y, a, 12.5, INK, 700)
        s.text(170, y, b, 12, INK)
        y += 30
    falta = [
        ("Vistoria do corte.", "Nenhuma vistoria da SVMA é exigida durante o corte e o transplante."),
        ("Prazo para a vistoria 2.", "A norma não diz em quantos dias a SVMA deve vistoriar depois do informe de plantio."),
        ("Intervalo entre o corte e o plantio.", "Não há prazo máximo geral; fica a cargo de cada TCA. A obra pode durar anos."),
        ("Silêncio do interessado.", "Se ele nunca informar o plantio, o prazo de manutenção não começa e a vistoria 2 não é disparada."),
        ("Efeito de cada certificado.", "A portaria não diz o que o recebimento parcial ou provisório libera (por exemplo, o Habite-se)."),
    ]
    y = ry + 40
    for a, b in falta:
        s.text(778, y, a, 12.5, RED, 700)
        y = s.para(778, y + 17, b, 670, 12, INK) + 12
    s.text(30, H - 10, "Fonte: Portaria SVMA 105/2024, arts. 4º a 96 e Anexos; Decreto Municipal 53.889/2013, art. 8º. Leitura do projeto Arboriki, outubro de 2026.", 10.5, MUTED)
    s.save("ciclo-de-vida-tca.svg")


# ======================================================================
# 2. CÁLCULO DA COMPENSAÇÃO
# ======================================================================
def calculo():
    W, H = 1500, 1270
    s = Svg(W, H, "Cálculo da compensação ambiental pela Portaria SVMA 105/2024: do inventário das árvores ao número de mudas, com as exceções")
    s.text(30, 44, "Como se calcula a compensação ambiental", 26, INK, 700)
    s.text(30, 68, "Portaria SVMA 105/2024, arts. 28 a 47 e Anexos VI a VIII. Do inventário das árvores ao número de mudas e ao modo de cumprir. À direita, as exceções.", 13, MUTED)

    MX, MW = 30, 960          # coluna principal
    EX, EW = 1010, 460        # coluna das exceções

    # passo 0
    y = 92
    y2 = s.card(MX, y, MW, "0. Dados de entrada: uma linha por árvore a manejar", [
        "Espécie · DAP (cm) · nativa, exótica, ameaçada de extinção, invasora (ou eucalipto e pínus) ou morta · corte ou transplante · situação da área: APP, vegetação significativa, patrimônio ambiental, fragmento florestal."
    ], PANEL, RULE, INK, "Planta de Situação Atual e Planta de Situação Pretendida (Anexos II e III)")
    s.arrow(MX + MW / 2, y2, MX + MW / 2, y2 + 22)

    # passo 1 - regime
    y = y2 + 24
    s.text(MX, y + 14, "1. QUAL REGIME?", 11.5, MUTED, 700)
    y += 22
    a = s.card(MX, y, 470, "Regime 1:1", [
        "Obra de infraestrutura; utilidade pública, interesse público ou social; HIS; HMP; recuperação de área degradada; remediação.",
        "CF = F × Fm",
        "F = nº de árvores cortadas ou transplantadas.",
    ], AMBER_BG, AMBER, INK, "art. 38 e Anexo VI, item 1", h=150)
    b = s.card(MX + 490, y, 470, "Regime geral", [
        "Todas as demais obras e atividades.",
        "CF = (A + B + C + D + E + P + M) × Fr",
        "Cada parcela é uma categoria de vegetação (passo 2).",
    ], GREEN_BG, GREEN, INK, "Anexo VI, item 2", h=150)
    s.arrow(MX + 490 + 235, b, MX + 490 + 235, b + 22)

    # passo 2 - parcelas
    y = b + 24
    s.text(MX, y + 14, "2. PARCELAS DO REGIME GERAL", 11.5, MUTED, 700)
    y += 22
    pw = 232
    parc = [
        ("A, B, D e P", ["A: significativa em APP. B: preservação permanente ou significativa fora de APP. D: restante do imóvel. P: patrimônio ambiental ou imune de corte.",
                         "[(It·T + Ic·C) exóticas × 50% + (It·T + Ic·C) nativas] × Fm"]),
        ("C · ameaçadas de extinção", ["(It·T + Ic·C) × Fm, sem desconto.", "Mais 2 mudas da mesma espécie para cada exemplar cortado (art. 76, §1º)."]),
        ("E · eucalipto, pínus e invasoras", ["1 muda por árvore.", "Vezes Fm se estiver em APP ou for patrimônio ambiental ou imune de corte."]),
        ("M · árvores mortas", ["1 muda por árvore morta removida.", "Tabela VII."]),
    ]
    yb = y
    for i, (t, ls) in enumerate(parc):
        yb = max(yb, s.card(MX + i * (pw + 10.5), y, pw, t, ls, PANEL, GREEN, INK, None, h=158))
    s.arrow(MX + MW / 2, yb, MX + MW / 2, yb + 22)

    # passo 3 - fatores
    y = yb + 24
    s.text(MX, y + 14, "3. FATORES", 11.5, MUTED, 700)
    y += 22
    fh = 222
    s.rect(MX, y, 310, fh, PANEL, RULE)
    s.text(MX + 10, y + 22, "Ic (corte) e It (transplante)", 13, INK, 600)
    s.para(MX + 10, y + 40, "Pela média dos 10% maiores DAP do grupo, e não árvore por árvore.", 290, 11.5)
    rows = [("DAP (cm)", "corte", "transpl."), ("5 a 10", "3", "2"), ("11 a 30", "6", "3"), ("31 a 60", "9", "6"), ("61 a 90", "15", "10"), ("91 a 120", "21", "14"), ("121 a 150", "30", "18"), ("acima de 150", "45", "20")]
    ty = y + 78
    for i, (c1, c2, c3) in enumerate(rows):
        wt = 700 if i == 0 else 400
        col = MUTED if i == 0 else INK
        s.text(MX + 14, ty, c1, 11.5, col, wt)
        s.text(MX + 170, ty, c2, 11.5, col, wt, "end")
        s.text(MX + 250, ty, c3, 11.5, col, wt, "end")
        ty += 15
    s.text(MX + 300, y + 22, "Tabelas V e VI", 10.5, MUTED, 500, "end")

    s.rect(MX + 325, y, 395, fh, PANEL, RULE)
    s.text(MX + 335, y + 22, "Fm · Fator Multiplicador (valor ecológico)", 13, INK, 600)
    fm = [("10", "vegetação significativa em APP"), ("5", "espécie ameaçada de extinção"), ("4", "fragmento florestal, copa a suprimir acima de 1.000 m²"),
          ("3", "fragmento até 1.000 m²; ou preservação permanente, DAP 31 a 60"), ("2", "preservação permanente, DAP 10 a 30; patrimônio ambiental"), ("1", "todas as demais situações")]
    ty = y + 44
    for v, d in fm:
        s.text(MX + 358, ty, v, 13, GREEN, 700, "end")
        ty = s.para(MX + 368, ty, d, 345, 11.5) + 5
    s.text(MX + 710, y + fh - 8, "Anexo VIII · vale o maior fator aplicável", 10.5, MUTED, 500, "end")

    s.rect(MX + 735, y, 225, fh, PANEL, RULE)
    s.text(MX + 745, y + 22, "Fr · fator redutor", 13, INK, 600)
    yy = s.para(MX + 745, y + 42, "Desconto por plantar muda maior que o padrão de DAP 3 cm.", 205, 11.5)
    s.text(MX + 745, yy + 8, "Muda DAP 5 cm", 11.5, INK, 400)
    s.text(MX + 950, yy + 8, "30%", 11.5, INK, 700, "end")
    s.text(MX + 745, yy + 26, "Muda DAP 7 cm", 11.5, INK, 400)
    s.text(MX + 950, yy + 26, "50%", 11.5, INK, 700, "end")
    s.para(MX + 745, yy + 50, "Só vale para as mudas efetivamente plantadas.", 205, 11.5)
    s.text(MX + 950, y + fh - 8, "Tabela IX", 10.5, MUTED, 500, "end")
    y += fh
    s.arrow(MX + MW / 2, y, MX + MW / 2, y + 22)

    # passo 4
    y += 24
    y2 = s.card(MX, y, MW, "4. Compensação Final (CF), em número de mudas", [
        "Toda fração arredonda para o inteiro de cima (art. 39, parágrafo único).",
        "Compara-se com o cálculo pela legislação estadual e vale o mais restritivo, caso a caso: árvores isoladas, fragmento florestal, intervenção em APP (Anexo VI, item 3).",
    ], BLUE_BG, BLUE, INK, "Unidade: 1 muda de espécie nativa, DAP 3 cm, com tutor (art. 40)")
    s.arrow(MX + MW / 2, y2, MX + MW / 2, y2 + 22)

    # passo 5 - piso
    y = y2 + 24
    y2 = s.card(MX, y, MW, "5. Piso: densidade arbórea", [
        "Densidade final (preservadas + transplantadas + plantadas no imóvel e no passeio) igual ou maior que a inicial. No mínimo, uma muda plantada para cada árvore cortada ou removida.",
        "Supressões não autorizadas entram na densidade inicial. Plantio de TAC não conta.",
    ], PANEL, RULE, INK, "art. 34, §§1º a 6º")
    s.arrow(MX + MW / 2, y2, MX + MW / 2, y2 + 22)

    # passo 6 - onde cumprir
    y = y2 + 24
    s.text(MX, y + 14, "6. ONDE E COMO CUMPRIR, NESTA ORDEM", 11.5, MUTED, 700)
    y += 22
    cw = 182
    seq = [
        ("No imóvel", ["Prioridade. Até atingir a densidade final."], "art. 16, I", GREEN_BG, GREEN),
        ("Passeio e entorno", ["Se não couber no lote, com anuência do órgão gestor."], "arts. 16, I e 71", GREEN_BG, GREEN),
        ("Plantio externo", ["Excedente vai à CTCA. Preferência pela área de influência indireta."], "arts. 33, §1º e 40", PANEL, BLUE),
        ("Viveiro municipal", ["Mudas excedentes × 5,35. Ao menos 10% em DAP 5 cm."], "art. 41", AMBER_BG, AMBER),
        ("Depósito no FEMA", ["VCF = CF × (Vm + Vt). Vm é “calculado pela SVMA”."], "art. 42 e Anexo VII", AMBER_BG, AMBER),
    ]
    yb = y
    for i, (t, ls, ref, fill, st) in enumerate(seq):
        x = MX + i * (cw + 12.5)
        yb = max(yb, s.card(x, y, cw, t, ls, fill, st, INK, ref, h=132))
        if i:
            s.arrow(x - 12.5, y + 66, x, y + 66)
    y = yb + 12
    yend = s.card(MX, y, MW, "Ou conversão em obras e serviços", [
        "Excepcional. Praças, parques, arborização, recuperação de área degradada, compra de área verde. Custo = nº de mudas × custo da muda divulgado pela CLA. Formalizada por Carta de Obrigação.",
    ], AMBER_BG, AMBER, INK, "arts. 33, §2º, 43 a 47 · Decreto 53.889/2013")
    HF = int(yend + 44)
    s.text(MX, HF - 14, "Fonte: Portaria SVMA 105/2024 (texto integral com Anexos). Valores do Fator Multiplicador conforme Anexo VIII. Leitura do projeto Arboriki, outubro de 2026.", 10.5, MUTED)

    # ---------------- exceções
    s.rect(EX, 92, EW, yend - 92, PANEL, RED, 1.4)
    s.text(EX + 16, 118, "EXCEÇÕES E CASOS ESPECIAIS", 12, RED, 700)
    exc = [
        ("Isenção total", "Intervenção em APP sem manejo de árvores, para melhoria ambiental: limpeza e desassoreamento de córrego, implantação de área verde, canalização de esgoto. Depende de parecer favorável.", "art. 29"),
        ("Retificação de curso d'água", "A APP reduzida é compensada com plantio em área igual ao dobro da área perdida, dentro do terreno.", "art. 30"),
        ("HIS e HMP", "O regime 1:1 só vale para projeto exclusivamente dessas categorias. O plantio pode ir para outra unidade da mesma instituição.", "art. 38, III e parágrafo único"),
        ("Dispensa da densidade arbórea", "Com utilidade pública ou interesse social; ou se o projeto preservar “a porção mais significativa da vegetação” e mantiver área permeável arborizada acima de 50% do mínimo legal e de 30% do terreno.", "art. 35"),
        ("Exóticas valem metade", "Nas parcelas A, B, D e P, as árvores exóticas entram com 50% do peso das nativas.", "Anexo VI"),
        ("Transplante que morre", "1 muda DAP 7 cm no local, mais 2 a 10 mudas ao viveiro conforme o DAP perdido. Com culpa técnica, soma multa.", "arts. 67 e 69"),
        ("Árvore a preservar que morre", "1 muda nativa DAP 7 cm no mesmo local.", "art. 64"),
        ("Plantio externo que morre ou some", "Converte em FEMA ou viveiro: 2 por 1 se há relatório de execução no prazo; 6 por 1 se não há.", "art. 77"),
        ("TCA rescindido depois do corte", "Repor cada árvore com muda DAP 7 cm, no mesmo local, em 6 meses. Não livra das demais obrigações.", "art. 54"),
        ("Competência do Estado", "Vegetação nativa em estágio médio ou avançado e casos da CETESB: a SVMA só lavra TCA complementar se a regra municipal for mais restritiva.", "art. 2º, §§1º a 3º"),
    ]
    y = 140
    for t, d, ref in exc:
        s.text(EX + 16, y, t, 13, INK, 700)
        y = s.para(EX + 16, y + 17, d, EW - 32, 11.5, INK)
        s.text(EX + 16, y + 1, ref, 10.5, MUTED, 500)
        y += 22
        s.p.append(f'<line x1="{EX + 16}" y1="{y - 8}" x2="{EX + EW - 16}" y2="{y - 8}" stroke="{RULE}" stroke-width="1"/>')
        y += 8
    s.save("calculo-compensacao.svg", HF)


ciclo()
calculo()
