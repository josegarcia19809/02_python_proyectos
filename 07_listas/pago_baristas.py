# Este programa calcula el salario total de cada uno de los baristas de Megan

def imprimir_linea():
    print("-" * 20)


NUM_EMPLEADOS = 6

horas = [0] * NUM_EMPLEADOS

for index in range(NUM_EMPLEADOS):
    horas[index] = int(input(f"Horas del empleado {index + 1}: "))

print()
pago_hora = float(input("Dame el pago por hora: "))
print()

for index in range(NUM_EMPLEADOS):
    pago_total = horas[index] * pago_hora
    print(f"Pago total para empleado {index + 1} es ${pago_total:,.2f}")

imprimir_linea()
