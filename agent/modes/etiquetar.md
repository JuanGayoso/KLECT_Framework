# Modo `/etiquetar [texto libre]`

**Propósito:** convertir texto libre en metadatos listos para la wiki.
**Rige el PROTOCOLO DE FIDELIDAD.** Etiquetar es clasificar [I] y extraer [T]; no es redactar la lección.

## Procedimiento
1. Fase 1: extraer lo que el texto dice, con cita literal.
2. Asignar CAT y facetas F1–F8 como **inferencias [I]**, cada una con la cita que la sustenta.
   Si una faceta no se puede sustentar (p. ej. severidad sin cifras), dejarla `null`/provisional y preguntar.
3. Términos de indización (controlados, sinónimos de obra, relacionados, 3–5 preguntas): son [I] y no alteran los hechos.
4. Preguntar solo lo bloqueante para clasificar (máx. 5).
5. Entregar el YAML con `estado_publicacion: BORRADOR`, `trazabilidad` y `citas_fuente`.

## Salida mínima
```yaml
estado_publicacion: BORRADOR
categoria:
sistema:
tipo_proyecto:
fase:
severidad:
disciplina:
causa_raiz:
impacto: []
uniclass_ss:
citas_fuente: []
trazabilidad: {}
terminos_controlados: []
sinonimos_sectoriales: []
preguntas_busqueda: []
campos_faltantes: []
```
