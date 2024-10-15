# funciones_operaciones_basicas.py

# debe llevar 5 funciones: main, sumar, restar, multiplicar, dividir

# La función sumar debe recibir 2 valores float para numero1 y numero2, debe mostrar
# la suma de ambos números. Las demás funciones son semejantes.
# Solamente la función dividir debe llevar una validación, puesto que no
# puede hacer divisiones entre cero.


def sumar(numero1: float, numero2: float):
    suma = numero1 + numero2
    print(f"la suma de {numero1} + {numero2} es: {suma}")


def restar(numero1: float, numero2: float):
    resta = numero1 - numero2
    print(f"la resta de {numero1} - {numero2} es: {resta}")


def multiplicar(numero1: float, numero2: float):
    multiplicacion = numero1 * numero2
    print(f"la multiplicacion de {numero1} * {numero2} es: {multiplicacion}")


def dividir(numero1: float, numero2: float):
    if numero2 == 0:
        print("No se puede hacer la división entre cero")
    else:
        division = numero1 / numero2
        print(f"la division de {numero1} / {numero2} es: {division}")


def main():
    sumar(7, 9)  # Mostrar 16
    sumar(20, 50)  # Mostrar 70
    dividir(100, 20)  # Mostrar 5
    dividir(5, 0)  # Mostrar mensaje de error
    restar(8, 4) # 4
    multiplicar(8, 12) #96


main()
