# @lat: [[analysis-lenses#Lentes de análise#Scripts]]
import pathlib, re
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
S = ROOT / ".arboriki" / "extracted"
R = ROOT / "wiki" / "assets" / "infograficos"
t = (HERE / "lentes.src.html").read_text(encoding="utf-8")
core = (S / "conceitos_core.json").read_text(encoding="utf-8")
assert "/*CORE*/null" in t
t = t.replace("/*CORE*/null", core)
for tag, f in (("<!--SVG_CICLO-->", "ciclo-de-vida-tca.svg"), ("<!--SVG_CALCULO-->", "calculo-compensacao.svg")):
    svg = (R / f).read_text(encoding="utf-8")
    svg = re.sub(r"<defs>.*?</defs>", "", svg, count=1, flags=re.S)
    assert tag in t
    t = t.replace(tag, svg)
(S / "lentes.html").write_text(t, encoding="utf-8")
print("ok", len(t) // 1024, "KB")
