# SamiSalud — Telemedicina

Página informativa para socios de SamiSalud sobre el servicio de videoconsulta
médica, prestado a través de la app **Doctor en Casa · Convenios** (Grupo Ayuda
Médica).

## Contenido

| Ruta | Qué es |
|---|---|
| `index.html` | La página completa, autónoma. Se abre en cualquier navegador. |
| `privacidad.html` | Política de privacidad completa del servicio, enlazada desde las preguntas frecuentes. |
| `imagenes/` | Capturas de la app (iOS) y logo. |
| `wordpress/telemedicina-wordpress.html` | La misma página como bloque HTML para pegar en WordPress, con el CSS acotado bajo `.sami-tm`. |
| `wordpress/privacidad-wordpress.html` | La política de privacidad como bloque HTML para WordPress, con el CSS acotado bajo `.sami-lg`. |
| `wordpress/LEEME.txt` | Instrucciones paso a paso para montarla en WordPress. |

## Estado

**Borrador. No publicar todavía.**

No quedan datos en amarillo. Los tres pendientes originales de la página de
telemedicina están resueltos: el fundamento del art. 12 de la Ley 25.326, el
plazo de conservación (Ley 26.529, art. 18: diez años) y el responsable de la
base de datos, más el link a `privacidad.html`.

El responsable declarado es **Grupo Ayuda Médica A.C.E.**, CUIT 30-71113973-3,
domicilio legal en Sarmiento 4260, CABA.

Antes de publicar hay que **confirmar con asesoría legal** dos textos que se
afirman en la página y en la política:

- Que los términos y condiciones que el socio acepta al registrarse incluyan
  efectivamente el consentimiento expreso para la transferencia internacional
  de datos sensibles (Ley 25.326, art. 12). Los servidores de AWS y Twilio
  están en Estados Unidos.
- Que Grupo Ayuda Médica sea el responsable de la base de datos declarado,
  y no SamiSalud o una figura compartida entre ambos.

## Notas sobre las capturas

- Los datos de la pantalla de historia clínica son **de ejemplo**, no reales.
  Se editaron para reemplazar los datos de prueba que traía el build
  (`Test Ayelen Maité`, `Admin Admin`).
- La pantalla de selección de especialidad se editó para mostrar las dos
  especialidades disponibles. En la app real solo aparecen las que en ese
  momento tienen un profesional conectado.
- Los campos de contraseña de la pantalla de registro se completaron con
  puntos de enmascarado.

## Pendientes de producto (para el equipo de desarrollo)

Errores de texto detectados en la app durante la revisión:

- Login: `¿Todavia no tenes cuenta? Registrate aqui` — faltan las tres tildes.
- Modal de especialidad: `Selecciona la especialidad del medico que deseas que
  te atienda` — mezcla tuteo con el voseo del resto de la app y falta la tilde
  en «médico».
- Sala de espera: `¡Ya te encuentras en lista de espera!` — debería ser
  «encontrás».
- Diálogo de cancelación: el botón `Si` va con tilde.
- Home iOS: `uno de nuestro doctores` — falta la «s». En Android está bien.
- Solapa Noticias en Android: se renderizan dos botones flotantes de WhatsApp
  superpuestos.

## Aviso

Este repositorio contiene capturas de una aplicación de salud y referencias a
la marca de un tercero. **No hacerlo público** sin autorización de SamiSalud y
de Grupo Ayuda Médica.
