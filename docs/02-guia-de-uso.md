# 2. Guía de uso del agente

## Formas de usar KLECT Agent

| Forma | Cuándo | Cómo |
|---|---|---|
| **Prompt de sistema (versión completa)** | Entornos sin límite de instrucciones o integraciones propias | `agent/system_prompt.md` (≈14.000 caracteres) |
| **Claude / ChatGPT / Gemini** | Uso diario, sin instalar nada | Ver [`06-despliegue-sin-instalar.md`](06-despliegue-sin-instalar.md) |
| **Skill de Claude** | Comandos `/analizar`… automáticos | Subir `deploy/claude/klect-agent.zip` |
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
1. Pegar el relato bruto de quien vivió la lección (sin resumirlo).
2. `/analizar`: el agente extrae, muestra lo que falta y **pregunta** (no redacta por su cuenta).
3. Responder, revisar el borrador y la Declaración de fidelidad; escribir `PUBLICAR` solo si está conforme.
3b. (Opcional) Validar: `python tools/validate_f01.py ficha.yaml --fuente relato.txt`.
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
