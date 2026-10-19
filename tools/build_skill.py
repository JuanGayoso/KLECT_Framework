#!/usr/bin/env python3
"""Empaqueta KLECT Agent como skill de Claude en dist/klect-agent/ (+ .zip).

Uso: python tools/build_skill.py
"""
from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "agent" / "claude-skill" / "klect-agent"
DIST = ROOT / "dist" / "klect-agent"


def main() -> None:
    if DIST.parent.exists():
        shutil.rmtree(DIST.parent)
    shutil.copytree(SRC, DIST)
    ref = DIST / "references"
    ref.mkdir(parents=True, exist_ok=True)
    shutil.copy(ROOT / "agent" / "system_prompt.md", ref / "system_prompt.md")
    shutil.copytree(ROOT / "agent" / "modes", ref / "modes")
    shutil.copy(ROOT / "taxonomy" / "klect_taxonomy.yaml", ref / "taxonomy.yaml")
    shutil.copy(ROOT / "schema" / "klect_f01.schema.json", ref / "klect_f01.schema.json")
    shutil.copytree(ROOT / "templates", ref / "templates")
    archive = shutil.make_archive(str(DIST.parent / "klect-agent"), "zip", DIST.parent, "klect-agent")
    print(f"Skill generada en {DIST}\nZIP: {archive}")


if __name__ == "__main__":
    main()
