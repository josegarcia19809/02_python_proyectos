# Created by: Ing. José Luis García Morales on 30 de junio de 2020, 11:14

# Comprobación positivos o negativos
# En este ejercicio, [x, y] son dos variables aleatorias.
# El código en la parte superior del archivo los asigna aleatoriamente
# (aprenderemos cómo funciona más adelante).
# Por ahora, solo déjalo en paz :)
# #
# Si ambos son números positivos, escriba "ambos positivos".
# Si ambos son negativos, imprima "ambos negativos".
# De lo contrario, díganos cuál es positivo y cuál es negativo,
# por ejemplo. "x es positivo, y es negativo"


# NO TOUCHING==NO TOUCHING==NO TOUCHING==NO TOUCHING #| \
from random import randint  # |  \

x = randint(-100, 100)  # |   \
while x == 0:  # asegurarse de que x no sea cero     #|    \
    x = randint(-100, 100)  # |     NO TOUCHING!!!!!! (please)
y = randint(-100, 100)  # |    /
while y == 0:  # asegurarse de que y no sea cero     #|   /
    y = randint(-100, 100)  # |  /
# NO TOUCHING==NO TOUCHING==NO TOUCHING==NO TOUCHING #| /

print(f'x: {x}, y: {y}')

# ESCRIBE TU CÓDIGO AQUI vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
if x > 0 and y > 0:
    print("Ambos positivos")
elif x < 0 and y < 0:
    print("Ambos negativos")
elif x > 0 and y < 0:
    print("x es positivo, y es negativo")
elif x < 0 and y > 0:
    print("y es positivo, x es negativo")
# YOUR CODE GOES HERE ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
