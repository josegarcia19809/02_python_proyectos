# La clase Celular contiene datos sobre un teléfono celular.

class Celular:
    # El método __init__ inicializa los atributos.
    def __init__(self, fabricante, modelo, precio):
        self.__fabricante = fabricante
        self.__modelo = modelo
        self.__precio_minorista = precio

    # El método set_fabricante acepta un argumento para el fabricante del teléfono.
    def set_fabricante(self, fabricante):
        self.__fabricante = fabricante

    # El método set_modelo acepta un argumento para el número de modelo del teléfono.
    def set_modelo(self, modelo):
        self.__modelo = modelo

    # El método set_precio_minorista acepta un argumento para el precio minorista
    # del teléfono.
    def set_precio_minorista(self, precio):
        self.__precio_minorista = precio

    # El método get_fabricante devuelve el fabricante del teléfono.
    def get_fabricante(self):
        return self.__fabricante

    # El método get_modelo devuelve el número de modelo del teléfono.
    def get_modelo(self):
        return self.__modelo

    # El método get_precio_minorista devuelve el precio minorista del teléfono.
    def get_precio_minorista(self):
        return self.__precio_minorista
