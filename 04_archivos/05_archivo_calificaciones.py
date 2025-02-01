"""
Crear el archivo calificaciones.txt
Mediante código escribir 5 alumnos y sus calificaciones en el siguiente formato:
"nombre\tcalificacion"
Por ejemplo: 
José    99
"""

archivo = open ("calificaciones.txt", "w", encoding="utf-8")
archivo.write("Juan\t90\n")
archivo.write("Pedro\t80\n")
archivo.write("Ana\t80\n")
archivo.write("Antonia\t70\n")
archivo.write("Ami\t80\n")
archivo.close()
print("El archivo se ha escrito correctamente")