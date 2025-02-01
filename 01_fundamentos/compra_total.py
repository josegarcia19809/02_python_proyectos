# Este programa mostrará el total de una venta de cinco artículos junto con su impuesto.

print("COMPRA TOTAL")
# Pedir los precios de los cinco productos
precio1 = float(input("Dame el precio del producto 1: "))
precio2 = float(input("Dame el precio del producto 2: "))
precio3 = float(input("Dame el precio del producto 3: "))
precio4 = float(input("Dame el precio del producto 4: "))
precio5 = float(input("Dame el precio del producto 5: "))

# Calcular el subtotal
subtotal = precio1 + precio2 + precio3 + precio4 + precio5

# Calcular el impuesto
impuesto = subtotal * (15 / 100)

# Calcular el total de la venta
total = subtotal + impuesto

# Mostrar en pantalla el subtotal, impuesto y total
print()
print(f"El subtotal es ${subtotal}")
print(f"El impuesto es ${impuesto}")
print(f"El total de la venta es ${total}")
