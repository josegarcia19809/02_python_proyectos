# invertir_nombre_apellido.py

# Este programa mostrará cómo pasar 2 cadenas como argumentos a una función

def invertir_nombre(nombre: str, apellido: str):
    print(f"{apellido} {nombre}")


def main():
    nombre = input("Dame tu nombre: ")
    apellido = input("Dame tu apellido: ")

    print("Tu nombre invertido es:")
    invertir_nombre(nombre, apellido)


main()
