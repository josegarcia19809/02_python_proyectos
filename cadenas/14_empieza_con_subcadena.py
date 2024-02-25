# 14_empieza_con_subcadena.py

# Realizar un programa que comprueba si una cadena leída por teclado comienza por
# una subcadena introducida por teclado.
print("-"*100)
cad = input("Introduce una cadena: ")
subcad = input("Introduce una subcadena: ")
if cad.startswith(subcad):
    print("La cadena comienza con la subcadena")
else:
    print("La cadena NO comienza con la subcadena")
