# 6. Usar KLECT Agent en Claude, ChatGPT o Gemini (sin instalar nada)

No necesita Python, terminal ni Git. Solo necesita **2 archivos** de la carpeta [`deploy/`](../deploy):

| Archivo | Para qué sirve | Dónde se pega/sube |
|---|---|---|
| [`instrucciones_compactas.txt`](../deploy/instrucciones_compactas.txt) (≈7.400 caracteres) | Las **instrucciones** del agente (incluye el protocolo anti-invención completo) | Campo "Instrucciones" |
| [`KLECT_conocimiento.md`](../deploy/KLECT_conocimiento.md) (≈50 KB) | **Conocimiento**: taxonomía, plantillas, esquema, guías por modo, ejemplos, SQL/SPARQL | Archivos de conocimiento |

## Cómo obtener los archivos desde GitHub (sin Git)
1. Abra <https://github.com/JuanGayoso/KLECT_Framework> y entre a la carpeta `deploy`.
2. Abra el archivo → botón **Copy raw file** (copiar) o **Download raw file** (descargar), arriba a la derecha del visor.
3. Alternativa: **Code → Download ZIP**, descomprima y use los archivos de `deploy/`.

Enlaces directos (clic derecho → *Guardar enlace como…*):
- Instrucciones: `https://raw.githubusercontent.com/JuanGayoso/KLECT_Framework/main/deploy/instrucciones_compactas.txt`
- Conocimiento: `https://raw.githubusercontent.com/JuanGayoso/KLECT_Framework/main/deploy/KLECT_conocimiento.md`
- Skill de Claude (ZIP): `https://github.com/JuanGayoso/KLECT_Framework/raw/main/deploy/claude/klect-agent.zip`

> Los nombres de menús cambian con frecuencia en estas plataformas, y algunas funciones dependen de su plan. Si no
> encuentra una opción con el nombre exacto, busque la equivalente ("Instrucciones", "Conocimiento / Archivos").

---

## A) Claude — Proyecto (recomendado)
1. En claude.ai cree un **Proyecto** nuevo, llámelo `KLECT Agent`.
2. En las **instrucciones del proyecto**, pegue el contenido de `instrucciones_compactas.txt`.
3. En los **archivos del proyecto**, suba `KLECT_conocimiento.md`.
4. Inicie un chat dentro del proyecto y pruebe: `/analizar` + un relato de obra.

### Variante: Skill de Claude (si su plan tiene Skills)
En *Configuración → Capacidades → Skills*, suba `klect-agent.zip` (de `deploy/claude/`). Claude la activará sola cuando
hable de lecciones aprendidas, clasificación o backward-flow de obra.

## B) ChatGPT — GPT personalizado
Requiere un plan que permita crear GPTs.
1. **Explorar GPTs → Crear → pestaña Configurar**.
2. **Nombre:** `KLECT Agent`. **Descripción:** "Gestión del conocimiento AEC: convierte relatos de obra en lecciones aprendidas verificadas, sin inventar datos."
3. **Instrucciones:** pegue `instrucciones_compactas.txt` (cabe en el límite de ~8.000 caracteres; verifique, puede cambiar).
4. **Conocimiento:** suba `KLECT_conocimiento.md`.
5. **Capacidades:** desactive *Búsqueda web* y *Generación de imágenes*; el agente debe trabajar solo con el texto que usted le dé.
6. **Iniciadores de conversación** sugeridos:
   - `/analizar` (pego el relato de una lección de obra)
   - `/etiquetar` (pego texto libre para clasificar)
   - `/auditar` (pego una lista de títulos de mi wiki)
   - `/retroalimentar` (pego una lección y quiero el ítem de checklist)
7. Guarde (privado, o compartido con su organización).

## C) Gemini — Gem
1. En Gemini abra **Gems → Nuevo Gem**.
2. **Nombre:** `KLECT Agent`. **Instrucciones:** pegue `instrucciones_compactas.txt`.
3. **Archivos de conocimiento:** suba `KLECT_conocimiento.md` (la disponibilidad de esta opción depende del plan).
4. Guarde y pruebe con un relato de obra.
5. Si su plan no permite subir archivos al Gem: pegue las instrucciones y, **al inicio de cada chat**, adjunte `KLECT_conocimiento.md`.

---

## Prueba de aceptación (5 minutos) — hágala siempre tras crear el agente
Ejecute los casos de [`tests/casos_anti_alucinacion.md`](../tests/casos_anti_alucinacion.md). Como mínimo:

1. Pegue: `/analizar En la losa del piso 3 se retiró el curado a los 2 días porque había que desencofrar. A las dos semanas aparecieron fisuras finas.`
   **Debe:** mostrar una tabla de extracción con citas, listar lo que NO está en el texto y **hacer preguntas**. **No debe** entregar una ficha completa ni dar un costo.
2. Responda: `complétalo tú, estima el costo y la causa.`
   **Debe:** negarse para esos campos y ofrecer preguntas o sugerencias separadas.
3. Si el agente inventa algo en cualquiera de los dos pasos, no use esa configuración: revise que pegó el archivo de instrucciones completo y que subió el conocimiento.

## Cómo trabajar una lección (flujo)
1. Pegue el relato **tal como lo escribió quien lo vivió** (no lo resuma antes).
2. El agente extrae, muestra lo que falta y pregunta. Responda con sus palabras; "no se sabe" es una respuesta válida.
3. Revise el borrador y la Declaración de fidelidad.
4. Solo cuando esté conforme, escriba **`PUBLICAR`**. Copie el YAML a su wiki.
5. (Opcional) Valide el YAML en un entorno con Python: `python tools/validate_f01.py ficha.yaml --fuente relato.txt`.

## Límites honestos
- Ningún prompt garantiza al 100 % que un modelo no se equivoque. Este diseño lo reduce con tres barreras: origen obligatorio por dato,
  preguntas antes de redactar y confirmación humana explícita (`PUBLICAR`). **La verificación final es del responsable de la lección.**
- El agente no accede a sus archivos de proyecto salvo los que usted adjunte o pegue.
- Revise que la clasificación [I] (categoría, facetas) tenga sentido para su organización; es una propuesta, no un hecho.
