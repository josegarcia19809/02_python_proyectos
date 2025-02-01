# Programa para obtener promedios

num_estudiantes = int(input("¿Cuántos estudiantes son? "))
num_calificaciones = int(input("¿Cuántas calificaciones son por estudiante? "))

# Procesa a todos los estudiantes
for estudiante in range(1, num_estudiantes + 1):
    total_por_estudiante = 0  # establece el acumulador en cero.
    # Pide todas las calificaciones de un estudiante.
    print(f"Estudiante número {estudiante}")
    print("-" * 40)
    for examen in range(1, num_calificaciones + 1):
        puntuacion = int(input(f"Ingresa puntuación {examen}: "))
        total_por_estudiante += puntuacion

    # Calcula y muestra el promedio por Estudiante.
    promedio_por_estudiante = total_por_estudiante / num_calificaciones
    print(f"El promedio del estudiante {estudiante} es {promedio_por_estudiante:.1f}")
    print()
