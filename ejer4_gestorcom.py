# GESTOR DE COMPRAS CON TOTALES 
# Clase CarroCompras que: (1) tenga método agregar_articulo(nombre, precio)
# que guarde en un diccionario {nombre: precio}; (2) tenga método total_carrito() 
# que retorne la suma de todos los precios; 
# (3) tenga método articulos_por_rango(precio_min, precio_max) 
# que retorne una lista con artículos dentro del rango.

class CarroCompras:

    def __init__(self):
        self.articulos = {}

    def agregar_articulo(self, nombre, precio):
        self.articulos[nombre] = precio

    def total_carrito(self):
        return sum(self.articulos.values())

    def articulos_por_rango(self, precio_min, precio_max):
        resultado = []

        for nombre, precio in self.articulos.items():
            if precio >= precio_min and precio <= precio_max:
                resultado.append(nombre)

        return resultado



c = CarroCompras()


c.agregar_articulo("pan", 2.50)
c.agregar_articulo("leche", 3.00)
c.agregar_articulo("arroz", 5.00)
c.agregar_articulo("cafe", 8.00)


print("Total:", c.total_carrito())


print("Artículos en rango:", c.articulos_por_rango(2, 5))




# EJERCICIO#4.1
# GESTOR DE PRODUCTOS

class GestorProductos:

    def __init__(self):
        self.productos = {}

    def agregar_producto(self, nombre, cantidad):
        self.productos[nombre] = cantidad

    def total_productos(self):
        return sum(self.productos.values())

    def productos_por_rango(self, cantidad_min, cantidad_max):
        resultado = []

        for nombre, cantidad in self.productos.items():
            if cantidad >= cantidad_min and cantidad <= cantidad_max:
                resultado.append(nombre)

        return resultado



gestor = GestorProductos()



gestor.agregar_producto("cuadernos", 10)
gestor.agregar_producto("lapices", 25)
gestor.agregar_producto("borradores", 5)
gestor.agregar_producto("marcadores", 15)

print("Productos registrados:", gestor.productos)



print("Total de productos:", gestor.total_productos())


print("Productos en rango de 10 a 20:", gestor.productos_por_rango(10, 20))

