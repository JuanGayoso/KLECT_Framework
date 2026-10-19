#!/usr/bin/env python3
"""Valida fichas KLECT-F01 (YAML o Markdown con front-matter YAML) contra el esquema JSON
y contra reglas de coherencia KLECT.

Uso:
    python tools/validate_f01.py examples/ficha_ejemplo.yaml
    python tools/validate_f01.py wiki/01-Lecciones/**/*.md
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parent.parent
SCHEMA = json.loads((ROOT / "schema" / "klect_f01.schema.json").read_text(encoding="utf-8"))

# Coherencia CAT ↔ fase de origen típica (taxonomy/klect_taxonomy.yaml)
ORIGEN_TIPICO = {
    "CAT-1": {"Prefactibilidad", "Diseño Básico"},
    "CAT-2": {"Diseño Básico", "Diseño Detallado"},
    "CAT-3": {"Diseño Detallado", "Procura"},
    "CAT-4": {"Construcción"},
    "CAT-5": {"Operación"},
}


def load_ficha(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if path.suffix.lower() in {".md", ".markdown"}:
        m = re.search(r"```yaml\s*\n(.*?)\n```", text, re.S) or re.match(r"---\n(.*?)\n---", text, re.S)
        if not m:
            raise ValueError("no se encontró bloque YAML (front-matter o ```yaml)")
        text = m.group(1).strip().strip("-").strip()
    data = yaml.safe_load(text)
    if not isinstance(data, dict):
        raise ValueError("el YAML no es un mapeo")
    return data


def reglas_klect(f: dict) -> list[str]:
    avisos: list[str] = []
    cat = f.get("categoria")
    fase = f.get("fase")
    if cat in ORIGEN_TIPICO and fase and fase not in ORIGEN_TIPICO[cat]:
        avisos.append(
            f"coherencia: {cat} suele originarse en {sorted(ORIGEN_TIPICO[cat])}, "
            f"pero fase='{fase}'. Si difiere la fase de detección, registre fase_origen y fase_deteccion."
        )
    if f.get("id") and cat and not f["id"].startswith(cat.replace("-", "")):
        avisos.append(f"nomenclatura: el id '{f['id']}' no empieza con {cat.replace('-', '')}")
    if f.get("severidad") in {"Alta", "Media", "Baja"} and not f.get("impacto_costo") and not f.get("severidad_provisional"):
        avisos.append("severidad por % de contrato sin impacto_costo: marque severidad_provisional: true")
    if f.get("uniclass_ss") and not f.get("uniclass_verificado"):
        avisos.append("uniclass_ss sin verificar (uniclass_verificado: false)")
    if len(f.get("campos_faltantes") or []) > 3:
        avisos.append("calidad: >3 campos faltantes; el agente debería solicitar más información")
    return avisos


def main(argv: list[str]) -> int:
    if not argv:
        print(__doc__)
        return 2
    validator = Draft202012Validator(SCHEMA)
    errores = 0
    for arg in argv:
        path = Path(arg)
        try:
            ficha = load_ficha(path)
        except Exception as exc:  # noqa: BLE001
            print(f"✗ {path}: {exc}")
            errores += 1
            continue
        errs = sorted(validator.iter_errors(ficha), key=lambda e: list(e.path))
        for e in errs:
            loc = ".".join(map(str, e.path)) or "(raíz)"
            print(f"✗ {path} [{loc}]: {e.message}")
        errores += len(errs)
        for a in reglas_klect(ficha):
            print(f"! {path}: {a}")
        if not errs:
            print(f"✓ {path}")
    return 1 if errores else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
