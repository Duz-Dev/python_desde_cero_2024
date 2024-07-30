#Ejercicio 5
#!Pide un dato al usuario y verifica que sea entre 8 y 14 caracteres. De lo contrario, pidele que que dicho dato no es valido y lo vuelva a ingresar.
#!Con este, verifica si contiene una vocal, o un numero entre el uno y el tres, si es asi, elimina dichos caracteres del dato y vuélvalo a imprimir con la leyenda "dato modificado" y adjunta el resultado.
#? Requisitos: 
#* -Usa el ciclo for
#* -Nada de funciones nativas, módulos, funciones.


#*variables
dato = 0
i = 0
patron = 'aeiouAEIOU123'
dato2 = ""


#*input
print(">>>Datos de entrada<<<")
dato = input("ingresa un texto: ")

#*process


while True:
    for _ in dato:
        i += 1

    if not(8 <= i <= 14):
        print("Dato no valido, vuelvelo a ingresar.")
        dato = dato = input("ingresa un texto: ")
    else:
        break


for char in dato:
    if not(char in patron):
        dato2 += char

dato = dato2

#*output
print("\n-----Datos de salida--------")
print(f">>>{datoñ}")
print("----------------------------")