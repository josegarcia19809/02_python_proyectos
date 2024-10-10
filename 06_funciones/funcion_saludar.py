# Este programa crea una función saludar que recibe un argumento,
# después manda imprimir un mensaje en pantalla.

def saludar(nombre: str):
    print(f"Hola amigo(a): {nombre}")


def main():
    saludar("José")
    saludar("Luis")
    saludar("Rosa")
    saludar("Fabiola")
    nombre_amigo = "Ana"  # Primero se crea la variable
    saludar(nombre_amigo)  # Se manda la variable a la función


main()
