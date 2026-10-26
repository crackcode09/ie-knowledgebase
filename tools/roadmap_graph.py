"""Draw ROADMAP.md as a radial knowledge graph (roadmap.svg) and build the
interactive site (public/index.html, public/course.html) from the roadmap and course READMEs.
GitHub Pages publishes the repo root; the site lives in public/ and reads courses/ in place.

Usage:  python tools/roadmap_graph.py
Re-run after editing ROADMAP.md or adding a course. Standard library only.
"""
import json
import math
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "ROADMAP.md"
PUBLIC = ROOT / "public"
OUT = PUBLIC / "roadmap.svg"
HTML_OUT = PUBLIC / "index.html"
TEMPLATE = ROOT / "tools" / "roadmap_template.html"
READER_OUT = PUBLIC / "course.html"
READER_TEMPLATE = ROOT / "tools" / "reader_template.html"
REPO_URL = "https://github.com/crackcode09/ie-knowledgebase"

DONE, TODO, CAT, HUB, LINK, INK, MUTED = (
    "#2E8B57", "#C9D2D8", "#0078E6", "#005BA6", "#D5DDE3", "#1F2A33", "#7A8A96")

LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)\s]+)\)")


def parse(md):
    """ROADMAP.md -> [{name, slug, items: [(title, done, link_path)]}]"""
    cats, cur = [], None
    for line in md.splitlines():
        m = re.match(r"^## (.+?) \(\d+/\d+\)", line)
        if m:
            cur = {"name": m.group(1), "items": [], "slug": None}
            cats.append(cur)
            continue
        m = re.match(r"^Folder: \[`courses/([a-z0-9-]+)/`\]", line)
        if m and cur is not None:
            cur["slug"] = m.group(1)
            continue
        m = re.match(r"^- \[([ x])\] (.+)", line)
        if m and cur is not None:
            lm = LINK_RE.search(m.group(2))
            title = LINK_RE.sub(r"\1", m.group(2))
            title = re.split(r" — ", title)[0].strip()
            folded = "folded into" in m.group(2)
            cur["items"].append((title, m.group(1) == "x", lm.group(2) if lm else None, folded))
    return cats


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


# ----------------------------------------------------------------- static SVG

def render(cats):
    size = 1850
    cx = cy = size / 2
    r_cat, r_leaf = 300, 580
    total = sum(len(c["items"]) for c in cats)
    done = sum(ok for c in cats for _, ok, _p, _f in c["items"])
    gap = 0.012  # radians of padding between category sectors
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {size} {size}" '
             f'font-family="Roboto, Arial, sans-serif" font-size="11">',
             f'<rect width="{size}" height="{size}" fill="#FFFFFF"/>',
             f'<text x="{size - 30}" y="{size - 44}" text-anchor="end" font-size="22" font-weight="700" fill="{INK}">'
             f'IE Knowledgebase roadmap</text>',
             f'<text x="{size - 30}" y="{size - 22}" text-anchor="end" font-size="13" fill="{MUTED}">'
             f'{done} of {total} courses built</text>']
    edges, nodes, labels = [], [], []
    ang = -math.pi / 2
    for c in cats:
        n = len(c["items"])
        span = 2 * math.pi * n / total
        a_cat = ang + span / 2
        x1, y1 = cx + r_cat * math.cos(a_cat), cy + r_cat * math.sin(a_cat)
        edges.append(f'<line x1="{cx:.1f}" y1="{cy:.1f}" x2="{x1:.1f}" y2="{y1:.1f}" stroke="{LINK}" stroke-width="2"/>')
        inner = span - 2 * gap
        for i, (title, ok, _p, _f) in enumerate(c["items"]):
            a = ang + gap + inner * (i + 0.5) / n
            x2, y2 = cx + r_leaf * math.cos(a), cy + r_leaf * math.sin(a)
            edges.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
                         f'stroke="{DONE if ok else LINK}" stroke-width="{1.6 if ok else 1}"/>')
            fill = DONE if ok else "#FFFFFF"
            nodes.append(f'<circle cx="{x2:.1f}" cy="{y2:.1f}" r="{6 if ok else 4.5}" fill="{fill}" '
                         f'stroke="{DONE if ok else TODO}" stroke-width="1.5"/>')
            deg = math.degrees(a)
            flip = 90 < (deg % 360) < 270
            tx, ty = cx + (r_leaf + 11) * math.cos(a), cy + (r_leaf + 11) * math.sin(a)
            rot = deg + 180 if flip else deg
            anchor = "end" if flip else "start"
            labels.append(f'<text transform="translate({tx:.1f},{ty:.1f}) rotate({rot:.1f})" '
                          f'text-anchor="{anchor}" dominant-baseline="middle" '
                          f'fill="{INK if ok else MUTED}" font-weight="{700 if ok else 400}">{esc(title)}</text>')
        k = sum(ok for _, ok, _p, _f in c["items"])
        nodes.append(f'<circle cx="{x1:.1f}" cy="{y1:.1f}" r="36" fill="{CAT}"/>')
        name = c["name"].replace(" & ", " &amp; ")
        words = name.split()
        lines, line = [], ""
        for w in words:
            if len(line) + len(w) > 13 and line:
                lines.append(line)
                line = w
            else:
                line = (line + " " + w).strip()
        lines.append(line)
        lines.append(f"{k}/{n}")
        y0 = y1 - (len(lines) - 1) * 5.5
        for j, ln in enumerate(lines):
            w = "700" if j == len(lines) - 1 else "500"
            labels.append(f'<text x="{x1:.1f}" y="{y0 + j * 11:.1f}" text-anchor="middle" '
                          f'dominant-baseline="middle" fill="#FFFFFF" font-size="9.5" font-weight="{w}">{ln}</text>')
        ang += span
    nodes.append(f'<circle cx="{cx}" cy="{cy}" r="44" fill="{HUB}"/>')
    labels.append(f'<text x="{cx}" y="{cy - 6}" text-anchor="middle" fill="#FFFFFF" font-size="12" font-weight="700">IE</text>')
    labels.append(f'<text x="{cx}" y="{cy + 9}" text-anchor="middle" fill="#FFFFFF" font-size="10">Knowledgebase</text>')
    legend_y = size - 28
    parts.append(f'<circle cx="30" cy="{legend_y}" r="6" fill="{DONE}"/>'
                 f'<text x="42" y="{legend_y + 4}" fill="{INK}">built</text>'
                 f'<circle cx="100" cy="{legend_y}" r="4.5" fill="#FFFFFF" stroke="{TODO}" stroke-width="1.5"/>'
                 f'<text x="112" y="{legend_y + 4}" fill="{INK}">not started</text>')
    return "\n".join(parts + edges + nodes + labels + ["</svg>"])


# ------------------------------------------------------------ interactive map

def slugify(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def rel(path):
    return str(path).replace("\\", "/")


def category_table(slug):
    """Course README path -> (topic, length) from the category README table."""
    out = {}
    p = ROOT / "courses" / slug / "README.md"
    if not p.exists():
        return out
    for line in p.read_text(encoding="utf-8").splitlines():
        if not line.startswith("| ["):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        m = LINK_RE.match(cells[0])
        if m and len(cells) >= 3:
            out[f"courses/{slug}/{m.group(2)}"] = (cells[1], cells[2])
    return out


def category_description(slug):
    p = ROOT / "courses" / slug / "README.md"
    if not p.exists():
        return ""
    for line in p.read_text(encoding="utf-8").splitlines()[1:]:
        if line.strip() and not line.startswith("#"):
            return line.strip()
    return ""


def module_summary(path, limit=220):
    """Topics line for a module whose syllabus row has none: its learning objectives
    joined with semicolons; else its section headings; else its first paragraph."""
    try:
        lines = (ROOT / path).read_text(encoding="utf-8").splitlines()
    except OSError:
        return "", "", 0
    items, grab, kind = [], False, "objectives"
    for line in lines:
        if re.match(r"^#+\s*(learning\s+)?objectives", line, re.I):
            grab = True
            continue
        if grab and line.startswith("#"):
            break
        if grab:
            m = re.match(r"^\s*(?:\d+[.)]|[-*])\s+(.+)", line)
            if m:
                items.append(m.group(1).strip())
    if not items:
        items = [re.sub(r"^\d+\.\s*", "", h[3:]).strip() for h in lines if h.startswith("## ")]
        kind = "sections"
    if not items:
        kind = "summary"
        for line in lines[1:]:
            s = line.strip()
            if s and not re.match(r"^(#|\||\*\*Time|\*\*Data|!|`|<|-|\*|\d+[.)])", s):
                items = [s]
                break
    def clean(s):
        s = LINK_RE.sub(r"\1", s)
        s = re.sub(r"(\*\*|\*|_|`)([^*_`]+)\1", r"\2", s)
        return re.sub(r"[.;:]\s*$", "", s.strip())
    cleaned = [clean(i) for i in items if i]
    out = "; ".join(cleaned)
    if len(out) > limit:
        head = out[:limit]
        cut = head.rsplit(";", 1)[0] if ";" in head else head.rsplit(" ", 1)[0]
        out = cut.rstrip(" ;,") + " …"
    return out, kind, len(cleaned)


def course_info(readme_path):
    """Description, module rows, prerequisite and related course paths from a course README."""
    base = Path(readme_path).parent
    lines = (ROOT / readme_path).read_text(encoding="utf-8").splitlines()
    desc = ""
    for line in lines[1:]:
        s = line.strip()
        if s and not s.startswith(("#", "|", "**", "-", "!", "`")):
            desc = re.sub(r"(\*\*|\*|_)([^*_]+)\1", r"\2", LINK_RE.sub(r"\1", s))
            break
    modules = []
    time_idx = topics_idx = None
    for line in lines:
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if time_idx is None and topics_idx is None and not any("](" in c for c in cells):
            # header row of the syllabus table: learn which column holds time and which holds topics
            for i, c in enumerate(cells):
                if re.search(r"time|duration|length", c, re.I):
                    time_idx = i
                elif re.search(r"body of knowledge|topics?|covers?|contents?", c, re.I):
                    topics_idx = i
            continue
        m = re.search(r"\[([^\]]+)\]\((modules/[^)\s]+)\)", line)
        if not m:
            continue
        note = cells[time_idx] if time_idx is not None and time_idx < len(cells) else ""
        topics = cells[topics_idx] if topics_idx is not None and topics_idx < len(cells) else ""
        if not note and not topics and len(cells) > 1 and "](" not in cells[-1]:
            last = cells[-1]
            if re.search(r"\d\s*(min|h\b|hour|day)", last):
                note = last
            else:
                topics = last
        mpath = rel(base / m.group(2))
        if topics:
            tkind, tcount = "topics", len([x for x in re.split(r"[;,]", topics) if x.strip()])
        else:
            topics, tkind, tcount = module_summary(mpath)
        modules.append({"title": m.group(1), "path": mpath, "note": note, "topics": topics, "tkind": tkind, "tcount": tcount})
    prereq, related = [], []
    for line in lines:
        is_prereq_line = "prerequisite" in line.lower()
        # On a prerequisites line, links after "Helpful" are recommendations, not requirements.
        hard, soft = (re.split(r"helpful|helps\b", line, maxsplit=1, flags=re.I) + [""])[:2] if is_prereq_line else ("", line)
        for part, bucket in ((hard, prereq), (soft, related)):
            for _label, href in LINK_RE.findall(part):
                if not href.startswith("../") or not href.endswith("/README.md"):
                    continue
                target = rel((ROOT / base / href).resolve().relative_to(ROOT))
                if target not in prereq and target not in related:
                    bucket.append(target)
    return desc, modules, prereq, related


def first_heading(path):
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^#\s+(.+)", line)
        if m:
            return LINK_RE.sub(r"\1", m.group(1)).strip()
    return path.stem


def course_extras(readme_path):
    """Reference, solutions and template markdown files shipped with a course, for the reader's nav."""
    base = ROOT / Path(readme_path).parent
    out = []
    for pattern in ("reference/*.md", "solutions/README.md", "templates/*.md", "examples/*.md"):
        for f in sorted(base.glob(pattern)):
            out.append({"label": first_heading(f), "path": rel(f.relative_to(base))})
    return out


def build_model(cats):
    nodes = [{"id": "hub", "type": "hub", "label": "IE Knowledgebase"}]
    links = []
    by_path = {}
    pending = []  # (course node id, prereq paths, related paths)
    total_items = sum(len(c["items"]) for c in cats) or 1
    ang = -math.pi / 2
    for c in cats:
        slug = c["slug"] or slugify(c["name"])
        cid = "cat:" + slug
        span = 2 * math.pi * len(c["items"]) / total_items
        nodes.append({"id": cid, "type": "category", "label": c["name"], "a": round(ang + span / 2, 4),
                      "description": category_description(slug),
                      "path": f"courses/{slug}/README.md"})
        links.append({"source": "hub", "target": cid, "type": "tree"})
        table = category_table(slug)
        for i, (title, ok, path, folded) in enumerate(c["items"]):
            a = round(ang + span * (i + 0.5) / len(c["items"]), 4)
            if ok and path and folded:
                nid = "topic:" + slugify(title)
                nodes.append({"id": nid, "type": "topic", "label": title, "parent": cid, "a": a, "covered_path": path})
            elif ok and path:
                nid = "course:" + Path(path).parent.name
                topic, length = table.get(path, ("", ""))
                desc, modules, prereq, related = course_info(path)
                nodes.append({"id": nid, "type": "course", "label": title, "parent": cid, "path": path, "a": a,
                              "length": length, "description": desc, "search": topic, "extras": course_extras(path)})
                by_path[path] = nid
                pending.append((nid, prereq, related))
                for i, m in enumerate(modules):
                    mid = f"{nid}/{i}"
                    nodes.append({"id": mid, "type": "module", "label": m["title"], "parent": nid, "a": a,
                                  "path": m["path"], "note": m["note"], "topics": m["topics"],
                                  "tkind": m["tkind"], "tcount": m["tcount"]})
                    links.append({"source": nid, "target": mid, "type": "tree"})
            else:
                nid = "topic:" + slugify(title)
                nodes.append({"id": nid, "type": "topic", "label": title, "parent": cid, "a": a})
            links.append({"source": cid, "target": nid, "type": "tree"})
        ang += span
    seen = set()
    for nid, prereq, related in pending:
        for tp in prereq:
            src = by_path.get(tp)
            if src and (src, nid) not in seen:
                links.append({"source": src, "target": nid, "type": "prereq"})
                seen.add((src, nid))
    for nid, prereq, related in pending:
        for tp in related:
            other = by_path.get(tp)
            if not other:
                continue
            key = tuple(sorted((other, nid)))
            if key in seen or (other, nid) in seen or (nid, other) in seen:
                continue
            links.append({"source": nid, "target": other, "type": "related"})
            seen.add(key)
    for n in nodes:
        if n.get("covered_path"):
            n["covered"] = by_path.get(n.pop("covered_path"))
    total = sum(len(c["items"]) for c in cats)
    built = sum(1 for c in cats for _, ok, _p, f in c["items"] if ok and not f)
    covered = sum(1 for c in cats for _, ok, _p, f in c["items"] if ok and f)
    return {"repo": REPO_URL, "total": total, "built": built, "covered": covered, "nodes": nodes, "links": links}


def write_html(cats):
    model = build_model(cats)
    data = json.dumps(model, ensure_ascii=False).replace("</", "<\\/")
    HTML_OUT.write_text(TEMPLATE.read_text(encoding="utf-8").replace("__DATA__", data), encoding="utf-8")
    READER_OUT.write_text(READER_TEMPLATE.read_text(encoding="utf-8").replace("__DATA__", data), encoding="utf-8")
    return model


if __name__ == "__main__":
    PUBLIC.mkdir(exist_ok=True)
    cats = parse(SRC.read_text(encoding="utf-8"))
    OUT.write_text(render(cats), encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)}: {sum(len(c['items']) for c in cats)} courses in {len(cats)} categories")
    model = write_html(cats)
    print(f"wrote {READER_OUT.relative_to(ROOT)}")
    kinds, edges = {}, {}
    for n in model["nodes"]:
        kinds[n["type"]] = kinds.get(n["type"], 0) + 1
    for l in model["links"]:
        edges[l["type"]] = edges.get(l["type"], 0) + 1
    print(f"wrote {HTML_OUT.relative_to(ROOT)}: nodes {kinds}, edges {edges}")
