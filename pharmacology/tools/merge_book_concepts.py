"""Join same-named concepts across files in a graphify extraction.

graphify's extraction gives every node an ID prefixed with its source file, so
"Propranolol" found on Lippincott pages 170, 172 and 317 arrives as three
separate nodes, and graphify's default build never merges them. For a textbook
that defeats the point of the graph. This step runs between graphify's Part C
(which writes .graphify_extract.json) and Step 4 (build and cluster):

    $(cat graphify-out/.graphify_python) pharmacology/tools/merge_book_concepts.py

It merges every `concept` / `rationale` node that shares a normalised label
(case, hyphens, Greek letters, a trailing bracket and a plural "s" are
ignored) into one node with ID `concept_<label>`, and records:

    pages         printed Lippincott pages the concept appears on (sorted)
    source_files  every file it was extracted from
    rationale     the distinct "why" notes, joined with " | "

Edges and hyperedges are rewired to the merged nodes; self-loops are dropped
and duplicate edges collapsed (highest confidence kept, `count` recorded).
Document nodes (files, figures, exam questions) are left as they are.

The unmerged extraction is saved as .graphify_extract_premerge.json; use that
file, not the merged one, when stamping graphify's manifest (Step 9), so every
page that produced nodes is recorded as extracted.
"""
import json
import re
import shutil
import sys
from collections import Counter, defaultdict
from pathlib import Path

OUT = Path("graphify-out")
EXTRACT = OUT / ".graphify_extract.json"
PREMERGE = OUT / ".graphify_extract_premerge.json"
MERGE_TYPES = {"concept", "rationale"}
GREEK = {"β": "beta", "α": "alpha", "γ": "gamma", "δ": "delta", "κ": "kappa", "μ": "mu"}
PAGE_RE = re.compile(r"/lippincott/(\d{4})\.txt$")


def singular(word):
    if len(word) <= 3 or word.endswith(("ss", "us", "is")):
        return word
    if word.endswith("ies"):
        return word[:-3] + "y"
    if word.endswith("s"):
        return word[:-1]
    return word


def norm(label):
    s = label.strip().lower()
    for g, name in GREEK.items():
        s = s.replace(g, f" {name} ")
    s = re.sub(r"\s*\([^)]*\)\s*$", "", s)          # trailing "(INH)", "(Inderal)"
    s = s.replace("'", "").replace("’", "")
    s = re.sub(r"[^a-z0-9]+", " ", s).strip()
    words = s.split()
    if not words:
        return ""
    words[-1] = singular(words[-1])
    return " ".join(words)


def page_of(source_file):
    m = PAGE_RE.search(source_file or "")
    return int(m.group(1)) if m else None


def main():
    data = json.loads(EXTRACT.read_text(encoding="utf-8"))
    if not PREMERGE.exists():
        shutil.copyfile(EXTRACT, PREMERGE)
    else:
        data = json.loads(PREMERGE.read_text(encoding="utf-8"))   # idempotent re-run

    nodes, edges = data.get("nodes", []), data.get("edges", [])
    hyperedges = data.get("hyperedges", [])

    groups = defaultdict(list)
    kept = []
    for n in nodes:
        key = norm(n.get("label") or "") if n.get("file_type") in MERGE_TYPES else ""
        if key:
            groups[key].append(n)
        else:
            kept.append(n)

    remap = {}
    merged = []
    for key, members in groups.items():
        new_id = "concept_" + key.replace(" ", "_")
        labels = Counter(m["label"].strip() for m in members)
        files = sorted({m.get("source_file") for m in members if m.get("source_file")})
        pages = sorted({p for p in map(page_of, files) if p is not None})
        rationales = []
        for m in members:
            r = (m.get("rationale") or "").strip()
            if r and r not in rationales:
                rationales.append(r)
        node = {
            "id": new_id,
            "label": labels.most_common(1)[0][0],
            "file_type": "concept" if any(m.get("file_type") == "concept" for m in members) else "rationale",
            "source_file": next((f for f in files if page_of(f) is not None), files[0] if files else None),
            "source_location": ("pp. " + ", ".join(map(str, pages))) if pages else members[0].get("source_location"),
            "pages": pages,
            "source_files": files,
            "_origin": "semantic",
        }
        if rationales:
            node["rationale"] = " | ".join(rationales)
        merged.append(node)
        for m in members:
            remap[m["id"]] = new_id

    best = {}
    for e in edges:
        e = dict(e)
        e["source"] = remap.get(e["source"], e["source"])
        e["target"] = remap.get(e["target"], e["target"])
        if e["source"] == e["target"]:
            continue
        k = (e["source"], e["target"], e.get("relation"), e.get("kind"))
        if k in best:
            prev = best[k]
            prev["count"] = prev.get("count", 1) + 1
            if (e.get("confidence_score") or 0) > (prev.get("confidence_score") or 0):
                e["count"] = prev["count"]
                best[k] = e
        else:
            best[k] = e
    new_edges = list(best.values())

    new_hyper = []
    for h in hyperedges:
        h = dict(h)
        members = []
        for nid in h.get("nodes", []):
            nid = remap.get(nid, nid)
            if nid not in members:
                members.append(nid)
        if len(members) >= 3:
            h["nodes"] = members
            new_hyper.append(h)

    data["nodes"] = kept + merged
    data["edges"] = new_edges
    data["hyperedges"] = new_hyper
    EXTRACT.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")

    joined = sum(1 for g in groups.values() if len(g) > 1)
    print(f"nodes {len(nodes)} -> {len(data['nodes'])} "
          f"({len(groups)} concepts, {joined} joined from 2+ nodes); "
          f"edges {len(edges)} -> {len(new_edges)}; hyperedges {len(hyperedges)} -> {len(new_hyper)}")
    top = sorted(merged, key=lambda n: len(n["pages"]), reverse=True)[:12]
    print("most widely mentioned:", ", ".join(f"{n['label']} ({len(n['pages'])} pp.)" for n in top))


if __name__ == "__main__":
    sys.exit(main())
