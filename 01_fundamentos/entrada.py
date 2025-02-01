# Created by: Ing. José Luis García Morales on 28 de junio de 2020, 11:14
# Este programa pide datos de diferentes tipos al usuario

# Pedir cadena en 2 instrucciones
print("¿Cómo se llama?")
nombre = input()
# Pedir un entero en una sola instrucción
# Nótese que se tiene que hacer la conversión de cadena a entero usando int()
edad = int(input("Dame tu edad: "))
print(f"Te llamas {nombre} y tu edad es: {edad}")

# Pedir un valor flotante, con decimales
peso = float(input("Dame tu peso: "))
print(f"Tu peso es: {peso}")
