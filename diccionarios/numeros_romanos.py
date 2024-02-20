numeros_romanos = {'i': 1, 'ii': 2, 'iii': 3, 'v': 5, 'x': 100}  # Error a propósito
print(numeros_romanos)

# Accediendo a un valor asociado a una clave
print(numeros_romanos['v']) #Mostrará 5

#Actualizando un valor asociado a una clave
numeros_romanos['x'] = 10
print(numeros_romanos)

#Anexando un nuevo valor al diccionario
numeros_romanos['l'] = 50
print(numeros_romanos)

#Borrando un elemento asociado a una clave
del numeros_romanos['iii']
print(numeros_romanos)

#El método pop saca un elemento del diccionario y menciona el valor sacado
print(f"Sacando: {numeros_romanos.pop('x')}")
print(numeros_romanos)

# Intento de acceder a un elemento no existente
# print(numeros_romanos['iii'])
print(numeros_romanos.get('iii', 'iii no existe en el diccionario'))

# Probando si un diccionario contiene una determinada clave
print(f"¿Existe v en el diccionario? {'v' in numeros_romanos}")
print(f"¿Existe iii en el diccionario? {'iii' in numeros_romanos}")
print(f"¿No existe iii en el diccionario? {'iii' not in numeros_romanos}")
