# MAPEO DE ESTUDIANTES Y NOTAS 

# Clase RegistroNotas que: 
# (1) tenga método registrar(estudiante, nota) que guarde en un diccionario;
# (2) tenga método estudiantes_aprobados(nota_minima) 
# que retorne lista de estudiantes;
# (3) tenga método mejor_estudiante() 
# que retorne nombre y nota del que tiene mayor calificación.


class RegistroNotas:

    def __init__(self):
        self.notas = {}

    def registrar(self, estudiante, nota):
        self.notas[estudiante] = nota

    def estudiantes_aprobados(self, nota_minima):
        aprobados = []

        for estudiante, nota in self.notas.items():
            if nota >= nota_minima:
                aprobados.append(estudiante)

        return aprobados

    def mejor_estudiante(self):
        mejor_nombre = ""
        mejor_nota = 0

        for estudiante, nota in self.notas.items():
            if nota > mejor_nota:
                mejor_nota = nota
                mejor_nombre = estudiante

        return (mejor_nombre, mejor_nota)


rn = RegistroNotas()

rn.registrar("Ana", 95)
rn.registrar("Bob", 70)
rn.registrar("Carlos", 85)

print(rn.estudiantes_aprobados(70))
print(rn.mejor_estudiante())





# EJERCICIO 15.1
# REGISTRO DE PRODUCTOS Y PRECIOS

# Clase RegistroProductos que:
# (1) tenga método registrar(producto, precio)
# que guarde el producto y su precio en un diccionario;
# (2) tenga método productos_baratos(precio_maximo)
# que retorne una lista de productos cuyo precio sea
# menor o igual al precio máximo;
# (3) tenga método producto_mas_caro()
# que retorne el nombre y precio del producto
# que tenga el mayor valor.



# REGISTRO DE PRODUCTOS Y PRECIOS

class RegistroProductos:

    def __init__(self):
        self.productos = {}

    def registrar(self, producto, precio):
        self.productos[producto] = precio

    def productos_baratos(self, precio_maximo):
        baratos = []

        for producto, precio in self.productos.items():
            if precio <= precio_maximo:
                baratos.append(producto)

        return baratos

    def producto_mas_caro(self):
        producto = max(self.productos, key=self.productos.get)
        return producto, self.productos[producto]


# Crear objeto
registro = RegistroProductos()


registro.registrar("Laptop", 800)
registro.registrar("Mouse", 25)
registro.registrar("Teclado", 50)
registro.registrar("Monitor", 300)


print("Productos baratos:", registro.productos_baratos(100))
print("Producto más caro:", registro.producto_mas_caro())


