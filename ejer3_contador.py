# CONTADOR DE PALABRAS UNICAS 
# Clase AnalizadorTexto que: (1) tenga método agregar_palabra(palabra)
# que agregue la palabra a un conjunto (para evitar duplicados) 
# y a una lista (para el orden); (2) tenga método contar_palabras() 
# que retorne cuántas palabras únicas hay; (3) tenga método agregar_multiples(*args)
# que reutilice agregar_palabra para varios.

class AnalizadorTexto:

    def __init__(self):
        self.conjunto = set()
        self.lista = []

    def agregar_palabra(self, palabra):
        if palabra not in self.conjunto:
            self.conjunto.add(palabra)
            self.lista.append(palabra)

    def contar_palabras(self):
        return len(self.conjunto)

    def agregar_multiples(self, *args):
        for palabra in args:
            self.agregar_palabra(palabra)



analizador = AnalizadorTexto()

analizador.agregar_palabra("hola")
analizador.agregar_palabra("mundo")
analizador.agregar_palabra("hola")


analizador.agregar_multiples("python", "clase", "mundo", "programacion")


print(analizador.lista)


print("Cantidad de palabras únicas:", analizador.contar_palabras())







# EJERCICIO#3.1
# REGISTRO DE NOMBRES

class RegistroNombres:

    def __init__(self):
        self.conjunto = set()
        self.lista = []

    def agregar_nombre(self, nombre):
        if nombre not in self.conjunto:
            self.conjunto.add(nombre)
            self.lista.append(nombre)

    def contar_nombres(self):
        return len(self.conjunto)

    def agregar_multiples(self, *args):
        for nombre in args:
            self.agregar_nombre(nombre)



registro = RegistroNombres()



registro.agregar_nombre("Ana")
registro.agregar_nombre("Pedro")
registro.agregar_nombre("Ana")

print("Nombres después de agregar individualmente:", registro.lista)



registro.agregar_multiples("Luis", "Maria", "Pedro", "Carlos")

print("Nombres después de agregar múltiples:", registro.lista)


print("Cantidad de nombres únicos:", registro.contar_nombres())