# calificaciones6_7.py

# Se piden seis calificaciones con decimales, se desea saber cuántos alumnos tienen
# entre 6.0 y 7.0 de calificación. Usar la instrucción while

# 7.0   6.4     5.0     10.0    2.2     1.0
# Si    si      no      no      no      no

# Hubo 2 Calificaciones que están entre 6.0 y 7.0

i = 1
total_calificaciones_6_y_7 = 0

while i <= 6:
    calificacion = float(input(f"Dame calificacion {i}: "))

    if 6.0 <= calificacion <= 7.0:
        total_calificaciones_6_y_7 += 1

    i = i + 1

print(f"Total de alumnos con calificacion entre 6 y 7: {total_calificaciones_6_y_7}")
