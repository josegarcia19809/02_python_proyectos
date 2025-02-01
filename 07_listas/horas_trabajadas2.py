# Este programa muestra una lista que se procesa con ciclos

print("-" * 100)
EMPLEADOS = 3  # Numero de empleados
horas = [0] * EMPLEADOS  # Lista de horas

print(f"Ingresa las horas trabajadas por los {EMPLEADOS} empleados")

# Lee las horas trabajadas por cada empleado
for index in range(EMPLEADOS):
    horas[index] = int(input(f"Empleado {index + 1}: "))

# Muestra los valores almacenados.
print("Las horas que ingresaste son: ")
for index in range(EMPLEADOS):
    print(horas[index])
