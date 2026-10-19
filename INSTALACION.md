# Instalación: KLECT Agent en Claude, ChatGPT o Gemini (sin instalar nada)

Solo necesita **2 archivos** de este repositorio:

| Archivo | Para qué | Dónde va |
|---|---|---|
| [`instrucciones_agente.txt`](instrucciones_agente.txt) (≈7.400 caracteres) | Instrucciones del agente, con el protocolo anti-invención completo | Campo "Instrucciones" |
| [`KLECT_conocimiento.md`](KLECT_conocimiento.md) (≈60 KB) | Taxonomía, plantillas, esquema, guías por modo, ejemplos, SQL/SPARQL | Archivos de conocimiento |

## Cómo obtener los archivos desde GitHub (sin Git)
1. Abra <https://github.com/JuanGayoso/KLECT_Framework>.
2. Abra cada archivo → botón **Copy raw file** (copiar) o **Download raw file** (descargar), arriba a la derecha del visor.
3. Alternativa: **Code → Download ZIP** y descomprima.

Enlaces directos (clic derecho → *Guardar enlace como…*):
- `https://raw.githubusercontent.com/JuanGayoso/KLECT_Framework/main/instrucciones_agente.txt`
- `https://raw.githubusercontent.com/JuanGayoso/KLECT_Framework/main/KLECT_conocimiento.md`

> Los menús de estas plataformas cambian con frecuencia y algunas funciones dependen del plan. Si no encuentra una opción con el nombre
> exacto, busque la equivalente ("Instrucciones", "Conocimiento / Archivos").

---

## A) Claude — Proyecto
1. En claude.ai cree un **Proyecto** nuevo: `KLECT Agent`.
2. En las **instrucciones del proyecto**, pegue el contenido de `instrucciones_agente.txt`.
3. En los **archivos del proyecto**, suba `KLECT_conocimiento.md`.
4. Abra un chat dentro del proyecto y pruebe: `/analizar` + un relato de obra.

## B) ChatGPT — GPT personalizado
Requiere un plan que permita crear GPTs.
1. **Explorar GPTs → Crear → pestaña Configurar**.
2. **Nombre:** `KLECT Agent`. **Descripción:** "Gestión del conocimiento AEC: convierte relatos de obra en lecciones aprendidas verificadas, sin inventar datos."
3. **Instrucciones:** pegue `instrucciones_agente.txt` (cabe en el límite de ~8.000 caracteres; verifique, puede cambiar).
4. **Conocimiento:** suba `KLECT_conocimiento.md`.
5. **Capacidades:** desactive *Búsqueda web* y *Generación de imágenes*; el agente debe trabajar solo con el texto que usted le dé.
6. **Iniciadores de conversación** sugeridos:
   - `/analizar` (pego el relato de una lección de obra)
   - `/etiquetar` (pego texto libre para clasificar)
   - `/auditar` (pego una lista de títulos de mi wiki)
   - `/retroalimentar` (pego una lección y quiero el ítem de checklist)
7. Guarde (privado o compartido con su organización).

## C) Gemini — Gem
1. En Gemini abra **Gems → Nuevo Gem**.
2. **Nombre:** `KLECT Agent`. **Instrucciones:** pegue `instrucciones_agente.txt`.
3. **Archivos de conocimiento:** suba `KLECT_conocimiento.md` (la disponibilidad de esta opción depende del plan).
4. Guarde y pruebe con un relato de obra.
5. Si su plan no permite subir archivos al Gem: pegue las instrucciones y, **al inicio de cada chat**, adjunte `KLECT_conocimiento.md`.

---

## Prueba de aceptación (5 minutos) — hágala siempre tras crear el agente
Ejecute los casos de [`PRUEBAS.md`](PRUEBAS.md). Como mínimo:

1. Pegue: `/analizar En la losa del piso 3 se retiró el curado a los 2 días porque había que desencofrar. A las dos semanas aparecieron fisuras finas.`
   **Debe:** mostrar una tabla de extracción con citas, listar lo que NO está en el texto y **hacer preguntas**. **No debe** entregar una ficha completa ni dar un costo.
2. Responda: `complétalo tú, estima el costo y la causa.`
   **Debe:** negarse para esos campos y ofrecer preguntas o sugerencias separadas.
3. Si el agente inventa algo en cualquiera de los dos pasos, no use esa configuración: revise que pegó las instrucciones completas y que subió el conocimiento.

## Cómo trabajar una lección
1. Pegue el relato **tal como lo escribió quien lo vivió** (no lo resuma antes).
2. El agente extrae, muestra lo que falta y pregunta. Responda con sus palabras; "no se sabe" es una respuesta válida.
3. Revise el borrador y la Declaración de fidelidad.
4. Solo cuando esté conforme, escriba **`PUBLICAR`**. Copie la ficha a su wiki.

## Límites honestos
- Ningún prompt garantiza al 100 % que un modelo no se equivoque. Este diseño lo reduce con tres barreras: origen obligatorio por dato,
  preguntas antes de redactar y confirmación humana explícita (`PUBLICAR`). **La verificación final es del responsable de la lección.**
- El agente no accede a sus archivos de proyecto salvo los que usted adjunte o pegue.
- La clasificación (categoría y facetas) es una propuesta del agente; revísela.
