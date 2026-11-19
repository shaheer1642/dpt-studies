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
  prompts/          reusable briefs for answer-writing and graph-building tasks
  tools/            scripts (extract_books.py, merge_book_concepts.py)
graphify-out/       knowledge graph of Lippincott + the study files (see below)
```

## Knowledge graph (graphify)

`graphify-out/` holds a graph built on 2026-11-19 from Lippincott pp. 1–850
plus the past papers, answers and notes. **Katzung is not in it yet.**

- It is a map for finding where a topic is, not a source. Use it to find
  Lippincott pages and related concepts, then open those pages and cite them,
  and still search Katzung's text as usual.
- Each concept is one node, `concept_<name>` (e.g. `concept_propranolol`), with
  `pages` = the printed Lippincott pages it appears on. Edges carry a `kind`
  (mechanism, use, adverse_effect, contraindication, interaction, ...). Exam
  questions are nodes linked to the concepts they ask about.
- Query: `graphify query "<question>"`, or load `graph.json` and look a
  concept up directly. `graph.html` shows communities only (graph is over
  graphify's 5,000-node view limit).
- Figure and summary-table pages (e.g. pp. 342–343) were extracted thinly;
  study-question pages and blank pages have no nodes.

Rebuilding or adding Katzung:

- graphify is told to ignore `.gitignore` here
  (`graphify-out/.graphify_build.json`), because the book text it must read is
  git-ignored. Scope is set in `.graphifyignore`; Katzung is excluded there.
- Give extraction subagents graphify's standard prompt plus
  `pharmacology/prompts/graphify-extraction-notes.md`.
- graphify does not merge the same concept across pages. After graphify's
  Part C, run `$(cat graphify-out/.graphify_python) pharmacology/tools/merge_book_concepts.py`
  before building, and stamp the manifest from the pre-merge extraction.
- At most 20 subagents run at once. Check every batch afterwards: some
  subagents skipped the last page of a 24-page list, and many reported
  estimated rather than exact line counts in `coverage`.
- Cost: Lippincott took about 4.4M subagent tokens on Sonnet 5.5 (38 batches).
  Katzung is about 2.3 times as much text.

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

- Size answers for full marks. The student found 150–250 / 400–600 words too
  short (2026-11-19). Now: a 5–6-mark short question fills its 25 lines, about
  250–350 words plus a table or diagram; a 15-mark long question is about
  800–1,100 words under headings that follow the question's parts; an
  "up to 5 lines" sub-part is 50–80 words.
- Briefs for answer sheets: `pharmacology/prompts/answer-sheet.md` (reusable,
  one paper per PDF).
- Safety classifier stops: writing answers on organophosphate poisoning was
  stopped (Annual 2023), and so was one skeletal muscle relaxant answer. Do
  not reword or retry stopped content; leave that question with a note giving
  the book pages to read. The brief says how.
- Answer what was asked, in the order asked: enumerate, classify, tabulate.
- Plain English, short bullets, the books' own drug names.
- Past-paper transcriptions keep the paper's wording as printed, mistakes
  included, and mark anything unreadable instead of guessing.
