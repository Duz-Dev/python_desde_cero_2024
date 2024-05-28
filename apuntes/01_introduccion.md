# Introducción a Python

![curso python](https://i.postimg.cc/XY4MTZxc/banner-py.png)

Antes de comenzar de lleno en este repositorio, es requisito que tengas a la mano las siguientes herramientas y conocimientos:

- ¿Qué es un lenguaje de programación?
- ¿Qué es Python?
- Interpretador vs compilador
- Editor de código
- ¿Qué es una terminal? (utilización básica)

También, en caso de que Python sea el primer lenguaje de programación con el cual tengas contacto, seria muy recomendable que primero abordes algunos conceptos y temas de "lógica de programación". Entender lo que son las variables, tipos de dato, condicionales, ciclos, ect. De lo contrario te sera mucho mas difícil comprender lo que empezaremos abordar de aquí en adelante.

## Origen de Python y su Propuesta

Python fue concebido en diciembre de 1989 por Guido van Rossum en el Centrum Wiskunde & Informatica (CWI) en los Países Bajos. Guido, quien había trabajado en el lenguaje ABC, quería crear un lenguaje que mantuviera la sencillez y el aprendizaje intuitivo de ABC pero con capacidades más avanzadas. La primera versión pública de Python (versión 0.9.0) se lanzó en febrero de 1991.

El lenguaje fue diseñado con la filosofía de enfatizar la legibilidad del código y permitir a los desarrolladores escribir código limpio y lógico para proyectos pequeños y grandes. Python adopta el principio de "menos es más", promoviendo una sintaxis y una estructura que hacen que el código sea fácil de leer y entender. Su sintaxis se asemeja al inglés, esto lo hace perfecto para los principiantes, pero también es muy poderoso para los desarrolladores experimentados.

### Características Clave de Python:

**Sintaxis Clara y Legible**: Python utiliza una sintaxis limpia y su estructura se basa en la indentación, lo cual fuerza a los desarrolladores a escribir código legible y organizado.

**Multiparadigma**: Soporta varios paradigmas de programación, incluyendo la programación orientada a objetos, la programación estructurada y la programación funcional.

**Bibliotecas Estándar Extensas**: Python viene con una gran biblioteca estándar que ofrece módulos y paquetes para realizar muchas tareas comunes como manipulación de archivos, operaciones matemáticas, y acceso a protocolos de internet.

### Comparación con Otros Lenguajes

**Java**: Java es robusto y ampliamente utilizado en grandes sistemas empresariales. Es más complicado de aprender que Python debido a su sintaxis más estricta.

**C++**: Es muy potente y rápido, ideal para aplicaciones de alto rendimiento como videojuegos. Sin embargo, es más complejo debido a la gestión manual de la memoria.

**JavaScript**: Es el rey del desarrollo web, especialmente en el frontend. Python, aunque también se puede usar para el desarrollo web (sobre todo backend), es más generalista.

## Python como lenguaje

Python como ya hice mención, es un lenguaje Interpretado. Con ello trae tanto ventajas como desventajas. La primera contra que se tiene al momento de utilizar lenguajes Interpretados es que son menos optimos en cuestion de eficiencia de procesos y tiempos a comparación de los compilados. Python solucióna gran parte de dicha desventaja con una propuesta interesante, imitando a un lenguaje ya conocido como lo es java utiliza la siguiente forma:

1. **Escritura del Código Fuente:**
   - Escribes tu código en un archivo con extensión `.py`. Este archivo contiene instrucciones en lenguaje Python, que es de alto nivel y fácil de leer para los humanos.

2. **Compilación a Bytecode:**
   - Cuando ejecutas tu archivo Python (por ejemplo, usando `python mi_programa.py`), el intérprete de Python primero compila el código fuente a una representación intermedia llamada bytecode. El bytecode es una forma optimizada y más eficiente del código que la computadora puede procesar más rápidamente.
   - Este bytecode es independiente de la plataforma y se almacena en archivos con extensión `.pyc` dentro de un directorio `__pycache__`.

3. **Ejecución del Bytecode en la Máquina Virtual de Python (PVM):**
   - La Python Virtual Machine (PVM) toma el bytecode y lo ejecuta. La PVM es un motor de ejecución que interpreta el bytecode y lo traduce a instrucciones específicas de la máquina en la que se está ejecutando.
   - La PVM maneja la gestión de la memoria, la ejecución de los bloques de código y otras tareas importantes para ejecutar tu programa.

**Diagrama del Proceso:**

```markdown
Código Fuente (mi_programa.py)
        ↓
Compilación a Bytecode
        ↓
Bytecode (archivos .pyc en __pycache__)
        ↓
Ejecución en la Máquina Virtual de Python (PVM)
```

### Ventajas del Proceso

- **Portabilidad:** El bytecode es independiente de la plataforma, lo que significa que puedes ejecutar el mismo bytecode en cualquier sistema operativo que tenga un intérprete de Python compatible.
- **Eficiencia:** Compilar a bytecode optimiza el código, permitiendo una ejecución más rápida en comparación con interpretar directamente el código fuente.
- **Facilidad de Uso:** Los desarrolladores no necesitan preocuparse por estos detalles; Python maneja automáticamente la compilación y ejecución del bytecode.

Visualmente se podria ver de la siguiente manera:

![representación del proceso de python](https://i.postimg.cc/ht6Gcw2S/image.png)


## Primeros pasos en python

Ya que sabemos lo que propone, algunas de las cosas que podemos hacer con python y la utilidad de este mismo, ahora veremos como empezar a utilizarlo.

Primeramente debemos tener una manera de poder ejecutar nuestros archivos de python. Para ello existen diferentes herramentas que nos permitiran hacer dicha tarea como las que se mencionan en el libro de [AprendePython](https://aprendepython.es/core/devenv/). En mi caso, utilizo y recomiendo descargar y empezar a utilizar python con ayuda del ejecutable que ofrece de manera oficial en https://www.python.org/

![alt](https://i.postimg.cc/zGRdPbMx/image.png)

Dependiendo del sistema operativo de nuestro computador, debemos escoger una de las opciones de la lista. En mi caso yo uso Windows, pero perfectamente podemos intalarlo en mac y linux

> nota: En linux ya viene instalado por defecto, pero es necesario verificar que tengamos la version mas reciente y el gestor de paquetes 'pip'

Si decides instarlo por este metodo, te guiare en caso de que seas usuario de windows.

1. Primero lo descargas desde el sitio que ya comente y le daras en el boton de 'downloads' y veras que te aparece la lista de la imagen anterior, le das clic al boton de python 3.12.X y la descarga empezara.

2. Ejecutas el archivo y te recomiendo activar las casillas: 'user admin privileges when installing py.exe' y 'add python.exe to path'. Con ambas opciones evitaremos un posible error de instalacion por culpa de permisos.
![alt](https://i.postimg.cc/15N5RSjf/image.png)

Si ya las marcaste, ahora procede a darle al boton de 'install now'.

3. La instalacion procedera a realizarse y solo quedara esperar. Cuando termine te quedara una ventana como la siguiente:
![alt](https://i.postimg.cc/FKhLJzMP/image.png)
Solo con darle a el boton de close, cerramos la instalación terminada.

Con dicha instalacion python nos incluye algunas cosas adicionales como el 'IDLE'para python, el cual nos dejara ejecutar y probar nuestros archivos de python en dado de caso de no tener otra herraminta para ello. Yo en lo personal no la utilizo, ya que ejecuto los archivos con ayuda de la terminal de windows 11, o en su defecto desde mi editor de codigo favorito [Visual Studio Code.](https://code.visualstudio.com/)

Te recomiendo encarecidamente que utilices VSCode y aprendas a utlizarlo. En mi canal de Youtube podras encontrar como instalar dicho programa y utilzarlo con Python.

Otra manera de ejecutar nuestros archivos de python, una vez que instalamos python es utlizando una terminal. En windows por predeterminado esta la CMD y PoweShell. En lo personal no utilizo ninguna y opte por trabajar en la terminal que ofrece git en windows, [git bash.](git-scm.com/downloads) La gran diferencia de esta a las otras que ofrece windows, es que podemos utlizar comandos como normalmente se implementarian en linux o mac.

Ya sea que utilices cualquiera de estas terminales en el caso de windows, el utilizar los comandos de python seran exactamente igual.

A modo de ejemplo: Escribe en la aplicacion de windows 'cmd' el texto `python --version` y después dale enter. Veras que te mostrara la version de python que tienes instalada en tu equipo.

Ejemplo en cmd

![alt](https://i.postimg.cc/1XrPkRzd/image.png)
Ejemplo en git bash

![alt](https://i.postimg.cc/J4Q4gxDh/image.png)

## Hola mundo en python

Ya para terminar, te dire como crear y ejecutar archivos de python. Personalmente recomiendo que para este paso si no tienes experiencia en VSCode, mires otras explicaciones aparte de la que te dare a continuación:

1. Si tienes visual studio code, abrelo. Debes crear un archivo nuevo, esto se puede lograr precionando la combinación de teclas `ctrl + n` y dicho archivo guardalo con la combinación `ctrl + s`. Se te desplegara la ventana de gestor de archivos en windows y lo que te pedira es que le indiques donde deseas guardar el archivo, por ejemplo el Escritorio. Con ello debes darle un nombre a tu archivo, puede ser cualquiera pero solo recuerda que para especificar que nuestro archivo esta hecho para utilizar python le debemos escribir la extensión .py al final del nombre.
Algo asi se vera cuando guardes el archivo:
![alt](https://i.postimg.cc/v8SfS5jf/image.png)

2. Es posible que VScode reconozca que ahora estas utilizando python y te pida instalar algunas cosas, no te preocupes. Son extensiones que agregara a Visual Code para que utilizar python sea aun mas fácil.

3. Ahora en tu archivo de python, escribe dentro de este la expresión `print("Hola mundo")`. Esto con la finalidad de mostrar el texto hola mundo en la terminal que tenemos por defecto en nuestro equipo. usa `ctrl + s` para guardar los cambios. Tu VSCode se debe ver algo parecido a esto:
![image.png](https://i.postimg.cc/B6JZgw4s/image.png)

4. Ahora solo te faltara ejecutar dicho archivo. Para ello podemos darle al boton de arriba a la derecha (> es como una flecha) y esto ara que el código se ejecute en la terminal de nuestro ordenador pero dentro de VScode.
![alt](https://i.postimg.cc/MpZh92j9/image.png)
Si el 'hola mundo' sale en dicha terminal, significa que todo a funcionado correctamente.

Ahora empecemos con los demas temas que nos competen de python...

<span>repositorio: https://github.com/Duz-Dev/python_desde_cero_2024</span>