"""
Ejercicio de iteración de listas
Te he proporcionado una lista llamada sonidos. Se ve así:
sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
Escribe código que recorra la lista y agregue todas las cadenas para que forme una cadena
combinada grande (no agregues espacios entre ellas). La cadena combinada también debe
estar en MAYÚSCULAS. Guarda el resultado en una variable llamada result.
"""
sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]

# Define your code below:
result = ""
for sound in sounds:
    result += sound.upper()

print(result)