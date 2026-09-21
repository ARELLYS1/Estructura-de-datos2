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




# ejercicio 12.1
# Clase AnalizadorNumeros que:
# (1) tenga método agregar_numero(numero)
# que guarde en un diccionario contando cuántas veces se repite cada número;
# (2) tenga método numero_mas_repetido()
# que retorne el número con mayor frecuencia;
# (3) tenga método frecuencia_numero(numero)
# que retorne cuántas veces aparece el número;
# (4) tenga método mostrar_numeros()
# que retorne el diccionario con todos los números y sus frecuencias.


# ANALIZADOR DE NÚMEROS

class AnalizadorNumeros:

    def __init__(self):
        self.numeros = {}

    def agregar_numero(self, numero):
        if numero in self.numeros:
            self.numeros[numero] += 1
        else:
            self.numeros[numero] = 1

    def numero_mas_repetido(self):
        return max(self.numeros, key=self.numeros.get)

    def frecuencia_numero(self, numero):
        return self.numeros.get(numero, 0)

    def mostrar_numeros(self):
        return self.numeros


# Crear objeto
analizador = AnalizadorNumeros()

# Agregar números
analizador.agregar_numero(5)
analizador.agregar_numero(3)
analizador.agregar_numero(5)
analizador.agregar_numero(8)
analizador.agregar_numero(5)
analizador.agregar_numero(3)

# Mostrar resultados
print("Número más repetido:", analizador.numero_mas_repetido())
print("Frecuencia del número 5:", analizador.frecuencia_numero(5))
print("Todos los números:", analizador.mostrar_numeros())

