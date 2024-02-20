print("-"*100)
traductor = {
    "gato": "cat",
    "perro": "dog",
    "caballo": "horse"
}

# Imprimir valores según la clave.
print(traductor["perro"])

# Iterar sobre todos los elementos del diccionario usando la clave, llave o key
print()

for key in traductor.keys():
    print(key, "->", traductor[key])

print()

# Se utiliza una tupla para conseguir los elementos de un diccionario
for spanish, english in sorted(traductor.items()):
    print(spanish, "->", english)

print()

# Modificar un valor de un diccionario
traductor["gato"] = "Miau"
print(traductor)


