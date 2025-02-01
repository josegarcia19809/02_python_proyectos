from gallina import Gallina

print("-"*100)
def main():
    gallina_1 = Gallina("lola", "Leghorn")
    print(gallina_1)
    gallina_1.poner_huevo()
    print(f"Ha puesto {gallina_1.obtener_cantidad_huevos()}")
    gallina_1.poner_huevo()
    print(f"Ha puesto {gallina_1.obtener_cantidad_huevos()}")
    gallina_1.poner_huevo()
    print(f"Ha puesto {gallina_1.obtener_cantidad_huevos()}")
    gallina_1.poner_huevo()
    print(f"Ha puesto {gallina_1.obtener_cantidad_huevos()}")
    gallina_1.poner_huevo()
    print(f"Ha puesto {gallina_1.obtener_cantidad_huevos()}")
    print(gallina_1)

    gallina_2 = Gallina("daniela", "Isa Brown")
    print(gallina_2)

    gallina_2 = Gallina("rosa", "Lohman")
    print(gallina_2)



if __name__ == "__main__":
    main()
