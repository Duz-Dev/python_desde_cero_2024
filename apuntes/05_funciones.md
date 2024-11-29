# Funciones

![alt text](./img/image6.png)

> *Repositorio*: [python_desde_cero_2024](https://github.com/Duz-Dev/python_desde_cero_2024) - fecha de edición: 16/11/2024

## Introducción

Imagina que estás desarrollando un sistema para una tienda que calcula el precio total de una compra. Cada cliente tiene diferentes productos y cantidades. Podrías escribir el mismo cálculo una y otra vez, pero esto haría que el código fuera repetitivo, difícil de leer y propenso a errores. Aquí es donde las funciones se vuelven indispensables: nos permiten encapsular lógica reutilizable en una sola parte del programa.

Por ejemplo, queremos calcular el precio total de tres compras diferentes. Sin funciones, tendríamos que escribir esto de manera repetitiva:  

```python
precio1 = 10 * 2  # Producto 1
precio2 = 5 * 3   # Producto 2
precio3 = 20 * 1  # Producto 3
total = precio1 + precio2 + precio3
```

Ahora bien, con una función podemos resolver este problema de forma más clara y eficiente.

En su forma más básica, **una función es un bloque de código que realiza una tarea específica y se puede reutilizar tantas veces como necesites.** Python implementa las funciones de manera sencilla, utilizando la palabra clave `def` para definirías. Cuando llamas a una función, el programa ejecuta el código dentro de ella y te da un resultado (si la función lo tiene).  

**Sintaxis básica de una función:**

```python
def nombre_de_funcion(parametros_opcionales):
    # Código dentro de la función
    return resultado_opcional
```

**Ejemplo básico 1. Mensaje de bienvenida:**

```python
def saludo(nombre):
    print(f"¡Hola, {nombre}! Bienvenido a nuestra tienda.")

saludo("Juan")  # Salida: ¡Hola, Juan! Bienvenido a nuestra tienda.
```

Una analogia que tal vez te sea mas util es imaginar que las funciones no son mas que maquinas. Estas maquinas tienen forma de caja y lo que hacemos con ellas es ingresar un dato, digamos una letra como la 'x' y lo que esperamos cuando ingresamos este dato a la maquina es otro valor, 'y'

![alt text](./img/image6_01.png)

Como puedes intuir en los ejemplos. Primeramente creamos una función con la palabra reservada `def` y seguida de esta escribimos el nombre de nuestra función y adjuntamos paréntesis. Dentro de estos podemos añadir parámetros, que no son mas que variables que podemos utilizar solo y exclusivamente dentro de nuestra función. Estas tomaran el valor que les demos, ya sea que les indiquemos unos por defecto u el el programador le pase dichos valores cuando se mande a llamar a la función.

Con llamar a la función nos referimos a que en un inicio las funciones no se ejecutara, a no ser que el programador explícitamente escriba el nombre de dicha función después de crearla y le adjunte un par de paréntesis. Ejemplo de esto:

**Ejemplo básico 2. Sumar dos números:**

```python
def sumar(a, b):
    return a + b

resultado = sumar(4, 5)
print("El resultado es:", resultado)  # Salida: El resultado es: 9
```

Ahora con esto, pasemos a ver con mayor detalle los siguientes temas.

## Parámetros y valores  

Los **parámetros** son variables que pasamos a una función para personalizar su comportamiento. Existen diferentes formas de utilizarlos en Python:

### 1. **Valores predeterminados**  

Podemos asignar un valor por defecto a los parámetros, para que la función lo use si no proporcionamos uno al llamarla. Esto es muy util si es que esperamos que los parametros si o si tengan un valor por defecto y asi evitar posibles errores.

```python
def saludo(nombre="Cliente"):
    print(f"Hola, {nombre}")

saludo()  # Salida: Hola, Cliente
saludo("Ana")  # Salida: Hola, Ana
```

### 2. **`*args` (argumentos variables)**  

`*args` permite pasar un número indefinido de argumentos posicionales a una función. Util si no se tiene en mente, un numero finito de valores a utilizar.

```python
def sum(*args):
    value = 0
    for n in args:
        value += n
    return print(value)

sum()
sum(2, 3, 4)
sum(2, 3, 4, 6, 9, 21)

# Salida:
# 0
# 9
# 45
```

Pero también podemos invocar una función resultante  con un único parámetro de tipo iterable, como una tupla o una lista, del siguiente modo (*args):

```python
def resultado(x, y, op):
    if op == '+':
        return x + y
    elif op == '-':
        return x – y

a = (1, 2, '+')
resultado(*a)
# salida: 3

#O incluso así:

a = (2, '-')
resultado(3, *a)
# salida: 3

```

### 3. **`**kwargs` (argumentos nombrados variables)**  

`**kwargs` permite pasar un número indefinido de argumentos con nombre (clave-valor) a una función. Similar al anterior, pero con mayor utilidad para diccionarios

```python
def mostrar_info(**datos):
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre="Ana", edad=25, ciudad="Monterrey")
# Salida:
# nombre: Ana
# edad: 25
# ciudad: Monterrey
```

Un ejemplo de cada uno de ellos es la función mas elemental que hemos utilizado desde el principio, la función [**print**](./01-1-funcion%20_print.md). *Visita dicho tema para mas referencia*

Ahora, antes de dar entrada a mas utilidades de las funciones, quiero hacer énfasis en dos temas, los docstrings y los type hints.

## Docstrings

Un *docstring* es una cadena de texto que se utiliza para documentar funciones, métodos, clases o módulos. Aparece inmediatamente después de la declaración de una función (o clase) y sirve para describir qué hace la función, los parámetros que recibe y qué devuelve.
Esta ya la llegamos a nombrar en su momento en el bloque 1 de esta recopilación de guia de python, [clic aqui](./01_introduccion.md/#8-docstrings).

### ¿Por qué son útiles?

1. **Claridad del propósito del código:** Facilita a otros (o a ti mismo) entender qué hace una función sin necesidad de analizar toda su implementación.

2. **Compatibilidad con herramientas:** Herramientas como `help()` o generadores de documentación pueden extraer y mostrar docstrings automáticamente.

3. **Estandarización:** Promueven la escritura de documentación consistente dentro de un equipo.

**Ejemplo 1. Docstring básico:**

```python
def sumar(a, b):
    """
    Suma dos números.

    Parámetros:
        a (int o float): El primer número.
        b (int o float): El segundo número.
    
    Retorna:
        int o float: La suma de a y b.
    """
    return a + b

# Llamada
help(sumar)
```

Precisamente, si ejecutamos esta ultima función seria vista como un mensaje en la terminal.

![alt text](./img/image6_02.png)

Como dato adicional, herramientas como visual studio code también hace uso de estos comentarios para que de manera mas cómoda puedas ver una previsualización de la funcionalidad de dichas funciones, e incluso respeta las normas de markdown, por lo que podrías añadir títulos y énfasis en palabras en negritas. Ejemplo, si pasamos el cursos por en sima de la función help(sumar), veremos algo tal asi:

![alt text](./img/image6_03.png)

**Ejemplo 2. Docstring en funciones más complejas:**

```python
def filtrar_pares(numeros):
    """
    Filtra los números pares de una lista.

    Parámetros:
        numeros (list[int]): Lista de números enteros.

    Retorna:
        list[int]: Una lista con los números pares.
    """
    return [n for n in numeros if n % 2 == 0]

# Llamada
help(filtrar_pares)
# Salida:
# Filtra los números pares de una lista.
#
# Parámetros:
#    numeros (list[int]): Lista de números enteros.
#
# Retorna:
#    list[int]: Una lista con los números pares.
```

Encontraras con el tiempo que muchas librerías para llevar una mejor compresión de su código usan estos constantemente, por lo que no dudes en utilizarlo tu también a partir de ahora.

## Type Hints

Los *type hints* (o anotaciones de tipo) son una característica introducida en Python 3.5 que permite especificar los tipos de datos de los parámetros y del valor de retorno en una función. Esto mejora la legibilidad del código y ayuda a herramientas como **linters** (e.g., MyPy) a detectar errores antes de ejecutar el código. En palabras simples, son comentarios mas cortos que los que ya vimos, que solo ayudan aportar contexto al programador. No esta incorporando una especie de tipado fuerte en python si lo que solamente ayuda a orientar en base que tipo de dato se intenta trabajar.

Debido a que python es un lenguaje de tipado dinámico, es util, al punto que lenguajes de la misma índole también adoptaron esto mismo.

### Utilidad

1. **Prevención de errores:** Ayudan a evitar errores de tipo al escribir o modificar el código.
2. **Documentación implícita:** Sirven como una forma de documentación para los desarrolladores, indicando qué tipo de datos esperan las funciones.
3. **Soporte avanzado con módulos:** La biblioteca estándar incluye el módulo `typing` para definir tipos avanzados como `Union`, `List`, `Optional`, etc.

Con esto mencionado, veamos como se emplean.

**Ejemplo 1. Type hints básicos:**

```python
def dividir(a: float, b: float):
    """
    Divide dos números.

    Retorna:
        float: Resultado de la división.
    """
    return a / b

# Llamada
print(dividir(10.0, 2.0))  # Salida: 5.0
```

Si analizamos, vemos que ahora los paramentros 'a' y 'b' no solo estan asignados en la funcón `dividir()` si no que tambien tienen dos puntos adjuntos y seguido de esto la palabra float. Esto ultimo es la sintaxis para añadir las anotaciones de tipo. En este caso se coloco la palabra float, porque es el tipo de dato que se espera que sea a y b. Pero cabe aclarar que aunque se espera un dato flotante, aun asi puedes manipularlo como el dato que deses, no estas estrictamente obligado a usar flotantes.

Esto puede ser algo innecesario si lo ves asi en primer logar, pero en realidad es muy util ya que no solo te ayuda a limitar a el programador a entender que datos se deben ingresar y manipular, si no que para librerías mas avanzadas que inventan sus nuevos tipos de datos, mas allá de lo que python aporta, te ayuda a ver que funcionalidad u operaciones puedes realizar.
Esto igualmente le tomaras mas importancia y daras gracia de su utilidad cuando pasemos a librerias como el uso de Discord.py y Flask.

Ahora mira este ejemplo:

```python
def saludar(nombre: str) -> str:
    """
    Genera un saludo personalizado.

    Retorna:
        str: Mensaje de saludo.
    """
    return f"Hola, {nombre}!"

# Llamada
print(saludar("Pablo"))  # Salida: Hola, Pablo!
```

Aquí hay un pequeño añadido, y es que al colocar `(nombre: str)` este le adjuntamos una anotacion `-> str`. Este ultimo indica que se espera que la función debe retornar un dato de tipo str, pero como ya aclare, este solo es un comentario, técnicamente si puedes devolver cualquier dato aunque no sea un str, solo que se espera que tu respetes dicho tipo.

**Ejemplo 2. Precio de un producto:**

Este es otro ejemplo de usando el type hints con todo lo que sabemos hasta el momento.

```python
def calcular_precio(base: float, impuesto: float = 0.16, descuento: float = 0.0) -> float:
    """
    ## calcular_precio
    > Calcula el precio final de un producto considerando el impuesto y un descuento opcional.

    **Parámetros:**
        base (float): Precio base del producto.
        impuesto (float): Porcentaje de impuesto a aplicar (por defecto 16%).
        descuento (float): Porcentaje de descuento a aplicar (por defecto 0%).

    **Retorna:**
        float: Precio final tras aplicar impuesto y descuento.
    """
    precio_con_impuesto = base + (base * impuesto)
    precio_final = precio_con_impuesto - (precio_con_impuesto * descuento)
    return precio_final

# Llamadas a la función
print(calcular_precio(100))  # Precio base de 100 con impuesto del 16%, sin descuento. Salida: 116.0
print(calcular_precio(100, descuento=0.10))  # Precio base de 100 con impuesto del 16% y descuento del 10%. Salida: 104.4
print(calcular_precio(100, 0.08, 0.05))  # Precio base de 100 con impuesto del 8% y descuento del 5%. Salida: 102.6

```

Como vemos, editores de código como visual studio code utiliza estas herramientas para dar contexto de las utilidades de nuestras funciones con mayor comodidad.

![alt text](./img/image6_04.png)

### Modulo Typing

Hasta el momento hemos utilizado un par de módulos para el manejo de números a una mayor precisión, pero los módulos no solo existen para ello, si no para demasiadas utilidades. Hay módulos que como este que vamos a ver, nos ayuda a extender las funcionalidades de el type hints.

El módulo `typing` en Python se introdujo en la versión 3.5 para proporcionar soporte avanzado a las *type hints*. Este módulo permite anotar los tipos de datos en funciones, clases y otros componentes del código, mejorando la claridad, la mantenibilidad y la capacidad de detectar errores antes de la ejecución (por ejemplo, usando herramientas como `mypy`).

**Características principales del módulo `typing`:**

1. **Compatibilidad con estructuras de datos complejas:**
   - Puedes especificar tipos para listas, diccionarios, tuplas, conjuntos, etc.
   - Ejemplo: `List[int]`, `Dict[str, float]`, `Tuple[int, str]`.

2. **Soporte para tipos opcionales y combinados:**
   - Permite manejar valores que pueden ser de múltiples tipos o incluso nulos.
   - Ejemplo: `Union[int, str]`, `Optional[str]`.

3. **Definición de funciones más precisas:**
   - Puedes usar tipos para funciones que retornan otras funciones, clases, o cualquier objeto.
   - Ejemplo: `Callable[[int, int], int]`.

4. **Documentación del código:**
   - Los *type hints* mejoran la comprensión del propósito de las funciones, parámetros y variables.

#### **Conceptos clave

1. **Tipos genéricos básicos:**
   - `List`, `Dict`, `Tuple`, `Set` son genéricos para anotar colecciones.
   - Ejemplo:

     ```python
     from typing import List

     def sumar_valores(valores: List[int]) -> int:
         return sum(valores)
     ```

2. **`Union`:**
   - Permite especificar que un valor puede ser de más de un tipo.
   - Ejemplo:

     ```python
     from typing import Union

     def procesar_dato(dato: Union[int, str]) -> str:
         return str(dato)
     ```

3. **`Optional`:**
   - Es equivalente a `Union[T, None]`, indicando que un valor puede ser nulo.
   - Ejemplo:

     ```python
     from typing import Optional

     def obtener_nombre(id: int) -> Optional[str]:
         return "Nombre" if id == 1 else None
     ```

4. **`Callable`:**
   - Anota funciones como argumentos o valores retornados.
   - Ejemplo:

     ```python
     from typing import Callable

     def ejecutar(func: Callable[[int, int], int], a: int, b: int) -> int:
         return func(a, b)
     ```

5. **Alias de tipos personalizados:**
   - Permiten dar nombres a tipos complejos para simplificar el código.
   - Ejemplo:

     ```python
     from typing import List, Dict

     Registro = Dict[str, List[int]]

     def agregar_registro(registros: Registro, nombre: str, valores: List[int]) -> None:
         registros[nombre] = valores
     ```

6. **Clases genéricas personalizadas:**
   - Puedes usar `TypeVar` para crear clases genéricas.
   - Ejemplo:

     ```python
     from typing import TypeVar, Generic

     T = TypeVar('T')

     class Caja(Generic[T]):
         def __init__(self, contenido: T):
             self.contenido = contenido
     ```

Ahora que conocemos estos detalles del lenguaje python, continuemos con la explicación de las funciones.

## devoluciones múltiples

Imagina que estás desarrollando un programa para calcular información estadística básica de un conjunto de números. Necesitas una función que, al proporcionarle una lista, devuelva tres datos: el promedio, el número máximo y el número mínimo. En lugar de crear varias funciones para cada cálculo, puedes usar una sola función en Python que devuelva todos estos valores.

En Python, una función puede devolver múltiples valores empaquetándose en una tupla. Esto es muy útil cuando necesitas resultados relacionados entre sí. Los valores devueltos se pueden desempaquetar en variables individuales al momento de llamar la función. A continuación planteare 2 escenarios donde esto puede ser util.

### Ejemplo Practico 1. Calcular area y perimetro de un triangulo

Supongamos que queremos calcular el área y el perímetro de un rectángulo dadas su base y altura. Esto lo hacemos dentro de una función que devuelve ambos valores.

```python
def calcular_area_y_perimetro(base, altura):
    # Cálculos
    area = base * altura
    perimetro = 2 * (base + altura)
    # Aquí ocurre el empaquetamiento en una tupla
    return area, perimetro

# Llamada a la función
resultado = calcular_area_y_perimetro(5, 3)
print(resultado)  # Salida: (15, 16)

# Desempaquetando la tupla en variables individuales
area, perimetro = calcular_area_y_perimetro(5, 3)
print(f"Área: {area}")       # Salida: Área: 15
print(f"Perímetro: {perimetro}")  # Salida: Perímetro: 16
```

**Explicación:**

En la línea return area, perimetro, Python crea automáticamente una tupla con los valores area y perimetro. Esto ocurre sin necesidad de escribir explícitamente return (area, perimetro) porque el uso de la coma , ya indica el empaquetamiento.

Cuando llamamos a la función, podemos almacenar el resultado en una variable (en este caso, resultado), que será una tupla que contiene los valores devueltos.

Podemos extraer los valores individuales de la tupla usando el desempaquetamiento, como en la línea area, perimetro = calcular_area_y_perimetro(5, 3). Así asignamos cada valor de la tupla a una variable independiente.

### Ejemplo Practico 2. El anillo rojo de la muerte (Xbox 360)

El problema del "anillo rojo de la muerte" en las Xbox 360 fue causado por sobrecalentamiento y fallos en la placa base. Supongamos que tenemos una función que evalúa el estado de una consola basándose en su temperatura y el estado de su hardware, y devuelve si está en buen estado o no, junto con un mensaje de advertencia si es necesario.

```python
def diagnosticar_consola(temperatura, hardware_ok):
    if temperatura > 70:
        estado = "Defectuosa"
        mensaje = "Advertencia: Temperatura crítica. RIESGO DE FALLA."
    elif not hardware_ok:
        estado = "Defectuosa"
        mensaje = "Error: Problemas detectados en el hardware."
    else:
        estado = "Funcional"
        mensaje = "Todo está en orden."
    return estado, mensaje

# Llamada a la función
estado, mensaje = diagnosticar_consola(75, True)
print(estado)  # Salida: Defectuosa
print(mensaje) # Salida: Advertencia: Temperatura crítica. RIESGO DE FALLA.
```

### Ejemplo Practico 3. La era de los hackeos en PlayStation 2

Imagina que Sony está evaluando la vulnerabilidad de sus consolas frente a ataques de hackers. Crearemos una función que toma el número de intentos de hackeo y los sistemas afectados, y devuelve si la consola es vulnerable y un reporte con detalles.

```python
def evaluar_seguridad(intentos_hackeo, sistemas_afectados):
    if intentos_hackeo > 5 or len(sistemas_afectados) > 2:
        vulnerable = True
        reporte = f"Vulnerable: {intentos_hackeo} intentos detectados. Sistemas comprometidos: {', '.join(sistemas_afectados)}."
    else:
        vulnerable = False
        reporte = "Sistema seguro. No se detectaron vulnerabilidades críticas."
    return vulnerable, reporte

# Llamada a la función
vulnerable, reporte = evaluar_seguridad(6, ["Kernel", "Red"])
print(vulnerable)  # Salida: True
print(reporte)     # Salida: Vulnerable: 6 intentos detectados. Sistemas comprometidos: Kernel, Red.
```
