#!/usr/bin/env python3
"""Score desk.html. Source, Pages, and raw are the closed plates. jsDelivr @main is a cache alias and is reported, not a fail."""
import re
import sys
import urllib.request

EXPECTED = "Desk · snowphamtom"
SOURCE = "desk.html"
FAIL_EDGES = (
    ("pages", "https://snowphamtom.github.io/desk.html"),
    ("raw", "https://raw.githubusercontent.com/snowphamtom/snowphamtom.github.io/main/desk.html"),
)
LAG_EDGES = (
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
    source_ok = st == EXPECTED and "Score" in src
    print(f"SOURCE title={st!r} expected={EXPECTED!r} score={'Score' in src} match={source_ok}")
    failed = not source_ok
    for name, url in FAIL_EDGES:
        try:
            html = fetch(url)
            et = title(html)
            match = et == EXPECTED and "Score" in html
            print(f"EDGE {name} title={et!r} score={'Score' in html} match={match} url={url}")
            if not match:
                failed = True
        except Exception as e:
            print(f"EDGE {name} error={e} url={url}")
            failed = True
    for name, url in LAG_EDGES:
        try:
            html = fetch(url)
            et = title(html)
            match = et == EXPECTED and "Score" in html
            label = "match" if match else "body-lag" if et == EXPECTED else "mismatch-visible"
            print(f"LAG {name} title={et!r} score={'Score' in html} {label} url={url}")
        except Exception as e:
            print(f"LAG {name} error={e} url={url}")
    print("RESULT mismatch-visible" if failed else "RESULT match")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
