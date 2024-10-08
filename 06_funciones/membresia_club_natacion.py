# membresia_club_natacion.py
# Escribe un programa que tenga funciones para mostrar la siguiente información:
# Nombre del miembro: mostrar_nombre()
# Tarifas de membresía: mostrar_tarifas()
# Fecha de registro: ver_fecha_registro()
# Fecha de vencimiento: ver_fecha_vencimiento()


def imprimir_linea():
    print("-" * 100)


def mostrar_nombre():
    print("José L. García")
    imprimir_linea()


def mostrar_tarifas():
    print("Tarifas")
    print("Niños: $300.00")
    print("Jóvenes: $600.00")
    print("Adultos: $800.00")
    imprimir_linea()


def ver_fecha_registro():
    print("Fecha de registro: 25/09/2020")
    imprimir_linea()


def ver_fecha_vencimiento():
    print("Fecha de vencimiento: 07/10/2024")
    imprimir_linea()


def main():
    print("Membresía club de natación")
    print("Bienvenido")
    mostrar_nombre()
    mostrar_tarifas()
    ver_fecha_registro()
    ver_fecha_vencimiento()


main()
