# paises.py

# Crear una lista de países
paises = ["Argentina", "México", "Estados Unidos", "Canada", "España", "Francia"]

print(paises)

print(paises[0])
print(paises[1])
print(paises[2])
print(paises[3])
print(paises[4])
print(paises[5])
print()

# Longitud de una lista
print(f"Número de países en la lista: {len(paises)}")
print()

# Cambiar el elemento en el índice 3. En lugar de Canada, será Brasil
paises[3] = "Brasil"
print(paises)

# Agregar un país
nuevo_pais = input("Dame nombre del país: ")
paises.append(nuevo_pais)
print(paises)
print()

# Mostrar todos los paises con un for
for pais in paises:
    print(pais)

print()
# Agregar otros 5 países
for i in range(5):
    nuevo_pais = input("Escribe país: ")
    paises.append(nuevo_pais)

print()
# Mostrar el número de país
for index in range(len(paises)):
    print(f"{index + 1}: {paises[index]}")

# print(paises[100]) # ERROR
