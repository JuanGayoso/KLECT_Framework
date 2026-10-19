# Ejemplo — Fases 1 y 2 (extracción y preguntas)

> Caso **hipotético**. Muestra qué hace el agente con un texto corto: **no redacta la lección**; extrae lo que hay,
> señala lo que falta y pregunta.

## Entrada del usuario
```
/analizar En la losa del piso 3 se retiró el curado a los 2 días porque había que desencofrar.
A las dos semanas aparecieron fisuras finas. Residente dice que "faltó mojar".
```

## Respuesta esperada del agente

**FASE 1 — EXTRACCIÓN** (nada redactado por mí; solo lo que está en el texto)

| Campo | Valor | Origen | Cita literal |
|---|---|---|---|
| componente | Losa del piso 3 | [T] | "En la losa del piso 3" |
| qué pasó | Se retiró el curado a los 2 días, por el desencofrado | [T] | "se retiró el curado a los 2 días porque había que desencofrar" |
| consecuencia observada | Fisuras finas a las dos semanas | [T] | "A las dos semanas aparecieron fisuras finas" |
| causa (según el residente) | "faltó mojar" | [T] | "Residente dice que «faltó mojar»" |

⚠️ **Ambigüedad:** "faltó mojar" parece una apreciación del residente, no una causa confirmada.

**NO ESTÁ EN EL TEXTO:** proyecto · tipo de proyecto · qué especificaba el proyecto para el curado · quién ejecutaba el curado ·
qué se hizo ante las fisuras · consecuencias en costo/plazo/paralización · recomendación del equipo · condiciones de aplicabilidad.

**Diagnóstico de calidad:** fallan TRAZABILIDAD y COMPLETITUD (2 de 6). No genero ficha todavía.

**FASE 2 — PREGUNTAS** (responda lo que sepa; "no se sabe" es una respuesta válida)

**P1 (bloqueantes)**
1. ¿De qué proyecto es y de qué tipo? (Residencial / Comercial / Industrial / Salud / Educación / Infraestructura / otro)
2. ¿Qué pedía la especificación o el procedimiento para el curado de esa losa (método y duración)? ¿Dónde está documentado?
3. El texto dice "faltó mojar". ¿Es la causa confirmada o la apreciación del residente? ¿Se identificó otra causa?
4. ¿Qué se hizo con las fisuras (reparación, ensayos, nada)?
5. ¿Qué haría distinto el equipo? (con sus propias palabras)

**P2 (complementarias)**
6. ¿Hubo costo, atraso o paralización asociados? Si tiene cifras reales, indíquelas; si no, responda "sin dato".
   ¿Y quién ejecutaba el curado: contratista general, subcontratista u otro?
