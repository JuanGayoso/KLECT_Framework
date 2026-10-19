# Modo `/buscar [pregunta en lenguaje natural]`

**Propósito:** traducir una pregunta de usuario a términos controlados KLECT y a consultas formales.
**Salida:** términos de búsqueda controlados → facetas aplicables → query SPARQL (+ SQL L2).

## Procedimiento
1. Identificar la intención (¿evitar un error en diseño?, ¿diagnosticar un problema en obra?, ¿preparar checklist?).
2. Normalizar a términos controlados y expandir con sinónimos de obra.
3. Mapear a facetas (CAT, F1, F3, F4…) con los valores que la pregunta sustenta; no restringir de más.
4. Describir **qué tipo de lecciones** debería devolver el sistema (el agente no inventa lecciones existentes).
5. Emitir SPARQL (`queries/sparql/`) y su equivalente SQL (`queries/sql/`).

## Ejemplo
Pregunta: *"¿Qué problemas hemos tenido con filtraciones en sótanos?"*
- Controlados: filtración, impermeabilización, muro de sótano, junta de construcción.
- Facetas: F1 Envolvente/Estructural; CAT-2, CAT-3, CAT-4; F3 Diseño Detallado y Construcción.
- SPARQL: ver `queries/sparql/consultas_tipo.rq` adaptando categoría y sistema.
