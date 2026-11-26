"""Insert a Mermaid diagram into each example of the built specification.

Every `<aside class="example" ... src="examples/NAME.ttl">` in the HTML
produced by Pandoc gets a `<pre class="mermaid">` diagram, generated from
that Turtle file, as its first child; the `src` attribute is removed. The
diagram is rendered in the browser by Mermaid (see respec.template).

Optional files next to the Turtle file adjust the diagram:
- NAME.LR: left-to-right layout
- NAME.elk: ELK layout engine (better edge-label placement)
- NAME.labels: labels shown instead of node names, one per line as
  `<IRI> label`; `*text*` is set in italics
- NAME.nodiagram: no diagram for this example (e.g. too complex to read)

Only the example asides are touched; the rest of the page is left exactly
as Pandoc wrote it.

Usage: python3 add_diagrams.py [--base DIR] input.html output.html
"""
import argparse
import html
import os
import re
import sys

from mermaid_lib import turtle_to_mermaid

ASIDE = re.compile(r'(<aside\b[^>]*?)\s+src="([^"]+)"([^>]*>)')


def read_labels(path):
    labels = {}
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            for line in f:
                m = re.match(r"\s*<([^>]+)>\s+(.+?)\s*$", line)
                if m:
                    labels[m.group(1)] = m.group(2)
                elif line.strip():
                    raise SystemExit("%s: expected `<IRI> label`, got: %s" % (path, line.rstrip()))
    return labels


def diagram_for(ttl_path):
    """The Mermaid source for an example, or None if it has no diagram."""
    stem = os.path.splitext(ttl_path)[0]
    if os.path.exists(stem + ".nodiagram"):
        return None
    with open(ttl_path, encoding="utf-8") as f:
        text = f.read()
    direction = "LR" if os.path.exists(stem + ".LR") else None
    elk = os.path.exists(stem + ".elk")
    return turtle_to_mermaid(text, direction, elk, read_labels(stem + ".labels"))


def add_diagrams(page, base_dir):
    """Returns the new page and the number of diagrams added."""
    added = []

    def insert(m):
        src = m.group(2)
        mermaid = diagram_for(os.path.join(base_dir, src))
        if mermaid is None:
            return m.group(1) + m.group(3)
        added.append(src)
        return '%s%s\n<pre class="mermaid">%s</pre>' % (
            m.group(1), m.group(3), html.escape(mermaid, quote=False))
    page = ASIDE.sub(insert, page)
    return page, len(added)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("input_file")
    parser.add_argument("output_file")
    parser.add_argument("--base", default=".",
                        help="directory that the src of example asides is relative to (default: .)")
    args = parser.parse_args()

    with open(args.input_file, encoding="utf-8") as f:
        page = f.read()
    page, n = add_diagrams(page, args.base)
    with open(args.output_file, "w", encoding="utf-8") as f:
        f.write(page)
    sys.stderr.write("Added %d example diagrams\n" % n)
