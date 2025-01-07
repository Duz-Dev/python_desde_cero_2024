
def huevo():
    return gallina()
    
def gallina():
    return huevo()

print(gallina() + "LLego primero")

# def saludar():
#     print("Hola, ¿cómo estás?")
#     despedirse()

# def despedirse():
#     print("Adiós, cuídate.")

# # Llamada inicial
# saludar()

def factorial(n):
    if n == 0:  # Caso base
        return 1
    # Caso recursivo
    return n * factorial(n - 1)    

# Ejemplo de uso
print(factorial(3))



# def factorial(3):
#     if 3 == 0:  # Caso base
#         return 1
#     # Caso recursivo
#     return 3 * 2               

# # Ejemplo de uso
# print(factorial(3))

# def factorial(n):
#     if n == 0:  # Caso base
#         return 1
#     # Caso recursivo
#     return n * factorial(n - 1)

# # Ejemplo de uso
# print(6)