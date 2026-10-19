# Guía de implementación KLECT

Complemento del agente: cómo llevar el framework a una organización constructora (cultura, wiki, plan por fases y gobierno).
KLECT = *Knowledge Lifecycle for Engineering and Construction Toolbox*.

## 1. Visión, principios y cultura de aprendizaje

### Problema que resuelve
Las constructoras repiten errores porque las lecciones aprendidas se escriben pero no se **encuentran**,
no tienen **contexto** y no regresan al **diseño** de los proyectos nuevos. KLECT convierte el archivo
de lecciones en un sistema de conocimiento: clasificado, indexado, recuperable y conectado con la
revisión de diseño (backward-flow).

### Cuatro bases metodológicas
| Base | Aporte a KLECT |
|---|---|
| Bibliotecología y clasificación facetada (Ranganathan; Taylor & Joudrey) | Facetas independientes y combinables (F1–F8) en lugar de una única jerarquía rígida |
| Taxonomía de 5 categorías (Love et al., 2016) | Origen del error: supuestos, diseño, especificación, construcción, mantenibilidad |
| Ontología formal OWL/RDF | Relaciones explícitas y consultas de grafo (SPARQL, nivel L3) |
| Gestión del conocimiento en construcción | Ciclo capturar → clasificar → indexar → recuperar → reutilizar |

### Niveles de recuperación
- **L1** — búsqueda por texto y navegación de la wiki.
- **L2** — consultas relacionales por facetas (SQL).
- **L3** — consultas semánticas sobre grafo (SPARQL).

### Cultura de la organización (condiciones para que funcione)
Una taxonomía no cambia conductas por sí sola. Estas condiciones son parte del framework:

1. **Sin culpables.** Las fichas describen hechos y causas de proceso, no personas. La causa raíz
   se clasifica en F6 (Comunicación, Proceso, Competencia, Herramienta, Condición externa).
2. **Capturar en el momento.** Cierre de hito, no de proyecto: el olvido es el mayor enemigo.
3. **Dueño de cada lección.** Un responsable (disciplina) mantiene vigencia y vínculos.
4. **Cierre del ciclo.** Toda lección CAT-1/2/3 o de severidad Alta/Crítica genera un ítem de
   checklist; si no regresa al diseño, no hay aprendizaje organizacional.
5. **Reconocer a quien reporta.** Medir y valorar contribuciones, no solo resultados.
6. **Calidad antes que cantidad.** Los 6 criterios de calidad filtran fichas incompletas.

### Los 6 criterios de calidad del conocimiento
Recuperabilidad · Contexto · Accionabilidad · Trazabilidad · Completitud · Unicidad.
Si una ficha falla **más de 2**, el agente pide más información antes de clasificar.

### Alcance y límites
- El agente **no inventa** costos, plazos ni códigos Uniclass.
- La clasificación es una propuesta: la valida el responsable de gestión del conocimiento.
- La auditoría por títulos es preliminar; exige leer el contenido para confirmar.

## 2. Arquitectura de la wiki de conocimiento

### Árbol de categorías (propuesta base)
```
KLECT/
├── 01-Lecciones/
│   ├── CAT-1-Supuestos/
│   ├── CAT-2-Diseno/
│   ├── CAT-3-Especificaciones/
│   ├── CAT-4-Construccion/
│   │   └── Estructural/ Envolvente/ Acabados/ MEP-Mec/ MEP-Elec/ MEP-San/ Sitio/
│   └── CAT-5-Mantenibilidad/
├── 02-Procedimientos/        (plantilla KLECT-PROC)
├── 03-Referencias/           (plantilla KLECT-REF)
├── 04-Backward-Flow/         (checklists por fase, alertas)
├── 05-Taxonomia/             (vocabulario controlado, Uniclass, glosario)
└── 99-Gobierno/              (roles, métricas, cola de revisión)
```
Regla: la carpeta refleja **CAT → Sistema**; las demás facetas (fase, severidad, tipo…) se
expresan como metadatos y se filtran, no como carpetas (evita jerarquías rígidas).

### Plantillas
| Contenido | Plantilla |
|---|---|
| Lección aprendida | `KLECT-F01` |
| Procedimiento repetible | `KLECT-PROC` |
| Estándar / referencia técnica | `KLECT-REF` |

### Convención de nomenclatura
`CATn-SIS-FAS-NNN / Título descriptivo`

| Parte | Significado | Valores |
|---|---|---|
| `CATn` | Categoría | CAT1…CAT5 |
| `SIS` | Sistema F1 | EST, ENV, ACA, MEC, ELE, SAN, SIT |
| `FAS` | Fase F3 | PRE, DBA, DDE, PRO, CON, OPE |
| `NNN` | Correlativo por combinación | 001… |

Ejemplo: `CAT4-EST-CON-001 / Curado inadecuado de concreto`.
Procedimientos: `PROC-SIS-FAS-NNN`; referencias: `REF-SIS-NNN`.

### Relaciones entre artículos
`padre` · `hermano` · `relacionado` · `duplica` · `origina_procedimiento`
(modeladas en `leccion_vinculo` de L2 y en `klect:relacionadaCon`/`klect:duplicaA` de L3).

### Política de metadatos
- Todas las facetas F1–F8 son **obligatorias** al clasificar; si no se pueden determinar, se
  declara el faltante, no se supone.
- `uniclass_ss` solo con código verificable (`uniclass_verificado`).
- Una lección = un problema. Si mezcla varios, se divide.

### Plataformas
La estructura es agnóstica: SharePoint, Notion, Confluence, MediaWiki u otra. Lo esencial es
que los metadatos sean campos filtrables (propiedades/columnas), no texto libre.

## 3. Hoja de ruta de implementación

Plan por fases, escalable según el tamaño de la organización. Los plazos son **referenciales**;
ajústelos a su capacidad.

### Fase 0 — Alineación (1–2 semanas)
- Patrocinador y responsable de gestión del conocimiento designados.
- Acuerdo de cultura sin culpables (ver sección 1).
- Elegir plataforma de wiki.

### Fase 1 — Fundamentos (2–4 semanas)
- Crear la estructura de la sección 2.
- Adoptar taxonomía y plantillas; verificar y completar los códigos Uniclass con el catálogo oficial de NBS (el agente solo cita los que puede respaldar).
- Configurar el agente (prompt de sistema o skill).

### Fase 2 — Migración y piloto (4–8 semanas)
- `/auditar` sobre lo existente: cobertura, huecos, duplicados.
- Migrar primero lecciones de severidad Alta/Crítica y CAT-1/2/3.
- Piloto en 1–2 proyectos; revisar cada ficha con la Declaración de fidelidad del agente y los casos de `PRUEBAS.md`.

### Fase 3 — Cierre del ciclo (continuo)
- Integrar `/retroalimentar` en las revisiones de diseño de proyectos nuevos.
- Mantener la checklist de revisión de diseño (sección [08] de `KLECT_conocimiento.md`) como documento vivo.
- Captura al cierre de cada hito de obra.

### Fase 4 — Recuperación avanzada (opcional)
- Base relacional L2 (esquema SQL en la sección [13] de `KLECT_conocimiento.md`).
- Grafo L3 con la ontología (sección [11] de `KLECT_conocimiento.md`) y un triple store.
- Búsqueda en lenguaje natural con `/buscar` conectado a su repositorio.

### Hitos de éxito
| Hito | Evidencia |
|---|---|
| Taxonomía adoptada | 100 % de fichas nuevas con F1–F8 |
| Cobertura | Huecos críticos de `/auditar` cerrados |
| Ciclo cerrado | Ítems de checklist usados en ≥1 revisión de diseño por proyecto |

## 4. Gobierno y métricas

### Roles
| Rol | Responsabilidad |
|---|---|
| Patrocinador | Prioriza y protege tiempo para el aprendizaje |
| Knowledge Manager | Custodia taxonomía, calidad y agente; valida clasificaciones |
| Dueño de lección | Disciplina responsable de vigencia y vínculos de cada ficha |
| Revisor de diseño | Aplica el checklist backward-flow en cada fase |
| Contribuidores | Residentes, ingenieros, gestores: capturan lecciones |

### Flujo de una ficha
`Borrador` → `Clasificada (agente)` → `Validada (Knowledge Manager)` → `Publicada` → `Revisión periódica` / `Obsoleta`

### Métricas sugeridas
| Métrica | Pregunta que responde | Fuente |
|---|---|---|
| Cobertura CAT × Sistema | ¿Dónde no estamos aprendiendo? | `/auditar`, consulta 4 de `consultas_tipo.sql` |
| % fichas con F1–F8 completas | ¿Se puede recuperar? | Revisión de fichas / `PRUEBAS.md` |
| % fichas con >2 criterios fallidos | ¿Calidad de captura? | Revisión de calidad |
| Duplicados detectados / fusionados | ¿Unicidad? | `/auditar`, consulta 5 |
| Ítems de checklist aplicados por proyecto | ¿Se cierra el ciclo? | `leccion_backward` |
| Tiempo desde evento hasta ficha publicada | ¿Capturamos a tiempo? | Registro de la wiki |

### Revisión periódica
Trimestral: obsolescencia (normas cambiadas), duplicados nuevos, vínculos rotos, vocabulario
controlado (nuevos sinónimos de obra).

### Gestión del propio framework
Los cambios a la taxonomía se versionan en el historial de GitHub y deben reflejarse a la vez en `instrucciones_agente.txt` y en `KLECT_conocimiento.md`.

