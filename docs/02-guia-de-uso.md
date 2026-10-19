# 2. Guía de uso del agente

## Formas de usar KLECT Agent

| Forma | Cuándo | Cómo |
|---|---|---|
| **Prompt de sistema** | Proyecto/GPT/asistente de su organización | Pegar `agent/system_prompt.md` como instrucciones |
| **Skill de Claude** | Uso recurrente con comandos `/analizar`… | `python tools/build_skill.py` → `dist/klect-agent.zip` |
| **API** | Integrar con su wiki o flujo automatizado | `python tools/run_agent.py "/analizar …"` |

## Comandos

| Comando | Entrada | Salida |
|---|---|---|
| `/analizar` | Artículo de wiki | Diagnóstico, clasificación, ficha F01, recomendaciones |
| `/auditar` | Lista de títulos o sección | Mapa de cobertura, huecos, duplicados, prioridades |
| `/etiquetar` | Texto libre | YAML de metadatos + términos de indización |
| `/buscar` | Pregunta en lenguaje natural | Términos controlados, facetas, SPARQL/SQL |
| `/retroalimentar` | Lección o ID | Alerta KLECT-BACKWARD, ítem de checklist, justificación |
| `/arquitectura` | Descripción de la organización | Árbol de wiki, plantillas, nomenclatura, hoja de ruta |

Sin comando: texto pegado → `/analizar`; pregunta → `/buscar`.

## Flujo recomendado de adopción de una lección
1. `/etiquetar` sobre el relato bruto del residente (captura rápida).
2. `/analizar` para completar la ficha y detectar faltantes.
3. Validar: `python tools/validate_f01.py ficha.yaml`.
4. Publicar en la wiki con la plantilla `KLECT-F01`.
5. `/retroalimentar` si aplica; agregar el ítem a `templates/backward_flow_checklist.md`.
6. Registrar en la base L2 (`queries/sql/schema.sql`) y/o grafo L3.

## Validación
```bash
pip install -r requirements.txt
python tools/validate_f01.py examples/ficha_ejemplo.yaml
```
El validador revisa el esquema JSON y reglas de coherencia (CAT↔fase, nomenclatura, severidad
provisional, Uniclass sin verificar, exceso de campos faltantes).

## Buenas prácticas de entrada
- Incluya proyecto, tipo, fase, sistema/componente, qué pasó, por qué y qué se hizo.
- Aporte montos reales (o diga que no los tiene); el agente no los estimará.
- Pegue una lista de lecciones existentes para que se evalúe la unicidad.
