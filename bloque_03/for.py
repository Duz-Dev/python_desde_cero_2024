
#!Hacer un algoritmo en python que diga si un número es par o impar

lista = [1,2,3,4,5,6,7,8,9,10]

for x in lista:
    if x % 2 == 0:
        print(f"{x} es par")
    else:
        if not(x == 1):
            break