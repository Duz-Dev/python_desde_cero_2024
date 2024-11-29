def sumar(a, b):
    """
    # Suma dos numeros.

    Parametros:
        a (int o float): El primer numero.
        b (int o float): El segundo numero.
    
    Retorna:
        int o float: La suma de a y b.
    """
    return a + b

# Llamada
help(sumar)

def calcular_precio(base: float, impuesto: float = 0.16, descuento: float = 0.0) -> float:
    """
    ## calcular_precio
    > Calcula el precio final de un producto considerando el impuesto y un descuento opcional.

    **Parámetros:**
        base (float): Precio base del producto.
        impuesto (float): Porcentaje de impuesto a aplicar (por defecto 16%).
        descuento (float): Porcentaje de descuento a aplicar (por defecto 0%).

    **Retorna:**
        float: Precio final tras aplicar impuesto y descuento.
    """
    precio_con_impuesto = base + (base * impuesto)
    precio_final = precio_con_impuesto - (precio_con_impuesto * descuento)
    return precio_final

# Llamadas a la función
print(calcular_precio(100))  # Precio base de 100 con impuesto del 16%, sin descuento. Salida: 116.0
print(calcular_precio(100, descuento=0.10))  # Precio base de 100 con impuesto del 16% y descuento del 10%. Salida: 104.4
print(calcular_precio(100, 0.08, 0.05))  # Precio base de 100 con impuesto del 8% y descuento del 5%. Salida: 102.6

def diagnosticar_consola(temperatura, hardware_ok):
    if temperatura > 70:
        estado = "Defectuosa"
        mensaje = "Advertencia: Temperatura crítica. RIESGO DE FALLA."
    elif not hardware_ok:
        estado = "Defectuosa"
        mensaje = "Error: Problemas detectados en el hardware."
    else:
        estado = "Funcional"
        mensaje = "Todo está en orden."
    return estado, mensaje

# Llamada a la función
estado, mensaje = diagnosticar_consola(75, True)
print(estado)  # Salida: Defectuosa
print(mensaje) # Salida: Advertencia: Temperatura crítica. RIESGO DE FALLA.

