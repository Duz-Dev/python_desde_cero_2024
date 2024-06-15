# Tipos de datos

![img: Tipos de datos](https://i.postimg.cc/htBKShRQ/tema-py-02.png)

> *Repositorio*: [python_desde_cero_2024](https://github.com/Duz-Dev/python_desde_cero_2024) - fecha: 14/06/2024

## ¿Qué es un datos?

En programación, un dato es cualquier tipo de información que puedes almacenar y manipular en tu programa. Puede ser un número, una palabra, una lista de cosas, o incluso algo más complejo como la información de un estudiante. Los datos son los bloques básicos con los que trabajas cuando creas programas.

En términos mas técnicos, un dato es una representación simbólica de información que puede ser almacenada, manipulada y transmitida por un programa. Los datos pueden ser de diferentes tipos, como numéricos, textuales, lógicos, etc.

En Python, siendo un lenguaje de programación de alto nivel y dinámicamente tipado [¹], gestiona los datos mediante objetos. Todo en Python es un objeto, incluidas las variables y los valores primitivos.

En Python, los datos se definen mediante clases y tipos incorporados. Cuando asignas un valor a una variable, Python automáticamente crea un objeto de la clase correspondiente para ese tipo de dato y gestiona la memoria para almacenar este valor. Por ejemplo, al asignar `x = 5`, Python crea un objeto entero con el valor 5.

## Definición

En Python, un dato como cualquier entidad que puede ser almacenada en la memoria y manipulada por el programa. Los datos en Python están estructurados como objetos de diversas clases incorporadas, tales como `int`, `float`, `str`, `list`, `dict`, `set`, `tuple` y `bool`.

## Tipos

A continuación mostrare de manera mas detallada cada uno de estos:

1. **Enteros (`int`):** Python usa una representación de enteros que permite almacenar números de tamaño arbitrario, solo limitado por la memoria disponible. Los enteros en Python son objetos de la clase `int`. Se plasman escribiendo directamente el numero.

   ```python
   a = 10
   b = -5
   ```

2. **Flotantes (`float`):** Los números de punto flotante son aquellos que comúnmente conocemos como decimales. En Python siguen el estándar IEEE 754 de doble precisión, que usa 64 bits para representar el número. Los flotantes son instancias de la clase `float`.

   ```python
   pi = 3.14159
   decimal = -.023
   uno = 0.99999999
   ```

   Python soporta múltiples formas de representar números, incluyendo la notación científica, que utiliza la letra e para denotar potencias de 10.

   ```python
   numero = 3.14e2
   print(numero)  # Salida: 314.0

   ```

   Python permite la representación de números en diferentes bases numéricas:

   - Hexadecimal: Utiliza el prefijo 0x o 0X.
   - Binario: Utiliza el prefijo 0b o 0B.
   - Octal: Utiliza el prefijo 0o o 0O.

   ```python
   hexadecimal = 0x1a
   binario = 0b1010
   octal = 0o12

   print(hexadecimal)  # Salida: 26
   print(binario)  # Salida: 10
   print(octal)  # Salida: 10

   ```

3. **Cadenas de texto (`str`):** Las cadenas en Python son inmutables, lo que significa que no pueden ser modificadas después de su creación. Están implementadas como objetos de la clase `str`. Este tipo de dato se crea al escribir entre comillas simples o dobles.

   ```python
   mensaje = "Hola, mundo"
   saludo = 'Saludos desde python'
   ```

   Python no permite escribir este tipo de dato anidando comillas del mismo tipo.

      ```python
      #Esto no es valido
      mensaje = "Vivo en "mexico""
      #Esto es correcto
      mensaje = 'Vivo en "mexico"'
      #Posible solución
      mensaje = "Vivo en \"mexico\""
      ```

   En el ultimo caso, si funciona, esto debido a que el carácter `\` en Python se conoce como el carácter de escape[²]. Se utiliza para introducir secuencias de escape en cadenas de texto y para continuar líneas de código largas en la siguiente línea.

   Otras características aplicables a este tipo de datos es la `concatenación` que no es mas que el acto de unir strings mediante el operador `+`. También es posible multiplicar los strings con el operador `*` y sera equivalente a escribir seguidamente el mismo texto uno detrás de otro.

   ```python
   mensaje = "texto" * 3
   print(mensaje) # Salida: textotextotexto

   mensaje = "hola" + "me" + "llamo" + 'pablos'
   print(mensaje) # Salida: Holamellamopablo
   ```

4. **Booleanos (`bool`):** Los booleanos son un subclase de enteros en Python. `True` y `False` son equivalentes a 1 y 0, respectivamente.

   ```python
   es_verdadero = True
   es_falso = False
   ```

   En Python, ciertos valores se consideran equivalentes a False cuando se evalúan en un contexto booleano, como en una condición if o en un operador lógico. Estos valores se conocen comúnmente como "falsy" o "valores falsos".Algunos de estos serian el valor `None`,el numero cero `0`,cadena vacía `""` o `''`,lista vacía `[]`,tupla vacía `()`,`range(0)`, diccionario vació `{}`,conjunto vació `set()`,bytes vacío `b''`.

5. **Listas (`list`):** Las listas son colecciones ordenadas y mutables de elementos. Pueden contener elementos de cualquier tipo y son instancias de la clase `list`.

   ```python
   numeros = [1, 2, 3, 4, 5]
   ```

6. **Tuplas (`tuple`):** Las tuplas son similares a las listas, pero son inmutables. Una vez creadas, no pueden ser modificadas. Son instancias de la clase `tuple`.

   ```python
   coordenadas = (10.0, 20.0)
   ```

7. **Conjuntos (`set`):** Los conjuntos son colecciones no ordenadas de elementos únicos. Los conjuntos son instancias de la clase `set`.

   ```python
   frutas = {"manzana", "naranja", "plátano"}
   ```

8. **Diccionarios (`dict`):** Los diccionarios son colecciones de pares clave-valor. Las claves deben ser únicas e inmutables, mientras que los valores pueden ser de cualquier tipo. Los diccionarios son instancias de la clase `dict`.

   ```python
   estudiante = {"nombre": "Juan", "edad": 20, "carrera": "Computación"}
   ```

## Menciones Honorificas

Existen otro tipos de datos en python de forma nativa, pero que no son tan utilizados a diferencia de los antes nombrados. A continuación mencionare estos:

**Complex**
Los datos tipo complex (abreviatura de «números complejos»), en Python, son aquellos que representan números que tienen una parte real y una parte imaginaria. En matemáticas, los números complejos se definen como la suma de una parte real y una parte imaginaria multiplicada por la unidad imaginaria (que se denota como «i» o «j»).

Los datos tipo complex se representan escribiendo un número real seguido por una «j» para indicar la parte imaginaria.

```python
z = 3 + 4j
print(z.real)  # Salida: 3.0
print(z.imag)  # Salida: 4.0
```

**Bytes (bytes)**
Los objetos de tipo bytes son secuencias inmutables de enteros en el rango de 0 a 255. Se utilizan principalmente para representar datos binarios, como archivos o datos transmitidos a través de una red.

```python
b = b"Hello"
print(b)  # Salida: b'Hello'
```

**Frozenset (frozenset)**
frozenset es una versión inmutable de set. Los elementos de un frozenset no pueden ser modificados después de su creación.

```python
fs = frozenset([1, 2, 3, 4])
print(fs)  # Salida: frozenset({1, 2, 3, 4})
```

### Amplia tus conocimientos

[¹]: #amplia-tus-conocimientos "tooltip"
[²]: #amplia-tus-conocimientos "tooltip"

[1] Un lenguaje de programación es dinámicamente tipado si una variable puede tomar valores de distintos tipos.

[2] Este es un tema mas ampleo que puedes consultar en el siguente [enlace](https://www.freecodecamp.org/espanol/news/secuencias-de-escape-en-python).

Visita: [Aprendepython.es](https://aprendepython.es/core/datatypes/) para conocer mas de tipos de datos.
