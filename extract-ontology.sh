#!/bin/sh
# Build index.html from index.md and extract the frac: ontology from its
# RDFa markup as Turtle. See "The ontology (RDFa)" in README.md for the
# individual steps and what each dependency is for.
#
# Usage: ./extract-ontology.sh [output.ttl]
#   (defaults to frac.ttl)

set -e

OUT="${1:-frac.ttl}"
HTML="$(mktemp --suffix=.html)"
trap 'rm -f "$HTML"' EXIT

pandoc --template respec.template -f markdown-auto_identifiers --wrap=none index.md -o "$HTML"
python3 expand_tags.py "$HTML" "$HTML"

rapper -i rdfa -o turtle \
  -f 'xmlns:frac="http://www.w3.org/ns/lemon/frac#"' \
  -f 'xmlns:ontolex="http://www.w3.org/ns/lemon/ontolex#"' \
  -f 'xmlns:synsem="http://www.w3.org/ns/lemon/synsem#"' \
  -f 'xmlns:decomp="http://www.w3.org/ns/lemon/decomp#"' \
  -f 'xmlns:vartrans="http://www.w3.org/ns/lemon/vartrans#"' \
  -f 'xmlns:lime="http://www.w3.org/ns/lemon/lime#"' \
  -f 'xmlns:lexicog="http://www.w3.org/ns/lemon/lexicog#"' \
  -f 'xmlns:lexinfo="http://www.lexinfo.net/ontology/3.0/lexinfo#"' \
  -f 'xmlns:dct="http://purl.org/dc/terms/"' \
  -f 'xmlns:oa="http://www.w3.org/ns/oa#"' \
  -f 'xmlns:dcam="http://purl.org/dc/dcam/"' \
  -f 'xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"' \
  -f 'xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"' \
  -f 'xmlns:owl="http://www.w3.org/2002/07/owl#"' \
  -f 'xmlns:xsd="http://www.w3.org/2001/XMLSchema#"' \
  -f 'xmlns:voaf="http://purl.org/vocommons/voaf#"' \
  "$HTML" > "$OUT"

echo "Wrote $OUT" >&2
