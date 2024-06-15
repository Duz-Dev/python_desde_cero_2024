
#TODO : Datos en python

#! string (str) -> cadena de texto
#ejemplos
"Soy un texto"
'Soy un texto pero de comillas simples'
'Vivo en "Bolivia"'
#?Recuerda que no es valido anidar comillas del mismo tipo.

#!Números. int(integer),float -> Enteros, flotantes/decimales

14 #int
31.15 #float
01.2 #No es recomendable empezar números con cero como en este caso.
0.1345 # esto si es valido.
45.00 #float

#!Booleanos. True, False -> Verdadero, Falso

True #Ambos valores deben de empezar con mayúscula
False

#? Dependiendo del contexto como en la situación de comparar valores o esperar expresiones lógicas, se puede decir que existen expresiones equivalentes a falso.

#ejemplo
#>>> cadena vacia ""
#>>> numero cero 0
#>>> None
#>>> diccionario vacio {}


#!None -> nada

None #Expresa 'nada', la ausencia de valor.

#ejemplo
print(print()) #Salida: none


#*Estructuras de datos

#!List -> Lista

#? Pueden contener cualquier dato existente que ya conocemos
[1,2,3,4,5]
[10,506,"doce",13.413,True,None]

#!Tuple -> Tupla
#? exactamente a su hermano la lista, pero una vez que añadamos la primera vez los datos, estos ya no pueden ser modificados (mutados)
(123,123,"lorem","#")

#! dict -> diccionario
#?parecidos a estructuras como los objetos en javascript
{"clave":"valor"}

#! set -> conjunto
#?Estan orientados a crear conjuntos de valores de un tipo en común y ahorrar recursos de búsqueda e index
{"valor","valor2"}
