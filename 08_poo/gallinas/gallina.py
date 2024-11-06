class Gallina:
    # Constructor
    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie
        self.huevos = 0

    def __str__(self) -> str:
        datos = f"Nombre: {self.nombre}, "
        datos += f"especie: {self.especie}, "
        datos += f"ha puesto {self.huevos} huevos"
        return datos

    def poner_huevo(self):
        self.huevos += 1

    def obtener_cantidad_huevos(self) -> int:
        return self.huevos
