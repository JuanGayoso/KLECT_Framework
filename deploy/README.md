# deploy/ — archivos listos para usar (sin instalar nada)

| Archivo | Uso |
|---|---|
| `instrucciones_compactas.txt` | Pegar en las **instrucciones** de un Proyecto de Claude, un GPT o un Gem (≈7.400 caracteres) |
| `KLECT_conocimiento.md` | Subir como **conocimiento / archivo del proyecto** |
| `claude/klect-agent.zip` | Skill de Claude (opcional, si su plan tiene Skills) |

Guía paso a paso: [`../docs/06-despliegue-sin-instalar.md`](../docs/06-despliegue-sin-instalar.md).

Estos archivos se generan con `tools/build_knowledge.py` (solo para mantenedores del repositorio).
`instrucciones_compactas.txt` se edita a mano: mantenga sincronizado con `agent/protocolo_fidelidad.md` y `agent/system_prompt.md`.
