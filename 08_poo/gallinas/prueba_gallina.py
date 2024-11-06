import os

os.system("clear")
from gallina import Gallina


def main():
    gallina_1 = Gallina("Lola", "Leghorn")
    print(gallina_1)
    gallina_1.poner_huevo()
    gallina_1.poner_huevo()
    print(f"Ha puesto {gallina_1.obtener_cantidad_huevos()} huevos")
    print(gallina_1)
    #################################
    gallina_2 = Gallina("Turuleca", "Isa Brown")
    for i in range(5):
        gallina_2.poner_huevo()
    print(gallina_2)


if __name__ == "__main__":
    main()
