
#TODO : Datos en python

#!string (str) -> cadena/texto

"Soy un texto"
'Soy un texto pero de comillas simples'

#!Números. int(integer),float -> Enteros, flotantes/decimales
14 #int
31.15 #float
01.2 #No es recomendable empezar números con cero como en este caso.
0.1345 # esto si es valido.
45.00

#!Booleanos. True, False -> Verdadero, Falso

True #Ambos valores deben de empezar con mayúscula
False

#!None -> nada

None #Expresa 'nada', la ausencia de valor.

#*Estructuras de datos

#!List -> Lista

[1,2,3,4,5]
[10,506,"doce",13.413,True,None]

#!Tuple -> Tupla

(123,123,"lorem","#")

a = 10
b = 5

lista = [1,2,3]
lista2 = lista
x = 10
y = x

print(id(lista))
print(id(lista2))

print(id(x))
print(id(y))