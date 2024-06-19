"""
!En un negocio de productos electrodomésticos se aplica un descuento del 8% a todos los clientes cuya compra sea mayor a $2500. Teniendo como dato el monto de la compra del cliente.
>>>imprime lo que debe el cliente.
"""

#*variables
compra = 0.0
descuento = 0.0
total = 0

#*input
print(">>>Compras Electrodomésticos<<<")
compra = float(input("ingresa el monto de la compra: "))

#*process
if compra > 2500:
    descuento = compra * 0.08
    print("Monto de compra mayor a 2500. Aplica descuento del 8%")

total = compra - descuento

#*output
print("-----------------------")
print("Total a pagar:", total)
print("-----------------------")
