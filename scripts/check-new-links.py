#!/usr/bin/env python3
"""Report content on the sibling sites that this playbook does not link yet.

Run: python3 scripts/check-new-links.py [--report FILE]
Exit 0 always; writes a markdown report and prints it. Empty report = nothing new.
"""
import argparse, json, os, re, sys, urllib.request
from xml.etree import ElementTree

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT = os.path.join(ROOT, "content")
UA = {"User-Agent": "devops-professional-link-sweep"}

# name, sitemap, keep-regex (what counts as a linkable page), label
SITEMAP_SOURCES = [
    ("Architecture Field Notes", "https://architectures.metacog.co.kr/sitemap.xml",
     r"/docs/[a-z-]+/[a-z0-9-]+/$"),
    ("IT Automation Playbook", "https://automations.metacog.co.kr/sitemap.xml",
     r"/docs/[a-z-]+/[a-z0-9-]+/$"),
    ("IT Checklists (devops/operations)", "https://checklists.metacog.co.kr/sitemap.xml",
     r"/docs/(devops|operations)/[a-z0-9-]+/$"),
    ("IT Template Library", "https://templates.metacog.co.kr/sitemap.xml",
     r"/docs/[a-z-]+/[a-z0-9-]+/$"),
    ("Field Cases", "https://fieldcases.metacog.co.kr/sitemap.xml",
     r"/(problems|concepts)/[a-z0-9-]+$"),
    ("Pipeline Field Guide", "https://jeonck.github.io/pipelines/sitemap.xml",
     r"/(docs/[a-z0-9-]+|diagrams)/$"),
    # catalogues: watch for new *sections* only, their per-item pages are linked in bulk
    ("Toolian (sections)", "https://toolian.metacog.co.kr/sitemap.xml", r"/docs/[a-z-]+/$"),
    ("Framework Thinking (sections)", "https://fw-thinking.metacog.co.kr/sitemap.xml", r"/docs/[a-z-]+/$"),
    ("IT Checklists (other sections)", "https://checklists.metacog.co.kr/sitemap.xml", r"/docs/[a-z-]+/$"),
]
HANDSON_INDEX = "https://handson.metacog.co.kr/data/index.json"
HANDSON_NOTE = "https://handson.metacog.co.kr/#/note/"


def fetch(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


def sitemap_urls(url):
    root = ElementTree.fromstring(fetch(url))
    ns = "{http://www.sitemaps.org/schemas/sitemap/0.9}"
    return [loc.text.strip() for loc in root.iter(ns + "loc") if loc.text]


def linked_urls():
    """Every external URL already referenced in content/, normalised."""
    found = set()
    for dirpath, _, names in os.walk(CONTENT):
        for n in names:
            if not n.endswith(".md"):
                continue
            text = open(os.path.join(dirpath, n), encoding="utf-8").read()
            for u in re.findall(r"https?://[^\s)\"'<>]+", text):
                found.add(u.rstrip(".,").rstrip("/"))
    return found


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--report", default="")
    args = ap.parse_args()

    linked = linked_urls()
    sections = []

    for name, sm, keep in SITEMAP_SOURCES:
        try:
            urls = sitemap_urls(sm)
        except Exception as e:                      # a source being down must not fail the sweep
            sections.append("- **%s** — could not be fetched (%s)" % (name, e))
            continue
        pat = re.compile(keep)
        new = [u for u in urls if pat.search(u) and u.rstrip("/") not in linked]
        if new:
            sections.append("### %s (%d new)\n\n%s" % (
                name, len(new), "\n".join("- %s" % u for u in sorted(new))))

    try:
        notes = json.loads(fetch(HANDSON_INDEX))["notes"]
        new = [n for n in notes if (HANDSON_NOTE + n["slug"]) not in linked]
        if new:
            sections.append("### handson (%d new)\n\n%s" % (len(new), "\n".join(
                "- %s%s — %s [%s]" % (HANDSON_NOTE, n["slug"], n["title"], ", ".join(n.get("tags", [])[:4]))
                for n in new)))
    except Exception as e:
        sections.append("- **handson** — could not be fetched (%s)" % e)

    report = "\n\n".join(sections).strip()
    if args.report:
        open(args.report, "w", encoding="utf-8").write(report + ("\n" if report else ""))
    print(report if report else "nothing new")
    return 0


if __name__ == "__main__":
    sys.exit(main())
