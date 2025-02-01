# ajustador_ingredientes_galletas.py

# Programa para calcular la cantidad de tazas de varios
# ingredientes para producir una cantidad especifica de galletas
print("-" * 100)
print("*****Ajustador de ingredientes para producir galletas*****")
# 1. Pedir el número de galletas a producir.
galletas_requeridas = int(input("Dime cuántas galletas se quieren producir: "))

# 2. Calcular el número de tazas de azúcar requeridas para dicha cantidad de galletas
tazas_azucar_una_galleta = 1.5 / 48
tazas_azucar_requeridas = tazas_azucar_una_galleta * galletas_requeridas

# 3. Calcular el número de tazas de mantequilla requeridas para dicha cantidad de galletas
tazas_mantequilla_una_galleta = 1.0 / 48
tazas_mantequilla_requeridas = tazas_mantequilla_una_galleta * galletas_requeridas

# 4. Calcular el número de tazas de harina requeridas para dicha cantidad de galletas
tazas_harina_una_galleta = 2.75 / 48
tazas_harina_requeridas = tazas_harina_una_galleta * galletas_requeridas

# 5. Mostrar el número de tazas requeridas por ingrediente
print(f"Para producir {galletas_requeridas} galletas se requieren: ")
print(f"Tazas de azucar: {tazas_azucar_requeridas}")
print(f"Tazas de mantequilla: {tazas_mantequilla_requeridas}")
print(f"Tazas de harina: {tazas_harina_requeridas}")
