print("-" * 100)
# Este programa demuestra que el usuario puede especificar el tamaño de una lista

num_examenes = int(input("¿Cuántos exámenes se aplicaron?: "))

# Crear la lista con un tamaño de acuerdo al número de exámenes
calificaciones = [0] * num_examenes

# Pedir cada una de las calificaciones
for i in range(num_examenes):
    calificaciones[i] = int(input(f"Introduce la calificación {(i + 1)}: "))

# Mostrar las calificaciones
print("Las calificaciones de los exámenes son: ")
for calificacion in calificaciones:
    print(calificacion, end=" ")
