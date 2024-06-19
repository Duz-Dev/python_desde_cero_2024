"""
!Se reciben como datos las coordenadas de los puntos P1, P2, P3, que corresponde a los vértices de un triangulo. Desarrolla un algoritmo para calcular e 
>>>imprimir su perímetro.
"""

#*variables
p1 = [0,0]
p2 = [0,0]
p3 = [0,0]
distancia_a = 0.0
distancia_b = 0.0
distancia_c = 0.0
perimetro = 0.0
x = 0 #primer indice
y = 1 #segundo indice

#*input
print(">>>Datos del triangulo<<<")

print("- datos del punto 1 -")
p1[x] = int(input("valor en x: "))
p1[y] = int(input("valor en y: "))

print("- datos del punto 2 -")
p2[x] = int(input("valor en x: "))
p2[y] = int(input("valor en y: "))

print("- datos del punto 3 -")
p3[x] = int(input("valor en x: "))
p3[y] = int(input("valor en y: "))

#*process
distancia_a = ( (p1[x]-p2[x])**2 + (p1[y]-p2[y])**2 )**(1/2)
distancia_b = ( (p2[x]-p3[x])**2 + (p2[y]-p3[y])**2 )**(1/2)
distancia_c = ( (p3[x]-p1[x])**2 + (p3[y]-p1[y])**2 )**(1/2)

perimetro = (distancia_a + distancia_b + distancia_c)

#*output
print("-----------------------")
print(f"perímetro = {perimetro:.2f}")
print("-----------------------")