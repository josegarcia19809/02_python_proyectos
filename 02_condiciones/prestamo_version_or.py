# Programa para determinar si una persona recibira un préstamo con tasa baja de interés

# Definiendo valores constantes
SALARIO_MINIMO = 50000
MINIMO_ANIOS = 2

print("Préstamos con tasa baja de interés")

# Obtener el salario y el número de años del usuario en el trabajo actual
salario = float(input("¿Cuál es su salario anual? "))
anios_en_trabajo = int(input("¿Cuántos años ha estado en su trabajo actual? "))

# Determinar si el usuario califica para el préstamo
if salario >= SALARIO_MINIMO or anios_en_trabajo >= MINIMO_ANIOS:
    print(f"Calificas para el préstamo")
else:
    print("¡No calificas!")
