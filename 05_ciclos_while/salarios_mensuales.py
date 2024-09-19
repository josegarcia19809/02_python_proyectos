# Este programa recibe seis sueldos mensuales de un empleado, calculará tanto el
# ingreso total como el promedio mensual. Mostrará ambos resultados

print("-" * 100)
print("Programa para calcular el ingreso total de un empleado y su sueldo promedio")

ingreso_total = 0

sueldo = float(input("Ingresa sueldo 1: "))
ingreso_total = ingreso_total + sueldo

sueldo = float(input("Ingresa sueldo 2: "))
ingreso_total = ingreso_total + sueldo

sueldo = float(input("Ingresa sueldo 3: "))
ingreso_total = ingreso_total + sueldo

sueldo = float(input("Ingresa sueldo 4: "))
ingreso_total = ingreso_total + sueldo

sueldo = float(input("Ingresa sueldo 5: "))
ingreso_total = ingreso_total + sueldo

sueldo = float(input("Ingresa sueldo 6: "))
ingreso_total = ingreso_total + sueldo

sueldo_promedio = ingreso_total / 6.0

print(f"El ingreso total es ${ingreso_total}")
print(f"El sueldo mensual promedio es ${sueldo_promedio}")

# 100   200     300     400     500     600
# ingreso_total: 2100
# sueldo_promedio: 350
