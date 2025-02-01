archivo = open("docentes.txt", "r")
print()
print("{:>40}|{:>50}".format("Docente", "Asignatura"))
print("-" * 91)
for docente in archivo.readlines():
    nombre, asignatura = docente.split(", ")
    print(f"{nombre:>40}|{asignatura:>50}", end="")
    
archivo.close()
print()
print()
