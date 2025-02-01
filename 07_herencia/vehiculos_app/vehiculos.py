# La clase de Vehiculo contendrá datos generales
# sobre todos los vehículos en un inventario

class Vehiculo:
    # Constructor
    def __init__(self, marca, modelo, kilometraje, precio) -> None:
        self.__marca = marca
        self.__modelo = modelo
        self.__kilometraje = kilometraje
        self.__precio = precio

    # Métodos set y get para cada atributo
    def set_marca(self, marca):
        self.__marca = marca

    def get_marca(self):
        return self.__marca

    def set_modelo(self, modelo):
        self.__modelo = modelo

    def get_modelo(self):
        return self.__modelo

    def set_kilometraje(self, kilometraje):
        self.__kilometraje = kilometraje

    def get_kilometraje(self):
        return self.__kilometraje

    def set_precio(self, precio):
        self.__precio = precio

    def get_precio(self):
        return self.__precio


# La clase Automovil representa un carro.
# Es una subclase de la clase Vehiculo
class Automovil(Vehiculo):
    # Constructor
    def __init__(self, marca, modelo, kilometraje, precio, puertas) -> None:
        super().__init__(marca, modelo, kilometraje, precio)
        self.__puertas = puertas

    # Métodos set y get
    def set_puertas(self, puertas):
        self.__puertas = puertas

    def get_puertas(self):
        return self.__puertas


# La clase Camioneta representa un vehiculo con tracción
# Es una subclase de la clase Vehiculo
class Camioneta(Vehiculo):
    # Constructor
    def __init__(self, marca, modelo, kilometraje, precio, tipo_traccion) -> None:
        super().__init__(marca, modelo, kilometraje, precio)
        self.__tipo_traccion = tipo_traccion

    # Métodos set y get
    def set_tipo_traccion(self, tipo_traccion):
        self.__tipo_traccion = tipo_traccion

    def get_tipo_traccion(self):
        return self.__tipo_traccion
