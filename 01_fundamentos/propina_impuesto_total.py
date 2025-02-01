# Este programa calculará el impuesto del cargo de la comida, de la propina
# y el monto total
print("-" * 100)
print("***************Factura del restaurante*****************")
cargo_por_comida = float(input("Ingresa el cargo por la comida: "))
impuesto = cargo_por_comida * (7 / 100)
propina = (cargo_por_comida + impuesto) * (18 / 100)
total = cargo_por_comida + impuesto + propina

print(f"El cargo por la comida es ${cargo_por_comida}")
print(f"El monto del impuesto es ${impuesto}")
print(f"El monto de la propina es ${propina}")
print(f"El monto total es ${total}")
