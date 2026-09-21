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





# EJERCICIO 20.1


# Clase ControlAlmacen que:
# (1) tenga método ingresar_producto(producto, cantidad)
# que guarde o aumente la cantidad en un diccionario;
# (2) tenga método retirar_producto(producto, cantidad)
# que disminuya la cantidad y retorne True si hay suficiente stock;
# (3) tenga método productos_bajo_stock(minimo)
# que retorne una lista de productos cuya cantidad sea menor al mínimo;
# (4) tenga método producto_mayor_stock()
# que retorne el producto que tenga la mayor cantidad disponible.



class ControlAlmacen:

    def __init__(self):
        self.productos = {}

    def ingresar_producto(self, producto, cantidad):
        if producto in self.productos:
            self.productos[producto] += cantidad
        else:
            self.productos[producto] = cantidad

    def retirar_producto(self, producto, cantidad):
        if producto in self.productos and self.productos[producto] >= cantidad:
            self.productos[producto] -= cantidad
            return True
        else:
            return False

    def productos_bajo_stock(self, minimo):
        productos = []

        for producto, cantidad in self.productos.items():
            if cantidad < minimo:
                productos.append(producto)

        return productos

    def producto_mayor_stock(self):
        if len(self.productos) == 0:
            return None

        producto = max(self.productos, key=self.productos.get)
        return producto


almacen = ControlAlmacen()


almacen.ingresar_producto("Laptop", 10)
almacen.ingresar_producto("Mouse", 5)
almacen.ingresar_producto("Teclado", 8)


print("¿Se pudo retirar?", almacen.retirar_producto("Mouse", 2))


print("Productos con bajo stock:",
      almacen.productos_bajo_stock(5))


print("Producto con mayor stock:",
      almacen.producto_mayor_stock())

