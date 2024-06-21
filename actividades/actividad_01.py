"""
!Realiza un algoritmo para calcular el sueldo de un operador de tal manera que se otorgara un aumento del 5% si el operador trabaja mas de 40 horas. Se tiene como datos:
? nombre del empleado
? horas de trabajo
? pago por horas trabajadas
>>>Imprimir el nombre del operador y su sueldo.
"""

#*variables
#La notación a continuación no es necesaria. Se le conoce como declaración explicita
nombre: str = "" 
horas: float = 0.0 #horas trabajadas
pago_hora: float = 0.0
sueldo: float = 0.0
sueldo_aumento: float = 0.0
sueldo_neto:float = 0.0

#*input
print(">>> DATOS DEL EMPLEADO <<<")
nombre = input("Ingresa el nombre: ")
horas = float(input("Ingresa las horas: "))
pago_hora = float(input("Ingresa el pago por hora: "))

#*process
sueldo = pago_hora * horas

if horas > 40:
    sueldo_aumento = sueldo * 0.05

sueldo_neto = sueldo + sueldo_aumento #Sueldo final a mostrar

#*output
print("----------------------------")
print("Nombre del operador:",nombre)
print("sueldo:\t",sueldo_neto)
print("----------------------------")