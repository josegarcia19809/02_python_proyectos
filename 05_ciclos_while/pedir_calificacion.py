# pedir_calificacion.py

# Obtener la puntuación de un examen y validar de que sea positiva

puntuacion = int(input("Ingresa la puntuación del examen: "))

# Asegurarse de que no sea inferior a 0
while puntuacion < 0:
    print("ERROR: La puntuación no puede ser negativa.")
    puntuacion = int(input("Ingresa la puntuación correcta: "))

print(f"Puntuación válida: {puntuacion}")
