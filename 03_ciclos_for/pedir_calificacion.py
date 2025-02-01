# pedir_calificacion.py
print("-" * 100)
# Obtener la puntuación de un examen.

puntuacion = int(input('Ingresa la puntuación del examen: '))

# Asegúrarse de que no sea inferior a 0 o mayor que 100.
while puntuacion < 0 or puntuacion > 100:
    print('ERROR: La puntuación no puede ser negativa')
    print('o mayor que 100')
    puntuacion = int(input('Ingrese la puntuación correcta: '))

print("Puntuación válida")
