import hashlib


def calcular_sha256(dato):
    # Convert dato to bytes if it’s not already
    if isinstance(dato, str):
        dato = dato.encode()

    # Calcular SHA-256 hash
    sha256_hash = hashlib.sha256(dato).hexdigest()

    return sha256_hash


# Example usage:
entrada = "amor"
valor_hash = calcular_sha256(entrada)
print("SHA-256 Hash:", valor_hash)
