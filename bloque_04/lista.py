lista = [1,2,3,4,5,6]

conjunto = {1,2,3}

lista_nueva = lista.copy()
lista_nueva.append(conjunto)

print(lista_nueva)

print(
f"""
Elementos de la lista:
{lista}
Elementos del conjunto:
{conjunto}
Fusion de lista y conjuntos:
{lista_nueva}

"""#Esto ultimo retornara el ultimo elemento de la lista, en este caso el conjunto, y el ultimo elemento del conjunto
)

