# main.py
from vehiculos import Automovil, Camioneta


def prueba_automoviles():
    # Crear un objeto desde la clase Automovil
    # El carro es un Audi 2007 con 12,500 millas,
    # y su precio es de $21,500.00 y tiene cuatro puertas
    print("-" * 100)
    automovil_usado = Automovil("Audi", 2007, 12500, 21500, 4)

    # Mostrar los datos del Automóvil usado
    print("Datos del Automóvil usado")
    print(f"Marca: {automovil_usado.get_marca()}")
    print(f"Modelo: {automovil_usado.get_modelo()}")
    print(f"Kilometraje: {automovil_usado.get_kilometraje()}")
    print(f"Precio: {automovil_usado.get_precio()}")
    print(f"Número de puertas: {automovil_usado.get_puertas()}")


def prueba_camionetas():
    # Crear un objeto desde la clase Camioneta
    # La camioneta es una Toyota pickup 2002 con 40,000 millas 
    # su precio es de $12,000.00 y con una tracción en las cuatro ruedas

    camioneta_usada = Camioneta("Toyota", 2002, 40000, 12000, "4WD")
    print()
    print("-" * 40)
    print("Datos de la camioneta usada")
    print(f"Marca: {camioneta_usada.get_marca()}")
    print(f"Modelo: {camioneta_usada.get_modelo()}")
    print(f"Kilometraje: {camioneta_usada.get_kilometraje()}")
    print(f"Precio: {camioneta_usada.get_precio()}")
    print(f"Tipo de tracción: {camioneta_usada.get_tipo_traccion()}")


def main():
    prueba_automoviles()
    prueba_camionetas()


if __name__ == "__main__":
    main()

"""
Tarea: Crear la clase SUV
Hereda de Vehiculo y agrega el atributo pasajeros
Pone los métodos set y get faltantes

En main.py agrega el módulo para utilizar dicha clase.
Entregar para el lunes 16 octubre
"""
