"""Render the reports in reports/content.py to site/assets/pdf/*.pdf.
Run from the repo root:  python reports/make_pdfs.py   then: node reports/print.js (needs Node + playwright)"""
import pathlib, sys, asyncio
ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT)); sys.path.insert(0, str(ROOT / "reports"))
from content_insights import md
from content import REPORTS

OUT = ROOT / "site" / "assets" / "pdf"
OUT.mkdir(parents=True, exist_ok=True)

CSS = """
@page{size:A4;margin:22mm 20mm 20mm}
@page:first{margin:0}
*{box-sizing:border-box}
body{font-family:Inter,"Inter Display",system-ui,sans-serif;color:#111;font-size:10.5pt;line-height:1.6;margin:0}
.cover{height:297mm;background:#0A0A0A;color:#F4F4F2;padding:24mm 20mm;display:flex;flex-direction:column;justify-content:space-between;page-break-after:always;position:relative;overflow:hidden}
.cover .rings{position:absolute;right:-60mm;top:40mm;width:200mm;height:200mm;border:0.4mm solid rgba(255,255,255,.12);border-radius:50%}
.cover .rings::after{content:"";position:absolute;inset:25mm;border:0.4mm dashed rgba(255,255,255,.1);border-radius:50%}
.brand{display:flex;align-items:center;gap:4mm;font-weight:600;letter-spacing:-.01em}
.mark{width:10mm;height:10mm;border-radius:2.5mm;background:#F4F4F2;color:#0A0A0A;display:grid;place-items:center;font-weight:700;font-size:9pt}
.kind{font-size:8.5pt;letter-spacing:.18em;text-transform:uppercase;color:#A3A3A0}
.cover h1{font-family:"Inter Display",Inter,sans-serif;font-size:40pt;line-height:1.02;letter-spacing:-.035em;margin:6mm 0 6mm;font-weight:600;max-width:150mm}
.cover .sub{font-size:13pt;color:#C9C9C5;max-width:135mm;line-height:1.45}
.cover .meta{display:flex;justify-content:space-between;font-size:9pt;color:#A3A3A0;border-top:0.3mm solid rgba(255,255,255,.18);padding-top:5mm}
.toc{page-break-after:always}
.toc h2{margin-top:0}
.toc ol{padding:0;list-style:none;counter-reset:t}
.toc li{counter-increment:t;display:flex;gap:6mm;padding:3.2mm 0;border-bottom:0.25mm solid #ddd;font-size:11.5pt}
.toc li::before{content:counter(t,decimal-leading-zero);color:#888;font-variant-numeric:tabular-nums;width:9mm}
section{page-break-before:always}
section.first{page-break-before:avoid}
.secno{font-size:8.5pt;letter-spacing:.18em;text-transform:uppercase;color:#777;margin-bottom:3mm}
h2{font-family:"Inter Display",Inter,sans-serif;font-size:24pt;line-height:1.08;letter-spacing:-.03em;font-weight:600;margin:0 0 7mm}
h3{font-size:13pt;margin:7mm 0 2mm}
p{margin:0 0 3.4mm}
strong{font-weight:600}
ul,ol{margin:0 0 4mm;padding-left:5.5mm}
li{margin:1.2mm 0}
blockquote{margin:7mm 0;padding:5mm 7mm;background:#0A0A0A;color:#F4F4F2;font-size:14pt;line-height:1.35;border-radius:2mm;font-style:italic}
.table-wrap{margin:4mm 0 6mm;page-break-inside:avoid}
table{width:100%;border-collapse:collapse;font-size:9.5pt}
th{text-align:left;background:#0A0A0A;color:#F4F4F2;font-weight:500;padding:2.6mm 3mm;font-size:8.5pt;letter-spacing:.04em}
td{padding:2.6mm 3mm;border-bottom:0.25mm solid #ddd;vertical-align:top}
tr:nth-child(even) td{background:#F4F4F1}
.endnote{margin-top:10mm;font-size:8.5pt;color:#777;border-top:0.25mm solid #ddd;padding-top:4mm}
"""

FOOTER = '<div style="width:100%;font-family:Inter,sans-serif;font-size:7.5pt;color:#888;padding:0 20mm;display:flex;justify-content:space-between"><span>Saqib Ameer · {title}</span><span>saqibameer.com · <span class="pageNumber"></span></span></div>'


def render_html(r):
    toc = "".join(f"<li>{t}</li>" for t, _ in r["sections"])
    secs = "".join(
        f'<section class="{"first" if i == 0 else ""}"><div class="secno">{i+1:02d}</div><h2>{t}</h2>{md(body)}</section>'
        for i, (t, body) in enumerate(r["sections"]))
    return f"""<!doctype html><html><head><meta charset="utf-8"><title>{r['title']}</title><style>{CSS}</style></head><body>
<div class="cover"><div class="rings"></div>
<div class="brand"><span class="mark">SA</span>Saqib Ameer · AI Growth Leader</div>
<div><div class="kind">{r['kind']}</div><h1>{r['title']}</h1><p class="sub">{r['subtitle']}</p></div>
<div class="meta"><span>November 2026 · Edition 1</span><span>saqibameer.com · hello@saqibameer.com</span></div></div>
<div class="toc"><div class="secno">Contents</div><h2>Inside this {r['kind'].lower().rstrip('s')}</h2><ol>{toc}</ol>
<p class="endnote">All figures come from engagements led by the author and are reported as recorded in the original case studies, platform data and role records. Results depend on context; no outcome is guaranteed. © 2026 Saqib Ameer. You may share this document unchanged with attribution.</p></div>
{secs}</body></html>"""


if __name__ == "__main__":
    import json
    tmp = ROOT / "reports" / ".build"; tmp.mkdir(exist_ok=True)
    jobs = []
    for r in REPORTS:
        h = tmp / (r["file"][:-4] + ".html"); h.write_text(render_html(r), encoding="utf-8")
        jobs.append({"html": str(h), "pdf": str(OUT / r["file"]), "footer": FOOTER.format(title=r["title"])})
    (tmp / "jobs.json").write_text(json.dumps(jobs))
    print("HTML written; now run: node reports/print.js")
