def sumar(num1: int, num2: int) -> int:
    resultado = num1 + num2
    return resultado


def main():
    numero1 = int(input("Dame primer número: "))
    numero2 = int(input("Dame segundo número: "))
    respuesta = sumar(numero1, numero2)
    print(f"La respuesta es {respuesta}")


main()
