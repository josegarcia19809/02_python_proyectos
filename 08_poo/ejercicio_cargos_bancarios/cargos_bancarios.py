class CargosBancarios:
    # Constructor
    def __init__(self, saldo, cheques):
        self.__saldo_cuenta = saldo
        self.__cantidad_cheques_emitidos = cheques

    def obtener_cobro_total(self) -> float:
        # cobro por comisión base
        comision_base = 10
        self.__saldo_cuenta = self.__saldo_cuenta - comision_base

        # cobro por cargo adicional
        cargo_adicional = 0
        if self.__saldo_cuenta < 400:
            cargo_adicional = 15
            self.__saldo_cuenta = self.__saldo_cuenta - cargo_adicional

        # cobro por comisión de cheques
        comision_por_cheques = 0
        if self.__cantidad_cheques_emitidos < 20:
            comision_por_cheques = self.__cantidad_cheques_emitidos * 0.10
        elif 20 <= self.__cantidad_cheques_emitidos <= 39:
            comision_por_cheques = self.__cantidad_cheques_emitidos * 0.08
        elif 40 <= self.__cantidad_cheques_emitidos <= 59:
            comision_por_cheques = self.__cantidad_cheques_emitidos * 0.06
        elif self.__cantidad_cheques_emitidos >= 60:
            comision_por_cheques = self.__cantidad_cheques_emitidos * 0.04

        # Saldo final y cobro total
        self.__saldo_cuenta = self.__saldo_cuenta - comision_por_cheques

        # Sumar todos los cobros
        cargo_total = comision_base + cargo_adicional + comision_por_cheques
        return cargo_total

    def obtener_saldo_actual(self) -> float:
        return self.__saldo_cuenta
