# 01_funcion_pedir_datos.py
# Programa que define una función para pedir datos
def pedir_datos():
    print("Encuesta para saber cuántas personas tienen 19 años")
    nombre = input("Dame tu nombre: ")
    edad = int(input("Dame tu edad: "))
    # Se imprimen los datos
    print(f"Tu nombre es {nombre} y tienes {edad} años")


pedir_datos()
