# 5. Gobierno y métricas

## Roles
| Rol | Responsabilidad |
|---|---|
| Patrocinador | Prioriza y protege tiempo para el aprendizaje |
| Knowledge Manager | Custodia taxonomía, calidad y agente; valida clasificaciones |
| Dueño de lección | Disciplina responsable de vigencia y vínculos de cada ficha |
| Revisor de diseño | Aplica el checklist backward-flow en cada fase |
| Contribuidores | Residentes, ingenieros, gestores: capturan lecciones |

## Flujo de una ficha
`Borrador` → `Clasificada (agente)` → `Validada (Knowledge Manager)` → `Publicada` → `Revisión periódica` / `Obsoleta`

## Métricas sugeridas
| Métrica | Pregunta que responde | Fuente |
|---|---|---|
| Cobertura CAT × Sistema | ¿Dónde no estamos aprendiendo? | `/auditar`, consulta 4 de `consultas_tipo.sql` |
| % fichas con F1–F8 completas | ¿Se puede recuperar? | `validate_f01.py` |
| % fichas con >2 criterios fallidos | ¿Calidad de captura? | Revisión de calidad |
| Duplicados detectados / fusionados | ¿Unicidad? | `/auditar`, consulta 5 |
| Ítems de checklist aplicados por proyecto | ¿Se cierra el ciclo? | `leccion_backward` |
| Tiempo desde evento hasta ficha publicada | ¿Capturamos a tiempo? | Registro de la wiki |

## Revisión periódica
Trimestral: obsolescencia (normas cambiadas), duplicados nuevos, vínculos rotos, vocabulario
controlado (nuevos sinónimos de obra).

## Gestión del propio framework
Cambios a la taxonomía se versionan en `CHANGELOG.md` y se proponen según `CONTRIBUTING.md`.
