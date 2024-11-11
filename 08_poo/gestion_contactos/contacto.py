class Contacto:
    def __init__(self, nombre: str, telefono: str, email: str):
        self.__nombre = nombre
        self.__telefono = telefono
        self.__email = email

    # Métodos set y get
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_telefono(self, telefono):
        self.__telefono = telefono

    def set_email(self, email):
        self.__email = email

    def get_nombre(self) -> str:
        return self.__nombre

    def get_telefono(self) -> str:
        return self.__telefono

    def get_email(self) -> str:
        return self.__email

    def __str__(self) -> str:
        salida = f"Nombre: {self.__nombre}, "
        salida += f"teléfono: {self.__telefono}, "
        salida += f"email: {self.__email}"
        return salida
