-- KLECT · Nivel L2 (relacional) — esquema de referencia (PostgreSQL)
-- Framework KLECT · Icónica Gestión S.A.C. (2025) · CC BY-SA 4.0

CREATE TABLE IF NOT EXISTS lecciones (
    id                  TEXT PRIMARY KEY CHECK (id ~ '^CAT[1-5]-[A-Z]{3}-[A-Z]{3}-[0-9]{3}$'),
    titulo              TEXT NOT NULL,
    categoria           TEXT NOT NULL CHECK (categoria IN ('CAT-1','CAT-2','CAT-3','CAT-4','CAT-5')),
    sistema             TEXT NOT NULL CHECK (sistema IN ('Estructural','Envolvente','Acabados','MEP-Mec','MEP-Elec','MEP-San','Sitio')),
    tipo_proyecto       TEXT NOT NULL CHECK (tipo_proyecto IN ('Residencial','Comercial','Industrial','Salud','Educación','Infraestructura')),
    fase                TEXT NOT NULL CHECK (fase IN ('Prefactibilidad','Diseño Básico','Diseño Detallado','Procura','Construcción','Operación')),
    severidad           TEXT NOT NULL CHECK (severidad IN ('Crítica','Alta','Media','Baja')),
    severidad_provisional BOOLEAN NOT NULL DEFAULT FALSE,
    disciplina          TEXT NOT NULL CHECK (disciplina IN ('Arquitectura','Estructural','MEP','Gestión Proyecto','Contratista','Subcontratista')),
    causa_raiz          TEXT NOT NULL CHECK (causa_raiz IN ('Comunicación','Proceso','Competencia','Herramienta','Condición externa')),
    uniclass_ss         TEXT CHECK (uniclass_ss ~ '^Ss_[0-9]{2}(_[0-9]{2}){0,3}$'),
    uniclass_verificado BOOLEAN NOT NULL DEFAULT FALSE,
    componente          TEXT,
    ubicacion           TEXT,
    proyecto_origen     TEXT,
    descripcion         TEXT NOT NULL,
    solucion            TEXT,
    recomendacion       TEXT,
    aplica_cuando       TEXT,
    no_aplica_cuando    TEXT,
    impacto_costo       TEXT,
    impacto_plazo       TEXT,
    creado_en           TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- Faceta F7 es multivalor
CREATE TABLE IF NOT EXISTS leccion_impacto (
    leccion_id TEXT REFERENCES lecciones(id) ON DELETE CASCADE,
    impacto    TEXT CHECK (impacto IN ('Costo','Cronograma','Calidad','Seguridad','Medio Ambiente','Reputación')),
    PRIMARY KEY (leccion_id, impacto)
);

CREATE TABLE IF NOT EXISTS leccion_termino (
    leccion_id TEXT REFERENCES lecciones(id) ON DELETE CASCADE,
    termino    TEXT NOT NULL,
    tipo       TEXT NOT NULL CHECK (tipo IN ('controlado','sinonimo','relacionado')),
    PRIMARY KEY (leccion_id, termino, tipo)
);

CREATE TABLE IF NOT EXISTS leccion_backward (
    leccion_id        TEXT PRIMARY KEY REFERENCES lecciones(id) ON DELETE CASCADE,
    item_checklist    TEXT NOT NULL,
    fase_verificacion TEXT NOT NULL CHECK (fase_verificacion IN ('Prefactibilidad','Diseño Básico','Diseño Detallado','Procura','Construcción','Operación')),
    nivel_riesgo      TEXT NOT NULL CHECK (nivel_riesgo IN ('Crítico','Alto','Medio'))
);

CREATE TABLE IF NOT EXISTS leccion_vinculo (
    origen_id  TEXT REFERENCES lecciones(id) ON DELETE CASCADE,
    destino_id TEXT REFERENCES lecciones(id) ON DELETE CASCADE,
    relacion   TEXT NOT NULL CHECK (relacion IN ('padre','hermano','relacionado','duplica','origina_procedimiento')),
    PRIMARY KEY (origen_id, destino_id, relacion)
);

CREATE INDEX IF NOT EXISTS idx_lecciones_facetas ON lecciones (categoria, sistema, fase, severidad);
CREATE INDEX IF NOT EXISTS idx_lecciones_fts ON lecciones
    USING GIN (to_tsvector('spanish', titulo || ' ' || descripcion || ' ' || coalesce(recomendacion,'')));
