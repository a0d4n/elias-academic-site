#!/usr/bin/env python3
"""Check the built site before it is deployed.

Usage: check_site.py <site_dir> <base_url>   e.g. https://user.github.io/repo

Fails (exit code 1) if a navigation page is missing or if any internal
link, image, stylesheet or script on any page points to a file that does
not exist. External links are not checked.
"""
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse, unquote

site = Path(sys.argv[1])
base_url = urlparse(sys.argv[2].rstrip("/") if len(sys.argv) > 2 else "")
host, base = base_url.netloc, base_url.path

REQUIRED = ["/", "/research/", "/cv/", "/writing/", "/404.html"]


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.urls = []

    def handle_starttag(self, tag, attrs):
        for name, value in attrs:
            if value and (name in ("href", "src") or (tag == "link" and name == "href")):
                self.urls.append((tag, value))


def resolve(path: str) -> Path:
    p = site / path.lstrip("/")
    if path.endswith("/") or p.is_dir():
        p = p / "index.html"
    return p


errors = []

for page in REQUIRED:
    if not resolve(page).is_file():
        errors.append(f"missing page: {page}")

for html in sorted(site.rglob("*.html")):
    parser = Links()
    parser.feed(html.read_text(encoding="utf-8", errors="replace"))
    rel_page = "/" + str(html.relative_to(site))
    for tag, url in parser.urls:
        u = urlparse(url)
        if u.scheme in ("mailto", "tel", "javascript", "data"):
            continue
        if u.scheme in ("http", "https"):
            # Only absolute links to this site itself are checked.
            if u.netloc != host:
                continue
        path = unquote(u.path)
        if not path:
            continue  # pure #fragment
        if path.startswith("/"):
            if base and not path.startswith(base + "/") and path != base:
                errors.append(f"{rel_page}: link outside site base path: {url}")
                continue
            path = path[len(base):] or "/"
        else:
            path = str(Path(rel_page).parent / path)
        if not resolve(path).exists():
            errors.append(f"{rel_page}: broken link -> {url}")

pages = sorted("/" + str(p.relative_to(site)) for p in site.rglob("*.html"))
print("Pages built:")
for p in pages:
    print("  ", p)

if errors:
    print(f"\n{len(errors)} problem(s) found:")
    for e in sorted(set(errors)):
        print("  ::error::" + e)
    sys.exit(1)

print(f"\nAll {len(REQUIRED)} navigation pages exist and every internal link resolves.")
