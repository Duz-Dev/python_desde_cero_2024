# Función print()

![alt](https://i.postimg.cc/FHzTt9rD/image.png)

> *Repositorio*: [python_desde_cero_2024](https://github.com/Duz-Dev/python_desde_cero_2024) - fecha de edición: 3/06/2024
---

## Temas adjuntos

1.0 [Introducción a Python](./01_introduccion.md)

1.1 [Función Print](./01-1-funcion%20_print.md) (Estas aquí)
  
>Nota. Los temas adjuntos son la continuación del tema principal, ordenados en forma de indice numeral. **RECOMENDADO NO SALTÁRSELOS**

---

<!-- TOC -->

- [Función print()](#función-print)
  - [Temas adjuntos](#temas-adjuntos)
  - [Definición](#definición)
  - [Argumento `file`](#argumento-file)
    - [Detalles y Uso](#detalles-y-uso)
    - [Ejemplo 1: Redirigir la salida a un archivo](#ejemplo-1-redirigir-la-salida-a-un-archivo)
  - [Argumento `flush`](#argumento-flush)
    - [Detalles y Uso](#detalles-y-uso-1)
    - [Ejemplo 2: Forzar el vaciado del búfer](#ejemplo-2-forzar-el-vaciado-del-búfer)

<!-- /TOC -->
---
<!-- >[!NOTE] -->
> Esta función es nativa dentro de python y es la que utilizamos para mostrar información en la consola. El texto a continuación puede ser algo complejo si aun no conoces nada del tema de funciones, por lo que te recomendaría simplemente dar una leída y después compréndelo una vez ya hayas tocando el tema de funciones en este curso.

## Definición

`print()` en Python es una función incorporada que se utiliza para imprimir mensajes en la consola o en otros dispositivos de salida, como archivos de texto. Su sintaxis básica es la siguiente:

```python
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
```

- `objects`: Este es un argumento opcional y puede contener uno o más objetos que se imprimirán. Puedes pasar varios objetos separados por comas y `print()` los imprimirá uno después del otro. Gracias al asterisco '*' colocado al principio de este parámetro, todos los argumentos ingresados serán tomados como objetos a imprimir. Por ende, los demás parámetros de dicha función deben de ser **explícitamente** ingresados si es que queremos cambiar su argumento.

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

## Argumento `file`

El argumento `file` en la función `print()` determina hacia dónde se enviará la salida del texto que se imprima. Por defecto, este argumento está configurado en `sys.stdout`, que representa la consola estándar. Sin embargo, puedes cambiar este comportamiento para dirigir la salida a otro dispositivo, como un archivo de texto abierto en modo escritura.

### Detalles y Uso

- **Valor por defecto**: `sys.stdout`
- **Posibles valores**:
  - `sys.stdout`: Consola estándar.
  - Objeto de archivo abierto: Puedes especificar un objeto de archivo que se haya abierto previamente en modo escritura (`'w'` o `'a'`).

### Ejemplo 1: Redirigir la salida a un archivo

```python
# Abre un archivo en modo escritura
with open('output.txt', 'w') as f:
    # Redirige la salida de print() al archivo 'output.txt'
    print("Este es un mensaje de prueba.", file=f)
    print("Este es otro mensaje.", file=f)
```

En este ejemplo:

- Se abre el archivo `output.txt` en modo escritura (`'w'`).
- Se utiliza `print()` con el argumento `file=f` para redirigir la salida al archivo `output.txt`.
- Los mensajes especificados se escriben en el archivo en lugar de mostrarse en la consola.

## Argumento `flush`

El argumento `flush` en la función `print()` controla si el búfer de salida debe vaciarse inmediatamente después de imprimir los mensajes. El búfer es una región de memoria utilizada para almacenar temporalmente datos antes de enviarlos a su destino final (como la consola o un archivo).

### Detalles y Uso

- **Valor por defecto**: `False`
- **Posibles valores**:
  - `True`: Vacía el búfer inmediatamente después de imprimir.
  - `False`: Permite que el búfer se vacíe de manera automática según las políticas de optimización de Python.

### Ejemplo 2: Forzar el vaciado del búfer

```python
print("Mensaje 1")
# Espera para que el búfer se vacíe automáticamente

print("Mensaje 2", flush=True)
# Forza el vaciado del búfer después de imprimir "Mensaje 2"
```

En este ejemplo:

- El primer `print()` no tiene `flush=True`, por lo que el vaciado del búfer puede no ser inmediato.
- El segundo `print()` utiliza `flush=True`, lo que asegura que el búfer se vacíe inmediatamente después de imprimir "Mensaje 2". Esto puede ser útil cuando se necesita garantizar que la salida sea visible de inmediato, por ejemplo, en aplicaciones donde la sincronización de la salida es crítica.
