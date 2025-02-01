# Programa para calcular promedios
import os
os.system("clear")
num_estudiantes=int(input("¿Cuántos estudiantes son? "))
num_calificaciones=int(input("¿Calificaciones por estudiante? "))

# Procesa a todos los estudiantes
for estudiante in range(1, num_estudiantes + 1):
    total_por_estudiante = 0
    print(f"Estudiante número {estudiante}")
    print("-"*40)
    for examen in range(1, num_calificaciones+1):
        puntuacion=int(input(f"Ingresa puntuacion {examen}: "))
        total_por_estudiante += puntuacion
        
    # Calcula y muestra el promedio por estudiante    
    promedio = total_por_estudiante / num_calificaciones
    print (f"El promedio del estudiante {estudiante} es: {promedio}")
        
    print()
        