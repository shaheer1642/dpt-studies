# Brief: model answer sheet for one pharmacology past paper, as a PDF

Reusable. The task message that points you here names the paper, the output
file names, and anything specific to that paper. Read this whole brief, then
`/Users/macbook/Documents/GitHub/studies/CLAUDE.md`, before starting.

## Who it is for

A 3rd-year DPT (Doctor of Physical Therapy) student revising for the
university pharmacology exam (Paper VI, Pharmacology & Therapeutics). They
will learn these answers and write them out by hand in the exam, so each
answer must be complete enough to score full marks, laid out the way an
examiner expects, and every fact must be one they can find in their textbook.

## The rule that matters most: only the two books

Answers come only from **Lippincott** (Illustrated Reviews: Pharmacology, South
Asian Edition) and **Katzung** (Basic & Clinical Pharmacology, 14th ed.).
Find the passage first, then write from it. Do not write from memory and
attach a page afterwards: correct pharmacology that neither book states is
exactly the error the student cannot detect.

- Every answer has a source line: book, chapter, printed page numbers used.
- Put a short page mark after each point or table row (`L 317`, `K 712`).
- Anything you include that is in neither book gets a visible `[not in book]`
  tag on that point. Include it when the answer needs it; the student prefers
  a complete answer with honest tags to a gap.
- If a whole question or part is not covered, say so in a note at the top of
  that answer.
- Applying the book's facts to an exam scenario (a farmer, an athlete) is
  fine untagged. Tag only facts missing from the books.
- Lippincott is the base; add Katzung where Lippincott is thin.
- Not sources: the earlier answer PDFs and exam notes in `pharmacology/`.
  The one exception: `pharmacology/answers/past-paper-answers.html` was
  written from the books with page citations, so you may use a matching
  answer there as a starting draft. Re-check its citations against the pages
  and expand it to the length below.

## Length: long enough for full marks

The student asked for answers long enough from an exam point of view. The
earlier sheet was too short. Aim for:

- **Short question (5 or 6 marks, "up to 25 lines"):** fill the 25 lines.
  About 250–350 words, plus a table or a labelled diagram where it helps.
  Cover every part the question asks, with a definition, the classification
  or mechanism, examples with drug names, and the clinical point.
- **Long question (15 marks):** about 800–1,100 words, under headings that
  follow the question's own parts and mark split, with more where more marks
  are. Include a classification table, mechanism, uses, adverse effects
  (grouped by system), and contraindications or interactions where relevant.
- **"Up to 5 lines" sub-parts:** about 50–80 words each, direct.

Length is not padding: more correct, cited content, organised so an examiner
can tick it. When the books have more on the topic than this, include the
exam-relevant part, not everything.

## Format of each answer

Answer what was asked, in the order asked. "Enumerate" means a list;
"classify" means a classification with example drugs; "tabulated form" or
"compare" means a table; "with help of diagram" means draw one (inline SVG,
labelled, simple enough to reproduce by hand). Plain English, short bullets,
the books' drug names. Define a term the first time it appears.

Repeated topics: if this paper repeats a question answered elsewhere in the
same sheet, answer it fully once and point back. Do not point to other PDFs;
each sheet must stand on its own.

## How to find things in the books

- Text, one file per printed page:
  `pharmacology/books/text/lippincott/0317.txt`, `.../katzung/0712.txt`;
  `_toc.txt` in each folder lists chapters.
- Knowledge graph (Lippincott only): `graphify query "<topic>"` from the repo
  root, or load `graphify-out/graph.json` and look up `concept_<name>`; its
  `pages` attribute lists every Lippincott page it appears on, and edges carry
  a `kind` (mechanism, use, adverse_effect, ...). It is a map: open and read
  the pages it points to before writing. Search Katzung's text with grep.
- Figures and tables come out garbled in the text. For one you rely on,
  render the page with PyMuPDF and look at it
  (`/Users/macbook/Documents/GitHub/studies/.venv/bin/python`,
  `import pymupdf`; PDF page = printed page + 17 Lippincott, + 14 Katzung).
  The Read tool's `pages` option does not work on this machine.
- `grep` here is ugrep: no long `.{0,150}` context patterns; use Python to
  print context.

## The PDF

- Write one standalone HTML file and render it with headless Chrome (command
  in CLAUDE.md). Save both in `pharmacology/answers/` under the names given
  in the task message.
- Match the look of `pharmacology/answers/past-paper-answers.html` (reuse its
  CSS): A4, opening "Read this first" note (sources, printed page numbers,
  the `[not in book]` tag), each question shown in full above its answer with
  marks and source line, red `[not in book]` pills, and a final page listing
  every tagged point by question.
- Title it with the paper name. If the paper has known transcription doubts
  (see the task message), say so in one line in the opening note.
- Chrome honours `break-inside: avoid` on tables, list items and sections, not
  `break-after: avoid` on a header row. Long answers may span pages; keep a
  question's heading with the start of its answer.

## Check before you finish

1. **Sourcing.** Re-read every answer against the page files you cited. Each
   untagged point must be on a cited page; fix the citation, tag it, or cut
   it. Cited numbers are printed page numbers.
2. **Length.** Count words per answer and compare with the targets above.
3. **Rendering.** Render every PDF page to an image with PyMuPDF and look at
   it: tables off the page, broken symbols (Na⁺, β, H₂), orphaned headings,
   unreadable tags, diagrams that did not render.

Scratch files go in the scratchpad directory named in the task message, never
in the repository.

## If a safety classifier stops your output

This has happened on organophosphate poisoning (antidotes) and on one skeletal
muscle relaxant answer. Do not reword or retry that content. Show the question
as usual with only a note in place of the answer, naming the book pages to
read (e.g. "Answer not included in this sheet. Read Lippincott pp. 127–128 …
for this question."), keep that topic out of the rest of the sheet, finish the
other questions, and list the question in your report. Writing the HTML in
several smaller files (one per question, assembled at the end) also keeps one
stopped answer from losing the whole sheet.

## Report back

Your report goes to the agent that briefed you. Keep it factual:

- Output paths and PDF page count.
- A table of every question: word count, sources (book and printed pages),
  and anything tagged `[not in book]`.
- What you verified against page text or page images, and what you did not.
- Points where the books disagree, and doubts about the paper's transcription.
- Whether the three checks ran and what they found.
