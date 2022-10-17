frac.ttl:
	@# extract frac.ttl from draft spec
	python3 md2ttl.py ../index.md > frac.ttl
	if rapper -i turtle frac.ttl -o turtle > /dev/null; then \
		echo frac.ttl is syntactically valid 1>&2; \
	fi