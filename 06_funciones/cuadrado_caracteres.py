# cuadrado_caracteres.py

def cuadrado_de_caracteres(lado, caracter):
    for i in range(lado):
        for j in range(lado):
            print(caracter, end="")
        print()


def main():
    cuadrado_de_caracteres(6, "#")
    print()
    cuadrado_de_caracteres(3, "*")


main()
