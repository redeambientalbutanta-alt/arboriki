# @lat: [[analysis-lenses#Lentes de análise#Scripts]]
"""Regera CSV, tabela markdown da wiki e o JSON compacto usado pela página de comparação."""
import csv, json, pathlib, re

R = pathlib.Path(__file__).resolve().parents[2]
S = R / ".arboriki" / "extracted"
d = json.loads((S / "conceitos.json").read_text(encoding="utf-8"))
ids = list(d["corpus"])
ABBR = {"FED_LEI_12651_2012": "L12651", "FED_LEI_9605_1998": "L9605", "FED_LC_140_2011": "LC140", "EST_DECRETO_30443_1989": "DE30443",
        "EST_DECRETO_39743_1994": "DE39743", "MUN_LEI_10365_1987": "L10365", "MUN_LEI_13293_2002": "L13293", "MUN_LEI_15442_2011": "L15442",
        "MUN_LEI_16050_2014": "PDE", "MUN_LEI_16402_2016": "LPUOS", "MUN_LEI_17794_2022": "L17794", "MUN_DECRETO_53889_2013": "D53889",
        "MUN_DECRETO_59671_2020": "D59671", "MUN_DECRETO_61859_2022": "D61859", "MUN_PORTARIA_SVMA_130_2013": "P130",
        "MUN_PORTARIA_SVMA_39_2024": "P39", "MUN_PORTARIA_SVMA_51_2024": "P51", "MUN_PORTARIA_SVMA_105_2024": "P105", "MUN_QUADRO1_LPUOS": "Q1"}
CORE = ["vegetação de porte arbóreo", "exemplar / espécime arbóreo", "vegetação significativa", "imune de corte", "patrimônio ambiental",
        "vegetação de preservação permanente", "área de preservação permanente (APP)", "área verde", "maciço arbóreo", "bosque", "fragmento florestal",
        "Mata Atlântica", "Cerrado", "vegetação nativa", "manejo", "supressão", "poda drástica", "compensação ambiental", "TCA", "TAC",
        "densidade arbórea", "área permeável", "Quota Ambiental", "utilidade pública", "interesse social"]

dados = R / "wiki" / "assets" / "dados"
dados.mkdir(parents=True, exist_ok=True)
with open(dados / "conceitos-por-norma.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["conceito"] + [ABBR[i] for i in ids])
    for c, por in d["conceitos"].items():
        w.writerow([c] + [por.get(i, {}).get("n", 0) for i in ids])
with open(dados / "normas-do-corpus.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["sigla", "id", "rotulo", "esfera", "tipo", "ano", "caracteres"])
    for i in ids:
        v = d["corpus"][i]
        w.writerow([ABBR[i], i, v["rotulo"], v["esfera"], v["tipo"], v["ano"], v["chars"]])

L = ["| Conceito | " + " | ".join(ABBR[i] for i in ids) + " | normas |", "|---|" + "---:|" * (len(ids) + 1)]
for c in CORE:
    por = d["conceitos"][c]
    L.append("| " + c + " | " + " | ".join(str(por[i]["n"]) if i in por else "·" for i in ids) + f" | {len(por)} |")
tabela = "\n".join(L)

pg = R / "wiki" / "mapa-de-conceitos.md"
t = pg.read_text(encoding="utf-8")
m = re.search(r"\| Conceito \| L12651 .*?\n(?:\|.*\n)+", t)
assert m, "tabela não encontrada na página"
pg.write_text(t[:m.start()] + tabela + "\n" + t[m.end():], encoding="utf-8")

core = {"normas": [{"s": ABBR[i], "l": d["corpus"][i]["rotulo"], "e": d["corpus"][i]["esfera"], "t": d["corpus"][i]["tipo"], "a": d["corpus"][i]["ano"]} for i in ids],
        "conceitos": [{"c": c, "n": [d["conceitos"][c].get(i, {}).get("n", 0) for i in ids]} for c in CORE]}
(S / "conceitos_core.json").write_text(json.dumps(core, ensure_ascii=False), encoding="utf-8")
print("ok;", len(d["conceitos"]), "conceitos no CSV;", len(CORE), "na tabela")
