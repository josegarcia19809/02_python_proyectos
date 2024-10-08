# Calcular el salario bruto según las horas trabajadas

def calcular_salario_bruto():
    horas_trabajadas = int(input("Dime cuántas horas trabajaste: "))
    salario_por_hora = float(input("Dime tu salario por hora: "))
    salario_bruto = horas_trabajadas * salario_por_hora
    print(f"El salario bruto es ${salario_bruto}")


def main():
    calcular_salario_bruto()


main()
