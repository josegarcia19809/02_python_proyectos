from contacto import Contacto
import os

os.system("clear")


def main():
    # Pedir los datos
    nombre = input("Dame nombre del contacto: ")
    telefono = input("Dame teléfono del contacto: ")
    email = input("Dame email del contacto: ")

    # Crear una instancia
    primer_contacto = Contacto(nombre, telefono, email)

    # Obtener el nombre del contacto creado
    print(f"Nombre del contacto: {primer_contacto.get_nombre()}")

    # Cambiar el teléfono
    nuevo_telefono = input("Dame nuevo teléfono: ")
    primer_contacto.set_telefono(nuevo_telefono)

    # Mostrar todos los datos del contacto
    print(primer_contacto)


if __name__ == "__main__":
    main()
