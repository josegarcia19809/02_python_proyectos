for horas in range(24):
    for minutos in range(60):
        for segundos in range(60):
            segundos = str(segundos).rjust(2, '0')
            minutos = str(minutos).rjust(2, '0')
            horas = str(horas).rjust(2, '0')
            print(f"{horas}:{minutos}:{segundos}")
