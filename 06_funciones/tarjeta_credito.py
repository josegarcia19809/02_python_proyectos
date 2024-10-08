# tarjeta_credito.py
# Este programa le pide al usuario que ingrese su salario anual y su
# calificación crediticia. Luego el programa determina si el usuario califica
# para una tarjeta de crédito.
# Se llama a una de las dos funciones:
# si_califica(),
# no_califica(), para mostrar un mensaje.
# Para calificar su salario anual debe ser por lo menos $2000 pesos y
# su calificación crediticia debe ser al menos 7 puntos

def si_califica():
    print("Felicidades 😁, si calificas para la tarjeta de credito")


def no_califica():
    print("Lo sentimos 😭, no calificas para la tarjeta de credito")


def main():
    salario_anual = float(input("¿Cuál es tu salario anual? "))
    calificacion_crediticia = int(
        input("En una escala del 1 al 10, ¿cuál sería tu calificación crediticia? "))

    # Verificar si califica
    if salario_anual >= 2000 and calificacion_crediticia >= 7:
        si_califica()
    else:
        no_califica()


main()
