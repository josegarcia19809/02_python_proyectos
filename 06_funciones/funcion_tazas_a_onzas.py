# funcion_tazas_a_onzas.py

# Tu amigo Michael dirige una empresa de catering (servicio de comidas). Algunos de
# los ingredientes que requieren sus recetas se miden en tazas. Sin embargo, cuando
# va al supermercado a comprar esos ingredientes, solo se venden por onzas líquidas.
# Él te ha pedido que escribas un programa simple que convierta tazas en
# onzas líquidas.

# En una taza hay aproximadamente 8.79 onzas

def tazas_a_onzas(tazas: float):
    onzas = tazas * 8.79
    print(f"{tazas} tazas es igual a {onzas:,.2f} onzas líquidas")


def intro():
    print("Este programa convierte medidas de tazas a onzas líquidas")
    print("Para su referencia, la formula es: ")
    print("\t\t1 taza = 8.79 onzas líquidas")
    print()


def main():
    intro()

    # Pide el número de tazas
    numero_tazas = float(input("---Ingresa el número de tazas: "))

    tazas_a_onzas(numero_tazas)


main()

# Prueba
# tazas_a_onzas(3) # 26.37
# tazas_a_onzas(5) # 43.95