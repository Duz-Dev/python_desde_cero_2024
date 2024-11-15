""" 
!Diagnóstico de Fallos de Xbox 360 - Red Ring of Death (RROD)

*Un poco de historia. 
*Es 2005, y Microsoft ha lanzado la Xbox 360 al mercado. Sin embargo, muchas consolas comienzan a experimentar un problema que provoca que tres de los cuatro anillos del botón de encendido se iluminen en rojo: el temido "Red Ring of Death" (RROD). 
*Tu tarea es desarrollar un sistema de diagnóstico y reparación para identificar y resolver algunos de los errores más comunes.

>>>Sobrecalentamiento: Si el sistema detecta que la temperatura interna es mayor a 80°C, debe lanzar una excepción personalizada SobrecalentamientoError.
>>>>Fallo de memoria: Si el sistema de diagnóstico encuentra un fallo en los módulos de memoria (como errores en la carga de datos), debe lanzar una excepción FalloMemoriaError.
>>>>Problemas de fuente de poder: Si el voltaje de la fuente de poder es menor a 110V o mayor a 240V, debe lanzar una excepción FuenteDePoderError.

*¨ñObjetivos del programa:

Crea un programa que simule un sistema de diagnóstico de Xbox 360 con los posibles errores mencionados.
Desarrolla funciones específicas para cada tipo de diagnóstico:
diagnostico_temperatura(): Verifica si la consola está sobrecalentada.
diagnostico_memoria(): Simula la carga de datos de la memoria y verifica si hay fallos.
diagnostico_fuente_poder(): Verifica el voltaje de la fuente de poder.
Implementa un ciclo principal que permita al usuario diagnosticar y resolver problemas hasta que la consola esté en estado óptimo.
En caso de que ocurra alguno de los problemas mencionados, el sistema debe manejar el error utilizando try y except y ofrecer instrucciones al usuario para intentar resolverlo.
Requisitos adicionales:

Crea un menú para que el usuario elija qué diagnóstico ejecutar.
Si un error es encontrado, muestra una breve descripción del problema y registra el intento de diagnóstico en una lista historial_diagnosticos.
Implementa un sistema de verificación de múltiples intentos: si un error persiste más de tres veces en el mismo diagnóstico, lanza una excepción ErrorIrreparable que indique que la consola necesita ser enviada a reparación.
Ejemplo de flujo de trabajo:

El programa comienza y muestra un menú con opciones de diagnóstico.
El usuario elige la opción de diagnosticar la temperatura.
Si la temperatura es muy alta, el programa lanza la excepción SobrecalentamientoError e informa al usuario, sugiriendo apagar la consola y esperar unos minutos.
El usuario elige diagnosticar la memoria.
Si ocurre un fallo, el programa lanza la excepción FalloMemoriaError e informa al usuario, recomendando reiniciar la consola y verificar la conexión de los módulos de memoria.
Al final de cada intento de diagnóstico, el sistema registra la operación en el historial_diagnosticos.
Si el usuario intenta solucionar el mismo problema más de tres veces sin éxito, el programa lanza la excepción ErrorIrreparable y sugiere enviar la consola al servicio técnico.

Salida esperada:

Mensajes específicos para cada error, que ofrecen instrucciones detalladas de cómo resolver el problema.
Registro de cada diagnóstico y el número de intentos realizados.
Al final, si todos los diagnósticos son exitosos, el programa muestra un mensaje de que la consola está lista para usarse sin problemas.
"""