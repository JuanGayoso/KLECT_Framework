# Ejemplo de salida del agente — `/analizar`

> Caso **hipotético** con fines didácticos. El texto de entrada es breve a propósito para mostrar
> cómo el agente declara campos faltantes en lugar de suponerlos.

**Entrada**
```
/analizar En la losa del piso 3 se retiró el curado a los 2 días porque había que desencofrar.
A las dos semanas aparecieron fisuras finas. Residente dice que "faltó mojar".
```

**Salida esperada**

---
**PASO 1 · Diagnóstico:** contenido tipo LL, sin clasificación; contexto de aplicación débil (sin proyecto, tipo ni especificación de curado). Criterios fallidos: TRAZABILIDAD, COMPLETITUD (2 de 6 → se puede clasificar, con advertencias).

🏷 **CLASIFICACIÓN KLECT**
Categoría: [CAT-4] Defectos de construcción — práctica de ejecución incumple el curado
Sistema (F1): Estructural — Uniclass: Ss_20 (verificar contra catálogo oficial NBS)
Tipo proyecto (F2): no determinable (opciones: Comercial/Residencial)
Fase (F3): Construcción
Severidad (F4): no determinable — provisional **Baja/Media** (sin monto de contrato ni costo de reparación)
Disciplina (F5): Contratista
Causa raíz (F6): Proceso (opción 2, 30 %: Comunicación)
Impacto (F7): Calidad, Cronograma (este último solo por presión de desencofrado; sin datos de plazo)

📋 **FICHA KLECT-F01** → ver `examples/ficha_ejemplo.yaml` (mismo formato; `campos_faltantes`: tipo_proyecto, proyecto_origen, impacto_costo, impacto_plazo, solucion, especificación de curado).

🔍 **INDEXACIÓN SEMÁNTICA**
Términos controlados: curado de concreto, fisuración por retracción, losa de entrepiso, desencofrado
Sinónimos sectoriales: "mojar la losa", rajaduras, plancha de concreto
Términos relacionados: resistencia a edad temprana, durabilidad, programación de obra
Preguntas de búsqueda: 1) ¿Cuántos días mínimos de curado exige una losa? 2) ¿Por qué aparecen fisuras finas tras el vaciado? 3) ¿Quién es responsable del curado en obra?

🗂 **ESTRUCTURA EN WIKI**
Ruta: 01-Lecciones > CAT-4-Construccion > Estructural > CAT4-EST-CON-001
Plantilla: KLECT-F01
Vinculaciones sugeridas: Procedimiento de curado (KLECT-PROC), Ficha técnica del concreto (KLECT-REF)
Nombre normalizado: CAT4-EST-CON-001 / Curado inadecuado de concreto en losa de entrepiso

⚠️ **BACKWARD-FLOW:** no aplica obligatoriamente (CAT-4, severidad no Alta/Crítica). Opcional: "Confirmar que el curado figura en el cronograma con responsable y registro." — Fase: Construcción — 🟡 Medio.

💻 **CONSULTA DE RECUPERACIÓN**
SQL (L2): `SELECT * FROM lecciones WHERE categoria='CAT-4' AND sistema='Estructural' AND fase='Construcción';`
SPARQL (L3): ver `queries/sparql/consultas_tipo.rq`

**Recomendaciones:** (1) completar los 6 campos faltantes con el residente; (2) crear el procedimiento KLECT-PROC de curado y enlazarlo; (3) reemplazar la cita "faltó mojar" por la causa raíz documentada.
---
