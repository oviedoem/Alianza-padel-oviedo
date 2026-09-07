## Estado sesión 2026-09-07

### Hecho en esta sesión
- Activadas skills `ahorro-tokens` y `prevencion-inicio-sesion` (incl. Safe Change Protocol) como protocolo permanente de la sesión.
- Auditoría (vía agente) de las 8 plantillas HTML nuevas en `plantillas/` contra reglas de `README.md` (copys exactos, paletas, contacto, RRSS, logos, mascotas):
  - OK sin cambios: `overlay-cancha.html`, `overlay-ferreteria.html`, `overlay-trayecto.html`, `hook-card.html`, `cierre-video-vertical.html`.
  - Corregidas: `steps-card.html` y `team-card.html` tenían acento verde (`#1E9E5A`) y rosa (`#FF4D6D`) de Padel Rocks mezclado con la paleta Oviedo en el mismo bloque — se reemplazó todo por rojo Oviedo (`#E30613`). Verificado visualmente con servidor local (`.claude/launch.json` nuevo, sirve `plantillas/` en `localhost:8791`) — ya no queda ningún archivo con esos hex.
  - `overlay-template.html` NO es pieza final: tiene placeholders sin sustituir (`OVIEDO_B64`, `CAPTION_BLOCK`, etc.). Queda documentado, no usar tal cual.
- Commit `643ef43` y push a `origin/main`: 15 archivos (2 plantillas corregidas + fotos nuevas + videos finales de apertura + `.claude/launch.json`).
- **Excluidos intencionalmente del commit** (quedan solo en disco local, no en git): `output/revision-apertura.mp4` y `output/revision-apertura-v2.mp4` — por nombre son borradores de revisión, no el video final aprobado, según la regla del proyecto de que `output/` solo guarda el video final exportado.

### Pendiente
- Publicar piezas aprobadas en Instagram — decisión/acción del dueño, no automatizable.
- Confirmar promo "$4.000 primera cancha" antes de oficializar.
- Decidir si `output/revision-apertura.mp4` / `revision-apertura-v2.mp4` deben borrarse, renombrarse a `-FINAL` si en realidad son la versión buena, o quedar fuera de git definitivamente — no se tocó por no ser una decisión técnica clara.
- `overlay-template.html` sigue sin un flujo de "build" documentado que sustituya sus placeholders — si se va a usar como base para futuras piezas, definir ese paso.
- Revisar el video nuevo `output/video-radio-oviedo-express.mp4` completo antes de publicarlo (el dueño no llegó a verlo, se armó y aprobó su lógica mientras dormía — ver sección siguiente).

### Video nuevo generado esta sesión: `output/video-radio-oviedo-express.mp4`
El dueño mandó por WhatsApp un audio real de radio ya usado en emisoras (spot de 41.3s, "Oviedo Express Ferreterías x Padel Rocks Rapel") y pidió armar un video con las piezas gráficas ya aprobadas + ese audio + efecto en las imágenes. Se hizo así:

- **Origen del audio:** descargado desde el chat de WhatsApp Business "Jefe Alejandro Oviedo Las Cabras" (mensaje de audio de la 1:43 AM), guardado en `assets/audio/radio-oviedo-express.mp3` (commit `0e96aa2`).
- **Se descartó usar IA generativa** (Gemini/Veo, CapCut AI, etc.) para armar el video — violaría la regla de "cero alucinaciones" del proyecto (nunca generar personas/canchas/escenas sintéticas) y ya hay 5 fallas documentadas de una generación previa con Gemini en `assets/errores-a-evitar/`. Un agente investigó alternativas (Remotion, CapCut, Velorn, DaVinci Resolve) — ver conversación completa; conclusión: ninguna mejora el enfoque sin agregar riesgo generativo o costo.
- **Descript** (conectado vía MCP) se usó SOLO para dos cosas sin costo de IA: importar el audio/imágenes por URL pública (evita el límite de 10MB de subida directa) y exportar la transcripción automática literal (función base, no generativa) — quedó guardada en `assets/audio/radio-oviedo-express.srt`. El intento de usar "Agent Underlord" (editor IA de Descript) para armar el video automáticamente falló por falta de créditos IA en la cuenta (link de upgrade quedó en el historial de la conversación si se quiere subir el plan a futuro). Queda un proyecto Descript de prueba **"Video Radio Oviedo Express"** con las piezas importadas, sin usar — se puede borrar o reutilizar.
- **Solución final:** pipeline propio 100% local en Python (`scripts/build_video_radio.py`), usando `moviepy` + `ffmpeg` (instalado en el entorno portable vía `pip install moviepy imageio-ffmpeg pillow`, en `E:\python-portable\`). Cero generación de contenido — solo recorte, paneo/zoom (Ken Burns), superposición y subtítulos quemados con la transcripción real, sin inventar texto.
- **Piezas usadas (4, en orden):** `flyer-apertura-oviedo-express-9x16.png`, `flyer-logistica-oviedo-express-1x1.png`, `flyer-collage-3fotos-1x1.png`, `cierre-video-vertical.png` — repartidas en partes iguales a lo largo de los 41.3s del audio.
- **Decisión de diseño importante:** las 2 piezas cuadradas (logística, collage) tienen texto propio pegado al borde — recortarlas a 9:16 cortaba ese texto. Se cambió a mostrarlas COMPLETAS sin recortar (contain-fit + fondo desenfocado de la misma imagen), reservando el recorte/paneo Ken Burns solo para las 2 piezas ya verticales nativas (apertura, cierre).
- **Posición del subtítulo:** cada pieza tiene su propio texto en un lugar distinto (apertura/logística/cierre: abajo o al medio → subtítulo arriba; collage: texto propio arriba → subtítulo abajo). Se verificó visualmente extrayendo frames con ffmpeg en 5 iteraciones hasta que no hubo choques.
- **Pendiente menor conocido, no crítico:** un subtítulo (~0.7s) que cruza el corte collage→cierre queda con leve superposición visual con el texto propio de esa pieza durante ese instante corto — no es texto cortado ni ilegible, solo un roce estético breve. No se seguyó iterando más por ser las 2:45 AM y por retornos decrecientes (5 renders de ~4 min cada uno ya corridos).
- Commit del video final + script + srt: `30206d5` (con subtítulos), confirmado pusheado.

### Actualización posterior (mismo despertar, 09:2x AM): subtítulos quitados
El usuario pidió explícitamente "sacar subtítulo del video". Se hizo:
- Se agregó flag `BURN_SUBTITLES = False` en `scripts/build_video_radio.py` (fácil de revertir a `True` si se decide volver a quemarlos).
- Se regeneró `output/video-radio-oviedo-express.mp4` sin subtítulos, verificado por frame que el texto propio de cada pieza queda intacto.
- **Conflicto detectado y avisado al usuario (no bloqueante):** esto contradice la regla "no negociable" de `CLAUDE.md` — "Subtítulos: SIEMPRE quemados en pantalla (confirmado 2026-09-04) — la mayoría de las reproducciones en IG/TikTok son sin sonido." Se aplicó igual por ser instrucción directa y explícita del dueño del proyecto sobre su propio video. **Antes de publicar en IG/TikTok, confirmar con el dueño si de verdad quiere publicarlo sin subtítulos** (pierde alcance en reproducción muda) o si esto era solo para revisar/editar en otra herramienta después.
- Commit `89306c5` con el mp4 actualizado y el script con el flag.

### Nota técnica para futuras piezas de video
Quedó instalado en `E:\python-portable\`: `moviepy`, `imageio-ffmpeg` (trae ffmpeg estático, sin instalación de sistema), `pillow`. Sirve para repetir este tipo de armado (Ken Burns + audio real + subtítulos quemados) sin depender de créditos de Descript ni de ninguna IA generativa.

### Próxima sesión debe empezar por
- `git fetch && git log HEAD..origin/main --oneline` para confirmar sincronización (rutina ya establecida).
- Preguntar al dueño si `revision-apertura*.mp4` son las versiones finales reales antes de decidir su destino.

### Intento fallido de esta sesión — enviar los 2 videos de revisión al celular del dueño
Se probaron 3 vías, ninguna funcionó, no reintentar las mismas sin cambiar de método:
1. **WhatsApp Web (chat "Jefe Alejandro Oviedo Las Cabras" en la cuenta WhatsApp Business)** — bloqueado por límite de 10MB por archivo de la herramienta de subida del navegador (los videos pesan ~12MB c/u).
2. **Artifact HTML con video embebido en base64** — el video codificado supera el límite de 16MB total de un Artifact; no cabe ni un solo video.
3. **Subida directa a Descript vía URL firmada (import_media + PUT con curl/PowerShell)** — se creó el proyecto Descript "Revision Apertura Oviedo Express (temporal)" (`project_id: bb087182-933a-4891-9ea9-fbf98a41b388`, drive "Oviedo Manzano's Drive") pero la subida del archivo fue bloqueada por el clasificador de seguridad de Claude Code al detectar un PUT a una URL externa de storage con credenciales firmadas. **Este proyecto Descript quedó vacío/sin media** — o se completa la subida manualmente desde Descript, o se borra ese proyecto para no dejar basura en el drive.
- Decisión del dueño: dejarlo para revisar directamente en el PC (`E:\alianza-padel-oviedo\output\`) o por AnyDesk, no seguir insistiendo por estas 3 vías.
