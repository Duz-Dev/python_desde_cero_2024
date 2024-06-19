"""
!Desarrolla un algoritmo para calcular el precio de venta de un articulo. Se tiene como datos, la descripción del articulo y el costo de producción, el precio de venta se calcula añadiéndole el costo de producción del 120% como utilidad y el 15% de impuesto de fabricación.
>>>Se imprimirá la descripción del articulo y el precio de venta.
"""

#*variables
desc: str = "" #Descripción
costo = 0.0 #Costo de producción
precio_base = 0.0
precio_venta = 0.0
impuesto = 0.0 #Impuesto calculado del articulo
utilidad = 0.0 

#*input
print(">>>Precio venta articulo<<<")
desc = input("Ingresa la descripción: ")
costo = float(input("Ingresa el costo de producción: "))

#*process
utilidad = costo * 1.20 #120% costo de producción
precio_base = costo + utilidad # precio antes de impuestos
impuesto = precio_base * 0.15
precio_venta = precio_base + impuesto # precio final. Después de impuestos

#*output
print("-----------------------")
print("descripción del articulo:",desc)
print("Precio de venta:\t",precio_venta)
print("-----------------------")


"""
# Observación
En México, la Ley del Impuesto al Valor Agregado (IVA) establece que el impuesto debe incluirse en el precio de venta al consumidor. De allí que seguí los siguientes pasos:
Calcular la utilidad: 120% del costo de producción.
Calcular el precio base antes de ajustar para el impuesto: costo de producción + utilidad.
Ajustar el precio de venta para incluir el impuesto.
"""