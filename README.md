# SamiSalud — Telemedicina

Página informativa para socios de SamiSalud sobre el servicio de videoconsulta
médica, prestado a través de la app **Doctor en Casa · Convenios** (Grupo Ayuda
Médica).

## Contenido

| Ruta | Qué es |
|---|---|
| `index.html` | La página completa, autónoma. Se abre en cualquier navegador. |
| `imagenes/` | Capturas de la app (iOS) y logo. |
| `wordpress/telemedicina-wordpress.html` | La misma página como bloque HTML para pegar en WordPress, con el CSS acotado bajo `.sami-tm`. |
| `wordpress/LEEME.txt` | Instrucciones paso a paso para montarla en WordPress. |

## Estado

**Borrador. No publicar todavía.**

Quedan tres datos por completar, marcados en amarillo dentro de la página
(buscar `class="todo"`):

1. Confirmar con asesoría legal que los términos y condiciones que el socio
   acepta al registrarse incluyan el consentimiento para la transferencia
   internacional de datos sensibles (Ley 25.326, art. 12). Los servidores de
   AWS y Twilio están en Estados Unidos.
2. Plazo de conservación de las consultas y responsable de la base de datos.
3. Link a la política de privacidad completa.

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
