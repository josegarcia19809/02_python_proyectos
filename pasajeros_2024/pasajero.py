class Pasajero:
    # Constructor
    def __init__(self, clave: int, nombre: str, origen: str, destino: str,
                 pasaje: float) -> None:
        self.clave: int = clave
        self.nombre: str = nombre
        self.origen: str = origen
        self.destino: str = destino
        self.pasaje: float = pasaje

    def __str__(self) -> str:
        origen_aux: str = self.origen
        if len(self.origen) > 14:
            origen_aux = self.origen[:10] + "..."

        destino_aux: str = self.destino
        if len(self.destino) > 14:
            destino_aux = self.destino[:10] + "..."

        return (f"{self.clave:>7}{self.nombre:>20}{origen_aux:>15}{destino_aux:>15}"
                f"{self.pasaje:>7}")
