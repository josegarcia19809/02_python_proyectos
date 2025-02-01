# Este programa prueba la clase Celular.
from celular import Celular


def main():
    print("-" * 100)
    # Pedir los datos del celular
    fabricante_c = input("Ingresa el fabricante: ")
    modelo_c = input("Ingresa el modelo del celular: ")
    precio_m = float(input("Ingresa el precio minorista del celular: "))

    # Crear una instancia de la clase Celular
    mi_celular = Celular(fabricante_c, modelo_c, precio_m)

    # Mostrar los datos ingresados
    print("Aquí están los datos que has ingresado")
    print(f"Fabricante: {mi_celular.get_fabricante()}")
    print(f"Número de modelo: {mi_celular.get_modelo()}")
    print(f"Precio minorista: ${mi_celular.get_precio_minorista():,.2f}")
    print()

    nuevo_precio_m = float(input("Ingresa el nuevo precio minorista del celular: "))
    mi_celular.set_precio_minorista(nuevo_precio_m)
    print()
    print("Aquí están los datos actualizados")
    print(f"Fabricante: {mi_celular.get_fabricante()}")
    print(f"Número de modelo: {mi_celular.get_modelo()}")
    print(f"Precio minorista: ${mi_celular.get_precio_minorista():,.2f}")


if __name__ == '__main__':
    main()
