import os
os.system("clear")

contador = 1
veces_si = 0
while contador <= 3:
    respuesta = input("¿Te gusta el helado de limón? (S/N): ")
    if respuesta == "S" or respuesta == "s":
        veces_si = veces_si + 1
    
    contador = contador + 1
    
print(f"{veces_si} personas eligieron helado de limón")