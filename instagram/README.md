# Pack de Instagram — lanzamiento de telemedicina

Trece placas para la cuenta de Instagram de SamiSalud, sobre el servicio de
videoconsulta. Usan la misma paleta, tipografías y textos que `index.html`.

El lienzo donde se ven y se editan las placas está publicado acá:
**https://claude.ai/code/artifact/16dccc72-a40e-4451-9b07-8d11d17eef7c**

Desde ahí se exporta cada placa como PNG a 1080 px reales, o todas juntas
como PDF.

## Las placas

| Archivo | Pieza | Medida |
|---|---|---|
| `Main.dc.html` | Carrusel 1 — portada | 1080×1350 |
| `Paso1.dc.html` … `Paso4.dc.html` | Carrusel 2 a 5 — pasos 1 a 4 | 1080×1350 |
| `Cierre.dc.html` | Carrusel 6 — paso 5 y cierre | 1080×1350 |
| `Historia1.dc.html` | Historia — el beneficio | 1080×1920 |
| `Historia2.dc.html` | Historia — qué podés consultar | 1080×1920 |
| `Historia3.dc.html` | Historia — receta digital | 1080×1920 |
| `ReelA.dc.html` | Portada de reel — tutorial | 1080×1920 |
| `ReelB.dc.html` | Portada de reel — gancho | 1080×1920 |
| `Feed1.dc.html` | Feed — anuncio | 1080×1080 |
| `Feed2.dc.html` | Feed — horarios | 1080×1080 |

`canvas.json` es la grilla: dónde se ubica cada placa en el lienzo y las
notas al costado de cada fila.

## Criterios de diseño

- Paleta y tipografías de la página: azul `#004B9C`, verde `#66B32F`, tinta
  `#15283A`, Barlow para títulos y Source Sans 3 para el texto.
- En las historias el contenido arranca a 268 px del borde superior y termina
  unos 300 px antes del inferior, para que no lo tape la interfaz de Instagram.
- En las portadas de reel el gancho está en la franja del medio, que es la
  parte que se ve recortada en la grilla del perfil.
- Los horarios que se prometen son los reales del servicio (9 a 22, todos los
  días). Cuidado al editar los ganchos: no plantear situaciones fuera de ese
  horario.

## Las imágenes

Salen de `../imagenes` y se regeneran con:

    python preparar-imagenes.py

El script achica las capturas y le saca el fondo blanco al logo, que viene en
RGB sin transparencia. Genera también `sami-logo-blanco.png`, la versión en
blanco puro que se usa sobre los fondos azules.
