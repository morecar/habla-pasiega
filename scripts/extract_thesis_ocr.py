#!/usr/bin/env python3
"""Extract the existing OCR layer from Penny's 1967 thesis PDF.

The output is deliberately kept outside the canonical LaTeX transcription.
OCR text is evidence and a typing aid, never an authoritative transcription.
"""

from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path

from pypdf import PdfReader


PRINTED_PAGE_RE = re.compile(r"^\s*[-—]?\s*(\d{1,3})\s*[-—]?\s*$", re.MULTILINE)


def normalise_line_endings(text: str) -> str:
    return text.replace("\r\n", "\n").replace("\r", "\n").strip() + "\n"


def guess_printed_page(text: str) -> str:
    """Return a conservative printed-page guess from the top of the OCR text."""
    top = "\n".join(text.splitlines()[:8])
    match = PRINTED_PAGE_RE.search(top)
    return match.group(1) if match else ""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("pdf", type=Path, help="Path to PennyRJ_1967redux.pdf")
    parser.add_argument("output", type=Path, help="Directory for extracted OCR pages")
    args = parser.parse_args()

    output = args.output
    pages_dir = output / "pages"
    pages_dir.mkdir(parents=True, exist_ok=True)

    reader = PdfReader(args.pdf)
    manifest_rows: list[dict[str, object]] = []

    for pdf_page, page in enumerate(reader.pages, start=1):
        raw_text = page.extract_text() or ""
        text = normalise_line_endings(raw_text) if raw_text.strip() else ""
        page_name = f"page-{pdf_page:03d}.txt"
        (pages_dir / page_name).write_text(text, encoding="utf-8")
        manifest_rows.append(
            {
                "pdf_page": pdf_page,
                "printed_page_guess": guess_printed_page(text),
                "ocr_characters": len(text),
                "ocr_lines": len(text.splitlines()),
                "file": f"pages/{page_name}",
                "status": "ocr-unverified",
            }
        )

    with (output / "manifest.csv").open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(
            stream, fieldnames=manifest_rows[0].keys(), lineterminator="\n"
        )
        writer.writeheader()
        writer.writerows(manifest_rows)

    total_characters = sum(int(row["ocr_characters"]) for row in manifest_rows)
    empty_pages = sum(int(row["ocr_characters"]) == 0 for row in manifest_rows)
    print(f"Extracted {len(manifest_rows)} pages")
    print(f"OCR characters: {total_characters}")
    print(f"Pages without OCR text: {empty_pages}")


if __name__ == "__main__":
    main()
