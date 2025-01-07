import inspect

def factorial(n):
    # Obtener información de la pila en este punto
    stack = inspect.stack()
    print("\n--- Estado de la pila ---")
    for frame_info in stack:
        print(f"Función: {frame_info.function}, Línea: {frame_info.lineno}, Archivo: {frame_info.filename}")
        print(f"Variables locales: {frame_info.frame.f_locals}")
    print("--- Fin del estado de la pila ---\n")
    
    # Caso base
    if n == 0:
        return 1

    # Caso recursivo
    return n * factorial(n - 1)

stack = inspect.stack()
print("\n--- Estado de la pila ---")
for frame_info in stack:
        print(f"Función: {frame_info.function}, Línea: {frame_info.lineno}, Archivo: {frame_info.filename}")
        # print(f"Variables locales: {frame_info.frame.f_locals}")
print("--- Fin del estado de la pila ---\n")
# Ejemplo de uso
print(factorial(3))
