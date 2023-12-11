import hashlib


def convertir():
    lista_hash = []
    with open('words502.txt', 'r') as palabras:
        lista_palabras = palabras.read().splitlines()

    for i, elemento in enumerate(lista_palabras, start=1):
        valor_hash = calcular_sha256(elemento)
        print(valor_hash)
        lista_hash.append(valor_hash)


def calcular_sha256(dato):
    # Convert dato to bytes if it’s not already
    if isinstance(dato, str):
        dato = dato.encode()

    # Calcular SHA-256 hash
    sha256_hash = hashlib.sha256(dato).hexdigest()

    return sha256_hash


if __name__ == '__main__':
    convertir()
