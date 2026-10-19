# Modo `/auditar [lista de títulos o sección wiki]`

**Propósito:** evaluar la coherencia global de una colección de artículos.
**Salida:** Mapa de cobertura → Huecos críticos → Duplicados → Prioridades.

## Procedimiento
1. **Clasificación rápida** de cada título (CAT, F1, F3 probables). Marcar `sin clasificar` si no hay base suficiente; no inventar.
2. **Mapa de cobertura:** matriz CAT × Sistema (F1) con conteo; segunda matriz Fase (F3) × Sistema.
3. **Huecos críticos:** celdas vacías donde la experiencia sectorial indica que debería haber lecciones (p. ej. CAT-1 en Estructural/Prefactibilidad). Distinguir "hueco real" de "no aplica al portafolio".
4. **Duplicados:** títulos semánticamente equivalentes; proponer fusión y cuál es el artículo maestro.
5. **Prioridades:** ordenar acciones por (severidad potencial × facilidad de corrección). Máx. 10 ítems.

## Formato
```
MAPA DE COBERTURA (CAT × F1)
| | EST | ENV | ACA | MEC | ELE | SAN | SIT |
...
HUECOS CRÍTICOS: ...
DUPLICADOS: A ≈ B → fusionar en A
PRIORIDADES: 1) ... 2) ...
```
Aclarar siempre que la auditoría por títulos es **preliminar**; la confirmación exige leer el contenido.
