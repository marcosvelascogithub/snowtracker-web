# SnowTracker · web

Política de privacidad y soporte de la app SnowTracker, publicadas con GitHub Pages, en español, en inglés y en alemán.

| Página | Español | Inglés | Alemán |
|---|---|---|---|
| Portada (URL de marketing) | https://marcosvelascogithub.github.io/snowtracker-web/ | https://marcosvelascogithub.github.io/snowtracker-web/en/ | https://marcosvelascogithub.github.io/snowtracker-web/de/ |
| Soporte | https://marcosvelascogithub.github.io/snowtracker-web/soporte/ | https://marcosvelascogithub.github.io/snowtracker-web/en/support/ | https://marcosvelascogithub.github.io/snowtracker-web/de/support/ |
| Privacidad | https://marcosvelascogithub.github.io/snowtracker-web/privacidad/ | https://marcosvelascogithub.github.io/snowtracker-web/en/privacy/ | https://marcosvelascogithub.github.io/snowtracker-web/de/datenschutz/ |
| Datos de OpenStreetMap (ODbL) | https://marcosvelascogithub.github.io/snowtracker-web/datos-osm/ | https://marcosvelascogithub.github.io/snowtracker-web/en/osm-data/ | https://marcosvelascogithub.github.io/snowtracker-web/de/osm-daten/ |

Las capturas de la portada son las capturas en bruto del iPhone de 6,9" de `docs/app-store/` del repositorio de la app, a la mitad de tamaño: en `img/`, en español, y en `img/en/`, en inglés. La cabecera (`img/cabecera.jpg`, 2400 × 1029) no lleva texto y vale para las dos: sale de `cabecera()` de `docs/app-store/scripts/componer-cabecera.py` con el titular vacío.

Las cifras de estaciones de la portada (total, países y los seis países con más estaciones) salen de `datos/estaciones.json`; se actualizan cuando cambia la lista.

Los ficheros de `datos-osm/` son los de `SnowTracker/Pistes/` de la app, publicados por la licencia ODbL (apartado 4.6). Se sustituyen con cada versión que regenere los datos, y se actualiza la fecha del extracto en las dos páginas.

La portada en alemán (`de/`) usa de momento las capturas en inglés (`img/en/`), con millas y pies, hasta que haya capturas en alemán (marcosvelascogithub/snowtracker#295). Los países de las estaciones en alemán (`country_de` de `datos/estaciones.json`) salen de `NAME_DE` de Natural Earth; `name_de` está vacío hasta que el script de la app lea `name:de` de OpenStreetMap.
