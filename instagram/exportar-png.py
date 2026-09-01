# -*- coding: utf-8 -*-
"""Exporta cada placa .dc.html a PNG, con Chrome o Edge en modo headless.

Los PNG salen en png/, a tamano real (1080 px de ancho), listos para subir.
Volve a correrlo cada vez que edites una placa.

Uso:  python exportar-png.py
"""
import io, json, os, re, shutil, subprocess, unicodedata

AQUI = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(AQUI, 'png')
TMP = os.path.join(AQUI, '_render')

NAVEGADORES = [
    r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe',
    r'C:\Program Files\Google\Chrome\Application\chrome.exe',
    r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe',
    r'C:\Program Files\Microsoft\Edge\Application\msedge.exe',
]
navegador = next((p for p in NAVEGADORES if os.path.exists(p)), None)
if not navegador:
    raise SystemExit('No encontre Chrome ni Edge. Editalos en NAVEGADORES.')


def slug(s):
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode()
    s = s.lower().replace('\u00b7', '-')
    return re.sub(r'[^a-z0-9]+', '-', s).strip('-')


def plano(src):
    """El .dc.html es formato de lienzo; lo paso a un HTML que el navegador abre."""
    helmet = re.search(r'<helmet>(.*?)</helmet>', src, re.S)
    head = helmet.group(1) if helmet else ''
    cuerpo = re.search(r'<x-dc>(.*?)</x-dc>', src, re.S).group(1)
    if helmet:
        cuerpo = cuerpo.replace(helmet.group(0), '')
    return ('<!doctype html>\n<html lang="es-AR">\n<head>\n<meta charset="utf-8">\n'
            + head + '\n</head>\n<body>\n' + cuerpo.strip() + '\n</body>\n</html>\n')


os.makedirs(OUT, exist_ok=True)
if os.path.isdir(TMP):
    shutil.rmtree(TMP)
os.makedirs(TMP)

# las imagenes tienen que quedar al lado del html temporal
for f in os.listdir(AQUI):
    ruta = os.path.join(AQUI, f)
    if os.path.isfile(ruta) and f.lower().split('.')[-1] in ('png', 'jpg'):
        shutil.copy2(ruta, os.path.join(TMP, f))

cj = json.load(io.open(os.path.join(AQUI, 'canvas.json'), encoding='utf-8'))
for a in cj['artboards']:
    src = io.open(os.path.join(AQUI, a['file']), encoding='utf-8').read()
    tmp = os.path.join(TMP, a['file'].replace('.dc.html', '.html'))
    io.open(tmp, 'w', encoding='utf-8', newline='').write(plano(src))

    destino = os.path.join(OUT, slug(a['title']) + '.png')
    subprocess.run([
        navegador, '--headless=new', '--disable-gpu', '--hide-scrollbars',
        '--force-device-scale-factor=1', '--virtual-time-budget=9000',
        '--default-background-color=ffffffff',
        '--window-size=%d,%d' % (a['w'], a['h']),
        '--screenshot=' + destino,
        'file:///' + tmp.replace('\\', '/'),
    ], capture_output=True, text=True)
    print(('ok   ' if os.path.exists(destino) else 'FALLO') + '  ' + os.path.basename(destino))

shutil.rmtree(TMP)
