# dias_por_mes.py
# Este programa muestra una lista que fue previamente inicializado con los días de
# cada mes.
# Enero se guarda en la posición 0; Febrero, en la 1; y asi sucesivamente
print("-"*100)
dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for indice in range(len(dias)):
    print(f"Mes {indice + 1} tiene {dias[indice]} días")

print()
for index, dia in enumerate(dias):
    print(f"Mes {index + 1} tiene {dia} dias")
