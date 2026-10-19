-- Consultas L2 tipo (PostgreSQL) — KLECT

-- 1) Lecciones críticas/altas de estructura en construcción
SELECT id, titulo, severidad
FROM lecciones
WHERE categoria = 'CAT-4' AND sistema = 'Estructural' AND severidad IN ('Crítica','Alta');

-- 2) Checklist de revisión de diseño para una fase de un nuevo proyecto
SELECT l.id, b.item_checklist, b.nivel_riesgo
FROM leccion_backward b JOIN lecciones l ON l.id = b.leccion_id
WHERE b.fase_verificacion = 'Diseño Detallado' AND l.tipo_proyecto = 'Salud'
ORDER BY CASE b.nivel_riesgo WHEN 'Crítico' THEN 1 WHEN 'Alto' THEN 2 ELSE 3 END;

-- 3) Búsqueda de texto completo en español
SELECT id, titulo
FROM lecciones
WHERE to_tsvector('spanish', titulo || ' ' || descripcion) @@ plainto_tsquery('spanish', 'filtración losa sótano');

-- 4) Mapa de cobertura: nº de lecciones por categoría y sistema (detecta huecos)
SELECT categoria, sistema, count(*) AS n
FROM lecciones GROUP BY ROLLUP (categoria, sistema) ORDER BY categoria, sistema;

-- 5) Candidatos a duplicado (mismo sistema, fase y componente)
SELECT a.id, b.id AS posible_duplicado
FROM lecciones a JOIN lecciones b
  ON a.id < b.id AND a.sistema = b.sistema AND a.fase = b.fase
 AND lower(a.componente) = lower(b.componente);

-- 6) Lecciones sin clasificar completamente
SELECT id, titulo FROM lecciones
WHERE uniclass_ss IS NULL OR uniclass_verificado = FALSE;
