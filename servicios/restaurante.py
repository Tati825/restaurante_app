#Primera clase de la carpeta Servicios, para representar a todo el restaurante
class Restaurante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []
        self.clientes = []

    def añadir_producto(self, producto):
        self.productos.append(producto)

    def añadir_cliente(self, cliente):
        self.clientes.append(cliente)

    def mostrar_productos(self):
        print("\nEl Menú")
        for producto in self.productos:
            print(producto)

    def mostrar_clientes(self):
        print("\nLos Clientes Registrados")
        for cliente in self.clientes:
            print(cliente)

    def mostrar_resumen(self):
        print(f"\nRESTAURANTE {self.nombre}")
        self.mostrar_productos()
        self.mostrar_clientes()
