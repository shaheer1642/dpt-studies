# Brief: answer two pharmacology past papers from the textbooks, as one PDF

## Who this is for and what it is for

The reader is a 3rd-year DPT (Doctor of Physical Therapy) student revising for a
university pharmacology exam (Paper VI, Pharmacology & Therapeutics). They will
study from the PDF you produce and reproduce these answers by hand in the exam.
So each answer has to be something a student can learn and write out in the time
and space the exam allows, and every fact in it has to be one they can trust and
look up in their own textbook.

## The task

Write model answers to every question in both past papers and deliver them as a
single PDF.

The papers (plain text, read both first):

- `/Users/macbook/Documents/GitHub/studies/pharmacology/past papers/pharmacology-paper-VI-section-II.txt`
  Annual exam, year cut off in the photo, paper code LK-1387. 8 short questions
  (5 marks each, "upto 25 lines maximum") and 3 long questions (15 marks each,
  mark splits printed on the paper).
- `/Users/macbook/Documents/GitHub/studies/pharmacology/past papers/annual 2024.txt`
  Annual 2024. 10 short and 3 long questions. No marks are given; assume the
  same pattern (5 marks short, 15 marks long).

Answer all 24 questions, including the long questions the paper lets candidates
choose between. The student wants every one covered.

## The one rule that matters most: only the two books

The student asked for answers drawn only from these two textbooks:

- **Lippincott** — Lippincott Illustrated Reviews: Pharmacology, South Asian Edition
- **Katzung** — Basic & Clinical Pharmacology, 14th ed. (2018)

Do not answer from your own memory of pharmacology and then look for a page to
attach. Find the passage first, then write the answer from what the page says.
Your recall of these subjects is good, which is exactly why this is the easy
place to go wrong: an answer can be correct pharmacology and still contain
points that neither book makes. The student cannot tell the difference unless
you tell them.

So, for every answer:

- Give a source line: book, chapter, and the printed page numbers you actually
  used.
- Anything you include that you could not find in either book gets a visible
  `[not in book]` tag on that point. Still include it when the question cannot
  be answered properly without it. The student would rather have a complete
  answer with honest tags than a gap.
- If a whole question, or a whole part of one, is not covered by the books, say
  so in a short note at the top of that answer before answering.
- Where the book gives the facts but does not discuss the exam's scenario (for
  example a book that describes a drug's effects but never mentions athletes),
  apply the book's facts to the scenario and cite them. That is fine untagged.
  Tag only the facts themselves that are missing from the books.

Expect some questions to be thin or absent in the books. Iontophoresis is the
known case: it appears on one page of Katzung (p. 115) and nowhere in
Lippincott, and phonophoresis appears in neither. Those questions (long Q.3 in
the LK-1387 paper on transcutaneous penetration techniques, long Q.3 in the 2024
paper) are physical-therapy topics. Search for what the books do have (the
transdermal and oral routes in the pharmacokinetics chapters, percutaneous
absorption in Katzung's dermatology chapter) and tag the rest.

When the two books disagree or one is more detailed, use Lippincott as the base,
since it is the simpler exam-style text, and add from Katzung where Lippincott
is thin. Cite whichever you used.

Do not use any other file in the `pharmacology/` folder as a source. The existing
answer PDFs and exam notes there are off limits for content.

## How to search the books

Both books are already extracted to text, one file per page, named by the
**printed** page number (the number to cite):

- `/Users/macbook/Documents/GitHub/studies/pharmacology/books/text/lippincott/0001.txt` … `0864.txt`
- `/Users/macbook/Documents/GitHub/studies/pharmacology/books/text/katzung/0001.txt` … `1250.txt`
- `_toc.txt` in each folder lists chapters with printed start pages. Start there.

`grep -rli "term" <folder>` returns the pages that mention a term; then read
those page files. Each book's index is also in the text (Katzung from p. 1183,
Lippincott from p. 851).

Tables and figures are sometimes garbled or missing in the extracted text, and
Katzung's equations are images. When a page file looks incomplete around a
table or figure you need, render that page of the PDF to an image with PyMuPDF
and read the image. (The Read tool's `pages` option does not work on this
machine; poppler is not installed.) PDF page = printed page + 14 for Katzung,
+ 17 for Lippincott. The PDFs are in
`/Users/macbook/Documents/GitHub/studies/pharmacology/books/`.

A Python environment with PyMuPDF is at
`/Users/macbook/Documents/GitHub/studies/.venv/bin/python` (`import pymupdf`).

## What a good answer looks like

- Sized to the marks. A short question is about what fits in 25 handwritten
  lines: roughly 150 to 250 words. A long question is roughly 400 to 600 words,
  split under headings that follow the question's own parts and mark split, with
  more written where more marks are.
- Answer the question that was asked, in the order it asks. If it says
  "enumerate", list. If it says "classify", give the classification with example
  drugs. If it asks for a table ("in tabulated form"), give a table. Comparisons
  (phase I versus phase II) read best as a table too.
- Plain, simple English in short bullet points. Define a term the first time it
  appears. This is a student writing under time pressure, not a reference text.
- Use the books' own drug names and terminology so the student can find the
  passage.

Several questions appear in both papers (biotransformation, loading dose,
corticosteroid adverse effects, iontophoresis). Write the full answer where the
question first appears. At the repeat, do not paste it again: point back to it,
add whatever the second wording asks for that the first did not, and mark the
question as asked in both papers, since a repeated question is one the student
should prioritise.

## The PDF

- Write the answers as one HTML file and render it to PDF with headless Chrome:

  ```
  "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --disable-gpu \
    --no-pdf-header-footer --print-to-pdf="<out.pdf>" "file://<in.html>"
  ```

  This is tested and works on this machine (ignore the CVDisplayLink warning).
- Save both in `/Users/macbook/Documents/GitHub/studies/pharmacology/answers/`:
  `past-paper-answers.html` and `Pharmacology - Past Paper Answers.pdf`.
- A4, comfortable to read on a phone or printed. Open with a short note
  explaining the sourcing rule, how page numbers are cited (printed page
  numbers), and what the `[not in book]` tag means. Then the LK-1387 paper, then
  Annual 2024, each question shown in full above its answer with its source
  line.
- Make `[not in book]` tags easy to spot at a glance.
- End with a one-page list of everything tagged `[not in book]`, by question, so
  the student can check those points with a teacher.
- Write superscripts, subscripts and Greek letters properly (Na⁺, β, H₂).

## Check your work before you finish

Two checks, both of which change what you deliver if they fail:

1. **Sourcing.** After writing, go back through every answer against the page
   files you cited. Each untagged point should be traceable to a cited page.
   Fix the citation, tag the point, or remove it. Check that cited page numbers
   are printed page numbers and that they hold the content claimed.
2. **Rendering.** Render the finished PDF's pages to images with PyMuPDF and
   look at them. Check for tables running off the page, broken symbols, a
   question separated from its answer by a page break, and unreadable tags.

## What to report back

Your final message is read by the agent that briefed you, not by the student.
Keep it factual:

- Paths of the files you wrote and the PDF's page count.
- A table of all 24 questions: sources used (book and printed pages) and what,
  if anything, was tagged `[not in book]`.
- Anything you are unsure about: points where the books conflict, citations you
  could not fully confirm, places where the extracted text was unreadable. Say
  which claims you checked against the page text and which you did not.
- Whether both checks above were actually run, and what they found.
- Anything you learned about the books or the tooling that would save time on
  the next paper (useful chapters, extraction quirks, rendering problems).
