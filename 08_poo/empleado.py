class Empleado:
    # Constructor
    def __init__(self, nombrex, idx, departamentox, puestox):
        self.nombre = nombrex
        self.identificacion = idx
        self.departamento = departamentox
        self.puesto = puestox

    def obtener_datos(self) -> str:
        salida = f"{self.nombre:>20}"
        salida += f"{self.identificacion:>7}"
        salida += f"{self.departamento:>15}"
        salida += f"{self.puesto:>20}"
        return salida


empleado1 = Empleado("Susan Meyers", 47899, "contabilidad", "vicepresidente")
empleado2 = Empleado("Mark Jones", 39119, "TI", "programador")
empleado3 = Empleado("Joy Rogers", 81774, "fabricación", "Ingeniero")

print()
titulo = f"{'Nombre':>20}"
titulo += f"{'id':>7}"
titulo += f"{'Departamento':>15}"
titulo += f"{'Puesto':>20}"

print(titulo)
print("-" * 70)
print(empleado1.obtener_datos())
print(empleado2.obtener_datos())
print(empleado3.obtener_datos())
