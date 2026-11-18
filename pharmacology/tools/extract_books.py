"""Extract the two pharmacology textbooks to one text file per page.

Run from the repo root:
    .venv/bin/python pharmacology/tools/extract_books.py

Output: pharmacology/books/text/<book>/<printed page>.txt
  - files are named by the book's PRINTED page number (the number to cite),
    zero-padded to 4 digits, e.g. katzung/0387.txt
  - front matter (before printed page 1) is named fm_<pdf page>.txt
  - each file starts with a header line giving both printed and PDF page
  - <book>/_toc.txt lists chapters with printed start pages

Printed page = PDF page - offset. Offsets were checked against page headers
at several points in each book (front, middle, index).
"""
import pathlib

import pymupdf

ROOT = pathlib.Path(__file__).resolve().parents[1]
BOOKS = {
    "katzung": {
        "pdf": "Basic-Clinical-Pharmacology-2018.pdf",
        "title": "Katzung, Basic & Clinical Pharmacology, 14th ed. (2018)",
        "offset": 14,
    },
    "lippincott": {
        "pdf": "Lippincott Illustrated Reviews Pharmacology South Asian Edition (visit Libtoon.com).pdf",
        "title": "Lippincott Illustrated Reviews: Pharmacology, South Asian Edition",
        "offset": 17,
    },
}


def main():
    for key, book in BOOKS.items():
        doc = pymupdf.open(ROOT / "books" / book["pdf"])
        out = ROOT / "books" / "text" / key
        out.mkdir(parents=True, exist_ok=True)
        offset = book["offset"]
        empty = 0
        for i, page in enumerate(doc):
            pdf_page = i + 1
            printed = pdf_page - offset
            text = page.get_text()
            if len(text.strip()) < 50:
                empty += 1
            name = f"{printed:04d}.txt" if printed >= 1 else f"fm_{pdf_page:03d}.txt"
            label = f"printed p. {printed}" if printed >= 1 else "front matter"
            header = f"[{book['title']} | {label} | pdf p. {pdf_page}]\n\n"
            (out / name).write_text(header + text, encoding="utf-8")
        lines = [f"{book['title']}\nprinted page = pdf page - {offset}\n"]
        for level, title, pdf_page in doc.get_toc():
            printed = pdf_page - offset
            where = f"p. {printed}" if printed >= 1 else f"front matter (pdf p. {pdf_page})"
            lines.append(f"{'  ' * (level - 1)}{title}  ..  {where}")
        (out / "_toc.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
        print(f"{key}: {len(doc)} pages -> {out} ({empty} pages with little or no text)")


if __name__ == "__main__":
    main()
