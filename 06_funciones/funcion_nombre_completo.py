# funcion_nombre_completo.py

# Debe llevar 2 funciones: main, mostrar_nombre_completo
# la función mostrar_nombre_completo debe recibir 3 valores de tipo string que guarde
# una variable para nombre, otra para apellido paterno y otra para apellido materno.
# Debe mostrar el nombre completo empezando por los apellidos y separando el nombre
# por una coma
# ("José Luis", "García", "Morales") => "García Morales, José Luis"

def mostrar_nombre_completo(nombre: str, apellido_paterno: str, apellido_materno: str):
    print(f"{apellido_paterno} {apellido_materno}, {nombre} ")


def main():
    mostrar_nombre_completo("José Luis", "García", "Morales")
    mostrar_nombre_completo("Mariana", "García", "Monroy")


main()
