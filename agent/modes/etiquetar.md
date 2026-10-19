# Modo `/etiquetar [texto libre]`

**Propósito:** convertir texto libre en metadatos listos para la wiki.
**Salida:** bloque YAML de metadatos + términos de indización.

## Procedimiento
1. Extraer las 8 facetas (F1–F8) y la categoría CAT.
2. Rellenar solo lo que el texto sustenta; el resto `null` y listado en `campos_faltantes`.
3. Generar términos controlados, sinónimos de obra/residencia/gerencia, términos relacionados y 3–5 preguntas de búsqueda.
4. Validar mentalmente contra `schema/klect_f01.schema.json` (o ejecutar `tools/validate_f01.py`).

## Salida mínima
```yaml
categoria: CAT-
sistema:
tipo_proyecto:
fase:
severidad:
disciplina:
causa_raiz:
impacto: []
uniclass_ss:
terminos_controlados: []
sinonimos_sectoriales: []
preguntas_busqueda: []
campos_faltantes: []
```
