# edad = 0

# try:
#     edad = int(input("Ingresa edad: "))

#     if edad < 0:
#         raise ValueError("No puedes tener una edad negativa")
# except ValueError as e:
#     print("[ERROR]:",e)

# class ErrorSaldoInsuficiente(Exception):
#     def __init__(self, saldo, retiro, mensaje="Saldo insuficiente para completar el retiro."):
#         self.saldo = saldo
#         self.retiro = retiro
#         self.mensaje = mensaje
#         super().__init__(self.mensaje)

#     def __str__(self):
#         return f"{self.mensaje} Saldo disponible: {self.saldo}. Intento de retiro: {self.retiro}."


# def procesar_retiro(saldo, retiro):
#     try:
#         if retiro > saldo:
#             raise ErrorSaldoInsuficiente(saldo, retiro)
#         saldo -= retiro
#         print("Retiro exitoso. Saldo restante:", saldo)
#     except ErrorSaldoInsuficiente as e:
#         print(e)

# # Prueba del manejo de la excepción personalizada
# saldo_actual = 100
# retiro = 150
# procesar_retiro(saldo_actual, retiro)

class MiExcepcionPersonalizada(Exception):
    pass

try:
    raise MiExcepcionPersonalizada()
except MiExcepcionPersonalizada as e:
    print("Capturada una excepción personalizada:", e)

# try:
#     edad = int(input("Ingresa edad: "))

# except ValueError as e:
#     print(e)