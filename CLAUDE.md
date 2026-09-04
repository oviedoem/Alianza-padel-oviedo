# CLAUDE.md — Alianza Padel Rocks Rapel × Ferretería Oviedo Express

Este archivo se carga automáticamente al inicio de cada sesión de Claude Code en este repo.

## LEER OBLIGATORIO ANTES DE CUALQUIER TAREA

1. Leer `README.md` — contexto estratégico, copys oficiales, datos de contacto, manual de estilo y reglas de control de identidad. Es la fuente de verdad única para todo texto y diseño generado en este repo.
2. No generar ninguna pieza (flyer, video, PPTX, HTML) sin haber releído `README.md` en esa sesión — los copys, colores y reglas anti-alucinación pueden actualizarse ahí.

## REGLAS NO NEGOCIABLES (resumen operativo)

- **Textos:** usar solo los copys/slogans listados en README.md § "Copys y Slogans Oficiales". No inventar variantes, no completar frases, no generar texto sintético en las piezas.
- **Marcas y RRSS:** únicos handles válidos: `@padel_rocks_rapel` y `@oviedo_elmanzano`. No mezclar extensiones de archivo ni inventar nombres.
- **Contacto:** WhatsApp Ferretería `+569 3862 3488`, Reservas Pádel `+569 5923 7808` — nunca intercambiar ni fusionar ambos números.
- **Identidad visual:** no mezclar paletas — Oviedo (rojo/blanco/negro industrial) y Padel Rocks (verde/blanco/rosa pastel) se mantienen segmentadas por marca, nunca combinadas en un mismo bloque cromático.
- **Logos:** no deformar, estirar, recortar ni pixelar. Proporciones originales siempre.
- **Personas/uniformes reales:** prohibido inpainting o sustitución de fondo sobre fotos de personal con uniforme oficial Oviedo (MTS, SOLMAQ, DIKMAN, BLACK+FRESEN visibles).
- **Entorno geográfico:** Sector El Estero, Las Cabras — nada de fondos artificiales (montañas nevadas, lagos tropicales, palmeras). Mantener canchas azules, terrazas de madera clara, pallets, toldos beige/arena.
- **QR dinámico:** siempre debe apuntar al link de reservas de pádel vigente en README.md — actualmente https://www.easycancha.com/es-CL/chile/club/padel-rocks-rapel (app/web EasyCancha, club "Padel Rocks Rapel").

## Antes de cualquier pieza nueva

```
PIEZA:       [flyer / video / story / pptx]
MARCA(S):    [Oviedo | Padel Rocks | ambas]
COPY USADO:  [cuál de los copys oficiales, textual]
NO TOCO:     [logos/fotos que se preservan íntegros]
```

## Estructura sugerida del repo

- `README.md` — fuente única de copys, contacto y reglas (no duplicar contenido en otros archivos)
- `assets/` — logos oficiales, fotos de campaña, fuentes
- `plantillas/` — layouts HTML/PPTX reutilizables para flyers
- `output/` — piezas generadas (no versionar assets pesados si el repo crece mucho; evaluar `.gitignore`)

## Registro de sesiones

Al cerrar una sesión con cambios, dejar un resumen breve en el commit (qué pieza se generó/modificó, qué falta). Este proyecto es de bajo volumen de código — no requiere `estado-sesion-*.md` salvo que el flujo se vuelva más complejo.
