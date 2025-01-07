# import time




# def contador(n: int) -> None:
#     for i in range(n): 
#         print(i)

# contador(1)

# print(inicio := time.time())


def mi_decorador(funcion):
    def envoltura(*args, **kwargs):
        # Código antes de la ejecución de la función original
        print("Ejecutando código antes de la función...")
        
        resultado = funcion(*args, **kwargs)
        
        # Código después de la ejecución de la función original
        print("Ejecutando código después de la función...")
        return resultado
    return envoltura

@mi_decorador
def saludar(nombre):
    print(f"Hola, {nombre}!")

saludar("Pablo")

# def contar(num:int)->None:
#     inicio = time.time()
#     for i in range(num):
#         print(i)
#     fin = time.time()
#     print(f"tiempo transcurrido: {fin - inicio} segundos")

# contar(1000)

def temporizador(funcion)-> None:
    def covertura(num):
        import time
        inicio = time.time()

        funcion(num)
        
        fin = time.time()
        print(f"tiempo transcurrido: {fin - inicio} segundos")
    return covertura

@temporizador
def contar(num:int)->None:
    for i in range(num):
        print(i)

contar(1000)

def contador_llamadas(funcion):
    contador = 0

    def envoltura(*args, **kwargs):
        nonlocal contador
        contador += 1
        print(f"Llamada #{contador}")
        return funcion(*args, **kwargs)

    return envoltura

@contador_llamadas
def saludar(nombre):
    print(f"¡Hola, {nombre}!")

# Uso
saludar("Juan")  # Salida: "Llamada #1" y "¡Hola, Juan!"
saludar("Ana")   # Salida: "Llamada #2" y "¡Hola, Ana!"
