temperatura = int(input("Dame temperatura: "))

es_temperatura_mayor_que_100 = temperatura > 100

if not es_temperatura_mayor_que_100:
    print("Está por debajo de la temperatura máxima")