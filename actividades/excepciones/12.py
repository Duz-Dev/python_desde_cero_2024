"""
!Evaluación de Préstamos Bancarios
* Imagina que trabajas en el área de préstamos de un banco, y tu tarea es evaluar si un cliente es elegible para un préstamo. Para esto, el cliente debe cumplir ciertas condiciones:

Ingresos anuales: Deben ser mayores a $20,000. Si los ingresos son menores, lanza una excepción IngresoInsuficienteError.
Historial crediticio: El usuario debe ingresar "bueno" o "malo". Si el valor ingresado no es válido, lanza una excepción HistorialInvalidoError.
Cantidad solicitada: No puede ser mayor al 40% de sus ingresos anuales. Si es mayor, lanza una excepción CantidadSolicitadaExcesiva.
Tareas:

Escribe una función que tome estos datos y determine si el cliente es elegible o no.
Utiliza try y except para capturar errores y mostrar mensajes de advertencia en cada caso.
Al final, si todos los datos son válidos, el programa debe imprimir “Préstamo aprobado” o “Préstamo denegado” en función de los ingresos y el historial.
Salida esperada:

El sistema debe informar al usuario cada vez que no cumpla con una condición y permitirle intentarlo nuevamente.
El resultado final debe ser un mensaje que indique si el préstamo fue aprobado o denegado.

"""