# saludo = "Hola me llamo pablo"

# print(saludo[0:4])

# print(saludo[0]+saludo[3])

# # saludo = "Hola"

# # list(saludo)

# # print(saludo)

# # frutas = ["hola","chettos"]

# # frutas.append(saludo)

# # print(frutas)


# lista = [None]

# lista[0] = "hola"

# print(lista)

# anidada = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# for i in anidada:
#     if 5 in i:
#         print(i)

lista2 = [1,2,3]

lista3 = [4,5,6]

# print((lista2+lista3)[0:3])


lista_copy = lista3.copy()

lista4 = lista2.copy()

print(lista4)

lista2[0] = False

print("lista 4:",lista4)
print(f"lista 2: {lista2}")


lista_de_listas = ["hola","chettos",lista4,lista3,[lista2,lista3]]

print(lista_de_listas[4][1][1])

frutas = ['manzana', 'fresa', 'banana', 'naranja', 'kiwi']

print(frutas[0:3])

print(lista4 * 3)

print(len(frutas))

for i in frutas:
    print(i)

for i in range(len(frutas)):
    print(frutas[i])