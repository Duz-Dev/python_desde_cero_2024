
#TODO: Existen muchos operadores en python. Te mostrare los mas utilizados

#! Aritméticos
"""
?suma +
?resta -
?division /
?division entera //
?modulo ó residuo %
?multiplicacion *
?exponente **
"""

suma = 10 + 5
print(suma)#Salida: 15

resta = 49 - 9
print(resta)#Salida: 40

division = 15 / 7
print(division)#Salida: 2.1428...

div_entera = 15 // 7
print(div_entera)#Salida: 2

residuo = 15 % 7
print(residuo)#Salida: 1

multiplicacion = 2 * 8
print(multiplicacion)#Salida: 16

exponente = 2**3

print(exponente)#Salida: 8

#? Por ejemplo, podremos plasmar con ayuda del exponente, las raices. Esto debido a que las raices se definen como aquellos números racionales que se utilizan en vez de los enteros.

#ejemplo
raiz_cuadrada = 4**(1/2)
print(raiz_cuadrada)#Salida: 2.0


#! Comparación
#Este tipo de comparadores comparan dos valores y devuelven un valor booleano (True o False) basado en la relación entre ellos. Sin embargo, cuando se comparan valores no numéricos como cadenas de texto, Python utiliza el orden lexicográfico (similar al orden del diccionario). 

"""
? mayor que >
?menor que  <
?igual ==
?'diferente a' o 'desigualdad' !=
?mayor o igual que >=
?menor o igual que <=
"""
#Ejemplos

#>>> ejercicio. Mayor de edad
edad = int(input("Ingresa tu edad: "))

print(edad >= 18)#Salida: True | False

#>>> ejercicio. Salario

salario = int(input())
print(salario <= 1000)

#>>> ejecicicio. Locacion
edad2 = int(input("ingresa tu edad: "))
locacion = int(input("cuanto tiempo llevas viviendo en tu recidencia actual: "))
comparacion = edad == locacion
print("Usted lleva viviendo toda su vida en la misma locacion: ", comparacion)

#* Cuando se comparan cadenas de texto, Python las compara carácter por carácter utilizando el valor ASCII de cada carácter.
#ejemplo
print("ejemplo de codigo acii")
print("texto" > "hola")#Salida: True
"""
?En este caso, Python compara los caracteres de "texto" y "hola". La comparación comienza con el primer carácter de cada cadena. Como t (ASCII 116) es mayor que h (ASCII 104), la comparación texto > hola es True.
"""
#Ejemplo
print("apple" < "banana")  # Salida: True
print("Cherry" > "cherry")  # Salida: False (C es menor que c en ASCII)
print("10" < "2")  # Salida: True (la comparación es lexicográfica, no numérica)


#*Python permite la comparación de otros tipos de datos, pero las reglas son más específicas y a veces pueden generar errores si los tipos no son compatibles.
#Ejemplo
print(19 > 10)  # Salida: True
print(3.5 < 7)  # Salida: True

#note: print(10 > "10")  # Esto generará un TypeError en Python

#! lógicos
#?Los operadores lógicos (and, or, not) pueden operar sobre cualquier tipo de dato. En Python, estos operadores no siempre devuelven un valor booleano, sino uno de los operandos.
"""
? and. Retorna el primer operando si es False, de lo contrario, retorna el segundo operando.
? or. Retorna el primer operando si es True, de lo contrario, retorna el segundo operando.
?not. Retorna el valor booleano opuesto del operando.
"""

#*Recuerda que valores como: 0, "", None, [], {}, etc. Son tomados como valores falsos
#Ejemplos
False and True #salida: false

print(0 and 5)#Salida: 0
print("" and 5)#Salida: 0
print({} and 0)#Salida: {}
print(False and 5)#Salida: False
print(5 and 0)#Salida: 0
resultado = 3 and 5
print(resultado)# Salida: 5
print(0 and 5)# Salida: 0
print([] and "hola")# Salida: []
print("hola" and [])# Salida: []
print(0 and 5)# Salida: 0

print(0 or 5) # Salida: 5
print(3 or 4) # Salida: 3. Dado que el primer valor no es un valor falso, asume que el valor ingresado es verdadero, por ende imprime el 3.

#ejemplo. Seudo-condicional
a = 3
b = 5
resultado = (a > b) and "a es mayor" or "b es mayor"
print(resultado)  # Salida: "b es mayor"


#!Operadores de asignación
#?los operadores de asignación se utilizan para asignar valores a variables. Además de la asignación básica con el operador =, Python proporciona varios operadores compuestos que combinan una operación aritmética con la asignación.
"""
? asignación simple. =
? asignación y suma, +=
? asignación y resta, -=
? asignación y multi, *=
? asignación y div, /=
? asignación y div entera, //=
? asignación y mod. %=
? asignación y exp. **=
"""
# Asignación simple
x = 10
print(x)  # Salida: 10

# Asignación y suma
x += 5 #>>> EQUIVALENTE A: x = x + (5)
print(x)  # Salida: 15

# Asignación y resta
x -= 3 # >>> EQUIVALENTE A: x = x - (3)
print(x)  # Salida: 12

# Asignación y multiplicación
x *= 2 # >>> EQUIVALENTE A: x = x * (2)
print(x)  # Salida: 24

# Asignación y división
x /= 4 # >>> EQUIVALENTE A: x = x / (4)
print(x)  # Salida: 6.0

# Asignación y división entera
x //= 2
print(x)  # Salida: 3.0

# Asignación y módulo
x %= 2
print(x)  # Salida: 1.0

# Asignación y exponenciación
x **= 3
print(x)  # Salida: 1.0

#ejemplo
x = 10
cal = 25
cal += x * 10 #>>> EQUIVALENTE A: cal = cal + (x * 10)
print(cal)# Salida: 125


#! Operadores de identidad
#? los operadores de identidad son is y is not. Estos operadores verifican si dos referencias apuntan al mismo objeto en la memoria. A diferencia de ==, que verifica si los valores de los objetos son iguales, is verifica si los dos objetos son exactamente el mismo objeto (es decir, tienen la misma identidad).

"""
?is: Evalúa a True si las dos variables apuntan al mismo objeto en la memoria.
?is not: Evalúa a True si las dos variables no apuntan al mismo objeto en la memoria.
"""
#Ejemplo
a = [1, 2, 3]
b = a
c = [1, 2, 3]

# a y b son el mismo objeto
print(a is b)  # Salida: True

# a y c no son el mismo objeto, aunque tienen los mismos valores
print(a is c)  # Salida: False

# a y c no son el mismo objeto
print(a is not c)  # Salida: True

# Comparando con None
x = None
print(x is None)  # Salida: True


#! Operadores de membresía
#?Los operadores de membresía en Python se utilizan para verificar si un valor o variable está presente en una secuencia como una cadena, lista, tupla, conjunto o diccionario.

"""
?in: Evalúa a True si el valor especificado se encuentra en la secuencia.
?not in: Evalúa a True si el valor especificado no se encuentra en la secuencia.
"""

# Uso en listas
frutas = ['manzana', 'banana', 'cereza']
print('manzana' in frutas)  # Salida: True
print('uva' in frutas)      # Salida: False

# Uso en cadenas
cadena = "Hola, mundo"
print('Hola' in cadena)     # Salida: True
print('hola' in cadena)     # Salida: False  # Python es sensible a mayúsculas y minúsculas

# Uso en tuplas
tupla = (1, 2, 3, 4)
print(3 in tupla)           # Salida: True
print(5 in tupla)           # Salida: False

# Uso en conjuntos
conjunto = {1, 2, 3, 4}
print(2 in conjunto)        # Salida: True
print(5 not in conjunto)    # Salida: True

# Uso en diccionarios (verifica solo las llaves/clave)
diccionario = {'a': 1, 'b': 2, 'c': 3}
print('a' in diccionario)   # Salida: True
print('d' not in diccionario) # Salida: True
