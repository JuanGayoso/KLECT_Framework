# KLECT — Knowledge Lifecycle for Engineering and Construction Toolbox

**Un agente de IA que convierte las lecciones aprendidas de obra en conocimiento clasificado, recuperable y reutilizable — sin inventar nada.**
Funciona en **Claude, ChatGPT y Gemini** pegando dos archivos. No hay que instalar nada.

> Framework KLECT · Icónica Gestión S.A.C. (Lima, Perú, 2025) · AEC Knowledge Series N°01 · [CC BY-SA 4.0](LICENSE.md)

## ¿Por qué se llama KLECT?

Según el documento del framework, **KLECT** es la sigla de **K**nowledge **L**ifecycle for **E**ngineering and **C**onstruction **T**oolbox
(*Ciclo de vida del conocimiento para ingeniería y construcción — caja de herramientas*):

| Parte del nombre | Qué significa en el framework |
|---|---|
| **Knowledge Lifecycle** | El conocimiento tiene un ciclo de vida de 5 fases: **adquisición → parametrización → almacenamiento → recuperación → uso y retroalimentación** (esta última devuelve la lección a la etapa de diseño: *backward-flow*) |
| **Engineering and Construction** | El sector AEC: arquitectura, ingeniería y construcción |
| **Toolbox** | Un conjunto de herramientas desplegable por niveles de madurez: taxonomía, ficha de lección, procedimientos, ontología, consultas SQL/SPARQL y, aquí, el agente de IA |

## Qué hace el agente

Clasifica con una taxonomía de **5 categorías** (supuestos de diseño erróneos, defectos de diseño, especificaciones deficientes, defectos de construcción,
problemas de mantenibilidad) y **8 facetas** (sistema, tipo de proyecto, fase, severidad, disciplina, causa raíz, impacto, Uniclass 2015).
Comandos: `/analizar` · `/auditar` · `/etiquetar` · `/buscar` · `/retroalimentar` · `/arquitectura`.

## Regla central: no inventa la lección

El agente es editor, no autor. Cada dato de hecho (qué pasó, causa, cifras, solución, recomendación) debe venir **del texto que usted le dio** o de
**sus respuestas**. Si falta algo, lo dice y pregunta. Flujo obligatorio:

**1 Extracción** (con citas literales) → **2 Preguntas** → **3 Borrador** → **4 Publicación**, que solo ocurre cuando usted escribe `PUBLICAR`.
Si le pide "complétalo tú" o "estima el costo", se niega para esos campos. Pruebas en [`PRUEBAS.md`](PRUEBAS.md).

## Cómo usarlo (sin instalar nada)

1. Cree un Proyecto de Claude, un GPT personalizado o un Gem de Gemini.
2. Pegue [`instrucciones_agente.txt`](instrucciones_agente.txt) en las **instrucciones**.
3. Suba [`KLECT_conocimiento.md`](KLECT_conocimiento.md) como **conocimiento**.
4. Haga la prueba de aceptación de [`PRUEBAS.md`](PRUEBAS.md).

Pasos detallados por plataforma y cómo descargar desde GitHub: [`INSTALACION.md`](INSTALACION.md).

## Qué hay en este repositorio

| Archivo | Para qué |
|---|---|
| [`instrucciones_agente.txt`](instrucciones_agente.txt) | Las instrucciones del agente (≈7.400 caracteres, caben en un GPT) |
| [`KLECT_conocimiento.md`](KLECT_conocimiento.md) | Todo el conocimiento: instrucciones completas, taxonomía, esquema de ficha, plantillas, guías por modo, ejemplos, ontología, SQL y SPARQL |
| [`INSTALACION.md`](INSTALACION.md) | Guía paso a paso para Claude, ChatGPT y Gemini |
| [`PRUEBAS.md`](PRUEBAS.md) | 11 casos para comprobar que el agente no alucina |
| [`GUIA_IMPLEMENTACION.md`](GUIA_IMPLEMENTACION.md) | Cultura de aprendizaje, arquitectura de la wiki, hoja de ruta y gobierno |
| [`LICENSE.md`](LICENSE.md) | Licencia CC BY-SA 4.0 |

## Pendientes conocidos
- Los códigos Uniclass de nivel específico no están incluidos: el agente cita solo lo que puede respaldar y marca "(verificar contra catálogo oficial NBS)".
- La ontología de `KLECT_conocimiento.md` es una **referencia simplificada**; no equivale al archivo `KLECT-ONT-v1.0.owl` del documento original y su namespace es un marcador de posición.
- Los ejemplos son hipotéticos.

## Cómo citar
Icónica Gestión S.A.C. (2025). *Framework KLECT*. AEC Knowledge Series N°01.
