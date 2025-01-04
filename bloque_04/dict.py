mi_dict = {
    "name": "pablo",
    1:"edad",
}

print(mi_dict)

libro = {
   "titulo": "El principito",
   "Autor": "Antoine de Saint-Exupéry",
   "publicacion":1943,
   "precio":340.94,
   "stock": 24,
   "Disponible_venta": False
}

print(libro.get("lorem"))

del libro["Disponible_venta"]

print(libro)

libro.pop("publicacion")

data = libro.keys()

print(data)
print(type(data))

print(libro)
print(libro.popitem())
print(libro)

ingredientes = {"harina": 500, "azúcar": 200, "mantequilla": 100}

for ingrediente in ingredientes:
    print(f"Ingrediente: {ingrediente}")
    
print(ingredientes.items())

print(ingredientes)

compra = ingredientes

compra["Leche"] = "2L"

print(f"""
Compra semanal: {compra}\n
lista de la receta: {ingredientes}
      """)