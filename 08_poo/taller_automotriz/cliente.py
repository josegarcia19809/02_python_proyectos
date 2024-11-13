# Clase Cliente

class Cliente:
    def __init__(self, nombre, direccion, telefono):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_direccion(self, direccion):
        self.__direccion = direccion

    def set_telefono(self, telefono):
        self.__telefono = telefono

    def get_nombre(self):
        return self.__nombre

    def get_direccion(self):
        return self.__direccion

    def get_telefono(self):
        return self.__telefono
