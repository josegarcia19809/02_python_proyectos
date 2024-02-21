# Tupla que guarda datos de un estudiante
# esta tupla se compone de dos cadenas y una lista
print("-"*100)
estudiante = ("Amanda", "Morales", [98, 75, 87])
print(estudiante)
# Imprimir el nombre
print(f"Nombre: {estudiante[0]}")
# Imprimir el apellido
print(f"Apellidos: {estudiante[1]}")
# Imprimir las calificaciones
print(f"Calificaciones: {estudiante[2]}")

# Imprimir las calificaciones una por una
print(f"Calificación 1: {estudiante[2][0]}")
print(f"Calificación 2: {estudiante[2][1]}")
print(f"Calificación 3: {estudiante[2][2]}")

# Cambiar ese 75 por un 85
estudiante[2][1] = 85
print(estudiante)

