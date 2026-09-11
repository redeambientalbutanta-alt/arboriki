"""CLI arboriki — re-lê raw/ e prepara o material para a atualização da wiki.

A parte mecânica (detectar mudanças, extrair texto) fica aqui. A análise
legística e a escrita das páginas continuam sendo trabalho do Claude, via a
skill `ingestao-wiki-legislativo`.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

from arboriki.extract import extract_text

RAIZ = Path(__file__).resolve().parents[2]
RAW = RAIZ / "raw"
STAGING = RAIZ / ".arboriki" / "extracted"
MANIFEST = RAIZ / ".arboriki" / "manifest.json"

FORMATOS = {".pdf", ".html", ".htm", ".txt", ".md"}


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _fontes() -> list[Path]:
    return sorted(
        p
        for p in RAW.rglob("*")
        if p.is_file()
        and p.suffix.lower() in FORMATOS
        and "descarte" not in p.relative_to(RAW).parts
    )


def _carregar_manifest() -> dict:
    if MANIFEST.exists():
        return json.loads(MANIFEST.read_text(encoding="utf-8"))
    return {}


def _salvar_manifest(dados: dict) -> None:
    MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    MANIFEST.write_text(
        json.dumps(dados, indent=2, ensure_ascii=False, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def _estado(fonte: Path, manifest: dict) -> tuple[str, str]:
    rel = fonte.relative_to(RAIZ).as_posix()
    registro = manifest.get(rel)
    if registro is None:
        return rel, "NOVO"
    if registro.get("sha256") != _sha256(fonte):
        return rel, "ALTERADO"
    return rel, "OK"


def cmd_scan(_: argparse.Namespace) -> int:
    manifest = _carregar_manifest()
    fontes = _fontes()
    pendentes = 0
    for fonte in fontes:
        rel, estado = _estado(fonte, manifest)
        print(f"{'  ' if estado == 'OK' else '* '}{estado:9} {rel}")
        pendentes += estado != "OK"
    conhecidas = {f.relative_to(RAIZ).as_posix() for f in fontes}
    for rel in sorted(set(manifest) - conhecidas):
        print(f"! {'REMOVIDO':9} {rel}")
    print(f"\n{len(fontes)} fonte(s), {pendentes} pendente(s) de ingestão.")
    return 0


def cmd_extract(args: argparse.Namespace) -> int:
    manifest = _carregar_manifest()
    alvos: list[tuple[Path, str]] = []
    for fonte in _fontes():
        rel, estado = _estado(fonte, manifest)
        if args.force or estado != "OK":
            alvos.append((fonte, rel))
    if not alvos:
        print("Nada a extrair. Use --force para reprocessar tudo.")
        return 0

    falhas = 0
    for fonte, rel in alvos:
        destino = STAGING / Path(rel).relative_to("raw").with_suffix(".txt")
        try:
            texto = extract_text(fonte)
        except Exception as e:  # noqa: BLE001 — reporta e segue para a próxima fonte
            print(f"  ERRO  {rel}: {e}", file=sys.stderr)
            falhas += 1
            continue
        destino.parent.mkdir(parents=True, exist_ok=True)
        destino.write_text(texto, encoding="utf-8")
        manifest[rel] = {
            "sha256": _sha256(fonte),
            "extracted": destino.relative_to(RAIZ).as_posix(),
            "chars": len(texto),
        }
        print(f"  OK    {rel} -> {destino.relative_to(RAIZ).as_posix()} ({len(texto)} chars)")

    _salvar_manifest(manifest)
    print(
        f"\n{len(alvos) - falhas} fonte(s) extraída(s) para "
        f"{STAGING.relative_to(RAIZ).as_posix()}/."
    )
    if falhas:
        print(f"{falhas} falha(s) — veja as mensagens acima.")
    print("Rode a skill `ingestao-wiki-legislativo` para atualizar as páginas da wiki.")
    return 1 if falhas else 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="arboriki",
        description="Re-lê raw/ e prepara a atualização da wiki de arborização.",
    )
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_scan = sub.add_parser("scan", help="lista as fontes de raw/ e o que mudou desde a última extração")
    p_scan.set_defaults(func=cmd_scan)

    p_extract = sub.add_parser("extract", help="extrai texto puro das fontes novas ou alteradas")
    p_extract.add_argument("--force", action="store_true", help="reprocessa todas as fontes")
    p_extract.set_defaults(func=cmd_extract)

    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
