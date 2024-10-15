# sumando_dos_valores.py
import os

os.system("clear")


# Este programa usa una función que recibe 2 argumentos


# La función mostrar_suma recibe 2 argumentos y muestra su suma
def mostrar_suma(num1: int, num2: int):
    suma = num1 + num2
    print(f"La suma es {suma}")


def main():
    mostrar_suma(12, 45)
    valor_1 = 2
    valor_2 = 3
    mostrar_suma(valor_1, valor_2)


main()
