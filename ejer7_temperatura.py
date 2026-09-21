# ESTADISTICAS DE TEMPERATURA

# Clase GestorTemperatura que: (1) tenga método registrar_temperatura(temp) 
# que guarde en una lista; (2) tenga método minima()`, `maxima()`, `promedio() que calculen estadísticas; 
# (3) tenga método registrar_multiples(*temps) 
# que reutilice el registro para varias temperaturas.

class GestorTemperatura:

    def __init__(self):
        self.temperaturas = []

    def registrar_temperatura(self, temp):
        self.temperaturas.append(temp)

    def minima(self):
        return min(self.temperaturas)

    def maxima(self):
        return max(self.temperaturas)

    def promedio(self):
        return sum(self.temperaturas) / len(self.temperaturas)

    def registrar_multiples(self, *temps):
        for temp in temps:
            self.registrar_temperatura(temp)



gt = GestorTemperatura()


gt.registrar_multiples(20, 25, 18, 30)


print("Temperatura mínima:", gt.minima())
print("Temperatura máxima:", gt.maxima())
print("Promedio:", gt.promedio())





#EJERCICIO#7.1
#GESTOR DE PRECIOS
# Crear una clase GestorPrecios.
# registrar_precio(precio) guarda los precios en una lista.
# menor() devuelve el precio más bajo.
# mayor() devuelve el precio más alto.
# promedio() calcula el precio promedio.
# registrar_multiples(*precios) permite registrar varios precios reutilizando registrar_precio().

class GestorPrecios:

    def __init__(self):
        self.precios = []

    def registrar_precio(self, precio):
        self.precios.append(precio)

    def menor(self):
        return min(self.precios)

    def mayor(self):
        return max(self.precios)

    def promedio(self):
        return sum(self.precios) / len(self.precios)

    def registrar_multiples(self, *precios):
        for precio in precios:
            self.registrar_precio(precio)


gp = GestorPrecios()

gp.registrar_multiples(10, 25, 15, 30)

print("Precio menor:", gp.menor())
print("Precio mayor:", gp.mayor())
print("Promedio:", gp.promedio())

