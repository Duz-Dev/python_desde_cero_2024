# Tipos de datos

![img: Tipos de datos](https://i.postimg.cc/htBKShRQ/tema-py-02.png)

> *Repositorio*: [python_desde_cero_2024](https://github.com/Duz-Dev/python_desde_cero_2024) - fecha: 3/06/2024

## ¿Qué es un datos?

En programación, un dato es cualquier tipo de información que puedes almacenar y manipular en tu programa. Puede ser un número, una palabra, una lista de cosas, o incluso algo más complejo como la información de un estudiante. Los datos son los bloques básicos con los que trabajas cuando creas programas.

En términos mas técnicos, un dato es una representación simbólica de información que puede ser almacenada, manipulada y transmitida por un programa. Los datos pueden ser de diferentes tipos, como numéricos, textuales, lógicos, etc.

En Python, siendo un lenguaje de programación de alto nivel y [dinámicamente tipado] [1], gestiona los datos mediante objetos. Todo en Python es un objeto, incluidas las variables y los valores primitivos.

En Python, los datos se definen mediante clases y tipos incorporados. Cuando asignas un valor a una variable, Python automáticamente crea un objeto de la clase correspondiente para ese tipo de dato y gestiona la memoria para almacenar este valor. Por ejemplo, al asignar `x = 5`, Python crea un objeto entero con el valor 5.

## Definición

En Python, un dato como cualquier entidad que puede ser almacenada en la memoria y manipulada por el programa. Los datos en Python están estructurados como objetos de diversas clases incorporadas, tales como `int`, `float`, `str`, `list`, `dict`, `set`,`tuple` y `bool`.

## Tipos

A continuación mostrare de manera mas detallada cada uno de estos:

1. **Enteros (`int`):** Python usa una representación de enteros que permite almacenar números de tamaño arbitrario, solo limitado por la memoria disponible. Los enteros en Python son objetos de la clase `int`.

   ```python
   a = 10
   b = -5
   ```

2. **Flotantes (`float`):** Los números de punto flotante en Python siguen el estándar IEEE 754 de doble precisión, que usa 64 bits para representar el número. Los flotantes son instancias de la clase `float`.

   ```python
   pi = 3.14159
   ```

3. **Cadenas de texto (`str`):** Las cadenas en Python son inmutables, lo que significa que no pueden ser modificadas después de su creación. Están implementadas como objetos de la clase `str`.

   ```python
   mensaje = "Hola, mundo"
   ```

4. **Booleanos (`bool`):** Los booleanos son un subclase de enteros en Python. `True` y `False` son equivalentes a 1 y 0, respectivamente.

   ```python
   es_verdadero = True
   es_falso = False
   ```

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

### Amplia tus conocimientos

[1]: #amplia-tus-conocimientos "tooltip"

[[1]] Un lenguaje de programación es dinámicamente tipado si una variable puede tomar valores de distintos tipos

Visita: [Aprendepython.es](https://aprendepython.es/core/datatypes/) para conocer mas de tipos de datos.
