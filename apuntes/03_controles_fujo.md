# Controles de flujo

![img: Tipos de datos](https://i.postimg.cc/xd3ZLrLM/image.png)

> *Repositorio*: [python_desde_cero_2024](https://github.com/Duz-Dev/python_desde_cero_2024) - fecha de edición: 14/06/2024
---
<!-- TOC -->

- [Controles de flujo](#controles-de-flujo)
  - [Estructuras Condicionales](#estructuras-condicionales)
    - [Reglas y Consideraciones](#reglas-y-consideraciones)
    - [Ejemplos condicionales](#ejemplos-condicionales)
  - [Match](#match)
    - [Definición](#definición)
    - [Sintaxis](#sintaxis)
    - [Reglas y Consideraciones](#reglas-y-consideraciones-1)
    - [Ejemplos match](#ejemplos-match)
    - [Guards (protecciones)](#guards-protecciones)
      - [Funcionamiento de los Guards](#funcionamiento-de-los-guards)
      - [Ejemplos de Guard](#ejemplos-de-guard)

<!-- /TOC -->

## Estructuras Condicionales

Las estructuras de control condicionales son constructos en los lenguajes de programación que permiten ejecutar bloques de código diferentes dependiendo de ciertas condiciones.

Las condicionales en Python permiten ejecutar código basado en condiciones booleanas. Las tres principales estructuras condicionales son `if`, `elif` (else if) y `else`. A continuación, se detalla cómo funcionan cada una de ellas:

1. **if**: Evalúa una condición y, si es verdadera, ejecuta el bloque de código asociado.
2. **elif**: (abreviatura de "else if") Evalúa otra condición si las anteriores `if` o `elif` fueron falsas. Puede haber múltiples `elif`.
3. **else**: Se ejecuta si ninguna de las condiciones anteriores fue verdadera. Solo puede haber un `else` y debe ser el último bloque en la estructura condicional.

Ten en cuenta que cualquiera de estas estructuras que veremos, trabajan con el principio de indentación entre los bloques y expresiones.

Cuando creas un condicional o una estructura en python, le indicamos a este que el código que le sigue trabajara bajo el contexto del la estructura, en pocas palabras, este código se ejecutara, siempre y cuando dicha estructura sea activada.

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

### Ejemplos condicionales

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

En las condiciones podemos hacer uso de todos los operadores que conocemos, por ejemplo esta el operador de membresía, que si recuerdas, se utiliza para verifica si un valor está presente en una secuencia.

```python
fruta = "manzana"
if "n" in fruta:
    print("La letra 'n' está en 'manzana'")
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

### Reglas y Consideraciones

- **Patrones**: Los patrones pueden ser valores literales, variables, tuplas, listas, diccionarios, entre otros.
- **Guardias**: Se pueden usar guardias (`if`) para agregar condiciones adicionales a los patrones.
- **Wildcard**: El patrón `_` actúa como un comodín y coincide con cualquier valor, similar a `default` en un `switch`.

### Ejemplos match

Coincidencia con valores literales (string)

```python
color = 'verde'
mgs = "" #mensaje
match color:
    case 'rojo':
        msg = "Es el color rojo"
    case 'verde':
        msg = "Es el color verde"
    case 'azul':
        msg = "Es el color azul"
    case _:
        msg = "Color desconocido"

print(print(msg))  # Salida: Es el color verde
```

Coincidencia con tuplas

```python
# Definir el punto constante
punto = (3, 4)

# Usar la estructura match para evaluar el punto
match punto:
    case (0, 0):
        print("Es el origen")
    case (x, 0):
        print(f"En el eje X en {x}")
    case (0, y):
        print(f"En el eje Y en {y}")
    case (x, y):
        print(f"En el punto ({x}, {y})")
    case _:
        print("Punto desconocido")
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

Existen otras estructuras que como vez pueden elevar la complejidad del código, ya es a criterio de cada persona explorar las utilidades de match.

### Guards (protecciones)

Los guards son expresiones que se utilizan dentro de la estructura `match` en Python para añadir condiciones adicionales que deben cumplirse para que el bloque de código correspondiente se ejecute. Los guards se implementan con la palabra clave `if` seguida de una expresión booleana.

La principal utilidad de los guards es permitir que se verifiquen condiciones más complejas junto con la coincidencia de patrones. Esto hace que la estructura `match` sea más poderosa y flexible, permitiendo manejar casos específicos de manera más precisa.

Los guards solo se pueden utilizar dentro de bloques `case` en una estructura `match`. No se pueden usar fuera de este contexto.

La sintaxis básica de un guard es:

```python
case patrón if expresión_booleana:
    # código a ejecutar si el patrón y la expresión booleana coinciden
```

Digamos que queremos crear un menú en el cual se ingrese en base a ciertas condiciones.
Un ejemplo seria como este:

```python
def menu(opcion, edad):
    match opcion:
        case 1 if edad == 18:
            print("La persona puede conducir.")
        case 2 if edad < 18:
            print("Aún no tienes la edad para conducir.")
        case 3 | _:
            print("Datos no válidos")

# Solicitar la edad del usuario
edad = int(input("Ingrese su edad: "))

# Solicitar la opción del menú
opcion = int(input("Ingrese una opción del menú (1, 2, 3): "))

# Ejecutar el menú
menu(opcion, edad)

```

**Explicación**. Posiblemente esto te parezca algo confuso, deja te explico el proceso que sigue este código:

1. Función `menu` con parámetros `opcion` y `edad`:

    - La función menu toma dos argumentos que le proporcionemos, en este caso seran los inputs opcion y edad.

2. Uso de ``match`` y ``case`` con guard:

    - Primer case: ``case 1 if edad == 18``:
        - Este caso se activa si opcion es 1 y edad es igual a 18.
        - Imprime "La persona puede conducir."
    - Segundo case: ``case 2 if edad < 18``:
        - Este caso se activa si opcion es 2 y edad es menor que 18.
        - Imprime "Aún no tienes la edad para conducir."
    - Tercer case: case 3 | _:
        - Este caso se activa si opcion es 3 o cualquier otro valor (_ es el comodín).
        - Imprime "Datos no válidos."

**Importante aclaracion:**
El operador `|` y el operador `or` en Python tienen diferencias fundamentales en cuanto a su uso y comportamiento, por lo que no podemos utilizarlos de manera equivalente como en otros lenguajes.

En el contexto de `match` en Python, el operador `|` se utiliza para separar múltiples patrones en un mismo caso, actuando como una "OR" para patrones. No es lo mismo que el operador lógico `or`.

```python
def clasificar_opcion(opcion):
    match opcion:
        case 1 | 2 | 3:
            print("Opción válida")
        case _:
            print("Opción no válida")

clasificar_opcion(1)  # Opción válida
clasificar_opcion(4)  # Opción no válida
```

En este ejemplo, el operador `|` se usa para combinar los patrones `1`, `2` y `3`, indicando que cualquier valor que sea igual a `1`, `2` o `3` coincide con este caso.

1. **Contexto:**
   - `|`: Utilizado para operaciones bitwise o para combinar patrones en un `match`.
   - `or`: Utilizado en expresiones lógicas para evaluar condiciones booleanas.

2. **Funcionamiento:**
   - `|`: Opera a nivel de bits en números enteros o combina patrones en un `match`.
   - `or`: Evalúa expresiones booleanas y devuelve el primer valor que sea `True` o el último valor si ninguno es `True`.

#### Funcionamiento de los Guards

1. **Evaluación del Patrón**: Primero, se evalúa si el valor coincide con el patrón del `case`.
2. **Evaluación del Guard**: Si el patrón coincide, se evalúa la expresión booleana del guard.
3. **Ejecución del Código**: Si el guard se evalúa como `True`, se ejecuta el bloque de código correspondiente. Si se evalúa como `False`, se pasa al siguiente `case`.
4. **Excepciones**: Si el guard produce una excepción durante su evaluación, la excepción se propaga y no se selecciona el bloque `case`.

#### Ejemplos de Guard

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

En este ejemplo, `x` se convierte en una variable que toma el valor de ``numero`` en cada línea de coincidencia.

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

**Ejemplo 4**. Patrón de tamaño de texto

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
