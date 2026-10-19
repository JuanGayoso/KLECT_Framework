#!/usr/bin/env python3
"""Ejecuta KLECT Agent contra la API de Anthropic usando agent/system_prompt.md.

Requiere: pip install anthropic   y   export ANTHROPIC_API_KEY=...
Variable opcional: KLECT_MODEL (modelo a usar; ver https://docs.claude.com).

Uso:
    python tools/run_agent.py "/analizar <texto del artículo>"
    python tools/run_agent.py --file articulo.md --mode analizar
    python tools/run_agent.py --chat           # sesión interactiva
"""
from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

import anthropic

ROOT = Path(__file__).resolve().parent.parent
MODES = ["analizar", "auditar", "etiquetar", "buscar", "retroalimentar", "arquitectura"]
DEFAULT_MODEL = os.environ.get("KLECT_MODEL", "claude-sonnet-5-5")


def build_system() -> str:
    base = (ROOT / "agent" / "system_prompt.md").read_text(encoding="utf-8")
    extras = []
    for m in MODES:
        extras.append((ROOT / "agent" / "modes" / f"{m}.md").read_text(encoding="utf-8"))
    schema = (ROOT / "schema" / "klect_f01.schema.json").read_text(encoding="utf-8")
    return (
        base
        + "\n\n## GUÍAS DETALLADAS POR MODO\n\n" + "\n\n".join(extras)
        + "\n\n## ESQUEMA JSON DE LA FICHA KLECT-F01\n```json\n" + schema + "\n```\n"
    )


def ask(client: anthropic.Anthropic, system: str, messages: list[dict]) -> str:
    resp = client.messages.create(model=DEFAULT_MODEL, max_tokens=4096, system=system, messages=messages)
    return "".join(b.text for b in resp.content if b.type == "text")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("prompt", nargs="?", help="Mensaje (puede iniciar con /modo)")
    ap.add_argument("--file", help="Archivo con el texto a procesar")
    ap.add_argument("--mode", choices=MODES, help="Modo a aplicar al contenido de --file")
    ap.add_argument("--chat", action="store_true", help="Sesión interactiva")
    args = ap.parse_args()

    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("Falta ANTHROPIC_API_KEY", file=sys.stderr)
        return 2

    client = anthropic.Anthropic()
    system = build_system()

    if args.chat:
        history: list[dict] = []
        print("KLECT Agent — escriba /modo texto (Ctrl+D para salir)")
        while True:
            try:
                user = input("\n> ").strip()
            except EOFError:
                break
            if not user:
                continue
            history.append({"role": "user", "content": user})
            answer = ask(client, system, history)
            history.append({"role": "assistant", "content": answer})
            print("\n" + answer)
        return 0

    content = args.prompt or ""
    if args.file:
        body = Path(args.file).read_text(encoding="utf-8")
        prefix = f"/{args.mode} " if args.mode else ""
        content = f"{prefix}{content}\n\n{body}".strip()
    if not content:
        ap.print_help()
        return 2
    print(ask(client, system, [{"role": "user", "content": content}]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
