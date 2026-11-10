# SnowTracker · web

Política de privacidad y soporte de la app SnowTracker, publicadas con GitHub Pages, en español, en inglés, en alemán, en francés y en italiano.

| Página | Español | Inglés | Alemán | Francés | Italiano |
|---|---|---|---|---|---|
| Portada (URL de marketing) | https://marcosvelascogithub.github.io/snowtracker-web/ | https://marcosvelascogithub.github.io/snowtracker-web/en/ | https://marcosvelascogithub.github.io/snowtracker-web/de/ | https://marcosvelascogithub.github.io/snowtracker-web/fr/ | https://marcosvelascogithub.github.io/snowtracker-web/it/ |
| Soporte | https://marcosvelascogithub.github.io/snowtracker-web/soporte/ | https://marcosvelascogithub.github.io/snowtracker-web/en/support/ | https://marcosvelascogithub.github.io/snowtracker-web/de/support/ | https://marcosvelascogithub.github.io/snowtracker-web/fr/assistance/ | https://marcosvelascogithub.github.io/snowtracker-web/it/assistenza/ |
| Privacidad | https://marcosvelascogithub.github.io/snowtracker-web/privacidad/ | https://marcosvelascogithub.github.io/snowtracker-web/en/privacy/ | (enlaza a la inglesa) | (enlaza a la inglesa) | (enlaza a la inglesa) |
| Datos de OpenStreetMap (ODbL) | https://marcosvelascogithub.github.io/snowtracker-web/datos-osm/ | https://marcosvelascogithub.github.io/snowtracker-web/en/osm-data/ | https://marcosvelascogithub.github.io/snowtracker-web/de/osm-daten/ | https://marcosvelascogithub.github.io/snowtracker-web/fr/donnees-osm/ | https://marcosvelascogithub.github.io/snowtracker-web/it/dati-osm/ |

Las capturas de la portada son las capturas en bruto del iPhone de 6,9" de `docs/app-store/` del repositorio de la app, a la mitad de tamaño: en `img/`, en español, y en `img/en/`, `img/de/` e `img/fr/`, en inglés, alemán y francés. La cabecera (`img/cabecera.jpg`, 2400 × 1029) no lleva texto y vale para las dos: sale de `cabecera()` de `docs/app-store/scripts/componer-cabecera.py` con el titular vacío.

Las cifras de estaciones de la portada (total, países y los seis países con más estaciones) salen de `datos/estaciones.json`; se actualizan cuando cambia la lista.

Los ficheros de `datos-osm/` son los de `SnowTracker/Pistes/` de la app, publicados por la licencia ODbL (apartado 4.6). Se sustituyen con cada versión que regenere los datos, y se actualiza la fecha del extracto en las dos páginas.

La portada en alemán (`de/`) usa las capturas en alemán (`img/de/`). Los países de las estaciones en alemán (`country_de` de `datos/estaciones.json`) salen de `NAME_DE` de Natural Earth; `name_de` está vacío hasta que el script de la app lea `name:de` de OpenStreetMap.

La portada en francés (`fr/`) usa las capturas en francés (`img/fr/`), de la versión 1.2 de la app. Los nombres y países en francés (`name_fr` y `country_fr` de `datos/estaciones.json`) salen de `name:fr` de OpenStreetMap y de `NAME_FR` de Natural Earth. La insignia `img/app-store/fr.svg` es la oficial de Apple (toolbox.marketingtools.apple.com, `fr-fr`), de la misma fuente que la alemana.

La portada en italiano (`it/`) usa de momento las capturas en inglés (`img/en/`); las italianas se harán al final, con las de la App Store. Los nombres y países en italiano (`name_it` y `country_it` de `datos/estaciones.json`) salen de `name:it` de OpenStreetMap y de `NAME_IT` de Natural Earth. La insignia `img/app-store/it.svg` es la oficial de Apple (toolbox.marketingtools.apple.com, `it-it`), de la misma fuente que la francesa.
