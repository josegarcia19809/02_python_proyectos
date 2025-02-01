# division.py
print("-" * 100)
# Programa para dividir un número entre otro.
# Si el segundo es cero mandará un mensaje de error
num1 = float(input("Dame un número: "))
num2 = float(input("Dame otro número: "))

# Determinar si puede ocurrir una división entre cero
if num2 == 0:
    # Error--- División entre cero
    print("No existe la división entre cero")
    print("Por favor, ejecute el programa nuevamente")
    print("Y escriba un número diferente de cero")

else:
    # Realizar la división y mostrar el resultado
    resultado = num1 / num2
    print(f"El resultado es {resultado:,.1f}")

# 10/5 => 2
# 10/0 => No existe la división entre cero
