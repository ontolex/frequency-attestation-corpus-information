# Regenerate frac.ttl from the RDFa markup in ../index.md.
# Requires pandoc, python3-bs4 and raptor2-utils (see ../README.md).
frac.ttl: ../index.md ../respec.template ../expand_tags.py ../extract-ontology.sh
	cd .. && ./extract-ontology.sh owl/frac.ttl
