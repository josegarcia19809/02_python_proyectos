# Creado por José L. García 2 de septiembre 2024
# Programa para determinar si una persona recibirá un préstamo
# con tasa baja de interés

print("Préstamos con tasa baja de interés")

# Obtener el salario anual del usuario
salario = float(input("Dame tu salario anual: "))

# Obtener el número de años del usuario en el trabajo actual
anios_en_trabajo = int(input("Número de años trabajados: "))

# Determinar si el usuario califica para el préstamo
if salario >= 50_000 or anios_en_trabajo >= 2:
    print("Calificas para el préstamo")
else:
    print("No calificas!")