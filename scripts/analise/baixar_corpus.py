# @lat: [[analysis-lenses#Lentes de análise#Scripts]]
"""Baixa o texto vigente das normas do rol que não estão em raw/ e grava texto puro em .arboriki/extracted/portais/."""
import pathlib, re, sys, urllib.request
from bs4 import BeautifulSoup

OUT = pathlib.Path(__file__).resolve().parents[2] / ".arboriki" / "extracted" / "portais"
OUT.mkdir(parents=True, exist_ok=True)
P = "https://legislacao.prefeitura.sp.gov.br/"
SVMA = "portaria-secretaria-municipal-do-verde-e-do-meio-ambiente-svma-"
FONTES = {
    "MUN_LEI_17794_2022": [P + "lei-17794-de-27-de-abril-de-2022/consolidado"],
    "MUN_DECRETO_61859_2022": [P + "decreto-61859-de-3-de-outubro-de-2022/consolidado"],
    "MUN_PORTARIA_SVMA_51_2024": [P + SVMA + "51-de-21-de-junho-de-2024/consolidado"],
    "MUN_PORTARIA_SVMA_39_2024": [P + SVMA + "39-de-29-de-maio-de-2024/consolidado"],
    "MUN_LEI_16050_2014": [P + "lei-16050-de-31-de-julho-de-2014/consolidado"],
    "MUN_LEI_10365_1987": [P + "lei-10365-de-22-de-setembro-de-1987/consolidado", P + "lei-10365-de-22-de-setembro-de-1987"],
    "MUN_PORTARIA_SVMA_130_2013": [P + "portaria-secretaria-municipal-do-verde-e-do-meio-ambiente-130-de-12-de-outubro-de-2013/consolidado",
                                   P + "portaria-secretaria-municipal-do-verde-e-do-meio-ambiente-130-de-12-de-outubro-de-2013"],
    "MUN_DECRETO_59671_2020": [P + "decreto-59671-de-7-de-agosto-de-2020/consolidado"],
    "MUN_LEI_13293_2002": [P + "lei-13293-de-14-de-janeiro-de-2002/consolidado"],
    "MUN_LEI_15442_2011": [P + "lei-15442-de-09-de-setembro-de-2011/consolidado"],
    "EST_DECRETO_39743_1994": ["https://www.al.sp.gov.br/repositorio/legislacao/decreto/1994/decreto-39743-23.12.1994.html"],
    "FED_LEI_12651_2012": ["https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2012/lei/l12651.htm"],
    "FED_LEI_9605_1998": ["https://www.planalto.gov.br/ccivil_03/leis/l9605.htm"],
    "FED_LC_140_2011": ["https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp140.htm"],
}

def baixar(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    raw = urllib.request.urlopen(req, timeout=60).read()
    try:
        html = raw.decode("utf-8")
    except UnicodeDecodeError:
        html = raw.decode("iso-8859-1")
    s = BeautifulSoup(html, "html.parser")
    for x in s(["script", "style", "nav", "footer"]):
        x.decompose()
    for st in s.find_all(["strike", "s"]):  # texto revogado no Planalto
        st.insert_before("[REVOGADO: ")
        st.insert_after("]")
    txt = s.get_text("\n")
    txt = re.sub(r"[ \t\xa0]+", " ", txt)
    txt = re.sub(r"\n\s*\n+", "\n", txt)
    return txt.strip()

for nome, urls in FONTES.items():
    ok = False
    for u in urls:
        try:
            t = baixar(u)
        except Exception as e:
            print(f"ERRO {nome}: {u} -> {e}")
            continue
        if "Página não encontrada" in t or len(t) < 1500:
            print(f"404  {nome}: {u} ({len(t)} chars)")
            continue
        (OUT / f"{nome}.txt").write_text(f"FONTE: {u}\n\n{t}", encoding="utf-8")
        print(f"OK   {nome}: {len(t)} chars")
        ok = True
        break
    if not ok:
        print(f"FALHOU {nome}")
