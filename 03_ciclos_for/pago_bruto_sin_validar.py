# pago_bruto_sin_validar
print("-"*100)
# Este programa muestra el salario bruto.

# Obtener el número de horas trabajadas.
horas = int(input("Ingresa las horas trabajadas esta semana: "))

# Obtener la tarifa de pago por hora.
tarifa_pago = float(input("Ingresa la tarifa de pago por hora: "))

# Calcular el salario bruto.
pago_bruto = horas * tarifa_pago

# Mostrar el salario bruto.
print(f"Salario bruto: ${pago_bruto:,.2f}")
