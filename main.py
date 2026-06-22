#Se traen las clases al menú principal
from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

#Se crea el restaurante
restaurante = Restaurante("Prueba de Concepto")

#Se crea productos del restaurante
producto1 = Producto("Plato #1", 3.99, "Comida")
producto2 = Producto("Plato #2", 5.99, "Comida")
producto3 = Producto("Bebida #1", 3.50, "Bebida")

#Se crean clientes
cliente1 = Cliente("Cliente Prueba A", "0912345678")
cliente2 = Cliente("Cliente Prueba B", "0987654321")

#Se agregan los productos creados
restaurante.añadir_producto(producto1)
restaurante.añadir_producto(producto2)
restaurante.añadir_producto(producto3)

#Se agregan los clientes
restaurante.añadir_cliente(cliente1)
restaurante.añadir_cliente(cliente2)

#Se presenta toda la información en general
restaurante.mostrar_resumen()
