# Este programa calcula el salario total de cada uno de los baristas de Megan

def imprimir_linea():
    print("-" * 20)

# NUM_EMPLEADOS es un valor constante que se usará para determinar
# el tamaño de la colección
NUM_EMPLEADOS = 6

# Crear un arreglo de horas trabajadas para cada uno de los empleados
horas = [0] * NUM_EMPLEADOS # [0, 0, 0, 0, 0, 0]

# Pedir las horas trabajadas de cada empleado
for index in range(NUM_EMPLEADOS):
    horas[index] = int(input(f"Horas del empleado {index + 1}: "))

# Pedir el pago por hora
print()
pago_hora = float(input("Dame el pago por hora: "))
print()

# Calcular el salario de cada trabajador
for index in range(NUM_EMPLEADOS):
    pago_total = horas[index] * pago_hora
    print(f"Pago total para empleado {index + 1} es ${pago_total:,.2f}")

imprimir_linea()
