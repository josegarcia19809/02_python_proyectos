bono = 0
ventas = float(input("Dame el total de ventas de cada día: "))
if ventas > 50000:
    bono = 500.00

print(f"Tu bono es de ${bono:,.2f}")
