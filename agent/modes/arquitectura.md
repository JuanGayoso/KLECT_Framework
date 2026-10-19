# Modo `/arquitectura [descripción de la organización]`

**Propósito:** diseñar la estructura completa de la wiki de conocimiento.
**Salida:** árbol de categorías → plantillas → convención de nomenclatura → hoja de ruta.

## Datos de entrada útiles
Tamaño de la organización, tipos de proyecto, herramientas actuales (SharePoint, Notion, Confluence, MediaWiki…), volumen de lecciones existentes, roles responsables.
Si faltan, preguntar como máximo 3 cosas y, aun así, proponer una versión inicial.

## Estructura base propuesta
```
KLECT/
├── 01-Lecciones/
│   ├── CAT-1-Supuestos/ … CAT-5-Mantenibilidad/
│   │   └── <Sistema F1>/
├── 02-Procedimientos/ (KLECT-PROC)
├── 03-Referencias/ (KLECT-REF)
├── 04-Backward-Flow/ (checklists por fase)
├── 05-Taxonomia/ (vocabulario controlado, Uniclass)
└── 99-Gobierno/ (roles, calidad, métricas)
```
## Convención de nombres
`CATn-SIS-FAS-NNN / Título descriptivo` (ver `docs/03-arquitectura-wiki.md`).

## Hoja de ruta
Usar la de `docs/04-hoja-de-ruta.md` adaptándola al tamaño y a los recursos de la organización.
