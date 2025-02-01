# venta_sin_validacion.py
print("-" * 100)

# Este programa calcula los precios minoristas.
MARGEN = 2.5  # El porcentaje de margen
hay_otro_elemento = 's'  # Variable para controlar el bucle.

# Procesar uno o más elementos.
while hay_otro_elemento == 's' or hay_otro_elemento == 'S':
    # Obtener el costo mayorista del artículo.
    venta_al_por_mayor = float(input("Ingresa el costo mayorista del artículo: "))
    # Calcular el precio de venta al público.
    precio_minorista = venta_al_por_mayor * MARGEN
    # Mostrar el precio de venta al público.
    print(f'Precio de venta al público: ${precio_minorista:,.2f}')
    # ¿Hacer esto de nuevo?
    hay_otro_elemento = input('¿Tiene otro elemento? ' + '(Ingrese S para decir sí): ')
