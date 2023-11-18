numeros = [1, 2, 3]

# Multiplicar cada elemento por 10
print([num * 10 for num in numeros])

# Sacar la mitad de cada número y guardar en nueva lista
numeros_mitad = [num / 2 for num in numeros]
print(numeros_mitad)

# Convertir cada letra en mayúscula y guardar en nueva lista
nombre = "José"
caracteres = [letra.upper() for letra in nombre]
print(caracteres)

# Poner cada nombre con su inicial en mayúscula
amigos = ["pedro", "rox", "carolina"]
amigos_may = [amigo.capitalize() for amigo in amigos]
print(amigos_may)

# Multiplicar varios elementos [1,2,3,4,5] por 5
print([num * 5 for num in range(1, 6)])

# Convertir valores numéricos a cadena
numeros = [1, 2, 3]
print([str(num) for num in numeros])

# Concatenar un numero a una cadena: ['imagen1', 'imagen2', 'imagen3']
print(["imagen" + str(num) for num in numeros])
