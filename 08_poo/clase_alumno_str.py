class Alumno:
    # Constructor
    def __init__(self, nombre, carrera):
        self.nombre = nombre
        self.carrera = carrera

    def __str__(self) -> str:
        return f"Nombre: {self.nombre}, carrera: {self.carrera}"


alumno1 = Alumno("Luis García", "Ing. en Computación")
alumno2 = Alumno("Rox Sánchez", "Lic. en Psicología")
print(alumno1)
print(alumno2)

# Agregar los 4 alumnos del programa anterior
