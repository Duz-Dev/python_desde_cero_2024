""" 
!Sistema de Registro de Usuarios
*Imagina que estás diseñando un sistema de registro para una aplicación. Los usuarios deben ingresar su nombre, su correo electrónico y su edad. Sin embargo, para garantizar que los datos sean correctos, implementa las siguientes reglas:

>>>Nombre: No debe contener números ni caracteres especiales. Si un usuario intenta registrarse con un nombre no válido, lanza una excepción personalizada NombreInvalidoError.

>>>Correo electrónico: Debe contener el símbolo @ y un dominio válido (como .com, .net). Si el formato es incorrecto, lanza una excepción EmailInvalidoError.

>>>Edad: Debe ser un número entero mayor de 13 años. Si no cumple con este requisito, lanza una excepción EdadInvalidaError.
Tareas:

Crea una función que tome estos datos como entrada y valide cada campo utilizando try y except.
Almacena los registros válidos en una lista llamada usuarios_registrados.
Muestra un mensaje de error específico cada vez que un campo no cumple con los requisitos y solicita los datos nuevamente hasta que sean válidos.
Salida esperada:

Para cada error, el sistema debe mostrar un mensaje adecuado y solicitar el dato de nuevo.
Al final, imprime la lista de usuarios registrados correctamente.
"""