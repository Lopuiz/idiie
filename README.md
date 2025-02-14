# Bienvenidos al proyecto de Desarrollo Web en Entorno Servidor (DWES)

En este proyecto de Desarrollo Web en Entorno Servidor de FP DAW, tendrás la oportunidad de crear tu propia
aplicación web basada en un tema que elijas. A lo largo del proyecto, podrás aplicar todo lo aprendido sobre
programación backend, trabajando con herramientas como Python, FastAPI y bases de datos. Lo más importante es
que aprenderás a construir una aplicación completa, desde la lógica que hace que funcione hasta la interfaz con
la que interactúan los usuarios. ¡Es tu oportunidad para poner en práctica tus habilidades y creatividad!


## Git y Github

Antes de empezar, es importante que te familiarices con Git y GitHub, ya que los usarás para gestionar tu proyecto.
A continuación te dejo algunos enlaces que pueden ser de ayuda:

* [Documentación de Git](https://git-scm.com/book/es/v2)
* [Documentación de Github](https://docs.github.com/es)

Para comenzar, crea una cuenta en GitHub si aún no tienes una. Luego, haz un fork de este repositorio para trabajar sobre el.
Clona el repositorio en tu ordenador y empieza a trabajar en tu proyecto. ¡Manos a la obra! 🚀


## Ejecuta el servicio web

Aquí tienes los pasos para crear un entorno virtual, instalar dependencias y ejecutar tu aplicación:

**Crear el entorno virtual:**

Abre la terminal y navega a la carpeta de tu proyecto. Escribe el siguiente comando:
```
python -m venv .venv
```

**Activar el entorno virtual:**

* En Windows: `.\.venv\Scripts\activate`
* En macOS/Linux: `source .venv/bin/activate`

**Instalar las dependencias:**

Asegúrate de tener el archivo `requirements.txt` en tu proyecto.
Instala las librerías necesarias con:
```
pip install -r requirements.txt
```

**Ejecutar la aplicación:**

Ejecuta el servicio con el comando:
```
python app.py
```

Ahora tu aplicación debería estar funcionando dentro del entorno virtual


## Requisitos del trabajo

En este proyecto tienes libertad para elegir el contenido de tu aplicación web, pero debes cumplir con algunos requisitos
técnicos básicos. La idea es que organices bien tu código y trabajes con herramientas que te ayudarán a desarrollar una
aplicación funcional.

Asegurate de:
* ✅ Separar la presentación (interfaz) de la lógica de negocio.
* ✅ Guardar los datos de forma permanente en una base de datos.

Herramientas:
* 🔹 Python y [FastAPI](https://fastapi.tiangolo.com/) para la lógica de negocio.
* 🔹 HTML, CSS y JavaScript para la interfaz de usuario.
* 🔹 [sqlite3](https://docs.python.org/3/library/sqlite3.html) de Python para manejar la base de datos.


Recuerda que, además de cumplir con los requisitos técnicos, es importante seguir buenas prácticas de programación. Esto significa escribir código limpio, organizado y fácil de entender, usando nombres claros para las variables y evitando repetir el mismo código. También debes manejar los errores de manera adecuada y seguir las recomendaciones de estilo de Python y JavaScript. Si necesitas más información sobre cómo hacerlo, puedes consultar estos enlaces útiles:

* [PEP 8 (estilo en Python)](http://peps.python.org/pep-0008/)
* [Guía de JavaScript](https://developer.mozilla.org/es/docs/Web/JavaScript/Guide/Introduction)


## Documenta el proyecto

Para que tu proyecto sea más fácil de entender, es importante que lo documentes bien. Dentro del repositorio ya tienes una
carpeta llamada "doc", donde debes crear un archivo en Markdown (.md) explicando de qué trata tu aplicación, cómo está organizada
y cómo se puede ejecutar. Piensa en esto como una pequeña guía para ti y para cualquiera que quiera usar o mejorar tu proyecto
en el futuro.

Aquí tienes algunos enlaces para escribir una documentación original y atractiva:
* [Escribir en Github](https://docs.github.com/es/get-started/writing-on-github)
* [Guía profesional sobre README](https://coding-boot-camp.github.io/full-stack/es/github/professional-readme-guide)

> [!CAUTION]
> Este fichero README.md debe ser sustituido por un fichero README que describa el proyecto.
