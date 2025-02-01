# Crear una lista de países
# Se utilizarán algunas operaciones sobre esta lista
print("-" * 100)
# Considera la lista paises, que contiene seis elementos de tipo cadena
paises = ["Argentina", "México", "Estados Unidos", "Cánada", "España", "Francia"]

print(paises)  # imprime la lista

# Acceso a países por su índice
print(paises[0])
print(paises[1])
print(paises[2])
print(paises[3])
print(paises[4])
print(paises[5])

print("-" * 100)
# Longitud de una lista
print(f"Número de países en la lista: {len(paises)}")
print("-" * 100)
# Cambiar el elemento que está en el índice 3
# En lugar de Cánada será Brasil
paises[3] = "Brasil"
# Imprime los países
print(paises)

# Agregar un país ------> Holanda
nuevo_pais = input("Dame el nombre de un país: ")
paises.append(nuevo_pais)
print(paises)

# Mostrar todos los países con un for
for pais in paises:
    print(pais)

print()

# Agregando otros 5 países
for i in range(5):
    nuevo_pais = input("Escribe país: ")
    paises.append(nuevo_pais)

print()
# Mostrar el número de país
for index in range(len(paises)):
    print(f"{index + 1}: {paises[index]}")

print("-" * 100)
# Intentar acceder a un elemento fuera de rango
# print(paises[100])
