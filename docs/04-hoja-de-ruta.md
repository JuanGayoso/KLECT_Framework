# 4. Hoja de ruta de implementación

Plan por fases, escalable según el tamaño de la organización. Los plazos son **referenciales**;
ajústelos a su capacidad.

## Fase 0 — Alineación (1–2 semanas)
- Patrocinador y responsable de gestión del conocimiento designados.
- Acuerdo de cultura sin culpables (ver `docs/01-vision-y-cultura.md`).
- Elegir plataforma de wiki.

## Fase 1 — Fundamentos (2–4 semanas)
- Crear estructura de `docs/03-arquitectura-wiki.md`.
- Adoptar taxonomía y plantillas; verificar y completar `taxonomy/uniclass_mapping.csv` con códigos oficiales NBS.
- Configurar el agente (prompt de sistema o skill).

## Fase 2 — Migración y piloto (4–8 semanas)
- `/auditar` sobre lo existente: cobertura, huecos, duplicados.
- Migrar primero lecciones de severidad Alta/Crítica y CAT-1/2/3.
- Piloto en 1–2 proyectos; validar fichas con `tools/validate_f01.py`.

## Fase 3 — Cierre del ciclo (continuo)
- Integrar `/retroalimentar` en las revisiones de diseño de proyectos nuevos.
- Mantener `templates/backward_flow_checklist.md` como documento vivo.
- Captura al cierre de cada hito de obra.

## Fase 4 — Recuperación avanzada (opcional)
- Base relacional L2 (`queries/sql/schema.sql`).
- Grafo L3 con la ontología (`queries/sparql/klect_ontology.ttl`) y un triple store.
- Búsqueda en lenguaje natural con `/buscar` conectado a su repositorio.

## Hitos de éxito
| Hito | Evidencia |
|---|---|
| Taxonomía adoptada | 100 % de fichas nuevas con F1–F8 |
| Cobertura | Huecos críticos de `/auditar` cerrados |
| Ciclo cerrado | Ítems de checklist usados en ≥1 revisión de diseño por proyecto |
