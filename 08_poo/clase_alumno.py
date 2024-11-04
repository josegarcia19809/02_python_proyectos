class Alumno:
    # Constructor
    def __init__(self, nombre, carrera):
        self.nombre = nombre
        self.carrera = carrera

    def obtener_datos(self):
        return f"Nombre: {self.nombre}, carrera: {self.carrera}"

    # Crear una instancia


alumno1 = Alumno("José García", "Ing. en Computación")
print(alumno1.obtener_datos())

# Crear otra instancia
alumno2 = Alumno("Rox Sánchez", "Lic. en Psicología")
print(alumno2.obtener_datos())

# Agregar otros 2 alumnos hombres
# y 2 alumnas
