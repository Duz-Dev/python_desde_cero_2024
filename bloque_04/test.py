import timeit

conjunto = set()

for i in range(1,2000001):
    conjunto.add(i)

lista = list(conjunto)


# Definimos los algoritmos como funciones
def algoritmo_1():
    return 140535 in conjunto    
    
def algoritmo_2():
    return 140535 in lista

    
# Usamos timeit para medir el tiempo de cada algoritmo
tiempo_1 = timeit.timeit(algoritmo_1, number=10)  # Repetimos 10 veces
tiempo_2 = timeit.timeit(algoritmo_2, number=10)

print(f"Tiempo promedio de algoritmo_1: {tiempo_1 / 10:.20f} segundos")
print(f"Tiempo promedio de algoritmo_2: {tiempo_2 / 10:.20f} segundos")
