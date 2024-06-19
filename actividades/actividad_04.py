"""
!Desarrolla un algoritmo para el cual se da el nombre del empleado, la clave del empleado, y los 6 primeros sueldos mensuales del año. Calcula el ingreso total del semestre y el promedio mensual.
>>>Imprime la clave del empleado, nombre del empleado, ingreso total y el promedio mensual.
"""

#*variables
nombre = ""
clave = 0
sueldo_1 = sueldo_2 = sueldo_3 = sueldo_4 = sueldo_5 = sueldo_6 = 0.0
ingreso = 0.0 #ingreso total
promedio = 0.0 #promedio mensual

#*input
print(">>>Datos del Empleado<<<")
nombre = input("ingresar nombre: ")
clave = input("ingresar clave: ")
sueldo_1 = float(input("ingresar sueldo mes 1: "))
sueldo_2 = float(input("ingresar sueldo mes 2: "))
sueldo_3 = float(input("ingresar sueldo mes 3: "))
sueldo_4 = float(input("ingresar sueldo mes 4: "))
sueldo_5 = float(input("ingresar sueldo mes 5: "))
sueldo_6 = float(input("ingresar sueldo mes 6: "))

#*process
ingreso = sueldo_1 + sueldo_2 + sueldo_3 + sueldo_4 + sueldo_5 + sueldo_6
promedio = ingreso / 6

#*output
print("-----Datos mensuales-empleado--------")
print("Nombre:\t",nombre)
print("clave:\t",clave)
print("ingreso total del empleado:", ingreso)
print("promedio mensual de ingresos:",promedio)
print("-------------------------------------")
