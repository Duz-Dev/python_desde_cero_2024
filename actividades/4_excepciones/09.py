""" 
!Ejercicio: Verificación de Archivo de Configuración
Descripción: Imagina que tu programa depende de un archivo de configuración llamado config.txt. Crea un programa que intente abrir este archivo y valide que contenga ciertos datos necesarios para que el programa funcione correctamente.

Si el archivo config.txt no existe, el programa debe capturar la excepción FileNotFoundError y crear un archivo nuevo con datos predeterminados.
Si el archivo existe pero está vacío o incompleto, el programa debe capturar una excepción personalizada llamada ConfiguracionInvalidaError.
En el caso de que el archivo esté completo, el programa debe leer y mostrar el contenido del archivo.
>>>Pistas:Considera un bloque finally para cerrar el archivo en caso de que haya sido abierto.

"""
