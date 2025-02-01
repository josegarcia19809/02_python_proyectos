print("-" * 100)
from animales import Mamifero, Perro, Gato

mamifero = Mamifero("Mamifero normal")
mamifero.mostrar_especie()
mamifero.hacer_sonido()
print()

firulais = Perro()
firulais.mostrar_especie()
firulais.hacer_sonido()
print()

mixi = Gato()
mixi.mostrar_especie()
mixi.hacer_sonido()
