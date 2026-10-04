#!/usr/bin/env python3
"""Score desk.html title. Source must match. Edges are scored, not assumed green."""
import re
import sys
import urllib.request

EXPECTED = "Desk · snowphamtom"
SOURCE = "desk.html"
EDGES = (
    ("pages", "https://snowphamtom.github.io/desk.html"),
    ("jsdelivr", "https://cdn.jsdelivr.net/gh/snowphamtom/snowphamtom.github.io@main/desk.html"),
)


def title(html: str) -> str:
    m = re.search(r"<title>(.*?)</title>", html, re.I | re.S)
    return m.group(1).strip() if m else ""


def fetch(url: str) -> str:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "desk-check", "Cache-Control": "no-cache"},
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", "replace")


def main() -> int:
    src = open(SOURCE, encoding="utf-8").read()
    st = title(src)
    source_ok = st == EXPECTED
    print(f"SOURCE title={st!r} expected={EXPECTED!r} match={source_ok}")
    failed = not source_ok
    for name, url in EDGES:
        try:
            et = title(fetch(url))
            match = et == EXPECTED
            print(f"EDGE {name} title={et!r} match={match} url={url}")
            if not match:
                failed = True
        except Exception as e:
            print(f"EDGE {name} error={e} url={url}")
            failed = True
    print("RESULT mismatch-visible" if failed else "RESULT match")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
