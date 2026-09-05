## Estado sesión 2026-09-05
**Versión activa:** primera campaña (apertura) — 3 piezas aprobadas (2 publicadas + 1 nueva lista para publicar)
**Deploy:** N/A (sin hosting propio en este repo)
**Commits:** varios (ver detalle abajo — fotos nuevas + tercera pieza)

### Hecho en esta sesión
- Verificado estado del repo: rama `claude/alianza-padel-oviedo-status-py3w19` limpia y sincronizada, README.md y CLAUDE.md consistentes entre sí.
- Confirmado con el dueño que de los 5 pendientes de la sesión 2026-09-04, quedaron resueltos:
  - `ACTUALIZAR_CONTEXTO_BOT.bat` corrido — `negocio.md` (repo `oviedo-whatsapp-bot`) ya tiene la sección del proyecto regenerada automáticamente, reemplazando el parche manual.
  - Las 2 piezas de apertura (flyer 1:1 feed + 9:16 Stories/Reels) ya se publicaron en Instagram con sus captions.

### Pendiente (sigue abierto)
- Subir clips de video reales a `assets/video/` (carpeta vacía, gitignored) para arrancar el flujo de edición con Descript.
- Confirmar texto exacto/vigencia de la promo "$4.000 primera cancha" (ver hallazgo abajo) antes de oficializarla como copy en README/CLAUDE.md.
- Reforzar con historias los días siguientes a la publicación (variable no probada la vez anterior) — evaluar resultado de alcance de las 2 piezas ya publicadas.

### Hallazgo importante (fotos nuevas recibidas en esta sesión)
El dueño entregó 16 fotos originales nocturnas del punto Oviedo Express dentro de Padel Rocks (deck, canchas, cartelería, camioneta con banner, mesa de productos). Guardadas en:
- `assets/fotos-padel-rocks/2026-09/` (9 fotos: canchas y deck nocturno)
- `assets/fotos-sucursal/2026-09/` (7 fotos: cartelería Oviedo Express/Ferreterías MTS, camioneta, mesa de productos)

Una de ellas (`mesa-productos-banner-promo-4000-01.jpg`) muestra un banner físico real en el local con una promo ya vigente para primeros clientes:
> "Ya que estás aquí... ¿Te animas a jugar? Juega tu primera cancha por $4.000 — 60 min + palas incluidas. Beneficio exclusivo Punto Oviedo. Escanea y reserva."

Esto resolvería el pendiente abierto de "definir promo/incentivo para primeros clientes" — **pero el dueño pidió NO oficializarla todavía en README/CLAUDE.md** hasta confirmar el texto exacto/vigencia. Queda pendiente de decisión, no de generación de piezas nuevas con ese copy hasta que se confirme.

### Tercera pieza aprobada (2026-09-05)
- **Flyer 1:1** `output/flyer-logistica-oviedo-express-1x1.png` (2160×2160, HD — 2x el estándar 1080×1080 de IG/FB, renderizado nativo del HTML sin upscaling) + caption en `output/flyer-logistica-oviedo-express-1x1-caption.txt`.
- Copy usado: "Texto de Facilidad Logística" oficial del README ("¿Construyendo en Rapel?...") + CTA ferretería.
- Foto de fondo: `assets/fotos-sucursal/2026-09/cartel-oviedo-ferreterias-mts-01-realzada.jpg` — foto real del cartel Oviedo Ferreterías + bandera chilena en el local, con brillo/contraste/nitidez realzados vía Pillow (Brightness 1.55, Contrast 1.12, Sharpness 2.0 + UnsharpMask) sobre la foto original, sin alterar contenido ni agregar elementos sintéticos.
- Plantilla nueva: `plantillas/flyer-logistica-1x1.html` (mismo layout que las 2 piezas anteriores: badges de ambos logos + gradiente + contactbar).
- **Aprobada por el dueño 2026-09-05** — lista para publicar en Instagram.

### Cuarta pieza: intento rechazado + versión aprobada
- **Intento 1 (rechazado):** `flyer-cta-padel-1x1.png` — cancha con demasiado lens flare/luces, "no se ve nada". Descartado y eliminado de `output/` (commit `edbb074`). Aprendizaje: evitar fondos con luces de cancha directas al lente; preferir tomas de deck/terraza o encuadres sin la fuente de luz en cámara.
- **Intento 2 (aprobado):** `output/flyer-collage-3fotos-1x1.png` (2160×2160 HD) — collage de 3 fotos reales completas, sin recortar (`object-fit:contain`, no `cover`): deck de Padel Rocks, cartel Oviedo Express, y el punto de venta en el deck. Brillo/contraste realzados de forma moderada (Brightness 1.15, Contrast 1.05 — mucho más suave que la pieza 3, a pedido explícito de "sin tanta luz").
- Copy usado: "Mensaje de Gancho" oficial ("Ven por el pádel, sal con tus materiales...") + Slogan principal en el caption.
- Incluye ambos logos, ambos teléfonos (WhatsApp Ferretería + Reservas Pádel) y ambos handles de Instagram.
- Plantilla: `plantillas/flyer-collage-3fotos-1x1.html`.
- Caption: `output/flyer-collage-3fotos-1x1-caption.txt`.
- **Aprobada por el dueño 2026-09-05** — lista para publicar.

### Próxima sesión debe empezar por
- Publicar la tercera y cuarta pieza (`flyer-logistica-oviedo-express-1x1.png` y `flyer-collage-3fotos-1x1.png`, con sus captions) en `@oviedo_elmanzano`.
- Revisar métricas reales de las piezas ya publicadas (alcance/views) para decidir si repetir el formato o ajustar.
- Si ya hay definición de promo "$4.000": redactar el copy siguiendo las reglas del README (nada inventado) y generar una pieza nueva.
- Si ya hay clips en `assets/video/`: iniciar el flujo con Descript (Agent Underlord) respetando las reglas de video (sin IA generativa, subtítulos quemados, sin música por ahora).
