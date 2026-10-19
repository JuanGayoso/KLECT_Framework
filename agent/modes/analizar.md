# Modo `/analizar [artículo]`

**Propósito:** clasificar un artículo de wiki, extraer metadatos y proponer mejoras estructurales — **sin inventar contenido**.
**Rige el PROTOCOLO DE FIDELIDAD** (`agent/protocolo_fidelidad.md`): 4 fases obligatorias.

## Flujo
1. **Fase 1 — Extracción:** tabla campo/valor/origen/cita literal + lista `NO ESTÁ EN EL TEXTO` + diagnóstico (paso 1 del protocolo de análisis).
2. **Fase 2 — Preguntas:** P1 bloqueantes y P2 complementarias; máx. 7; neutras. Esperar respuesta.
3. **Fase 3 — Borrador:** clasificación KLECT, ficha F01 (YAML conforme a `schema/klect_f01.schema.json` con `trazabilidad` y `citas_fuente`),
   indexación, estructura de wiki, backward-flow si aplica. Estado `BORRADOR`. Auditoría de fidelidad.
4. **Fase 4 — Publicación:** declaración de fidelidad; solo con `PUBLICAR` el estado pasa a `PUBLICABLE`.

## Puertas de calidad
- Evaluar los 6 criterios. Si **falla más de 2**, quedarse en Fases 1–2.
- Si el contenido es un procedimiento, redirigir a `KLECT-PROC`.
- Si ya existe una lista de lecciones, verificar unicidad antes de crear ficha.

## Recomendaciones (propias de este modo)
Mejoras de estructura (contenido faltante, enlaces, términos, adjuntos). Las recomendaciones **del agente** son [A]
y se mantienen separadas del contenido de la lección.
