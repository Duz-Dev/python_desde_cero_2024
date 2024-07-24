
#! Dado un numero entero, desarrolla un algoritmo para calcular la suma y el promedio de n números, e imprimir la suma y el promedio.

#*variables


#*input
print(">>>Datos de entrada<<<")
suma = 0
#*process
while True:
    num = int(input("Ingresa la cantidad de numeros a sumar: "))
    if num > 0:
        break
    else:
        print("dato no valido")


for i in range(1,num+1):
    suma += i



#*output
print("\n-----Datos de salida--------")
print(f">>> {suma}")
print("----------------------------")