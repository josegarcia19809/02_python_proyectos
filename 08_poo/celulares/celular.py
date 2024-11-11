# La clase Celular contiene datos sobre un teléfono celular


class Celular:
    def __init__(self, fabricante, modelo, precio):
        self.__fabricante = fabricante
        self.__modelo = modelo
        self.__precio_minorista = precio

    # Agregar métodos set y get para cada atributo
    def set_fabricante(self, fabricante):
        self.__fabricante = fabricante

    def get_fabricante(self):
        return self.__fabricante

    def set_modelo(self, modelo):
        self.__modelo = modelo

    def get_modelo(self):
        return self.__modelo

    def set_precio_minorista(self, precio):
        self.__precio_minorista = precio

    def get_precio_minorista(self):
        return self.__precio_minorista
