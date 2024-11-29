def pedir_numero(prompt, tipo=float):
    """
    Solicita al usuario un número y lo valida.
    Si la entrada no es válida, vuelve a pedir el dato.

    Parámetros:
    - prompt: Mensaje que se muestra al usuario.
    - tipo: Tipo de dato que se espera (por defecto, float).

    Retorna:
    - Un número (float o int) válido ingresado por el usuario.
    """
    while True:
        entrada = input(prompt)
        try:
            # Intentar convertir la entrada al tipo especificado
            return tipo(entrada)
        except ValueError:
            print(f"Error: Por favor, ingresa un valor numérico válido ({tipo.__name__}).")

numero = pedir_numero("Ingresa un número flotante: ")
print(f"Número ingresado: {numero}")

entero = pedir_numero("Ingresa un número entero: ", tipo=int)
print(f"Entero ingresado: {entero}")