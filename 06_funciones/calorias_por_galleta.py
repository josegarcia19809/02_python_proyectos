# calorias_por_galleta.py
# import os
# os.system("clear")
# Una bolsa de galletas contiene 40 galletas. La información de la bolsa dice que
# tiene 10 porciones. Cada porción tiene 300 calorías. Una persona dice que si ha
# comido más de 500 calorías está en riesgo. Escribir 2 funciones que manden mensajes
# al respecto.
# esta_en_riesgo()
# no_esta_en_riesgo()
# El programa preguntará cuántas galletas ha comido


def esta_en_riesgo():
    print("Cuidate. Ya casi ☠️")


def no_esta_en_riesgo():
    print("Todo bien. 👍🏼")


def main():
    galletas = int(input("¿Cuántas galletas te comiste? "))
    calorias_por_galleta = 75
    calorias_consumidas = galletas * calorias_por_galleta

    # Verificar riesgo
    if calorias_consumidas > 500:
        esta_en_riesgo()
    else:
        no_esta_en_riesgo()


main()
