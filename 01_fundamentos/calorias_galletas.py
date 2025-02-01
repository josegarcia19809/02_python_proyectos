# Este programa calcula el número de calorías consumidas a partir del
# número de galletas que se comieron
print("-" * 100)
print("Calorías consumidas")
# Obtener la cantidad de galletas consumidas
galletas_consumidas = int(input("Dime cuántas galletas te comiste: "))
galletas_por_bolsa = 40
porciones_por_bolsa = 10
calorias_por_porcion = 300

# Calcular las calorías totales consumidas
calorias_por_bolsa = porciones_por_bolsa * calorias_por_porcion
calorias_por_galleta = calorias_por_bolsa / galletas_por_bolsa
calorias_consumidas = calorias_por_galleta * galletas_consumidas

# Mostrar las calorías totales consumidas
print(f"Consumiste {calorias_consumidas} calorías")