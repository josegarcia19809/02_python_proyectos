dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
phone_numbers = {'jefe': 5551234567, 'Suzy': 22657854310}
empty_dictionary = {}

# Imprimir valores aquí.
print(dictionary["perro"])
print(phone_numbers["Suzy"])

print()

for key in dictionary.keys():
    print(key, "->", dictionary[key])

print()
# Se utiliza una tupla para conseguir los elementos de un diccionario
for spanish, french in sorted(dictionary.items()):
    print(spanish, "->", french)

print()

# Modificar un valor de un diccionario
dictionary["gato"]="Miau"
print(dictionary)

print()
pol_esp_dictionary = {
    "zamek": "castillo",
    "woda": "agua",
    "gleba": "tierra"
    }

for item in pol_esp_dictionary:
    print(item)

# salida: zamek
#         woda
#         gleba

