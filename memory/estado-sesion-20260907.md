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
