# Creado por José L. García 2 de septiembre 2024
# Programa para calcular el aumento de un sueldo
# de acuerdo a su sueldo actual

sueldo  = float(input("Dame tu sueldo actual: "))
aumento = 0
nuevo_sueldo = 0

if sueldo <= 1500:
    aumento = sueldo * 0.20
    nuevo_sueldo = sueldo + aumento
else:
    aumento = sueldo * 0.15
    nuevo_sueldo = sueldo + aumento
    
print(f"Tu sueldo anterior era de {sueldo}")
print(f"Tu aumento fue de {aumento}")
print(f"Tu sueldo nuevo es de {nuevo_sueldo}")




