# GESTOR DE TAREAS CON PRIORIDAD 

# Clase Tareas que: (1) tenga método agregar_tarea(descripcion, prioridad)
# que guarde en una lista de tuplas (descripción, prioridad); 
# (2) tenga método tareas_prioritarias() 
# que retorne solo las de prioridad alta;
# (3) tenga método eliminar_completada(descripcion) 
# que borre la tarea de la lista.

class Tareas:

    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, descripcion, prioridad):
        self.tareas.append((descripcion, prioridad))

    def tareas_prioritarias(self):
        prioritarias = []

        for tarea in self.tareas:
            if tarea[1] == "alta":
                prioritarias.append(tarea)

        return prioritarias

    def eliminar_completada(self, descripcion):
        for tarea in self.tareas:
            if tarea[0] == descripcion:
                self.tareas.remove(tarea)
                break


t = Tareas()

t.agregar_tarea("Estudiar", "alta")
t.agregar_tarea("Leer", "baja")
t.agregar_tarea("Programar", "alta")

print(t.tareas_prioritarias())





# 11.1 GESTOR DE INVENTARIO

# Clase "GestorInventario" 

# 1. Tenga un método `agregar_producto(nombre, precio, cantidad)` que guarde los productos en una lista de tuplas `(nombre, precio, cantidad)`.
# 2. Tenga un método `productos_disponibles()` que retorne únicamente los productos cuya cantidad sea mayor que cero.
# 3. Tenga un método `eliminar_producto(nombre)` que elimine de la lista el producto indicado.
# 4. Tenga un método `contar_productos()` que retorne la cantidad total de productos registrados.
# 5. Tenga un método `valor_inventario()` que calcule y retorne el valor total del inventario, multiplicando el precio por la cantidad de cada producto.
# 6. Tenga un método `mostrar_inventario()` que muestre todos los productos registrados junto con su precio y cantidad.



class GestorInventario:

    def __init__(self):
        self.productos = []

    def agregar_producto(self, nombre, precio, cantidad):
        self.productos.append((nombre, precio, cantidad))

    def productos_disponibles(self):
        disponibles = []

        for producto in self.productos:
            if producto[2] > 0:
                disponibles.append(producto)

        return disponibles

    def eliminar_producto(self, nombre):
        for producto in self.productos:
            if producto[0] == nombre:
                self.productos.remove(producto)
                break

    def contar_productos(self):
        return len(self.productos)

    def valor_inventario(self):
        total = 0

        for producto in self.productos:
            total += producto[1] * producto[2]

        return total

    def mostrar_inventario(self):
        for producto in self.productos:
            print(
                "Producto:", producto[0],
                " Precio:", producto[1],
                " Cantidad:", producto[2]
            )



inventario = GestorInventario()

# Agregar productos
inventario.agregar_producto("Laptop", 800, 5)
inventario.agregar_producto("Mouse", 20, 10)
inventario.agregar_producto("Teclado", 35, 0)
inventario.agregar_producto("Monitor", 250, 3)

print("Productos disponibles:")
print(inventario.productos_disponibles())


print("\nCantidad de productos:")
print(inventario.contar_productos())


print("\nInventario:")
inventario.mostrar_inventario()


print("\nValor total del inventario:")
print(inventario.valor_inventario())


inventario.eliminar_producto("Mouse")

print("\nDespués de eliminar Mouse:")
inventario.mostrar_inventario()