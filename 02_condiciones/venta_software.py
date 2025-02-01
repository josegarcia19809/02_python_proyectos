# import os
#
# os.system("clear")
print("-"*100)
print("Venta de software")
print("Los siguientes descuentos aplican según los paquetes comprados")
print("Cantidad\tDescuento")
print("10–19\t\t20%")
print("20–49\t\t30%")
print("50–99\t\t40%")
print("100 o más\t50%")
print()

PRECIO = 99.00
cantidad = int(input("Dame la cantidad de paquetes: "))

porcentaje_descuento = 0
if cantidad >= 10 and cantidad <= 19:
    porcentaje_descuento = 20
elif cantidad >= 20 and cantidad <= 49:
    porcentaje_descuento = 30
elif cantidad >= 50 and cantidad <= 99:
    porcentaje_descuento = 40
elif cantidad >= 100:
    porcentaje_descuento = 50

subtotal = cantidad * PRECIO
descuento = subtotal * (porcentaje_descuento / 100)
total_venta = subtotal - descuento
print(f"Descuento aplicado: {porcentaje_descuento}%")
print(f"El total de la venta es ${total_venta:,.2f}")
