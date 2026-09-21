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