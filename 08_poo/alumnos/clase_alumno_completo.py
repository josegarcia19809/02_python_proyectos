# clase_alumno.py
import os

os.system("clear")  # cls


class Alumno:
    # Constructor
    def __init__(self, no_cuenta, nombre, asignatura,
                 parcial1, parcial2, estado="Comprobando") -> None:
        self.no_cuenta = no_cuenta
        self.nombre = nombre
        self.asignatura = asignatura
        self.parcial1 = parcial1
        self.parcial2 = parcial2
        self.estado = estado

    def obtener_promedio(self):
        promedio = (self.parcial1 + self.parcial2) / 2
        return promedio

    def obtener_estado(self):
        self.estado = "Extraordinario"
        promedio_alumno = self.obtener_promedio()
        if 6.0 <= promedio_alumno < 8.0:
            self.estado = "Ordinario"
        elif 8.0 <= promedio_alumno <= 10.0:
            self.estado = "Exento"

        return self.estado

    def obtener_datos(self):
        salida = f"Tu cuenta es {self.no_cuenta}, "
        salida += f" te llamas {self.nombre}"
        salida += f", tu asignatura es {self.asignatura}. \n"
        salida += f"Tus calificaciones son: Primer parcial: {self.parcial1},"
        salida += f" Segundo parcial: {self.parcial2}"
        salida += f"; tu promedio es {self.obtener_promedio()},\n"
        salida += f"estás en {self.obtener_estado()}"
        return (salida)


alumno1 = Alumno("20103601", "Juan Perez",
                 "Programación I", 10.0, 1.5)
print(alumno1.obtener_datos())

print("-" * 100)
alumno2 = Alumno("20103602", "María Salazar",
                 "Programación I", 8.0, 8.5)
print(alumno2.obtener_datos())
