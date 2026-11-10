#!/usr/bin/env python3
#
#  estaciones.py
#
#  Genera las páginas de estaciones (`estaciones/`, `en/resorts/`, `de/skigebiete/`, `fr/stations/`, `it/comprensori/`, `nl/skigebieden/`, `pl/osrodki/`, `cs/strediska/`,
#  `sv/skidorter/`, `da/skiomraader/`, `ru/kurorty/`, `ja/ski-jo/` y `pt/estancias/`) a partir de
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
        "lang": "es", "label": "Español", "root": "../",
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
        "dir": "estaciones/",
    },
    "en": {
        "path": ROOT / "en" / "resorts" / "index.html",
        "lang": "en", "label": "English", "root": "../../",
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
        "dir": "en/resorts/",
    },
    "de": {
        "path": ROOT / "de" / "skigebiete" / "index.html",
        "lang": "de", "label": "Deutsch", "root": "../../",
        "home": "../", "css": "../../estilo.css",
        "title": "Skigebiete mit Pisten in SnowTracker",
        "h1": "Skigebiete",
        "intro": "SnowTracker zeigt die Pisten und Lifte von {n} Skigebieten in {c} Ländern unter deiner Route, auf der Karte jedes Tages. Sie sind in der App enthalten: Sie werden offline angezeigt und senden keine Daten.",
        "note": "Die Daten stammen von OpenStreetMap, einer Karte, die von ihren Mitwirkenden erstellt wird, und werden mit jeder Version der App aktualisiert. Hat dein Skigebiet Pisten in OpenStreetMap, siehst du sie auch, wenn es nicht in dieser Liste steht – sie enthält nur Skigebiete mit Namen.",
        "search": "Skigebiet oder Land suchen", "none": "Kein Skigebiet gefunden.",
        "count": "{n} Skigebiete", "count1": "1 Skigebiet",
        "data": "Daten: © OpenStreetMap-Mitwirkende, lizenziert unter der ODbL. Länder: Natural Earth und Apple. Stand: {date}.",
        "footer": "SnowTracker · Marcos Velasco Fernández",
        "country": "country_de", "name": "name_de",
        "dir": "de/skigebiete/",
    },
    "fr": {
        "path": ROOT / "fr" / "stations" / "index.html",
        "lang": "fr", "label": "Français", "root": "../../",
        "home": "../", "css": "../../estilo.css",
        "title": "Stations de ski avec pistes dans SnowTracker",
        "h1": "Stations",
        "intro": "SnowTracker affiche les pistes et les remontées de {n} stations dans {c} pays sous votre parcours, sur le plan de chaque journée. Elles sont incluses dans l’app : elles s’affichent hors connexion et n’envoient aucune donnée.",
        "note": "Les données viennent d’OpenStreetMap, une carte réalisée par ses contributeurs, et sont mises à jour à chaque version de l’app. Si votre station a des pistes dans OpenStreetMap, vous les verrez même si elle ne figure pas dans cette liste, qui ne reprend que les stations ayant un nom.",
        "search": "Rechercher une station ou un pays", "none": "Aucune station ne correspond.",
        "count": "{n} stations", "count1": "1 station",
        "data": "Données : © contributeurs d’OpenStreetMap, sous licence ODbL. Pays : Natural Earth et Apple. Mis à jour le {date}.",
        "footer": "SnowTracker · Marcos Velasco Fernández",
        "country": "country_fr", "name": "name_fr",
        "dir": "fr/stations/",
    },
    "it": {
        "path": ROOT / "it" / "comprensori" / "index.html",
        "lang": "it", "label": "Italiano", "root": "../../",
        "home": "../", "css": "../../estilo.css",
        "title": "Comprensori sciistici con piste in SnowTracker",
        "h1": "Comprensori",
        "intro": "SnowTracker mostra le piste e gli impianti di {n} comprensori in {c} paesi sotto il tuo percorso, sulla mappa di ogni giornata. Sono inclusi nell’app: si vedono senza connessione e non inviano alcun dato.",
        "note": "I dati provengono da OpenStreetMap, una mappa realizzata dai suoi collaboratori, e si aggiornano a ogni versione dell’app. Se il tuo comprensorio ha piste in OpenStreetMap, le vedrai anche se non compare in questo elenco, che include solo i comprensori con un nome.",
        "search": "Cerca un comprensorio o un paese", "none": "Nessun comprensorio corrisponde.",
        "count": "{n} comprensori", "count1": "1 comprensorio",
        "data": "Dati: © collaboratori di OpenStreetMap, con licenza ODbL. Paesi: Natural Earth e Apple. Aggiornato il {date}.",
        "footer": "SnowTracker · Marcos Velasco Fernández",
        "country": "country_it", "name": "name_it",
        "dir": "it/comprensori/",
    },
    "nl": {
        "path": ROOT / "nl" / "skigebieden" / "index.html",
        "lang": "nl", "label": "Nederlands", "root": "../../",
        "home": "../", "css": "../../estilo.css",
        "title": "Skigebieden met pistes in SnowTracker",
        "h1": "Skigebieden",
        "intro": "SnowTracker toont de pistes en liften van {n} skigebieden in {c} landen onder je route, op de kaart van elke dag. Ze zitten in de app: je ziet ze offline en ze versturen geen gegevens.",
        "note": "De gegevens komen van OpenStreetMap, een kaart die door bijdragers wordt gemaakt, en worden bij elke versie van de app bijgewerkt. Heeft je skigebied pistes in OpenStreetMap, dan zie je ze ook als het niet in deze lijst staat, die alleen skigebieden met een naam bevat.",
        "search": "Zoek een skigebied of land", "none": "Geen skigebied gevonden.",
        "count": "{n} skigebieden", "count1": "1 skigebied",
        "data": "Gegevens: © bijdragers van OpenStreetMap, onder de ODbL-licentie. Landen: Natural Earth en Apple. Bijgewerkt op {date}.",
        "footer": "SnowTracker · Marcos Velasco Fernández",
        "country": "country_nl", "name": "name_nl",
        "dir": "nl/skigebieden/",
    },
    "pl": {
        "path": ROOT / "pl" / "osrodki" / "index.html",
        "lang": "pl", "label": "Polski", "root": "../../",
        "home": "../", "css": "../../estilo.css",
        "title": "Ośrodki narciarskie z trasami w SnowTracker",
        "h1": "Ośrodki narciarskie",
        "intro": "SnowTracker pokazuje pod Twoją trasą, na mapie każdego dnia, trasy i wyciągi z {n} {rw} w {c} {cw}. Są wbudowane w aplikację: widać je bez połączenia i nie wysyłają żadnych danych.",
        "note": "Dane pochodzą z OpenStreetMap, mapy tworzonej przez jej współtwórców, i są aktualizowane z każdą wersją aplikacji. Jeśli Twój ośrodek ma trasy w OpenStreetMap, zobaczysz je, nawet jeśli nie ma go na tej liście, która obejmuje tylko ośrodki z nazwą.",
        "search": "Szukaj ośrodka lub kraju", "none": "Żaden ośrodek nie pasuje.",
        "counts": {'one': '{n} ośrodek', 'few': '{n} ośrodki', 'many': '{n} ośrodków'},
        "data": "Dane: © współtwórcy OpenStreetMap, licencja ODbL. Kraje: Natural Earth i Apple. Aktualizacja: {date}.",
        "footer": "SnowTracker · Marcos Velasco Fernández",
        "country": "country_pl", "name": "name_pl",
        "dir": "pl/osrodki/",
        "words": {'rw': {'one': 'ośrodka narciarskiego', 'other': 'ośrodków narciarskich'}, 'cw': {'one': 'kraju', 'other': 'krajach'}},
    },
    "cs": {
        "path": ROOT / "cs" / "strediska" / "index.html",
        "lang": "cs", "label": "Čeština", "root": "../../",
        "home": "../", "css": "../../estilo.css",
        "title": "Lyžařská střediska se sjezdovkami ve SnowTrackeru",
        "h1": "Lyžařská střediska",
        "intro": "SnowTracker na mapě každého dne ukazuje pod vaší trasou sjezdovky a vleky z {n} {rw} v {c} {cw}. Jsou součástí aplikace: zobrazí se i bez připojení a neodesílají žádná data.",
        "note": "Data pocházejí z OpenStreetMap, mapy, kterou tvoří její přispěvatelé, a aktualizují se s každou verzí aplikace. Pokud má vaše středisko sjezdovky v OpenStreetMap, uvidíte je, i když na tomto seznamu není; obsahuje jen střediska s názvem.",
        "search": "Hledat středisko nebo zemi", "none": "Žádné středisko neodpovídá.",
        "counts": {'one': '{n} středisko', 'few': '{n} střediska', 'other': '{n} středisek'},
        "data": "Data: © přispěvatelé OpenStreetMap, licence ODbL. Země: Natural Earth a Apple. Aktualizováno {date}.",
        "footer": "SnowTracker · Marcos Velasco Fernández",
        "country": "country_cs", "name": "name_cs",
        "dir": "cs/strediska/",
        "words": {'rw': {'one': 'lyžařského střediska', 'other': 'lyžařských středisek'}, 'cw': {'one': 'zemi', 'other': 'zemích'}},
    },
    "sv": {
        "path": ROOT / "sv" / "skidorter" / "index.html",
        "lang": "sv", "label": "Svenska", "root": "../../",
        "home": "../", "css": "../../estilo.css",
        "title": "Skidorter med backar i SnowTracker",
        "h1": "Skidorter",
        "intro": "SnowTracker visar backarna och liftarna i {n} {rw} i {c} {cw} under din rutt, på kartan för varje dag. De finns i appen: de visas utan anslutning och skickar inga data.",
        "note": "Uppgifterna kommer från OpenStreetMap, en karta som skapas av dess bidragsgivare, och uppdateras med varje version av appen. Om din skidort har backar i OpenStreetMap ser du dem även om den inte finns i den här listan, som bara tar med skidorter med namn.",
        "search": "Sök efter en skidort eller ett land", "none": "Ingen skidort matchar.",
        "counts": {'one': '{n} skidort', 'other': '{n} skidorter'},
        "data": "Data: © OpenStreetMaps bidragsgivare, licens ODbL. Länder: Natural Earth och Apple. Uppdaterad {date}.",
        "footer": "SnowTracker · Marcos Velasco Fernández",
        "country": "country_sv", "name": "name_sv",
        "dir": "sv/skidorter/",
        "words": {'rw': {'one': 'skidort', 'other': 'skidorter'}, 'cw': {'one': 'land', 'other': 'länder'}},
    },
    "da": {
        "path": ROOT / "da" / "skiomraader" / "index.html",
        "lang": "da", "label": "Dansk", "root": "../../",
        "home": "../", "css": "../../estilo.css",
        "title": "Skiområder med pister i SnowTracker",
        "h1": "Skiområder",
        "intro": "SnowTracker viser pisterne og liftene i {n} {rw} i {c} {cw} under din rute på kortet for hver dag. De ligger i appen: de vises uden forbindelse og sender ingen data.",
        "note": "Dataene kommer fra OpenStreetMap, et kort, som dets bidragydere laver, og opdateres med hver version af appen. Har dit skiområde pister i OpenStreetMap, ser du dem, selv om det ikke er på denne liste, som kun omfatter skiområder med navn.",
        "search": "Søg efter et skiområde eller et land", "none": "Ingen skiområder passer.",
        "counts": {'one': '{n} skiområde', 'other': '{n} skiområder'},
        "data": "Data: © OpenStreetMaps bidragydere, licens ODbL. Lande: Natural Earth og Apple. Opdateret {date}.",
        "footer": "SnowTracker · Marcos Velasco Fernández",
        "country": "country_da", "name": "name_da",
        "dir": "da/skiomraader/",
        "words": {'rw': {'one': 'skiområde', 'other': 'skiområder'}, 'cw': {'one': 'land', 'other': 'lande'}},
    },
    "ru": {
        "path": ROOT / "ru" / "kurorty" / "index.html",
        "lang": "ru", "label": "Русский", "root": "../../",
        "home": "../", "css": "../../estilo.css",
        "title": "Горнолыжные курорты с трассами в SnowTracker",
        "h1": "Горнолыжные курорты",
        "intro": "SnowTracker показывает на карте каждого дня под Вашим маршрутом трассы и подъемники {n} {rw} в {c} {cw}. Они встроены в приложение: видны без подключения и не отправляют никаких данных.",
        "note": "Данные взяты из OpenStreetMap — карты, которую создают ее участники, — и обновляются с каждой версией приложения. Если у Вашего курорта есть трассы в OpenStreetMap, Вы увидите их, даже если его нет в этом списке: в него входят только курорты с названием.",
        "search": "Поиск курорта или страны", "none": "Нет подходящих курортов.",
        "counts": {'one': '{n} курорт', 'few': '{n} курорта', 'many': '{n} курортов'},
        "data": "Данные: © участники OpenStreetMap, лицензия ODbL. Страны: Natural Earth и Apple. Обновлено {date}.",
        "footer": "SnowTracker · Marcos Velasco Fernández",
        "country": "country_ru", "name": "name_ru",
        "dir": "ru/kurorty/",
        "words": {'rw': {'one': 'курорта', 'other': 'курортов'}, 'cw': {'one': 'стране', 'other': 'странах'}},
    },
    "ja": {
        "path": ROOT / "ja" / "ski-jo" / "index.html",
        "lang": "ja", "label": "日本語", "root": "../../",
        "home": "../", "css": "../../estilo.css",
        "title": "SnowTrackerでコースを表示できるスキー場",
        "h1": "スキー場",
        "intro": "SnowTrackerは、{c}か国・{n}か所のスキー場のコースとリフトを、毎日の地図でルートの下に表示します。データはアプリに内蔵されているため、オフラインでも表示され、データを送信することはありません。",
        "note": "データは協力者が作成している地図、OpenStreetMapのもので、アプリのバージョンごとに更新されます。OpenStreetMapにコースがあるスキー場なら、この一覧になくても表示されます。この一覧には名前のあるスキー場だけを載せています。",
        "search": "スキー場または国を検索", "none": "該当するスキー場はありません。",
        "counts": {'other': '{n}か所'},
        "data": "データ：© OpenStreetMap協力者（ODbLライセンス）。国名：Natural EarthとApple。更新日：{date}。",
        "footer": "SnowTracker · Marcos Velasco Fernández",
        "country": "country_ja", "name": "name_ja",
        "dir": "ja/ski-jo/",
    },
    "pt": {
        "path": ROOT / "pt" / "estancias" / "index.html",
        "lang": "pt-PT", "label": "Português", "root": "../../",
        "home": "../", "css": "../../estilo.css",
        "title": "Estâncias com pistas no SnowTracker",
        "h1": "Estâncias de esqui",
        "intro": "O SnowTracker mostra as pistas e os meios mecânicos de {n} {rw} em {c} {cw} por baixo do seu percurso, no mapa de cada dia. Estão incluídos na aplicação: veem-se sem ligação e não enviam dados.",
        "note": "Os dados vêm do OpenStreetMap, um mapa feito pelos seus colaboradores, e são atualizados com cada versão da aplicação. Se a sua estância tiver pistas no OpenStreetMap, também as vê, mesmo que não esteja nesta lista, que só inclui estâncias com nome.",
        "search": "Procure uma estância ou um país", "none": "Nenhuma estância corresponde.",
        "counts": {'one': '{n} estância', 'other': '{n} estâncias'},
        "data": "Dados: © colaboradores do OpenStreetMap, licença ODbL. Países: Natural Earth e Apple. Atualizado em {date}.",
        "footer": "SnowTracker · Marcos Velasco Fernández",
        "country": "country_pt", "name": "name_pt",
        "dir": "pt/estancias/",
        "words": {'rw': {'one': 'estância', 'other': 'estâncias'}, 'cw': {'one': 'país', 'other': 'países'}},
    },
}

SITE = "https://marcosvelascogithub.github.io/snowtracker-web/"


def fold(s):
    return "".join(c for c in unicodedata.normalize("NFD", s.casefold()) if unicodedata.category(c) != "Mn")


SCRIPTS = {"name_ru": ("CYRILLIC",), "name_ja": ("CJK", "HIRAGANA", "KATAKANA", "IDEOGRAPHIC")}


def readable(name, key):
    """Como `ResortCatalog.isReadable` de la app: cada letra, del alfabeto latino o, en ruso,
    del cirílico y, en japonés, kanji o kana."""
    if LATIN.match(name):
        return True
    scripts = ("LATIN",) + SCRIPTS.get(key, ())
    return all(not c.isalpha() or unicodedata.name(c, "").startswith(scripts) for c in name)


def category(lang, n):
    """Categoría de plural de CLDR (*Language Plural Rules*) para enteros."""
    if lang == "ja":
        return "other"
    if lang == "pl":
        return "one" if n == 1 else "few" if n % 10 in (2, 3, 4) and n % 100 not in (12, 13, 14) else "many"
    if lang == "cs":
        return "one" if n == 1 else "few" if n in (2, 3, 4) else "other"
    if lang == "ru":
        if n % 10 == 1 and n % 100 != 11:
            return "one"
        return "few" if n % 10 in (2, 3, 4) and n % 100 not in (12, 13, 14) else "many"
    return "one" if n == 1 else "other"


def phrase_category(lang, n):
    """Forma del sustantivo tras el número en la frase de la cabecera, en genitivo o locativo
    («z 3147 ośrodków», «w 63 krajach»): en ruso, la de singular con 1, 21, 31… (salvo 11);
    en los demás, solo con 1. Decisión propia, sin fuente."""
    if lang == "ru":
        return "one" if n % 10 == 1 and n % 100 != 11 else "other"
    return "one" if n == 1 else "other"


def display_name(r, key):
    """El nombre en el idioma de la página si lo hay; si el original no usa el alfabeto
    latino, el inglés, con el original entre paréntesis."""
    own = r.get(key)
    if own:
        return own, r["name"] if own != r["name"] else None
    if not readable(r["name"], key) and r.get("name_en"):
        return r["name_en"], r["name"]
    return r["name"], None


def render(lang, data):
    t = TEXT[lang]
    resorts = data["resorts"]
    by_country = collections.defaultdict(list)
    for r in resorts:
        by_country[r[t["country"]]].append(r)
    countries = sorted(by_country, key=fold)
    # Separador de miles: punto en español, alemán, italiano y neerlandés, espacio fino en francés, coma en inglés.
    # En los idiomas nuevos, como `Int.formatted()` de Foundation: espacio duro en polaco, checo, sueco,
    # ruso y portugués (en polaco y portugués, solo desde 10 000), punto en danés y coma en japonés.
    sep = {"es": ".", "de": ".", "fr": "\u202f", "it": ".", "nl": ".", "pl": "\u00a0", "cs": "\u00a0", "sv": "\u00a0",
           "da": ".", "ru": "\u00a0", "pt": "\u00a0"}.get(lang, ",")
    min_group = 10000 if lang in ("pl", "pt") else 1000
    fmt = lambda n: f"{n:,}".replace(",", sep) if n >= min_group else str(n)
    words = {k: v[phrase_category(lang, len(resorts) if k == "rw" else len(countries))] for k, v in t.get("words", {}).items()}
    intro = t["intro"].format(n=fmt(len(resorts)), c=len(countries), **words)
    alternates = "".join(f'<link rel="alternate" hreflang="{o["lang"]}" href="{SITE}{o["dir"]}">\n'
                         for k, o in TEXT.items() if k != lang)
    others = " · ".join(f'<a href="{t["root"]}{o["dir"]}" hreflang="{o["lang"]}" lang="{o["lang"]}">{o["label"]}</a>'
                        for k, o in TEXT.items() if k != lang)
    e = html.escape
    out = [f"""<!doctype html>
<html lang="{t['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(t['title'])}</title>
<meta name="description" content="{e(intro)}">
<link rel="canonical" href="{SITE}{t['dir']}">
{alternates}<link rel="stylesheet" href="{t['css']}">
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
<p>{e(intro)}</p>
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
        if "counts" in t:
            count = t["counts"][category(lang, n)].format(n=fmt(n))
        else:
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
<footer>{e(t['footer'])} · {others}</footer>
</main>
<script>
(() => {{
  const input = document.getElementById("buscar"), empty = document.getElementById("vacio");
  const groups = [...document.querySelectorAll("#lista details")];
  const fold = s => s.normalize("NFD").replace(/\\p{{Mn}}/gu, "").toLowerCase();
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
