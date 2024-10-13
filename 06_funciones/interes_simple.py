# Este programa demuestra el uso de argumentos por palabra clave.
# interes_simple.py
def main():
    # Muestra la cantidad de interés simple, usando 0.01 como tasa de interés por
    # período, 10 como el número de períodos, y $10,000 como el principal.
    mostrar_interes(tasa=0.01,
                    periodos=10,
                    principal=10000.0)
    mostrar_interes(10000.0, tasa=0.01, periodos=10)

    # Esto causará un ERROR!
    # mostrar_interes(1000.0, rate=0.01, 10)


# La función mostrar_interes muestra la cantidad de interés simple para un principal
# dado, tasa de interés por período y número de períodos.
def mostrar_interes(principal, tasa, periodos):
    interes = principal * tasa * periodos
    print(f'El interés simple será de ${interes:,.2f}.')


main()
