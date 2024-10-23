# Este programa usa una lista de calificaciones

calificaciones = [10.0, 9.5, 8.2, 7.3, 4.5]

print("Las calificaciones son: ")
for calificacion in calificaciones:
    print(calificacion)

print("-" * 30)

# Sacar el total de la suma de todas las calificaciones
total = 0
for calificacion in calificaciones:
    total = total + calificacion

print(f"Suma total: {total}")
print("-" * 30)

# Sacar el promedio
promedio = total / len(calificaciones)
print(f"Promedio: {promedio}")
print("-" * 30)

# Mostrar las calificaciones solo de aquellos que aprobaron.
print("Calificaciones de solo aquellos que aprobaron")
for calificacion in calificaciones:
    if calificacion >= 6.0:
        print(calificacion)

print("-" * 30)
# Mostrar las calificaciones solo de aquellos que están entre 7.0 y 9.0
print("Calificaciones solo de aquellos que están entre 7.0 y 9.0")
for calificacion in calificaciones:
    if 7.0 <= calificacion <= 9.0:
        print(calificacion)
