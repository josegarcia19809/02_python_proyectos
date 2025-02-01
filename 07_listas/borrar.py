frutas  = ["manzana", "pera", "mango", "sandía", "melón"]

def mostrar_frutas():
    for index, fruta in enumerate(frutas):
        print(f"{index + 1}: {fruta}") 
    print()
    
mostrar_frutas()

# Pedir al usuario el número de fruta a eliminar
numero = int(input("Dame número de fruta a eliminar: "))
numero = numero - 1

# Eliminar la fruta con ese número
frutas.pop(numero)

# Mostrar las frutas restantes
mostrar_frutas()