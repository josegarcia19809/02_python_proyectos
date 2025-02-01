# Este programa demuestra 2 funciones que tienen variables locales
# con el mismo nombre.

def main():
    mostrar_aves_texas()
    mostrar_aves_california()


# Definición de la función mostrar_aves_texas.
# La función crea una variable local que se llama aves.
def mostrar_aves_texas():
    aves = 5000
    print(f'Texas tiene {aves} aves.')


# Definición de la función mostrar_aves_california.
# La función también crea una variable local que se llama aves.
def mostrar_aves_california():
    aves = 8000
    print(f'California tiene {aves} aves.')


# Llamar a la función main.
main()
