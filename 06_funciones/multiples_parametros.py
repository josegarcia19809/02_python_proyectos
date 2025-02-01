# multiples_parametros.py

# Este programa obtendrá el máximo valor de 3 valores

def maximo(valor1, valor2, valor3):
    """Retorna el máximo de 3 valores"""
    valor_maximo = valor1
    if valor2 > valor_maximo:
        valor_maximo = valor2
    if valor3 > valor_maximo:
        valor_maximo = valor3

    return valor_maximo


def main():
    print(f"El máximo es {maximo(12, 27, 36)}")  # números enteros
    print(f"El máximo es {maximo(12.3, 45.6, 9.7)}")  # números flotantes
    print(f"El máximo es {maximo('yellow', 'red', 'orange')}")  # cadenas


main()
