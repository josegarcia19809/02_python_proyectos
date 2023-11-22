def imprimir_linea():
    print("-" * 100)


# Primera forma de crear un diccionario
cat = {
    "name": "blue",
    "age": 3.5,
    "es_lindo": True
}

print(cat)

# Otra forma de crear un diccionario
cat2 = dict(name="Kitty", age=4.0, es_lindo=True)
print(cat2)

imprimir_linea()
# Mostrar datos
print(cat["name"])
print(cat2["name"])
try:
    print(cat2["color"])
except KeyError:
    print("La llave no existe")

imprimir_linea()
# Mostrar los valores
print(cat.values())
# Iterar sobre los valores
for value in cat.values():
    print(value)

imprimir_linea()
# Mostrar las claves
print(cat.keys())
# Iterar sobre los valores
for key in cat.keys():
    print(key)

imprimir_linea()

# Mostrar ambos valores
print(cat.items())
# Iterar sobre ambos valores
for k, v in cat.items():
    print(f"{k}: {v}")

imprimir_linea()
# Existe una llave
print("name" in cat)
print("last" in cat)
imprimir_linea()

# Existe un valor
print("blue" in cat.values())
print("red" in cat.values())
