from random import choice, randint

conjunto_nombres = ["pablo", "jorge","maria","paola","matin","ruben","diego"]
conjunto_apellido = ["acosta", "mendelez","martinez","ortiz","hernandez","gonzalez","paz"]
conjunto_edad = randint(14,17) #Retorna un numero entre 14-17
conjunto_carrera = ["LCC", "LSTI","ACTUARIA","LF","LMAD","MATEMATICA"]
conjunto_materias = ["CALCULO INTEGRAL", "PROGRAMACION BASICA","TOPICOS DE ALGEBRA","FISICA 1","CALCULO DIFERENCIAL","METODOLOGIA DE LA PROGRAMACION"]



def Insertar_Datos(limite:int = 0) -> list:
    #Insertar datos randoms de una muestra
    estudiante = {}
    estudiantes = []
    for _ in range(limite):
        estudiante["ID"] = _ + 1
        estudiante["nombre"] = choice(conjunto_nombres)
        estudiante["apellido"] = choice(conjunto_apellido)
        estudiante["edad"] = conjunto_edad
        estudiante["carrera"] = choice(conjunto_carrera)
        estudiante["materias_inscritas"] = [choice(conjunto_materias),choice(conjunto_materias),choice(conjunto_materias),choice(conjunto_materias)]
        #Añadimos el estudiante a la lista:
        estudiantes.append(estudiante.copy()) #ten en cuenta que el diccionario de estudiante al ser añadido a la lista, agg una referencia de este, por lo que todos los estudiantes añadidos serán una referencia uno tras otro del mismo, por lo que tendrían los mismos datos. Para corregir esto se puede explícitamente indicar que sera una copia lo añadido u añadir una ultima linea donde el diccionario estudiante este vació nuevamente:
        #Solución 2
        #estudiante = {}
        
    
    return estudiantes
total = 10

lista = Insertar_Datos(total)
for item in lista:
    print("---"*20)
    for clave,valor in item.items():
        print(f"{clave}: {valor}")
    

# print(lista[1]["materias_inscritas"][-1])