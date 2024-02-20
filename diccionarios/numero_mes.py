dias_x_mes = {
    'Enero': 1,
    'Febrero': 2,
    'Marzo': 3,
    'Abril': 4,
    'Mayo': 5,
    'Junio': 6,
    'Julio': 7,
    'Agosto': 8,
    'Septiembre': 9,
    'Octubre': 10,
    'Noviembre': 11,
    'Diciembre': 12
}

# Acceder a los nombres de las claves
for mes in dias_x_mes.keys():
    print(mes, end=' ')
print()
# Acceder a los valores
for dias in dias_x_mes.values():
    print(dias, end=' ')

print("\nMeses ordenados:")
# Se pueden ordenar las claves usando el método sorted
for nombre_mes in sorted(dias_x_mes.keys()):
    print(nombre_mes, end=' ')
