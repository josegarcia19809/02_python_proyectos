print("Departamento de becas")

promedio = float(input("Ingresa tu promedio: "))
salario = float(input("Ingresa tu salario mensual: "))

if promedio >= 8.0 or salario <= 2000:
    print("Tienes beca")
else:
    print("No tienes beca")