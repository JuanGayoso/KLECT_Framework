#!/usr/bin/env python3
"""Genera deploy/KLECT_conocimiento.md (un solo archivo para subir como 'conocimiento' a un GPT,
un Gem de Gemini o un Proyecto de Claude) y deploy/claude/klect-agent.zip (skill de Claude).

Solo lo necesita quien MANTIENE el repositorio. Quien solo desea usar el agente descarga los archivos ya
generados de deploy/ y no instala nada.
"""
from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEPLOY = ROOT / "deploy"

SECCIONES = [
    ("PROTOCOLO DE FIDELIDAD (completo)", "agent/protocolo_fidelidad.md", "md"),
    ("TAXONOMÍA KLECT (YAML)", "taxonomy/klect_taxonomy.yaml", "yaml"),
    ("REFERENCIA UNICLASS Ss", "taxonomy/uniclass_ss_reference.md", "md"),
    ("ESQUEMA JSON DE LA FICHA KLECT-F01", "schema/klect_f01.schema.json", "json"),
    ("PLANTILLA KLECT-F01 (lección aprendida)", "templates/KLECT-F01.md", "md"),
    ("PLANTILLA KLECT-PROC (procedimiento)", "templates/KLECT-PROC.md", "md"),
    ("PLANTILLA KLECT-REF (referencia técnica)", "templates/KLECT-REF.md", "md"),
    ("CHECKLIST BACKWARD-FLOW", "templates/backward_flow_checklist.md", "md"),
    ("MODO /analizar", "agent/modes/analizar.md", "md"),
    ("MODO /auditar", "agent/modes/auditar.md", "md"),
    ("MODO /etiquetar", "agent/modes/etiquetar.md", "md"),
    ("MODO /buscar", "agent/modes/buscar.md", "md"),
    ("MODO /retroalimentar", "agent/modes/retroalimentar.md", "md"),
    ("MODO /arquitectura", "agent/modes/arquitectura.md", "md"),
    ("EJEMPLO — Fases 1 y 2", "examples/01_fase1_extraccion_y_preguntas.md", "md"),
    ("EJEMPLO — Fases 3 y 4", "examples/02_respuestas_y_borrador.md", "md"),
    ("EJEMPLO — ficha YAML (hipotética)", "examples/ficha_ejemplo.yaml", "yaml"),
    ("ONTOLOGÍA OWL/Turtle (para SPARQL)", "queries/sparql/klect_ontology.ttl", "turtle"),
    ("CONSULTAS SPARQL TIPO", "queries/sparql/consultas_tipo.rq", "sparql"),
    ("ESQUEMA SQL (L2)", "queries/sql/schema.sql", "sql"),
    ("CONSULTAS SQL TIPO", "queries/sql/consultas_tipo.sql", "sql"),
]


def build_knowledge() -> Path:
    out = ["# KLECT_conocimiento\n",
           "Archivo único de conocimiento de KLECT Agent. Framework KLECT · Icónica Gestión S.A.C. (2025) · CC BY-SA 4.0.\n",
           "Generado por tools/build_knowledge.py — no editar a mano; edite los archivos fuente del repositorio.\n"]
    for i, (titulo, rel, lang) in enumerate(SECCIONES, 1):
        body = (ROOT / rel).read_text(encoding="utf-8").strip()
        out.append(f"\n\n---\n\n# [{i:02d}] {titulo}\n(fuente: {rel})\n")
        out.append(body if rel.endswith(".md") else f"```{lang}\n{body}\n```")
    path = DEPLOY / "KLECT_conocimiento.md"
    path.write_text("\n".join(out) + "\n", encoding="utf-8")
    return path


def build_skill() -> Path:
    tmp = ROOT / "dist"
    if tmp.exists():
        shutil.rmtree(tmp)
    skill = tmp / "klect-agent"
    shutil.copytree(ROOT / "agent" / "claude-skill" / "klect-agent", skill)
    ref = skill / "references"
    ref.mkdir(parents=True, exist_ok=True)
    shutil.copy(ROOT / "agent" / "system_prompt.md", ref / "system_prompt.md")
    shutil.copy(DEPLOY / "KLECT_conocimiento.md", ref / "KLECT_conocimiento.md")
    shutil.copy(ROOT / "taxonomy" / "klect_taxonomy.yaml", ref / "taxonomy.yaml")
    shutil.copy(ROOT / "schema" / "klect_f01.schema.json", ref / "klect_f01.schema.json")
    (DEPLOY / "claude").mkdir(parents=True, exist_ok=True)
    archive = shutil.make_archive(str(DEPLOY / "claude" / "klect-agent"), "zip", tmp, "klect-agent")
    shutil.rmtree(tmp)
    return Path(archive)


if __name__ == "__main__":
    k = build_knowledge()
    z = build_skill()
    print(f"{k} ({k.stat().st_size // 1024} KB)\n{z} ({z.stat().st_size // 1024} KB)")
