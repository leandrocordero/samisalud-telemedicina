# -*- coding: utf-8 -*-
"""Prepara las imagenes del pack de Instagram a partir de ../imagenes.

- Del logo saca el fondo blanco (el original viene en RGB, sin transparencia)
  y genera ademas una version en blanco puro para las placas azules.
- Achica las capturas de la app a 560 px de ancho.

Uso:  python preparar-imagenes.py     (necesita Pillow)
"""
import os
from PIL import Image

AQUI = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(AQUI, '..', 'imagenes')
OUT = AQUI

# --- logo: sacar el fondo blanco (unpremultiply sobre blanco) ---
im = Image.open(os.path.join(SRC, 'sami-logo.png')).convert('RGB')
out = []
for r, g, b in im.getdata():
    a = 255 - min(r, g, b)
    if a == 0:
        out.append((0, 0, 0, 0))
    else:
        k = 255 - a
        out.append((
            max(0, min(255, (r - k) * 255 // a)),
            max(0, min(255, (g - k) * 255 // a)),
            max(0, min(255, (b - k) * 255 // a)),
            a))
logo = Image.new('RGBA', im.size)
logo.putdata(out)
logo = logo.crop(logo.getbbox())

w = 640
logo = logo.resize((w, round(logo.height * w / logo.width)), Image.LANCZOS)
logo.save(os.path.join(OUT, 'sami-logo.png'), optimize=True)

# version blanca: el verde del logo da alpha ~208 con la formula de arriba,
# asi que la normalizo para que no quede mas transparente que el azul
alpha = logo.getchannel('A').point(lambda v: min(255, v * 255 // 208))
blanco = Image.new('RGBA', logo.size, (255, 255, 255, 0))
blanco.putalpha(alpha)
blanco.save(os.path.join(OUT, 'sami-logo-blanco.png'), optimize=True)

# --- capturas de la app ---
for name in ['app-01-ingreso', 'app-02-empresa', 'app-03-cuenta',
             'app-04-especialidad', 'app-05-espera', 'app-inicio']:
    s = Image.open(os.path.join(SRC, name + '.jpg')).convert('RGB')
    s = s.resize((560, round(s.height * 560 / s.width)), Image.LANCZOS)
    s.save(os.path.join(OUT, name + '.jpg'), quality=80, optimize=True, progressive=True)

print('listo')
