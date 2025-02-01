# La clase CuentaAhorro representa una cuenta de ahorros
class CuentaAhorro:
    # Constructor
    def __init__(self, numero_cuenta, tasa_interes, balance):
        self.__numero_cuenta = numero_cuenta
        self.__tasa_interes = tasa_interes
        self.__balance = balance

    # Métodos set
    def set_numero_cuenta(self, numero_cuenta):
        self.__numero_cuenta = numero_cuenta

    def set_tasa_interes(self, tasa_interes):
        self.__tasa_interes = tasa_interes

    def set_balance(self, balance):
        self.__balance = balance

    # Métodos get
    def get_numero_cuenta(self):
        return self.__numero_cuenta

    def get_tasa_interes(self):
        return self.__tasa_interes

    def get_balance(self):
        return self.__balance


# La cuenta de CD representa una cuenta de certificado de depósito (CD).
# Es una subclase de la clase CuentaAhorro.

class CD(CuentaAhorro):
    # El método init acepta argumentos para el número de cuenta,
    # tasa de interés, deposito y fecha de vencimiento.
    def __init__(self, numero_cuenta, tasa_interes, balance, fecha_vencimiento):
        # Llamar al método __init__ de la superclase
        CuentaAhorro.__init__(self, numero_cuenta, tasa_interes, balance)
        # Inicializar el atributo fecha_vencimiento
        self.__fecha_vencimiento = fecha_vencimiento

    # Métodos set y get de fecha_vencimiento
    def set_fecha_vencimiento(self, fecha_vencimiento):
        self.__fecha_vencimiento = fecha_vencimiento

    def get_fecha_vencimiento(self):
        return self.__fecha_vencimiento
