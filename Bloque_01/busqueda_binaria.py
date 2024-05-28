"""REGISTRO DE EMPLEADOS
Crea una lista de diccionarios llamada empleados. Cada registro de empleado contiene: "nombre","puesto","salario", y "proyectos".
Los proyectos es una lista de los proyectos en los que se encuentra trabajando en el pasado que, ademas del nombre del proyecto, indica el estatus (activo o concluido), su rol y, para los proyectos concluidos, su principal aportación al proyecto.
No hay limite de empleados ni de proyectos, se debe capturar el usuario quiera en cada caso.
Al final imprime el nombre de todos los empleados , su puesto y 3 proyectos en los que haya participado con estatus y rol de participación; si algún empleado tiene 1 o 2 proyectos, solo imprime esos, y si no tiene ninguno, omite esa parte de la impresión.
"""

empleados = [] # -> lista de empleados

empleado = {
    "nombre":None,
    "puesto": None,
    "salario": None,
    "proyectos":[]
}

def registrar_empleado():
    empleado["nombre"] = input("Ingresa el nombre: ")
    empleado["puesto"] = input("Ingresa el puesto: ")
    empleado["salario"] = input("Ingresa el salario: ")
    # empleado["proyectos"].append(registrar_proyectos())
    return empleado

while True:
    empleados.append(registrar_empleado())
    if input().upper == 's':
        break


# def registrar_proyectos():
#     proyecto = {
#         "nombre": None,
#         "estatus": None,
#         "rol":None,
#         "aportacion":None
#     }
#     return


