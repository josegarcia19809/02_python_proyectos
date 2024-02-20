def imprimir_linea():
    print("-" * 100)


# Primera forma de crear un diccionario
gato = {
    "nombre": "blue",
    "edad": 3.5,
    "es_lindo": True
}

print(gato)

# Otra forma de crear un diccionario
gato2 = dict(nombre="Kitty", edad=4.0, es_lindo=True)
print(gato2)

imprimir_linea()
# Mostrar datos
print(gato["nombre"])
print(gato2["nombre"])
try:
    print(gato2["color"])
except KeyError:
    print("La llave no existe")

imprimir_linea()
# Mostrar los valores
print(gato.values())
# Iterar sobre los valores
for value in gato.values():
    print(value)

imprimir_linea()
# Mostrar las claves
print(gato.keys())
# Iterar sobre los valores
for key in gato.keys():
    print(key)

imprimir_linea()

# Mostrar ambos valores
print(gato.items())
# Iterar sobre ambos valores
for k, v in gato.items():
    print(f"{k}: {v}")

imprimir_linea()

# Existe una llave
print("nombre" in gato)
print("last" in gato)
imprimir_linea()

# Existe un valor
print("blue" in gato.values())
print("red" in gato.values())
