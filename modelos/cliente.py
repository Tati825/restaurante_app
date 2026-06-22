#Segunda clase, para representar al cliente
class Cliente:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono

    def info_cliente(self):
        print(self)

    def __str__(self):
        return f"Cliente: {self.nombre} | Teléfono: {self.telefono}"
