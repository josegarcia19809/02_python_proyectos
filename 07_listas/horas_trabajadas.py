# Este programa muestra los valores guardados en una lista de 3 elementos
print("-" * 100)
EMPLEADOS = 3  # Numero de empleados
horas = [0] * EMPLEADOS  # Lista de horas

print(f"Ingresa las horas trabajadas por los {EMPLEADOS} empleados")

# Lee las horas trabajadas por el empleado 1.
horas[0] = int(input("Empleado 1: "))

# Lee las horas trabajadas por el empleado 2.
horas[1] = int(input("Empleado 2: "))

# Lee las horas trabajadas por el empleado 3.
horas[2] = int(input("Empleado 3: "))

# Mostrar los valores almacenados
print("Las horas que ingresaste son: ")
print(horas[0])
print(horas[1])
print(horas[2])
