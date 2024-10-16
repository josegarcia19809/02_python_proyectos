# funcion_devolver_saludo.py


def devolver_saludo() -> str:
    return "Buenos días"


def main():
    # Lo que devuelve la función se guarda
    # en la variable saludo
    saludo = devolver_saludo()
    print(saludo)
    # Lo que devuelve la función se manda
    # imprimir en pantalla
    print(devolver_saludo())


main()
