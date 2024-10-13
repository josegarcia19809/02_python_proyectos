# Este programa demuestra cómo pasar dos cadenas como argumentos por palabra clave
# a una función.

def main():
    # Solicita al usuario su nombre y apellido.
    nombre_usuario = input('Ingresa tu nombre: ')
    apellido_usuario = input('Ingresa tu apellido: ')

    # Muestra el nombre al revés.
    print('Tu nombre al revés es:')
    invertir_nombre(apellido=nombre_usuario, nombre=apellido_usuario)


# La función invertir_nombre imprime el nombre y apellido en orden inverso.
def invertir_nombre(nombre, apellido):
    print(apellido, nombre)


# Llamada a la función principal.
main()
