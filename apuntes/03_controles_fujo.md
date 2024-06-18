# Controles de flujo

![img: Tipos de datos](https://i.postimg.cc/xd3ZLrLM/image.png)

> *Repositorio*: [python_desde_cero_2024](https://github.com/Duz-Dev/python_desde_cero_2024) - fecha de edición: 14/06/2024
---
<!-- TOC -->

- [Controles de flujo](#controles-de-flujo)
    - [if](#if)
    - [if...else](#ifelse)
    - [if...elif...else](#ifelifelse)
    - [Reglas y Consideraciones](#reglas-y-consideraciones)
    - [Ejemplos](#ejemplos)
  - [Match](#match)
    - [Definición](#definición)
    - [Sintaxis](#sintaxis)
    - [Ejemplos](#ejemplos-1)
    - [Reglas y Consideraciones](#reglas-y-consideraciones-1)
    - [Guards (protecciones)](#guards-protecciones)
      - [Ejemplos](#ejemplos-2)
      - [Funcionamiento de los Guards](#funcionamiento-de-los-guards)
    - [Sintaxis](#sintaxis-1)
    - [Ejemplo Explicado](#ejemplo-explicado)
    - [Ejemplo Básico Adicional](#ejemplo-básico-adicional)

<!-- /TOC -->o Básico Adicional](#ejemplo-básico-adicional)

<!-- /TOC -->
Las estructuras de control condicionales son constructos en los lenguajes de programación que permiten ejecutar bloques de código diferentes dependiendo de ciertas condiciones.

Las condicionales en Python permiten ejecutar código basado en condiciones booleanas. Las tres principales estructuras condicionales son `if`, `elif` (else if) y `else`. A continuación, se detalla cómo funcionan cada una de ellas:

1. **if**: Evalúa una condición y, si es verdadera, ejecuta el bloque de código asociado.
2. **elif**: (abreviatura de "else if") Evalúa otra condición si las anteriores `if` o `elif` fueron falsas. Puede haber múltiples `elif`.
3. **else**: Se ejecuta si ninguna de las condiciones anteriores fue verdadera. Solo puede haber un `else` y debe ser el último bloque en la estructura condicional.

Ten en cuenta que cualquiera de estas estructuras que veremos, trabajan con el principio de indentación entre los bloques y expresiones.

Cuando creas un condicional o una estructura en python, le indicamos a este que el código que le sigue trabajara bajo el contexto del la estructura, en pocas palabras, este código se ejecutara, siempre y cuando dicha estructura sea activada.

### if

La estructura `if` evalúa una condición. Si la condición es verdadera (True), se ejecuta el bloque de código siguiente.

```python
if condición:
    # código a ejecutar si la condición es verdadera
```

le indicamos a python que el código que queremos que se ejecute si el la condición se cumple indentando el código como en tal ejemplo.
Los *PEP* aconsejan que debe ser una separación de la indentación de ser de  cuatro espacios vacíos, pero con darle uno en realidad es suficiente.

Ejemplo:

```python
edad = 18
if edad >= 18:
    print("Eres mayor de edad")
```

### if...else

El uso de `if` junto con `else` permite ejecutar un bloque de código alternativo si la condición es falsa (False).

```python
if condición:
    # código a ejecutar si la condición es verdadera
else:
    # código a ejecutar si la condición es falsa
```

Ejemplo:

```python
edad = 16
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
```

### if...elif...else

La estructura `if...elif...else` permite evaluar múltiples condiciones en secuencia. La primera condición verdadera ejecutará su bloque de código, y las condiciones posteriores serán ignoradas.

```python
if condición1:
    # código a ejecutar si condición1 es verdadera
elif condición2:
    # código a ejecutar si condición1 es falsa y condición2 es verdadera
else:
    # código a ejecutar si ninguna de las condiciones anteriores es verdadera
```

Ejemplo:

```python
nota = 75
if nota >= 90:
    print("Excelente")
elif nota >= 75:
    print("Bueno")
else:
    print("Necesita mejorar")
```

### Reglas y Consideraciones

- **Indentación**: Python usa la indentación para definir bloques de código. Todos los bloques de código dentro de un `if`, `elif`, o `else` deben estar correctamente indentados.
- **Condiciones**: Las condiciones dentro de `if`, `elif`, y `else` deben ser expresiones booleanas o evaluables a booleanos.
- **Else**: El bloque `else` es opcional y solo puede haber uno por estructura condicional.
- **Elif**: Puedes tener múltiples `elif` en una estructura condicional para manejar varias condiciones.

### Ejemplos

Podemos expresar múltiples expresiones a la vez.

```python
x = 5
y = 10

if (x < 10) and ( y > 5):
    print("Ambas condiciones son verdaderas")
```

Es valido anidar las estructuras de control. En este ejemplo mira que sucede si anidamos el condicional if.

```python
x = 10

if x > 0:
    if x % 2 == 0:
        print("x es un número positivo y par")
    else:
        print("x es un número positivo e impar")
else:
    print("x es un número negativo")
```

## Match

La estructura condicional `match` es una característica introducida en Python 3.10 que proporciona una forma poderosa y flexible de hacer coincidencias (matching) con patrones en lugar de solo valores simples. Esta estructura es similar a las expresiones de coincidencia de patrones (pattern matching) que se encuentran en otros lenguajes de programación como Swift y Rust.

### Definición

La estructura `match` permite comparar un valor contra varios patrones, ejecutando el bloque de código asociado con el primer patrón coincidente. Dichos patrones pueden ser de cualquier tipo de dato como strings, variables, tuplas, listas, diccionarios e incluso estructuras de datos más complejas. La sintaxis básica de `match` se asemeja a la de `switch` en otros lenguajes, pero con capacidades de coincidencia de patrones mucho más avanzadas.

### Sintaxis

```python
match valor:
    case patrón1:
        # código a ejecutar si valor coincide con patrón1
    case patrón2:
        # código a ejecutar si valor coincide con patrón2
    case _:
        # código a ejecutar si valor no coincide con ningún patrón anterior (similar a default en switch)
```

>[!NOTE]
> el `_` se utiliza en varios contextos, la intención detrás de su uso es siempre la misma: ignorar valores que no son necesarios. En el caso del match, se utiliza como un comodín para coincidir con cualquier valor no especificado por otros patrones. Este amiguito no lo vamos a topar en muchos otros escenarios.

### Ejemplos

Coincidencia con valores literales (string)

```python
def identificar_color(color):
    match color:
        case 'rojo':
            return "Es el color rojo"
        case 'verde':
            return "Es el color verde"
        case 'azul':
            return "Es el color azul"
        case _:
            return "Color desconocido"

print(identificar_color('rojo'))  # Salida: Es el color rojo
print(identificar_color('amarillo'))  # Salida: Color desconocido
```

Coincidencia con tuplas

```python
def manejar_punto(punto):
    match punto:
        case (0, 0):
            return "Es el origen"
        case (x, 0):
            return f"En el eje X en {x}"
        case (0, y):
            return f"En el eje Y en {y}"
        case (x, y):
            return f"En el punto ({x}, {y})"
        case _:
            return "Punto desconocido"

print(manejar_punto((0, 0)))  # Salida: Es el origen
print(manejar_punto((3, 0)))  # Salida: En el eje X en 3
print(manejar_punto((0, 4)))  # Salida: En el eje Y en 4
print(manejar_punto((3, 4)))  # Salida: En el punto (3, 4)
```

Coincidencia con listas

```python
def procesar_lista(lista):
    match lista:
        case []:
            return "Lista vacía"
        case [x]:
            return f"Lista con un solo elemento: {x}"
        case [x, y]:
            return f"Lista con dos elementos: {x} y {y}"
        case _:
            return "Lista con más de dos elementos"

print(procesar_lista([]))  # Salida: Lista vacía
print(procesar_lista([42]))  # Salida: Lista con un solo elemento: 42
print(procesar_lista([1, 2]))  # Salida: Lista con dos elementos: 1 y 2
print(procesar_lista([1, 2, 3]))  # Salida: Lista con más de dos elementos
```

### Reglas y Consideraciones

- **Patrones**: Los patrones pueden ser valores literales, variables, tuplas, listas, diccionarios, entre otros.
- **Guardias**: Se pueden usar guardias (`if`) para agregar condiciones adicionales a los patrones.
- **Wildcard**: El patrón `_` actúa como un comodín y coincide con cualquier valor, similar a `default` en un `switch`.

### Guards (protecciones)

Los guards son expresiones que se utilizan dentro de la estructura `match` en Python para añadir condiciones adicionales que deben cumplirse para que el bloque de código correspondiente se ejecute. Los guards se implementan con la palabra clave `if` seguida de una expresión booleana.

La principal utilidad de los guards es permitir que se verifiquen condiciones más complejas junto con la coincidencia de patrones. Esto hace que la estructura `match` sea más poderosa y flexible, permitiendo manejar casos específicos de manera más precisa.

Los guards solo se pueden utilizar dentro de bloques `case` en una estructura `match`. No se pueden usar fuera de este contexto.

La sintaxis básica de un guard es:

```python
case patrón if expresión_booleana:
    # código a ejecutar si el patrón y la expresión booleana coinciden
```

#### Ejemplos

Veamos un ejemplo muy sencillo para comprender mejor su uso:

**Ejemplo 1**. Clasificar numero

```python
def clasificar_numero(numero):
    match numero:
        case x if x < 0:
            return "Número negativo"
        case x if x == 0:
            return "Cero"
        case x if x > 0:
            return "Número positivo"
        case _:
            return "Valor desconocido"

print(clasificar_numero(-5))  # Salida: Número negativo
print(clasificar_numero(0))   # Salida: Cero
print(clasificar_numero(10))  # Salida: Número positivo
print(clasificar_numero(None))  # Salida: Valor desconocido
```

En este ejemplo:

- `case x if x < 0:` coincide si `numero` es menor que 0.
- `case x if x == 0:` coincide si `numero` es igual a 0.
- `case x if x > 0:` coincide si `numero` es mayor que 0.
- `case _:` coincide con cualquier otro valor.

**Ejemplo 2**. Mayoría de edad

```python
def clasificar_edad(edad):
    match edad:
        case x if x < 18:
            return "Menor de edad"
        case x if x >= 18 and x < 65:
            return "Adulto"
        case x if x >= 65:
            return "Adulto mayor"
        case _:
            return "Edad desconocida"

print(clasificar_edad(10))   # Salida: Menor de edad
print(clasificar_edad(30))   # Salida: Adulto
print(clasificar_edad(70))   # Salida: Adulto mayor
print(clasificar_edad(None)) # Salida: Edad desconocida
```

**Ejemplo 3**. Nota estudiante

```python
def clasificar_nota(nota):
    match nota:
        case x if x >= 90:
            return "Excelente"
        case x if x >= 70:
            return "Bueno"
        case x if x >= 50:
            return "Aprobado"
        case x if x < 50:
            return "Reprobado"
        case _:
            return "Nota desconocida"

print(clasificar_nota(95))  # Salida: Excelente
print(clasificar_nota(75))  # Salida: Bueno
print(clasificar_nota(55))  # Salida: Aprobado
print(clasificar_nota(45))  # Salida: Reprobado
print(clasificar_nota(None))  # Salida: Nota desconocida
```

#### Funcionamiento de los Guards

1. **Evaluación del Patrón**: Primero, se evalúa si el valor coincide con el patrón del `case`.
2. **Evaluación del Guard**: Si el patrón coincide, se evalúa la expresión booleana del guard.
3. **Ejecución del Código**: Si el guard se evalúa como `True`, se ejecuta el bloque de código correspondiente. Si se evalúa como `False`, se pasa al siguiente `case`.
4. **Excepciones**: Si el guard produce una excepción durante su evaluación, la excepción se propaga y no se selecciona el bloque `case`.




Un guard es una expresión condicional que se usa junto con la coincidencia de patrones en la estructura `match`.
La sintaxis para un guard es `case patrón if expresión_booleana:`.
La idea es que primero se evalúa si el valor coincide con el patrón del `case`, y si es así, se evalúa la expresión booleana (guard). Si el guard evalúa a `True`, se ejecuta el bloque de código correspondiente; de lo contrario, se pasa al siguiente `case`.

Cuando usamos un patrón como `x` en el `match`, `x` se convierte en una variable de captura que toma el valor del objeto que estamos evaluando. Así, en el caso de `case x if x < 0:`, `x` toma el valor de `numero` y se evalúa la condición `x < 0`.

### Sintaxis

La sintaxis para un guard es la siguiente:
```python
case patrón if expresión_booleana:
    # código a ejecutar si el patrón y la expresión booleana coinciden
```

### Ejemplo Explicado

Tomemos el ejemplo anterior y expliquémoslo en detalle:

```python
def clasificar_numero(numero):
    match numero:
        case x if x < 0:
            return "Número negativo"
        case x if x == 0:
            return "Cero"
        case x if x > 0:
            return "Número positivo"
        case _:
            return "Valor desconocido"

print(clasificar_numero(-5))  # Salida: Número negativo
print(clasificar_numero(0))   # Salida: Cero
print(clasificar_numero(10))  # Salida: Número positivo
print(clasificar_numero(None))  # Salida: Valor desconocido
```

- `case x if x < 0:`:
  - `x` captura el valor de `numero`.
  - Si `x` es menor que 0, se devuelve "Número negativo".
- `case x if x == 0:`:
  - `x` captura el valor de `numero`.
  - Si `x` es igual a 0, se devuelve "Cero".
- `case x if x > 0:`:
  - `x` captura el valor de `numero`.
  - Si `x` es mayor que 0, se devuelve "Número positivo".
- `case _:`:
  - `_` es un patrón comodín que coincide con cualquier valor.
  - Si ningún otro caso coincide, se devuelve "Valor desconocido".

En resumen, `x` actúa como una variable que captura el valor de `numero`, y el guard (condición `if`) determina si se ejecuta el bloque de código correspondiente.

### Ejemplo Básico Adicional

Aquí tienes otro ejemplo para clarificar el uso de guards:

```python
def clasificar_texto(texto):
    match texto:
        case t if len(t) == 0:
            return "Texto vacío"
        case t if len(t) < 5:
            return "Texto corto"
        case t if len(t) >= 5:
            return "Texto largo"
        case _:
            return "Texto desconocido"

print(clasificar_texto(""))      # Salida: Texto vacío
print(clasificar_texto("hola"))  # Salida: Texto corto
print(clasificar_texto("Python"))  # Salida: Texto largo
```

En este ejemplo:

- `case t if len(t) == 0:`:
  - `t` captura el valor de `texto`.
  - Si la longitud de `t` es 0, se devuelve "Texto vacío".
- `case t if len(t) < 5:`:
  - `t` captura el valor de `texto`.
  - Si la longitud de `t` es menor que 5, se devuelve "Texto corto".
- `case t if len(t) >= 5:`:
  - `t` captura el valor de `texto`.
  - Si la longitud de `t` es 5 o mayor, se devuelve "Texto largo".
- `case _:`:
  - `_` es un patrón comodín que coincide con cualquier valor.
  - Si ningún otro caso coincide, se devuelve "Texto desconocido".
