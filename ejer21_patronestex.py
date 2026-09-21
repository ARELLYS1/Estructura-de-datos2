# ANALIZADOR DE PATRONES EN TEXTOS

# Clase AnalizadorPatrones que:
# (1) tenga método encontrar_palabras(texto, patron)
# que busque palabras que inicien con el patrón y retorne una lista;
# (2) tenga método agrupar_por_longitud(texto)
# que retorne un diccionario {longitud: [palabras]}; 
# (3) tenga método palabras_unicas() usando un conjunto.


class AnalizadorPatrones:

    def __init__(self):
        self.palabras = set()

    def encontrar_palabras(self, texto, patron):
        resultado = []

        palabras = texto.split()

        for palabra in palabras:
            if palabra.startswith(patron):
                resultado.append(palabra)

        return resultado

    def agrupar_por_longitud(self, texto):
        grupos = {}

        palabras = texto.split()

        for palabra in palabras:
            longitud = len(palabra)

            if longitud not in grupos:
                grupos[longitud] = []

            grupos[longitud].append(palabra)

        return grupos

    def palabras_unicas(self):
        return self.palabras


ap = AnalizadorPatrones()

print(ap.encontrar_palabras("el gato está aquí", "ga"))

print(ap.agrupar_por_longitud("el gato está aquí"))

ap.palabras.add("gato")
ap.palabras.add("el")
ap.palabras.add("gato")

print(ap.palabras_unicas())





# EJERCICIO 21.1

# Clase AnalizadorPalabras que:
# (1) tenga método encontrar_palabras(texto, letra)
# que busque palabras que contengan la letra indicada
# y retorne una lista;
# (2) tenga método agrupar_por_longitud(texto)
# que retorne un diccionario {longitud: [palabras]};
# (3) tenga método palabras_unicas(texto)
# que retorne las palabras sin repetirse usando un conjunto;
# (4) tenga método palabra_mas_larga(texto)
# que retorne la palabra con mayor longitud.

# ANALIZADOR DE PALABRAS

class AnalizadorPalabras:

    def encontrar_palabras(self, texto, letra):
        palabras = texto.split()
        resultado = []

        for palabra in palabras:
            if letra.lower() in palabra.lower():
                resultado.append(palabra)

        return resultado

    def agrupar_por_longitud(self, texto):
        palabras = texto.split()
        resultado = {}

        for palabra in palabras:
            longitud = len(palabra)

            if longitud not in resultado:
                resultado[longitud] = []

            resultado[longitud].append(palabra)

        return resultado

    def palabras_unicas(self, texto):
        palabras = texto.split()
        return set(palabras)

    def palabra_mas_larga(self, texto):
        palabras = texto.split()

        if len(palabras) == 0:
            return None

        return max(palabras, key=len)


analizador = AnalizadorPalabras()

texto = "python es un lenguaje poderoso y python es divertido"

print("Palabras que contienen 'o':")
print(analizador.encontrar_palabras(texto, "o"))


print("\nPalabras agrupadas por longitud:")
print(analizador.agrupar_por_longitud(texto))


print("\nPalabras únicas:")
print(analizador.palabras_unicas(texto))


print("\nPalabra más larga:")
print(analizador.palabra_mas_larga(texto))

