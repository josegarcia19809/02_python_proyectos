# Programa que le pide al usuario que ingrese el peso de un paquete
# y luego muestre los costos de envío.
print("-"*100)
peso_paquete = float(input("Dame el peso del paquete: "))

tarifa = 0

if 0.0 <= peso_paquete <= 2.0:
    tarifa = 1.50
elif 2.0 < peso_paquete <= 6.0:
    tarifa = 3.00
elif 6.0 < peso_paquete <= 10.0:
    tarifa = 4.00
elif peso_paquete > 10.00:
    tarifa = 4.75

costos_envio = tarifa * peso_paquete
print(f"Costo de envío ${costos_envio:,.2f}")
