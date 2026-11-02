#!/usr/bin/env python3
#
#  estaciones.py
#
#  Genera las páginas de estaciones (`estaciones/` y `en/resorts/`) a partir de
#  `datos/estaciones.json`, que sale del script `scripts/pistas/estaciones.py` de la app
#  con el mismo extracto de OpenStreetMap que los datos de pistas de cada versión.
#
#      python3 -I scripts/estaciones.py
#

import collections
import html
import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LATIN = re.compile(r"^[\u0000-ɏḀ-ỿ\s'’.,()\-–/&0-9]+$")

TEXT = {
    "es": {
        "path": ROOT / "estaciones" / "index.html",
        "lang": "es", "other": "../en/resorts/", "other_lang": "en", "other_label": "English",
        "home": "../", "css": "../estilo.css",
        "title": "Estaciones con pistas en SnowTracker",
        "h1": "Estaciones",
        "intro": "SnowTracker dibuja las pistas y los remontes de {n} estaciones de {c} países debajo de tu ruta, en el mapa de cada día. Van dentro de la app: se ven sin conexión y no envían ningún dato.",
        "note": "Los datos vienen de OpenStreetMap, un mapa que hacen sus colaboradores, y se actualizan con cada versión de la app. Si tu estación tiene pistas en OpenStreetMap, también la verás aunque no figure en esta lista, que solo recoge las que tienen nombre.",
        "search": "Busca una estación o un país", "none": "Ninguna estación coincide.",
        "count": "{n} estaciones", "count1": "1 estación",
        "data": "Datos: © colaboradores de OpenStreetMap, con licencia ODbL. Países: Natural Earth y Apple. Actualizado el {date}.",
        "footer": "SnowTracker · Marcos Velasco Fernández",
        "country": "country_es", "name": "name_es",
        "canonical": "https://marcosvelascogithub.github.io/snowtracker-web/estaciones/",
        "alternate": "https://marcosvelascogithub.github.io/snowtracker-web/en/resorts/",
    },
    "en": {
        "path": ROOT / "en" / "resorts" / "index.html",
        "lang": "en", "other": "../../estaciones/", "other_lang": "es", "other_label": "Español",
        "home": "../", "css": "../../estilo.css",
        "title": "Ski resorts with pistes in SnowTracker",
        "h1": "Ski resorts",
        "intro": "SnowTracker draws the pistes and lifts of {n} ski resorts in {c} countries beneath your route on each day’s map. They’re built into the app: they show offline and send no data.",
        "note": "The data comes from OpenStreetMap, a map made by its contributors, and is updated with each version of the app. If your resort has pistes in OpenStreetMap, you’ll see them even if it isn’t on this list, which only includes named resorts.",
        "search": "Search for a resort or a country", "none": "No resorts match.",
        "count": "{n} resorts", "count1": "1 resort",
        "data": "Data: © OpenStreetMap contributors, licensed under the ODbL. Countries: Natural Earth and Apple. Updated {date}.",
        "footer": "SnowTracker · Marcos Velasco Fernández",
        "country": "country_en", "name": "name_en",
        "canonical": "https://marcosvelascogithub.github.io/snowtracker-web/en/resorts/",
        "alternate": "https://marcosvelascogithub.github.io/snowtracker-web/estaciones/",
    },
}


def fold(s):
    return "".join(c for c in unicodedata.normalize("NFD", s.casefold()) if unicodedata.category(c) != "Mn")


def display_name(r, key):
    """El nombre en el idioma de la página si lo hay; si el original no usa el alfabeto
    latino, el inglés, con el original entre paréntesis."""
    own = r.get(key)
    if own:
        return own, r["name"] if own != r["name"] else None
    if not LATIN.match(r["name"]) and r.get("name_en"):
        return r["name_en"], r["name"]
    return r["name"], None


def render(lang, data):
    t = TEXT[lang]
    resorts = data["resorts"]
    by_country = collections.defaultdict(list)
    for r in resorts:
        by_country[r[t["country"]]].append(r)
    countries = sorted(by_country, key=fold)
    fmt = (lambda n: f"{n:,}".replace(",", ".")) if lang == "es" else (lambda n: f"{n:,}")
    e = html.escape
    out = [f"""<!doctype html>
<html lang="{t['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(t['title'])}</title>
<meta name="description" content="{e(t['intro'].format(n=fmt(len(resorts)), c=len(countries)))}">
<link rel="canonical" href="{t['canonical']}">
<link rel="alternate" hreflang="{t['other_lang']}" href="{t['alternate']}">
<link rel="stylesheet" href="{t['css']}">
<style>
  main {{ max-width: 760px; }}
  .buscar {{ width: 100%; font: inherit; color: var(--texto); background: var(--superficie); border: 1px solid rgba(255, 255, 255, .12);
             border-radius: 14px; padding: 12px 16px; margin: 8px 0 20px; }}
  .buscar:focus {{ outline: 2px solid var(--cian); outline-offset: 1px; }}
  details {{ border-top: 1px solid rgba(255, 255, 255, .08); }}
  summary {{ cursor: pointer; padding: 14px 4px; display: flex; justify-content: space-between; gap: 12px; font-weight: 600; list-style: none; }}
  summary::-webkit-details-marker {{ display: none; }}
  summary::after {{ content: "›"; color: var(--secundario); transition: transform .2s; }}
  details[open] summary::after {{ transform: rotate(90deg); }}
  summary .n {{ margin-left: auto; color: var(--secundario); font-weight: 400; }}
  ul {{ list-style: none; margin: 0 0 14px; padding: 0 4px; columns: 2 260px; column-gap: 28px; }}
  li {{ break-inside: avoid; padding: 3px 0; }}
  li .orig {{ color: var(--secundario); }}
  .vacio {{ color: var(--secundario); }}
  .datos {{ font-size: 14px; }}
</style>
</head>
<body>
<main>
<header>
<a class="marca" href="{t['home']}">SnowTracker</a>
<h1>{e(t['h1'])}</h1>
<p>{e(t['intro'].format(n=fmt(len(resorts)), c=len(countries)))}</p>
<p class="secundario">{e(t['note'])}</p>
</header>
<label class="secundario" for="buscar" style="position:absolute;left:-9999px">{e(t['search'])}</label>
<input class="buscar" id="buscar" type="search" placeholder="{e(t['search'])}" autocomplete="off">
<p class="vacio" id="vacio" hidden>{e(t['none'])}</p>
<div id="lista">
"""]
    for country in countries:
        items = sorted(by_country[country], key=lambda r: fold(display_name(r, t["name"])[0]))
        n = len(items)
        count = t["count1"] if n == 1 else t["count"].format(n=fmt(n))
        out.append(f'<details data-pais="{e(fold(country))}">\n<summary>{e(country)}<span class="n">{count}</span></summary>\n<ul>\n')
        for r in items:
            name, orig = display_name(r, t["name"])
            key = fold(" ".join(x for x in (name, orig or "", r["name"]) if x))
            extra = f' <span class="orig" lang="">({e(orig)})</span>' if orig else ""
            out.append(f'<li data-n="{e(key)}">{e(name)}{extra}</li>\n')
        out.append("</ul>\n</details>\n")
    out.append(f"""</div>
<p class="secundario datos">{e(t['data'].format(date=data['date'][lang]))}</p>
<footer>{e(t['footer'])} · <a href="{t['other']}" hreflang="{t['other_lang']}" lang="{t['other_lang']}">{t['other_label']}</a></footer>
</main>
<script>
(() => {{
  const input = document.getElementById("buscar"), empty = document.getElementById("vacio");
  const groups = [...document.querySelectorAll("#lista details")];
  const fold = s => s.normalize("NFD").replace(/[\\u0300-\\u036f]/g, "").toLowerCase();
  input.addEventListener("input", () => {{
    const q = fold(input.value.trim()); let shown = 0;
    for (const g of groups) {{
      const countryHit = q && g.dataset.pais.includes(q);
      let hits = 0;
      for (const li of g.querySelectorAll("li")) {{
        const show = !q || countryHit || li.dataset.n.includes(q);
        li.hidden = !show; if (show) hits++;
      }}
      g.hidden = hits === 0; g.open = !!q && hits > 0; shown += hits;
    }}
    empty.hidden = shown > 0;
  }});
}})();
</script>
</body>
</html>
""")
    t["path"].parent.mkdir(parents=True, exist_ok=True)
    t["path"].write_text("".join(out), encoding="utf-8")
    print(t["path"].relative_to(ROOT), len(resorts), len(countries))


def main():
    data = json.loads((ROOT / "datos" / "estaciones.json").read_text(encoding="utf-8"))
    for lang in TEXT:
        render(lang, data)


if __name__ == "__main__":
    main()
