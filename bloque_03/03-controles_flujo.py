
#TODO: Estructuras de control

#! Condicionales. IF-ELSE-ELIF

"""
if (condición):
    #código
"""

"""
if (condición):
    #código
else:
    #código
"""
"""
if (condición):
    #código
elif (condición):
    #código
else:
    #código
"""

#! Operador morza ':='
#sin operador morza
x = 10
print(x * 2)
#con el operador morza 
print(y:=10 * 2)

#segundo ejemplo
#sin :=
line = input()
while line != "stop":
    print("tu mensaje es",line)
    line = input()
#con :=
while (line:=input()) != "stop":
    print(f"tu mensaje es '{line}'")
