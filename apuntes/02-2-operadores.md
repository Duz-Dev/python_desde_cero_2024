# Operadores

![img: Tipos de datos](https://i.postimg.cc/pXWwQLbP/imagen.png)

> *Repositorio*: [python_desde_cero_2024](https://github.com/Duz-Dev/python_desde_cero_2024) - fecha de edición: 17/06/2024

<!-- TOC -->

- [Operadores](#operadores)
  - [Definición](#definición)
  - [Operadores Aritméticos](#operadores-aritméticos)
  - [Operadores de Comparación](#operadores-de-comparación)
  - [Operadores Lógicos](#operadores-lógicos)
    - [Operador `and`](#operador-and)
    - [Operador `or`](#operador-or)
    - [Operador `not`](#operador-not)
    - [Ejemplos](#ejemplos)
  - [Operadores de Asignación](#operadores-de-asignación)
  - [Operadores de Identidad](#operadores-de-identidad)
  - [Operadores de Membresía](#operadores-de-membresía)
  - [Jerarquía de Operadores](#jerarquía-de-operadores)
    - [Operador walrus](#operador-walrus)
  - [Amplia tus conocimientos](#amplia-tus-conocimientos)

<!-- /TOC -->

## Definición

Un operador en Python es un símbolo que indica una operación a realizar sobre uno o más operandos. Los operadores permiten realizar cálculos aritméticos, comparaciones, operaciones lógicas, entre otros. Por ejemplo, el operador `+` se usa para sumar dos números.

En Python, los operadores se dividen en varias categorías:

1. **Aritméticos:** Realizan operaciones matemáticas básicas.
2. **De comparación:** Comparan dos valores y devuelven `True` o `False`.
3. **Lógicos:** Operan sobre valores booleanos (`True` o `False`).
4. **De asignación:** Asignan valores a las variables.
5. **De identidad:** Verifican si dos objetos son idénticos.
6. **De membresía:** Verifican si un valor pertenece a una secuencia (como una lista, tupla, etc.).


## Operadores Aritméticos


  ```python
  x = 5 + 3  # x = 8
  ```

- **Resta (`-`):** Resta el segundo operando del primero.

  ```python
  y = 5 - 3  # y = 2
  ```

- **Multiplicación (`*`):** Multiplica dos operandos.

  ```python
  z = 5 * 3  # z = 15
  ```

- **División (`/`):** Divide el primer operando por el segundo.

  ```python
  a = 5 / 2  # a = 2.5
  ```

- **División entera (`//`):** Divide el primer operando por el segundo y retorna la parte entera del resultado.

  ```python
  b = 5 // 2  # b = 2
  ```

- **Módulo (`%`):** Retorna el residuo de la división del primer operando por el segundo.

  ```python
  c = 5 % 2  # c = 1
  ```

- **Exponenciación (`**`):** Eleva el primer operando a la potencia del segundo.

  ```python
  d = 5 ** 2  # d = 25
  ```

## Operadores de Comparación

- **Igualdad (`==`):** Verifica si dos operandos son iguales.

  ```python
  e = (5 == 3)  # e = False
  ```

- **Desigualdad (`!=`):** Verifica si dos operandos no son iguales.

  ```python
  f = (5 != 3)  # f = True
  ```

- **Mayor que (`>`):** Verifica si el primer operando es mayor que el segundo.

  ```python
  g = (5 > 3)  # g = True
  ```

- **Menor que (`<`):** Verifica si el primer operando es menor que el segundo.

  ```python
  h = (5 < 3)  # h = False
  ```

- **Mayor o igual que (`>=`):** Verifica si el primer operando es mayor o igual que el segundo.

  ```python
  i = (5 >= 3)  # i = True
  ```

- **Menor o igual que (`<=`):** Verifica si el primer operando es menor o igual que el segundo.

  ```python
  j = (5 <= 3)  # j = False
  ```

## Operadores Lógicos

Los operadores lógicos `and`, `or`, y `not` se utilizan para realizar operaciones lógicas sobre valores. Estos operadores evalúan expresiones y devuelven uno de los valores de los operandos en lugar de simplemente `True` o `False`.

- **Y (`and`):** Retorna `True` si ambos operandos son `True`.

  ```python
  k = (True and False)  # k = False
  ```

- **O (`or`):** Retorna `True` si al menos uno de los operandos es `True`.

  ```python
  l = (True or False)  # l = True
  ```

- **No (`not`):** Invierte el valor lógico del operando.

  ```python
  m = not True  # m = False
  ```

En este tipo de operadores hay que tener algo muy en cuenta, los operadores lógicos `and`, `or`, y `not` en Python no siempre devuelven un valor booleano (es decir, `True` o `False`). En su lugar, devuelven uno de los valores de los operandos. Vamos a ver cómo funciona esto en detalle:

### Operador `and`

El operador `and` devuelve el primer operando si es falso; de lo contrario, devuelve el segundo operando. Esto significa que si el primer operando es un valor "falso" (como `0`, `None`, una cadena vacía, una lista vacía, etc.), ese valor será el resultado. Si el primer operando es verdadero, el resultado será el valor del segundo operando.

Ejemplo:

```python
result = 0 and 5  # result será 0
result = 3 and 5  # result será 5
```

### Operador `or`

El operador `or` devuelve el primer operando si es verdadero; de lo contrario, devuelve el segundo operando. Esto significa que si el primer operando es un valor "verdadero", ese valor será el resultado. Si el primer operando es falso, el resultado será el valor del segundo operando.

Ejemplo:

```python
result = 0 or 5  # result será 5
result = 3 or 5  # result será 3
```

### Operador `not`

El operador `not` siempre devuelve un valor booleano: `True` si el operando es falso, y `False` si el operando es verdadero.

Ejemplo:

```python
result = not 0  # result será True
result = not 3  # result será False
```

### Ejemplos

Aquí hay más ejemplos para ilustrar cómo funcionan estos operadores:

```python
# Ejemplos del operador `and`
print(0 and 1)  # Devuelve 0
print(1 and 2)  # Devuelve 2
print([] and "hello")  # Devuelve []
print("hello" and "world")  # Devuelve "world"

# Ejemplos del operador `or`
print(0 or 1)  # Devuelve 1
print(1 or 2)  # Devuelve 1
print([] or "hello")  # Devuelve "hello"
print("hello" or "world")  # Devuelve "hello"

# Ejemplos del operador `not`
print(not 0)  # Devuelve True
print(not 1)  # Devuelve False
print(not [])  # Devuelve True
print(not "hello")  # Devuelve False
```

## Operadores de Asignación

- **Asignación (`=`):** Asigna el valor del operando derecho al operando izquierdo.

  ```python
  n = 5  # n = 5
  ```

- **Asignación suma (`+=`):** Suma el operando derecho al operando izquierdo y asigna el resultado al operando izquierdo.

  ```python
  n += 3  # n = 8
  ```

- **Asignación resta (`-=`):** Resta el operando derecho al operando izquierdo y asigna el resultado al operando izquierdo.

  ```python
  n -= 2  # n = 6
  ```

- **Asignación multiplicación (`*=`):** Multiplica el operando derecho al operando izquierdo y asigna el resultado al operando izquierdo.

  ```python
  n *= 2  # n = 12
  ```

- **Asignación división (`/=`):** Divide el operando derecho al operando izquierdo y asigna el resultado al operando izquierdo.

  ```python
  n /= 3  # n = 4.0
  ```

- **Asignación división entera (`//=`):** Realiza la división entera del operando derecho al operando izquierdo y asigna el resultado al operando izquierdo.

  ```python
  n //= 2  # n = 2.0
  ```

- **Asignación módulo (`%=`):** Realiza la operación módulo del operando derecho al operando izquierdo y asigna el resultado al operando izquierdo.

  ```python
  n %= 2  # n = 0.0
  ```

- **Asignación exponenciación (`**=`):** Realiza la exponenciación del operando derecho al operando izquierdo y asigna el resultado al operando izquierdo.

  ```python
  n **= 3  # n = 0.0
  ```

## Operadores de Identidad

Estos están mas orientados para utilizarlos al momento de trabajar con clases e instancias. Aun asi, te hago mención de estos para que los conozcas.

- **Es (`is`):** Verifica si dos referencias apuntan al mismo objeto.

  ```python
  u = (5 is 5)  # u = True
  ```

- **No es (`is not`):** Verifica si dos referencias no apuntan al mismo objeto.

  ```python
  v = (5 is not 5)  # v = False
  ```

## Operadores de Membresía

- **En (`in`):** Verifica si un valor está presente en una secuencia.

  ```python
  w = (3 in [1, 2, 3])  # w = True
  ```

- **No en (`not in`):** Verifica si un valor no está presente en una secuencia.

  ```python
  x = (4 not in [1, 2, 3])  # x = True
  ```

## Jerarquía de Operadores

La jerarquía (o precedencia) de operadores determina el orden en que las operaciones se realizan. Aquí está una tabla que muestra la jerarquía de operadores en Python, de mayor a menor precedencia:

| Precedencia | Operador(es)                                        | Descripción                                 |
|-------------|-----------------------------------------------------|---------------------------------------------|
| 1           | `()`                                                | Paréntesis                                  |
| 2           | `**`                                                | Exponenciación                              |
| 3           | `*`, `/`, `//`, `%`                                  | Multiplicación, división, división entera, módulo |
| 4           | `+`, `-`                                            | Suma, resta
| 5          | `in`, `not in`, `is`, `is not`, `<`, `<=`, `>`, `>=`, `!=`, `==` | Operadores de comparación, identidad, y membresía |
| 6          | `not`                                               | NOT lógico                                  |
| 7          | `and`                                               | AND lógico                                  |
| 8          | `or`                                                | OR lógico                                   |
| 10          | `:=`                                                | Operador de asignación por expresión "walrus"|

Si ya eres un conocedor a lujo de detalle, veras que omití algunos operadores como los bit a bit, debido a que no tocare dichos operadores en todo el curso.

### Operador walrus

Si vez a detalle, al final coloque el operador "walrus" (morza en español), que fue añadido en la 3.8. Este es en realidad un operador algo infravalorado dentro de python, ya que no se utiliza con frecuencia. Dicho operador permite asignar el valor de una variable y luego usarlo en una sola expresión en la misma linea de código.
Aca un ejemplo:

```python
# Sin el operador "walrus"
x = 5
print(x * 2)
```

Como vez, primero creo una variable y después en la impresión tomo el valor de la variable y la multiplico por 2.
Con el operador *morza* podríamos acortar esta misma lógica en una sola linea.

```python
# Con el operador "morza"
print((x:= 5) * 2)

```

Como veras, no es muy util en este tipo de casos. En donde considero que dicho operador puede ser mas utilizado es en condicionales y ciclos.
Ejemplo: Crea un ciclo donde le pidas con antelación palabras a un usuario y que cuando coloque la palabra "stop", salga de dicho ciclo.

```python
# Sin :=
line = input()
while line != "stop":
  print(f"Has ingresado {line}")
  line = input()
```

```python
#con :=
while (line := input()) != "stop":
  print(f"Has ingresado {line}")
```

Veras que si ejecutas ambos scripts, te darán el mismo resultado.
Ten en cuenta que:

- El operador := no reemplaza al operador de asignación =. La asignación con = sigue siendo la forma estándar de asignar valores a variables en declaraciones independientes.
- El operador := es útil principalmente en expresiones dentro de estructuras de control como if, while, listas por comprensión, etc.
- No se debe abusar del operador := para mantener la legibilidad del código. Su uso debe ser justificado y claro.

## Amplia tus conocimientos

Visita: [Aprendepython.es](https://aprendepython.es) para conocer más.
