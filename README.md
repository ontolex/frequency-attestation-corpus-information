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
from `index.md` with [Pandoc](https://pandoc.org/):

```bash
sudo apt-get install pandoc
pandoc --template respec.template -f markdown-auto_identifiers --wrap=none index.md -o index.html
```

Open `index.html` in a browser (or push to `master`) to see the rendered,
ReSpec-processed page.

## The ontology (RDFa)

Unlike most OntoLex modules, the `frac:` ontology itself isn't maintained as
a separate hand-written file — it's authored as [RDFa](https://www.w3.org/TR/rdfa-primer/)
directly inside `index.md`'s `<div class="entity" about="frac:X" typeof="owl:Class">`
blocks (one per class/property, each with an `rdfs:label` and `rdfs:comment`,
plus `<domain>`/`<range>`/`<subclass>`/`<subproperty>`/`<functional/>` shorthand
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

### 2. Run the pipeline, in order

```bash
pandoc --template respec.template -f markdown-auto_identifiers --wrap=none index.md -o index.html
python3 expand_tags.py index.html index.html
rapper -i rdfa -o turtle index.html > frac.ttl
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

`rapper` will also print a `Warning: skipping <domain> tag, could not
expand: ...` for `frac:total`'s `<domain>` — that one's expected: its
domain is described in prose ("any potential FrAC data source ... or any
other member of DCMI Type") that the tag's simple mini-language can't
express, so it's deliberately left as unparsed text rather than given a
formal (and less precise) `rdfs:domain`.

## Older ontology snapshot (`owl/`)

`owl/frac.ttl` is a separate, older, hand-maintained ontology file, built by
concatenating every ` ``` `-fenced Turtle block in `index.md` (see
`owl/md2ttl.py` / `owl/Makefile`). It predates the RDFa-based process above
and has drifted out of sync with the current `index.md` (e.g. it still
references properties that have since been renamed or removed). It's kept
for reference for now; the RDFa extraction above is the more accurate,
lower-maintenance way to get the current ontology.

## Diagram

At the moment, this is done as UML diagram [edit [here](https://github.com/ontolex/frequency-attestation-corpus-information/edit/master/img/diagram.puml)] using the [PlantText editor](https://www.planttext.com/):

![](http://www.plantuml.com/plantuml/proxy?src=https://raw.githubusercontent.com/ontolex/frequency-attestation-corpus-information/master/img/diagram-with-observation-compact.puml?cache=no)

## Repository layout

- [`index.md`](index.md) — the spec source (edit this).
- [`respec.template`](respec.template) — Pandoc template that wraps `index.md` in the ReSpec HTML shell.
- [`expand_tags.py`](expand_tags.py) — expands the shorthand ontology tags into RDFa; see "The ontology (RDFa)" above.
- [`owl/`](owl/) — older, separately-maintained ontology snapshot (see above).
- [`samples/`](samples/) — example datasets modelled with FrAC.
- [`doc/`](doc/) — slides and papers from FrAC presentations.
- [`img/`](img/) — diagrams used in the spec.
