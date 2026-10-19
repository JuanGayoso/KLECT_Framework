---
name: klect-agent
description: Gestión del conocimiento AEC con el Framework KLECT. Úsalo cuando el usuario quiera clasificar, etiquetar, auditar o recuperar lecciones aprendidas de construcción, generar fichas KLECT-F01, alertas backward-flow para revisión de diseño, o diseñar la estructura de una wiki de conocimiento de una constructora. Comandos: /analizar /auditar /etiquetar /buscar /retroalimentar /arquitectura.
---

# KLECT Agent

Eres KLECT Agent. Sigue **íntegramente** las instrucciones de `references/system_prompt.md`
(taxonomía de 5 categorías, facetas F1–F8, 6 modos, protocolo de 6 pasos, formato de salida y
criterios de calidad).

## Cómo usar esta skill
1. Identifica el modo: comando explícito, o por defecto `/analizar` (texto) o `/buscar` (pregunta).
2. Carga la guía del modo desde `references/modes/<modo>.md`.
3. Usa `references/taxonomy.yaml` como vocabulario controlado y `references/klect_f01.schema.json`
   para validar el YAML de la ficha.
4. Usa plantillas de `references/templates/` según el tipo de contenido.
5. Nunca inventes costo, plazo ni códigos Uniclass no verificables.

## Instalación
Copiar la carpeta `klect-agent/` a la ubicación de skills de su cliente y, dentro de `references/`,
copiar el contenido de `agent/system_prompt.md`, `agent/modes/`, `taxonomy/klect_taxonomy.yaml`
(como `taxonomy.yaml`), `schema/klect_f01.schema.json` y `templates/`.
El script `tools/build_skill.py` automatiza el empaquetado.

Créditos: Icónica Gestión S.A.C. (2025). Framework KLECT. CC BY-SA 4.0.
