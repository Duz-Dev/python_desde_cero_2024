# Controles de flujo

![img: Tipos de datos](https://i.postimg.cc/xd3ZLrLM/image.png)

> *Repositorio*: [python_desde_cero_2024](https://github.com/Duz-Dev/python_desde_cero_2024) - fecha: 14/06/2024

Los controles de flujo o tambien llamados "Estructuras de control", son mecanismos que permiten controlar el orden de ejecución de las instrucciones en un programa. Existen varios tipos de controles de flujo que incluyen estructuras condicionales, bucles y estructuras de salto.

## Estructuras Condicionales

**`if`, `elif`, `else`**

Estas estructuras permiten ejecutar bloques de código basados en condiciones booleanas.

```python
# Ejemplo de uso
x = 10
if x > 5:
    print("x es mayor que 5")
elif x == 5:
    print("x es igual a 5")
else:
    print("x es menor que 5")
```

## Bucles

### `for`
El bucle `for` en Python se utiliza para iterar sobre una secuencia (como una lista, tupla, diccionario, conjunto o cadena de caracteres).

```python
# Ejemplo de uso
for i in range(5):
    print(i)
```

### `while`
El bucle `while` se ejecuta mientras una condición sea verdadera.

```python
# Ejemplo de uso
i = 0
while i < 5:
    print(i)
    i += 1
```

## Estructuras de Salto

### `break`
El `break` se usa para salir de un bucle antes de que haya terminado normalmente.

```python
# Ejemplo de uso
for i in range(10):
    if i == 5:
        break
    print(i)
```

### `continue`
El `continue` se usa para saltar el resto del código dentro de un bucle y pasar a la siguiente iteración del bucle.

```python
# Ejemplo de uso
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
```

### `pass`
El `pass` es una operación nula. No hace nada y se usa generalmente como un marcador de posición para futuras implementaciones de código.

```python
# Ejemplo de uso
if x > 0:
    pass  # Aún no se ha decidido qué hacer aquí
```

### `else` en bucles
Python permite usar `else` con bucles `for` y `while`. El bloque `else` se ejecuta cuando el bucle se completa sin que se haya ejecutado un `break`.

```python
# Ejemplo de uso
for i in range(5):
    print(i)
else:
    print("Bucle completado sin interrupción")
```

### `try`, `except`, `finally`
Estas estructuras se utilizan para manejar excepciones (errores) en Python.

```python
# Ejemplo de uso
try:
    x = 1 / 0
except ZeroDivisionError:
    print("División por cero no permitida")
finally:
    print("Este bloque se ejecuta siempre")
```

## Controles de Flujo que No Existen en Python y sus Equivalentes

### `switch` / `case`
Python no tiene una estructura `switch` / `case` como algunos otros lenguajes de programación (como C, C++ o Java). Sin embargo, se puede lograr un comportamiento similar utilizando diccionarios o múltiples declaraciones `if-elif-else`.

```python
# Ejemplo de uso de diccionario para simular switch-case
def switch_demo(argument):
    switcher = {
        0: "Cero",
        1: "Uno",
        2: "Dos",
    }
    return switcher.get(argument, "Valor no encontrado")

print(switch_demo(1))  # Salida: Uno
```

## Resumen de Controles de Flujo en Python

| Tipo            | Estructura        | Descripción                                                                      |
|-----------------|-------------------|----------------------------------------------------------------------------------|
| Condicional     | `if`, `elif`, `else` | Ejecuta bloques de código basados en condiciones.                                |
| Bucle           | `for`             | Itera sobre una secuencia (lista, tupla, cadena, etc.).                          |
| Bucle           | `while`           | Ejecuta un bloque de código mientras una condición sea verdadera.                |
| Salto           | `break`           | Sale del bucle inmediatamente.                                                   |
| Salto           | `continue`        | Salta el resto del código en la iteración actual y pasa a la siguiente iteración.|
| Salto           | `pass`            | Operación nula, utilizada como marcador de posición.                             |
| Manejo de Excepciones | `try`, `except`, `finally` | Maneja excepciones y errores en el código.                                   |
| Post-Bucle      | `else`            | Se ejecuta si el bucle se completa sin interrupción.                             |

### Ejemplo Práctico

```python
# Combinación de varios controles de flujo
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num == 3:
        continue
    elif num == 4:
        break
    print(num)
else:
    print("Bucle completado sin interrupción")

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: División por cero")
finally:
    print("Operación completa")
```
