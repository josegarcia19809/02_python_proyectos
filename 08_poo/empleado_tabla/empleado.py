class Empleado:
    def __init__(self, nombre, identificacion, departamento, puesto) -> None:
        self.nombre = nombre
        self.identificacion = identificacion
        self.departamento = departamento
        self.puesto = puesto

    def __str__(self) -> str:
        datos = f"{self.nombre:<20}"
        datos += f"{self.identificacion:>7}"
        datos += f"{self.departamento:>15}"
        datos += f"{self.puesto:>20}"
        return datos
