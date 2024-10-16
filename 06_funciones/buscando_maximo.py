# buscando_maximo.py

# Define una función que determine y devuelva el mayor de 3 valores
def maximo(valor1, valor2, valor3):
    valor_maximo = valor1
    if valor2 > valor_maximo:
        valor_maximo = valor2
    if valor3 > valor_maximo:
        valor_maximo = valor3

    return valor_maximo


def main():
    # evalua el máximo de 3 enteros
    print(f"El máximo es {maximo(12, 27, 36)}")
    # evalua el máximo de 3 flotantes
    print(f"El máximo es {maximo(12.3, 45.6, 9.7)}")
    # evalua el máximo de 3 05_cadenas
    print(f"El máximo es {maximo('yellow', 'red', 'orange')}")


main()
