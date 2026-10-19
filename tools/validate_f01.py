#!/usr/bin/env python3
"""Valida fichas KLECT-F01 (YAML o Markdown con bloque YAML) contra el esquema JSON y las
reglas de fidelidad KLECT (no inventar).

Uso:
    python tools/validate_f01.py examples/ficha_ejemplo.yaml
    python tools/validate_f01.py ficha.yaml --fuente texto_original.txt   # verifica citas literales
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parent.parent
SCHEMA = json.loads((ROOT / "schema" / "klect_f01.schema.json").read_text(encoding="utf-8"))

ORIGEN_TIPICO = {
    "CAT-1": {"Prefactibilidad", "Diseño Básico"},
    "CAT-2": {"Diseño Básico", "Diseño Detallado"},
    "CAT-3": {"Diseño Detallado", "Procura"},
    "CAT-4": {"Construcción"},
    "CAT-5": {"Operación"},
}

# Campos de hecho: nunca pueden tener origen "inferencia"
CAMPOS_HECHO = [
    "descripcion", "causa_raiz_detalle", "solucion", "recomendacion", "impacto_costo",
    "impacto_plazo", "proyecto_origen", "ubicacion", "componente", "aplica_cuando", "no_aplica_cuando",
]
# Campos de hecho bloqueantes (P1) para poder publicar
BLOQUEANTES = ["descripcion", "causa_raiz_detalle", "recomendacion"]


def norm(t: str) -> str:
    t = unicodedata.normalize("NFKD", t)
    t = "".join(c for c in t if not unicodedata.combining(c))
    return re.sub(r"\s+", " ", t).strip().lower()


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


def reglas_fidelidad(f: dict, fuente: str | None) -> tuple[list[str], list[str]]:
    errores: list[str] = []
    avisos: list[str] = []
    traz = f.get("trazabilidad") or {}

    for campo in CAMPOS_HECHO:
        valor = f.get(campo)
        if valor in (None, "", []):
            continue
        origen = traz.get(campo)
        if origen is None:
            errores.append(f"fidelidad: el campo de hecho '{campo}' tiene valor pero no tiene origen en 'trazabilidad'")
        elif origen == "inferencia":
            errores.append(f"fidelidad: '{campo}' es campo de hecho y no puede ser 'inferencia' (solo texto o usuario)")

    if any(traz.get(c) == "texto" for c in traz) and not f.get("citas_fuente"):
        errores.append("fidelidad: hay campos con origen 'texto' pero 'citas_fuente' está vacío")

    if fuente is not None:
        base = norm(fuente)
        for i, cita in enumerate(f.get("citas_fuente") or [], 1):
            if norm(cita) not in base:
                errores.append(f"fidelidad: la cita #{i} NO aparece literalmente en la fuente: «{cita[:80]}»")

    estado = f.get("estado_publicacion")
    if estado == "PUBLICABLE":
        for c in BLOQUEANTES:
            if f.get(c) in (None, ""):
                errores.append(f"publicación: falta el campo bloqueante '{c}' en una ficha PUBLICABLE")
        if f.get("sugerencias_agente"):
            errores.append("publicación: una ficha PUBLICABLE no debe llevar 'sugerencias_agente'")
        if f.get("severidad_provisional"):
            avisos.append("severidad provisional en ficha PUBLICABLE: confirmar con datos de costo")
    if estado in {"VERIFICADA", "PUBLICABLE"} and len(f.get("campos_faltantes") or []) > 5:
        avisos.append("muchos campos faltantes para el estado declarado")

    cat, fase = f.get("categoria"), f.get("fase")
    if cat in ORIGEN_TIPICO and fase and fase not in ORIGEN_TIPICO[cat]:
        avisos.append(f"coherencia: {cat} suele originarse en {sorted(ORIGEN_TIPICO[cat])}; fase='{fase}'. Registre fase_origen/fase_deteccion.")
    if f.get("id") and cat and not f["id"].startswith(cat.replace("-", "")):
        avisos.append(f"nomenclatura: el id '{f['id']}' no empieza con {cat.replace('-', '')}")
    if f.get("severidad") in {"Alta", "Media", "Baja"} and not f.get("impacto_costo") and not f.get("severidad_provisional"):
        avisos.append("severidad por % de contrato sin impacto_costo: marque severidad_provisional: true")
    if f.get("uniclass_ss") and not f.get("uniclass_verificado"):
        avisos.append("uniclass_ss sin verificar (uniclass_verificado: false)")
    return errores, avisos


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("fichas", nargs="+")
    ap.add_argument("--fuente", help="Archivo de texto original para verificar que las citas sean literales")
    args = ap.parse_args()

    fuente = Path(args.fuente).read_text(encoding="utf-8") if args.fuente else None
    validator = Draft202012Validator(SCHEMA)
    total = 0
    for arg in args.fichas:
        path = Path(arg)
        try:
            ficha = load_ficha(path)
        except Exception as exc:  # noqa: BLE001
            print(f"✗ {path}: {exc}")
            total += 1
            continue
        errs = [f"[{'.'.join(map(str, e.path)) or '(raíz)'}] {e.message}" for e in validator.iter_errors(ficha)]
        e2, avisos = reglas_fidelidad(ficha, fuente)
        errs += e2
        for e in errs:
            print(f"✗ {path}: {e}")
        for a in avisos:
            print(f"! {path}: {a}")
        if not errs:
            print(f"✓ {path} (estado: {ficha.get('estado_publicacion')})")
        total += len(errs)
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
