# intento_cambio_parametro.py
# Este programa demuestra qué pasa cuando cambias el valor de un parámetro

def cambiar_parametro(argumento):
    print("Estoy cambiando el valor")
    argumento = 0
    print(f"Ahora el nuevo valor es {argumento}")


def main():
    valor = 99
    print(f"El valor es {valor}")
    cambiar_parametro(valor)
    print(f"De vuelta a main. El valor es {valor}")


main()
