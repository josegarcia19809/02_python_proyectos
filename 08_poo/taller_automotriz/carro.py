# Clase Carro

class Carro:
    def __init__(self, marca, modelo, anio):
        self.__marca = marca
        self.__modelo = modelo
        self.__anio = anio

    def set_marca(self, marca):
        self.__marca = marca

    def set_modelo(self, modelo):
        self.__modelo = modelo

    def set_anio(self, anio):
        self.__anio = anio

    def get_marca(self):
        return self.__marca

    def get_modelo(self):
        return self.__modelo

    def get_anio(self):
        return self.__anio
