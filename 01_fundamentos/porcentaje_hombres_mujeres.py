# Este programa calcula el porcentaje de hombres y mujeres en una clase
print("-" * 100)
print("Porcentaje de hombres y mujeres en una clase")

# Pedir cantidades de hombres y mujeres
cantidad_hombres = int(input("Cantidad de hombres registrados: "))
cantidad_mujeres = int(input("Cantidad de mujeres registradas: "))

# Calcular el total de personas
total = cantidad_hombres + cantidad_mujeres

# Calcular los porcentajes
porcentaje_hombres = cantidad_hombres * 100 / total
porcentaje_mujeres = cantidad_mujeres * 100 / total

# Mostrar los porcentajes de hombres y mujeres
print(f"Porcentaje de hombres: {porcentaje_hombres}%")
print(f"Porcentaje de mujeres: {porcentaje_mujeres}%")
