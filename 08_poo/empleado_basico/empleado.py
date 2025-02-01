class Empleado:
    # Constructor
    def __init__(self, nombrex, id, departamentox, puestox):
        self.nombre = nombrex
        self.idNumero = id
        self.departamento = departamentox
        self.puesto = puestox

    def obtener_datos(self) -> str:
        salida = f"{self.nombre:>20}"
        salida += f"{self.idNumero:>7}"
        salida += f"{self.departamento:>15}"
        salida += f"{self.puesto:>20}"
        return salida


empleado1 = Empleado("Susan Meyers", 47899, "contabilidad", "Vicepresidente")
empleado2 = Empleado("Mark Jones", 39119, "TI", "Programador")
empleado3 = Empleado("Joy Rogers", 81774, "fabricación", "Ingeniero")

print()
print(f"{'Nombre':>20}{'id':>7}{'Departamento':>15}{'Puesto':>20}")
print("-" * 70)
print(empleado1.obtener_datos())
print(empleado2.obtener_datos())
print(empleado3.obtener_datos())
print()
