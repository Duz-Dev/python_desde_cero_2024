#Yan
# En base a eI ejercicio planteado con la estructura match, donde se creo una
#calculadora. Crea un menu, donde el usuario ingrese una de las opciones validas, de Io
#contrario, que vuelva a ingresar dicho valor.
#! Modifica las opciones para que pueda salir de dichas opciones y pueda volver a
#escoger entre las opciones.
operador = ""
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
operadores=["+","-","*","/"]
while operador not in operadores:
  operador = input("Ingrese un operador \n Suma (+) \n Resta (-) \n Multiplicacion(*) \n Division(/) \n :")
  if operador not in operadores:
    print("Operador no válido")
match operador:
  case "+":
    resultado = num1 + num2
  case "-":
    resultado = num1 - num2
  case "*":
    resultado = num1 * num2
  case "/":
    resultado = num1 / num2
  case _:
    print("Operador no válido")
    exit()
print(resultado)
