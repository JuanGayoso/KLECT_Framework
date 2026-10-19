# 3. Arquitectura de la wiki de conocimiento

## Árbol de categorías (propuesta base)
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

## Plantillas
| Contenido | Plantilla |
|---|---|
| Lección aprendida | `KLECT-F01` |
| Procedimiento repetible | `KLECT-PROC` |
| Estándar / referencia técnica | `KLECT-REF` |

## Convención de nomenclatura
`CATn-SIS-FAS-NNN / Título descriptivo`

| Parte | Significado | Valores |
|---|---|---|
| `CATn` | Categoría | CAT1…CAT5 |
| `SIS` | Sistema F1 | EST, ENV, ACA, MEC, ELE, SAN, SIT |
| `FAS` | Fase F3 | PRE, DBA, DDE, PRO, CON, OPE |
| `NNN` | Correlativo por combinación | 001… |

Ejemplo: `CAT4-EST-CON-001 / Curado inadecuado de concreto`.
Procedimientos: `PROC-SIS-FAS-NNN`; referencias: `REF-SIS-NNN`.

## Relaciones entre artículos
`padre` · `hermano` · `relacionado` · `duplica` · `origina_procedimiento`
(modeladas en `leccion_vinculo` de L2 y en `klect:relacionadaCon`/`klect:duplicaA` de L3).

## Política de metadatos
- Todas las facetas F1–F8 son **obligatorias** al clasificar; si no se pueden determinar, se
  declara el faltante, no se supone.
- `uniclass_ss` solo con código verificable (`uniclass_verificado`).
- Una lección = un problema. Si mezcla varios, se divide.

## Plataformas
La estructura es agnóstica: SharePoint, Notion, Confluence, MediaWiki u otra. Lo esencial es
que los metadatos sean campos filtrables (propiedades/columnas), no texto libre.
