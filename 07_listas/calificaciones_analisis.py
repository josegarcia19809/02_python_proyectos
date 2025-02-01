# calificaciones_analisis.py


def imprimir_linea():
    print("-" * 20)


# Pedir el número de asignaturas
num_asignaturas = int(input("Dame el número de asignaturas: "))

# Crear las 2 listas
asignaturas = [""] * num_asignaturas
calificaciones = [0] * num_asignaturas

# Pedir los datos
for index in range(num_asignaturas):
    asignaturas[index] = input(f"Asignatura {index + 1}: ")
    calificaciones[index] = int(input("Calificación? "))

print(asignaturas)
print(calificaciones)
imprimir_linea()

print("Materias no aprobadas")
for index in range(num_asignaturas):
    if calificaciones[index] < 70:
        print(f"{asignaturas[index]}: {calificaciones[index]}")

print("Materias aprobadas")
for index in range(num_asignaturas):
    if calificaciones[index] >= 70:
        print(f"{asignaturas[index]}: {calificaciones[index]}")

# Calcular el promedio
total = 0
for index in range(num_asignaturas):
    total = total + calificaciones[index]

if num_asignaturas > 0:
    promedio = total / num_asignaturas
    print(f"Promedio: {promedio}")

imprimir_linea()
