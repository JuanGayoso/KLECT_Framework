# Ejemplo — Fases 3 y 4 (borrador y publicación)

> Continuación de `01_fase1_extraccion_y_preguntas.md`. Las respuestas del usuario son **hipotéticas**.

## Respuestas del usuario (origen [U])
```
1. Torre Demo, edificio de oficinas.
2. La especificación pedía 7 días de curado húmedo.
3. Es la apreciación del residente. El desencofrado estaba programado en el cronograma para el día 2.
4. Se inyectó sellador en las fisuras. No se hicieron ensayos adicionales.
5. Programar el curado como actividad con responsable en el cronograma.
6. No se registró costo ni atraso. No paralizó la obra. Lo ejecutaba el contratista general.
```

## FASE 3 — BORRADOR (estado: BORRADOR)

Ficha completa en [`ficha_ejemplo.yaml`](ficha_ejemplo.yaml). Puntos que el agente destaca:

- **Hechos**: todos con origen [T] o [U] (columna `trazabilidad`). Ninguna oración sale del conocimiento general del agente.
- **No se usó** "retracción", "evaporación" ni ninguna causa técnica que nadie haya afirmado.
- **Facetas inferidas [I]** (para confirmar): CAT-4 (la práctica de ejecución no siguió lo especificado), Sistema Estructural,
  Fase Construcción, Causa raíz Proceso (apoyada en [U]: cronograma día 2 vs. especificación 7 días), Impacto Calidad.
- **Severidad Baja — provisional**: no hay cifras de costo y el usuario dijo que no paralizó la obra. Se confirmará si aparecen datos.
- **Backward-flow**: no corresponde (CAT-4 con severidad no Alta/Crítica).
- **Campos faltantes**: ubicación, impacto_costo, impacto_plazo, aplica_cuando, no_aplica_cuando.

**Auditoría de fidelidad:** 6 afirmaciones de hecho; 6 con origen [T]/[U]; 0 sin origen.

## FASE 4 — DECLARACIÓN DE FIDELIDAD

Se publicará, campo por campo:
| Campo | Contenido | Origen |
|---|---|---|
| descripcion | "En la losa del piso 3 se retiró el curado a los 2 días porque había que desencofrar. A las dos semanas aparecieron fisuras finas." | [T] |
| causa_raiz_detalle | Desencofrado programado al día 2 vs. 7 días especificados; "faltó mojar" es apreciación del residente | [U] |
| solucion | Se inyectó sellador; sin ensayos adicionales | [U] |
| recomendacion | Programar el curado como actividad con responsable en el cronograma | [U] |
| Facetas | CAT-4 · Estructural · Construcción · Contratista · Proceso · Calidad · Baja (provisional) | [I]/[U] |

Para publicar, responda exactamente **`PUBLICAR`**, o indique qué corregir.

## Si en lugar de eso el usuario hubiera escrito "complétalo tú"
> No completo campos de hecho (costo, plazo, causa, solución) porque la lección debe reflejar lo que ocurrió, no lo que es plausible.
> Puedo (a) hacerle las preguntas que faltan o (b) dejar sugerencias mías, marcadas [A] y fuera de la ficha, para que un responsable las valide.
