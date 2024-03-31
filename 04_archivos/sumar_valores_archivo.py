
suma: float = 0.0

nombre_archivo = "numeros.txt"
archivo = open(nombre_archivo, "r")
for linea in archivo.readlines():
    if linea[-1] == '\n':
        linea = linea[:-1]
    numero: float = float(linea)
    suma += numero

archivo.close()

print(suma)
