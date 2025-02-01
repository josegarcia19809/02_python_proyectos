# Definición de la función principal.
def main():
    obtener_nombre()
    print(f'Hola {nombre}.')  # ¡Esto provoca un error!


# Definición de la función obtener_nombre.
def obtener_nombre():
    nombre = input('Ingresa tu nombre: ')


# Llamar a la función principal.
main()


def funcion_erronea():
    valor = 99
    print(f'El valor es {valor}.')
