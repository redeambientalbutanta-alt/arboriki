"""Extração de texto puro das fontes de raw/ para o staging da wiki."""

from __future__ import annotations

import os
from pathlib import Path

import pymupdf

OCR_MIN_CHARS = 20  # página com menos que isto é tratada como digitalizada
OCR_LANG = os.environ.get("ARBORIKI_OCR_LANG", "por")
OCR_DPI = 300


def extract_text(path: Path) -> str:
    """Devolve o texto puro de um PDF, HTML ou arquivo de texto."""
    suffix = path.suffix.lower()
    if suffix == ".pdf":
        return _extract_pdf(path)
    if suffix in {".html", ".htm"}:
        return _extract_html(path)
    if suffix in {".txt", ".md"}:
        return path.read_text(encoding="utf-8", errors="replace").strip()
    raise ValueError(f"formato não suportado: {path.suffix}")


# @lat: [[ingestion-flow#Ingestion Pipeline Specification#Ferramenta de extração — CLI arboriki]]
def _extract_pdf(path: Path) -> str:
    partes: list[str] = []
    with pymupdf.open(path) as doc:
        for page in doc:
            texto = page.get_text().strip()
            if len(texto) < OCR_MIN_CHARS:
                texto = _ocr_page(page)
            partes.append(texto)
    return "\n\n".join(p for p in partes if p).strip()


def _ocr_page(page: pymupdf.Page) -> str:
    import pytesseract
    from PIL import Image

    cmd = os.environ.get("TESSERACT_CMD")
    if cmd:
        pytesseract.pytesseract.tesseract_cmd = cmd

    pix = page.get_pixmap(dpi=OCR_DPI)
    img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
    try:
        return pytesseract.image_to_string(img, lang=OCR_LANG).strip()
    except pytesseract.TesseractNotFoundError as e:
        raise RuntimeError(
            "Tesseract não encontrado no PATH. Instale com "
            "`winget install UB-Mannheim.TesseractOCR` ou defina a variável TESSERACT_CMD."
        ) from e
    except pytesseract.pytesseract.TesseractError as e:
        raise RuntimeError(
            f"OCR falhou (idioma {OCR_LANG!r}). Confirme o arquivo "
            f"`{OCR_LANG}.traineddata` na pasta tessdata do Tesseract."
        ) from e


def _extract_html(path: Path) -> str:
    from bs4 import BeautifulSoup

    bruto = path.read_bytes()
    try:
        texto = bruto.decode("utf-8")
    except UnicodeDecodeError:
        texto = bruto.decode("iso-8859-1")
    sopa = BeautifulSoup(texto, "lxml")
    for tag in sopa(["script", "style", "nav", "footer"]):
        tag.decompose()
    return sopa.get_text("\n", strip=True)
