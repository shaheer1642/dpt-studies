# Studies

Study material for a 3rd-year DPT (Doctor of Physical Therapy) student. Work here
is exam preparation: transcribing past papers, writing model answers, making
revision notes. Currently one subject, `pharmacology/`.

## Sourcing rule

Answers and notes come **only from the textbooks in `pharmacology/books/`**:

- **Lippincott** — Lippincott Illustrated Reviews: Pharmacology, South Asian Edition
- **Katzung** — Basic & Clinical Pharmacology, 14th ed. (2018)

Find the passage first, then write from it. Do not write from memory and attach
a page afterwards.

- Every answer carries a source line: book, chapter, printed page numbers.
- A point that is in neither book is still included when the answer needs it,
  and is tagged `[not in book]` right on that point.
- If a whole question is not covered by the books, say so at the top of the
  answer.
- Other files in `pharmacology/` (earlier answer PDFs, exam notes) are not
  sources.
- Use Lippincott as the base (simpler, exam-style) and Katzung to fill gaps.

## Layout

```
pharmacology/
  books/            the two textbook PDFs
  books/text/       extracted text, one file per page (generated)
  past papers/      exam papers: photos and their .txt transcriptions
  answers/          model answers: HTML source and rendered PDF
  prompts/          reusable briefs for answer-writing tasks
  tools/            scripts (extract_books.py)
```

## Searching the books

The PDFs are 880 and 1264 pages, too large to read directly. Use the extracted
text in `pharmacology/books/text/<lippincott|katzung>/`:

- Files are named by **printed** page number, zero-padded: `katzung/0387.txt`.
  That is the number to cite.
- `_toc.txt` in each folder lists chapters with printed start pages.
- `grep -rli "term" pharmacology/books/text/lippincott` lists pages mentioning a
  term.
- Figure and table text comes out in reading order with columns interleaved,
  and Katzung's equations are images, so they are missing from the text. To see
  the real page, render it to an image with PyMuPDF
  (`doc[pdf_page - 1].get_pixmap(dpi=110).save(...)`) and read the image.
  **PDF page = printed page + 14 (Katzung) or + 17 (Lippincott).** The Read
  tool's `pages` option does not work here: it needs poppler, which is not
  installed.
- Lippincott's summary figures hold the most exam-shaped content (routes of
  administration Fig. 1.19, drug lists, adverse-effect and contraindication
  figures). Check them as images; do not rely on the extracted text alone.
- `grep` on this machine is ugrep and rejects long `.{0,150}`-style context
  patterns. For text with context, use `grep -rli` to find pages and Python to
  print the surrounding text.
- Iontophoresis and phonophoresis, which the DPT papers ask about, are
  effectively absent from both books (one passing mention, Katzung p. 115).
- To regenerate: `.venv/bin/python pharmacology/tools/extract_books.py`

## Tools on this machine

- `.venv/` at the repo root has PyMuPDF (`import pymupdf`). If it has to be
  reinstalled, use `pip install --only-binary=:all: pymupdf`; building from
  source fails here.
- No `pdftotext`, `pandoc` or `reportlab`. Make PDFs by writing HTML and
  rendering with headless Chrome:

  ```
  "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --disable-gpu \
    --no-pdf-header-footer --print-to-pdf="out.pdf" "file:///abs/path/in.html"
  ```

- After rendering, turn the PDF pages into images with PyMuPDF and look at them
  before calling it done.
- Chrome honours `break-inside: avoid` on tables, list items and sections, but
  not `break-after: avoid` on a table header row. Make a table unbreakable or
  let it break; do not count on keeping its header with the first row.

## Writing answers

- Size answers to the marks: a 5-mark short question is about 25 handwritten
  lines (150 to 250 words); a 15-mark long question is 400 to 600 words under
  headings that follow the question's parts.
- Answer what was asked, in the order asked: enumerate, classify, tabulate.
- Plain English, short bullets, the books' own drug names.
- Past-paper transcriptions keep the paper's wording as printed, mistakes
  included, and mark anything unreadable instead of guessing.
