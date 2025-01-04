
<!-- TODO redactar correctamente el principio de este apunte y añadir mas modulos built in -->

# Introducción

Cuando se desarrollan aplicaciones que requieren interactuar con otros servicios o sistemas, las peticiones a APIs (Interfaz de Programación de Aplicaciones) se vuelven cruciales. Python, al ser un lenguaje flexible y popular, ofrece varias formas de realizar solicitudes HTTP, siendo el módulo `requests` uno de  los más utilizados por su simplicidad y eficiencia.

Imagina que estás construyendo una aplicación que necesita obtener datos de un servicio externo, como un pronóstico del clima, información financiera o incluso integrar un servicio de autenticación. Para ello, puedes hacer uso de las peticiones HTTP. `requests` es una librería que facilita este proceso y permite enviar peticiones de forma sencilla, manejar las respuestas, y gestionar errores comunes de manera amigable.

Este módulo simplifica las interacciones con APIs al permitirte realizar peticiones GET, POST, PUT, DELETE y otras más, además de manejar parámetros, autenticación, y los encabezados de las solicitudes. A continuación, exploraremos cómo empezar a trabajar con `requests` para interactuar con servicios web.

## Instalación

Para instalar la librería `requests`, solo necesitas usar el siguiente comando:

```bash
pip install requests
```

Este comando instalará la librería y la hará disponible para su uso en tus proyectos. Es recomendable crear un entorno virtual para mantener las dependencias organizadas.

## Hacer una solicitud GET

Una de las formas más comunes de interactuar con una API es a través de una solicitud GET. Esta solicitud se usa cuando deseas obtener datos de un servidor.

Ejemplo de una solicitud GET simple:

```python
import requests

url = "https://api.exemplo.com/datos"
respuesta = requests.get(url)

if respuesta.status_code == 200:
    print("Datos obtenidos correctamente")
    print(respuesta.json())  # Imprime la respuesta en formato JSON
else:
    print(f"Error al hacer la solicitud: {respuesta.status_code}")
```

En este ejemplo, `requests.get()` realiza la petición a la URL especificada. Si el código de estado HTTP es 200 (lo que indica éxito), se muestra el contenido de la respuesta en formato JSON.

- **`url`**: la URL de la API o el recurso al que deseas acceder.
- **`respuesta.status_code`**: devuelve el código de estado HTTP. 200 es el código de éxito, pero puede haber otros códigos que indican errores.
- **`respuesta.json()`**: método para obtener la respuesta en formato JSON si el servidor la envió de esa forma.

## Hacer una solicitud POST

Si necesitas enviar datos al servidor, como enviar un formulario o enviar datos JSON, debes utilizar una solicitud POST.

Ejemplo de una solicitud POST:

```python
import requests

url = "https://api.exemplo.com/usuario"
datos = {
    "nombre": "Juan",
    "edad": 28
}

respuesta = requests.post(url, json=datos)

if respuesta.status_code == 201:
    print("Datos enviados correctamente")
else:
    print(f"Error al enviar los datos: {respuesta.status_code}")
```

En este caso, estamos enviando un diccionario como un cuerpo JSON en la solicitud POST.

- **`json=datos`**: al pasar un diccionario, `requests` automáticamente lo convierte a formato JSON y agrega la cabecera adecuada.
- **`respuesta.status_code == 201`**: el código 201 indica que los datos se han creado correctamente en el servidor.

## Manejo de respuestas

Las respuestas de una solicitud pueden ser mucho más que solo el cuerpo del mensaje. `requests` ofrece herramientas para obtener información adicional como los encabezados, el código de estado y la duración de la solicitud.

Ejemplo de cómo obtener los encabezados y el contenido de la respuesta:

```python
respuesta = requests.get("https://api.exemplo.com/datos")

print("Encabezados:", respuesta.headers)  # Muestra los encabezados de la respuesta
print("Contenido:", respuesta.content)    # Muestra el contenido crudo
print("Tiempo de respuesta:", respuesta.elapsed)  # Muestra el tiempo de la solicitud
```

- **`respuesta.headers`**: devuelve un diccionario con los encabezados HTTP.
- **`respuesta.content`**: devuelve el contenido de la respuesta en formato binario.
- **`respuesta.elapsed`**: muestra el tiempo que tardó la solicitud en procesarse.

## Manejo de errores

Al trabajar con APIs y servicios web, es crucial manejar errores que puedan surgir, como la falta de conexión, un código de estado no exitoso o problemas en la respuesta.

Ejemplo de manejo de errores:

```python
try:
    respuesta = requests.get("https://api.exemplo.com/datos")
    respuesta.raise_for_status()  # Lanza una excepción para errores 4xx o 5xx
except requests.exceptions.HTTPError as err:
    print(f"Error HTTP: {err}")
except requests.exceptions.RequestException as err:
    print(f"Error general en la solicitud: {err}")
```

- **`raise_for_status()`**: lanza una excepción si el código de estado no es 2xx (por ejemplo, 404 o 500).
- **`requests.exceptions.RequestException`**: captura cualquier otro error relacionado con la solicitud, como problemas de red.

## Parámetros y cabeceras

Las peticiones HTTP pueden llevar parámetros y cabeceras, que son necesarios para interactuar correctamente con muchas APIs. Los parámetros se pueden enviar en la URL, y las cabeceras proporcionan información adicional sobre la solicitud.

Ejemplo de cómo enviar parámetros en una solicitud GET y agregar cabeceras:

```python
url = "https://api.exemplo.com/datos"
parametros = {"nombre": "Juan", "edad": 28}
cabeceras = {"Authorization": "Bearer token_aqui"}

respuesta = requests.get(url, params=parametros, headers=cabeceras)

print(respuesta.json())
```

- **`params`**: diccionario que se convierte en parámetros en la URL (como `?nombre=Juan&edad=28`).
- **`headers`**: diccionario con los encabezados HTTP, útil para pasar tokens de autenticación o tipos de contenido.

## Autenticación

Muchos servicios API requieren autenticación, y `requests` ofrece varias formas de manejarla, como autenticación básica, con tokens, o mediante un sistema más complejo.

Ejemplo de autenticación con un token:

```python
url = "https://api.exemplo.com/protegido"
cabeceras = {"Authorization": "Bearer mi_token_de_acceso"}

respuesta = requests.get(url, headers=cabeceras)

if respuesta.status_code == 200:
    print("Acceso autorizado")
else:
    print("No autorizado")
```

En este caso, la autenticación se realiza mediante un token de acceso que se incluye en los encabezados de la solicitud.

---

Con este flujo de trabajo básico, puedes empezar a interactuar con diversas APIs utilizando Python y el módulo `requests`. Desde obtener datos hasta enviar información o autenticarte, este módulo facilita todas esas tareas de manera eficiente.

```
