"""
Crear un archivo que se llame amigos.txt
usando la opción "w"
Juan
Pedro
Ana
Antonia
Ami
"""

archivo = open ("amigos.txt", "w", encoding="utf-8")
archivo.write("Juan\n")
archivo.write("Pedro\n")
archivo.write("Ana\n")
archivo.write("Antonia\n")
archivo.write("Ami\n")
archivo.close()
print("El archivo se ha escrito correctamente")