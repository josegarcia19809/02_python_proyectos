# Programa para saber si un número está dentro de un rango

print("-" * 100)
x = float(input('Ingrese el valor de la x: '))

if x < 20 or x > 40:
    print(f"{x} está fuera del rango 👍🏼")
else:
    print(f"{x} NO está fuera del rango 👎🏼")