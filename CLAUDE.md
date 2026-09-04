# CLAUDE.md — Alianza Padel Rocks Rapel × Ferretería Oviedo Express

Este archivo se carga automáticamente al inicio de cada sesión de Claude Code en este repo.

## 📋 COPYS OFICIALES (texto exacto — fuente de verdad duplicada aquí a propósito)

> Nota técnica: esta sección repite textual el contenido de README.md § "Copys y Slogans Oficiales".
> Es una duplicación deliberada: herramientas externas (ej. paneles de agentes IA de otros repos del
> ecosistema) leen CLAUDE.md primero y, si existe, NO leen README.md — así que si esto no está acá,
> esas herramientas "no ven" los copys reales. Si se edita un copy, actualizar en AMBOS archivos.

- Slogan principal: "Juega. Cotiza. Retira. Todo en un solo lugar."
- Mensaje de gancho: "Ven por el pádel, sal con tus materiales: Oviedo Express atiende dentro del club."
- Texto de facilidad logística: "¿Construyendo en Rapel? Cotiza en la mañana y retira tus materiales en el pádel desde las 15:30 hrs. ¡Aprovecha tu tarde jugando!"
- CTA pádel: "No te quedes sin jugar. ¡Escanea el código QR y asegura tu horario ahora mismo!"
- CTA ferretería: "Cotiza y compra aquí. Despacho en el día o Retiro de productos desde las 15:30 hrs."
- Gancho de apertura: "Nuevo en Rapel: Oviedo Express ya está funcionando dentro de Padel Rocks."
- Gancho de apertura (emocional): "Desde hoy, cada vez que vengas a jugar, tu obra también avanza."
- Contacto: WhatsApp Ferretería +569 3862 3488 · Reservas Pádel +569 5923 7808 · Sector El Estero S/N, Las Cabras · RRSS: `@padel_rocks_rapel` y `@oviedo_elmanzano`

## LEER OBLIGATORIO ANTES DE CUALQUIER TAREA

1. Leer `README.md` — contexto estratégico, copys oficiales, datos de contacto, manual de estilo y reglas de control de identidad. Es la fuente de verdad única para todo texto y diseño generado en este repo.
2. No generar ninguna pieza (flyer, video, PPTX, HTML) sin haber releído `README.md` en esa sesión — los copys, colores y reglas anti-alucinación pueden actualizarse ahí.

## REGLAS NO NEGOCIABLES (resumen operativo)

- **Textos:** usar solo los copys/slogans listados en README.md § "Copys y Slogans Oficiales". No inventar variantes, no completar frases, no generar texto sintético en las piezas.
- **Marcas y RRSS:** únicos handles válidos: `@padel_rocks_rapel` y `@oviedo_elmanzano`. No mezclar extensiones de archivo ni inventar nombres.
- **Contacto:** WhatsApp Ferretería `+569 3862 3488`, Reservas Pádel `+569 5923 7808` — nunca intercambiar ni fusionar ambos números.
- **Identidad visual:** no mezclar paletas — Oviedo (rojo/blanco/negro industrial) y Padel Rocks (verde/blanco/rosa pastel) se mantienen segmentadas por marca, nunca combinadas en un mismo bloque cromático.
- **Logos:** nunca redibujar ni regenerar con IA — siempre insertar el archivo real de `assets/logos/`. No deformar, estirar, recortar ni pixelar. Proporciones originales siempre.
- **Personas/uniformes reales:** prohibido inpainting o sustitución de fondo sobre fotos de personal con uniforme oficial Oviedo (MTS, SOLMAQ, DIKMAN, BLACK+FRESEN visibles). Personas y escenas SIEMPRE de foto real (`assets/fotos-padel-rocks/` o `assets/fotos-sucursal/`) — nunca generar una persona o cancha nueva.
- **Mascotas/personajes:** esta marca NO tiene mascota oficial. Prohibido crear o insertar cualquier personaje ilustrado/avatar.
- **Ver `assets/errores-a-evitar/`:** 5 fallas reales de una generación previa con Gemini (texto gibberish, logo redibujado, RRSS inventadas, persona de stock, contacto duplicado) — detalle en README.md § "Errores Reales Documentados". Repasar antes de aprobar cualquier pieza.
- **Entorno geográfico:** Sector El Estero, Las Cabras — nada de fondos artificiales (montañas nevadas, lagos tropicales, palmeras). Mantener canchas azules, terrazas de madera clara, pallets, toldos beige/arena.
- **QR dinámico:** siempre debe apuntar al link de reservas de pádel vigente en README.md — actualmente https://www.easycancha.com/es-CL/chile/club/padel-rocks-rapel (app/web EasyCancha, club "Padel Rocks Rapel").

## Antes de cualquier pieza nueva

```
PIEZA:       [flyer / video / story / pptx]
MARCA(S):    [Oviedo | Padel Rocks | ambas]
COPY USADO:  [cuál de los copys oficiales, textual]
NO TOCO:     [logos/fotos que se preservan íntegros]
```

## Estructura del repo

- `README.md` — fuente única de copys, contacto y reglas (no duplicar contenido en otros archivos)
- `assets/logos/` — logos oficiales Oviedo y Padel Rocks Rapel, badges
- `assets/fotos-sucursal/` — fotos reales de la sucursal Oviedo El Manzano
- `assets/fotos-padel-rocks/` — fotos reales del complejo (canchas, terraza, food truck)
- `assets/piezas-referencia/` — flyers/banners ya publicados por ambas marcas, usados solo como referencia de formato/composición (nunca como fuente de texto)
- `assets/video/` — clips de video reales para editar con Descript (ver § Herramientas)
- `assets/errores-a-evitar/` — capturas de fallas reales de una generación previa con Gemini (checklist de qué NO repetir, ver README.md)
- `plantillas/` — layouts HTML reutilizables para flyers (pendiente de crear)
- `output/` — piezas finales exportadas

## Herramientas — qué se usa para qué

| Necesidad | Herramienta | Por qué |
|---|---|---|
| Flyers (foto real + logo + texto) | **HTML/CSS por código** | Composición determinística: no toca píxeles de fotos ni logos, cero riesgo de alucinación. Se exporta a PNG. Es la herramienta principal del repo. |
| Video promocional (clips reales del club/sucursal) | **Descript** | Edita metraje ya filmado por texto (cortar, subtítulos, quitar muletillas). No genera video desde cero — necesita los clips en `assets/video/`. |
| Arte/diagramas 100% generados (ilustraciones, gráficos de datos) | Skills de diseño (canvas-design, dataviz, artifact-diagramming) | **Descartadas para piezas publicitarias** — dibujan desde cero, lo que viola la regla de fidelidad geográfica/de personas. Solo aptas para material interno no publicitario (ej. un diagrama de flujo para capacitación). |
| Generación de imágenes fotorrealistas nuevas (tipo Midjourney/DALL-E) | No disponible / no se usa | Además de no estar conectada, iría directamente contra la regla "cero alucinaciones" del manual — no hace falta. |
| Edición masiva/resize para redes por personal no técnico | Canva (conector) | **Decisión 2026-09-04: no autorizado por ahora.** Se evaluará si aparece la necesidad de bulk-resize entre varios formatos por alguien sin conocimientos de código. |

## Reglas de video (definidas 2026-09-04)

- **Peso de archivos:** los clips crudos NO se versionan en git — `assets/video/` está en `.gitignore` salvo `.gitkeep`. Los clips viven en Descript/drive externo; el repo solo guarda el video final exportado en `output/`.
- **Música:** por ahora los videos van sin música de fondo (solo audio ambiente/voz). Si en el futuro se agrega una pista, hay que documentar acá la licencia de uso comercial antes de publicar, para evitar reclamos de derechos de autor en Instagram/Facebook.
- **Personas que aparecen en cámara:** confirmado por el cliente (2026-09-04) que las personas que aparecen jugando en los clips (no solo personal Oviedo) ya cuentan con autorización de imagen para uso publicitario del club. No requiere blur ni corte adicional por este motivo.

## Registro de sesiones

Al cerrar una sesión con cambios, dejar un resumen breve en el commit (qué pieza se generó/modificó, qué falta). Este proyecto es de bajo volumen de código — no requiere `estado-sesion-*.md` salvo que el flujo se vuelva más complejo.
