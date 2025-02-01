class FacturaMensual:
    # Constructor
    def __init__(self, paquete, minutos):
        self.__paquete = paquete
        self.__minutos = minutos

    def cargos_totales(self):
        pago = 0.0
        if self.__paquete == 1:
            pago = 40.00
            if self.__minutos > 10:
                minutos_adicionales = self.__minutos - 10
                pago += minutos_adicionales * 0.50
        elif self.__paquete == 2:
            pago = 60.00
            if self.__minutos > 20:
                minutos_adicionales = self.__minutos - 20
                pago += minutos_adicionales * 0.40
        elif self.__paquete == 3:
            pago = 70.00
            if self.__minutos > 30:
                minutos_adicionales = self.__minutos - 30
                pago += minutos_adicionales * 0.30
        return pago
