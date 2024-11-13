# Constante para la tasa de impuesto sobre ventas
TASA_IMPUESTO = 0.05


# Clase CotizacionServicio
class CotizacionServicio:
    def __init__(self, cargos_piezas, cargos_mano_obra):
        self.__cargos_piezas = cargos_piezas
        self.__cargos_mano_obra = cargos_mano_obra

    def set_cargos_piezas(self, cargos_piezas):
        self.__cargos_piezas = cargos_piezas

    def set_cargos_mano_obra(self, cargos_mano_obra):
        self.__cargos_mano_obra = cargos_mano_obra

    def get_cargos_piezas(self):
        return self.__cargos_piezas

    def get_cargos_mano_obra(self):
        return self.__cargos_mano_obra

    def get_impuesto_ventas(self):
        return self.__cargos_piezas * TASA_IMPUESTO

    def get_cargos_totales(self):
        return self.__cargos_piezas + self.__cargos_mano_obra + (
            self.__cargos_piezas * TASA_IMPUESTO)
