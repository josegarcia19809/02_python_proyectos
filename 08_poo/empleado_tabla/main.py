from empleado import Empleado

print("-" * 100)
def main():
    empleado1 = Empleado("Susan Meyers", 47899, "contabilidad", "Vicepresidente")
    empleado2 = Empleado("Mark Jones", 39119, "TI", "Programador")
    empleado3 = Empleado("Joy Rogers", 81774, "fabricación", "Ingeniero")

    print()
    print(f"{'Nombre':<20}{'id':>7}{'Departamento':>15}{'Puesto':>20}")
    print("-" * 65)
    print(empleado1)
    print(empleado2)
    print(empleado3)
    print()


if __name__ == "__main__":
    main()
