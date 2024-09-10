import os

os.system("clear")


# El siguiente programa calcula la sventas totales
# de una empresa durante un periodo de tiempo
# leyendo las cifras de ventas diarias como
# entrada y calculando un total acumulado a
# medida que se recopilan

# Se pedirán ventas para 5 días
# Lunes: 60.00
# Martes: 40.00
# Miércoles: 35.00
# Jueves: 15.00
# Viernes: 50.00

# Total: $200.00

total_ventas = 0 # Acumulador
dias = int(input("¿Para cuántos días tienes cifras de ventas? "))

# Obtener las ventas de cada día y acumular un total
for contador in range(1, dias+1):
    ventas = float(input(f"Ventas del día {contador}: "))
    total_ventas = total_ventas + ventas
    print(total_ventas)
    
# Mostrar la venta total
print(f"Ventas totales: ${total_ventas:.2f}") 
