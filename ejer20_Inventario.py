# INVENTARIO DE PRODUCTOS

# Clase Inventario que: 
# (1) tenga método agregar_stock(producto, cantidad) 
# que guarde en un diccionario;
# (2) tenga método restar_stock(producto, cantidad) 
# que disminuya y retorne True si hay suficiente; 
# (3) tenga método productos_bajo_stock(minimo) 
# que retorne una lista de productos con cantidad < minimo.


class Inventario:

    def __init__(self):
        self.productos = {}

    def agregar_stock(self, producto, cantidad):
        if producto in self.productos:
            self.productos[producto] += cantidad
        else:
            self.productos[producto] = cantidad

    def restar_stock(self, producto, cantidad):
        if producto in self.productos:
            if self.productos[producto] >= cantidad:
                self.productos[producto] -= cantidad
                return True

        return False

    def productos_bajo_stock(self, minimo):
        resultado = []

        for producto in self.productos:
            if self.productos[producto] < minimo:
                resultado.append(producto)

        return resultado



inv = Inventario()

inv.agregar_stock("Arroz", 10)
inv.agregar_stock("Leche", 3)
inv.agregar_stock("Pan", 7)

print(inv.productos)

print(inv.restar_stock("Arroz", 4))

print(inv.productos)

print(inv.productos_bajo_stock(5))