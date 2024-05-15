# Función print()

`print()` en Python es una función incorporada que se utiliza para imprimir mensajes en la consola o en otros dispositivos de salida, como archivos de texto. Su sintaxis básica es la siguiente:

```python
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
```

- `objects`: Este es un argumento opcional y puede contener uno o más objetos que se imprimirán. Puedes pasar varios objetos separados por comas y `print()` los imprimirá uno después del otro.

- `sep`: Este es el separador entre los objetos que se van a imprimir. Por defecto, es un espacio en blanco. Puedes cambiarlo especificando otro valor como una cadena de texto.

- `end`: Esta es la cadena que se agrega al final de la impresión. Por defecto, es un salto de línea (`'\n'`), lo que significa que después de imprimir los objetos, la siguiente impresión comenzará en una nueva línea. Puedes cambiar esto especificando cualquier cadena de texto.

- `file`: Este es el destino de la salida. Por defecto, es `sys.stdout`, que representa la consola estándar. Sin embargo, puedes redirigir la salida a otros dispositivos como archivos especificando el nombre del archivo o un objeto de archivo abierto.

- `flush`: Este es un indicador booleano que controla si se debe vaciar el búfer de salida después de imprimir. Por defecto, es `False`, lo que significa que el búfer no se vaciará automáticamente. Puedes establecerlo en `True` para forzar el vaciado del búfer inmediatamente después de imprimir.

Por ejemplo, aquí hay algunos usos típicos de la función `print()`:

```python
print("Hola, mundo!")
# >>> Hola, mundo!

nombre = "Juan"
edad = 25
print("Mi nombre es", nombre, "y tengo", edad, "años.")
# >>> Mi nombre es Juan y tengo 25 años.

print("Python", "es", "genial", sep='-')
# >>> Python-es-genial

print("Esto es una línea.", end=' ')
print("Esto está en la misma línea.")
# >>> Esto es una línea. Esto está en la misma línea
```

<span>repositorio: https://github.com/Duz-Dev/python_class</span>
