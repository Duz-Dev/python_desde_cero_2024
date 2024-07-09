
#!Operador ternario

#Es una forma de escribir un condicional de una manera mas compacta
#?<valor_si_verdadero> if <condición> else <valor_si_falso>


#>>>Ejemplo 1
x = 10
y = 20

resultado = "x es mayor" if x > y else "y es mayor"
print(resultado)  # Salida: "y es mayor"

#>>>Ejemplo 2

numero = 5
tipo = "par" if numero % 2 == 0 else "impar"
print(tipo)  # Salida: "impar"

#>>>Ejemplo 3
a = 5
b = 10
mayor = a if a > b else b
print(mayor)  # Salida: 10