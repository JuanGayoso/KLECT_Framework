# Contribuir a KLECT

Gracias por mejorar el framework. Las contribuciones se publican bajo CC BY-SA 4.0.

## Qué se puede proponer
- Correcciones y mejoras al prompt (`agent/system_prompt.md`) y a las guías de modo.
- Códigos Uniclass **verificados** para `taxonomy/uniclass_mapping.csv` (cite la fuente oficial y la fecha).
- Nuevos sinónimos sectoriales o casos de ejemplo (hipotéticos o anonimizados).
- Plantillas, consultas y mejoras de herramientas.

## Reglas
1. **Cambios a la taxonomía** (categorías o facetas) requieren un issue con justificación y un
   aumento de versión en `taxonomy/klect_taxonomy.yaml` y `CHANGELOG.md`.
2. Mantenga sincronizados: `agent/system_prompt.md` ↔ `taxonomy/klect_taxonomy.yaml` ↔
   `schema/klect_f01.schema.json` ↔ `queries/sql/schema.sql` ↔ `queries/sparql/klect_ontology.ttl`.
3. Ejemplos: nunca incluya datos confidenciales de proyectos reales ni nombres de personas.
4. Valide antes de proponer: `python tools/validate_f01.py examples/*.yaml`.
5. Mensajes de commit claros, en español o inglés.

## Flujo
Fork → rama descriptiva → cambios → pull request describiendo el problema y la verificación realizada.
