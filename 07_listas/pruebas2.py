calificaciones = [100, 80, 50, 10, 90]
num_asignaturas = len(calificaciones)

for index in range(num_asignaturas):
    if calificaciones[index] < 70:
        print(f"{calificaciones[index]}")

print()
for index in range(num_asignaturas):
    if calificaciones[index] >= 70:
        print(f"{calificaciones[index]}")

total = 0
for index in range(num_asignaturas):
    total = total + calificaciones[index]

if num_asignaturas > 0:
    promedio = total / num_asignaturas
    print(f"Promedio: {promedio}")

temperaturas = [98, 87, 92, 79, 85]

codigos = ['m', 'u', 'e', 's', 't', 'r', 'a']

valoresx = [1.3, 3.2, 6.4, 7.8, 45.2, 12.0, 3.8]

kilometros = [8, 7, 92, 9, 5]
