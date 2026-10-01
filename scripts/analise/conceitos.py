# @lat: [[analysis-lenses#Lentes de análise#Scripts]]
"""Varre o corpus de normas e conta, por conceito, onde aparece e onde é definido."""
import json, pathlib, re, sys

BASE = pathlib.Path(__file__).resolve().parents[2] / ".arboriki" / "extracted"
CORPUS = {
    # id: (arquivo, rótulo, esfera, tipo, ano)
    "FED_LEI_12651_2012": ("portais/FED_LEI_12651_2012.txt", "Lei Federal 12.651/2012", "F", "lei", 2012),
    "FED_LEI_9605_1998": ("portais/FED_LEI_9605_1998.txt", "Lei Federal 9.605/1998", "F", "lei", 1998),
    "FED_LC_140_2011": ("portais/FED_LC_140_2011.txt", "LC 140/2011", "F", "lei", 2011),
    "EST_DECRETO_30443_1989": ("legislacao/Decreto Estadual 30.443-1989.txt", "Decreto Est. 30.443/1989", "E", "dec", 1989),
    "EST_DECRETO_39743_1994": ("portais/EST_DECRETO_39743_1994.txt", "Decreto Est. 39.743/1994", "E", "dec", 1994),
    "MUN_LEI_10365_1987": ("portais/MUN_LEI_10365_1987.txt", "Lei 10.365/1987", "M", "lei", 1987),
    "MUN_LEI_13293_2002": ("portais/MUN_LEI_13293_2002.txt", "Lei 13.293/2002", "M", "lei", 2002),
    "MUN_LEI_15442_2011": ("portais/MUN_LEI_15442_2011.txt", "Lei 15.442/2011", "M", "lei", 2011),
    "MUN_LEI_16050_2014": ("portais/MUN_LEI_16050_2014.txt", "Lei 16.050/2014 (PDE)", "M", "lei", 2014),
    "MUN_LEI_16402_2016": ("legislacao/Lei 16402-2016.txt", "Lei 16.402/2016 (LPUOS)", "M", "lei", 2016),
    "MUN_LEI_17794_2022": ("portais/MUN_LEI_17794_2022.txt", "Lei 17.794/2022", "M", "lei", 2022),
    "MUN_DECRETO_53889_2013": ("legislacao/Decreto Municipail 53.889-2013.txt", "Decreto 53.889/2013", "M", "dec", 2013),
    "MUN_DECRETO_59671_2020": ("portais/MUN_DECRETO_59671_2020.txt", "Decreto 59.671/2020", "M", "dec", 2020),
    "MUN_DECRETO_61859_2022": ("portais/MUN_DECRETO_61859_2022.txt", "Decreto 61.859/2022", "M", "dec", 2022),
    "MUN_PORTARIA_SVMA_130_2013": ("portais/MUN_PORTARIA_SVMA_130_2013.txt", "Portaria SVMA 130/2013 (revogada)", "M", "infra", 2013),
    "MUN_PORTARIA_SVMA_39_2024": ("portais/MUN_PORTARIA_SVMA_39_2024.txt", "Portaria SVMA 39/2024", "M", "infra", 2024),
    "MUN_PORTARIA_SVMA_51_2024": ("portais/MUN_PORTARIA_SVMA_51_2024.txt", "Portaria SVMA 51/2024", "M", "infra", 2024),
    "MUN_PORTARIA_SVMA_105_2024": ("legislacao/Portaria SVMA 105-2024_anexos completos.txt", "Portaria SVMA 105/2024", "M", "infra", 2024),
    "MUN_QUADRO1_LPUOS": ("legislacao/Quadro 1 – Conceitos e definições.txt", "Proposta de Quadro 1 (LPUOS)", "M", "prop", 2024),
}
CONCEITOS = {
    "vegetação de porte arbóreo": r"vegeta[çc][ãa]o de porte arb[óo]reo",
    "exemplar / espécime arbóreo": r"(?:exemplar(?:es)?|esp[ée]cimes?|indiv[íi]duos?) arb[óo]reos?",
    "DAP": r"\bDAP\b|di[âa]metro (?:do caule )?[àa] altura do peito",
    "vegetação significativa": r"vegeta[çc][ãa]o (?:arb[óo]rea )?significativa",
    "imune de corte": r"imunes? (?:de|ao) corte",
    "patrimônio ambiental": r"patrim[ôo]nio ambiental",
    "vegetação de preservação permanente": r"vegeta[çc][ãa]o de preserva[çc][ãa]o permanente|de preserva[çc][ãa]o permanente,? (?:para efeitos desta lei, )?a vegeta[çc][ãa]o|vegeta[çc][ãa]o consideradas? de preserva[çc][ãa]o permanente",
    "área de preservação permanente (APP)": r"[áa]reas? de preserva[çc][ãa]o permanente|\bAPPs?\b",
    "área verde": r"[áa]reas? verdes?",
    "maciço arbóreo": r"maci[çc]os?(?: arb[óo]reos?| cont[íi]nuos?| de vegeta[çc][ãa]o)?",
    "bosque": r"\bbosques?\b",
    "fragmento florestal": r"fragmentos? florestal|fragmentos? florestais|fragmentos? de (?:mata|vegeta[çc][ãa]o)",
    "floresta": r"\bflorestas?\b",
    "Mata Atlântica": r"mata atl[âa]ntica",
    "Cerrado": r"\bcerrados?\b",
    "vegetação nativa": r"vegeta[çc][ãa]o nativa",
    "estágio de regeneração": r"est[áa]gios? (?:\w+ ){0,3}de regenera[çc][ãa]o|est[áa]gio (?:pioneiro|inicial|m[ée]dio|avan[çc]ado)",
    "espécie nativa": r"esp[ée]cies? nativas?|mudas? nativas?",
    "espécie exótica / invasora": r"esp[ée]cies? ex[óo]ticas?|ex[óo]ticas? invasoras?|esp[ée]cies? invasoras?",
    "espécie ameaçada de extinção": r"amea[çc]ad[ao]s? de extin[çc][ãa]o",
    "manejo": r"\bmanejo\b",
    "supressão": r"supress[ãa]o|supress[õo]es|suprimi",
    "corte": r"\bcortes?\b",
    "transplante": r"transplant",
    "poda": r"\bpodas?\b",
    "poda drástica": r"poda dr[áa]stica",
    "risco de queda": r"risco(?: iminente)? de queda",
    "manejo de urgência": r"manejo de urg[êe]ncia|car[áa]ter de urg[êe]ncia|situa[çc][ãa]o de urg[êe]ncia",
    "compensação ambiental": r"compensa[çc][ãa]o ambiental|medidas? compensat[óo]rias?",
    "reparação": r"repara[çc][ãa]o (?:ambiental|integral|do dano|dos danos)",
    "TCA": r"Termo de Compromisso Ambiental|\bTCA\b",
    "TAC": r"Termo de (?:Compromisso de )?Ajustamento de Conduta|\bTAC\b",
    "densidade arbórea": r"densidade arb[óo]rea",
    "área permeável": r"[áa]reas? perme[áa]ve(?:l|is)|permeabilidade",
    "Quota Ambiental": r"quota ambiental",
    "calçada verde": r"cal[çc]adas? verdes?",
    "arborização urbana": r"arboriza[çc][ãa]o urbana",
    "utilidade pública": r"utilidade p[úu]blica",
    "interesse social": r"interesse social",
    "unidade de conservação": r"unidades? de conserva[çc][ãa]o",
    "ZEPAM": r"\bZEPAMs?\b|Zonas? Especia(?:l|is) de Prote[çc][ãa]o Ambiental",
    "bem de interesse comum / especialmente protegido": r"bem de interesse comum|bem especialmente protegido|bens? de uso comum",
    "muda (padrão)": r"padr[ãa]o de muda|mudas? (?:de )?padr[ãa]o|muda com DAP|mudas? DAP",
    "licenciamento ambiental": r"licenciamento ambiental",
    "impacto local": r"impactos? (?:ambienta(?:l|is) )?(?:de [âa]mbito )?loca(?:l|is)",
    "área de influência": r"[áa]rea de influ[êe]ncia",
    "reserva legal": r"reserva legal",
    "remanescente": r"remanescentes?",
}
DEF = re.compile(r"considera(?:m)?-se|consideram-se|entende-se|entendem-se|para (?:os )?(?:efeitos?|fins)|define-se|denomina-se|são considerad|é considerad|fica(?:m)? considerad|defini[çc][õo]es|:\s", re.I)

res = {"corpus": {k: {"rotulo": v[1], "esfera": v[2], "tipo": v[3], "ano": v[4]} for k, v in CORPUS.items()}, "conceitos": {}}
textos = {}
for k, v in CORPUS.items():
    t = (BASE / v[0]).read_text(encoding="utf-8", errors="replace")
    textos[k] = re.sub(r"\s+", " ", t)
    res["corpus"][k]["chars"] = len(textos[k])

for nome, pat in CONCEITOS.items():
    rx = re.compile(pat, re.I)
    por = {}
    for k, t in textos.items():
        ms = list(rx.finditer(t))
        if not ms:
            continue
        defs = []
        for m in ms:
            a, b = max(0, m.start() - 160), min(len(t), m.end() + 260)
            ctx = t[a:b]
            pre = t[max(0, m.start() - 90):m.start()]
            pos = t[m.end():m.end() + 40]
            if DEF.search(pre) or re.match(r"\s*(?:\([^)]{1,30}\))?\s*(?::|[-–—]\s|é |são |aquel|todo|toda |qualquer)", pos, re.I):
                defs.append(ctx)
            if len(defs) >= 3:
                break
        por[k] = {"n": len(ms), "defs": defs}
    res["conceitos"][nome] = por

out = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else BASE / "conceitos.json"
out.write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
# resumo
ids = list(CORPUS)
print("conceito".ljust(46), " ".join(i.split("_", 1)[1][:11].ljust(11) for i in ids))
for nome, por in res["conceitos"].items():
    print(nome[:45].ljust(46), " ".join((str(por[i]["n"]) + ("*" if por.get(i, {}).get("defs") else "")).ljust(11) if i in por else ".".ljust(11) for i in ids))
