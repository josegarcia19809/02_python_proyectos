# raiz_cuadrada.py

import math
print("Programa para sacar la raíz de un número")
numero = float(input("Dame un número: "))
if numero >= 0: 
    raiz= math.sqrt(numero)
    print(f"La raiz es:{raiz}")
else:
    print(f"No es un numero positivo")
    
"""Pedir un número
Si ese número es mayor o igual a cero entonces
    Sacar raíz cuadrada(número)
    Imprimir raíz 
De lo contrario
    imprimir "No es un numero positivo"
"""