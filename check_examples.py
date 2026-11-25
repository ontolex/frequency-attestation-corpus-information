"""Check that every example listing in index.md matches its Turtle file.

Each `<aside class="example" src="examples/NAME.ttl">` in index.md contains
an inline ```turtle listing (what readers see) and points at a Turtle file
(what the diagram is generated from, and what people download). This checks
that, for every such example, the listing and the file describe the same
graph, so the two cannot silently drift apart.

The listing is parsed with the file's @prefix declarations prepended, since
the listings in the spec rely on the namespaces declared at its start.

Usage: python3 check_examples.py [index.md]    (exit status 1 on mismatch)
"""
import re
import sys

from rdflib import Graph
from rdflib.compare import isomorphic, to_isomorphic, graph_diff

ASIDE = re.compile(r'<aside\b[^>]*\bsrc="([^"]+)"[^>]*>(.*?)</aside>', re.S)
LISTING = re.compile(r"```turtle\n(.*?)```", re.S)
PREFIX = re.compile(r"^\s*@prefix\s[^\n]*$", re.M)


def parse(text, where):
    g = Graph()
    try:
        g.parse(data=text, format="turtle")
    except Exception as e:  # rdflib raises various parser exceptions
        raise SystemExit("%s: Turtle does not parse: %s" % (where, e))
    return g


def main(spec):
    with open(spec, encoding="utf-8") as f:
        text = f.read()
    failures = 0
    asides = ASIDE.findall(text)
    for src, body in asides:
        listings = LISTING.findall(body)
        if len(listings) != 1:
            print("%s: expected one ```turtle listing in its aside, found %d" % (src, len(listings)))
            failures += 1
            continue
        with open(src, encoding="utf-8") as f:
            file_text = f.read()
        header = "\n".join(PREFIX.findall(file_text))
        g_file = parse(file_text, src)
        g_listing = parse(header + "\n" + listings[0], "listing for " + src)
        if not isomorphic(g_file, g_listing):
            failures += 1
            _, only_file, only_listing = graph_diff(to_isomorphic(g_file), to_isomorphic(g_listing))
            print("%s: listing in %s differs from the file" % (src, spec))
            for s, p, o in sorted(only_file):
                print("  only in file:    %s %s %s" % (s.n3(), p.n3(), o.n3()))
            for s, p, o in sorted(only_listing):
                print("  only in listing: %s %s %s" % (s.n3(), p.n3(), o.n3()))
    print("Checked %d examples, %d mismatches" % (len(asides), failures), file=sys.stderr)
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "index.md"))
