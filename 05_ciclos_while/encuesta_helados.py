# encuesta_helados.py

# Se hace una encuesta a tres personas si les gusta o no el helado de limón,
# imprimir a cuántos de ellos les gusta

contador = 1
veces_si = 0

while contador <= 3:
    # upper() convierte las cadenas a mayúsculas
    respuesta = input("¿Te gusta el helado de limón? (S o N): ").upper()
    if respuesta == "S":
        veces_si = veces_si + 1

    contador = contador + 1

print(f"{veces_si} personas eligieron helado de limón")
