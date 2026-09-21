# MAPEADOR DE EDADES 

#Clase GestorPersonas que: (1) tenga método agregar_persona(nombre, edad)
# que guarde en un diccionario; (2) tenga método personas_mayores(edad_minima) 
# que retorne una lista de nombres cuya edad sea ≥; (3) tenga método edad_promedio()
# que retorne el promedio de edades.

class GestorPersonas:

    def __init__(self):
        self.personas = {}

    def agregar_persona(self, nombre, edad):
        self.personas[nombre] = edad

    def personas_mayores(self, edad_minima):
        mayores = []

        for nombre, edad in self.personas.items():
            if edad >= edad_minima:
                mayores.append(nombre)

        return mayores

    def edad_promedio(self):
        return sum(self.personas.values()) / len(self.personas)


gp = GestorPersonas()


gp.agregar_persona("Ana", 28)
gp.agregar_persona("Bob", 17)
gp.agregar_persona("Carlos", 25)


print(gp.personas_mayores(18))


print("Edad promedio:", gp.edad_promedio())





#EJERCICIO# 8.1
#GESTOR DE PRODUCTOS
# Tenga un método agregar_producto(nombre, precio) que guarde el producto y su precio en un diccionario.
# Tenga un método productos_caros(precio_minimo) que retorne una lista con los nombres de los
# productos cuyo precio sea mayor o igual al precio indicado.
# Tenga un método precio_promedio() que retorne el promedio de todos los precios

class GestorProductos:

    def __init__(self):
        self.productos = {}

    def agregar_producto(self, nombre, precio):
        self.productos[nombre] = precio

    def productos_caros(self, precio_minimo):
        caros = []

        for nombre, precio in self.productos.items():
            if precio >= precio_minimo:
                caros.append(nombre)

        return caros

    def precio_promedio(self):
        return sum(self.productos.values()) / len(self.productos)


gp = GestorProductos()

gp.agregar_producto("Cuaderno", 3)
gp.agregar_producto("Mochila", 25)
gp.agregar_producto("Calculadora", 15)


print(gp.productos_caros(10))

print("Precio promedio:", gp.precio_promedio())