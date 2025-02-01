# Abrir el archivo
archivo = open ("numeros.txt", "w", encoding="utf-8")
# w: write
# Escribir en el archivo
archivo.write("Lista de números: \n")
for i in range(10):
    archivo.write(f"{i} ")

# Cerrar el archivo
archivo.close()
print("El archivo se ha escrito correctamente")