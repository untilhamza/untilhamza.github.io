#!/usr/bin/env python3
"""Verify the built portfolio's navigation and downloads through a running server.

Usage: python3 bin/verify_site.py http://127.0.0.1:4318
Writes a repeatable verification artifact under output/site-review-2026-10-13.
"""

from html.parser import HTMLParser
import json
from pathlib import Path
import sys
from urllib.error import HTTPError
from urllib.parse import urljoin, urlparse
from urllib.request import urlopen

base = (sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:4318").rstrip("/") + "/"
checks = []


class Page(HTMLParser):
    def __init__(self, source):
        super().__init__()
        self.links = []
        self.text = []
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "a" and attrs.get("href"):
            self.links.append(attrs["href"])

    def handle_data(self, text):
        self.text.append(text)


def fetch(path):
    try:
        with urlopen(urljoin(base, path), timeout=15) as response:
            data = response.read()
            checks.append({"path": path, "status": response.status})
            return data
    except HTTPError as error:
        checks.append({"path": path, "status": error.code})
        return None


home = Page(fetch("").decode())
projects = Page(fetch("projects/").decode())
cv = Page(fetch("cv/").decode())
pages = [home, projects, cv]
project_paths = sorted({href for href in projects.links if urlparse(href).path.startswith("/projects/")})
for path in project_paths:
    content = fetch(path)
    if content:
        pages.append(Page(content.decode()))

pdfs = sorted({urlparse(href).path for page in [home, cv] for href in page.links
               if urlparse(href).path.startswith("/assets/pdf/")})
for path in pdfs:
    data = fetch(path)
    if data is not None and not data.startswith(b"%PDF-"):
        checks.append({"path": path, "error": "Download is not a PDF"})

json_data = fetch("assets/json/resume.json")
if json_data:
    resume = json.loads(json_data)
    if resume.get("basics", {}).get("name") != "Hamza Kyamanywa":
        checks.append({"error": "JSON resume has the wrong identity"})

rendered = " ".join(" ".join(page.text) for page in pages)
for placeholder in ["AlbertEinstein", "Professor of Theoretical Physics", "Institute for Advanced Study"]:
    if placeholder in rendered:
        checks.append({"error": "Template resume content present", "value": placeholder})

for path in ["career_evidence/README.md", "linkedin-backup/linkedin-about-approved-2026-10-13.txt",
             "project_contributions/TEXTUTOR_HAMZA_CONTRIBUTIONS.md", "AGENTS.md"]:
    fetch(path)
    if checks[-1]["status"] != 404:
        checks.append({"error": "Internal source material is served", "path": path})
    else:
        checks[-1]["expected"] = 404

failures = [c for c in checks if "error" in c or c.get("status") != c.get("expected", 200)]
report = {"base_url": base, "checks": checks, "passed": not failures,
          "project_routes": len(project_paths), "resume_downloads": pdfs}
output = Path(__file__).resolve().parents[1] / "output/site-review-2026-10-13"
output.mkdir(parents=True, exist_ok=True)
(output / "verification.json").write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps({"passed": not failures, "checks": len(checks), "failures": failures}, indent=2))
sys.exit(bool(failures))
