# Programa que mostrará la cantidad de clientes que prefieren bebidas energéticas
# y la cantidad de clientes que prefieran bebidas energéticas con sabor a cítricos.
print("-" * 100)
print("Consumo de bebidas energéticas.")
# Definir los datos de inicio
num_clientes = 15000
porcentaje_bebidas_energeticas = 18
porcentaje_sabor_citricos = 58
# Calcular los porcentajes de clientes
clientes_b_energeticas = num_clientes * (porcentaje_bebidas_energeticas / 100)
clientes_b_sabor_citricos = clientes_b_energeticas * (porcentaje_sabor_citricos / 100)
# Mostrar los totales de clientes que prefieren bebidas energéticas y
# los que compran con sabor a cítricos
print(f"Personas que compran bebidas energéticas: {clientes_b_energeticas}")
print(f"Los que compran con sabor a cítricos: {clientes_b_sabor_citricos}")
