# Programa para determinar si una persona recibira un préstamo con tasa baja de interés

# Obtenga el salario anual del usuario.
salario = float(input("¿Cuál es su salario anual? "))
# Obtenga el número de años del usuario en el trabajo actual
anios_en_trabajo = int(input("¿Cuántos años ha estado en su trabajo actual? "))

# Determinar si el usuario califica para el préstamo
if salario >= 50000 and anios_en_trabajo >= 2:
    print(f"Calificas para el prestamo")
else:
    print("¡No calificas!")
