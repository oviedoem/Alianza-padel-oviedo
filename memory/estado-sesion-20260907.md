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

### Próxima sesión debe empezar por
- `git fetch && git log HEAD..origin/main --oneline` para confirmar sincronización (rutina ya establecida).
- Preguntar al dueño si `revision-apertura*.mp4` son las versiones finales reales antes de decidir su destino.

### Intento fallido de esta sesión — enviar los 2 videos de revisión al celular del dueño
Se probaron 3 vías, ninguna funcionó, no reintentar las mismas sin cambiar de método:
1. **WhatsApp Web (chat "Jefe Alejandro Oviedo Las Cabras" en la cuenta WhatsApp Business)** — bloqueado por límite de 10MB por archivo de la herramienta de subida del navegador (los videos pesan ~12MB c/u).
2. **Artifact HTML con video embebido en base64** — el video codificado supera el límite de 16MB total de un Artifact; no cabe ni un solo video.
3. **Subida directa a Descript vía URL firmada (import_media + PUT con curl/PowerShell)** — se creó el proyecto Descript "Revision Apertura Oviedo Express (temporal)" (`project_id: bb087182-933a-4891-9ea9-fbf98a41b388`, drive "Oviedo Manzano's Drive") pero la subida del archivo fue bloqueada por el clasificador de seguridad de Claude Code al detectar un PUT a una URL externa de storage con credenciales firmadas. **Este proyecto Descript quedó vacío/sin media** — o se completa la subida manualmente desde Descript, o se borra ese proyecto para no dejar basura en el drive.
- Decisión del dueño: dejarlo para revisar directamente en el PC (`E:\alianza-padel-oviedo\output\`) o por AnyDesk, no seguir insistiendo por estas 3 vías.
