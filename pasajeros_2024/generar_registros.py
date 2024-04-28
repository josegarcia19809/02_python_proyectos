import random
import os

# Lista expandida de nombres
nombres = ["Juan", "Ana", "Pedro", "Luisa", "Miguel", "Sofía", "Carlos", "Laura", "Diego", "Elena",
           "Francisco", "Valeria", "Javier", "María", "Andrés", "Isabel", "José", "Lucía", "Ricardo", "Carmen",
           "Fernando", "Paula", "Alberto", "Cristina", "Roberto", "Claudia", "Pablo", "Martina", "Jorge", "Lorena"]

origenes = ["París", "México", "Nueva York", "Tokio", "Londres", "Roma", "Madrid", "Berlín", "Pekín", "Sídney"]
destinos = ["Roma", "Los Ángeles", "Sídney", "Londres", "Pekín", "Berlín", "Madrid", "París", "México", "Nueva York"]

registros = []
claves_generadas = set()
nombres_generados = set()

while len(registros) < 30:
    clave = random.randint(1, 100)
    if clave in claves_generadas:
        continue
    
    nombre = random.choice(nombres)
    if nombre in nombres_generados:
        continue
    
    origen = random.choice(origenes)
    destino = random.choice(destinos)
    pasaje = round(random.uniform(100, 500), 2)
    
    registro = f"{clave}|{nombre}|{origen}|{destino}|{pasaje}"
    registros.append(registro)
    claves_generadas.add(clave)
    nombres_generados.add(nombre)

for registro in registros:
    print(registro)
