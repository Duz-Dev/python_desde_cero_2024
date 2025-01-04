#Sets

#! CREAR SETS
mi_set = {1,2,3,4,5,6}
mi_set2 = set()

print(type(mi_set))    
"""
- Los elementos de un set no están nunca ordenados, pueden mantener un patrón pero no esta garantizado que el orden de añadido de los elementos sea fijo.
- Es muy utilizado para verificar si un objeto pertenece a un conjunto (set en ingles).
"""

pertenece = "Si pertenece al conjunto" if 3 in mi_set  else "no pertenece"
print(pertenece)

"""
- Los sets están pensados y creados para ser lo mas optimo al momento de hacer búsquedas de información
"""


#? Usamos el método add para añadir elementos al set
mi_set2.add(7)
mi_set2.add(2)
mi_set2.add(4)
mi_set2.add(5)
mi_set2.add(6)

print(mi_set2)

#Los sets no admiten valores duplicados, si añadimos uno ya existente, este lo omitirá
mi_set2.add(7)
print(mi_set2)

#? Esto es muy util para poder filtrar datos duplicados.
""" 
!Si nos pidieran filtrar datos duplicados de una lista, seria util transformar la lista a un set
"""

lista = [1,2,3,4,5,2,3,1,5,10]
print(lista)

set_list = set(lista)
print(set_list)


#>>>OBS: Los set solo pueden contener elementos 'hashables', es decir aquellos elementos que solo son inmutables, como los str y los números. De lo contrario, python nos dirá que no es posible almacenar un valor que no cumpla con esta característica.

#Si ejecutas esta parte, dará error:
new_set = {"1234",[1,2,3]}
print(new_set)
