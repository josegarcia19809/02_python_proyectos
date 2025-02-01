# La clase Mamifero representa un mamífero genérico
class Mamifero:
    # El constructor solo acepta la especie a la que pertenece el mamífero
    def __init__(self, especie):
        self.__especie = especie

    # El método mostrar_especie muestra un mensaje indicando la especie
    def mostrar_especie(self):
        print(f"Soy un(a) {self.__especie}")

    # El método hacer_sonido es la forma genérica en la que se muestra el sonido
    # de un mamífero
    def hacer_sonido(self):
        print("Grrrr")


# La clase Perro es una subclase de la clase Mamifero
class Perro(Mamifero):
    # El constructor de Perro inicializa a la especie de su superclase
    def __init__(self):
        Mamifero.__init__(self, "Perro")

    # El método hacer_sonido sobreescribe al método hacer_sonido de su superclase
    def hacer_sonido(self):
        print("Guau, guau")


# La clase Gato es una subclase de la clase Mamifero
class Gato(Mamifero):
    # El constructor de Gato inicializa a la especie de su superclase
    def __init__(self):
        Mamifero.__init__(self, "Gato")

    # El método hacer_sonido sobreescribe al método hacer_sonido de su superclase
    def hacer_sonido(self):
        print("Miau")
