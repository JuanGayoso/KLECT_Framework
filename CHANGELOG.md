# Changelog

## [1.1.0] — 2026-10-19
### Añadido
- **Protocolo de fidelidad anti-invención** (prioridad máxima): orígenes [T]/[U]/[I]/[A], campos de hecho nunca inferidos,
  flujo obligatorio Extracción → Preguntas → Borrador → Publicación (palabra `PUBLICAR`), estados BORRADOR/VERIFICADA/PUBLICABLE.
- Esquema F01: `estado_publicacion`, `trazabilidad`, `citas_fuente`, `fuente`, `sugerencias_agente`.
- Validador: exige origen por campo de hecho y verifica citas literales contra el relato (`--fuente`).
- `deploy/`: instrucciones compactas (≈7.400 caracteres), archivo único de conocimiento y skill ZIP para usar en Claude, ChatGPT y Gemini sin instalar nada.
- `docs/06-despliegue-sin-instalar.md` y `tests/casos_anti_alucinacion.md` (11 casos).
### Cambiado
- Ejemplos reescritos: la ficha de ejemplo contiene solo datos del relato y de respuestas del usuario.
- `tools/build_skill.py` reemplazado por `tools/build_knowledge.py`.

## [1.0.0] — 2026-10-19
### Añadido
- Prompt maestro de KLECT Agent (taxonomía 5 categorías + facetas F1–F8, 6 modos, protocolo de 6 pasos, criterios de calidad) con especificaciones complementarias v1.1.
- Guías por modo, skill de Claude y empaquetador.
- Taxonomía legible por máquina y referencia/mapeo Uniclass (pendiente de verificación oficial).
- Esquema JSON de la ficha KLECT-F01 y validador con reglas de coherencia.
- Plantillas KLECT-F01, KLECT-PROC, KLECT-REF y checklist backward-flow.
- Esquema SQL (L2), ontología Turtle y consultas SPARQL (L3).
- Documentación: visión y cultura, guía de uso, arquitectura de wiki, hoja de ruta, gobierno y métricas.
