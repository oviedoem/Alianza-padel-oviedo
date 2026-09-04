## Estado sesión 2026-09-04
**Versión activa:** repo recién creado, primera campaña en curso (apertura)
**Deploy:** N/A (no hay hosting propio en este repo — piezas se publican manualmente en Instagram/Facebook)
**Commits:** múltiples en `oviedoem/Alianza-padel-oviedo` (main) + 3 commits en `oviedoem/oviedo-whatsapp-bot` (main)

### Hecho en esta sesión
- Creado el repo `oviedoem/Alianza-padel-oviedo` desde cero (no existía).
- `README.md`: contexto estratégico, copys oficiales (incluye 2 ganchos de apertura nuevos aprobados), datos de contacto, manual de estilo, formatos de exportación por canal (IG/FB 1:1 y 4:5, Stories/Reels/TikTok 9:16, WhatsApp, banner panel-admin/cliente con medidas reales), estado de campaña y alerta de tráfico, y sección "Errores Reales Documentados" (5 fallas reales de una generación previa con Gemini).
- `CLAUDE.md`: reglas operativas + bloque de copys oficiales duplicado a propósito al inicio (ver nota técnica dentro del archivo — necesario porque herramientas externas leen CLAUDE.md O README.md, nunca ambos), reglas de video (sin vocero, subtítulos obligatorios, IA generativa de Descript prohibida), tabla de herramientas (HTML/CSS por código = herramienta principal para flyers; Descript para video; Canva NO autorizado; skills de arte generado descartadas para piezas publicitarias).
- Assets subidos: `assets/logos/`, `assets/fotos-sucursal/`, `assets/fotos-padel-rocks/` (8 fotos reales del complejo), `assets/piezas-referencia/` (18 flyers ya publicados, referencia de formato), `assets/errores-a-evitar/` (5 capturas de fallas reales de Gemini), `assets/video/` (vacía, en `.gitignore`, pendiente de clips).
- **2 piezas de flyer aprobadas y en `output/`:**
  - `flyer-apertura-oviedo-express-1x1.png` (feed IG/FB, canal `@oviedo_elmanzano` — 572 seguidores, mayor alcance) + caption.
  - `flyer-apertura-oviedo-express-9x16.png` (Stories/Reels) + caption.
  - Plantillas HTML reutilizables en `plantillas/flyer-apertura-1x1.html` y `-9x16.html` (renderizadas con Chromium headless + recorte con Pillow — método documentado más abajo).
- Panel de Agentes IA (`oviedo-agentes-panel.onrender.com`, vive en repo `oviedo-whatsapp-bot`):
  - Agregado `alianza-padel-oviedo` a `contexto/repos.json` (path local esperado: `E:\alianza-padel-oviedo`).
  - Insertada manualmente la sección del proyecto en `contexto/negocio.md` (parche temporal — se reemplaza solo la próxima vez que se corra `ACTUALIZAR_CONTEXTO_BOT.bat` en el PC con el repo ya clonado).
  - Diagnosticado que el botón "Ejecutar revisión completa" del panel NO sirve para este proyecto (está cableado para auditoría de stock/ERP de la ferretería). Usar "Generar idea" o "Consulta rápida" en su lugar.

### Datos de negocio relevantes (no asumidos, verificados)
- Solo 1 visita al punto de venta en 2 días desde la apertura — prioridad de contenido: visibilidad, no conversión.
- `@oviedo_elmanzano`: 572 seguidores (canal principal). `@padel_rocks_rapel`: 327 seguidores (refuerzo/cross-tag).
- Reel de co-branding ya publicado antes tuvo 159 views vs 332-511 de otros posts de la misma cuenta — causa no confirmada.
- Reservas Pádel vía app **EasyCancha** (club "Padel Rocks Rapel" en https://www.easycancha.com/es-CL/chile/club/padel-rocks-rapel) además de WhatsApp — es el link oficial para el QR dinámico.

### Pendiente
- Correr `ACTUALIZAR_CONTEXTO_BOT.bat` en el PC (con `alianza-padel-oviedo` ya clonado en `E:\alianza-padel-oviedo`) para que `negocio.md` se regenere de forma automática y reemplace el parche manual.
- Subir clips de video reales a `assets/video/` (no versionados en git) para arrancar el flujo de Descript.
- Publicar las 2 piezas aprobadas en Instagram, reforzando con historias los días siguientes (variable no probada la vez anterior).
- Definir si hay un incentivo/promo real para los primeros clientes (no inventado por IA) — quedó como pregunta abierta sin cerrar.
- Confirmar si el muñequito/mascota que apareció en una generación de Gemini debía usarse — ya se definió que NO es oficial, queda prohibido explícitamente.

### Próxima sesión debe empezar por
- Verificar en `oviedo-agentes-panel.onrender.com/agentes` que el proyecto `alianza-padel-oviedo` sigue mostrando los copys correctos (probar con "Generar idea").
- Si ya se corrió el `.bat` local: confirmar que `negocio.md` se regeneró bien (buscar la sección `## alianza-padel-oviedo`).
- Seguir con la tercera pieza de contenido (banner panel-admin/cliente, o video si ya hay clips en `assets/video/`).
