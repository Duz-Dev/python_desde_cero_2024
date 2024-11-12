# Tipos de datos ll

![alt text](./img/lorem.png)

> *Repositorio*: [python_desde_cero_2024](https://github.com/Duz-Dev/python_desde_cero_2024) - fecha de edición: 30/07/2024

<!-- TOC -->

- [Tipos de datos ll](#tipos-de-datos-ll)
  - [Introducción](#introducción)
  - [Strings](#strings)
    - [Concatenación](#concatenación)
    - [Formateo de Texto](#formateo-de-texto)
    - [Métodos de Strings](#métodos-de-strings)
    - [Detalles y usos](#detalles-y-usos)
  - [Enteros (int) y Flotantes (float)](#enteros-int-y-flotantes-float)
    - [Métodos](#métodos)
    - [Detalles y usos](#detalles-y-usos-1)
    - [Funciones Matemáticas del Módulo `math`](#funciones-matemáticas-del-módulo-math)
    - [Redondeo de Valores](#redondeo-de-valores)
    - [Modulo decimal](#modulo-decimal)
      - [Redondeo Explícito](#redondeo-explícito)
      - [Ejemplo: Cálculo Financiero](#ejemplo-cálculo-financiero)
  - [Listas en Python](#listas-en-python)
    - [Creación y Acceso](#creación-y-acceso)
    - [Métodos](#métodos-1)
    - [Ejemplos](#ejemplos)
    - [Detalles y usos](#detalles-y-usos-2)

<!-- /TOC -->
> *Repositorio*: [python_desde_cero_2024](https://github.com/Duz-Dev/python_desde_cero_2024) - fecha de edición: 24/07/2024

## Introducción

Si recordamos lo de la parte numero uno sobre los tipos de datos, sabemos que en programación, un dato es cualquier información que puede ser procesada por un programa. En Python, existen varios tipos de datos básicos que se utilizan con frecuencia, tales como enteros, flotantes, cadenas de texto (strings), listas, tuplas y diccionarios. Cada uno de estos tipos de datos tiene sus propias características y usos específicos.

En Python, todo es un objeto. Esto significa que cada dato tiene asociado una serie de métodos que se pueden utilizar para manipular y operar sobre él. Esta característica es fundamental en Python, ya que permite un manejo más intuitivo y flexible de los datos.

A partir de a qui profundizaremos en cada uno de los tipos de datos que tenemos con mayor utilización en python, métodos, funciones, curiosidades, entre otras cosas, pero es necesario recordar y tener en mano las siguientes funciones: `type` , `isinstance` y `dir`.

La función `type` se utiliza para determinar el tipo de dato de un objeto. Por ejemplo:

```python
x = 10
print(type(x))  # <class 'int'>
```

Esta devuelve el mensaje "class" y el tipo porque todos los objetos son instancias de alguna clase en python. Esto puede ser muy confuso ya que aun no vemos el tema de clases y objetos, pero de antemano ten en cuenta que todas las clases son una plantilla y los objetos son como elementos que a base de una plantilla (clase) se crearon. Este procedimiento es llamado instancia, por ende, podemos comprobar si un objeto pertenece a una instancia, es decir, si se origino de una clase que pensamos, usando la siguiente función:

La función `isinstance` se utiliza para comprobar si un objeto es una instancia de una clase específica:

```python
x = 10
print(isinstance(x, int))  # True
print(isinstance(x, float))  # False
```

Todo objeto en python tiene métodos. Un método es básicamente una función encapsulada dentro de la clase. Esto es util porque puede ayudarnos a modificar el objeto. Gran parte de este apunte se basa en poder modificar los tipos de datos de python mas usado.
Si quisiéramos saber cuales métodos tiene alguna clase y por ende un objeto, podemos utilizar la función `dir`

La función `dir` se utiliza para listar todos los atributos y métodos disponibles de un objeto. Esto es útil para explorar qué operaciones se pueden realizar sobre un objeto específico.

```python
x = "hello"
print(dir(x))
```

Al ejecutar esto veremos todos los métodos del tipo de dato que le pasamos a la función. En este caso la variable `x` contiene texto y por ende es un string.

## Strings

Las cadenas de texto (strings) son uno de los tipos de datos más comunes y útiles en Python. Los strings se utilizan para almacenar y manipular texto. En Python, los strings son objetos inmutables, lo que significa que no pueden cambiar después de su creación.

### Concatenación

La concatenación es el proceso de unir dos o más strings en uno solo. Esto se puede hacer utilizando el operador `+`.

```python
str1 = "Hola"
str2 = "Mundo"
result = str1 + " " + str2
print(result)  # Hola Mundo
```

### Formateo de Texto

Python ofrece varias formas de formatear strings. Uno de los métodos más utilizados es el método `format`.

```python
nombre = "Juan"
edad = 25
mensaje = "Me llamo {} y tengo {} años.".format(nombre, edad)
print(mensaje)
```

Otra forma moderna de formateo es utilizando f-strings (a partir de Python 3.6).

```python
nombre = "Juan"
edad = 25
mensaje = f"Me llamo {nombre} y tengo {edad} años."
print(mensaje)
```

### Métodos de Strings

1. **`upper`**: Convierte todos los caracteres de la cadena a mayúsculas.

```python
s = "hola"
print(s.upper())  # HOLA
```

2. **`lower`**: Convierte todos los caracteres de la cadena a minúsculas.

```python
s = "HOLA"
print(s.lower())  # hola
```

3. **`capitalize`**: Convierte el primer carácter de la cadena a mayúscula y el resto a minúsculas.

```python
s = "hola mundo"
print(s.capitalize())  # Hola mundo
```

4. **`title`**: Convierte el primer carácter de cada palabra a mayúscula.

```python
s = "hola mundo"
print(s.title())  # Hola Mundo
```

5. **`strip`**: Elimina los espacios en blanco al principio y al final de la cadena.

```python
s = "  hola  "
print(s.strip())  # "hola"
```

6. **`replace`**: Reemplaza una subcadena por otra.

```python
s = "hola mundo"
print(s.replace("mundo", "Python"))  # hola Python
```

7. **`find`**: Devuelve el índice de la primera aparición de una subcadena. Si no se encuentra, devuelve -1.

```python
s = "hola mundo"
print(s.find("mundo"))  # 5
```

### Detalles y usos

- **inmutabilidad**: Los strings en Python son inmutables. Esto significa que cualquier operación que modifique un string crea una nueva cadena en lugar de modificar la original.
  
- **Iteración**: Los strings pueden ser iterados carácter por carácter usando un bucle `for`.

- **Extracción**: Se trata de sacar fuera de una cadena, una porción de la misma según su posición dentro de ella. Para lo cual es necesario indicar la posición a extraer.

```python
s = "Python"
print(s[0])  # P
print(s[1])  # y
print(s[-1])  # n
print(s[2:4]) #tho
```

- **Manipulación de input**: También es posible aplicar los cambios que vimos sobre los strings a funciones que devuelvan este valor. Un ejemplo claro de este es la función `input`. Este por defecto le pide un dato al usuario y en automático python lo toma como un str, y por ende podemos manipularlo como uno.

```python
#!Ejemplo 1
saludo = input("primera frase: ") + input("segunda frase:")
print(saludo)

#!Ejemplo 2
text_lower = input("intresa un mensaje: ").lower()
print(text_lower)
```

## Enteros (int) y Flotantes (float)

Un entero es un número sin decimales. Puede ser positivo, negativo o cero. Los enteros en Python tienen una precisión ilimitada, lo que significa que pueden ser tan grandes o pequeños como lo permita la memoria disponible.
Los enteros se utilizan en una amplia variedad de contextos, desde contar elementos en una lista hasta realizar operaciones matemáticas complejas.

```python
a = 5
b = 3
suma = a + b  # 8
resta = a - b  # 2
multiplicacion = a * b  # 15
division_entera = a // b  # 1
modulo = a % b  # 2
```

Un número de punto flotante es un número que contiene una parte decimal. Los `float` se utilizan para representar números no enteros, permitiendo una mayor precisión en los cálculos.

Para declarar un `float`, se incluye un punto decimal.

```python
x = 10.5
y = -3.14
z = 0.0
```

Los números de punto flotante son esenciales en aplicaciones científicas, financieras y de ingeniería donde se necesita precisión decimal.

```python
a = 5.5
b = 2.2
suma = a + b  # 7.7
resta = a - b  # 3.3
multiplicacion = a * b  # 12.1
division = a / b  # 2.5
```

### Métodos

Ambos tipos de datos numéricos (`int` y `float`) soportan una variedad de operaciones y funciones matemáticas que se pueden utilizar para manipular y operar con números.

1. **Conversión entre `int` y `float`**: Puedes convertir entre estos tipos de datos utilizando las funciones `int()` y `float()`.

```python
x = 10
y = 10.5
x_float = float(x)  # 10.0
y_int = int(y)  # 10
```

2. **Redondeo**: El método `round()` redondea un número de punto flotante a un número específico de decimales.

```python
a = 5.5678
print(round(a, 2))  # 5.57
```

3. **Valor absoluto**: La función `abs()` devuelve el valor absoluto de un número.

```python
a = -5
b = -3.14
print(abs(a))  # 5
print(abs(b))  # 3.14
```

4. **Potencia**: La función `pow()` o el operador `**` se utiliza para elevar un número a una potencia.

```python
a = 2
b = 3
print(pow(a, b))  # 8
print(a ** b)  # 8
```

### Detalles y usos

- **Precisión de `float`**: Los números de punto flotante pueden tener problemas de precisión debido a cómo se representan internamente en el hardware. Esto puede llevar a resultados inesperados en algunos cálculos.

```python
a = 0.1 + 0.2
print(a == 0.3)  # False
print(a)  # 0.30000000000000004
```

Descuida, este es un problema clásico y que sucede en casi todos los lenguajes de programación, y es inevitable. El tema es aun mas extenso de lo que crees porque involucra mucho el tema de como se gestionan los números en nuestros ordenadores. Te recomiendo visitar el siguiente [enlace](http://puntoflotante.org/).

- **Operaciones entre `int` y `float`**: Cuando se realizan operaciones entre estos dos tipos, el resultado será un `float`.

```python
a = 5
b = 2.0
c = a + b
print(type(c))  # <class 'float'>
```

### Funciones Matemáticas del Módulo `math`

Estaba dudando si hablar sobre esto aun sin tocar el tema de módulos en python, pero veo aun asi conveniente mostrarte que existen herramientas fuera de lo que ofrece inicialmente python que nos ayudan para resolver problemas, en este caso, problemas matemáticos.

El módulo `math` en Python proporciona una variedad de funciones matemáticas adicionales que pueden ser útiles al trabajar con números. Para trabajar con este o cualquier modulo usamos la palabra `import` y seguido de este el nombre de dicho modulo, en este caso se llama `math`. Este proporciona una variedad de funciones matemáticas adicionales que pueden ser útiles al trabajar con números.

```python
import math

# Raíz cuadrada
print(math.sqrt(16))  # 4.0

# Logaritmo natural
print(math.log(2.7183))  # 0.999896315728952

# Logaritmo base 10
print(math.log10(100))  # 2.0

# Valor del número pi
print(math.pi)  # 3.141592653589793

# Exponencial (e^x)
print(math.exp(2))  # 7.38905609893065
```

### Redondeo de Valores

- El método `round()` redondea un número de punto flotante a un número específico de decimales. Este es el método más directo para redondear números.

```python
a = 5.5678
print(round(a, 2))  # 5.57
```

- La función `format()` permite dar formato a los números de punto flotante, limitando la cantidad de decimales mostrados.

```python
a = 5.5678
print(format(a, '.2f'))  # 5.57
```

- Las f-strings en Python 3.6+ proporcionan una forma conveniente y legible de dar formato a los números.

```python
a = 5.5678
print(f"{a:.2f}")  # 5.57
```

- El método `str.format()` también permite formatear números de punto flotante de manera similar a las f-strings.

```python
a = 5.5678
print("{:.2f}".format(a))  # 5.57
```

- El módulo `math` también proporciona funciones para redondear hacia abajo (`math.floor()`) y hacia arriba (`math.ceil()`).

```python
import math

a = 5.5678
print(math.floor(a))  # 5
print(math.ceil(a))  # 6
```

- La función `divmod()` devuelve una tupla que contiene el cociente y el resto al dividir dos números.

```python
a = 10
b = 3
print(divmod(a, b))  # (3, 1)
```

- Redondeo a Dos Decimales

```python
a = 5.5678
print(round(a, 2))  # 5.57
print(f"{a:.2f}")  # 5.57
print("{:.2f}".format(a))  # 5.57
print(format(a, '.2f'))  # 5.57
```

### Modulo decimal

Para manejar decimales y no perder precisión en Python, especialmente en cálculos financieros o científicos, es importante seguir algunas mejores prácticas. Aquí te detallo algunas de las más importantes:

El módulo `decimal` en Python proporciona soporte para aritmética decimal de precisión fija. A diferencia del tipo `float`, que puede introducir errores de redondeo debido a su representación en punto flotante binario, el tipo `Decimal` permite un control preciso sobre el número de dígitos decimales.

```python
from decimal import Decimal, getcontext

# Establecer el contexto de precisión
getcontext().prec = 10

# Crear números decimales
a = Decimal('0.1')
b = Decimal('0.2')

# Realizar cálculos con alta precisión
c = a + b
print(c)  # 0.3
```

Los números de punto flotante (`float`) son adecuados para cálculos donde la precisión no es crítica, pero no son recomendables para cálculos financieros debido a su posible pérdida de precisión.
Utilizar el contexto de `decimal` para establecer la precisión necesaria para tus cálculos.

```python
from decimal import Decimal, getcontext

# Establecer precisión global
getcontext().prec = 10

# Ejemplo de cálculo preciso
result = Decimal('1.123456789') + Decimal('2.987654321')
print(result)  # 4.111111110
```

#### Redondeo Explícito

Cuando sea necesario redondear números, hazlo explícitamente usando los métodos disponibles en `Decimal`.

```python
from decimal import Decimal, ROUND_HALF_UP

# Redondear a dos decimales
number = Decimal('2.34567')
rounded_number = number.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
print(rounded_number)  # 2.35
```

Al mostrar números en tu aplicación, utiliza formateo de salida para asegurarte de que los números se muestren con la precisión adecuada.

```python
value = Decimal('123.456789')
print(f"{value:.2f}")  # 123.46
```

#### Ejemplo: Cálculo Financiero

Aquí tienes un ejemplo completo de cómo utilizar el módulo `decimal` para realizar cálculos financieros precisos:

```python
from decimal import Decimal, getcontext, ROUND_HALF_UP

# Establecer precisión global
getcontext().prec = 10

# Crear valores decimales
precio_producto = Decimal('19.99')
cantidad = Decimal('3')
descuento = Decimal('0.10')  # 10% de descuento

# Calcular el total sin descuento
total_sin_descuento = precio_producto * cantidad

# Calcular el total con descuento
total_descuento = total_sin_descuento * descuento
total_con_descuento = total_sin_descuento - total_descuento

# Redondear el resultado final
total_con_descuento = total_con_descuento.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

print(f"Total con descuento: {total_con_descuento}")  # Total con descuento: 53.97
```

En si, existen muchos mas módulos creados por terceros para el manejo de números, ya que este problema es inevitable en todos los lenguajes de programación debido a la naturaleza del punto decimal.

## Listas en Python

Las listas son uno de los tipos de datos más versátiles y utilizados en Python. Permiten almacenar colecciones ordenadas de elementos y ofrecen una gran variedad de métodos para manipular y acceder a sus elementos.

Una lista en Python es una colección ordenada y mutable de elementos, que pueden ser de diferentes tipos. Las listas se definen usando corchetes (`[]`) y los elementos se separan por comas.

```python
# Ejemplo de lista en Python
mi_lista = [1, 2, 3, 4, 5]
```

### Creación y Acceso

Las listas se pueden crear de diversas formas y permiten acceder a sus elementos mediante índices.

```python
# Crear una lista vacía
lista_vacia = []

# Crear una lista con elementos
frutas = ["manzana", "banana", "cereza"]

# Acceder a elementos de la lista
print(frutas[0])  # Output: manzana
print(frutas[1])  # Output: banana
```

### Métodos

Las listas en Python vienen con una serie de métodos incorporados que facilitan su manipulación:

- **append()**: Añade un elemento al final de la lista.
- **extend()**: Añade múltiples elementos al final de la lista.
- **insert()**: Inserta un elemento en una posición específica.
- **remove()**: Elimina la primera aparición de un elemento.
- **pop()**: Elimina y devuelve el último elemento (o un elemento específico).
- **clear()**: Elimina todos los elementos de la lista.
- **index()**: Devuelve el índice de la primera aparición de un elemento.
- **count()**: Cuenta cuántas veces aparece un elemento en la lista.
- **sort()**: Ordena la lista en orden ascendente.
- **reverse()**: Invierte el orden de los elementos en la lista.
- **copy()**: Devuelve una copia superficial de la lista.

### Ejemplos

```python
# Añadir elementos a la lista
frutas.append("naranja")
print(frutas)  # Output: ['manzana', 'banana', 'cereza', 'naranja']

# Extender la lista con múltiples elementos
frutas.extend(["kiwi", "mango"])
print(frutas)  # Output: ['manzana', 'banana', 'cereza', 'naranja', 'kiwi', 'mango']

# Insertar un elemento en una posición específica
frutas.insert(1, "fresa")
print(frutas)  # Output: ['manzana', 'fresa', 'banana', 'cereza', 'naranja', 'kiwi', 'mango']

# Eliminar un elemento de la lista
frutas.remove("cereza")
print(frutas)  # Output: ['manzana', 'fresa', 'banana', 'naranja', 'kiwi', 'mango']

# Eliminar y devolver el último elemento de la lista
ultimo = frutas.pop()
print(ultimo)  # Output: mango
print(frutas)  # Output: ['manzana', 'fresa', 'banana', 'naranja', 'kiwi']

# Ordenar la lista
frutas.sort()
print(frutas)  # Output: ['banana', 'fresa', 'kiwi', 'manzana', 'naranja']

# Invertir el orden de la lista
frutas.reverse()
print(frutas)  # Output: ['naranja', 'manzana', 'kiwi', 'fresa', 'banana']
```

### Detalles y usos

- **Mutabilidad**: Las listas son mutables, lo que significa que sus elementos pueden ser modificados después de su creación.
- **Tipos Mixtos**: Las listas pueden contener elementos de diferentes tipos, aunque generalmente se usa un solo tipo para mantener la coherencia.
- **Listas Anidadas**: Las listas pueden contener otras listas, lo que permite crear estructuras complejas.

```python
# Lista con elementos de diferentes tipos
mixta = [1, "hola", 3.14, True]

# Lista anidada
anidada = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(anidada[1][2])  # Output: 6
```

- **Slicing**: Las listas soportan slicing, lo que permite acceder a subpartes de la lista.

```python
# Slicing de lista
sublista = frutas[1:3]
print(sublista)  # Output: ['fresa', 'kiwi']
```
