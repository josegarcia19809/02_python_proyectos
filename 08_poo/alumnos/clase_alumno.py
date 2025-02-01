
class Alumno:
    # Constructor
    def __init__(self, nombre, carrera) -> None:
        self.nombre = nombre
        self.carrera = carrera

    def obtener_datos(self):
        return f"Nombre: {self.nombre}, carrera: {self.carrera}"


alumno1 = Alumno("José García", "Ing. en Computación")
print(alumno1.obtener_datos())

alumno2 = Alumno("María Sánchez", "Licenciatura en Informática")
print(alumno2.obtener_datos())

