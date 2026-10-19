# KLECT — Knowledge Lifecycle for Engineering and Construction Toolbox

**Un agente de IA que convierte las lecciones aprendidas de obra en conocimiento clasificado, recuperable y reutilizable — sin inventar nada.**
Funciona en **Claude, ChatGPT y Gemini** pegando dos archivos. No hay que instalar nada.

> Framework KLECT · Icónica Gestión S.A.C. (Lima, Perú, 2025) · AEC Knowledge Series N°01 · [CC BY-SA 4.0](LICENSE.md)
> Este repositorio es la implementación como agente de IA del paper original: [**Framework para la gestión, clasificación y transmisión de lecciones aprendidas en organizaciones de construcción**](KLECT_Framework_IconicaGestion_2025.pdf) (Juan Germán Gayoso Arnillas, Icónica Gestión / Icónica Arquitectura Integral SAC, 2025).

## ¿Por qué se llama KLECT?

Según el [paper original](KLECT_Framework_IconicaGestion_2025.pdf) (Resumen y §1 Introducción), **KLECT** es la sigla de **K**nowledge **L**ifecycle for **E**ngineering and **C**onstruction **T**oolbox
(*Ciclo de vida del conocimiento para ingeniería y construcción — caja de herramientas*):

| Parte del nombre | Qué significa en el framework |
|---|---|
| **Knowledge Lifecycle** | El conocimiento tiene un ciclo de vida de 5 fases: **adquisición → parametrización → almacenamiento → recuperación → uso y retroalimentación** (esta última devuelve la lección a la etapa de diseño: *backward-flow*) |
| **Engineering and Construction** | El sector AEC: arquitectura, ingeniería y construcción |
| **Toolbox** | Un conjunto de herramientas desplegable por niveles de madurez: taxonomía, ficha de lección, procedimientos, ontología, consultas SQL/SPARQL y, aquí, el agente de IA |

## Qué hace el agente

Clasifica con una taxonomía de **5 categorías** (supuestos de diseño erróneos, defectos de diseño, especificaciones deficientes, defectos de construcción,
problemas de mantenibilidad) y **8 facetas** (sistema, tipo de proyecto, fase, severidad, disciplina, causa raíz, impacto, Uniclass 2015).
Comandos: `/analizar` · `/auditar` · `/etiquetar` · `/buscar` · `/retroalimentar` · `/arquitectura` · `/piloto`.

## Regla central: no inventa la lección

El agente es editor, no autor. Cada dato de hecho (qué pasó, causa, cifras, solución, recomendación) debe venir **del texto que usted le dio** o de
**sus respuestas**. Si falta algo, lo dice y pregunta. Flujo obligatorio:

**1 Extracción** (con citas literales) → **2 Preguntas** → **3 Borrador** → **4 Publicación**, que solo ocurre cuando usted escribe `PUBLICAR`.
Si le pide "complétalo tú" o "estima el costo", se niega para esos campos. Pruebas en [`PRUEBAS.md`](PRUEBAS.md).

## Lecciones relevantes pero sin cifras: sello de validez y plan piloto

Una lección con buenas recomendaciones pero sin datos cuantitativos de impacto o costo **sí se levanta**, pero queda marcada:
`🧪 EN VALIDACIÓN — FALTAN INDICADORES OBJETIVOS` (campo `validez` de la ficha, con la lista de `indicadores_faltantes`).
La organización puede adoptarla como **buena práctica en validación**, con esa advertencia, y el agente propone un **plan piloto** (`/piloto`)
para generar los sustentos cuantitativos. El agente nunca estima cifras para quitar el sello: pasa a `VALIDADA` solo con datos medidos que usted aporte.
Detalle en [`GUIA_IMPLEMENTACION.md`](GUIA_IMPLEMENTACION.md) (sección 5).

## Cómo usarlo (sin instalar nada)

1. Cree un Proyecto de Claude, un GPT personalizado o un Gem de Gemini.
2. Pegue [`instrucciones_agente.txt`](instrucciones_agente.txt) en las **instrucciones**.
3. Suba [`KLECT_conocimiento.md`](KLECT_conocimiento.md) como **conocimiento**.
4. Haga la prueba de aceptación de [`PRUEBAS.md`](PRUEBAS.md).

Pasos detallados por plataforma y cómo descargar desde GitHub: [`INSTALACION.md`](INSTALACION.md).

## Qué hay en este repositorio

| Archivo | Para qué |
|---|---|
| [`KLECT_Framework_IconicaGestion_2025.pdf`](KLECT_Framework_IconicaGestion_2025.pdf) | **Paper original** (22 p.): de aquí sale toda la taxonomía, el ciclo de vida, la ontología y el toolbox. Es referencia para personas; no se sube al agente |
| [`instrucciones_agente.txt`](instrucciones_agente.txt) | Las instrucciones del agente (≈7.900 caracteres, caben en un GPT) |
| [`KLECT_conocimiento.md`](KLECT_conocimiento.md) | Todo el conocimiento: instrucciones completas, taxonomía, esquema de ficha, plantillas (incluye KLECT-PILOT), guías por modo, ejemplos, ontología, SQL y SPARQL |
| [`INSTALACION.md`](INSTALACION.md) | Guía paso a paso para Claude, ChatGPT y Gemini |
| [`PRUEBAS.md`](PRUEBAS.md) | 15 casos para comprobar que el agente no alucina |
| [`GUIA_IMPLEMENTACION.md`](GUIA_IMPLEMENTACION.md) | Cultura de aprendizaje, arquitectura de la wiki, hoja de ruta y gobierno |
| [`LICENSE.md`](LICENSE.md) | Licencia CC BY-SA 4.0 |

## Pendientes conocidos
- Los códigos Uniclass de nivel específico no están incluidos: el agente cita solo lo que puede respaldar y marca "(verificar contra catálogo oficial NBS)".
- La ontología de `KLECT_conocimiento.md` es una **referencia simplificada**; no equivale a la ontología OWL descrita en el paper (§5) y su namespace es un marcador de posición.
- El agente usa las 6 fases de proyecto de sus instrucciones; el paper (Tabla 3) lista además *Comisionamiento* y *Demolición*.
- Los ejemplos son hipotéticos.

## Cómo citar
Icónica Gestión S.A.C. (2025). *Framework KLECT*. AEC Knowledge Series N°01.

Paper: Gayoso Arnillas, J. G. (2025). *Framework para la gestión, clasificación y transmisión de lecciones aprendidas en organizaciones de construcción: un enfoque desde la bibliotecología, las ontologías formales y la inteligencia artificial*. Icónica Gestión / Icónica Arquitectura Integral SAC, Lima, Perú.
