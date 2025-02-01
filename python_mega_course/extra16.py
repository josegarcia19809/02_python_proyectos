nombres_archivos = ["1. tarea SO.txt", "2. Reporte Redes.pdf", "3. Presentacion.pptx"]

for nombre_archivo in nombres_archivos:
    nuevo_nombre = nombre_archivo.replace(".", "-", 1)
    print(nuevo_nombre)
