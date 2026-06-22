#Primera clase para definir el producto de un restaurante
class Producto:
    def __init__(self, nombre, precio, tamaño):
        self.nombre = nombre
        self.precio = precio
        self.tamaño = tamaño

    def info_producto(self):
        print(self)

    def __str__(self):
        return f"Producto: {self.nombre} | Tamaño: {self.tamaño} | Precio: ${self.precio:.2f}"
