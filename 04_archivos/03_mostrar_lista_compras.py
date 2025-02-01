archivo = open("lista_compras.txt", "r")

for linea in archivo.readlines():
    print(linea.upper(), end="")
    
archivo.close()