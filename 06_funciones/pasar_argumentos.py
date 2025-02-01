# Este programa muestra cómo se pasa un argumento a una función

def main():
    valor = 5
    duplicar_numero(valor)


# La función duplicar_numero acepta un argumento y muestra su valor duplicado
def duplicar_numero(numero):
    resultado = numero * 2
    print(resultado)


main()
duplicar_numero(50)