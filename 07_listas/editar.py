frutas  = ["manzana", "pera", "mango", "sandía", "melón"]

def mostrar_frutas():
    for index, fruta in enumerate(frutas):
        print(f"{index + 1}: {fruta}") 
    print()
    
mostrar_frutas()

numero = int(input("Dame número de fruta a cambiar: "))
numero = numero - 1

# Pedir el nombre de la fruta
nuevo_nombre = input("Dame nuevo nombre de fruta: ")

frutas[numero] = nuevo_nombre
mostrar_frutas()