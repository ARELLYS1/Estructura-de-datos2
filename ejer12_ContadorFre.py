# CONTADOR DE FRECUENCIA 

# Clase ContadorFrecuencia que: (1) tenga método agregar_elemento(elemento) 
# que guarde en un diccionario contando repeticiones; 
# (2) tenga método elemento_mas_frecuente()
# que retorne el elemento con mayor frecuencia; 
# (3) tenga método frecuencia_elemento(elemento)
# que retorne cuántas veces aparece.



class ContadorFrecuencia:

    def __init__(self):
        self.frecuencias = {}

    def agregar_elemento(self, elemento):
        if elemento in self.frecuencias:
            self.frecuencias[elemento] += 1
        else:
            self.frecuencias[elemento] = 1

    def elemento_mas_frecuente(self):
        mayor = None
        cantidad = 0

        for elemento, frecuencia in self.frecuencias.items():
            if frecuencia > cantidad:
                cantidad = frecuencia
                mayor = elemento

        return mayor

    def frecuencia_elemento(self, elemento):
        return self.frecuencias.get(elemento, 0)



cf = ContadorFrecuencia()


cf.agregar_elemento("manzana")
cf.agregar_elemento("pera")
cf.agregar_elemento("manzana")
cf.agregar_elemento("banana")
cf.agregar_elemento("manzana")
cf.agregar_elemento("pera")


print(cf.frecuencias)
print("Más frecuente:", cf.elemento_mas_frecuente())
print("Frecuencia de manzana:", cf.frecuencia_elemento("manzana"))