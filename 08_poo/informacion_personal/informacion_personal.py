class InformacionPersonal:
    # Constructor
    def __init__(self, nombre, direccion, edad, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.edad = edad
        self.telefono = telefono

    def __str__(self):
        salida = f"Nombre: {self.nombre}, "
        salida += f"dirección: {self.direccion}, "
        salida += f"edad: {self.edad}, "
        salida += f"número de teléfono: {self.telefono}"
        return salida


persona_1 = InformacionPersonal("José García", "Atlacomulco", 40, "7121203300")
persona_2 = InformacionPersonal("Luis Morales", "Toluca", 24, "7121203301")
persona_3 = InformacionPersonal("Rox Sánchez", "Cd de México", 18, "7121203303")

print(persona_1)
print(persona_2)
print(persona_3)
print("-"*100)
