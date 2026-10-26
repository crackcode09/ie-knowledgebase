"""Draw ROADMAP.md as a radial knowledge graph (docs/roadmap.svg).

Usage:  python tools/roadmap_graph.py
Re-run after editing ROADMAP.md. No dependencies beyond the standard library.
"""
import math
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "ROADMAP.md"
OUT = ROOT / "docs" / "roadmap.svg"

DONE, TODO, CAT, HUB, LINK, INK, MUTED = (
    "#2E8B57", "#C9D2D8", "#0078E6", "#005BA6", "#D5DDE3", "#1F2A33", "#7A8A96")


def parse(md):
    cats, cur = [], None
    for line in md.splitlines():
        m = re.match(r"^## (.+?) \(\d+/\d+\)", line)
        if m:
            cur = {"name": m.group(1), "items": []}
            cats.append(cur)
            continue
        m = re.match(r"^- \[([ x])\] (.+)", line)
        if m and cur is not None:
            title = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", m.group(2))
            title = re.split(r" — ", title)[0].strip()
            cur["items"].append((title, m.group(1) == "x"))
    return cats


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def render(cats):
    size = 1850
    cx = cy = size / 2
    r_cat, r_leaf = 300, 580
    total = sum(len(c["items"]) for c in cats)
    done = sum(ok for c in cats for _, ok in c["items"])
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
        for i, (title, ok) in enumerate(c["items"]):
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
        k = sum(ok for _, ok in c["items"])
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


if __name__ == "__main__":
    cats = parse(SRC.read_text(encoding="utf-8"))
    OUT.write_text(render(cats), encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)}: {sum(len(c['items']) for c in cats)} courses in {len(cats)} categories")
