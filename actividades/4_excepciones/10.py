"""
!Sistema de Reseñas de Productos
* Estás diseñando un sistema de reseñas para una tienda en línea. Cada usuario puede dejar una reseña para un producto, pero debes validar que las reseñas cumplan con ciertas condiciones:

Puntuación del producto: Debe ser un número entre 1 y 5. Si el usuario ingresa un número fuera de este rango, lanza una excepción PuntuacionInvalida.
Comentario: Debe tener al menos 15 caracteres. Si el comentario es demasiado corto, lanza una excepción ComentarioCortoError.
ID del producto: Debe ser un número entero positivo. Si el ID no es válido, lanza una excepción IDProductoInvalido.
Tareas:

Escribe una función que tome la puntuación, comentario y ID del producto como entrada y valide cada campo.
Utiliza try, except, y finally para gestionar errores y, al final, confirmar si la reseña fue guardada.
Almacena las reseñas válidas en una lista reseñas.
Salida esperada:

El programa debe mostrar mensajes de error cada vez que un campo no cumpla con los requisitos.
Si la reseña es válida, se guarda en la lista y muestra un mensaje de confirmación.
"""