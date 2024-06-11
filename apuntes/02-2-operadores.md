# Operadores en Python y su Jerarquía

## ¿Qué es un operador?

Un operador en Python es un símbolo que indica una operación a realizar sobre uno o más operandos. Los operadores permiten realizar cálculos aritméticos, comparaciones, operaciones lógicas, entre otros. Por ejemplo, el operador `+` se usa para sumar dos números.

## Definición

En Python, los operadores se dividen en varias categorías:

1. **Aritméticos:** Realizan operaciones matemáticas básicas.
2. **De comparación:** Comparan dos valores y devuelven `True` o `False`.
3. **Lógicos:** Operan sobre valores booleanos (`True` o `False`).
4. **De asignación:** Asignan valores a las variables.
5. **Bit a bit (bitwise):** Realizan operaciones a nivel de bits.
6. **De identidad:** Verifican si dos objetos son idénticos.
7. **De membresía:** Verifican si un valor pertenece a una secuencia (como una lista, tupla, etc.).

### Sintaxis y Ejemplos

#### Operadores Aritméticos

- **Suma (`+`):** Suma dos operandos.

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

#### Operadores de Comparación

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

#### Operadores Lógicos

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

##### ¿Qué es el concepto?

Los operadores lógicos `and`, `or`, y `not` se utilizan para realizar operaciones lógicas sobre valores. Estos operadores evalúan expresiones y devuelven uno de los valores de los operandos en lugar de simplemente `True` o `False`.

##### Operador `and`

El operador `and` devuelve el primer operando si es falso; de lo contrario, devuelve el segundo operando. Esto significa que si el primer operando es un valor "falso" (como `0`, `None`, una cadena vacía, una lista vacía, etc.), ese valor será el resultado. Si el primer operando es verdadero, el resultado será el valor del segundo operando.

Ejemplo:

```python
result = 0 and 5  # result será 0
result = 3 and 5  # result será 5
```

##### Operador `or`

El operador `or` devuelve el primer operando si es verdadero; de lo contrario, devuelve el segundo operando. Esto significa que si el primer operando es un valor "verdadero", ese valor será el resultado. Si el primer operando es falso, el resultado será el valor del segundo operando.

Ejemplo:

```python
result = 0 or 5  # result será 5
result = 3 or 5  # result será 3
```

##### Operador `not`

El operador `not` siempre devuelve un valor booleano: `True` si el operando es falso, y `False` si el operando es verdadero.

Ejemplo:

```python
result = not 0  # result será True
result = not 3  # result será False
```

##### Sintaxis y Ejemplos

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

#### Operadores de Asignación

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

#### Operadores Bit a Bit

- **Y (`&`):** Realiza una operación AND a nivel de bits.

  ```python
  o = 5 & 3  # o = 1
  ```

- **O (`|`):** Realiza una operación OR a nivel de bits.

  ```python
  p = 5 | 3  # p = 7
  ```

- **XOR (`^`):** Realiza una operación XOR a nivel de bits.

  ```python
  q = 5 ^ 3  # q = 6
  ```

- **NOT (`~`):** Invierte los bits del operando.

  ```python
  r = ~5  # r = -6
  ```

- **Desplazamiento a la izquierda (`<<`):** Desplaza los bits del operando a la izquierda.

  ```python
  s = 5 << 1  # s = 10
  ```

- **Desplazamiento a la derecha (`>>`):** Desplaza los bits del operando a la derecha.

  ```python
  t = 5 >> 1  # t = 2
  ```

#### Operadores de Identidad

- **Es (`is`):** Verifica si dos referencias apuntan al mismo objeto.

  ```python
  u = (5 is 5)  # u = True
  ```

- **No es (`is not`):** Verifica si dos referencias no apuntan al mismo objeto.

  ```python
  v = (5 is not 5)  # v = False
  ```

#### Operadores de Membresía

- **En (`in`):** Verifica si un valor está presente en una secuencia.

  ```python
  w = (3 in [1, 2, 3])  # w = True
  ```

- **No en (`not in`):** Verifica si un valor no está presente en una secuencia.

  ```python
  x = (4 not in [1, 2, 3])  # x = True
  ```

### Jerarquía de Operadores

La jerarquía (o precedencia) de operadores determina el orden en que las operaciones se realizan. Aquí está una tabla que muestra la jerarquía de operadores en Python, de mayor a menor precedencia:

| Operador                                        | Descripción                              |
|-------------------------------------------------|------------------------------------------|
| `()`                                            | Paréntesis                               |
| `**`                                            | Exponenciación                           |
| `+x`, `-x`, `~x`                                | Signo positivo, signo negativo, bitwise NOT |
| `*`, `/`, `//`, `%`                             | Multiplicación, división, división entera, módulo |
| `+`, `-`                                        | Suma, resta                              |
| `<<`, `>>`                                      | Desplazamiento a la izquierda, derecha   |
| `&`                                             | AND a nivel de bits                      |
| `^`                                             | XOR a nivel de bits                      |
| `|`                                             | OR a nivel de bits                       |
| `in`, `not in`, `is`, `is not`, `<`, `<=`, `>`, `>=`, `!=`, `==` | Operadores de comparación, identidad, y
