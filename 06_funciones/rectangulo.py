def calcular_area_perimetro_rectangulo():
    print("Calcular área y perímetro de un Rectángulo")
    alto = float(input("Proporciona el alto: "))
    ancho = float(input("Proporciona el ancho: "))
    # Calcular
    area = alto * ancho
    perimetro = (alto + ancho) * 2

    print(f"Área: {area}")
    print(f"Perímetro: {perimetro}")


calcular_area_perimetro_rectangulo()
