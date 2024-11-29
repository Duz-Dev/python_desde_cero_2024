""" 
!Gestión de Inventario para una Tienda
*Eres el encargado de desarrollar un sistema de gestión de inventario para una tienda de electrónicos. Cada producto debe tener un nombre, una cantidad en inventario y un precio. Los empleados necesitan ingresar esta información, y el sistema debe verificar que los datos sean correctos.

Nombre del producto: No puede estar vacío ni tener menos de 3 caracteres. Si esto ocurre, lanza una excepción NombreProductoInvalido.
Cantidad: Debe ser un número entero positivo. Si se ingresa una cantidad negativa, lanza una excepción CantidadInvalida.
Precio: Debe ser un número decimal positivo mayor que cero. Si el precio no cumple con esta regla, lanza una excepción PrecioInvalido.
Tareas:

Crea un programa que permita registrar productos en el inventario utilizando try y except.
Si un producto es registrado con éxito, añade un mensaje de confirmación y almacénalo en una lista inventario.
Después de varios registros, el sistema debe imprimir el inventario completo.
Salida esperada:

Cada vez que hay un error en los datos, el programa debe informar al usuario y permitirle corregirlo.
Al finalizar, muestra todos los productos registrados en el inventario.
"""