# -*- coding: utf-8 -*-
"""Baixa fotos reais (Wikimedia Commons) p/ prototipo Top Show Piscinas."""
import json, os, subprocess, sys

OUT = os.path.dirname(os.path.abspath(__file__)) + "/img"
os.makedirs(OUT, exist_ok=True)

QUERIES = {
    "hero.jpg": "swimming pool backyard",
    "limpeza.jpg": "pool skimmer net swimming",
    "instalacao.jpg": "swimming pool under construction",
    "aquecimento.jpg": "solar water heater panels",
    "cristalina.jpg": "resort swimming pool water",
}

UA = "Mozilla/5.0 (Windows NT 10.0) RioPretoTech/1.0"

for fn, q in QUERIES.items():
    url = ("https://commons.wikimedia.org/w/api.php?action=query&format=json"
           f"&generator=search&gsrsearch={q.replace(' ', '%20')}%20filetype:bitmap"
           "&gsrlimit=8&gsrnamespace=6&prop=imageinfo&iiprop=url|size&iiurlwidth=1280")
    raw = subprocess.run(["curl", "-s", "--max-time", "30", "-A", UA, url],
                         capture_output=True, text=True).stdout
    try:
        d = json.loads(raw)
    except Exception:
        print(fn, "API fail"); continue
    pages = list((d.get("query") or {}).get("pages", {}).values())
    pages.sort(key=lambda p: -(p.get("index") if isinstance(p.get("index"), int) else 99))
    ok = False
    for p in pages:
        ii = (p.get("imageinfo") or [{}])[0]
        u = ii.get("thumburl") or ii.get("url")
        w, h = ii.get("width", 0), ii.get("height", 0)
        if not u or w < 900 or h < 500 or w / h < 1.1:
            continue  # quer landscape decente
        r = subprocess.run(["curl", "-sL", "--max-time", "45", "-A", UA, "-o", os.path.join(OUT, fn), u])
        if r.returncode == 0 and os.path.getsize(os.path.join(OUT, fn)) > 40000:
            print(fn, "<-", p.get("title")[:70], os.path.getsize(os.path.join(OUT, fn)))
            ok = True
            break
    if not ok:
        print(fn, "FALHOU", q)
