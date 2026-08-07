#!/usr/bin/env python3
"""Convert Trading in the Zone PDFs to Markdown.

Heading detection per page:
- Line directly after page-break comment that is ALL CAPS (>= 5 chars),
  no trailing punctuation except colon, single line (no paragraph join).
- Use ## (h2) for chapters / major sections, # (h1) only for the file title.
"""

import argparse
import re
import sys
from pathlib import Path

import pdfplumber
import regex  # type: ignore


ALL_CAPS_RE = regex.compile(r"^[\p{Lu}][\p{Lu}0-9 \-'’:]+$")
CHAPTER_RE = re.compile(
    r"^\s*(?:CHAPTER|CHƯƠNG)\s+([A-Z0-9]+)", re.IGNORECASE
)
PART_RE = re.compile(r"^\s*(?:PART|PHẦN)\s+([A-Z0-9]+)", re.IGNORECASE)


def clean_lines(text: str) -> list[str]:
    lines = []
    for raw in text.splitlines():
        line = raw.rstrip()
        lines.append(line)
    out = []
    blank = False
    for ln in lines:
        if not ln.strip():
            if not blank:
                out.append("")
            blank = True
        else:
            out.append(ln.rstrip())
            blank = False
    return out


def is_heading_candidate(line: str) -> bool:
    s = line.strip()
    if len(s) < 5 or len(s) > 80:
        return False
    if not ALL_CAPS_RE.match(s):
        return False
    # Allow letters, digits, spaces, hyphen, apostrophe, colon
    return True


def is_real_heading(line: str, prev_blank: bool) -> bool:
    """A line is a heading if all-caps AND preceded by a blank line
    (visual separation). Used within paragraph flow."""
    if not is_heading_candidate(line):
        return False
    return prev_blank


def extract(pdf_path: Path, md_path: Path) -> dict:
    md: list[str] = []
    md.append(f"# {pdf_path.stem}")
    md.append("")
    md.append(f"_Nguồn: `{pdf_path.name}`_")
    md.append("")

    stats = {"pages": 0, "words": 0, "headings": 0}

    with pdfplumber.open(pdf_path) as pdf:
        stats["pages"] = len(pdf.pages)
        for page_no, page in enumerate(pdf.pages, start=1):
            text = page.extract_text() or ""
            lines = clean_lines(text)
            md.append(f"<!-- page {page_no} -->")

            prev_blank = True  # treat start of page as blank
            i = 0
            while i < len(lines):
                line = lines[i]
                stripped = line.strip()

                # Page-break heading: very first non-blank line of the page
                if prev_blank and is_heading_candidate(stripped):
                    # Heading at top of page -> chapter/section heading
                    md.append("")
                    md.append(f"## {stripped}")
                    md.append("")
                    stats["headings"] += 1
                    i += 1
                    # Consume one optional blank after heading
                    if i < len(lines) and not lines[i].strip():
                        i += 1
                    prev_blank = True
                    continue

                # Mid-flow all-caps heading preceded by blank
                if is_real_heading(line, prev_blank):
                    md.append("")
                    md.append(f"## {stripped}")
                    md.append("")
                    stats["headings"] += 1
                    i += 1
                    prev_blank = True
                    continue

                md.append(line)
                prev_blank = not stripped
                i += 1
            md.append("")

    final = "\n".join(md)
    md_path.write_text(final, encoding="utf-8")
    stats["words"] = len(final.split())
    return stats


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf", type=Path)
    ap.add_argument("md", type=Path)
    args = ap.parse_args()

    if not args.pdf.exists():
        print(f"missing pdf: {args.pdf}", file=sys.stderr)
        return 1

    stats = extract(args.pdf, args.md)
    print(f"OK {args.pdf.name} -> {args.md}")
    print(f"  pages    : {stats['pages']}")
    print(f"  words    : {stats['words']}")
    print(f"  headings : {stats['headings']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
