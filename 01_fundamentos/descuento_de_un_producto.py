# Programa que descuenta 10% a un producto, del cual se pide su precio.

print("PROGRAMA PARA CALCULAR UN DESCUENTO DEL 10% A UN PRODUCTO")
precio_inicial = float(input("Dime el precio del producto: "))

descuento = precio_inicial * 0.10
precio_con_descuento = precio_inicial - descuento

print(f"El precio con descuento es de {precio_con_descuento}")
