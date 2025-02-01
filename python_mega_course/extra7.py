print("-" * 100)
frutas = ["manzana", "pera", "mango", "sandía", "melón"]


# Función para imprimir en pantalla los elementos de una lista
def mostrar_frutas():
    global frutas
    for index, fruta in enumerate(frutas):
        print(f"{index + 1}: {fruta}")

    print()


mostrar_frutas()

numero = int(input("Dame número de fruta a cambiar: "))
numero -= 1  # numero = numero - 1
# Pedir el nombre de la fruta
nuevo_nombre = input("Dame nuevo nombre de fruta: ")

# Cambiar la fruta en la posición solicitada
frutas[numero] = nuevo_nombre
mostrar_frutas()
