# OntoLex-FrAC

Working draft of an OntoLex module for **Fr**equency, **A**ttestations and
**C**orpus data (FrAC). FrAC complements the OntoLex-Lemon core model with a
vocabulary for expressing corpus-derived information (frequency, collocation,
attestations) about lexical resources.

The current draft is [`index.md`](index.md) (Markdown source; this is the
file to edit — [edit it directly on GitHub](https://github.com/ontolex/frequency-attestation-corpus-information/edit/master/index.md)).
The rendered specification is published at
https://ontolex.github.io/frequency-attestation-corpus-information/, built
automatically by a GitHub Action on every push to `master`
(see `.github/workflows/publish.yaml`).

This page supersedes the original repository under
https://github.com/acoli-repo/ontolex-frac.

[comment]: See https://www.w3.org/community/ontolex/wiki/Frequency,_Attestation_and_Corpus_Information for the discussions on and behind this draft within the W3C Ontolex community group.

[comment]: See [FrAC meeting minutes](https://docs.google.com/document/d/1N2w_r6WLhFGESSMSUkG5FSROorXscDMQuB77qg9uDIA/edit) for most recent updates (not reflected on GitHub yet), and the [FrAC minutes archive](https://www.w3.org/community/ontolex/wiki/Frequency,_Attestation_and_Corpus_Information) for older minutes

## Building the specification

The specification uses [ReSpec](https://respec.org/docs/) and is generated
from `index.md` with [Pandoc](https://pandoc.org/); the diagrams of the
examples are then added by `add_diagrams.py`, which needs Python's
[`rdflib`](https://rdflib.readthedocs.io/):

```bash
sudo apt-get install pandoc python3-rdflib
pandoc --template respec.template -f markdown-auto_identifiers --wrap=none index.md -o index.html
python3 add_diagrams.py index.html index.html
```

Open `index.html` in a browser (or push to `master`) to see the rendered,
ReSpec-processed page. The listings in `index.md` are the source of the
examples: after changing one, run `python3 extract_examples.py`, which writes
the files in `examples/` from them. The GitHub Action runs the same steps,
after checking that the example files are up to date
(`extract_examples.py --check`) and that `owl/frac.ttl` matches the
specification; it also runs on pull requests.

## The ontology (RDFa)

Unlike most OntoLex modules, the `frac:` ontology itself isn't maintained as
a separate hand-written file — it's authored as [RDFa](https://www.w3.org/TR/rdfa-primer/)
directly inside `index.md`'s `<div class="entity" about="frac:X" typeof="owl:Class">`
blocks (one per class/property, each with an `rdfs:label` and `rdfs:comment`,
plus `<domain>`/`<range>`/`<subclass>`/`<superclass>`/`<subproperty>`/`<functional/>` shorthand
tags for axioms), following the same process used in the sister
[`ontolex`](https://github.com/ontolex/ontolex) repository. `index.md` is the
single source of truth — don't hand-edit an extracted ontology file and
expect it to stay in sync.

Extracting the ontology takes two extra steps beyond the plain HTML build
above, because a couple of tools are involved:

### 1. Install the extra dependencies

- **`expand_tags.py`** (turns the shorthand `<domain>`/`<range>`/etc. tags into
  real RDFa spans) needs Python's `beautifulsoup4`. On a system with an
  "externally managed" Python (Debian/Ubuntu, most modern distros), `pip
  install beautifulsoup4` will refuse to run — install the distro package
  instead:
  ```bash
  sudo apt-get install python3-bs4
  ```
  (If you're not on a Debian-based system, or don't want to touch system
  Python packages, use a virtualenv instead:
  `python3 -m venv .venv && .venv/bin/pip install beautifulsoup4`, then run
  `expand_tags.py` with `.venv/bin/python3`.)
- **`rapper`** (extracts RDFa into Turtle) comes from the Raptor RDF library:
  ```bash
  sudo apt-get install raptor2-utils
  ```

### 2. Run the pipeline

```bash
make -C owl          # regenerates owl/frac.ttl
# or, to write somewhere else:
./extract-ontology.sh path/to/frac.ttl
```

[`extract-ontology.sh`](extract-ontology.sh) runs the three steps in order —
`pandoc`, then `expand_tags.py`, then `rapper` (with a `-f xmlns:PREFIX=...`
flag per namespace, so the output Turtle actually gets `@prefix` lines
instead of full URIs everywhere) — and writes the result to the path you
give it (`frac.ttl` if you don't specify one). Besides expanding the
shorthand tags, `expand_tags.py` replaces ReSpec `[=term=]` links in
`rdfs:comment`s with plain text and tags the comments `@en`, so the extracted
Turtle reads cleanly outside the rendered spec.

**Whenever you change an entity block in `index.md`, regenerate
`owl/frac.ttl` and commit it in the same change**, so the published Turtle
never drifts from the spec. A quick check that they agree:

```bash
./extract-ontology.sh /tmp/frac.ttl && diff owl/frac.ttl /tmp/frac.ttl
```

**The `expand_tags.py` step is required, not optional** — running `rapper`
directly on Pandoc's raw HTML output will fail. Pandoc's HTML5 output isn't
guaranteed to be well-formed XML (e.g. bare boolean attributes, or tags that
a lenient HTML5 parser tolerates but a strict XML parser won't), and
`rapper`'s RDFa parser requires strict XML. Parsing the file with
BeautifulSoup and re-serializing it (which is what `expand_tags.py` does,
on top of expanding the shorthand tags) normalizes it into well-formed XML
along the way. If you skip straight to `rapper` you'll typically see errors
like:
```
rapper: Error -  - XML parser error: Opening and ending tag mismatch: ...
```

## The ontology file (`owl/frac.ttl`)

[`owl/frac.ttl`](owl/frac.ttl) is the generated output of the pipeline
above, committed so that the ontology can be downloaded or dereferenced
without building anything. Don't edit it by hand — edit `index.md` and
regenerate it. (It used to be maintained by hand, most recently reconciled
in [#72](https://github.com/ontolex/frequency-attestation-corpus-information/issues/72),
but it drifted again with the class renames in #74, so it is now generated.)

## Diagram

The overview diagram in the spec is [`img/FrAC.drawio.png`](img/FrAC.drawio.png)
(vector version: [`img/FrAC.svg`](img/FrAC.svg)); both can be edited with
[draw.io](https://app.diagrams.net/). The `img/*.puml` PlantUML files and
other dated images in `img/` are diagrams of earlier drafts, kept for
reference.

## Repository layout

- [`index.md`](index.md) — the spec source (edit this).
- [`respec.template`](respec.template) — Pandoc template that wraps `index.md` in the ReSpec HTML shell.
- [`expand_tags.py`](expand_tags.py) — expands the shorthand ontology tags into RDFa; see "The ontology (RDFa)" above.
- [`extract-ontology.sh`](extract-ontology.sh) — runs the full build + extraction pipeline; see "The ontology (RDFa)" above.
- [`examples/`](examples/) — the spec's examples as Turtle files, generated from `index.md`; [`add_diagrams.py`](add_diagrams.py), [`mermaid_lib.py`](mermaid_lib.py) draw their diagrams, and [`extract_examples.py`](extract_examples.py) writes them from the listings in the spec.
- [`owl/frac.ttl`](owl/frac.ttl) — the ontology in Turtle, generated from `index.md` (see above).
- [`public-review-1.md`](public-review-1.md), [`index-old.md`](index-old.md), [`archive/`](archive/) — earlier drafts, kept for reference.
- [`samples/`](samples/) — example datasets modelled with FrAC.
- [`doc/`](doc/) — slides and papers from FrAC presentations.
- [`img/`](img/) — diagrams used in the spec.
