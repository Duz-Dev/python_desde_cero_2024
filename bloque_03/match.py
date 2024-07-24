
#!variables
a = 0
b = 0
opcion = 0
resultado = 0

print("calculadora")
print(
    "ingresa una de las siguiente opciones:\n"
    "opcion 1. Suma\n"
    "opcion 2. Resta\n"
    "opcion 3. Multiplicación\n"
    "opcion 4. Salir del programa\n"
)
opcion = int(input("Ingresa una opcion: "))
__

match opcion:
    case 1:
        print(">>>SUMA<<<")
        a = int(input("ingresa el primer numero: "))
        b = int(input("ingresa el segundo numero: "))
        resultado = a + b
    case 2:
        print(">>>RESTA<<<")
        a = int(input("ingresa el primer numero: "))
        b = int(input("ingresa el segundo numero: "))
        resultado = a - b
    case 3:
        print(">>>MULTIPLICACION<<<")
        a = int(input("ingresa el primer numero: "))
        b = int(input("ingresa el segundo numero: "))
        resultado = a * b
    case 4:
        print("saliendo del programa...")
        exit()
    case _:
        print("El caso no existe")
        exit()

print(f"El resultado es: {resultado}")


