# Graphify extraction notes for this repo

Appended to graphify's standard extraction prompt (references/extraction-spec.md in the graphify
skill) for every extraction subagent when the Lippincott graph was built on 2026-11-19. Reuse them
when adding Katzung or re-extracting pages. The PDF path in note 8 pointed at a session scratch folder;
regenerate the extracted PDF text before reusing it.

```
PROJECT NOTES for this corpus (they add to the rules above; where they are
more specific, follow them):

1. What the corpus is. Pharmacology study material for a physical-therapy
   (DPT) student's exam. Most files are single pages of the textbook
   "Lippincott Illustrated Reviews: Pharmacology" (South Asian Edition),
   extracted to text. Each such file is named by the book's PRINTED page
   number: .../lippincott/0317.txt is page 317. `_toc.txt` is the chapter
   list. Page text can have figure labels and table cells out of order; read
   past that, and ignore running headers, page numbers and figure-credit
   lines.

2. What to extract. The pharmacology: drugs, drug classes, receptors and
   targets, mechanisms of action, clinical uses, adverse effects,
   contraindications, drug interactions, diseases and conditions treated,
   and pharmacokinetic/pharmacodynamic concepts. Give every one of these
   `file_type: "concept"`. Use "document" only for a node that stands for a
   file itself or for one of its sections or figures (e.g. "Figure 16.9").

3. Labels. Use the plain generic or concept name as the book writes it,
   without brand names or bracketed abbreviations: "Propranolol",
   "Beta-blockers", "Isoniazid", "Hypokalemia", "Loading dose". Always the
   same label for the same thing; a later step joins nodes across pages by
   label, so consistent labels are what connect the graph.

4. Edges. Keep to the allowed `relation` values. A drug `implements` its
   mechanism; use `conceptually_related_to` for drug-class membership, uses,
   adverse effects, contraindications and interactions. Also put a `kind`
   attribute on every edge, one of: is_a, mechanism, use, adverse_effect,
   contraindication, interaction, pharmacokinetics, other. Mark an edge
   EXTRACTED only when the page states it.

5. Rationale. Short "why" notes from the book (why a drug is contraindicated,
   why a dose is tapered) go in the `rationale` attribute of the concept node.

6. source_location. For a textbook page use the printed page, e.g. "p. 317"
   (add the figure or table number if the fact comes from one). For other
   files use the question number or heading.

7. Past papers and answer files (only in the study-files chunks). Make one
   node per exam question, `file_type: "document"`, labelled with the paper
   and question, e.g. "Annual 2024 Short Q.4: hydrochlorothiazide". Link each
   question with `references` edges (kind: other) to the concept nodes it asks
   about, using the same concept labels as rule 3.

8. PDFs (only in the study-files chunks). The Read tool cannot open PDFs on
   this machine. For a .pdf in FILE_LIST, read its extracted text instead, at
   /private/tmp/claude-501/-Users-macbook-Documents-GitHub-studies/dfecc426-ff96-4d72-af7a-fa85b5963a40/scratchpad/pdftext/<PDF file name without .pdf, trailing spaces trimmed>.txt
   Still use the .pdf path from FILE_LIST as source_file and in coverage.
```
