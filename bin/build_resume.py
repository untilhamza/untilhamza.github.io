#!/usr/bin/env python3
"""Export the site's maintained CV data to PDF, Markdown, and JSON Resume.

Requires Ruby (already used by Jekyll) and Python's reportlab package.
Run from any directory: python3 bin/build_resume.py
"""

import html
import json
from pathlib import Path
import re
import subprocess

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import KeepTogether, Paragraph, SimpleDocTemplate, Spacer

ROOT = Path(__file__).resolve().parents[1]
STAMP = "2026-10-13"
PDF = ROOT / "assets/pdf" / f"{STAMP}-Hamza-Kyamanywa-Resume.pdf"
MARKDOWN = ROOT / f"{STAMP}-hamza-kyamanywa-resume.md"
DATA = json.loads(subprocess.check_output([
    "ruby", "-ryaml", "-rjson", "-e",
    "print YAML.safe_load_file(ARGV[0]).to_json", str(ROOT / "_data/cv.yml"),
], text=True))
SECTIONS = {section["title"]: section for section in DATA}


def plain(value):
    return html.unescape(re.sub(r"<[^>]+>", "", str(value)))


def markup(value):
    text = str(value).replace("<strong>", "<b>").replace("</strong>", "</b>")
    text = re.sub(r'<a href="([^"]+)">', r'<link href="\1" color="#245967">', text)
    text = text.replace("</a>", "</link>")
    text = re.sub(r"&(?!#?\w+;)", "&amp;", text)
    return text.translate(str.maketrans({"\u2011": "-", "\u2013": "-", "\u2014": "-"}))


body = ParagraphStyle("Body", fontName="Helvetica", fontSize=9.3, leading=12.5,
                      textColor=colors.HexColor("#25323a"), spaceAfter=4)
section_style = ParagraphStyle("Section", parent=body, fontName="Helvetica-Bold",
                               fontSize=10.6, leading=14, spaceBefore=11,
                               spaceAfter=6, keepWithNext=True,
                               textColor=colors.HexColor("#245967"))
role_style = ParagraphStyle("Role", parent=body, fontName="Helvetica-Bold",
                            fontSize=10, leading=13, spaceBefore=7,
                            spaceAfter=2, keepWithNext=True)
meta_style = ParagraphStyle("Meta", parent=body, fontSize=8.6, leading=11,
                            textColor=colors.HexColor("#57656e"), keepWithNext=True)
bullet_style = ParagraphStyle("Bullet", parent=body, leftIndent=10,
                              firstLineIndent=-7, spaceAfter=3)

story = [
    Paragraph("Hamza Kyamanywa", ParagraphStyle("Name", parent=body,
              fontName="Helvetica-Bold", fontSize=25, leading=29, spaceAfter=5)),
    Paragraph("Technical Founder | Full-Stack AI Engineer", role_style),
    Paragraph('Seoul, South Korea | <link href="mailto:untilhamza@gmail.com">untilhamza@gmail.com</link>', meta_style),
    Paragraph('<link href="https://untilhamza.github.io">untilhamza.github.io</link> | '
              '<link href="https://www.linkedin.com/in/untilhamza">LinkedIn</link> | '
              '<link href="https://github.com/untilhamza">GitHub</link>', meta_style),
    Spacer(1, 5),
]
markdown = [f"# Hamza Kyamanywa\n\nTechnical Founder | Full-Stack AI Engineer\n\n"
            f"Seoul, South Korea | untilhamza@gmail.com | https://untilhamza.github.io\n\n"
            f"Updated {STAMP}. Generated from `_data/cv.yml` by `bin/build_resume.py`.\n"]

# Keep the PDF focused on current work first; skills remain near the top of
# the web CV, while the printable resume gives experience the first pages.
pdf_sections = [s for s in DATA if s["title"] != "Core Skills"]
pdf_sections.append(SECTIONS["Core Skills"])
for section in pdf_sections:
    story.append(Paragraph(html.escape(section["title"]), section_style))
    markdown.append(f"\n## {section['title']}\n")
    if section["type"] == "time_table":
        for entry in section["contents"]:
            heading = [Paragraph(markup(entry["title"]), role_style),
                       Paragraph(markup(entry["institution"]), meta_style),
                       Paragraph(markup(entry["year"]), meta_style)]
            descriptions = entry.get("description", [])
            if descriptions:
                heading.append(Paragraph("- " + markup(descriptions[0]), bullet_style))
            heading.extend(Paragraph("- " + markup(item), bullet_style) for item in descriptions[1:])
            story.append(KeepTogether(heading))
            markdown.append(f"\n### {plain(entry['title'])}\n\n"
                            f"{plain(entry['institution'])} | {entry['year']}\n")
            markdown.extend(f"- {plain(item)}\n" for item in descriptions)
    elif section["type"] == "nested_list":
        for entry in section["contents"]:
            text = f"<b>{html.escape(entry['title'])}:</b> " + "; ".join(markup(item) for item in entry["items"])
            story.append(Paragraph(text, body))
            markdown.append(f"\n**{entry['title']}:** " + "; ".join(plain(item) for item in entry["items"]) + "\n")
    else:
        for item in section["contents"]:
            story.append(Paragraph(markup(item), body))
            markdown.append(f"\n{plain(item)}\n")


def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.HexColor("#66747b"))
    canvas.drawString(42, 25, "Hamza Kyamanywa | October 2026")
    canvas.drawRightString(A4[0] - 42, 25, str(doc.page))
    canvas.restoreState()


PDF.parent.mkdir(parents=True, exist_ok=True)
SimpleDocTemplate(str(PDF), pagesize=A4, leftMargin=42, rightMargin=42,
                  topMargin=32, bottomMargin=40, title="Hamza Kyamanywa - Resume",
                  author="Hamza Kyamanywa").build(story, onFirstPage=footer, onLaterPages=footer)
MARKDOWN.write_text("".join(markdown), encoding="utf-8")

# Machine-readable export; the HTML resume continues to use the same YAML source.
resume = {
    "basics": {
        "name": "Hamza Kyamanywa", "label": "Technical Founder | Full-Stack AI Engineer",
        "email": "untilhamza@gmail.com", "url": "https://untilhamza.github.io",
        "location": {"city": "Seoul", "countryCode": "KR"},
        "summary": plain(SECTIONS["Professional Summary"]["contents"][0]),
        "profiles": [{"network": "LinkedIn", "username": "untilhamza", "url": "https://www.linkedin.com/in/untilhamza"},
                     {"network": "GitHub", "username": "untilhamza", "url": "https://github.com/untilhamza"}],
    },
    "work": [{"name": plain(e["institution"]), "position": plain(e["title"]),
              "summary": e["year"], "highlights": [plain(t) for t in e["description"]]}
             for e in SECTIONS["Professional Experience"]["contents"]],
    "volunteer": [{"organization": plain(e["institution"]), "position": plain(e["title"]),
                   "summary": e["year"], "highlights": [plain(t) for t in e["description"]]}
                  for e in SECTIONS["Leadership & Community"]["contents"]],
    "education": [{"institution": plain(e["institution"]), "area": plain(e["title"]),
                   "summary": e["year"] + "; " + "; ".join(plain(t) for t in e["description"])}
                  for e in SECTIONS["Education"]["contents"]],
    "skills": [{"name": e["title"], "keywords": [plain(t) for t in e["items"]]}
               for e in SECTIONS["Core Skills"]["contents"]],
    "meta": {"lastModified": STAMP, "source": "_data/cv.yml"},
}
(ROOT / "assets/json/resume.json").write_text(json.dumps(resume, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"Generated {PDF.relative_to(ROOT)}, {MARKDOWN.name}, assets/json/resume.json")
