def contar_letras(frase):
    # Inicializamos un diccionario para contar las ocurrencias de cada letra
    contador_letras = {}

    # Recorremos cada caracter en la frase
    for caracter in frase:
        # Ignoramos los caracteres que no son letras
        if caracter.isalpha():
            # Convertimos el caracter a minúsculas para evitar diferencias entre mayúsculas y minúsculas
            letra = caracter.lower()
            # Si la letra ya está en el diccionario, incrementamos su contador
            if letra in contador_letras:
                contador_letras[letra] += 1
            # Si no está, la inicializamos con 1
            else:
                contador_letras[letra] = 1

    return contador_letras

def imprimir_tabla(contador_letras):
    print("Tabla de ocurrencias de letras:")
    for letra in sorted(contador_letras):
        print(f"{letra}: {contador_letras[letra]}")

def main():
    frase = input("Ingrese una frase: ")
    contador_letras = contar_letras(frase)
    imprimir_tabla(contador_letras)

if __name__ == "__main__":
    main()