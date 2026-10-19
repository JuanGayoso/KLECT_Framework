# Modo `/analizar [artículo]`

**Propósito:** clasificar un artículo de wiki, extraer metadatos y proponer mejoras estructurales.
**Salida:** Diagnóstico → Clasificación KLECT → Ficha F01 → Recomendaciones.

## Procedimiento
Ejecutar los 6 pasos del protocolo (ver `agent/system_prompt.md`):
1. Diagnóstico inicial (tipo de contenido, clasificación actual, recuperabilidad, contexto).
2. Clasificación taxonómica (CAT + F1–F8; si es ambiguo, 2 opciones con probabilidad).
3. Extracción de metadatos → ficha KLECT-F01 (YAML conforme a `schema/klect_f01.schema.json`).
4. Indexación semántica (controlados, sinónimos, relacionados, 3–5 preguntas, vinculaciones).
5. Estructura en wiki (ruta, plantilla, padre/hermanos/hijos, nombre normalizado).
6. Backward-flow (solo CAT-1/2/3 o severidad Alta/Crítica).

## Puertas de calidad
- Evaluar los 6 criterios (recuperabilidad, contexto, accionabilidad, trazabilidad, completitud, unicidad).
- Si **falla más de 2**, no clasificar: pedir la información faltante, listando los campos concretos.
- Si el contenido es un procedimiento, redirigir a `KLECT-PROC`.

## Sección "Recomendaciones" (propia de este modo)
Lista priorizada de mejoras: contenido faltante, reestructuración, enlaces, términos, adjuntos.
