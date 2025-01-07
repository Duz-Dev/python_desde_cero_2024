tareas = [
    {"nombre": "Lavar platos", "completada": False, "prioridad": 2},
    {"nombre": "Comprar comida", "completada": True, "prioridad": 1},
    {"nombre": "Hacer ejercicio", "completada": False, "prioridad": 3}
]

# 1. Filtrar tareas incompletas
incompletas = filter(lambda tarea: not tarea["completada"], tareas)

# 2. Ordenar por prioridad
ordenadas = sorted(incompletas, key=lambda tarea: tarea["prioridad"])

# 3. Generar informe en mayúsculas
informe = map(lambda tarea: tarea["nombre"].upper(), ordenadas)

print(list(informe))