# Variables

![img: Tipos de datos](https://i.postimg.cc/MTV6VRrV/imagen.png)

> *Repositorio*: [python_desde_cero_2024](https://github.com/Duz-Dev/python_desde_cero_2024) - fecha: 3/06/2024
---
<!-- TOC -->
- [Variables](#variables)
  - [¿Qué es un variable?](#qué-es-un-variable)
  - [Definición](#definición)
    - [Declaración y Asignación](#declaración-y-asignación)
    - [Sintaxis](#sintaxis)
    - [Asignación de valores](#asignación-de-valores)
    - [Identificadores, Valores y Tipos de Datos](#identificadores-valores-y-tipos-de-datos)
    - [Reglas para Nombres de Variables](#reglas-para-nombres-de-variables)
  - [Amplia tus conocimientos](#amplia-tus-conocimientos)
<!-- /TOC -->
---

## ¿Qué es un variable?

Una variable es un espacio en la memoria de la computadora que se usa para almacenar un valor que puede cambiar durante la ejecución de un programa.

Imagina que es una caja con una etiqueta (nombre de la variable) donde puedes poner y sacar cosas (valores) cuando lo necesites. Por ejemplo, puedes tener una variable llamada `edad` que almacena el valor `25`. Las variables son útiles para guardar información que necesitas usar o modificar más adelante en tu programa.

## Definición

en Python, una variable es un identificador que se vincula a un objeto en la memoria. Python es un lenguaje de tipado dinámico, lo que significa que no necesitas declarar explícitamente el tipo de una variable; el tipo se infiere a partir del valor asignado. La variable actúa como un contenedor que apunta a un valor almacenado en una dirección de memoria específica.

La utilidad de las variables radica en su capacidad para facilitar la gestión y manipulación de datos. Puedes realizar operaciones matemáticas, almacenar resultados de funciones, mantener el estado del programa y mucho más. Las variables en Python son nombres simbólicos que siguen ciertas reglas de sintaxis y convenciones de nomenclatura.

Cada «trozo» de memoria contiene realmente un objeto, de ahí que se diga que en Python todo son objetos. Y cada objeto tiene, al menos, los siguientes campos:

- Un **tipo** del dato almacenado.

- Un **identificador** único para distinguirlo de otros objetos.

- Un **valor** consistente con su tipo.

<center><img src="./img/object.jpg" alt="alt" width="500"/></center>


### Declaración y Asignación

La **declaración** de una variable es el proceso de crear la variable y reservar espacio en memoria para ella. En Python, no hay una declaración separada como en otros lenguajes; se declara y se asigna en una sola línea. La **asignación** es el proceso de darle un valor a la variable.

### Sintaxis

La sintaxis para declarar y asignar una variable en Python es sencilla. Se usa el signo igual `=` para asignar un valor a una variable. No se requiere especificar el tipo de dato.

```python
#ejemplo
variable = "valor"

x = 0  # Aquí, 'x' se declara y se le asigna el valor 10
nombre = "Juan"  # 'nombre' se declara y se le asigna el valor "Juan"
```

### Asignación de valores

Python no solo tiene una forma de asignar los valores, también soporta otras formas de asignación, como la asignación múltiple y el desempaquetado de tuplas o listas:

- **Asignación múltiple:** Asigna un valor a varias variables al mismo tiempo.

  ```python
  a = b = c = 5
  ```

- **Desempaquetado de tuplas/listas:** Asigna valores de una tupla o lista a varias variables.

  ```python
  x, y, z = 1, 2, 3
  # lo mismo sucede con listas
  x, y, z = [4,5,6] 
  # x = 4; y = 5; z = 6
  ```

Las variables en Python son flexibles y pueden cambiar de tipo a lo largo del programa. Aquí hay un ejemplo de reasignación de variables:

```python
variable = 10
print(variable)  # Salida: 10

variable = "ahora soy una cadena de texto"
print(variable)  # Salida: ahora soy una cadena de texto

variable = [1, 2, 3]
print(variable)  # Salida: [1, 2, 3]
```

### Identificadores, Valores y Tipos de Datos

Puedes obtener el identificador (ID), el valor, y el tipo de una variable usando las funciones integradas `id()`, `repr()`, y `type()` respectivamente:

```python
x = 10
print(id(x))  # Identificador único del objeto
print(repr(x))  # Representación del valor del objeto
print(type(x))  # Tipo de dato del objeto
```

### Reglas para Nombres de Variables

1. Los nombres de variables deben comenzar con una letra (a-z, A-Z) o un guion bajo (_).
2. Los caracteres siguientes pueden ser letras, dígitos (0-9), o guion bajo (_).
3. Los nombres de variables son sensibles a mayúsculas y minúsculas (`edad` y `Edad` son variables diferentes).
4. No se pueden usar palabras reservadas de Python como nombres de variables (como `if`, `else`, `for`, etc.).

> nota: Puedes ver todas las palabras reservadas (keywords) de python con la función `help('keywords')`

> Observación: Los nombres de variables son «case-sensitive» [^1]. Por ejemplo, stuff y Stuff son nombres diferentes.

Entre los programadores tenemos convenciones para nombrar elementos en nuestro código, aparte de lo que el propio lenguaje dicte, de esta manera sera mas legible y entendible entre nosotros lo que otros hacen.
A continuación en listare algunos puntos mas a tener en cuenta al menos en python:

- Todas las variables deben ser escritas con el estilo **Snake case**.

```python
num_elements = [1,2,3] #Snake case

#! Ejemplo de otras convenciones:
NumElements = [1,2,3] #Pascal case
numElements = [1,2,3] #camael case
```

- Si queremos dar a entender que un valor sera constante, podemos escribirla en mayúsculas.

```python
PI = 3.141519

MY_NAME = "Juan"
```

- A pesar de poder colocar guiones bajos al principio, no los utilices a no ser que estés en el contexto de clases o funciones especiales.

- Elije buenos nombres para tus variables y evita que no sean mayores a tres palabras.
  1. ``n``
  2. ``num_elements``
  3. ``number_of_elements``
  4. ``number_of_elements_to_be_handled``
  - En este caso, la mejor a utilizar sera la 2da o en su defecto la 3era opción.

- Usar nombres para variables (ejemplo ``article``).

- Usar verbos para funciones (ejemplo ``get_article()``).

- Usar adjetivos para booleanos (ejemplo ``available``)

## Amplia tus conocimientos

[^1]: Sensible a cambios en mayúsculas y minúsculas.

Visita: [Aprendepython.es](https://aprendepython.es/core/datatypes/data/#variables) para conocer mas de tipos de datos.
