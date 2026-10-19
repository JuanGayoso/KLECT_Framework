# KLECT Framework · KLECT Agent

**Gestión del conocimiento y lecciones aprendidas para la industria AEC** (Architecture, Engineering and Construction).
Taxonomía de 5 categorías + 8 facetas (con Uniclass 2015), plantillas de wiki, ontología OWL/RDF,
consultas SQL/SPARQL y un **agente de IA** que clasifica, indexa, audita y cierra el ciclo con la
revisión de diseño (*backward-flow*).

> Framework KLECT · Icónica Gestión S.A.C. (Lima, Perú, 2025) · AEC Knowledge Series N°01 · [CC BY-SA 4.0](LICENSE.md)

## Qué incluye

| Carpeta | Contenido |
|---|---|
| [`agent/`](agent) | Prompt de sistema del agente, guías por modo y skill de Claude |
| [`taxonomy/`](taxonomy) | Taxonomía legible por máquina, referencia y mapeo Uniclass |
| [`schema/`](schema) | Esquema JSON de la ficha KLECT-F01 |
| [`templates/`](templates) | Plantillas F01 (lección), PROC (procedimiento), REF (referencia) y checklist backward-flow |
| [`queries/`](queries) | Esquema SQL (L2), ontología Turtle y consultas SPARQL (L3) |
| [`deploy/`](deploy) | Archivos listos para pegar/subir en Claude, ChatGPT y Gemini (sin instalar nada) |
| [`tools/`](tools) | Validador de fichas (con verificación de citas), ejecutor por API y generador de `deploy/` |
| [`tests/`](tests) | Casos de prueba anti-alucinación |
| [`examples/`](examples) | Flujo completo de ejemplo (extracción → preguntas → borrador → publicación) y ficha YAML |
| [`docs/`](docs) | Visión y cultura, guía de uso, arquitectura de wiki, hoja de ruta, gobierno |

## Taxonomía de un vistazo

**Categorías:** CAT-1 Supuestos de diseño erróneos · CAT-2 Defectos de diseño · CAT-3 Especificaciones deficientes ·
CAT-4 Defectos de construcción · CAT-5 Problemas de mantenibilidad.

**Facetas obligatorias:** F1 Sistema · F2 Tipo de proyecto · F3 Fase · F4 Severidad · F5 Disciplina ·
F6 Causa raíz · F7 Impacto · F8 Uniclass 2015 (Ss).

## Comandos del agente

`/analizar` · `/auditar` · `/etiquetar` · `/buscar` · `/retroalimentar` · `/arquitectura`

Detalle en [`docs/02-guia-de-uso.md`](docs/02-guia-de-uso.md).

## Inicio rápido — sin instalar nada

Funciona en **Claude, ChatGPT (GPT personalizado) y Gemini (Gem)**. Solo necesita 2 archivos de [`deploy/`](deploy):

1. [`instrucciones_compactas.txt`](deploy/instrucciones_compactas.txt) → pegar en las *instrucciones*.
2. [`KLECT_conocimiento.md`](deploy/KLECT_conocimiento.md) → subir como *conocimiento / archivo del proyecto*.

Pasos detallados para cada plataforma, cómo bajar los archivos desde GitHub y la prueba de aceptación:
**[`docs/06-despliegue-sin-instalar.md`](docs/06-despliegue-sin-instalar.md)**.

Opcionales (requieren Python): `python tools/run_agent.py "/etiquetar …"` para usar la API de Anthropic y
`python tools/validate_f01.py ficha.yaml --fuente relato.txt` para validar fichas.

## Protocolo de fidelidad (anti-invención)
El agente **no es el autor de la lección**. Cada dato de hecho debe venir del texto aportado [T] o de una respuesta del usuario [U];
las facetas de clasificación son inferencias [I] marcadas; las sugerencias propias del agente [A] van aparte y no se publican sin validación.
Flujo obligatorio: **1 Extracción → 2 Preguntas → 3 Borrador → 4 Publicación (solo con la palabra `PUBLICAR`)**.
Detalle en [`agent/protocolo_fidelidad.md`](agent/protocolo_fidelidad.md); pruebas en [`tests/casos_anti_alucinacion.md`](tests/casos_anti_alucinacion.md);
ejemplo en [`examples/`](examples).

## Principios de comportamiento del agente
- No inventa datos de impacto (costo, plazo) ni códigos Uniclass no verificables.
- Declara los campos faltantes en lugar de suponerlos y pregunta lo necesario.
- Si una ficha falla más de 2 de los 6 criterios de calidad, pide más información antes de clasificar.
- Redirige procedimientos a la plantilla KLECT-PROC.
- Terminología AEC; tono de Knowledge Manager especialista.

## Estado y verificación pendiente
- `taxonomy/uniclass_mapping.csv` contiene solo códigos de **grupo** marcados como no verificados; complételo con el catálogo oficial de NBS (Fase 1 de la hoja de ruta).
- El namespace de la ontología (`https://iconicagestion.example/klect#`) es un marcador de posición.
- Los ejemplos son hipotéticos, no casos reales.

## Cómo citar
Icónica Gestión S.A.C. (2025). *Framework KLECT*. AEC Knowledge Series N°01. Ver [`CITATION.cff`](CITATION.cff).

## Licencia
CC BY-SA 4.0 — uso libre con atribución obligatoria y compartir igual. Ver [`LICENSE.md`](LICENSE.md).
