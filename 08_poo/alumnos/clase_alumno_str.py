# clase_alumno_str.py
import os
os.system("cls")
class Alumno:
    # Constructor
    def __init__(self, nombre, carrera) -> None:
        self.nombre = nombre
        self.carrera = carrera

    def __str__(self) -> str:
        datos = f"Nombre: {self.nombre}, "
        datos += f"Carrera: {self.carrera}"
        return datos
    
alumno1 = Alumno("José García",
                 "Ing. en Computación")
alumno2 = Alumno("María Sánchez",
                 "Licenciatura en Informática")
print("-"*70)
print(alumno1)
print(alumno2)
print("-"*70)

